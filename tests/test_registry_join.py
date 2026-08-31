"""The registry join is keyed on `oar_name`, and the key is load-bearing.

ERF's ADR 0003 splits one string into two: `name` becomes the body's STATUTORY name, and
`oar_name` keeps the OAR chapter title — "the string OAR-derived joins must match". This
corpus resolves `appropriated_to` strings lifted out of appropriation bills, which spell
agencies the way the rules index does, so `oar_name` is the side of that split this join
belongs on.

The two fields hold identical values in the registry today, which is exactly why this test
cannot simply diff the current registry: on today's data EVERY key works and the test would
pass by construction. So the fixture below is a registry in which the two fields DISAGREE --
the state ERF#168 will actually ship — and the assertions pin which side the join lands on.
Without that disagreement there is nothing here to observe.
"""
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import build_joins                                              # noqa: E402


@pytest.fixture
def split_registry(tmp_path):
    """A registry after ERF#168: `name` is statutory, `oar_name` is the OAR chapter title.

    Carries BOTH `das_agency_number` and `budget_agency_code`, equal, matching ERF's actual
    dual-write today -- these tests are about the oar_name/alias key, not about which of the
    two code fields wins, so an agreeing fixture is correct here (that disagreement is
    `disagreeing_org` below, the one built to observe it).
    """
    p = tmp_path / "agencies.yml"
    p.write_text(yaml.safe_dump({"organizations": [
        # No aliases: nothing but `oar_name` can reach this one, so a test that resolves it
        # is observing the join key and not resolve_agency's spelling variants.
        {"slug": "department-of-forestry",
         "name": "Oregon Department of Forestry",          # statutory
         "oar_name": "Forestry Department, Oregon",        # OAR chapter title
         "das_agency_number": "629", "budget_agency_code": "629"},
        # Aliases live on a SEPARATE body so the alias test cannot be satisfied by the
        # key under test, nor the key test by an alias.
        {"slug": "department-of-revenue",
         "name": "Oregon Department of Revenue",
         "oar_name": "Revenue Department, Oregon",
         "das_agency_number": "150", "budget_agency_code": "150",
         "aliases": ["Revenue Division"]},
    ]}), encoding="utf-8")
    return p


def test_index_is_keyed_on_oar_name(split_registry):
    by_name = build_joins.erf_agencies(split_registry)
    assert "forestry department, oregon" in by_name


def test_bill_spelling_resolves_via_oar_name(split_registry):
    """The join must reach the body through the OAR chapter title."""
    by_name = build_joins.erf_agencies(split_registry)
    hit = build_joins.resolve_agency("Forestry Department, Oregon", by_name)
    assert hit is not None and hit["slug"] == "department-of-forestry"


def test_statutory_name_is_not_the_join_key(split_registry):
    """`name` must NOT silently keep working, or ERF#168 changes what this corpus matches
    with no commit here. It resolves only if someone records it as an alias."""
    by_name = build_joins.erf_agencies(split_registry)
    assert build_joins.resolve_agency("Oregon Department of Forestry", by_name) is None


def test_row_without_oar_name_is_not_oar_joinable(tmp_path):
    """19 registry bodies hold no OAR chapter, so after #168 they may carry no chapter
    title. That is a legitimate registry state: the body is simply not reachable by an
    OAR-derived name. It must not crash the build, and it must still resolve by alias."""
    p = tmp_path / "agencies.yml"
    p.write_text(yaml.safe_dump({"organizations": [
        {"slug": "governors-office", "name": "Office of the Governor",
         "das_agency_number": "100", "aliases": ["Governor's Office"]},
    ]}), encoding="utf-8")
    by_name = build_joins.erf_agencies(p)
    assert build_joins.resolve_agency("Office of the Governor", by_name) is None
    hit = build_joins.resolve_agency("Governor's Office", by_name)
    assert hit is not None and hit["slug"] == "governors-office"


def test_aliases_still_resolve(split_registry):
    """Aliases assert that two names denote the same BODY, so they survive the re-key."""
    by_name = build_joins.erf_agencies(split_registry)
    hit = build_joins.resolve_agency("Revenue Division", by_name)
    assert hit is not None and hit["slug"] == "department-of-revenue"


# --- oregon-budget#37: a present, parsing registry that carries neither key is a refusal,
# not an empty mapping. -----------------------------------------------------------------
#
# A fixture where every entry disagrees with the CURRENT registry on the field that
# matters would pass by construction if it merely repeated `budget_agency_code` under a
# new name. So `stale_registry` below carries NEITHER `das_agency_number` NOR
# `budget_agency_code` -- the actual shape of the checkout the issue measured: it parses,
# every slug resolves, and it is not detectably old by looking at any one field. Only the
# absence of BOTH fields across every organization distinguishes it, so that is what the
# fixture withholds.


@pytest.fixture
def stale_registry(tmp_path):
    """A pre-migration registry: present, parses, resolves nothing this corpus can use.

    Carries `parent_slug`, the schema ERF's ADR 0004 retired, to match the real checkout
    the issue measured -- present only for realism, not read by anything under test.
    """
    p = tmp_path / "agencies.yml"
    p.write_text(yaml.safe_dump({"organizations": [
        {"slug": "department-of-forestry", "name": "Oregon Department of Forestry",
         "oar_name": "Forestry Department, Oregon", "parent_slug": None},
        {"slug": "department-of-revenue", "name": "Oregon Department of Revenue",
         "oar_name": "Revenue Department, Oregon", "parent_slug": None},
    ]}), encoding="utf-8")
    return p


def test_registry_with_neither_key_is_refused_not_emptied(stale_registry):
    """Today's loader would skip both rows for lacking `budget_agency_code` and hand back
    `{}` -- a mapping indistinguishable from 'the registry has no bodies at all', and the
    caller's only signal is that emptiness. A registry that IS present and DOES parse but
    carries neither expected key must refuse loudly, not degrade into that same empty
    shape by accident."""
    with pytest.raises(ValueError):
        build_joins.erf_agencies(stale_registry)


def test_refusal_names_the_file_it_read(stale_registry):
    """The refusal must identify which file was actually opened -- not a generic 'no
    registry found', which reads as though the path were never reached at all."""
    with pytest.raises(ValueError) as exc:
        build_joins.erf_agencies(stale_registry)
    assert str(stale_registry) in str(exc.value)


def test_unresolved_report_refuses_a_stale_registry_rather_than_running(stale_registry,
                                                                         capsys):
    """`--unresolved-report` calls through to the same registry loader as the build path,
    but had its own ad hoc emptiness check rather than the shared refusal -- so a stale
    registry that raises here must still come back as a clean exit 2, not an uncaught
    traceback. Asserting `REFUSED` specifically -- not just exit 2 -- matters: the base
    this replaced also returned 2 with a message on the same input, just the wrong one
    (`SKIPPED`, not `REFUSED`), so exit code alone cannot tell the new behaviour from the
    old."""
    code = build_joins.unresolved_report(stale_registry)
    assert code == 2
    assert "REFUSED" in capsys.readouterr().err


def test_unresolved_report_refusal_names_the_file(stale_registry, capsys):
    build_joins.unresolved_report(stale_registry)
    assert str(stale_registry) in capsys.readouterr().err


def test_the_dead_former_name_candidate_is_gone():
    """oregon-policy-repo was ERF's name before its rename; that checkout was verified
    deleted, but the path itself must not still be listed, or any other checkout -- a
    different machine, a fresh clone of the old branch -- reproduces the exact fallback
    this issue was filed on."""
    assert not any("oregon-policy-repo" in str(p) for p in build_joins.ERF_REGISTRY_CANDIDATES)


def test_registry_carrying_only_das_agency_number_resolves(tmp_path):
    """#49: erf_agencies() now selects on `das_agency_number`, so a registry that has
    already migrated and dropped `budget_agency_code` must resolve normally rather than
    degrade to an empty mapping. (Before #49, filtering on `budget_agency_code` alone
    excluded this org entirely -- this test used to assert `by_name == {}` and document
    that "building the mapping from it is #49's job"; that job is this one.)"""
    p = tmp_path / "agencies.yml"
    p.write_text(yaml.safe_dump({"organizations": [
        {"slug": "department-of-forestry", "name": "Oregon Department of Forestry",
         "oar_name": "Forestry Department, Oregon", "das_agency_number": "629"},
    ]}), encoding="utf-8")
    by_name = build_joins.erf_agencies(p)
    hit = build_joins.resolve_agency("Forestry Department, Oregon", by_name)
    assert hit is not None and hit["slug"] == "department-of-forestry"


def test_load_registry_or_refuse_does_not_call_an_existing_file_absent(tmp_path, capsys):
    """#49: a registry carrying only `budget_agency_code` -- the actual pre-migration shape
    #37's own review measured (80 real orgs, all `budget_agency_code`, zero
    `das_agency_number`) -- exists, parses, and does not trip the `neither key` refusal,
    but `erf_agencies` now filters every row out because it reads `das_agency_number`. The
    resulting empty mapping must not be reported with the message reserved for a registry
    that was never found: the file is right there. This is the exact shape #37's own
    acceptance criteria were filed to kill, now reached from the other field after the
    hard switch, at the caller `erf_agencies` does not control.

    (Before #49 this fixture carried only `das_agency_number`, the mirror image of today's
    shape, because at that point `erf_agencies` still read `budget_agency_code`.)"""
    p = tmp_path / "agencies.yml"
    p.write_text(yaml.safe_dump({"organizations": [
        {"slug": "department-of-forestry", "name": "Oregon Department of Forestry",
         "oar_name": "Forestry Department, Oregon", "budget_agency_code": "629"},
    ]}), encoding="utf-8")
    result = build_joins.load_registry_or_refuse(p)
    assert result is None
    assert "no agency registry at" not in capsys.readouterr().err


def test_main_refuses_a_stale_registry_rather_than_building(stale_registry, monkeypatch,
                                                              capsys):
    """The consolidation's own justification is that `--build` and `--unresolved-report`
    now behave identically; `unresolved_report` was exercised directly above, but nothing
    called `main()` -- the path that actually writes the 474 join documents and the one
    issue #37 is titled after. This is the cheap seam that checks the claim instead of
    assuming it."""
    monkeypatch.setattr(sys, "argv", ["build_joins.py", "--registry", str(stale_registry)])
    code = build_joins.main()
    assert code == 2
    assert "REFUSED" in capsys.readouterr().err


# --- oregon-budget#50: the determinism claim that makes an empty `git diff` over joins/ a
# meaningful thing to require, rather than something that merely happened to be true the day
# someone ran it. ---------------------------------------------------------------------------
#
# `main()` computes `today` once and threads it into every `build()` call, so a signature
# test alone would not show whether the value actually reaches the document -- `build()`
# could read `today` and simply be called with the same value on both runs of a regen and
# the diff would still be empty by coincidence. The only way to observe "unused" is to call
# `build()` directly with two DIFFERENT `today` values and require byte-identical output;
# if `today` ever starts landing in the document (a "generated on <date>" line, say) this is
# the test that would need to start disagreeing with itself to still pass -- PROVIDED the
# fixture actually reaches the branch a real date line would land in. That pins one axis of
# AC3 -- that the `today` parameter itself never reaches the output. It says nothing about
# any OTHER source of non-determinism (an internal clock read, unstable dict/set ordering),
# because two `build()` calls in one test process would share those anyway; that broader
# claim is the double-regen-and-diff run manually and pasted into #50, not this test.
#
# `org["das_agency_number"]` is `107` -- Department of Administrative Services, a REAL DAS
# code, chosen because the committed Parquet mirror carries rows for it in both FY2024 and
# FY2025 (verified: `select agency, fiscal_year, sum(expense) ... where agency = '107'`
# returns a row for each year). That is deliberate, not incidental: a fabricated code with
# no mirror rows sends `build()` down the "no spending at all" branch, which never renders
# the "## Agency spending by fiscal year" table that all 474 committed join documents DO
# carry when they have overlapping fiscal years -- so a date line hidden in that table's
# rendering would go unobserved by this test. `fm`'s biennium and `cw`'s mapping are still
# entirely synthetic (the crosswalk key and slug name a body that doesn't exist in any real
# registry), so this still does not depend on the real ERF registry checkout the other
# fixtures in this file also avoid -- only the bare numeric code needs to line up with the
# mirror, not the identity attached to it.
#
# `con` is a `duckdb.connect()` in-memory database, not a connection "over" the mirror in
# any stored sense -- it reads the committed Parquet files only because `spending()`'s SQL
# globs them by path on every query. With agency `107` that glob genuinely returns rows;
# with the old fabricated `999999` it always returned none, which is what let the fixture's
# blind spot go unnoticed. The connection is closed at the end of the test that uses it.


@pytest.fixture
def synthetic_fm():
    return {
        "id": "appropriations-test-hb0000",
        "citation": "Test HB 0000 (2025)",
        "source_url": "https://example.invalid/test-hb0000",
        "biennium_fiscal_years": [2024, 2025],
        "biennium": "biennium ending June 30, 2025",
        "sibling_corpus": "oregon-legislature",
        "sibling_document_id": "bill-test-hb0000",
    }


@pytest.fixture
def synthetic_org():
    return {"das_agency_number": "107", "slug": "test-agency", "name": "Test Agency"}


@pytest.fixture
def synthetic_cw():
    return {"mapping": {"TEST AGENCY, OR": {"das_agency_number": "107",
                                            "basis": "das_agency_number",
                                            "slug": "test-agency"}}}


@pytest.fixture
def con():
    """A `duckdb.connect()` in-memory database, closed after the test. Not a connection
    "over" the mirror in any stored sense -- it reads the committed Parquet files only
    because spending()'s SQL globs them by path on every query."""
    import duckdb

    c = duckdb.connect()
    yield c
    c.close()


def test_build_output_is_identical_regardless_of_today(synthetic_fm, synthetic_org,
                                                         synthetic_cw, con):
    """The only date `build()` is handed must never reach the document it returns."""
    doc_id_early, text_early = build_joins.build(
        synthetic_fm, synthetic_org, con, "2020-01-01", synthetic_cw)
    doc_id_late, text_late = build_joins.build(
        synthetic_fm, synthetic_org, con, "2099-12-31", synthetic_cw)
    # The fixture must actually exercise the branch every real document with overlapping
    # fiscal years takes, or a date line hidden inside it would go unobserved.
    assert "Agency spending by fiscal year" in text_early
    assert doc_id_early == doc_id_late
    assert text_early == text_late


# --- oregon-budget#49: build_joins.py reads das_agency_number, not budget_agency_code, and
# the field name it emits into the 474 published join documents' agency-identity line moves
# with it. -------------------------------------------------------------------------------
#
# ERF writes both keys and asserts them equal (measured on the real registry: 80
# organizations carry both, zero disagree), so a fixture where the two fields AGREE would
# pass this ticket's tests whichever one `build()` actually reads -- exactly the "passes by
# construction" trap this file's own module docstring warns against, and exactly why the
# ticket itself rejects a `das_agency_number or budget_agency_code` fallback: such a
# fallback would also pass an agreeing fixture, coincidentally. `disagreeing_org` below
# gives one organization a `das_agency_number` that DIFFERS from its `budget_agency_code`,
# so only a genuine, exclusive read of the new field lands on the value these tests assert.


@pytest.fixture
def disagreeing_org():
    """A resolved org record carrying both code fields with DIFFERENT values. build() must
    select `das_agency_number` (629) and never `budget_agency_code` (999999) -- a fallback
    that read the fields in the wrong order would land on 999999 here, which is exactly
    what distinguishes this fixture from one where the two fields merely agree."""
    return {"das_agency_number": "629", "budget_agency_code": "999999",
            "slug": "test-agency-disagree", "name": "Test Agency Disagree"}


@pytest.fixture
def disagreeing_cw():
    """The crosswalk's own mapping is keyed on `das_agency_number` already (unaffected by
    this ticket); it must name the SAME code build() is expected to select, or
    basis_provenance() raises KeyError on a code it cannot find."""
    return {"mapping": {"TEST AGENCY DISAGREE, OR": {
        "das_agency_number": "629", "basis": "das_agency_number",
        "slug": "test-agency-disagree"}}}


def test_build_code_is_das_agency_number_not_budget_agency_code(synthetic_fm, disagreeing_org,
                                                                  disagreeing_cw, con):
    """The hard switch, proved where it actually matters: the `code` that ends up in the
    document id is das_agency_number's value, 629 -- Department of Forestry, a REAL code
    with rows in the committed mirror for both FY2024 and FY2025 (4,293 records/$197.0M and
    4,351 records/$393.9M respectively), so this exercises code selection through the same
    "Agency spending by fiscal year" branch every one of the 474 committed documents takes
    when built, not the empty-mirror branch. Only budget_agency_code's fabricated 999999
    has no mirror rows; a fallback landing on it would both misname the code AND silently
    swap the document onto that empty branch, which `assert "999999" not in text` below
    catches either way."""
    doc_id, text = build_joins.build(synthetic_fm, disagreeing_org, con, "2026-08-27",
                                     disagreeing_cw)
    assert doc_id == "join-test-hb0000-agency-629"
    assert "999999" not in text


def test_build_output_names_das_agency_number_not_budget_agency_code(synthetic_fm,
                                                                      disagreeing_org,
                                                                      disagreeing_cw, con):
    """The agency-identity line every one of the 474 committed join documents carries must
    name the field ERF's registry actually carries going forward -- not the alias ERF#177
    is scheduled to retire, and not both (a stray leftover mention would misdescribe the
    provenance this line records)."""
    _, text = build_joins.build(synthetic_fm, disagreeing_org, con, "2026-08-27",
                                disagreeing_cw)
    assert "das_agency_number: 629" in text
    assert "budget_agency_code" not in text


# --- oregon-budget#53: unresolved_report()'s suggest() reads the registry's raw YAML
# directly, NOT through erf_agencies() -- so #49's hard switch never touched it. This is
# the second and last reader of `budget_agency_code` outside the #37 dual-key detection
# block (erf_agencies() lines 112/116, which intentionally checks both keys). --------------
#
# The two code fields agree on every REAL org today (ERF dual-writes them and asserts
# equality), so a fixture where they merely agree would pass this ticket's test whichever
# field suggest() actually read -- the exact "passes by construction" trap this file's own
# module docstring warns against. `migrated_only_registry` below carries ONLY
# `das_agency_number`, the post-ERF#177 shape: not a differing value but an ABSENT key, so
# a reader still keyed on the retired alias sees nothing there at all. That absence is what
# gives the fixture power to fail the unfixed code and pass only the fix.


@pytest.fixture
def migrated_only_registry(tmp_path):
    """Post-ERF#177: the registry carries `das_agency_number` and no `budget_agency_code`
    at all -- not `erf_agencies()`'s already-covered case (#49), but `unresolved_report()`'s
    own raw-YAML `reg` list, which `suggest()` reads directly."""
    p = tmp_path / "agencies.yml"
    p.write_text(yaml.safe_dump({"organizations": [
        {"slug": "department-of-forestry", "name": "Oregon Department of Forestry",
         "oar_name": "Forestry Department, Oregon", "das_agency_number": "629"},
    ]}), encoding="utf-8")
    return p


@pytest.fixture
def unmatched_bill(tmp_path):
    """One synthetic bill whose `appropriated_to` is the word-order variant
    `resolve_agency` DELIBERATELY refuses to resolve ("State Forestry Department" vs the
    registry's "Forestry Department, Oregon" -- see resolve_agency's own docstring on this
    exact example). It must reach `suggest()`, the codepath under test, rather than
    resolving exactly and never reaching it."""
    bills = tmp_path / "bills"
    bills.mkdir()
    fm = {"id": "appropriations-test-hb0001",
          "appropriated_to": "State Forestry Department",
          "biennium_fiscal_years": [2024, 2025]}
    (bills / "appropriations-test-hb0001.md").write_text(
        "---\n" + yaml.safe_dump(fm) + "---\nbody\n", encoding="utf-8")
    return bills


@pytest.fixture
def report_root(unmatched_bill, monkeypatch, tmp_path):
    """Points `unresolved_report()` at `unmatched_bill` and a scratch `_meta/` it can write
    into, so the two tests below share one setup instead of repeating the same four lines."""
    monkeypatch.setattr(build_joins, "BILLS", unmatched_bill)
    out_root = tmp_path / "out"
    (out_root / "_meta").mkdir(parents=True)
    monkeypatch.setattr(build_joins, "ROOT", out_root)
    return out_root


def test_unresolved_report_variant_reads_das_agency_number_not_budget_agency_code(
        migrated_only_registry, report_root):
    """`suggest()`'s `best.get("budget_agency_code")` truthiness check, and the code column
    it prints, must read `das_agency_number` -- like `erf_agencies()` has since #49 -- or a
    migrated registry (ONLY `das_agency_number`, no `budget_agency_code` at all) sees every
    truthy check on the retired key come back None, and a genuine name-variant match falls
    from "## 2. Probable name variant" into "## 3. ... no `das_agency_number` -- cannot
    join", exactly the misclassification ERF#177 was filed to cause (#53)."""
    code = build_joins.unresolved_report(migrated_only_registry)
    assert code == 0
    text = (report_root / "_meta" / "unresolved-agencies.md").read_text()

    variant_section = text.split("## 2. Probable name variant")[1].split("## 3.")[0]
    nocode_section = text.split("## 3. In the registry")[1].split("## 4.")[0]
    assert "State Forestry Department" in variant_section
    assert "| 629 |" in variant_section
    assert "State Forestry Department" not in nocode_section


def test_unresolved_report_prose_does_not_name_the_retired_alias(
        migrated_only_registry, report_root):
    """The report's own prose (module-level intro, section headings, table headers, and
    the section 3 explanation) must not keep asserting the retired field name once every
    reader is switched."""
    build_joins.unresolved_report(migrated_only_registry)
    text = (report_root / "_meta" / "unresolved-agencies.md").read_text()
    assert "budget_agency_code" not in text
    assert "budget code" not in text

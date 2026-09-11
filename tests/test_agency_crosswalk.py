"""The agency crosswalk: every agency string this corpus records is a DECISION.

The file under test is `_meta/agency-crosswalk.yml` and its validator
`src/link_agency_registry.py`. The seam is that validator's pure functions —
`check()`, `verify_registry()`, `stamp_state()` — which take the corpus's agency
strings and the parsed crosswalk as arguments rather than reading the repo, so a
guard can be watched failing on a two-entry fixture instead of on 1,762 documents.
Two tests deliberately use the REAL committed data: the corpus must actually be
accounted for, and `--check` must actually exit 0 with no sibling present.

WHY THIS FILE EXISTS AT ALL, restated so the tests below are read the right way:
an entry under `unmapped` is a decision with a stated reason, never a blank —
"we looked and there is no counterpart" and "nobody has looked yet" must not be
the same state. Several tests here exist only to keep those two states apart.
"""
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import link_agency_registry as lar                              # noqa: E402


def test_every_expenditure_agency_string_is_accounted_for():
    """AC1. No expenditure agency_name may be in neither block.

    Real committed data: this is the measurement the issue was filed on.
    """
    cw = lar.load_crosswalk()
    names = lar.corpus_names()
    assert names, "no expenditure agency_name strings found — the reader is broken"
    unclassified = sorted(set(names) - set(cw.get("mapping") or {})
                          - set(cw.get("unmapped") or {}))
    assert unclassified == []


# --- the fixture the guards are watched failing on -------------------------------------
# Two mapped agencies and one recorded absence, small enough to read. Every negative test
# below starts from a copy of this and breaks exactly one thing.
def good() -> dict:
    return {
        "mapping": {
            "ENVI QUALITY, DEPT": {"slug": "department-of-environmental-quality",
                                   "das_agency_number": "340", "basis": "das_number"},
            "SECRETARY OF STATE": {"slug": "secretary-of-state",
                                   "das_agency_number": "165", "basis": "exact"},
        },
        "unmapped": {
            "CNTRL AGY": {"basis": "not-reviewed", "checked": "no entry carries 999",
                          "reason": "NOT REVIEWED — nobody has established what it is."},
        },
    }


NAMES = {"ENVI QUALITY, DEPT": 7, "SECRETARY OF STATE": 7, "CNTRL AGY": 1}
STAMPED = [{"id": "join-a", "agency_code": "340",
            "agency_registry_slug": "department-of-environmental-quality",
            "agency_registry_basis": "das_number",
            "agency_registry_basis_key": "ENVI QUALITY, DEPT"}]


def test_check_passes_on_a_consistent_crosswalk():
    assert lar.check(good(), NAMES, {}, STAMPED) == []


def test_check_flags_a_mapped_agency_code_carrying_no_slug_at_all():
    """Coverage gap closed (test-quality review on #42): a LOST stamp — a document whose
    `agency_code` the crosswalk maps but which carries no `agency_registry_slug` at
    all — was previously invisible to `--check`; `stamped_docs()` only ever looks at
    documents that already carry a slug, so nothing looked at this direction.
    Mutation-verified against the real committed tree: deleting the four
    `agency_registry_*` lines from `expenditures-100-fy2019.md` moved `--check` from
    exit 0 to exit 1 (then restored, no working-tree change survives that test)."""
    unslugged = [{"id": "expenditures-340-fy2019", "agency_code": "340"}]
    assert lar.check(good(), NAMES, {}, STAMPED, unslugged=unslugged) == [
        "1 document(s) have an agency_code the crosswalk maps but carry no "
        "agency_registry_slug at all — run "
        "`python3 src/link_agency_registry.py --stamp`: "
        "[\"expenditures-340-fy2019 (das number '340')\"]"
    ]
    # An unslugged document with an agency_code the crosswalk does NOT map is exactly
    # the two `unmapped` strings' expected state — not a defect, so no line for it.
    assert lar.check(good(), NAMES, {}, STAMPED,
                     unslugged=[{"id": "x", "agency_code": "999"}]) == []


def test_check_names_an_expenditure_agency_string_with_no_entry():
    """AC4. Adding an agency to the corpus without classifying it must fail, by name."""
    names = dict(NAMES, **{"SPACE FORCE, DEPT OF": 3})
    problems = lar.check(good(), names, {}, STAMPED)
    assert problems, "an unclassified agency string passed the check"
    assert any("SPACE FORCE, DEPT OF" in p for p in problems), problems


def test_check_names_a_mapping_entry_with_no_basis():
    """AC4. A slug with no basis is a mapping whose warrant nobody recorded."""
    cw = good()
    del cw["mapping"]["ENVI QUALITY, DEPT"]["basis"]
    problems = lar.check(cw, NAMES, {}, STAMPED)
    assert any("ENVI QUALITY, DEPT" in p and "basis" in p for p in problems), problems


def test_check_names_a_mapping_entry_with_no_slug():
    cw = good()
    del cw["mapping"]["ENVI QUALITY, DEPT"]["slug"]
    problems = lar.check(cw, NAMES, {}, STAMPED)
    assert any("ENVI QUALITY, DEPT" in p and "slug" in p for p in problems), problems


def test_check_rejects_a_basis_outside_the_vocabulary():
    """AC2. `basis: probably` is not a warrant; the vocabulary is closed."""
    cw = good()
    cw["mapping"]["ENVI QUALITY, DEPT"]["basis"] = "probably"
    problems = lar.check(cw, NAMES, {}, STAMPED)
    assert any("probably" in p for p in problems), problems


def test_check_requires_a_das_agency_number_on_a_das_number_entry():
    """AC2. `basis: das_number` asserts the number joins them — so it must name it."""
    cw = good()
    del cw["mapping"]["ENVI QUALITY, DEPT"]["das_agency_number"]
    problems = lar.check(cw, NAMES, {}, STAMPED)
    assert any("ENVI QUALITY, DEPT" in p and "das_agency_number" in p
               for p in problems), problems


@pytest.mark.parametrize("field", ["note", "reviewed_by", "reviewed_on"])
def test_check_requires_note_and_reviewer_on_an_alias(field):
    """AC2. An alias asserts an identity the names do not state. It must say why, and
    who accepted it — that is the whole difference between an alias and a guess."""
    cw = good()
    cw["mapping"]["ENVI QUALITY, DEPT"] = {
        "slug": "department-of-environmental-quality", "basis": "alias",
        "note": "same body", "reviewed_by": "@someone", "reviewed_on": "2026-08-22"}
    # No stamped documents here: an alias carries no DAS number, so this fixture has
    # nothing for join-a to resolve through, and that is a different guard's business.
    assert lar.check(cw, NAMES, {}, []) == []            # complete alias is accepted
    del cw["mapping"]["ENVI QUALITY, DEPT"][field]
    problems = lar.check(cw, NAMES, {}, [])
    assert any("ENVI QUALITY, DEPT" in p and field in p for p in problems), problems


@pytest.mark.parametrize("reason", ["", None, "   ", "TODO", "TBD", "n/a", "-", "?"])
def test_check_rejects_an_unmapped_entry_with_no_real_reason(reason):
    """AC3. A blank, a dash or a TODO is not a decision. This is the guard the whole
    file is for: without it, "we looked and there is no counterpart" and "nobody has
    looked yet" collapse back into the same state."""
    cw = good()
    cw["unmapped"]["CNTRL AGY"]["reason"] = reason
    problems = lar.check(cw, NAMES, {}, STAMPED)
    assert any("CNTRL AGY" in p and "reason" in p for p in problems), problems


def test_check_requires_an_unmapped_entry_to_say_what_was_checked():
    """AC3. `checked` records the thing actually tested, kept apart from `reason`, which
    records what was concluded. Merging them is how a prose reason acquires the authority
    of a measurement it never had."""
    cw = good()
    del cw["unmapped"]["CNTRL AGY"]["checked"]
    problems = lar.check(cw, NAMES, {}, STAMPED)
    assert any("CNTRL AGY" in p and "checked" in p for p in problems), problems


def test_check_rejects_an_unmapped_basis_outside_the_vocabulary():
    cw = good()
    cw["unmapped"]["CNTRL AGY"]["basis"] = "probably-fine"
    problems = lar.check(cw, NAMES, {}, STAMPED)
    assert any("probably-fine" in p for p in problems), problems


def test_check_requires_attribution_before_an_absence_may_be_called_reviewed():
    """AC3. `basis: reviewed` is the positive claim "we looked and there is no
    counterpart". Anyone may write that word; the check makes them also say whose reading
    it is — a `source` it was carried from, or a named reviewer and a date."""
    cw = good()
    cw["unmapped"]["CNTRL AGY"]["basis"] = "reviewed"
    problems = lar.check(cw, NAMES, {}, STAMPED)
    assert any("CNTRL AGY" in p and "reviewed" in p for p in problems), problems
    cw["unmapped"]["CNTRL AGY"]["source"] = "_meta/unresolved-agencies.md section 4"
    assert lar.check(cw, NAMES, {}, STAMPED) == []


def test_check_names_an_entry_the_corpus_no_longer_contains():
    """AC4. A crosswalk that outlives its corpus is a decision record about nothing."""
    cw = good()
    cw["unmapped"]["ABOLISHED, DEPT OF"] = {
        "basis": "not-reviewed", "checked": "no registry entry",
        "reason": "NOT REVIEWED — nobody has looked."}
    problems = lar.check(cw, NAMES, {}, STAMPED)
    assert any("ABOLISHED, DEPT OF" in p for p in problems), problems


def test_a_bill_appropriated_to_string_is_permitted_but_not_required():
    """AC1/AC8. Bill documents are out of scope for #23, so a bill string need not be
    classified — but the bodies _meta/unresolved-agencies.md finds no counterpart for are
    recorded here, and must not then be reported as entries matching nothing."""
    cw = good()
    cw["unmapped"]["Emergency Board"] = {
        "basis": "reviewed", "checked": "no registry entry is named Emergency Board",
        "reason": "A contingency fund that disburses through other agencies.",
        "source": "_meta/unresolved-agencies.md section 4"}
    assert lar.check(cw, NAMES, {"Emergency Board": 7}, STAMPED) == []
    # ... and once the bills stop naming it, the entry IS an orphan.
    assert any("Emergency Board" in p for p in lar.check(cw, NAMES, {}, STAMPED))


def test_check_rejects_a_string_that_is_both_mapped_and_unmapped():
    """A name cannot be both resolved and recorded as resolving to nothing."""
    cw = good()
    cw["unmapped"]["SECRETARY OF STATE"] = {
        "basis": "not-reviewed", "checked": "x", "reason": "NOT REVIEWED — placeholder."}
    problems = lar.check(cw, NAMES, {}, STAMPED)
    assert any("SECRETARY OF STATE" in p and "both" in p for p in problems), problems


# --- AC6: the same fact asserted in two places, with something gating the agreement ----
# A join document carries `agency_registry_slug` in its own frontmatter and the crosswalk
# carries it too. Two copies of one fact and no gate between them is how they drift, so
# every guard below is about their AGREEMENT, not about either one alone.

def test_check_names_a_slugged_document_carrying_no_basis():
    """AC6. A document may not claim a registry identity without the warrant for it."""
    stamped = [dict(STAMPED[0])]
    del stamped[0]["agency_registry_basis"]
    problems = lar.check(good(), NAMES, {}, stamped)
    assert any("join-a" in p and "basis" in p for p in problems), problems


def test_check_names_a_document_whose_slug_disagrees_with_the_crosswalk():
    stamped = [dict(STAMPED[0], agency_registry_slug="department-of-revenue")]
    problems = lar.check(good(), NAMES, {}, stamped)
    assert any("join-a" in p and "department-of-revenue" in p for p in problems), problems


def test_check_names_a_document_whose_basis_disagrees_with_the_crosswalk():
    stamped = [dict(STAMPED[0], agency_registry_basis="exact")]
    problems = lar.check(good(), NAMES, {}, stamped)
    assert any("join-a" in p and "exact" in p for p in problems), problems


def test_check_names_a_document_whose_agency_the_crosswalk_does_not_map():
    """A stamped document for an agency the crosswalk does not resolve is a slug with no
    recorded warrant anywhere — the state this file exists to abolish."""
    stamped = [dict(STAMPED[0], agency_code="777")]
    problems = lar.check(good(), NAMES, {}, stamped)
    assert any("join-a" in p and "777" in p for p in problems), problems


def test_check_rejects_two_entries_disagreeing_about_one_das_number():
    """Two spellings of one agency (the feed renamed 845 mid-series) must not resolve to
    two different slugs — the number is the join key, so it must answer once."""
    cw = good()
    cw["mapping"]["ENVIRONMENTAL QUALITY, DEPT OF"] = {
        "slug": "department-of-revenue", "das_agency_number": "340",
        "basis": "das_number"}
    names = dict(NAMES, **{"ENVIRONMENTAL QUALITY, DEPT OF": 2})
    problems = lar.check(cw, names, {}, STAMPED)
    assert any("340" in p for p in problems), problems


# --- AC5: correctness belongs to the registry ------------------------------------------

REG = {"department-of-environmental-quality":
       {"oar_name": "Department of Environmental Quality", "das_agency_number": "340"},
       "secretary-of-state":
       {"oar_name": "Secretary of State", "das_agency_number": "165"}}


# oregon-budget#49's hard switch, extended to this file's own registry reader:
# `registry_index()` fed a `das_agency_number or budget_agency_code` fallback into
# `verify_registry()`, which build_joins.py's own review found and #49 rejected as a
# pattern ("would buy independence the equality check already guarantees, and would then
# need a second change to remove"). An organization where the two fields AGREE would pass
# this either way, so the fixture below carries only `budget_agency_code` -- the shape a
# stale or not-yet-migrated registry, or ERF#177's retirement itself, actually produces --
# to prove the fallback is gone rather than merely untriggered.
def test_registry_index_does_not_fall_back_to_budget_agency_code(tmp_path):
    """An organization carrying only `budget_agency_code` must resolve to no
    das_agency_number here, not silently fall back to the deprecated alias."""
    p = tmp_path / "agencies.yml"
    p.write_text(yaml.safe_dump({"organizations": [
        {"slug": "department-of-forestry", "oar_name": "Forestry Department, Oregon",
         "budget_agency_code": "629"},
    ]}), encoding="utf-8")
    index = lar.registry_index(p)
    assert index["department-of-forestry"]["das_agency_number"] is None


def test_verify_registry_accepts_the_good_fixture():
    assert lar.verify_registry(good(), REG) == []


def test_verify_registry_names_a_slug_the_registry_does_not_carry():
    """AC5. A slug this file invents is a failure, and the registry is the judge."""
    cw = good()
    cw["mapping"]["ENVI QUALITY, DEPT"]["slug"] = "department-of-vibes"
    problems = lar.verify_registry(cw, REG)
    assert any("department-of-vibes" in p for p in problems), problems


def test_verify_registry_names_a_das_number_the_registry_contradicts():
    """The DAS number is the whole warrant for `basis: das_number`. If the registry now
    records a different one, the mapping rests on nothing."""
    cw = good()
    cw["mapping"]["ENVI QUALITY, DEPT"]["das_agency_number"] = "999"
    problems = lar.verify_registry(cw, REG)
    assert any("999" in p and "340" in p for p in problems), problems


def test_verify_registry_names_an_exact_claim_that_no_longer_holds():
    """`basis: exact` is a claim ABOUT the registry's oar_name — ERF's ADR 0003 splits
    `name` (statutory) from `oar_name` (the OAR chapter title), so it is checked against
    the field it is a claim about, and an upstream retitle must surface as a failure
    rather than as a sentence that quietly stopped being true."""
    cw = good()
    reg = dict(REG, **{"secretary-of-state":
                       {"oar_name": "Office of the Secretary of State, Elections Division",
                        "das_agency_number": "165"}})
    problems = lar.verify_registry(cw, reg)
    assert any("SECRETARY OF STATE" in p and "exact" in p for p in problems), problems


def test_verify_registry_exits_2_when_the_sibling_is_absent(tmp_path):
    """AC5. NOT a pass. Reporting "verified" for a comparison that never ran is the
    failure this platform keeps rediscovering."""
    r = subprocess.run([sys.executable, str(ROOT / "src" / "link_agency_registry.py"),
                        "--verify-registry", "--registry", str(tmp_path / "nope.yml")],
                       capture_output=True, text=True)
    assert r.returncode == 2, (r.returncode, r.stdout, r.stderr)
    assert "SKIPPED" in r.stderr and "NOT a pass" in r.stderr, r.stderr


def test_the_check_runs_in_ci():
    """AC7. A gate that exists but is not wired is worse than no gate: it reads as
    covered. AGENTS.md makes this rule explicit — "Add a `--check` CI step for every
    generated file you commit"."""
    ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text()
    assert "src/link_agency_registry.py --check" in ci, \
        "the crosswalk check is not wired into .github/workflows/ci.yml"


def test_the_committed_check_passes_with_no_sibling_present():
    """AC4. CI runs this with no ERF checkout, so it must pass from committed data alone.
    Run as a subprocess with the sibling candidates pointed at an empty directory, which
    is the state a fresh CI runner is in."""
    r = subprocess.run([sys.executable, str(ROOT / "src" / "link_agency_registry.py"),
                        "--check"], capture_output=True, text=True, cwd=ROOT)
    assert r.returncode == 0, r.stderr
    assert "expenditure agency_name string(s)" in r.stdout, r.stdout


# --- AC8: one fact, one voice -----------------------------------------------------------
# _meta/unresolved-agencies.md is GENERATED and marked "do not edit by hand", yet it held
# the only reasons this corpus had for bodies with no registry counterpart. Issue #23 asked
# for that to be decided rather than left to both files. The decision taken: the crosswalk
# is the source of record for those reasons and the report RENDERS them from here. These
# tests hold that line — the report may not name a body the crosswalk has not decided, and
# the reason text a reader sees must be the crosswalk's.

SECTION_4 = """# Unresolved agencies

## 3. In the registry, but no budget code — cannot join

| bill says | appropriations | registry entry (no budget code) |
|---|---:|---|
| Youth Development Division | 2 | `x` |

## 4. No registry counterpart — correctly unresolved

| bill says | appropriations | closest registry entry | recorded decision |
|---|---:|---|---|
| Emergency Board | 6 | — | reviewed: a contingency fund |
| Oregon Ocean Science Trust | 1 | — | not-reviewed: nobody has looked |

---
"""


def test_the_report_section_4_bodies_are_read_from_the_committed_report():
    """Read offline, from the committed markdown — --check must not need the sibling, and
    recomputing section 4 means re-running the fuzzy suggester against ERF."""
    assert lar.report_bodies(SECTION_4) == ["Emergency Board", "Oregon Ocean Science Trust"]


def test_check_names_a_report_body_the_crosswalk_has_not_decided():
    """AC8. If the report can name a body the crosswalk says nothing about, the reason
    goes back to living in the report — which is the state #23 was filed on."""
    cw = good()
    problems = lar.check(cw, NAMES, {"Emergency Board": 6}, STAMPED,
                         section_4_bodies=["Emergency Board"])
    assert any("Emergency Board" in p for p in problems), problems


def test_the_committed_report_and_crosswalk_agree_today():
    """The same guard, on the real committed files."""
    cw = lar.load_crosswalk()
    bodies = lar.report_bodies((ROOT / "_meta" / "unresolved-agencies.md").read_text())
    assert bodies, "section 4 of the committed report parsed empty — the reader is broken"
    undecided = [b for b in bodies if b not in (cw.get("unmapped") or {})
                 and b not in (cw.get("mapping") or {})]
    assert undecided == []


def test_the_report_renders_the_crosswalks_reason_rather_than_its_own():
    """AC8. The generated report shows the decision recorded here, verbatim, so the two
    files cannot drift into asserting the same fact in two voices."""
    import build_joins
    cw = good()
    cw["unmapped"]["Emergency Board"] = {
        "basis": "reviewed", "checked": "no registry entry",
        "reason": "A contingency fund that disburses through other agencies.",
        "source": "_meta/unresolved-agencies.md section 4"}
    rendered = build_joins.crosswalk_decision("Emergency Board", cw)
    assert "reviewed" in rendered
    assert "A contingency fund that disburses through other agencies." in rendered


def test_the_report_says_so_when_a_body_has_no_recorded_decision():
    """A body the crosswalk has not decided must READ as undecided in the report, not as
    a blank cell — a blank is exactly the state that made the two indistinguishable."""
    import build_joins
    rendered = build_joins.crosswalk_decision("Department of Nothing", good())
    assert "not recorded" in rendered.lower()
    assert "agency-crosswalk.yml" in rendered


def test_the_joins_builder_reads_the_basis_from_the_crosswalk():
    """A regenerated join must carry the same basis --stamp would write, from the same
    file. Two writers of one field reading different sources is how the crosswalk and the
    documents drift apart between builds."""
    import build_joins
    assert build_joins.basis_provenance("340", good())[0] == "das_number"
    assert build_joins.basis_provenance("165", good())[0] == "exact"


def test_the_joins_builder_refuses_to_stamp_a_slug_it_has_no_basis_for():
    """A join asserting a registry identity with no recorded warrant is the state #23 was
    filed on. The builder must stop, not write a blank."""
    import build_joins
    with pytest.raises(KeyError, match="777"):
        build_joins.basis_provenance("777", good())


def test_check_fails_when_the_section_4_gate_cannot_read_the_report():
    """A gate that quietly passes when its input is unreadable is not a gate. The report
    is a committed generated file; if it is missing, or its section 4 no longer parses,
    the crosswalk-vs-report agreement was NOT checked and must not be reported as checked."""
    problems = lar.check_report_readable(None)
    assert any("not read" in p or "missing" in p for p in problems), problems
    problems = lar.check_report_readable("# Unresolved agencies\n\nno section four here\n")
    assert any("section 4" in p for p in problems), problems
    assert lar.check_report_readable(SECTION_4) == []


def test_a_join_says_which_crosswalk_entry_its_basis_came_from():
    """The stamped `agency_registry_basis` is the crosswalk's warrant for the AGENCY,
    reached by DAS number — NOT a description of how this document's own
    `appropriated_to` string was matched. Those are different resolutions of the same
    body, and a document that carried the first while looking like the second would be
    attributing a warrant it does not have. So the document names the crosswalk key the
    basis belongs to, and a reader can check it."""
    import build_joins
    assert build_joins.basis_provenance("340", good()) == (
        "das_number", "ENVI QUALITY, DEPT")


def test_check_names_a_document_whose_basis_key_disagrees_with_the_crosswalk():
    """The key is what makes the stamped basis attributable. A document naming a key the
    crosswalk does not resolve that way is asserting a warrant that is not there."""
    stamped = [dict(STAMPED[0], agency_registry_basis_key="SECRETARY OF STATE")]
    problems = lar.check(good(), NAMES, {}, stamped)
    assert any("join-a" in p and "SECRETARY OF STATE" in p for p in problems), problems


def test_check_names_a_document_carrying_a_basis_but_no_key():
    stamped = [dict(STAMPED[0])]
    del stamped[0]["agency_registry_basis_key"]
    problems = lar.check(good(), NAMES, {}, stamped)
    assert any("join-a" in p and "agency_registry_basis_key" in p for p in problems), problems


# --- #42: 536 expenditure documents could carry a registry slug and carry none ---------
# Every join document already carries the four agency_registry_* fields, from a match
# against the BILL's `appropriated_to` wording. An expenditure document has no bill to
# match against — its only handle on identity is `agency_code`, the same DAS number the
# crosswalk's `das_number` entries are keyed by — so the same warrant `stamp()` writes
# beside an existing join slug must be reachable from `agency_code` alone, with nothing
# in ERF required to look it up.

def test_expenditure_registry_fields_reads_the_same_basis_a_join_would():
    """build_documents.py must write the same four fields for an expenditure document
    that link_agency_registry.py --stamp writes onto a join for the same DAS number —
    one crosswalk, one warrant, regardless of which content root reads it."""
    assert lar.expenditure_registry_fields("340", good()) == {
        "agency_registry_slug": "department-of-environmental-quality",
        "agency_registry_basis": "das_number",
        "agency_registry_basis_key": "ENVI QUALITY, DEPT",
        "agency_registry_corpus": "executive-regulatory-frameworks",
    }


def test_expenditure_registry_fields_is_none_for_an_unmapped_code():
    """An agency_code the crosswalk does not map must not be guessed at — the remaining
    8 documents (the two strings recorded as `unmapped`) stay unstamped, not wrong. Both
    now carry `basis: reviewed` since #43; "NOT YET REVIEWED" describes neither of them
    any more."""
    assert lar.expenditure_registry_fields("999", good()) is None


def test_deq_expenditure_documents_carry_the_slug_the_crosswalk_maps_them_to():
    """#42, on the real committed data. DEQ's seven `expenditures-340-fy20XX.md`
    documents are the ones the issue names as "the documents that actually hold what DEQ
    spent" — they must carry the slug, not just the 13 join documents that already did.
    Independent literals: das_agency_number 340 and the seven fiscal years come from the
    committed crosswalk and the issue's own count, not from re-running the code under
    test."""
    cw = lar.load_crosswalk()
    docs = {p.stem: yaml.safe_load(p.read_text().split("---\n", 2)[1])
            for p in sorted((ROOT / "expenditures").glob("expenditures-340-fy*.md"))}
    assert set(docs) == {f"expenditures-340-fy{y}" for y in range(2019, 2026)}
    for doc_id, fm in sorted(docs.items()):
        assert fm.get("agency_registry_slug") == "department-of-environmental-quality", \
            (doc_id, fm.get("agency_registry_slug"))
        assert fm.get("agency_registry_corpus") == "executive-regulatory-frameworks", doc_id
        assert fm.get("agency_registry_basis") == "das_number", doc_id
        assert fm.get("agency_registry_basis_key") == "ENVI QUALITY, DEPT", doc_id
    # Independent of the crosswalk fixture above: re-derive from the REAL crosswalk too.
    real = lar.expenditure_registry_fields("340", cw)
    assert docs["expenditures-340-fy2019"]["agency_registry_slug"] == real["agency_registry_slug"]


def test_build_documents_writes_the_same_registry_fields_a_rebuild_would():
    """#42. `src/build_documents.py`, not just `--stamp`, must write these fields — a
    rebuild-from-scratch is the second half the issue names ("extending it (and
    src/build_documents.py, so a rebuild writes the same thing) is mechanical"). Two
    writers of one field reading different sources is how the crosswalk and a freshly
    regenerated document would drift apart on the very next rebuild."""
    import build_documents
    assert build_documents.registry_fields("340", good()) == {
        "agency_registry_slug": "department-of-environmental-quality",
        "agency_registry_basis": "das_number",
        "agency_registry_basis_key": "ENVI QUALITY, DEPT",
        "agency_registry_corpus": "executive-regulatory-frameworks",
    }
    assert build_documents.registry_fields("999", good()) == {}


def test_build_one_actually_wires_the_registry_fields_into_a_document(tmp_path):
    """The wiring, not just the helper (test-quality caveat on #42): the previous test
    asserted only on `registry_fields()`, the pure `or {}` wrapper — deleting
    `**registry_fields(str(agency), cw)` from `build_one()` left that test, and every
    other test in the suite, green. This drives `build_one()` itself, the function a
    rebuild actually calls, and fails if that splat is ever removed.

    Also locks in the FIELD ORDER `build_one()` emits into frontmatter: slug, basis,
    basis_key, corpus — the order `stamp()` converges an already-slugged document to, so
    a document `build_documents.py` writes and one `--stamp` backfills read the same
    order (`test_stamp_round_trips_the_committed_tree_to_a_fixed_point` guards the other
    half: that this order is ALSO the order already on disk, not just the order the
    generator emits fresh).
    """
    import build_documents
    from decimal import Decimal

    year = 2019
    d = {
        "years": {year}, "statewide": {year: Decimal("1000")},
        "totals": {("340", year): Decimal("500")},
        "rank": {("340", year): (1, 1)},
        "by_budget": {("340", year): [("1000", "SALARIES", Decimal("500"), 3)]},
        "by_expend": {("340", year): [("100", "GENERAL", Decimal("500"), 3)]},
        "by_vendor": {("340", year): [("SOME VENDOR", Decimal("500"), 3)]},
    }
    doc_id, _body, fm = build_documents.build_one(
        "340", year, "ENVI QUALITY, DEPT", Decimal("500"), 3, d,
        "2026-01-01", "deadbeef", good())
    assert doc_id == "expenditures-340-fy2019"
    assert fm["agency_registry_slug"] == "department-of-environmental-quality"
    assert fm["agency_registry_basis"] == "das_number"
    assert fm["agency_registry_basis_key"] == "ENVI QUALITY, DEPT"
    assert fm["agency_registry_corpus"] == "executive-regulatory-frameworks"

    keys = list(fm.keys())
    i = keys.index("agency_registry_slug")
    assert keys[i:i + 4] == ["agency_registry_slug", "agency_registry_basis",
                            "agency_registry_basis_key", "agency_registry_corpus"]

    # And the ACTUAL frontmatter text a rebuild would write, not just the dict.
    text = build_documents.dump_fm(fm)
    lines = [ln for ln in text.splitlines() if ln.startswith("agency_registry_")]
    assert lines == [
        "agency_registry_slug: department-of-environmental-quality",
        "agency_registry_basis: das_number",
        "agency_registry_basis_key: ENVI QUALITY, DEPT",
        "agency_registry_corpus: executive-regulatory-frameworks",
    ]


def test_stamp_round_trips_the_committed_tree_to_a_fixed_point(tmp_path):
    """The missing half of the round trip (review finding on #42): the COMMITTED tree
    must already be what `--stamp` converges to, not just what a fresh rebuild converges
    to. Before `expenditure_registry_fields()`'s field order matched `stamp()`'s (slug,
    basis, basis_key, corpus), running `--stamp` on the clean committed tree reordered
    every one of the 536 stamped expenditure documents — a real, reproducible 536-file
    diff (536 insertions / 536 deletions, `agency_registry_corpus` moving from above the
    basis pair to below it), not a hypothetical one. A second `--stamp` was then a
    no-op, and a following rebuild flipped all 536 back — so an operator following
    `--check`'s own advice to run `--stamp` got a no-op diff and the next rebuild
    reversed it.

    Copies expenditures/, joins/ and bills/ into tmp_path (never touches the real working
    tree) and calls `stamp()` / `stamp_expenditures()` with `docs=` pointed at the copy,
    the seam those functions expose for exactly this. `changed == 0` on both IS the fixed
    point: nothing needed rewriting because the committed order already matches.
    """
    import shutil

    copies = {}
    for name in ("expenditures", "joins", "bills"):
        dst = tmp_path / name
        shutil.copytree(ROOT / name, dst)
        copies[name] = dst

    cw = lar.load_crosswalk()
    mapping = cw.get("mapping") or {}

    stamped = lar.stamped_docs(roots=(copies["joins"], copies["expenditures"],
                                      copies["bills"]))
    assert stamped, "fixture produced no stamped documents — the test proves nothing"
    examined, changed = lar.stamp(mapping, docs=stamped)
    assert changed == 0, (
        f"{changed} of {examined} already-slugged document(s) were rewritten by "
        f"--stamp on the committed tree — the tree is not a fixed point of --stamp")

    # unslugged_expenditure_docs() also returns the 8 documents behind the two
    # `unmapped` crosswalk strings (833, 999) — correctly unslugged, not a defect. The
    # fixed-point claim is narrower: of whichever documents carry no slug, none may have
    # a `agency_code` the crosswalk DOES map (that would be a lost stamp, #42's
    # coverage-gap fix in check_stamps), which is exactly what stamp_expenditures()'s
    # own `examined` count measures.
    unslugged = lar.unslugged_expenditure_docs(root=copies["expenditures"])
    ex_examined, ex_changed = lar.stamp_expenditures(mapping, docs=unslugged)
    assert ex_examined == 0, (
        f"{ex_examined} unslugged document(s) have an agency_code the crosswalk maps — "
        f"a lost stamp on the committed tree")
    assert ex_changed == 0


def test_documents_by_agency_floor_for_deq_now_includes_its_spending():
    """#42's headline number. Measured 2026-08-22 at 13 (joins only); this is the count
    #23's verification pinned and the issue's own warning says SHOULD change when this
    lands — deliberately re-measured and updated here, not left stale. DEQ has 13 join
    documents and 7 expenditure documents, both now carrying the slug, so the floor
    documents_by_agency answers from this corpus's committed files is 20."""
    import yaml as _yaml
    matches = []
    for root in ("joins", "expenditures"):
        for p in sorted((ROOT / root).glob("*.md")):
            fm = _yaml.safe_load(p.read_text().split("---\n", 2)[1])
            if fm.get("agency_registry_slug") == "department-of-environmental-quality":
                matches.append(fm["id"])
    assert len(matches) == 20, (len(matches), matches)

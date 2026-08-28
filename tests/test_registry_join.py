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
    """A registry after ERF#168: `name` is statutory, `oar_name` is the OAR chapter title."""
    p = tmp_path / "agencies.yml"
    p.write_text(yaml.safe_dump({"organizations": [
        # No aliases: nothing but `oar_name` can reach this one, so a test that resolves it
        # is observing the join key and not resolve_agency's spelling variants.
        {"slug": "department-of-forestry",
         "name": "Oregon Department of Forestry",          # statutory
         "oar_name": "Forestry Department, Oregon",        # OAR chapter title
         "budget_agency_code": "629"},
        # Aliases live on a SEPARATE body so the alias test cannot be satisfied by the
        # key under test, nor the key test by an alias.
        {"slug": "department-of-revenue",
         "name": "Oregon Department of Revenue",
         "oar_name": "Revenue Department, Oregon",
         "budget_agency_code": "150",
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
         "budget_agency_code": "100", "aliases": ["Governor's Office"]},
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


def test_registry_carrying_only_das_agency_number_is_not_stale(tmp_path):
    """The refusal is `neither` field, not `not budget_agency_code` alone -- a registry
    that has already migrated to `das_agency_number` and dropped the old key must NOT be
    mistaken for a pre-migration one. (Building the mapping from it is #49's job; this
    only proves the refusal itself does not fire.)"""
    p = tmp_path / "agencies.yml"
    p.write_text(yaml.safe_dump({"organizations": [
        {"slug": "department-of-forestry", "name": "Oregon Department of Forestry",
         "oar_name": "Forestry Department, Oregon", "das_agency_number": "629"},
    ]}), encoding="utf-8")
    by_name = build_joins.erf_agencies(p)  # must not raise
    assert by_name == {}


def test_load_registry_or_refuse_does_not_call_an_existing_file_absent(tmp_path, capsys):
    """A registry carrying only `das_agency_number` exists, parses, and does not trip the
    `neither key` refusal -- but `erf_agencies` still filters every row out because it
    still reads `budget_agency_code` (that switch is #49's job, not this one's). The
    resulting empty mapping must not be reported with the message reserved for a registry
    that was never found: the file is right there. This is the exact shape #37's own
    acceptance criteria were filed to kill, reached again one level up, at the caller
    `erf_agencies` does not control."""
    p = tmp_path / "agencies.yml"
    p.write_text(yaml.safe_dump({"organizations": [
        {"slug": "department-of-forestry", "name": "Oregon Department of Forestry",
         "oar_name": "Forestry Department, Oregon", "das_agency_number": "629"},
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

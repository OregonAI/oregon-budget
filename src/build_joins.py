#!/usr/bin/env python3
"""Build joins/*.md — appropriation documents mapped to the spending data, and CHECK them.

  python3 src/build_joins.py            # write the join documents
  python3 src/build_joins.py --check    # referential integrity; write nothing

THE `joins:` FRONTMATTER FIELD IS VALIDATED FOR SHAPE ONLY. The toolkit's schema requires
{document_id, dataset, key} on each entry and nothing anywhere reads it — no CLI resolves
a document_id, no validator confirms a key exists. A join block can therefore point at
documents that do not exist and dataset keys that match nothing, and every gate in this
platform stays green. Referential integrity here is ours to write, which is what `--check`
is.

WHAT AN APPROPRIATION-TO-SPENDING JOIN IS NOT
---------------------------------------------
It is NOT "appropriated $X, spent $Y". An appropriation goes to an agency for a stated
purpose; the expenditure data records that agency's TOTAL spending, from every funding
source, at vendor-transaction grain. HB4041 appropriates to Business Oregon, and Business
Oregon's recorded spending in the same years is many times larger and mostly unrelated.
Presenting the two figures side by side as though one accounts for the other is precisely
the "wrong join silently fabricates fiscal claims" failure this corpus was designed
against, and it is the easiest possible mistake to make with this data.

So a join document says: this appropriation was made to this agency, that agency's
spending in the covered fiscal years is this, and THE SECOND DOES NOT ACCOUNT FOR THE
FIRST. The link is entity-and-period, not dollars.

THE COVERAGE IS SMALL, AND SAYING SO IS THE POINT
--------------------------------------------------
Measured over the 170 extracted appropriation documents:

    150  biennium beginning July 1, 2025  -> FY2026-FY2027, OUTSIDE the mirror
     20  biennium ending June 30, 2025    -> FY2024-FY2025, inside it

The mirror ends at FY2025, so 88% of the appropriations in this corpus have no spending to
compare against — the money has not been spent yet, or the data does not exist yet. Of the
20 that overlap, 18 resolve to an agency code exactly; 2 do not and are recorded as
unresolved rather than guessed.

Reporting a join layer without that denominator would imply coverage this corpus does not
have.
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BILLS = ROOT / "bills"
OUT = ROOT / "joins"
GLOB = str(ROOT / "data" / "expenditures" / "*.parquet")
# The sibling's agency registry, which carries the hand-reviewed budget_agency_code.
# Found beside this repo under the upstream repo's current name. Override with --registry.
#
# oregon-budget#37: this list used to also try `oregon-policy-repo`, ERF's name before its
# rename -- sound while the two names meant the same content, but a fallback to a
# repository that was renamed away is not resilience, it is a second source of truth that
# can only ever be stale. Not repaired, because repairing it would keep the mechanism that
# caused the problem; the emptiness/staleness refusal in `erf_agencies` is the durable
# fix, and it holds for ANY candidate here, not just this one that got deleted.
#
# BUILDING needs this; --check does NOT, which is deliberate: referential integrity is a
# property of what was committed here and must be verifiable in CI without checking out a
# sibling. Only regenerating the joins requires the registry.
ERF_REGISTRY_CANDIDATES = [
    ROOT.parent / "executive-regulatory-frameworks" / "_meta/catalog/agencies.yml",
]


def default_registry() -> Path:
    return next((p for p in ERF_REGISTRY_CANDIDATES if p.is_file()),
                ERF_REGISTRY_CANDIDATES[0])


MIRROR_YEARS = set(range(2019, 2026))
MAINTAINER = "@dzinck"
DISCLAIMER = "NON-AUTHORITATIVE"


def erf_agencies(registry: Path) -> dict:
    """oar_name -> {slug, das_agency_number} for ERF orgs carrying a budget code.

    The codes are hand-reviewed in the sibling (src/link_budget_codes.py there). This
    corpus consumes them; it does not re-derive them, because a second fuzzy name match
    would reintroduce exactly the errors that review caught.

    KEYED ON `oar_name`, NOT `name`. ERF's ADR 0003 splits the registry's one name field in
    two: `name` becomes the body's STATUTORY name, while `oar_name` keeps the OAR chapter
    title and "remains the string OAR-derived joins must match". The strings this corpus
    resolves are `appropriated_to` lines lifted out of appropriation bills, which spell
    agencies the way the rules index does, so this join belongs on the `oar_name` side of
    that split. The two fields are identical in the registry today, so this changes nothing
    now — and that is the point: it is changed BEFORE the values diverge, because a join
    that silently keeps matching on a string that has quietly come to mean something else
    is the exact failure this crosswalk exists to prevent.
    """
    if not registry.is_file():
        return {}
    orgs = yaml.safe_load(registry.read_text())["organizations"]
    # A registry that is PRESENT and PARSES but carries neither key this corpus resolves
    # against is not "no registry" -- it is a pre-migration checkout (oregon-budget#37: a
    # local clone parked before ERF's ADR 0003/0004, or any future drift of the same
    # shape). Filtering rows below would quietly hand back `{}`, which reads identically
    # to "the registry has no bodies", and the run would proceed to build joins from
    # nothing while every slug still looked plausible. Refuse instead, and name the file
    # actually read so the refusal cannot be mistaken for "no registry found".
    if orgs and not any(o.get("das_agency_number") or o.get("budget_agency_code")
                        for o in orgs):
        raise ValueError(
            f"{registry} has {len(orgs)} organization(s) but none carries "
            f"das_agency_number or budget_agency_code -- this is a pre-migration "
            f"registry, not a current one. Refusing rather than building joins from an "
            f"empty mapping.")
    out = {}
    for o in orgs:
        if not o.get("das_agency_number"):
            continue
        # A row with no `oar_name` is NOT OAR-joinable, and that is a legitimate registry
        # state, not a defect: 19 bodies hold no OAR chapter (ADR 0003 admits bodies on
        # enabling authority alone), so after #168 they have no chapter title to carry.
        # Such a body stays reachable by alias below, and otherwise lands in the unresolved
        # report — the visible state this corpus already keeps for "no counterpart".
        if o.get("oar_name"):
            out[o["oar_name"].lower()] = o
        # ALIASES are the sibling's curated assertion that these names denote the same
        # body — reviewed once there rather than fuzzy-matched here. This is the seam that
        # lets "State Forestry Department" resolve without loosening the matcher, and it
        # absorbs renames: a former name stays an alias, so historical bills keep
        # resolving after a body is renamed.
        for alias in o.get("aliases") or []:
            out[alias.lower()] = o
    return out


def load_registry_or_refuse(registry: Path) -> dict | None:
    """The one place --build and --unresolved-report both go to get (or refuse) the
    registry, so `erf_agencies`'s ValueError -- raised only since #37, when the
    pre-migration refusal was added -- has exactly one catch site instead of needing to be
    added at both call sites separately. (That ValueError is the actual reason this exists:
    at the base #37 replaced, the two callers' own emptiness checks were already identical,
    both guarded on `if not by_name`, and could not have diverged on any input.)

    Returns None, having already printed why, when the registry should not be used:
    present-but-pre-migration (`erf_agencies` raises, caught here and reported as
    `REFUSED`, naming the file actually read); present but resolving to no mapping this
    corpus can build from (`SKIPPED`, naming the file and noting it was found); or the file
    not existing at all (also `SKIPPED`, with a message that says so instead).
    """
    try:
        by_name = erf_agencies(registry)
    except ValueError as e:
        print(f"REFUSED: {e}", file=sys.stderr)
        return None
    if not by_name:
        if registry.is_file():
            print(f"SKIPPED: {registry} exists but no organization in it resolves to a "
                  f"das_agency_number mapping this corpus can build from. Join documents "
                  f"cannot be built without one, and this is NOT a pass.", file=sys.stderr)
        else:
            print(f"SKIPPED: no agency registry at {registry}. Join documents cannot be "
                  f"built without the hand-reviewed das_agency_number mapping, and this "
                  f"is NOT a pass.", file=sys.stderr)
        return None
    return by_name


def _norm(s: str) -> str:
    """Typographic normalisation only — never a semantic guess.

    Bills use a curly apostrophe ("Department of Veterans’ Affairs"); the registry uses a
    straight one. That is the same name rendered two ways, and treating it as a mismatch
    left 4 appropriations unresolved for a reason that has nothing to do with identity.
    """
    return s.replace("’", "'").replace("‘", "'").strip().lower()


def resolve_agency(name: str, by_name: dict):
    """Exact match only, over a few PROVABLY UNAMBIGUOUS spelling variants. Never fuzzy.

    A near-match here attaches an appropriation to the wrong agency, and the result reads
    as a finding. Unresolved is a reportable state; a guess is not.

    Each variant below was measured against the corpus before being added, and each
    resolves to EXACTLY ONE registry entry — verified, not assumed:

      registry ALIASES        the sibling's curated identity assertions, consulted first
                              via erf_agencies(); this is where a name variant SHOULD be
                              recorded rather than encoded as a rule here
      "oregon X" / "X"        the registry is inconsistent about the prefix
      leading "State "        bills write "State Department of Agriculture" where the
                              registry writes "Department of Agriculture"; 38 appropriations
                              turned on this alone, all single-match
      curly -> straight quote see _norm

    DELIBERATELY NOT ADDED: word-order equivalence ("State Forestry Department" vs
    "Department of Forestry", 17 appropriations). It is almost certainly the same body, but
    "almost certainly" is how the Legislative Revenue Office got matched to the Department
    of Revenue in the sibling corpus. Those stay unresolved and reported until a human
    records the mapping, which is what the registry's das_agency_number exists for.
    """
    if not name:
        return None
    by_norm = {_norm(k): v for k, v in by_name.items()}
    k = _norm(name)
    for variant in (k, f"oregon {k}", k.removeprefix("oregon "), k.removeprefix("state ")):
        hit = by_norm.get(variant)
        if hit:
            return hit
    return None


def load_bills() -> list[dict]:
    out = []
    for p in sorted(BILLS.glob("*.md")):
        fm = yaml.safe_load(p.read_text().split("---\n", 2)[1])
        out.append(fm)
    return out


def spending(con, agency: str, years: list[int]) -> dict:
    ys = ", ".join(str(int(y)) for y in years)
    row = con.execute(
        f"select sum(expense), count(*), count(distinct vendor) from '{GLOB}' "
        f"where agency = ? and fiscal_year in ({ys})", [agency]).fetchone()
    per = con.execute(
        f"select fiscal_year, sum(expense) from '{GLOB}' where agency = ? "
        f"and fiscal_year in ({ys}) group by 1 order by 1", [agency]).fetchall()
    return {"total": row[0], "records": row[1], "vendors": row[2], "by_year": per}


def build(fm: dict, org: dict, con, today: str, cw: dict) -> tuple[str, str]:
    code = org["das_agency_number"]
    basis, basis_key = basis_provenance(code, cw)
    years = [y for y in fm["biennium_fiscal_years"] if y in MIRROR_YEARS]
    sp = spending(con, code, years)
    doc_id = f"join-{fm['id'].replace('appropriations-', '')}-agency-{code}"

    # The join entries. Every one is checked by --check: the document must exist here,
    # and the {dataset, key} must return rows from the mirror.
    joins = [{"document_id": f"expenditures-{code}-fy{y}", "dataset": "expenditures",
              "key": f"agency={code};fiscal_year={y}"} for y in years]

    out_fm = {
        "schema_version": 1, "corpus": "oregon-budget", "jurisdiction": "oregon",
        "id": doc_id,
        "title": f"{fm['citation']} → agency {code} spending, FY{years[0]}–FY{years[-1]}",
        "doc_type": "dataset_doc",
        "citation": f"Join: {fm['citation']} to Oregon Agency Expenditures agency {code}",
        "issuing_body": "Oregon Department of Administrative Services",
        "source_url": fm["source_url"],
        "source_format": "soda",
        "snapshot_policy": "hash-only",
        "status": "current",
        "content_mode": "summary",
        "last_verified": "",  # rule 6: only corpus-verify writes this
        "verified_by": "",
        "maintainer": MAINTAINER,
        "human_reviewed": False,
        "joins": joins,
        "relationships": {"implements": [], "implemented_by": [],
                          "references_external": [fm["citation"]],
                          "related": [fm["id"]] + [j["document_id"] for j in joins],
                          "supersedes": []},
        "tags": ["oregon-budget", "join", f"agency-{code}", "unreviewed"],
        "appropriation_document": fm["id"],
        "sibling_corpus": fm.get("sibling_corpus"),
        "sibling_document_id": fm.get("sibling_document_id"),
        "agency_code": code,
        "agency_registry_slug": org["slug"],
        # WHY that slug is right, carried from the crosswalk rather than restated, so a
        # consumer reading this document can tell a mechanical match from a judgment. It
        # is the crosswalk's warrant for the AGENCY, about the crosswalk key named below
        # — not a description of how this bill's own `appropriated_to` string matched.
        "agency_registry_basis": basis,
        "agency_registry_basis_key": basis_key,
        "agency_registry_corpus": "executive-regulatory-frameworks",
        "biennium": fm.get("biennium"),
        "fiscal_years": years,
        # The mapping that makes this join possible, recorded ON the join rather than
        # applied silently. A reader who rejects it can discard this document.
        "biennium_to_fiscal_year_assumption": (
            "Oregon's fiscal year runs 1 July to 30 June and is named for the calendar "
            "year it ends in, so a biennium ending 30 June 2025 covers FY2024 and FY2025. "
            "This is a stated convention, not something the expenditure dataset asserts "
            "about itself."),
    }

    L = []
    L.append(f"> **{DISCLAIMER} — UNREVIEWED.** This document links an appropriation to an")
    L.append("> agency's spending records. The spending figures **do not account for** the")
    L.append("> appropriation — see below. Neither side has been checked by a person.")
    L.append("")
    L.append(f"# {fm['citation']} → agency {code}")
    L.append("")
    L.append("## At a glance")
    L.append("")
    L.append(f"{fm['citation']} appropriates to **{org['name']}** "
             f"(budget agency code `{code}`, registry slug `{org['slug']}`) for the "
             f"**biennium {fm.get('biennium')}**, which on the stated fiscal-year "
             f"convention covers **FY{years[0]}–FY{years[-1]}**.")
    L.append("")
    if sp["total"] is not None:
        L.append(f"In those fiscal years that agency recorded **${sp['total']:,}** of "
                 f"spending across {sp['records']:,} transactions and "
                 f"{sp['vendors']:,} distinct payees.")
    else:
        L.append(f"The mirror holds **no spending at all** for agency {code} in "
                 f"FY{years[0]}–FY{years[-1]}. That is a finding, not an error: it means "
                 f"this agency recorded no expenditures in those years.")
    L.append("")
    L.append("## What this join does and does not say")
    L.append("")
    L.append("**It links an entity and a period, not dollars.** The appropriation was made "
             "to this agency for a purpose stated in the bill. The figure above is that "
             "agency's *total* recorded spending from *every* funding source, at "
             "vendor-transaction grain. It is not the appropriation being spent, it is "
             "not a superset of it in any traceable way, and the two numbers must not be "
             "compared as though one accounts for the other.")
    L.append("")
    L.append("Answering \"was this appropriation spent?\" needs an expenditure record "
             "carrying the appropriation's own identifier. This dataset has no such "
             "column, so that question cannot be answered from this corpus, and this "
             "document does not pretend otherwise.")
    L.append("")
    if sp["by_year"]:
        L.append("## Agency spending by fiscal year")
        L.append("")
        L.append("| Fiscal year | Recorded spending |")
        L.append("|---|---:|")
        for y, amt in sp["by_year"]:
            L.append(f"| FY{y} | ${amt:,} |")
        L.append("")
    L.append("## Provenance")
    L.append("")
    L.append(f"- Appropriation figures: `{fm['id']}` in this corpus — machine-extracted "
             f"from bill text and **not human-reviewed**.")
    L.append(f"- Bill text: `{fm.get('sibling_document_id')}` in the "
             f"`{fm.get('sibling_corpus')}` corpus, referenced not copied.")
    L.append(f"- Agency identity: `{org['slug']}` in the "
             f"`executive-regulatory-frameworks` corpus, whose registry carries the "
             f"hand-reviewed `das_agency_number: {code}`. Resolved here by matching this "
             f"bill's `appropriated_to` string against that registry, exact-only.")
    L.append(f"- Agency identity, independently: `_meta/agency-crosswalk.yml` resolves the "
             f"expenditure feed's own name for this body, `{basis_key}`, to the same slug "
             f"on basis `{basis}`. The `agency_registry_basis` in this document's "
             f"frontmatter is THAT claim, about THAT string — not a description of how the "
             f"bill's wording matched.")
    L.append(f"- Spending: the committed Parquet mirror, reconciled against live SODA "
             f"weekly.")
    L.append("")
    return doc_id, f"---\n{yaml.safe_dump(out_fm, sort_keys=False, allow_unicode=True, width=100)}---\n\n" + "\n".join(L)


def check(con) -> int:
    """Referential integrity for every `joins:` block. The gate the toolkit does not have."""
    docs = {p.stem for root in ("expenditures", "bills", "datasets", "joins")
            for p in (ROOT / root).glob("*.md")}
    files = sorted(OUT.glob("*.md"))
    if not files:
        print("no join documents", file=sys.stderr)
        return 1
    bad = entries = 0
    for p in files:
        fm = yaml.safe_load(p.read_text().split("---\n", 2)[1])
        for j in fm.get("joins") or []:
            entries += 1
            if j["document_id"] not in docs:
                print(f"  FAIL {p.name}: document_id {j['document_id']!r} resolves nowhere")
                bad += 1
                continue
            # The key must actually select rows. A key matching nothing is a join that
            # looks real and answers nothing.
            kv = dict(part.split("=", 1) for part in j["key"].split(";"))
            n = con.execute(
                f"select count(*) from '{GLOB}' where agency = ? and fiscal_year = ?",
                [kv["agency"], int(kv["fiscal_year"])]).fetchone()[0]
            if n == 0:
                print(f"  FAIL {p.name}: key {j['key']!r} matches no rows in the mirror")
                bad += 1
        for ref in ("appropriation_document",):
            if fm.get(ref) and fm[ref] not in docs:
                print(f"  FAIL {p.name}: {ref} {fm[ref]!r} resolves nowhere")
                bad += 1
    print(f"\n{len(files)} join document(s), {entries} join entries checked")
    print("every document_id resolves and every key matches rows" if not bad
          else f"  {bad} problem(s)")
    return 1 if bad else 0



# ONE reader and ONE lookup for the crosswalk, imported rather than reimplemented.
# Written the other way first, and the two copies immediately disagreed: this file's
# lookup rescanned the mapping linearly and could not see the das-number conflict that
# --check fails on, so a rebuild could write a basis the gate then rejected.
import link_agency_registry as registry_link                     # noqa: E402

CROSSWALK = registry_link.CROSSWALK


def load_crosswalk(path: Path = CROSSWALK) -> dict:
    """The crosswalk, or {} when it is absent. Absence is the caller's decision to make:
    --unresolved-report degrades to "not recorded", the builder refuses to run."""
    return registry_link.load_crosswalk(path) if path.is_file() else {}


def basis_provenance(code: str, cw: dict) -> tuple[str, str]:
    """(basis, crosswalk key) for DAS agency number `code`.

    TWO DIFFERENT RESOLUTIONS OF THE SAME BODY MEET IN A JOIN DOCUMENT, and conflating
    them would misattribute a warrant. This document's `agency_registry_slug` was reached
    by resolve_agency() matching the BILL's `appropriated_to` string ("Department of
    Justice") against the registry. The crosswalk reached the same slug from the
    EXPENDITURE feed's string ("JUSTICE, DEPT OF") through the DAS number. They agree —
    --check fails if they ever do not — but the `basis` recorded here is the crosswalk's,
    about the crosswalk's key, and stamping it unlabelled would read as a description of
    how the bill's own string matched. So the key travels with the basis and a reader can
    see which string it is a claim about.

    Raises rather than defaulting: a join that asserts a registry identity with no
    recorded basis is exactly the state oregon-budget#23 was filed on, and a blank there
    would be indistinguishable from a mapping nobody recorded.
    """
    index, conflicts = registry_link.by_das_number(cw.get("mapping") or {})
    if conflicts:
        raise KeyError("; ".join(conflicts))
    for key, entry in sorted((cw.get("mapping") or {}).items()):
        if str(entry.get("das_agency_number") or "") == str(code):
            return index[str(code)]["basis"], key
    raise KeyError(f"_meta/agency-crosswalk.yml maps no agency with das_agency_number "
                   f"{code!r}; the join cannot record why its slug is right")


def crosswalk_decision(name: str, cw: dict) -> str:
    """The decision recorded for `name` in _meta/agency-crosswalk.yml, for section 4.

    THE CROSSWALK IS THE SOURCE OF RECORD for why a body has no registry counterpart;
    this report renders it. Before that was decided (oregon-budget#23) the reason lived
    only in this generator's section-4 paragraph, which is a fixed class statement printed
    over whichever names scored below the fuzzy threshold — a bucket label being read as a
    finding about each body in it. A body with no entry reads as "not recorded" rather
    than as a blank cell, because a blank is precisely how "we looked and there is nothing"
    and "nobody has looked" became the same state.
    """
    entry = (cw.get("unmapped") or {}).get(name) or (cw.get("mapping") or {}).get(name)
    if not isinstance(entry, dict):
        return "**not recorded** — add an entry to `_meta/agency-crosswalk.yml`"
    if entry.get("slug"):
        return f"mapped to `{entry['slug']}` (basis `{entry.get('basis')}`)"
    reason = " ".join((entry.get("reason") or "").split())
    return f"`{entry.get('basis')}` — {reason}"


def unresolved_report(registry: Path) -> int:
    """Write the unresolved-agency work list.

    GENERATED, not hand-maintained, so it cannot quietly go stale as the extractor improves
    or the sibling registry gains codes. Regenerate with:

        python3 src/build_joins.py --unresolved-report

    The categories matter more than the count. Most of this list is NOT a missing registry
    mapping — it is the extractor failing to capture a name — and reporting one as the
    other would send someone to curate data that is already there.
    """
    import collections
    import re
    from datetime import datetime, timezone

    by_name = load_registry_or_refuse(registry)
    if by_name is None:
        return 2
    reg = yaml.safe_load(registry.read_text())["organizations"]

    STOP = {"of", "the", "and", "state", "oregon", "department", "office", "commission",
            "board", "division"}

    def toks(t):
        return {w for w in re.sub(r"[^a-z ]", " ", t.lower()).split() if w not in STOP}

    def suggest(name):
        """Closest registry entry by content-word overlap. A SUGGESTION for a human, never
        applied — this is exactly the fuzzy matching resolve_agency refuses to do.

        Scored against `oar_name` for the same reason erf_agencies() keys on it: a
        suggestion is only actionable if it is computed over the string the join would
        actually have to match."""
        t = toks(name)
        if not t:
            return None, 0.0
        best, score = None, 0.0
        for o in reg:
            ot = toks(o.get("oar_name") or "")
            if not ot:
                continue
            j = len(t & ot) / len(t | ot)
            if j > score:
                best, score = o, j
        return best, score

    groups = collections.defaultdict(list)
    for p in sorted(BILLS.glob("*.md")):
        fm = yaml.safe_load(p.read_text().split("---\n", 2)[1])
        if not (set(fm.get("biennium_fiscal_years") or []) & MIRROR_YEARS):
            continue
        name = (fm.get("appropriated_to") or "").strip()
        if resolve_agency(name, by_name):
            continue
        groups[name].append(fm)

    blank, modifies, multi, missing, variant, nocode, absent = [], [], [], [], [], [], []
    for name, docs in groups.items():
        if not name or len(toks(name)) == 0:
            # The bill itself leaves the recipient blank ("appropriated to ______") — a
            # budget-bill template with the agency not filled in. Separated from a real
            # extraction failure because they need opposite responses: nothing can fix a
            # name the bill does not contain.
            # Partition PER DOCUMENT, not per group. The empty-name group mixes both
            # cases, and an `all()` over the group put every one of them in whichever
            # bucket the outlier chose.
            b = [d for d in docs if d.get("blank_recipient")]
            rest = [d for d in docs if not d.get("blank_recipient")]
            # A null that is ACCURATE is not a parser failure. Two shapes, both flagged
            # by the extractor itself: bills that only modify/amend prior session laws
            # (the recipient lives in the amended chapter), and multi-recipient
            # itemizations (a single field cannot carry several recipients without
            # attributing the whole bill to one of them).
            mod = [d for d in rest if d.get("modifies_prior_appropriations")
                   or d.get("amends_prior_law")]
            mr = [d for d in rest
                  if d.get("recipients_in_itemization") and d not in mod]
            m = [d for d in rest if d not in mod and d not in mr]
            if b:
                blank.append((name, b, None, 0.0))
            if mod:
                modifies.append((name, mod, None, 0.0))
            if mr:
                multi.append((name, mr, None, 0.0))
            if m:
                missing.append((name, m, None, 0.0))
            continue
        best, score = suggest(name)
        if best and best.get("budget_agency_code") and score >= 0.6:
            variant.append((name, docs, best, score))
        elif best and score >= 0.6:
            # The body IS in the registry — it simply carries no budget_agency_code,
            # because it has no separately-recorded spending line. Reporting it as "no
            # registry counterpart" would send someone to create an entry that exists.
            nocode.append((name, docs, best, score))
        else:
            absent.append((name, docs, best, score))

    n = sum(len(d) for d in groups.values())
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    L = [f"# Unresolved agencies", "",
         f"_Generated {today} by `python3 src/build_joins.py --unresolved-report`. "
         f"Do not edit by hand._", "",
         f"**{n} appropriations** across **{len(groups)} distinct names** overlap the "
         f"FY2019–FY2025 expenditure mirror but name an agency that does not resolve "
         f"against the sibling registry's `budget_agency_code`, so no join was built.", "",
         "Resolution is deliberately exact-only. A near-match attaches an appropriation to "
         "the wrong agency and the result reads as a finding — which is how the "
         "*Legislative* Revenue Office once got matched to the Department of Revenue. "
         "Everything below stays unjoined until a human confirms it.", ""]

    L += ["## 1. The BILL leaves the recipient blank — nothing to fix", "",
          f"**{sum(len(d) for _, d, _, _ in blank)} appropriations.** The text reads "
          f"`appropriated to ______`. These are HB 5000-series budget templates whose "
          f"agency has not been filled in yet, so no agency could be extracted because "
          f"**the bill names none**. Not a parser defect and not a registry gap — there is "
          f"no fix, only accurate reporting.", "",
          "| captured value | appropriations | example bill |", "|---|---:|---|"]
    for name, docs, _, _ in sorted(blank, key=lambda x: -len(x[1])):
        L.append(f"| `{name or '(empty)'}` | {len(docs)} | `{docs[0]['id']}` |")

    L += ["", "## 1b. Extraction genuinely failed — the parser", "",
          f"**{sum(len(d) for _, d, _, _ in missing)} appropriations.** The bill names an "
          f"agency and `APPROPRIATED_TO` failed to capture it. This is parser work in "
          f"`src/extract_appropriations.py`.", ""]
    if missing:
        L += ["| captured value | appropriations | example bill |", "|---|---:|---|"]
        for name, docs, _, _ in sorted(missing, key=lambda x: -len(x[1])):
            L.append(f"| `{name or '(empty)'}` | {len(docs)} | `{docs[0]['id']}` |")
    else:
        L.append("_None._")

    L += ["", "## 1c. The bill only MODIFIES prior session laws — the null is accurate", "",
          f"**{sum(len(d) for _, d, _, _ in modifies)} appropriations.** These bills "
          f"increase, decrease or amend amounts appropriated by earlier session laws "
          f"(\"is increased by $X\", \"Section 3, chapter 598, Oregon Laws 2023, is "
          f"amended to read\"). The recipient of each amount lives in the amended "
          f"chapter, not in this bill's own text — no agency name exists here to "
          f"extract. Joining these means resolving the amended chapter first, which is "
          f"future work, not parser work.", ""]
    if modifies:
        L += ["| appropriations | example bill |", "|---:|---|"]
        for name, docs, _, _ in sorted(modifies, key=lambda x: -len(x[1])):
            L.append(f"| {len(docs)} | `{docs[0]['id']}` |")
    else:
        L.append("_None._")

    L += ["", "## 1d. Multi-recipient itemization — no single recipient exists", "",
          f"**{sum(len(d) for _, d, _, _ in multi)} appropriations.** The bill "
          f"appropriates to several bodies in one itemized list (\"(1) To the Housing "
          f"and Community Services Department: ...\"). A single `appropriated_to` "
          f"cannot carry that without attributing the whole bill to one recipient; the "
          f"names are recorded per document under `recipients_in_itemization`. "
          f"Per-recipient joins need the join model to carry them — an honest none "
          f"beats a wrong one.", ""]
    if multi:
        L += ["| recipients (from the bill) | appropriations | example bill |", "|---|---:|---|"]
        for name, docs, _, _ in sorted(multi, key=lambda x: -len(x[1])):
            names = "; ".join(docs[0].get("recipients_in_itemization") or [])
            L.append(f"| {names} | {len(docs)} | `{docs[0]['id']}` |")
    else:
        L.append("_None._")

    L += ["", "## 2. Probable name variant — needs a human to confirm", "",
          f"**{sum(len(d) for _, d, _, _ in variant)} appropriations.** A registry entry "
          f"with a budget code looks like the same body, usually differing only in word "
          f"order (\"State Forestry Department\" vs \"Department of Forestry\"). "
          f"**Suggestions are unverified** and were produced by exactly the fuzzy matching "
          f"`resolve_agency` refuses to apply. Confirm one by recording it in the "
          f"sibling's registry, not by loosening the matcher.", "",
          "| bill says | appropriations | suggested registry entry | code | overlap |",
          "|---|---:|---|---:|---:|"]
    for name, docs, best, score in sorted(variant, key=lambda x: -len(x[1])):
        L.append(f"| {name} | {len(docs)} | `{best['slug']}` | {best['budget_agency_code']} "
                 f"| {score:.2f} |")

    L += ["", "## 3. In the registry, but no budget code — cannot join", "",
          f"**{sum(len(d) for _, d, _, _ in nocode)} appropriations.** The body has a "
          f"registry entry, so this is NOT a missing agency. It carries no "
          f"`budget_agency_code` because the expenditure data records no separate "
          f"spending line for it — typically a sub-unit funded through its parent. "
          f"Nothing to join to; adding a code would mean inventing one.", "",
          "| bill says | appropriations | registry entry (no budget code) |", "|---|---:|---|"]
    for name, docs, best, score in sorted(nocode, key=lambda x: -len(x[1])):
        L.append(f"| {name} | {len(docs)} | `{best['slug']}` |")

    cw = load_crosswalk()
    L += ["", "## 4. No registry counterpart", "",
          f"**{sum(len(d) for _, d, _, _ in absent)} appropriations.** The exact-only "
          f"matcher resolved none of these names against the registry, and the "
          f"content-word suggester below found nothing close enough to propose. THAT IS "
          f"ALL THIS SECTION MEASURES. Whether a body is absent because it issues no "
          f"administrative rules and so holds no OAR chapter — the registry is keyed on "
          f"chapter assignment — or because nobody has looked, is a decision, and "
          f"decisions live in `_meta/agency-crosswalk.yml`. The last column is that "
          f"file's, rendered here rather than restated: `reviewed` means somebody "
          f"established why there is no counterpart, `not-reviewed` means the mechanical "
          f"check found none and nobody has established why.", "",
          "| bill says | appropriations | closest registry entry (no code / low overlap) "
          "| recorded decision (`_meta/agency-crosswalk.yml`) |",
          "|---|---:|---|---|"]
    for name, docs, best, score in sorted(absent, key=lambda x: -len(x[1])):
        near = f"`{best['slug']}` ({score:.2f})" if best and score >= 0.4 else "—"
        L.append(f"| {name} | {len(docs)} | {near} | "
                 f"{crosswalk_decision(name, cw).replace('|', chr(92) + '|')} |")

    L += ["", "---", "",
          "Appropriations whose biennium falls OUTSIDE FY2019–FY2025 are not listed here — "
          "they cannot be joined regardless of agency, because the expenditure mirror does "
          "not reach those years. See the README's coverage table.", ""]

    out = ROOT / "_meta" / "unresolved-agencies.md"
    out.write_text("\n".join(L))
    print(f"wrote {out.relative_to(ROOT)}")
    print(f"  {sum(len(d) for _,d,_,_ in blank):>4} bill leaves recipient blank (no fix exists)")
    print(f"  {sum(len(d) for _,d,_,_ in modifies):>4} modifies prior session laws (null is accurate)")
    print(f"  {sum(len(d) for _,d,_,_ in multi):>4} multi-recipient itemization (no single recipient)")
    print(f"  {sum(len(d) for _,d,_,_ in missing):>4} extraction genuinely failed (parser work)")
    print(f"  {sum(len(d) for _,d,_,_ in variant):>4} probable name variant (human confirms)")
    print(f"  {sum(len(d) for _,d,_,_ in nocode):>4} in registry, no budget code (cannot join)")
    print(f"  {sum(len(d) for _,d,_,_ in absent):>4} no registry counterpart (correct)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--unresolved-report", action="store_true",
                    help="write _meta/unresolved-agencies.md — the work list of "
                         "appropriations that overlap the mirror but name an agency the "
                         "registry does not resolve")
    ap.add_argument("--registry", default=None,
                    help="path to executive-regulatory-frameworks' agencies.yml")
    args = ap.parse_args()

    import duckdb
    con = duckdb.connect()
    if args.check:
        return check(con)
    if args.unresolved_report:
        return unresolved_report(Path(args.registry) if args.registry else default_registry())

    registry = Path(args.registry) if args.registry else default_registry()
    by_name = load_registry_or_refuse(registry)
    if by_name is None:
        return 2

    cw = load_crosswalk()
    if not (cw.get("mapping") or {}):
        print(f"SKIPPED: no crosswalk at {CROSSWALK}. Join documents cannot record the "
              f"basis for the registry slug they carry, and this is NOT a pass.",
              file=sys.stderr)
        return 2

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    OUT.mkdir(exist_ok=True)
    written = out_of_range = unresolved = 0
    unresolved_names = []
    for fm in load_bills():
        years = fm.get("biennium_fiscal_years") or []
        if not (set(years) & MIRROR_YEARS):
            out_of_range += 1
            continue
        org = resolve_agency(fm.get("appropriated_to") or "", by_name)
        if not org:
            unresolved += 1
            unresolved_names.append((fm["id"], (fm.get("appropriated_to") or "")[:48]))
            continue
        doc_id, text = build(fm, org, con, today, cw)
        (OUT / f"{doc_id}.md").write_text(text)
        written += 1

    print(f"{written} join document(s) -> {OUT.relative_to(ROOT)}/")
    print(f"  {out_of_range} appropriation(s) fall outside the mirror's FY2019-FY2025 "
          f"range and CANNOT be joined")
    print(f"  {unresolved} overlap the mirror but name an agency that does not resolve "
          f"exactly:")
    for i, n in unresolved_names:
        print(f"    {i}: {n!r}")
    print("\nEvery join is human_reviewed: false, and links an entity and a period — "
          "never dollars to dollars.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

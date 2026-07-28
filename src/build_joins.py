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
# The sibling's agency registry, which carries the hand-reviewed budget_agency_code. Tried
# in order beside this repo; the upstream repo is `executive-regulatory-frameworks` but a
# local checkout may still use its former name. Override with --registry.
#
# BUILDING needs this; --check does NOT, which is deliberate: referential integrity is a
# property of what was committed here and must be verifiable in CI without checking out a
# sibling. Only regenerating the joins requires the registry.
ERF_REGISTRY_CANDIDATES = [
    ROOT.parent / "executive-regulatory-frameworks" / "_meta/catalog/agencies.yml",
    ROOT.parent / "oregon-policy-repo" / "_meta/catalog/agencies.yml",
]


def default_registry() -> Path:
    return next((p for p in ERF_REGISTRY_CANDIDATES if p.is_file()),
                ERF_REGISTRY_CANDIDATES[0])
MIRROR_YEARS = set(range(2019, 2026))
MAINTAINER = "@dzinck"
DISCLAIMER = "NON-AUTHORITATIVE"


def erf_agencies(registry: Path) -> dict:
    """name -> {slug, budget_agency_code} for ERF orgs carrying a budget code.

    The codes are hand-reviewed in the sibling (src/link_budget_codes.py there). This
    corpus consumes them; it does not re-derive them, because a second fuzzy name match
    would reintroduce exactly the errors that review caught.
    """
    if not registry.is_file():
        return {}
    orgs = yaml.safe_load(registry.read_text())["organizations"]
    return {o["name"].lower(): o for o in orgs if o.get("budget_agency_code")}


def resolve_agency(name: str, by_name: dict):
    """Exact match only, with two spelling variants. Never fuzzy.

    A near-match here attaches an appropriation to the wrong agency, and the result reads
    as a finding. Unresolved is a reportable state; a guess is not.
    """
    if not name:
        return None
    k = name.strip().lower()
    return (by_name.get(k)
            or by_name.get(f"oregon {k}")
            or by_name.get(k.removeprefix("oregon ")))


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


def build(fm: dict, org: dict, con, today: str) -> tuple[str, str]:
    code = org["budget_agency_code"]
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
        "last_verified": today,
        "verified_by": MAINTAINER,
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
             f"hand-reviewed `budget_agency_code: {code}`.")
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--registry", default=None,
                    help="path to executive-regulatory-frameworks' agencies.yml")
    args = ap.parse_args()

    import duckdb
    con = duckdb.connect()
    if args.check:
        return check(con)

    registry = Path(args.registry) if args.registry else default_registry()
    by_name = erf_agencies(registry)
    if not by_name:
        print(f"SKIPPED: no agency registry at {registry}. Join documents cannot be "
              f"built without the hand-reviewed budget_agency_code mapping, and this is "
              f"NOT a pass.", file=sys.stderr)
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
        doc_id, text = build(fm, org, con, today)
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

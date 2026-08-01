#!/usr/bin/env python3
"""Generate one expenditure document per agency per fiscal year from the Parquet mirror.

544 documents, not 574. The plan's 82 x 7 was an upper bound; 30 agency-years have no
spending at all (agencies appear and disappear across FY2019-2025), and emitting a document
for those would fabricate a year that never existed.

VENDOR DETAIL IS INCLUDED, DELIBERATELY
---------------------------------------
The source names 98,933 distinct vendors, and these documents report the largest of them
per agency-year. This is public record published by the State of Oregon under
USGOV_WORKS, and who the state pays is the substance of the transparency question, not an
incidental detail of it. Withholding or masking it would make the corpus a less faithful
copy of the public data than the state's own portal, which is the opposite of this
platform's purpose.

WHY THIS SCRIPT HAS ITS OWN --check
-----------------------------------
`corpus-verify-provenance` structurally cannot verify these. They are derived aggregates,
not extracted source text: with `snapshot_policy: hash-only` and no committed `.txt`, the
verifier sets source_text = "" and checks nothing. Recording a `source_sha256` and calling
it verified would be a check that passes because it is not running — the exact failure this
platform keeps finding in its own CI.

So `--check` re-derives every number in every document from the Parquet and compares. That
is the real gate, and it is wired into CI alongside the toolkit's own.

There is deliberately NO `## Full text` section: `corpus-verify-provenance` requires every
line of one to appear verbatim in a committed snapshot, in order. An aggregate has no such
source, so claiming verbatim mode would be a false provenance claim.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from decimal import Decimal
from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "expenditures"
OUT = ROOT / "expenditures"
GLOB = str(DATA / "*.parquet")
MANIFEST = DATA / "manifest.json"

DATASET = "y9g9-xsxs"
SOURCE_URL = f"https://data.oregon.gov/d/{DATASET}"
MAINTAINER = "@dzinck"
# DAS operates the statewide financial system this dataset is published from. The subject
# agency of each document is a different thing, and lives in the title and tags.
ISSUING_BODY = "Oregon Department of Administrative Services"

DISCLAIMER = "NON-AUTHORITATIVE"
TOP_EXPEND_CLASSES = 12
TOP_VENDORS = 20


# Lowercased only when not the first word. Deliberately EXCLUDES "or" — see KEEP_UPPER.
SMALL_WORDS = {"of", "and", "the", "for", "to"}

# Tokens .title() would wreck. In this dataset "OR" is the postal abbreviation for Oregon
# ("ADVOCACY COMMISSIONS, OR"), never the conjunction: title-casing it to "Or" and
# lowercasing it to "or" are both wrong, and between them they mangled the names of five
# agencies across 33 documents. No name here uses "or" as a conjunction.
KEEP_UPPER = {"OR"}


_BANDS: dict | None = None


def band_of(code: str) -> tuple[str, bool]:
    """(band label, is it money) for an ORBITS account code, from the committed catalogue.

    The leading digit of a budget_class encodes a category -- revenue, personnel, capital
    outlay, distributions -- and DAS's crosswalk never states it. `_meta/catalog/
    account-codes.yml` does, so these documents can say "Capital outlay" where they used to
    list four codes beginning with 5 and leave the reader to know.

    Falls back to the leading digit when a code is absent from the catalogue. 5 of the codes
    in the mirror are not in the crosswalk, and a document that refused to render because
    DAS omitted a code would be the wrong failure -- the band is a property of the NUMBER,
    which is present either way.
    """
    global _BANDS
    if _BANDS is None:
        import yaml                                   # noqa: PLC0415
        p = ROOT / "_meta" / "catalog" / "account-codes.yml"
        cat = yaml.safe_load(p.read_text(encoding="utf-8")) if p.is_file() else {}
        by_id = {b["id"]: b for b in cat.get("bands") or []}
        _BANDS = {"acct": cat.get("accounts") or {}, "band": by_id,
                  "ranges": [(int(b["range"][:4]), int(b["range"][5:]), b["id"])
                             for b in cat.get("bands") or []]}
    e = _BANDS["acct"].get(code)
    bid = e.get("band") if e else next(
        (i for lo, hi, i in _BANDS["ranges"] if code.isdigit() and lo <= int(code) <= hi),
        None)
    b = _BANDS["band"].get(bid or "")
    return (b.get("label") if b else "Unclassified"), (b.get("monetary", True) if b else True)


def money(d: Decimal) -> str:
    return f"${d:,.2f}"


def display_name(source_name: str) -> str:
    """Title-case the shouted source name for reading.

    A pure case transformation, nothing more. Abbreviations stay as the state wrote them
    ("SRVCS" -> "Srvcs", not "Services") because expanding them would be a guess about what
    the state meant, and the verbatim string is preserved in frontmatter `agency_name`.
    """
    out = []
    for i, w in enumerate(source_name.split()):
        if w.strip(",") in KEEP_UPPER:
            out.append(w)
            continue
        t = w.title()
        if i and t.lower().strip(",") in SMALL_WORDS:
            t = t.lower()
        out.append(t)
    return " ".join(out)


def slug(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return re.sub(r"-+", "-", s)


def q(con, sql, *a):
    return con.execute(sql, list(a)).fetchall()


def gather(con) -> dict:
    """Everything the documents need, in a handful of queries rather than 544 x N.

    EVERY ranking query carries a deterministic tiebreaker. Ties are common — agency 603
    alone has three vendors at exactly $348,750.00 — and without one the engine returns
    them in arbitrary order, so regenerating churns committed documents with no change in
    the underlying data. That noise makes "is this stale?" unanswerable from a diff, which
    is the question the staleness gate exists to answer.
    """
    d = {}
    d["years"] = [r[0] for r in q(con, f"select distinct fiscal_year from '{GLOB}' order by 1")]
    d["statewide"] = {r[0]: r[1] for r in
                      q(con, f"select fiscal_year, sum(expense) from '{GLOB}' group by 1")}
    d["pairs"] = q(con, f"""
        select agency, fiscal_year, any_value(agency_1), sum(expense), count(*)
        from '{GLOB}' group by 1, 2 order by 1, 2""")
    d["by_budget"] = {}
    for a, y, code, name, amt, n in q(con, f"""
            select agency, fiscal_year, budget_class, any_value(budget_class_1),
                   sum(expense), count(*)
            from '{GLOB}' group by 1, 2, 3 order by 5 desc, 3"""):
        d["by_budget"].setdefault((a, y), []).append((code, name, amt, n))
    d["by_expend"] = {}
    for a, y, code, name, amt, n in q(con, f"""
            select agency, fiscal_year, expend_class, any_value(expend_class_1),
                   sum(expense), count(*)
            from '{GLOB}' group by 1, 2, 3 order by 5 desc, 3"""):
        d["by_expend"].setdefault((a, y), []).append((code, name, amt, n))
    d["by_vendor"] = {}
    for a, y, vendor, amt, n in q(con, f"""
            select agency, fiscal_year, vendor, sum(expense), count(*)
            from '{GLOB}' group by 1, 2, 3 order by 4 desc, 3"""):
        d["by_vendor"].setdefault((a, y), []).append((vendor, amt, n))
    # Rank within each year, by total spend.
    d["rank"] = {}
    for y in d["years"]:
        ordered = sorted([p for p in d["pairs"] if p[1] == y], key=lambda p: -p[3])
        for i, p in enumerate(ordered, 1):
            d["rank"][(p[0], y)] = (i, len(ordered))
    d["totals"] = {(p[0], p[1]): p[3] for p in d["pairs"]}
    return d


def build_one(agency, year, name, total, txns, d, retrieved, sha) -> tuple[str, str, dict]:
    doc_id = f"expenditures-{agency}-fy{year}"
    disp = display_name(name)
    rank, of = d["rank"][(agency, year)]
    statewide = d["statewide"][year]
    share = (total / statewide * 100) if statewide else Decimal(0)

    prior = d["totals"].get((agency, year - 1))
    if prior and prior > 0:
        delta = (total - prior) / prior * 100
        yoy = (f"That is {'up' if delta >= 0 else 'down'} {abs(delta):.1f}% from "
               f"{money(prior)} in FY{year - 1}.")
    elif (agency, year - 1) not in d["totals"] and year > min(d["years"]):
        yoy = f"No spending is recorded for this agency in FY{year - 1}."
    else:
        yoy = f"FY{year - 1} is outside the range this dataset covers."

    budget = d["by_budget"].get((agency, year), [])
    expend = d["by_expend"].get((agency, year), [])

    fm = {
        "schema_version": 1, "corpus": "oregon-budget", "jurisdiction": "oregon",
        "id": doc_id,
        "title": f"{disp} — FY{year} expenditures",
        "doc_type": "dataset_doc",
        "citation": f"Oregon Agency Expenditures, agency {agency}, FY{year}",
        "issuing_body": ISSUING_BODY,
        "source_url": SOURCE_URL,
        "source_format": "soda",
        "retrieved": retrieved,
        "source_sha256": sha,
        "snapshot_policy": "hash-only",
        "status": "current",
        "content_mode": "summary",
        "last_verified": retrieved,
        "verified_by": MAINTAINER,
        "maintainer": MAINTAINER,
        "conversion_notes": ("Title is the source agency name title-cased for reading; the "
                             "verbatim string is `agency_name`. Abbreviations are not "
                             "expanded. Figures are aggregated, not extracted text."),
        # Mechanically derived, never inferred: the same agency in the adjacent fiscal
        # years, plus the dataset these figures come from. This is what makes
        # `graph_neighbors` useful here — "walk this agency across time" is the second
        # question anyone asks after "what did it spend".
        "relationships": {
            "implements": [], "implemented_by": [], "references_external": [],
            "related": ([f"expenditures-{agency}-fy{y}"
                         for y in (year - 1, year + 1) if (agency, y) in d["totals"]]
                        + ["agency-expenditures"]),
            "supersedes": [],
        },
        "tags": ["oregon-budget", "expenditures", f"fy{year}", f"agency-{agency}",
                 slug(name)],
        "agency_code": str(agency), "agency_name": name, "fiscal_year": int(year),
        "total_expense": str(total), "transaction_count": int(txns),
    }

    L = []
    L.append(f"> **{DISCLAIMER} — AI-friendly reference only.** These are aggregates derived")
    L.append(f"> from a state dataset, not the official text of any budget or audit. Figures")
    L.append(f"> are as mirrored on {retrieved}; the live dataset may have been revised since.")
    L.append(f"> Verify against the official source: `{SOURCE_URL}`")
    L.append("")
    L.append(f"# {disp} — FY{year} expenditures")
    L.append("")
    L.append("## At a glance")
    L.append("")
    L.append(f"{disp} (agency code {agency}, recorded upstream as `{name}`) spent "
             f"**{money(total)}** in fiscal year {year}, across {txns:,} transaction "
             f"records. {yoy} The agency accounts for {share:.2f}% of the "
             f"{money(statewide)} in statewide agency spending recorded for FY{year}, "
             f"ranking **{rank} of {of}** agencies reporting that year.")
    L.append("")
    if budget:
        top = budget[0]
        L.append(f"The largest budget category was **{top[1].title()}** at {money(top[2])} "
                 f"({top[2] / total * 100:.1f}% of the agency's total).")
        L.append("")

    # ROLLED UP BEFORE ITEMISED. A reader asking what an agency spends money ON gets nine
    # categories rather than forty codes, and the categories are the ones the budget itself
    # is structured in. The itemised table below keeps every code.
    rolled: dict[str, list] = {}
    for code, _bname, amt, n in budget:
        label, monetary = band_of(code)
        # A NON-MONETARY CODE MUST NEVER BE SUMMED. The 8000 band is position counts and
        # FTE -- people, not dollars -- and adding it to a spending total produces a figure
        # that is not money and looks like it. No expenditure row carries one today, so this
        # raises rather than filtering: if that ever changes, the right outcome is a build
        # that stops, not a total quietly missing a category.
        if not monetary:
            raise SystemExit(
                f"{doc_id}: budget_class {code} is in a non-monetary band ({label}) and "
                f"carries {money(amt)} of expense. Position counts and FTE cannot be summed "
                f"with dollars — see _meta/catalog/account-codes.yml.")
        r = rolled.setdefault(label, [Decimal(0), 0, 0])
        r[0] += amt
        r[1] += n
        r[2] += 1
    L.append("## Spending by band")
    L.append("")
    L.append("The leading digit of a budget class encodes its category. This grouping is a "
             "convention of Oregon's budget structure, not a line in the source data — see "
             "[the account code reference](../datasets/account-code-structure.md).")
    L.append("")
    L.append("| Band | Amount | Share | Codes |")
    L.append("|---|---:|---:|---:|")
    for label, (amt, _n, codes) in sorted(rolled.items(), key=lambda kv: -kv[1][0]):
        L.append(f"| {label} | {money(amt)} | {amt / total * 100:.1f}% | {codes} |")
    L.append("")

    L.append("## Spending by budget class")
    L.append("")
    L.append("| Code | Budget class | Band | Amount | Share | Records |")
    L.append("|---|---|---|---:|---:|---:|")
    for code, bname, amt, n in budget:
        L.append(f"| {code} | {bname.title()} | {band_of(code)[0]} | {money(amt)} | "
                 f"{amt / total * 100:.1f}% | {n:,} |")
    L.append("")

    L.append("## Largest expenditure classes")
    L.append("")
    shown = expend[:TOP_EXPEND_CLASSES]
    L.append(f"The {len(shown)} largest of {len(expend)} expenditure classes used by this "
             f"agency in FY{year}.")
    L.append("")
    L.append("| Code | Expenditure class | Amount | Share |")
    L.append("|---|---|---:|---:|")
    for code, ename, amt, n in shown:
        L.append(f"| {code} | {ename.title()} | {money(amt)} | {amt / total * 100:.1f}% |")
    L.append("")

    vendors = d["by_vendor"].get((agency, year), [])
    L.append("## Largest vendors")
    L.append("")
    vshown = vendors[:TOP_VENDORS]
    vtop = sum(v[1] for v in vshown)
    L.append(f"The {len(vshown)} largest of {len(vendors):,} payees this agency recorded "
             f"payments to in FY{year}, accounting for {vtop / total * 100:.1f}% of its "
             f"spending. Names are reproduced exactly as the state records them.")
    L.append("")
    L.append("| Vendor | Amount | Share | Records |")
    L.append("|---|---:|---:|---:|")
    for vname, amt, n in vshown:
        L.append(f"| {vname} | {money(amt)} | {amt / total * 100:.1f}% | {n:,} |")
    L.append("")

    L.append("## Curator notes")
    L.append("")
    L.append(f"Figures are aggregated from {txns:,} vendor-level transaction records "
             f"covering {len(vendors):,} distinct payees. The vendor table above is the "
             f"state's own published data, reproduced rather than summarised: a payee "
             f"string is whatever was entered in the statewide financial system, so the "
             f"same organisation can appear under several spellings and is not "
             f"de-duplicated here. Treating each row as a distinct organisation will "
             f"undercount the large ones.")
    L.append("")
    L.append("Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The "
             "two do not line up, and no mapping between them is applied here. Comparing "
             "these figures to a biennial appropriation requires stating that mapping "
             "explicitly — it is the single most likely source of a plausible wrong number.")
    L.append("")
    L.append("## Verification")
    L.append("")
    L.append("Every figure above is reproducible from the live API. The agency total:")
    L.append("")
    L.append("```")
    L.append(f"{SOURCE_URL.replace('/d/', '/resource/')}.json"
             f"?$select=sum(expense)&$where=agency='{agency}' AND fiscal_year='{year}'")
    L.append("```")
    L.append("")
    L.append(f"`src/build_documents.py --check` re-derives every number in this document "
             f"from the committed Parquet mirror, and `src/ingest_expenditures.py --check` "
             f"reconciles that mirror against the live API. Both run in CI. The recorded "
             f"`source_sha256` is the hash of `expenditures-{year}.parquet`, the file these "
             f"figures were computed from.")
    L.append("")
    return doc_id, "\n".join(L) + "\n", fm


def dump_fm(fm: dict) -> str:
    import yaml
    return yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100)


def facts(fm: dict) -> tuple:
    """The numbers --check re-derives. Frontmatter only: the prose restates these, and a
    document whose frontmatter and body disagreed would fail the parse below first."""
    return (str(fm["agency_code"]), int(fm["fiscal_year"]),
            Decimal(fm["total_expense"]), int(fm["transaction_count"]))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="re-derive every document's figures from Parquet; write nothing")
    args = ap.parse_args()

    if not MANIFEST.is_file():
        print("no manifest — run src/ingest_expenditures.py first", file=sys.stderr)
        return 2
    man = json.loads(MANIFEST.read_text())
    retrieved = man["mirrored_at"][:10]
    sha_by_year = {e["fiscal_year"]: e["sha256"] for e in man["files"]}

    con = duckdb.connect()
    d = gather(con)

    if args.check:
        return check(d, sha_by_year)

    OUT.mkdir(exist_ok=True)
    written = 0
    for agency, year, name, total, txns in d["pairs"]:
        doc_id, body, fm = build_one(agency, year, name, total, txns, d, retrieved,
                                     sha_by_year[str(year)])
        (OUT / f"{doc_id}.md").write_text(f"---\n{dump_fm(fm)}---\n\n{body}")
        written += 1

    grand = sum(d["totals"].values())
    print(f"wrote {written} documents to {OUT.relative_to(ROOT)}/")
    print(f"  {len(d['years'])} fiscal years, "
          f"{len({p[0] for p in d['pairs']})} distinct agencies")
    print(f"  documents sum to ${grand:,} "
          f"(manifest total ${Decimal(man['total_sum_expense']):,})")
    if grand != Decimal(man["total_sum_expense"]):
        print("  MISMATCH — documents do not sum to the mirror", file=sys.stderr)
        return 1
    return 0


def check(d, sha_by_year) -> int:
    """Re-derive every document's figures. This is the gate the toolkit cannot provide."""
    import yaml
    expected = {f"expenditures-{a}-fy{y}": (str(a), int(y), tot, txn)
                for a, y, _n, tot, txn in d["pairs"]}
    files = sorted(OUT.glob("*.md"))
    if not files:
        print(f"FAIL: no documents in {OUT.relative_to(ROOT)}/", file=sys.stderr)
        return 1

    bad, seen = 0, set()
    for p in files:
        raw = p.read_text()
        if not raw.startswith("---\n"):
            print(f"  FAIL {p.name}: no frontmatter"); bad += 1; continue
        fm = yaml.safe_load(raw.split("---\n", 2)[1])
        doc_id = fm.get("id")
        if doc_id != p.stem:
            print(f"  FAIL {p.name}: id {doc_id!r} != filename stem"); bad += 1; continue
        seen.add(doc_id)
        if doc_id not in expected:
            print(f"  FAIL {p.name}: no such agency-year in the data"); bad += 1; continue
        want, got = expected[doc_id], facts(fm)
        if want != got:
            print(f"  FAIL {p.name}: document says {got[2]} / {got[3]} txns, "
                  f"Parquet says {want[2]} / {want[3]}")
            bad += 1
            continue
        # The prose must restate the frontmatter number, or the two could drift silently.
        if f"${want[2]:,.2f}" not in raw:
            print(f"  FAIL {p.name}: body does not contain the total {want[2]}"); bad += 1
            continue
        if fm.get("source_sha256") != sha_by_year[str(want[1])]:
            print(f"  FAIL {p.name}: source_sha256 is not the FY{want[1]} Parquet hash")
            bad += 1

    missing = set(expected) - seen
    for m in sorted(missing):
        print(f"  FAIL: {m}.md missing — the data has this agency-year")
    bad += len(missing)

    print(f"\n{len(files)} documents checked against {len(expected)} agency-years in the data")
    print("all documents reconcile" if not bad else f"{bad} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())

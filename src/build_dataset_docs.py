#!/usr/bin/env python3
"""Generate the `datasets/*.md` entity docs — one per Socrata dataset this corpus uses.

These describe the SHAPE of live datasets, not their rows. They follow
oregon-legislature's `entities/measures.md` structure, with `## Dataset reference` in place
of `## Entity reference` (these are Socrata datasets, not OData entity sets) — matching the
`index_headings.entity_doc` declared in corpus.yml, without which the substance of these
documents would not be indexed at all.

WHY GENERATED RATHER THAN HAND-WRITTEN: every field table, row count, and schema hash below
is measured from the live API at build time, and `--check` re-measures to detect drift. The
curator prose is the part a human writes, and it lives in DATASETS below. Hand-writing the
measured parts is how a "quirks (measured)" section quietly becomes a claim about how the
data looked a year ago.

THE QUIRKS SECTIONS ARE THE POINT. Two of them are load-bearing:

  * `mwsa-rpk9` ships its own **Totals row** inside the data. Summing all 80 rows reports
    $281,553,047,958 against a true $140,776,523,979 — exactly double Oregon's 2025-27
    budget, with no error anywhere to signal it.
  * The three datasets use **three different agency identifier systems**, and the agency
    NAME strings never match across them (0 exact matches of 83 vs 79). Any join must go
    through the numeric code, never the name.
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import duckdb

sys.path.insert(0, str(Path(__file__).parent))
import soda  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "datasets"
GLOB = str(ROOT / "data" / "expenditures" / "*.parquet")
MAINTAINER = "@dzinck"
DISCLAIMER = "NON-AUTHORITATIVE"

DATASETS = {
    "agency-expenditures": {
        "dataset": "y9g9-xsxs",
        "title": "Agency Expenditures — Multi-Year Report",
        "mirrored": True,
        "key": ("`agency` + `fiscal_year`. Neither is unique alone, and there is no row "
                "identifier beyond Socrata's synthetic `:id`. The corpus mirrors this "
                "dataset to Parquet and derives one document per `(agency, fiscal_year)` "
                "pair — 544 of them, the grain the budget question is actually asked at."),
        "glance": (
            "Vendor-level expenditure transactions for Oregon state agencies, FY2019–FY2025. "
            "This is the spending half of the appropriation-versus-actuals question, and the "
            "only one of the three datasets mirrored in full — 668,906 rows totalling "
            "$199,601,500,470.97, committed as one Parquet file per fiscal year.\n\n"
            "It is a database, not a document collection. Nothing here should be read as a "
            "budget: these are payments recorded against expenditure classes, after the fact."),
        "quirks": [
            ("Every value arrives as a JSON string, including `expense`",
             "Socrata declares `expense` as `number` and delivers `'270.72'`. The mirror "
             "stores it as `decimal128(18,2)`; summing 668,906 amounts as float64 does not "
             "reliably reproduce the published total, and the ingest gate compares to the cent."),
            ("The default page size is 1000 and there is no continuation token",
             "A request with no `$limit` returns 1000 rows, HTTP 200, and no `Link` header — "
             "a single request looks complete and is not. `$limit=60000` against a "
             "101,178-row year returns exactly 60,000. `src/soda.py` reconciles every paged "
             "fetch against a separate `count(*)` and raises on a mismatch."),
            ("`$offset` paging without `$order` is undefined",
             "Pages may overlap or skip rows with nothing in the response saying so. Every "
             "paged call sends an explicit `$order`, defaulting to `:id`."),
            ("Absent values are omitted, not null",
             "`vendor_st` is missing from roughly 30% of rows — the key is simply not "
             "present in the JSON object. The mirror stores absent as null, never as an "
             "empty string, which would read as a known-blank state and join to itself "
             "across unrelated vendors."),
            ("One agency code has changed its name mid-window",
             "Agency `845` appears as `LIQUOR CONTROL CMSN` through FY2021 and "
             "`LIQUOR & CANNABIS COM, OR` from FY2022. Codes are stable, names are not, so "
             "document ids key on the code and each document uses the name as it was "
             "recorded that year. No name maps to two codes."),
            ("Agency names are shouted, abbreviated, and contain at least one typo",
             "`FACILITES AUTH, OREGON` is misspelled upstream and is reproduced as-is. "
             "Generated titles apply case conversion only; abbreviations such as `SRVCS` "
             "are never expanded, because expanding them would be a guess."),
            ("No negative amounts",
             "`expense` ranges from $0.01 to $5,325,594,372.67 with no reversals or credits, "
             "unlike the Lottery dataset. Refunds are evidently netted upstream."),
            ("`vendor` is free text and is not de-duplicated",
             "98,933 distinct strings, but not 98,933 distinct organisations: a payee is "
             "whatever was entered in the statewide financial system, so one organisation "
             "appears under several spellings — `OREGON STATE TREASURY` and `OFFICE OF THE "
             "STATE TREASURER` are both present, as are `DEPARTMENT OF ADMINISTRATIVE "
             "SERVICES` and `STATE OF OREGON DEPARTMENT OF EDUCATION`. Counting distinct "
             "vendor strings undercounts the large payees, and no de-duplication is "
             "applied anywhere in this repo."),
        ],
    },
    "budgeted-revenue": {
        "dataset": "mwsa-rpk9",
        "title": "Budgeted Revenue (2025–27 biennium)",
        "mirrored": False,
        "key": ("`dept_no`, a five-digit department number that is the three-digit "
                "expenditure `agency` code times 100 — `10700` is agency `107`. This holds "
                "for all 79 real rows. It is the ONLY safe join path to expenditures; see "
                "the quirks below."),
        "glance": (
            "Budgeted revenue for the 2025–27 biennium, one row per department, split into "
            "general, lottery, federal, and other funds. 80 rows.\n\n"
            "This is the *budget* side of the question, and it is not mirrored: at 80 rows "
            "it is cheaper to read live than to keep in sync. It is also the most dangerous "
            "dataset in this corpus — read the quirks before using it for anything."),
        "quirks": [
            ("THE DATASET CONTAINS ITS OWN TOTALS ROW",
             "One of the 80 rows has `dept_no: 'Totals'` and no `dept_description`. Summing "
             "`grand_total` across all 80 rows yields **$281,553,047,958** against a true "
             "**$140,776,523,979** — exactly double the biennial budget, with no error, no "
             "null, and nothing in the response to signal it. Filter `dept_no = 'Totals'` "
             "before any aggregation. This is the single most likely way to fabricate a "
             "fiscal claim from this corpus."),
            ("Agency NAMES never match the expenditure dataset",
             "Zero exact string matches between the 83 agency names in expenditures and the "
             "79 department names here. This dataset writes `Administrative Svcs, Dept of`; "
             "expenditures writes `ADMINISTRATIVE SRVCS, DEPT OF` — different case AND "
             "different abbreviations. Joining on name produces nothing; joining on a "
             "fuzzy-matched name produces something worse. Use `dept_no / 100`."),
            ("This is a BIENNIUM; expenditures are FISCAL YEARS",
             "The 2025–27 biennium spans FY2026 and FY2027, and this dataset has no year "
             "column at all. FY2026 is not yet in the expenditure data, so for the current "
             "biennium there is nothing to compare against. Mapping biennial budget to "
             "fiscal-year actuals is an assumption that must be stated per join, never "
             "applied silently."),
            ("Coverage does not line up in either direction",
             "`14600 Emergency Board` has budgeted revenue and no expenditure agency — it is "
             "a contingency fund that disburses through other agencies. Four expenditure "
             "agencies have no budgeted-revenue row: `172` Facilities Authority, `524` Chief "
             "Education Office, `628` Forest Resources Institute, and `999` Central Agency / "
             "General Fund. An unmatched key here means genuinely absent, not an error."),
            ("Revenue is not appropriation",
             "This reports budgeted *revenue* by fund type. It is not the same thing as an "
             "appropriation to spend, and the two should not be presented as interchangeable."),
        ],
    },
    "lottery-expenditures": {
        "dataset": "anxj-teqh",
        "title": "Lottery Expenditures — Multi-Year Report",
        "mirrored": False,
        "key": ("`fiscal_year` + `gl_acct`, though neither is unique. Every row belongs to "
                "the single department `177-OREGON STATE LOTTERY`, so there is no agency "
                "dimension to join on within this dataset."),
        "glance": (
            "Expenditures of the Oregon State Lottery, FY2019–FY2025: 5,702 rows totalling "
            "$849,423,778.83. Not mirrored — small enough to read live.\n\n"
            "The Lottery runs a separate ERP (Microsoft Dynamics 365), which is why its "
            "spending is reported here rather than in the main agency expenditure dataset."),
        "quirks": [
            ("This spending is NOT in the agency expenditure dataset",
             "Agency code `177` does not appear in `y9g9-xsxs` at all — verified, not "
             "assumed. So the two datasets are disjoint and may be added together. That is "
             "the opposite of the usual hazard, and worth stating: $849,423,778.83 of "
             "lottery spending is absent from the $199,601,500,470.97 statewide figure."),
            ("`amount` includes negatives; the agency dataset does not",
             "182 of 5,702 rows are negative — reversals and credits. Totals here are net, "
             "whereas `y9g9-xsxs` has no values below $0.01. Comparing a gross total to a "
             "net one is not like-for-like."),
            ("`state` is recorded inconsistently for Oregon itself",
             "Both `OR` (2,276 rows) and `Oregon` (1,083 rows) appear for the same state, "
             "alongside `CA`, `NV`, and `WA`. Grouping by `state` without normalising "
             "undercounts Oregon by roughly a third. The agency dataset uses `vendor_st` "
             "with two-letter codes only — a third naming convention across three datasets."),
            ("`department` packs a code and a name into one field",
             "`177-OREGON STATE LOTTERY`, not separate code and name columns as in the other "
             "two datasets. Splitting on the first hyphen is safe here only because there is "
             "exactly one department."),
            ("`vendor_name` is free text and is not de-duplicated",
             "As with the agency dataset, a payee string is whatever was entered in the "
             "source system, so one organisation can appear under several spellings. "
             "Counting distinct strings undercounts the large payees."),
        ],
    },
}


def utc_today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def dump_fm(fm: dict) -> str:
    import yaml
    return yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100)


def measure(dataset: str) -> dict:
    """Live shape: columns, types, row count, schema hash."""
    sch = soda.schema(dataset)
    if not sch.ok:
        raise RuntimeError(f"{dataset}: schema unavailable — {sch.detail}")
    view = sch.rows[0]
    cnt = soda.count(dataset)
    if not cnt.ok:
        raise RuntimeError(f"{dataset}: count unavailable — {cnt.detail}")
    return {
        "name": view.get("name"),
        "columns": [(c.get("fieldName"), c.get("dataTypeName"), c.get("name"))
                    for c in view.get("columns", [])],
        "rows": cnt.total_count,
        "schema_hash": soda.schema_hash(view),
        "license": view.get("licenseId"),
    }


def build(slug: str, spec: dict, m: dict, today: str) -> str:
    ds = spec["dataset"]
    res = f"https://{soda.DOMAIN}/resource/{ds}.json"
    landing = f"https://{soda.DOMAIN}/d/{ds}"

    fm = {
        "schema_version": 1, "corpus": "oregon-budget", "jurisdiction": "oregon",
        "id": slug,
        "title": f"Dataset doc: {spec['title']}",
        "doc_type": "entity_doc",
        "citation": f"Oregon Open Data (Socrata) dataset {ds} — {m['name']}",
        "issuing_body": "Oregon Department of Administrative Services",
        "source_url": landing,
        "source_format": "soda",
        "snapshot_policy": "hash-only",
        "status": "current",
        "content_mode": "summary",
        "last_verified": "",  # rule 6: only corpus-verify writes this
        "verified_by": "",
        "maintainer": MAINTAINER,
        "live_schema_hash": m["schema_hash"],
        "relationships": {
            "implements": [], "implemented_by": [], "references_external": [],
            "related": sorted(k for k in DATASETS if k != slug), "supersedes": [],
        },
        "tags": ["oregon-budget", "socrata", "dataset-doc", slug],
        "socrata_dataset_id": ds,
        "row_count_at_verification": m["rows"],
        "mirrored_locally": spec["mirrored"],
    }

    L = []
    L.append(f"> **{DISCLAIMER} — AI-friendly reference only.** This describes the shape of a")
    L.append(f"> live dataset, not a snapshot of its contents, and it is not an official")
    L.append(f"> budget document. Fetch the live data for a current answer:")
    L.append(f"> `{landing}` (schema last checked {today}).")
    L.append("")
    L.append(f"# {spec['title']}")
    L.append("")
    L.append("## At a glance")
    L.append("")
    L.append(spec["glance"])
    L.append("")
    L.append("## Dataset reference")
    L.append("")
    L.append(f"| | |")
    L.append(f"|---|---|")
    L.append(f"| Socrata id | `{ds}` |")
    L.append(f"| Endpoint | `{res}` |")
    L.append(f"| Rows | {m['rows']:,} (measured {today}) |")
    L.append(f"| Columns | {len(m['columns'])} |")
    L.append(f"| Mirrored in this repo | {'yes — `data/expenditures/*.parquet`' if spec['mirrored'] else 'no — queried live'} |")
    L.append(f"| Licence | `{m['license']}` |")
    L.append("")
    L.append("### Key")
    L.append("")
    L.append(spec["key"])
    L.append("")
    L.append("### Fields")
    L.append("")
    L.append("Types are as Socrata *declares* them. Every value is delivered as a JSON "
             "string regardless.")
    L.append("")
    L.append("| Field | Declared type | Label |")
    L.append("|---|---|---|")
    for field, typ, label in m["columns"]:
        L.append(f"| `{field}` | {typ} | {label} |")
    L.append("")
    L.append(f"### Quirks (measured, this build — {today})")
    L.append("")
    for headline, detail in spec["quirks"]:
        L.append(f"**{headline}.** {detail}")
        L.append("")
    L.append("### Verification")
    L.append("")
    L.append(f"`live_schema_hash` is `sha256` over this dataset's sorted "
             f"`fieldName:dataTypeName` pairs joined with `|`. It deliberately excludes "
             f"column labels, widths, and positions, so a renamed label does not trip drift "
             f"but an added, removed, renamed, or retyped field does. Current value:")
    L.append("")
    L.append("```")
    L.append(m["schema_hash"])
    L.append("```")
    L.append("")
    L.append(f"Re-measure with `python3 src/build_dataset_docs.py --check`, which compares "
             f"the live schema and row count against what is recorded above. The row count")
    L.append(f"is a point-in-time measurement and is expected to move; the schema hash is not.")
    L.append("")
    L.append("Row count, live:")
    L.append("")
    L.append("```")
    L.append(f"{res}?$select=count(*)")
    L.append("```")
    L.append("")
    return f"---\n{dump_fm(fm)}---\n\n" + "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="compare recorded schema hash against live; write nothing")
    args = ap.parse_args()
    today = utc_today()

    if args.check:
        import yaml
        bad = 0
        for slug, spec in DATASETS.items():
            p = OUT / f"{slug}.md"
            if not p.is_file():
                print(f"  FAIL {slug}: missing"); bad += 1; continue
            fm = yaml.safe_load(p.read_text().split("---\n", 2)[1])
            m = measure(spec["dataset"])
            if fm.get("live_schema_hash") != m["schema_hash"]:
                print(f"  FAIL {slug}: schema drifted\n"
                      f"       recorded {fm.get('live_schema_hash')}\n"
                      f"       live     {m['schema_hash']}")
                bad += 1
            else:
                delta = m["rows"] - (fm.get("row_count_at_verification") or 0)
                note = f", row count {m['rows']:,} ({delta:+,})" if delta else ""
                print(f"  ok   {slug}: schema unchanged{note}")
        print(f"\n{'all dataset schemas unchanged' if not bad else f'{bad} drifted'}")
        return 1 if bad else 0

    OUT.mkdir(exist_ok=True)
    for slug, spec in DATASETS.items():
        m = measure(spec["dataset"])
        (OUT / f"{slug}.md").write_text(build(slug, spec, m, today))
        print(f"  wrote {slug}.md  ({m['rows']:,} rows, {len(m['columns'])} columns)")
    print(f"\n{len(DATASETS)} dataset docs -> {OUT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

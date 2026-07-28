#!/usr/bin/env python3
"""Mirror Agency Expenditures (y9g9-xsxs) to one Parquet file per fiscal year.

WHY PARQUET, NOT SQLITE: a denormalized SQLite of these 668,906 rows measures ~128 MB and
GitHub refuses files over 100 MB. Normalizing to fit would make the committed artifact a
*transformed* copy rather than a faithful one, and mirror-then-hash is the whole discipline
here. Parquet with dictionary encoding holds the source columns as delivered at ~1 MB/year.

WHY THE TYPES ARE WHAT THEY ARE (measured 2026-07-28):

    every column arrives as a JSON *string*, including `expense` ('270.72'), even though
    Socrata declares it `number`.

    expense: min 0.01, max 5,325,594,372.67, corpus sum 199,601,500,470.97

`expense` becomes decimal128(18,2) — NOT float64. Money through binary floating point
accumulates error that shows up exactly where it hurts most: an agency total that is off by
a few cents from the live API, in a corpus whose entire purpose is answering "what was
appropriated versus spent." Summing 668,906 float64 dollar amounts does not reliably
reproduce the published total; decimal does, exactly.

Codes (`agency`, `budget_class`, `expend_class`) stay strings. They are identifiers, not
quantities — nobody should be able to average an agency number — and string keys join
exactly. Measured: no leading zeros and no non-numeric values, so nothing is lost.

THE GATE: per year, the mirrored row count AND the summed expense must both equal a live
`count(*)` / `sum(expense)`. Row count alone would catch truncation but not a typing bug
that silently rounds; the sum catches both. Any mismatch raises and writes nothing.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from decimal import Decimal
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

sys.path.insert(0, str(Path(__file__).parent))
import soda  # noqa: E402

DATASET = "y9g9-xsxs"
OUT_DIR = Path(__file__).resolve().parent.parent / "data" / "expenditures"
MANIFEST = OUT_DIR / "manifest.json"

# Codes are identifiers; the paired *_1 columns are their labels. Dictionary encoding is
# made for this shape — 82 agencies and 138 budget classes repeating across 668k rows.
DICT_COLS = ["agency", "agency_1", "budget_class", "budget_class_1",
             "expend_class", "expend_class_1", "vendor", "vendor_st"]

SCHEMA = pa.schema([
    ("fiscal_year", pa.int16()),
    ("agency", pa.string()),
    ("agency_1", pa.string()),
    ("budget_class", pa.string()),
    ("budget_class_1", pa.string()),
    ("expend_class", pa.string()),
    ("expend_class_1", pa.string()),
    ("vendor", pa.string()),
    ("expense", pa.decimal128(18, 2)),
    ("vendor_st", pa.string()),      # measured ~30% null; the only nullable column
])


class ReconciliationError(RuntimeError):
    """Mirrored data disagrees with the live API. Fatal by design."""


def live_totals(year: str) -> tuple[int, Decimal]:
    """count(*) and sum(expense) for one year, straight from SODA."""
    where = soda.build_where(fiscal_year=year)
    r = soda.fetch(DATASET, {"$select": "count(*) AS n, sum(expense) AS total",
                             "$where": where})
    if not r.ok:
        raise ReconciliationError(f"could not read live totals for FY{year}: {r.detail}")
    row = r.rows[0]
    return int(row["n"]), Decimal(row["total"])


def to_table(rows: list) -> pa.Table:
    cols = {"fiscal_year": [int(r["fiscal_year"]) for r in rows],
            "expense": [Decimal(r["expense"]).quantize(Decimal("0.01")) for r in rows]}
    for c in DICT_COLS:
        # vendor_st is genuinely absent on ~30% of rows. Absent must stay null, not "" —
        # an empty string would read as a state that is known-blank rather than unrecorded,
        # and would quietly join to itself across unrelated vendors.
        cols[c] = [r.get(c) or None for r in rows]
    return pa.Table.from_pydict(cols, schema=SCHEMA)


def write_year(year: str, force: bool = False) -> dict:
    live_n, live_sum = live_totals(year)
    out = OUT_DIR / f"expenditures-{year}.parquet"

    if out.exists() and not force:
        t = pq.read_table(out)
        got = sum(t.column("expense").to_pylist())
        if t.num_rows == live_n and got == live_sum:
            print(f"  FY{year}  up to date ({live_n:,} rows)")
            return _entry(year, out, live_n, live_sum)
        print(f"  FY{year}  stale (have {t.num_rows:,}/{got}, live {live_n:,}/{live_sum}) — refetching")

    def progress(n, total):
        print(f"\r  FY{year}  {n:,}/{total:,}", end="", flush=True)

    res = soda.fetch_all(DATASET, where=soda.build_where(fiscal_year=year),
                         progress=progress)   # raises IncompleteFetch on a short read
    print()
    if not res.ok:
        raise ReconciliationError(f"FY{year} unavailable: {res.detail}")

    table = to_table(res.rows)

    # THE GATE. Both halves matter: rows catch truncation, the sum catches a typing or
    # rounding bug that would leave the count right and every total subtly wrong.
    got_sum = sum(table.column("expense").to_pylist())
    if table.num_rows != live_n:
        raise ReconciliationError(
            f"FY{year}: wrote {table.num_rows:,} rows, live count(*) says {live_n:,}")
    if got_sum != live_sum:
        raise ReconciliationError(
            f"FY{year}: mirrored sum {got_sum} != live sum {live_sum} "
            f"(delta {got_sum - live_sum}). The row count matched, so this is a typing or "
            f"rounding fault, not truncation — do not publish it.")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pq.write_table(table, out, compression="zstd", compression_level=9,
                   use_dictionary=DICT_COLS, version="2.6")
    print(f"  FY{year}  {table.num_rows:,} rows, ${live_sum:,} -> {out.name} "
          f"({out.stat().st_size / 1e6:.1f} MB)")
    return _entry(year, out, live_n, live_sum)


def _entry(year: str, path: Path, n: int, total: Decimal) -> dict:
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    return {"fiscal_year": year, "file": path.name, "rows": n, "sum_expense": str(total),
            "sha256": h, "bytes": path.stat().st_size}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--years", nargs="*", help="default: every year the dataset reports")
    ap.add_argument("--force", action="store_true", help="refetch even if reconciled")
    ap.add_argument("--check", action="store_true",
                    help="verify committed Parquet against live SODA; write nothing")
    args = ap.parse_args()

    years = args.years
    if not years:
        r = soda.fetch(DATASET, {"$select": "distinct fiscal_year"})
        if not r.ok:
            print(f"could not list fiscal years: {r.detail}", file=sys.stderr)
            return 2
        years = sorted(x["fiscal_year"] for x in r.rows)

    if args.check:
        return check(years)

    print(f"mirroring {DATASET} for {len(years)} fiscal years -> {OUT_DIR}")
    entries = [write_year(y, args.force) for y in years]

    total_rows = sum(e["rows"] for e in entries)
    total_sum = sum(Decimal(e["sum_expense"]) for e in entries)
    schema_res = soda.schema(DATASET)
    MANIFEST.write_text(json.dumps({
        "dataset": DATASET, "source": f"https://{soda.DOMAIN}/d/{DATASET}",
        "mirrored_at": soda._utc_now(),
        "live_schema_hash": soda.schema_hash(schema_res.rows[0]) if schema_res.ok else None,
        "total_rows": total_rows, "total_sum_expense": str(total_sum),
        "files": entries,
    }, indent=2) + "\n")
    print(f"\n{total_rows:,} rows, ${total_sum:,} across {len(entries)} files")
    print(f"manifest -> {MANIFEST}")
    return 0


def check(years) -> int:
    """CI gate: does what is committed still equal what the API reports?"""
    bad = 0
    for y in years:
        p = OUT_DIR / f"expenditures-{y}.parquet"
        if not p.exists():
            print(f"  FAIL FY{y}: {p.name} missing"); bad += 1; continue
        live_n, live_sum = live_totals(y)
        t = pq.read_table(p)
        got = sum(t.column("expense").to_pylist())
        if t.num_rows == live_n and got == live_sum:
            print(f"  ok   FY{y}  {live_n:,} rows, ${live_sum:,}")
        else:
            print(f"  FAIL FY{y}: have {t.num_rows:,}/${got:,}, live {live_n:,}/${live_sum:,}")
            bad += 1
    print(f"\n{'all years reconcile' if not bad else f'{bad} year(s) out of sync'}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())

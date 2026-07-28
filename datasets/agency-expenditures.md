---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: agency-expenditures
title: 'Dataset doc: Agency Expenditures — Multi-Year Report'
doc_type: entity_doc
citation: Oregon Open Data (Socrata) dataset y9g9-xsxs — Agency Expenditures – Multi-Year Report
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: '2026-07-28'
verified_by: '@dzinck'
maintainer: '@dzinck'
live_schema_hash: 3d5ab79dfc275effffbfaf9c7925f22913dfb650ffa57f27c835a376773aac67
relationships:
  implements: []
  implemented_by: []
  references_external: []
  related:
  - budgeted-revenue
  - lottery-expenditures
  supersedes: []
tags:
- oregon-budget
- socrata
- dataset-doc
- agency-expenditures
socrata_dataset_id: y9g9-xsxs
row_count_at_verification: 668906
mirrored_locally: true
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** This describes the shape of a
> live dataset, not a snapshot of its contents, and it is not an official
> budget document. Fetch the live data for a current answer:
> `https://data.oregon.gov/d/y9g9-xsxs` (schema last checked 2026-07-28).

# Agency Expenditures — Multi-Year Report

## At a glance

Vendor-level expenditure transactions for Oregon state agencies, FY2019–FY2025. This is the spending half of the appropriation-versus-actuals question, and the only one of the three datasets mirrored in full — 668,906 rows totalling $199,601,500,470.97, committed as one Parquet file per fiscal year.

It is a database, not a document collection. Nothing here should be read as a budget: these are payments recorded against expenditure classes, after the fact.

## Dataset reference

| | |
|---|---|
| Socrata id | `y9g9-xsxs` |
| Endpoint | `https://data.oregon.gov/resource/y9g9-xsxs.json` |
| Rows | 668,906 (measured 2026-07-28) |
| Columns | 10 |
| Mirrored in this repo | yes — `data/expenditures/*.parquet` |
| Licence | `USGOV_WORKS` |

### Key

`agency` + `fiscal_year`. Neither is unique alone, and there is no row identifier beyond Socrata's synthetic `:id`. The corpus mirrors this dataset to Parquet and derives one document per `(agency, fiscal_year)` pair — 544 of them, the grain the budget question is actually asked at.

### Fields

Types are as Socrata *declares* them. Every value is delivered as a JSON string regardless.

| Field | Declared type | Label |
|---|---|---|
| `fiscal_year` | number | FISCAL YEAR |
| `agency` | number | AGENCY # |
| `agency_1` | text | AGENCY |
| `budget_class` | number | BUDGET CLASS # |
| `budget_class_1` | text | BUDGET CLASS |
| `expend_class` | number | EXPEND CLASS # |
| `expend_class_1` | text | EXPEND CLASS |
| `vendor` | text | VENDOR |
| `expense` | number | EXPENSE |
| `vendor_st` | text | VENDOR ST |

### Quirks (measured, this build — 2026-07-28)

**Every value arrives as a JSON string, including `expense`.** Socrata declares `expense` as `number` and delivers `'270.72'`. The mirror stores it as `decimal128(18,2)`; summing 668,906 amounts as float64 does not reliably reproduce the published total, and the ingest gate compares to the cent.

**The default page size is 1000 and there is no continuation token.** A request with no `$limit` returns 1000 rows, HTTP 200, and no `Link` header — a single request looks complete and is not. `$limit=60000` against a 101,178-row year returns exactly 60,000. `src/soda.py` reconciles every paged fetch against a separate `count(*)` and raises on a mismatch.

**`$offset` paging without `$order` is undefined.** Pages may overlap or skip rows with nothing in the response saying so. Every paged call sends an explicit `$order`, defaulting to `:id`.

**Absent values are omitted, not null.** `vendor_st` is missing from roughly 30% of rows — the key is simply not present in the JSON object. The mirror stores absent as null, never as an empty string, which would read as a known-blank state and join to itself across unrelated vendors.

**One agency code has changed its name mid-window.** Agency `845` appears as `LIQUOR CONTROL CMSN` through FY2021 and `LIQUOR & CANNABIS COM, OR` from FY2022. Codes are stable, names are not, so document ids key on the code and each document uses the name as it was recorded that year. No name maps to two codes.

**Agency names are shouted, abbreviated, and contain at least one typo.** `FACILITES AUTH, OREGON` is misspelled upstream and is reproduced as-is. Generated titles apply case conversion only; abbreviations such as `SRVCS` are never expanded, because expanding them would be a guess.

**No negative amounts.** `expense` ranges from $0.01 to $5,325,594,372.67 with no reversals or credits, unlike the Lottery dataset. Refunds are evidently netted upstream.

### Verification

`live_schema_hash` is `sha256` over this dataset's sorted `fieldName:dataTypeName` pairs joined with `|`. It deliberately excludes column labels, widths, and positions, so a renamed label does not trip drift but an added, removed, renamed, or retyped field does. Current value:

```
3d5ab79dfc275effffbfaf9c7925f22913dfb650ffa57f27c835a376773aac67
```

Re-measure with `python3 src/build_dataset_docs.py --check`, which compares the live schema and row count against what is recorded above. The row count
is a point-in-time measurement and is expected to move; the schema hash is not.

Row count, live:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=count(*)
```

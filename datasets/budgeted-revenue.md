---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: budgeted-revenue
title: 'Dataset doc: Budgeted Revenue (2025–27 biennium)'
doc_type: entity_doc
citation: Oregon Open Data (Socrata) dataset mwsa-rpk9 — Budgeted Revenue
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/mwsa-rpk9
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: ''
verified_by: ''
maintainer: '@dzinck'
live_schema_hash: aa793e77813bcff98cb6c3f0a219c9686faad0e3225a104986a55c9067faef49
relationships:
  implements: []
  implemented_by: []
  references_external: []
  related:
  - agency-expenditures
  - lottery-expenditures
  supersedes: []
tags:
- oregon-budget
- socrata
- dataset-doc
- budgeted-revenue
socrata_dataset_id: mwsa-rpk9
row_count_at_verification: 80
mirrored_locally: false
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** This describes the shape of a
> live dataset, not a snapshot of its contents, and it is not an official
> budget document. Fetch the live data for a current answer:
> `https://data.oregon.gov/d/mwsa-rpk9` (schema last checked 2026-07-28).

# Budgeted Revenue (2025–27 biennium)

## At a glance

Budgeted revenue for the 2025–27 biennium, one row per department, split into general, lottery, federal, and other funds. 80 rows.

This is the *budget* side of the question, and it is not mirrored: at 80 rows it is cheaper to read live than to keep in sync. It is also the most dangerous dataset in this corpus — read the quirks before using it for anything.

## Dataset reference

| | |
|---|---|
| Socrata id | `mwsa-rpk9` |
| Endpoint | `https://data.oregon.gov/resource/mwsa-rpk9.json` |
| Rows | 80 (measured 2026-07-28) |
| Columns | 7 |
| Mirrored in this repo | no — queried live |
| Licence | `USGOV_WORKS` |

### Key

`dept_no`, a five-digit department number that is the three-digit expenditure `agency` code times 100 — `10700` is agency `107`. This holds for all 79 real rows. It is the ONLY safe join path to expenditures; see the quirks below.

### Fields

Types are as Socrata *declares* them. Every value is delivered as a JSON string regardless.

| Field | Declared type | Label |
|---|---|---|
| `dept_description` | text | Agency |
| `dept_no` | text | Agency # |
| `federal_funds` | number | Federal Funds |
| `general_funds` | number | General Funds |
| `lottery_funds` | number | Lottery Funds |
| `other_funds` | number | Other Funds |
| `grand_total` | number | Total |

### Quirks (measured, this build — 2026-07-28)

**THE DATASET CONTAINS ITS OWN TOTALS ROW.** One of the 80 rows has `dept_no: 'Totals'` and no `dept_description`. Summing `grand_total` across all 80 rows yields **$281,553,047,958** against a true **$140,776,523,979** — exactly double the biennial budget, with no error, no null, and nothing in the response to signal it. Filter `dept_no = 'Totals'` before any aggregation. This is the single most likely way to fabricate a fiscal claim from this corpus.

**Agency NAMES never match the expenditure dataset.** Zero exact string matches between the 83 agency names in expenditures and the 79 department names here. This dataset writes `Administrative Svcs, Dept of`; expenditures writes `ADMINISTRATIVE SRVCS, DEPT OF` — different case AND different abbreviations. Joining on name produces nothing; joining on a fuzzy-matched name produces something worse. Use `dept_no / 100`.

**This is a BIENNIUM; expenditures are FISCAL YEARS.** The 2025–27 biennium spans FY2026 and FY2027, and this dataset has no year column at all. FY2026 is not yet in the expenditure data, so for the current biennium there is nothing to compare against. Mapping biennial budget to fiscal-year actuals is an assumption that must be stated per join, never applied silently.

**Coverage does not line up in either direction.** `14600 Emergency Board` has budgeted revenue and no expenditure agency — it is a contingency fund that disburses through other agencies. Four expenditure agencies have no budgeted-revenue row: `172` Facilities Authority, `524` Chief Education Office, `628` Forest Resources Institute, and `999` Central Agency / General Fund. An unmatched key here means genuinely absent, not an error.

**Revenue is not appropriation.** This reports budgeted *revenue* by fund type. It is not the same thing as an appropriation to spend, and the two should not be presented as interchangeable.

### Verification

`live_schema_hash` is `sha256` over this dataset's sorted `fieldName:dataTypeName` pairs joined with `|`. It deliberately excludes column labels, widths, and positions, so a renamed label does not trip drift but an added, removed, renamed, or retyped field does. Current value:

```
aa793e77813bcff98cb6c3f0a219c9686faad0e3225a104986a55c9067faef49
```

Re-measure with `python3 src/build_dataset_docs.py --check`, which compares the live schema and row count against what is recorded above. The row count
is a point-in-time measurement and is expected to move; the schema hash is not.

Row count, live:

```
https://data.oregon.gov/resource/mwsa-rpk9.json?$select=count(*)
```

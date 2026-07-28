---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: lottery-expenditures
title: 'Dataset doc: Lottery Expenditures — Multi-Year Report'
doc_type: entity_doc
citation: Oregon Open Data (Socrata) dataset anxj-teqh — Lottery Expenditures - Multi-Year Report
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/anxj-teqh
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: '2026-07-28'
verified_by: '@dzinck'
maintainer: '@dzinck'
live_schema_hash: bdaef962f7dfdab21b33c00fd016c693400cd7a0df71a3d5c58b7e3d5bc9228d
relationships:
  implements: []
  implemented_by: []
  references_external: []
  related:
  - agency-expenditures
  - budgeted-revenue
  supersedes: []
tags:
- oregon-budget
- socrata
- dataset-doc
- lottery-expenditures
socrata_dataset_id: anxj-teqh
row_count_at_verification: 5702
mirrored_locally: false
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** This describes the shape of a
> live dataset, not a snapshot of its contents, and it is not an official
> budget document. Fetch the live data for a current answer:
> `https://data.oregon.gov/d/anxj-teqh` (schema last checked 2026-07-28).

# Lottery Expenditures — Multi-Year Report

## At a glance

Expenditures of the Oregon State Lottery, FY2019–FY2025: 5,702 rows totalling $849,423,778.83. Not mirrored — small enough to read live.

The Lottery runs a separate ERP (Microsoft Dynamics 365), which is why its spending is reported here rather than in the main agency expenditure dataset.

## Dataset reference

| | |
|---|---|
| Socrata id | `anxj-teqh` |
| Endpoint | `https://data.oregon.gov/resource/anxj-teqh.json` |
| Rows | 5,702 (measured 2026-07-28) |
| Columns | 7 |
| Mirrored in this repo | no — queried live |
| Licence | `USGOV_WORKS` |

### Key

`fiscal_year` + `gl_acct`, though neither is unique. Every row belongs to the single department `177-OREGON STATE LOTTERY`, so there is no agency dimension to join on within this dataset.

### Fields

Types are as Socrata *declares* them. Every value is delivered as a JSON string regardless.

| Field | Declared type | Label |
|---|---|---|
| `fiscal_year` | number | Fiscal Year |
| `department` | text | Department |
| `acct_name` | text | Acct Name |
| `amount` | number | Amount |
| `vendor_name` | text | Vendor Name |
| `state` | text | State |
| `gl_acct` | number | GL Acct |

### Quirks (measured, this build — 2026-07-28)

**This spending is NOT in the agency expenditure dataset.** Agency code `177` does not appear in `y9g9-xsxs` at all — verified, not assumed. So the two datasets are disjoint and may be added together. That is the opposite of the usual hazard, and worth stating: $849,423,778.83 of lottery spending is absent from the $199,601,500,470.97 statewide figure.

**`amount` includes negatives; the agency dataset does not.** 182 of 5,702 rows are negative — reversals and credits. Totals here are net, whereas `y9g9-xsxs` has no values below $0.01. Comparing a gross total to a net one is not like-for-like.

**`state` is recorded inconsistently for Oregon itself.** Both `OR` (2,276 rows) and `Oregon` (1,083 rows) appear for the same state, alongside `CA`, `NV`, and `WA`. Grouping by `state` without normalising undercounts Oregon by roughly a third. The agency dataset uses `vendor_st` with two-letter codes only — a third naming convention across three datasets.

**`department` packs a code and a name into one field.** `177-OREGON STATE LOTTERY`, not separate code and name columns as in the other two datasets. Splitting on the first hyphen is safe here only because there is exactly one department.

**Vendor names are individuals in some rows.** As with the agency dataset, `vendor_name` includes people. This corpus does not republish vendor-level detail as indexed text; see the note in any `expenditures/*.md` document.

### Verification

`live_schema_hash` is `sha256` over this dataset's sorted `fieldName:dataTypeName` pairs joined with `|`. It deliberately excludes column labels, widths, and positions, so a renamed label does not trip drift but an added, removed, renamed, or retyped field does. Current value:

```
bdaef962f7dfdab21b33c00fd016c693400cd7a0df71a3d5c58b7e3d5bc9228d
```

Re-measure with `python3 src/build_dataset_docs.py --check`, which compares the live schema and row count against what is recorded above. The row count
is a point-in-time measurement and is expected to move; the schema hash is not.

Row count, live:

```
https://data.oregon.gov/resource/anxj-teqh.json?$select=count(*)
```

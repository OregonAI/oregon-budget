---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-196-fy2025
title: Dist Attorneys/Deputies — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 196, FY2025
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5e9f0c30287913ac0bfff8d74a1225d0c2816ca6a307f2141ebb35602c5a91ed
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: '2026-07-28'
verified_by: '@dzinck'
maintainer: '@dzinck'
conversion_notes: Title is the source agency name title-cased for reading; the verbatim string is `agency_name`.
  Abbreviations are not expanded. Figures are aggregated, not extracted text.
relationships:
  implements: []
  implemented_by: []
  references_external: []
  related:
  - expenditures-196-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-196
- dist-attorneys-deputies
agency_code: '196'
agency_name: DIST ATTORNEYS/DEPUTIES
fiscal_year: 2025
total_expense: '1641970.27'
transaction_count: 16
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dist Attorneys/Deputies — FY2025 expenditures

## At a glance

Dist Attorneys/Deputies (agency code 196, recorded upstream as `DIST ATTORNEYS/DEPUTIES`) spent **$1,641,970.27** in fiscal year 2025, across 16 transaction records. That is up 66.1% from $988,345.42 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **56 of 80** agencies reporting that year.

The largest budget category was **Distribution To Counties** at $1,000,000.00 (60.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6020 | Distribution To Counties | $1,000,000.00 | 60.9% | 6 |
| 4225 | State Government Service Charges | $594,367.50 | 36.2% | 4 |
| 4300 | Professional Services | $46,808.00 | 2.9% | 2 |
| 4325 | Attorney General Legal Fees | $495.00 | 0.0% | 1 |
| 4650 | Other Services And Supplies | $134.17 | 0.0% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $131.04 | 0.0% | 1 |
| 3220 | Public Employes' Retirement System | $34.56 | 0.0% | 1 |

## Largest expenditure classes

The 7 largest of 7 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6300 | Distribution To Counties | $1,000,000.00 | 60.9% |
| 4600 | State Government Service Charges | $594,367.50 | 36.2% |
| 4500 | Professional Services Non-It | $46,808.00 | 2.9% |
| 4550 | Attorney General Legal Fees | $495.00 | 0.0% |
| 4701 | Other Services | $134.17 | 0.0% |
| 4975 | Agency Program Related Services | $131.04 | 0.0% |
| 3210 | Public Employees Retirement Contribution | $34.56 | 0.0% |

## Curator notes

Figures are aggregated from 16 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='196' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


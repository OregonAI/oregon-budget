---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-144-fy2024
title: Legislative Rev Office — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 144, FY2024
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: decef95a644d748f5c62eca57f2ec65a1ac01802ec192ae6fe9a4da7eed2a7c0
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
  - expenditures-144-fy2023
  - expenditures-144-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-144
- legislative-rev-office
agency_code: '144'
agency_name: LEGISLATIVE REV OFFICE
fiscal_year: 2024
total_expense: '70775.20'
transaction_count: 38
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Rev Office — FY2024 expenditures

## At a glance

Legislative Rev Office (agency code 144, recorded upstream as `LEGISLATIVE REV OFFICE`) spent **$70,775.20** in fiscal year 2024, across 38 transaction records. That is up 9.0% from $64,934.50 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **77 of 80** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $24,118.94 (34.1% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $24,118.94 | 34.1% | 3 |
| 4715 | It Expendable Property | $18,359.37 | 25.9% | 4 |
| 4300 | Professional Services | $10,500.00 | 14.8% | 1 |
| 4175 | Office Expenses | $7,002.39 | 9.9% | 9 |
| 4400 | Dues And Subscriptions | $5,604.42 | 7.9% | 4 |
| 4150 | Employee Training | $3,884.95 | 5.5% | 14 |
| 4650 | Other Services And Supplies | $827.64 | 1.2% | 2 |
| 4250 | Data Processing | $477.49 | 0.7% | 1 |

## Largest expenditure classes

The 12 largest of 19 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $24,118.94 | 34.1% |
| 4366 | Computer Technology Pc Software<$5K | $14,841.19 | 21.0% |
| 4500 | Professional Services Non-It | $10,500.00 | 14.8% |
| 4251 | Subscriptions And Publications | $5,604.42 | 7.9% |
| 4201 | Office Services | $3,667.72 | 5.2% |
| 4365 | Computer Technology Pc Equipment<$5K | $3,518.18 | 5.0% |
| 4202 | Equipment Rental | $2,669.04 | 3.8% |
| 4440 | Prof Dev Out-Of-State Air Transportation | $971.21 | 1.4% |
| 4434 | Prof Dev Out-Of-State Lodging | $888.58 | 1.3% |
| 4433 | Prof Dev Instate Lodging | $850.83 | 1.2% |
| 4704 | Other Supplies | $827.64 | 1.2% |
| 4200 | Office Supplies | $665.63 | 0.9% |

## Curator notes

Figures are aggregated from 38 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='144' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


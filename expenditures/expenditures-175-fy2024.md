---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-175-fy2024
title: Judicial Fitness & Disability — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 175, FY2024
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
  - expenditures-175-fy2023
  - expenditures-175-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-175
- judicial-fitness-disability
agency_code: '175'
agency_name: JUDICIAL FITNESS & DISABILITY
fiscal_year: 2024
total_expense: '68038.35'
transaction_count: 35
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Judicial Fitness & Disability — FY2024 expenditures

## At a glance

Judicial Fitness & Disability (agency code 175, recorded upstream as `JUDICIAL FITNESS & DISABILITY`) spent **$68,038.35** in fiscal year 2024, across 35 transaction records. That is up 101.8% from $33,712.40 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **78 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $26,993.57 (39.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $26,993.57 | 39.7% | 9 |
| 4175 | Office Expenses | $16,150.13 | 23.7% | 4 |
| 4225 | State Government Service Charges | $8,277.87 | 12.2% | 4 |
| 4425 | Lease Payments & Taxes | $6,050.00 | 8.9% | 1 |
| 4150 | Employee Training | $5,198.04 | 7.6% | 6 |
| 4400 | Dues And Subscriptions | $3,490.00 | 5.1% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $944.48 | 1.4% | 3 |
| 4715 | It Expendable Property | $624.12 | 0.9% | 1 |
| 4100 | Instate Travel | $306.52 | 0.5% | 2 |
| 4650 | Other Services And Supplies | $3.62 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 17 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $26,993.57 | 39.7% |
| 4201 | Office Services | $15,555.88 | 22.9% |
| 4600 | State Government Service Charges | $8,277.87 | 12.2% |
| 4804 | Other Lease Payments | $6,050.00 | 8.9% |
| 4250 | Dues/Memberships | $3,438.00 | 5.1% |
| 4434 | Prof Dev Out-Of-State Lodging | $1,841.29 | 2.7% |
| 4440 | Prof Dev Out-Of-State Air Transportation | $1,705.61 | 2.5% |
| 4411 | Prof Dev Out-Of-State Tuition/Regist | $1,050.00 | 1.5% |
| 4301 | Telecom/Voice Usage | $777.93 | 1.1% |
| 4366 | Computer Technology Pc Software<$5K | $624.12 | 0.9% |
| 4200 | Office Supplies | $594.25 | 0.9% |
| 4432 | Prof Dev Out-Of-State Meal W/Overnite | $533.25 | 0.8% |

## Curator notes

Figures are aggregated from 35 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='175' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


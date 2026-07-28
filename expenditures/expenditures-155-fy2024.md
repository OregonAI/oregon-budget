---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-155-fy2024
title: Legislative Assembly — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 155, FY2024
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
  - expenditures-155-fy2023
  - expenditures-155-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-155
- legislative-assembly
agency_code: '155'
agency_name: LEGISLATIVE ASSEMBLY
fiscal_year: 2024
total_expense: '3552639.69'
transaction_count: 493
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Assembly — FY2024 expenditures

## At a glance

Legislative Assembly (agency code 155, recorded upstream as `LEGISLATIVE ASSEMBLY`) spent **$3,552,639.69** in fiscal year 2024, across 493 transaction records. That is up 42.1% from $2,499,927.93 in FY2023. The agency accounts for 0.01% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **49 of 80** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $1,219,852.35 (34.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $1,219,852.35 | 34.3% | 4 |
| 4650 | Other Services And Supplies | $985,820.84 | 27.7% | 51 |
| 4175 | Office Expenses | $463,712.09 | 13.1% | 57 |
| 4275 | Publicity & Publications | $294,479.08 | 8.3% | 18 |
| 4300 | Professional Services | $174,359.61 | 4.9% | 6 |
| 4150 | Employee Training | $115,501.00 | 3.3% | 157 |
| 3240 | Unemployment Assessment | $111,840.17 | 3.1% | 1 |
| 4715 | It Expendable Property | $63,530.96 | 1.8% | 9 |
| 4125 | Out-Of-State Travel | $47,913.61 | 1.3% | 67 |
| 4100 | Instate Travel | $26,601.09 | 0.7% | 61 |
| 4425 | Lease Payments & Taxes | $19,684.85 | 0.6% | 17 |
| 4400 | Dues And Subscriptions | $8,145.59 | 0.2% | 28 |
| 4700 | Expendable Property $250-$5000 | $7,470.97 | 0.2% | 7 |
| 5200 | Technical Equipment | $7,100.00 | 0.2% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $2,800.30 | 0.1% | 4 |
| 4250 | Data Processing | $1,719.63 | 0.0% | 1 |
| 4500 | Food And Kitchen Supplies | $1,213.05 | 0.0% | 1 |
| 4325 | Attorney General Legal Fees | $599.50 | 0.0% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $215.00 | 0.0% | 1 |
| 4375 | Employee Recruitment And Development | $80.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 52 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $1,219,852.35 | 34.3% |
| 4701 | Other Services | $980,402.91 | 27.6% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $294,479.08 | 8.3% |
| 4200 | Office Supplies | $255,233.09 | 7.2% |
| 4201 | Office Services | $201,946.79 | 5.7% |
| 4500 | Professional Services Non-It | $174,359.61 | 4.9% |
| 3231 | Unemployment Compensation & Assessment | $111,840.17 | 3.1% |
| 4365 | Computer Technology Pc Equipment<$5K | $49,993.90 | 1.4% |
| 4440 | Prof Dev Out-Of-State Air Transportation | $28,607.64 | 0.8% |
| 4434 | Prof Dev Out-Of-State Lodging | $28,581.35 | 0.8% |
| 4411 | Prof Dev Out-Of-State Tuition/Regist | $27,019.94 | 0.8% |
| 4159 | Out-Of-State Air Transportation | $23,892.70 | 0.7% |

## Curator notes

Figures are aggregated from 493 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='155' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


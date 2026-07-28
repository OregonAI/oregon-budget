---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-155-fy2025
title: Legislative Assembly — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 155, FY2025
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
  - expenditures-155-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-155
- legislative-assembly
agency_code: '155'
agency_name: LEGISLATIVE ASSEMBLY
fiscal_year: 2025
total_expense: '2744716.16'
transaction_count: 538
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Assembly — FY2025 expenditures

## At a glance

Legislative Assembly (agency code 155, recorded upstream as `LEGISLATIVE ASSEMBLY`) spent **$2,744,716.16** in fiscal year 2025, across 538 transaction records. That is down 22.7% from $3,552,639.69 in FY2024. The agency accounts for 0.01% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **49 of 80** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $1,199,250.92 (43.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $1,199,250.92 | 43.7% | 5 |
| 4175 | Office Expenses | $567,856.15 | 20.7% | 62 |
| 4300 | Professional Services | $259,460.21 | 9.5% | 9 |
| 4715 | It Expendable Property | $178,494.26 | 6.5% | 13 |
| 4150 | Employee Training | $110,475.88 | 4.0% | 123 |
| 4650 | Other Services And Supplies | $100,467.73 | 3.7% | 81 |
| 3240 | Unemployment Assessment | $72,619.98 | 2.6% | 1 |
| 4425 | Lease Payments & Taxes | $64,201.80 | 2.3% | 18 |
| 4100 | Instate Travel | $42,403.14 | 1.5% | 113 |
| 4500 | Food And Kitchen Supplies | $41,611.85 | 1.5% | 3 |
| 4125 | Out-Of-State Travel | $25,817.64 | 0.9% | 51 |
| 4275 | Publicity & Publications | $19,344.39 | 0.7% | 6 |
| 4250 | Data Processing | $18,409.54 | 0.7% | 2 |
| 4700 | Expendable Property $250-$5000 | $15,284.86 | 0.6% | 9 |
| 5100 | Office Furniture And Fixtures | $9,718.00 | 0.4% | 1 |
| 4400 | Dues And Subscriptions | $9,474.91 | 0.3% | 29 |
| 4575 | Agency Program Related Svcs & Supp | $7,611.19 | 0.3% | 6 |
| 4200 | Telecomm/Tech Svc And Supplies | $1,927.51 | 0.1% | 5 |
| 4375 | Employee Recruitment And Development | $286.20 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 53 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $1,199,250.92 | 43.7% |
| 4200 | Office Supplies | $288,169.55 | 10.5% |
| 4201 | Office Services | $267,015.12 | 9.7% |
| 4500 | Professional Services Non-It | $259,460.21 | 9.5% |
| 4365 | Computer Technology Pc Equipment<$5K | $167,471.92 | 6.1% |
| 4701 | Other Services | $81,895.00 | 3.0% |
| 3231 | Unemployment Compensation & Assessment | $72,619.98 | 2.6% |
| 4800 | Interagency Lease Payments | $64,201.80 | 2.3% |
| 4875 | Food And Kitchen Supplies | $41,611.85 | 1.5% |
| 4434 | Prof Dev Out-Of-State Lodging | $34,199.32 | 1.2% |
| 4411 | Prof Dev Out-Of-State Tuition/Regist | $28,783.85 | 1.0% |
| 4440 | Prof Dev Out-Of-State Air Transportation | $22,395.25 | 0.8% |

## Curator notes

Figures are aggregated from 538 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='155' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


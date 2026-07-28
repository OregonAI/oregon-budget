---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-628-fy2024
title: Forest Resources Inst, OR — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 628, FY2024
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
  - expenditures-628-fy2023
  - expenditures-628-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-628
- forest-resources-inst-or
agency_code: '628'
agency_name: FOREST RESOURCES INST, OR
fiscal_year: 2024
total_expense: '2480760.35'
transaction_count: 211
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Forest Resources Inst, OR — FY2024 expenditures

## At a glance

Forest Resources Inst, OR (agency code 628, recorded upstream as `FOREST RESOURCES INST, OR`) spent **$2,480,760.35** in fiscal year 2024, across 211 transaction records. That is down 7.6% from $2,685,920.74 in FY2023. The agency accounts for 0.01% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **51 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $1,370,832.34 (55.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $1,370,832.34 | 55.3% | 19 |
| 4275 | Publicity & Publications | $577,834.82 | 23.3% | 14 |
| 4575 | Agency Program Related Svcs & Supp | $200,265.66 | 8.1% | 84 |
| 4425 | Lease Payments & Taxes | $111,315.19 | 4.5% | 11 |
| 4315 | It Professional Services | $95,591.50 | 3.9% | 2 |
| 4100 | Instate Travel | $33,861.94 | 1.4% | 40 |
| 4175 | Office Expenses | $23,908.10 | 1.0% | 8 |
| 4715 | It Expendable Property | $19,315.18 | 0.8% | 6 |
| 4200 | Telecomm/Tech Svc And Supplies | $13,838.40 | 0.6% | 3 |
| 4225 | State Government Service Charges | $8,131.54 | 0.3% | 4 |
| 4500 | Food And Kitchen Supplies | $7,402.06 | 0.3% | 1 |
| 4125 | Out-Of-State Travel | $6,633.72 | 0.3% | 9 |
| 4400 | Dues And Subscriptions | $5,446.48 | 0.2% | 2 |
| 4650 | Other Services And Supplies | $2,593.90 | 0.1% | 2 |
| 3110 | Class/Unclass Salary & Per Diem | $1,350.00 | 0.1% | 1 |
| 4325 | Attorney General Legal Fees | $1,255.10 | 0.1% | 1 |
| 4150 | Employee Training | $485.00 | 0.0% | 2 |
| 4375 | Employee Recruitment And Development | $400.00 | 0.0% | 1 |
| 4250 | Data Processing | $299.42 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 43 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4505 | Professional Services Non-It>$75K | $1,166,486.23 | 47.0% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $577,834.82 | 23.3% |
| 4500 | Professional Services Non-It | $204,346.11 | 8.2% |
| 4975 | Agency Program Related Services | $183,762.66 | 7.4% |
| 4800 | Interagency Lease Payments | $111,315.19 | 4.5% |
| 4516 | Professional Services Servers | $95,591.50 | 3.9% |
| 4206 | Catering Services | $14,538.19 | 0.6% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $13,156.77 | 0.5% |
| 4108 | Instate Ground Transportation | $8,888.62 | 0.4% |
| 4366 | Computer Technology Pc Software<$5K | $8,853.51 | 0.4% |
| 4200 | Office Supplies | $8,464.99 | 0.3% |
| 4600 | State Government Service Charges | $8,131.54 | 0.3% |

## Curator notes

Figures are aggregated from 211 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='628' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


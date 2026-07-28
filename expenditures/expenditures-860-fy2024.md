---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-860-fy2024
title: Public Utility Cmsn — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 860, FY2024
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
  - expenditures-860-fy2023
  - expenditures-860-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-860
- public-utility-cmsn
agency_code: '860'
agency_name: PUBLIC UTILITY CMSN
fiscal_year: 2024
total_expense: '37399129.28'
transaction_count: 434
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Public Utility Cmsn — FY2024 expenditures

## At a glance

Public Utility Cmsn (agency code 860, recorded upstream as `PUBLIC UTILITY CMSN`) spent **$37,399,129.28** in fiscal year 2024, across 434 transaction records. That is up 3.7% from $36,050,837.37 in FY2023. The agency accounts for 0.12% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **31 of 80** agencies reporting that year.

The largest budget category was **Distribution To Non-Governments** at $27,179,925.56 (72.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6030 | Distribution To Non-Governments | $27,179,925.56 | 72.7% | 31 |
| 4575 | Agency Program Related Svcs & Supp | $2,887,802.17 | 7.7% | 48 |
| 4325 | Attorney General Legal Fees | $2,383,204.21 | 6.4% | 2 |
| 4300 | Professional Services | $1,278,739.81 | 3.4% | 24 |
| 4425 | Lease Payments & Taxes | $1,217,474.21 | 3.3% | 6 |
| 4225 | State Government Service Charges | $700,907.72 | 1.9% | 5 |
| 4715 | It Expendable Property | $354,389.26 | 0.9% | 11 |
| 4250 | Data Processing | $305,648.83 | 0.8% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $227,252.53 | 0.6% | 12 |
| 4175 | Office Expenses | $213,833.22 | 0.6% | 17 |
| 4315 | It Professional Services | $140,834.25 | 0.4% | 4 |
| 4400 | Dues And Subscriptions | $127,140.60 | 0.3% | 14 |
| 4100 | Instate Travel | $121,287.49 | 0.3% | 51 |
| 4650 | Other Services And Supplies | $94,292.39 | 0.3% | 22 |
| 4125 | Out-Of-State Travel | $60,673.56 | 0.2% | 107 |
| 4150 | Employee Training | $48,475.30 | 0.1% | 60 |
| 4275 | Publicity & Publications | $22,229.66 | 0.1% | 7 |
| 5550 | Data Processing Software | $18,919.39 | 0.1% | 1 |
| 4475 | Facilities Maintenance | $8,737.87 | 0.0% | 4 |
| 6055 | Distribution To Contract Svc Provider | $6,087.06 | 0.0% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $734.19 | 0.0% | 1 |
| 5200 | Technical Equipment | $540.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 64 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6725 | Distribution To Non-Governments | $27,179,925.56 | 72.7% |
| 4550 | Attorney General Legal Fees | $2,383,204.21 | 6.4% |
| 4975 | Agency Program Related Services | $1,671,562.02 | 4.5% |
| 4500 | Professional Services Non-It | $1,272,929.81 | 3.4% |
| 4976 | Agency Program Related Supplies | $1,216,100.92 | 3.3% |
| 7007 | Lease Pmt For Buildings | $1,124,707.18 | 3.0% |
| 4600 | State Government Service Charges | $700,907.72 | 1.9% |
| 4367 | Computer Technology Pc Support | $273,562.22 | 0.7% |
| 4365 | Computer Technology Pc Equipment<$5K | $214,945.10 | 0.6% |
| 4201 | Office Services | $180,271.90 | 0.5% |
| 4301 | Telecom/Voice Usage | $122,912.01 | 0.3% |
| 4519 | Professional Serv/Managed Serv Provider | $105,505.50 | 0.3% |

## Curator notes

Figures are aggregated from 434 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='860' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


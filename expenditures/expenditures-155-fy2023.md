---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-155-fy2023
title: Legislative Assembly — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 155, FY2023
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 6400163010ab2f341831c864272a89c5e9f2a261fad3fd9572b230042f26e3d5
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
  - expenditures-155-fy2022
  - expenditures-155-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-155
- legislative-assembly
agency_code: '155'
agency_name: LEGISLATIVE ASSEMBLY
fiscal_year: 2023
total_expense: '2499927.93'
transaction_count: 616
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Assembly — FY2023 expenditures

## At a glance

Legislative Assembly (agency code 155, recorded upstream as `LEGISLATIVE ASSEMBLY`) spent **$2,499,927.93** in fiscal year 2023, across 616 transaction records. That is down 28.3% from $3,487,656.95 in FY2022. The agency accounts for 0.01% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **50 of 77** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $755,501.94 (30.2% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $755,501.94 | 30.2% | 4 |
| 4175 | Office Expenses | $361,368.71 | 14.5% | 81 |
| 5900 | Other Capital Outlay | $268,975.00 | 10.8% | 3 |
| 4650 | Other Services And Supplies | $250,892.96 | 10.0% | 82 |
| 4275 | Publicity & Publications | $205,490.60 | 8.2% | 18 |
| 4715 | It Expendable Property | $194,552.60 | 7.8% | 24 |
| 4125 | Out-Of-State Travel | $108,684.16 | 4.3% | 144 |
| 3240 | Unemployment Assessment | $79,204.83 | 3.2% | 1 |
| 4300 | Professional Services | $77,118.58 | 3.1% | 5 |
| 5200 | Technical Equipment | $47,162.00 | 1.9% | 3 |
| 4150 | Employee Training | $46,077.55 | 1.8% | 51 |
| 4100 | Instate Travel | $33,770.10 | 1.4% | 96 |
| 4700 | Expendable Property $250-$5000 | $20,727.75 | 0.8% | 14 |
| 4425 | Lease Payments & Taxes | $16,329.75 | 0.7% | 19 |
| 4400 | Dues And Subscriptions | $13,148.37 | 0.5% | 53 |
| 4325 | Attorney General Legal Fees | $10,710.00 | 0.4% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $3,605.97 | 0.1% | 7 |
| 4250 | Data Processing | $3,149.44 | 0.1% | 1 |
| 3270 | Flexible Benefits | $2,000.99 | 0.1% | 1 |
| 4500 | Food And Kitchen Supplies | $579.98 | 0.0% | 1 |
| 4315 | It Professional Services | $324.00 | 0.0% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $305.68 | 0.0% | 2 |
| 4375 | Employee Recruitment And Development | $230.00 | 0.0% | 2 |
| 4450 | Fuels And Utilities | $16.97 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 49 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $755,501.94 | 30.2% |
| 5905 | Other Capital Outlay>=$5K | $268,975.00 | 10.8% |
| 4701 | Other Services | $231,903.15 | 9.3% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $205,490.60 | 8.2% |
| 4200 | Office Supplies | $194,299.17 | 7.8% |
| 4365 | Computer Technology Pc Equipment<$5K | $177,729.56 | 7.1% |
| 4201 | Office Services | $160,921.37 | 6.4% |
| 3231 | Unemployment Compensation & Assessment | $79,204.83 | 3.2% |
| 4500 | Professional Services Non-It | $77,118.58 | 3.1% |
| 4150 | Out-Of-State Lodging | $49,335.48 | 2.0% |
| 5250 | Technical Equipment>=$5K | $47,162.00 | 1.9% |
| 4159 | Out-Of-State Air Transportation | $46,806.86 | 1.9% |

## Curator notes

Figures are aggregated from 616 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='155' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


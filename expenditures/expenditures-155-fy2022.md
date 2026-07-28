---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-155-fy2022
title: Legislative Assembly — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 155, FY2022
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5378b32aad5d54d03160dd49832cc5c4f45e517dde8ba96c7e5b8bbb6e3a99f4
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
  - expenditures-155-fy2021
  - expenditures-155-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-155
- legislative-assembly
agency_code: '155'
agency_name: LEGISLATIVE ASSEMBLY
fiscal_year: 2022
total_expense: '3487656.95'
transaction_count: 400
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Assembly — FY2022 expenditures

## At a glance

Legislative Assembly (agency code 155, recorded upstream as `LEGISLATIVE ASSEMBLY`) spent **$3,487,656.95** in fiscal year 2022, across 400 transaction records. That is up 66.2% from $2,098,428.48 in FY2021. The agency accounts for 0.01% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **44 of 76** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $924,594.94 (26.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $924,594.94 | 26.5% | 5 |
| 4650 | Other Services And Supplies | $718,836.35 | 20.6% | 43 |
| 4300 | Professional Services | $557,855.63 | 16.0% | 7 |
| 4175 | Office Expenses | $521,745.17 | 15.0% | 53 |
| 4275 | Publicity & Publications | $344,082.18 | 9.9% | 12 |
| 5900 | Other Capital Outlay | $104,250.00 | 3.0% | 1 |
| 4715 | It Expendable Property | $57,552.84 | 1.7% | 28 |
| 4325 | Attorney General Legal Fees | $53,185.40 | 1.5% | 1 |
| 4125 | Out-Of-State Travel | $52,982.83 | 1.5% | 90 |
| 4150 | Employee Training | $42,270.55 | 1.2% | 37 |
| 4500 | Food And Kitchen Supplies | $31,907.45 | 0.9% | 9 |
| 4425 | Lease Payments & Taxes | $22,800.50 | 0.7% | 14 |
| 4575 | Agency Program Related Svcs & Supp | $13,289.77 | 0.4% | 3 |
| 4100 | Instate Travel | $12,362.79 | 0.4% | 44 |
| 3240 | Unemployment Assessment | $9,150.24 | 0.3% | 1 |
| 4400 | Dues And Subscriptions | $8,789.94 | 0.3% | 34 |
| 4200 | Telecomm/Tech Svc And Supplies | $5,027.73 | 0.1% | 10 |
| 4250 | Data Processing | $3,084.77 | 0.1% | 3 |
| 4700 | Expendable Property $250-$5000 | $3,056.51 | 0.1% | 4 |
| 3110 | Class/Unclass Salary & Per Diem | $831.36 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 45 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $924,594.94 | 26.5% |
| 4701 | Other Services | $718,836.35 | 20.6% |
| 4500 | Professional Services Non-It | $557,855.63 | 16.0% |
| 4200 | Office Supplies | $362,616.24 | 10.4% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $344,082.18 | 9.9% |
| 4201 | Office Services | $149,352.81 | 4.3% |
| 5905 | Other Capital Outlay>=$5K | $104,250.00 | 3.0% |
| 4550 | Attorney General Legal Fees | $53,185.40 | 1.5% |
| 4365 | Computer Technology Pc Equipment<$5K | $42,308.99 | 1.2% |
| 4875 | Food And Kitchen Supplies | $31,907.45 | 0.9% |
| 4150 | Out-Of-State Lodging | $27,936.72 | 0.8% |
| 4800 | Interagency Lease Payments | $22,800.50 | 0.7% |

## Curator notes

Figures are aggregated from 400 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='155' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


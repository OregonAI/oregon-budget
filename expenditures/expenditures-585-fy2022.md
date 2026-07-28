---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-585-fy2022
title: Blind, Cmsn for the — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 585, FY2022
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
  - expenditures-585-fy2021
  - expenditures-585-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-585
- blind-cmsn-for-the
agency_code: '585'
agency_name: BLIND, CMSN FOR THE
fiscal_year: 2022
total_expense: '4281299.72'
transaction_count: 345
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Blind, Cmsn for the — FY2022 expenditures

## At a glance

Blind, Cmsn for the (agency code 585, recorded upstream as `BLIND, CMSN FOR THE`) spent **$4,281,299.72** in fiscal year 2022, across 345 transaction records. That is down 8.9% from $4,701,915.25 in FY2021. The agency accounts for 0.01% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **41 of 76** agencies reporting that year.

The largest budget category was **Other Special Payments** at $1,193,499.20 (27.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6085 | Other Special Payments | $1,193,499.20 | 27.9% | 102 |
| 4300 | Professional Services | $713,363.25 | 16.7% | 3 |
| 4575 | Agency Program Related Svcs & Supp | $335,896.00 | 7.8% | 66 |
| 4225 | State Government Service Charges | $323,829.93 | 7.6% | 5 |
| 4650 | Other Services And Supplies | $317,856.24 | 7.4% | 22 |
| 6040 | Distribution To Local School Dist | $288,912.42 | 6.7% | 2 |
| 4425 | Lease Payments & Taxes | $262,492.08 | 6.1% | 12 |
| 4325 | Attorney General Legal Fees | $180,206.60 | 4.2% | 1 |
| 4715 | It Expendable Property | $179,360.10 | 4.2% | 10 |
| 4200 | Telecomm/Tech Svc And Supplies | $138,085.84 | 3.2% | 15 |
| 4315 | It Professional Services | $104,195.58 | 2.4% | 3 |
| 4100 | Instate Travel | $70,363.66 | 1.6% | 38 |
| 4475 | Facilities Maintenance | $48,166.43 | 1.1% | 14 |
| 4175 | Office Expenses | $32,268.52 | 0.8% | 16 |
| 4400 | Dues And Subscriptions | $30,500.00 | 0.7% | 1 |
| 4150 | Employee Training | $19,939.52 | 0.5% | 11 |
| 4250 | Data Processing | $13,284.20 | 0.3% | 1 |
| 5100 | Office Furniture And Fixtures | $9,416.87 | 0.2% | 1 |
| 4125 | Out-Of-State Travel | $9,195.79 | 0.2% | 17 |
| 5200 | Technical Equipment | $7,845.00 | 0.2% | 1 |
| 4700 | Expendable Property $250-$5000 | $2,488.49 | 0.1% | 3 |
| 4275 | Publicity & Publications | $134.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 44 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6900 | Other Special Payments | $1,193,499.20 | 27.9% |
| 4500 | Professional Services Non-It | $713,363.25 | 16.7% |
| 4600 | State Government Service Charges | $323,829.93 | 7.6% |
| 6823 | Payments To Local School Districts | $288,912.42 | 6.7% |
| 4800 | Interagency Lease Payments | $262,492.08 | 6.1% |
| 4975 | Agency Program Related Services | $217,623.23 | 5.1% |
| 4704 | Other Supplies | $201,159.58 | 4.7% |
| 4550 | Attorney General Legal Fees | $180,206.60 | 4.2% |
| 4976 | Agency Program Related Supplies | $118,272.77 | 2.8% |
| 4701 | Other Services | $110,083.86 | 2.6% |
| 4519 | Professional Serv/Managed Serv Provider | $99,195.58 | 2.3% |
| 4365 | Computer Technology Pc Equipment<$5K | $97,922.29 | 2.3% |

## Curator notes

Figures are aggregated from 345 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='585' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


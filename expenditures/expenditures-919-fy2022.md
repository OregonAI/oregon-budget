---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-919-fy2022
title: Real Estate Agy — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 919, FY2022
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
  - expenditures-919-fy2021
  - expenditures-919-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-919
- real-estate-agy
agency_code: '919'
agency_name: REAL ESTATE AGY
fiscal_year: 2022
total_expense: '1140973.08'
transaction_count: 75
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Real Estate Agy — FY2022 expenditures

## At a glance

Real Estate Agy (agency code 919, recorded upstream as `REAL ESTATE AGY`) spent **$1,140,973.08** in fiscal year 2022, across 75 transaction records. That is down 6.7% from $1,223,429.94 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **55 of 76** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $293,351.25 (25.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $293,351.25 | 25.7% | 3 |
| 4225 | State Government Service Charges | $186,524.84 | 16.3% | 5 |
| 4325 | Attorney General Legal Fees | $174,710.62 | 15.3% | 1 |
| 4425 | Lease Payments & Taxes | $134,188.17 | 11.8% | 1 |
| 4650 | Other Services And Supplies | $92,386.41 | 8.1% | 6 |
| 4315 | It Professional Services | $59,315.00 | 5.2% | 1 |
| 4250 | Data Processing | $45,619.32 | 4.0% | 3 |
| 4300 | Professional Services | $38,954.73 | 3.4% | 4 |
| 4175 | Office Expenses | $35,739.65 | 3.1% | 12 |
| 4200 | Telecomm/Tech Svc And Supplies | $29,123.06 | 2.6% | 7 |
| 4125 | Out-Of-State Travel | $11,521.71 | 1.0% | 3 |
| 4150 | Employee Training | $9,826.50 | 0.9% | 4 |
| 4715 | It Expendable Property | $7,783.04 | 0.7% | 7 |
| 4275 | Publicity & Publications | $6,469.05 | 0.6% | 1 |
| 4100 | Instate Travel | $6,432.37 | 0.6% | 12 |
| 4700 | Expendable Property $250-$5000 | $6,211.24 | 0.5% | 1 |
| 4475 | Facilities Maintenance | $1,491.71 | 0.1% | 1 |
| 4400 | Dues And Subscriptions | $1,045.00 | 0.1% | 2 |
| 3240 | Unemployment Assessment | $279.41 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 37 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $293,351.25 | 25.7% |
| 4600 | State Government Service Charges | $186,524.84 | 16.3% |
| 4550 | Attorney General Legal Fees | $174,710.62 | 15.3% |
| 4800 | Interagency Lease Payments | $134,188.17 | 11.8% |
| 4730 | Merchant Fees | $83,781.02 | 7.3% |
| 4515 | Professional Services Application Maint | $59,315.00 | 5.2% |
| 4375 | Computer Technology Computer Processing | $45,619.32 | 4.0% |
| 4500 | Professional Services Non-It | $38,954.73 | 3.4% |
| 4201 | Office Services | $29,946.04 | 2.6% |
| 4301 | Telecom/Voice Usage | $23,375.83 | 2.0% |
| 4701 | Other Services | $7,756.74 | 0.7% |
| 4150 | Out-Of-State Lodging | $6,854.65 | 0.6% |

## Curator notes

Figures are aggregated from 75 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='919' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


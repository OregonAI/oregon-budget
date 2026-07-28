---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-919-fy2023
title: Real Estate Agy — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 919, FY2023
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
  - expenditures-919-fy2022
  - expenditures-919-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-919
- real-estate-agy
agency_code: '919'
agency_name: REAL ESTATE AGY
fiscal_year: 2023
total_expense: '1086456.86'
transaction_count: 104
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Real Estate Agy — FY2023 expenditures

## At a glance

Real Estate Agy (agency code 919, recorded upstream as `REAL ESTATE AGY`) spent **$1,086,456.86** in fiscal year 2023, across 104 transaction records. That is down 4.8% from $1,140,973.08 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **56 of 77** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $225,651.50 (20.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $225,651.50 | 20.8% | 3 |
| 4225 | State Government Service Charges | $197,592.75 | 18.2% | 6 |
| 4325 | Attorney General Legal Fees | $134,407.18 | 12.4% | 1 |
| 4175 | Office Expenses | $119,689.54 | 11.0% | 8 |
| 4425 | Lease Payments & Taxes | $116,601.21 | 10.7% | 1 |
| 4650 | Other Services And Supplies | $96,471.16 | 8.9% | 6 |
| 4200 | Telecomm/Tech Svc And Supplies | $38,833.22 | 3.6% | 3 |
| 4300 | Professional Services | $38,594.41 | 3.6% | 4 |
| 4715 | It Expendable Property | $30,958.51 | 2.8% | 7 |
| 4150 | Employee Training | $29,709.08 | 2.7% | 6 |
| 4250 | Data Processing | $16,802.67 | 1.5% | 3 |
| 4125 | Out-Of-State Travel | $12,062.54 | 1.1% | 21 |
| 4100 | Instate Travel | $8,609.69 | 0.8% | 29 |
| 4400 | Dues And Subscriptions | $6,973.00 | 0.6% | 2 |
| 4475 | Facilities Maintenance | $6,961.68 | 0.6% | 1 |
| 3240 | Unemployment Assessment | $5,131.00 | 0.5% | 1 |
| 4275 | Publicity & Publications | $1,137.00 | 0.1% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $270.72 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 41 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $225,651.50 | 20.8% |
| 4600 | State Government Service Charges | $197,592.75 | 18.2% |
| 4550 | Attorney General Legal Fees | $134,407.18 | 12.4% |
| 4800 | Interagency Lease Payments | $116,601.21 | 10.7% |
| 4201 | Office Services | $114,698.95 | 10.6% |
| 4730 | Merchant Fees | $83,161.55 | 7.7% |
| 4500 | Professional Services Non-It | $38,594.41 | 3.6% |
| 4301 | Telecom/Voice Usage | $33,397.02 | 3.1% |
| 4406 | Prof Dev Instate Tuition/Registration | $24,205.75 | 2.2% |
| 4365 | Computer Technology Pc Equipment<$5K | $19,773.62 | 1.8% |
| 4375 | Computer Technology Computer Processing | $15,434.15 | 1.4% |
| 4701 | Other Services | $9,933.66 | 0.9% |

## Curator notes

Figures are aggregated from 104 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='919' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


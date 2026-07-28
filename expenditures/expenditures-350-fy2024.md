---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-350-fy2024
title: Columbia River Gorge Cmsn — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 350, FY2024
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
  - expenditures-350-fy2023
  - expenditures-350-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-350
- columbia-river-gorge-cmsn
agency_code: '350'
agency_name: COLUMBIA RIVER GORGE CMSN
fiscal_year: 2024
total_expense: '972087.17'
transaction_count: 15
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Columbia River Gorge Cmsn — FY2024 expenditures

## At a glance

Columbia River Gorge Cmsn (agency code 350, recorded upstream as `COLUMBIA RIVER GORGE CMSN`) spent **$972,087.17** in fiscal year 2024, across 15 transaction records. That is up 40.2% from $693,463.94 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **60 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $962,085.03 (99.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $962,085.03 | 99.0% | 1 |
| 4225 | State Government Service Charges | $7,643.25 | 0.8% | 2 |
| 4100 | Instate Travel | $935.80 | 0.1% | 5 |
| 4250 | Data Processing | $662.85 | 0.1% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $253.64 | 0.0% | 1 |
| 4425 | Lease Payments & Taxes | $200.00 | 0.0% | 1 |
| 4650 | Other Services And Supplies | $159.32 | 0.0% | 1 |
| 4275 | Publicity & Publications | $72.03 | 0.0% | 1 |
| 4715 | It Expendable Property | $60.20 | 0.0% | 1 |
| 4175 | Office Expenses | $15.05 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 12 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $962,085.03 | 99.0% |
| 4600 | State Government Service Charges | $7,643.25 | 0.8% |
| 4375 | Computer Technology Computer Processing | $662.85 | 0.1% |
| 4106 | Instate Lodging | $452.41 | 0.0% |
| 4111 | Instate Mileage Reimbursmnt-Volunteers | $394.89 | 0.0% |
| 4977 | Agency Program Related Reimbursements | $253.64 | 0.0% |
| 4800 | Interagency Lease Payments | $200.00 | 0.0% |
| 4255 | Prizes And Awards | $159.32 | 0.0% |
| 4101 | Instate Meals With Overnight Stay | $88.50 | 0.0% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $72.03 | 0.0% |
| 4366 | Computer Technology Pc Software<$5K | $60.20 | 0.0% |
| 4201 | Office Services | $15.05 | 0.0% |

## Curator notes

Figures are aggregated from 15 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='350' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


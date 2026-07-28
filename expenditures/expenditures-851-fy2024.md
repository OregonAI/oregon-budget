---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-851-fy2024
title: Nursing, Brd of — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 851, FY2024
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
  - expenditures-851-fy2023
  - expenditures-851-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-851
- nursing-brd-of
agency_code: '851'
agency_name: NURSING, BRD OF
fiscal_year: 2024
total_expense: '5008896.12'
transaction_count: 215
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Nursing, Brd of — FY2024 expenditures

## At a glance

Nursing, Brd of (agency code 851, recorded upstream as `NURSING, BRD OF`) spent **$5,008,896.12** in fiscal year 2024, across 215 transaction records. That is up 14.1% from $4,391,796.52 in FY2023. The agency accounts for 0.02% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **45 of 80** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $1,453,025.43 (29.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $1,453,025.43 | 29.0% | 15 |
| 6050 | Distribution To Non-Profit Org | $936,707.00 | 18.7% | 2 |
| 4325 | Attorney General Legal Fees | $675,177.41 | 13.5% | 1 |
| 4300 | Professional Services | $517,920.69 | 10.3% | 8 |
| 4225 | State Government Service Charges | $344,439.72 | 6.9% | 8 |
| 4425 | Lease Payments & Taxes | $315,897.32 | 6.3% | 3 |
| 4650 | Other Services And Supplies | $240,871.77 | 4.8% | 7 |
| 4715 | It Expendable Property | $135,339.11 | 2.7% | 11 |
| 4200 | Telecomm/Tech Svc And Supplies | $112,042.46 | 2.2% | 12 |
| 4250 | Data Processing | $58,390.72 | 1.2% | 7 |
| 4700 | Expendable Property $250-$5000 | $58,059.78 | 1.2% | 5 |
| 4450 | Fuels And Utilities | $31,993.31 | 0.6% | 7 |
| 4150 | Employee Training | $29,508.41 | 0.6% | 9 |
| 4125 | Out-Of-State Travel | $29,078.84 | 0.6% | 36 |
| 4175 | Office Expenses | $26,745.21 | 0.5% | 17 |
| 4100 | Instate Travel | $21,080.75 | 0.4% | 60 |
| 3110 | Class/Unclass Salary & Per Diem | $19,937.59 | 0.4% | 2 |
| 4400 | Dues And Subscriptions | $1,289.00 | 0.0% | 2 |
| 3240 | Unemployment Assessment | $1,110.96 | 0.0% | 1 |
| 4475 | Facilities Maintenance | $214.40 | 0.0% | 1 |
| 3220 | Public Employes' Retirement System | $66.24 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 47 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $1,449,430.00 | 28.9% |
| 6735 | Distribution To Non-Profit Org | $936,707.00 | 18.7% |
| 4550 | Attorney General Legal Fees | $675,177.41 | 13.5% |
| 4500 | Professional Services Non-It | $517,920.69 | 10.3% |
| 4600 | State Government Service Charges | $344,439.72 | 6.9% |
| 7007 | Lease Pmt For Buildings | $315,707.56 | 6.3% |
| 4730 | Merchant Fees | $234,451.86 | 4.7% |
| 4301 | Telecom/Voice Usage | $91,997.99 | 1.8% |
| 4366 | Computer Technology Pc Software<$5K | $66,606.78 | 1.3% |
| 4999 | Expendable Property Non-It<$5K | $58,059.78 | 1.2% |
| 4375 | Computer Technology Computer Processing | $51,911.18 | 1.0% |
| 4365 | Computer Technology Pc Equipment<$5K | $43,350.79 | 0.9% |

## Curator notes

Figures are aggregated from 215 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='851' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


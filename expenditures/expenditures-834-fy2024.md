---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-834-fy2024
title: Dentistry, Brd of — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 834, FY2024
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
  - expenditures-834-fy2023
  - expenditures-834-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-834
- dentistry-brd-of
agency_code: '834'
agency_name: DENTISTRY, BRD OF
fiscal_year: 2024
total_expense: '692709.74'
transaction_count: 95
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dentistry, Brd of — FY2024 expenditures

## At a glance

Dentistry, Brd of (agency code 834, recorded upstream as `DENTISTRY, BRD OF`) spent **$692,709.74** in fiscal year 2024, across 95 transaction records. That is up 7.8% from $642,345.27 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **66 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $163,594.87 (23.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $163,594.87 | 23.6% | 10 |
| 4325 | Attorney General Legal Fees | $144,666.18 | 20.9% | 1 |
| 4425 | Lease Payments & Taxes | $106,011.02 | 15.3% | 2 |
| 4650 | Other Services And Supplies | $68,678.66 | 9.9% | 6 |
| 4250 | Data Processing | $63,464.08 | 9.2% | 5 |
| 4225 | State Government Service Charges | $47,843.69 | 6.9% | 4 |
| 4715 | It Expendable Property | $28,256.23 | 4.1% | 3 |
| 4575 | Agency Program Related Svcs & Supp | $23,807.71 | 3.4% | 2 |
| 4175 | Office Expenses | $12,138.87 | 1.8% | 9 |
| 4150 | Employee Training | $9,941.71 | 1.4% | 16 |
| 4200 | Telecomm/Tech Svc And Supplies | $9,894.30 | 1.4% | 4 |
| 4100 | Instate Travel | $8,333.72 | 1.2% | 25 |
| 4400 | Dues And Subscriptions | $4,806.80 | 0.7% | 4 |
| 4275 | Publicity & Publications | $1,151.90 | 0.2% | 3 |
| 4375 | Employee Recruitment And Development | $120.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 35 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $163,594.87 | 23.6% |
| 4550 | Attorney General Legal Fees | $144,666.18 | 20.9% |
| 7007 | Lease Pmt For Buildings | $80,687.63 | 11.6% |
| 4375 | Computer Technology Computer Processing | $62,024.08 | 9.0% |
| 4600 | State Government Service Charges | $47,843.69 | 6.9% |
| 4701 | Other Services | $37,074.74 | 5.4% |
| 4730 | Merchant Fees | $31,603.92 | 4.6% |
| 4366 | Computer Technology Pc Software<$5K | $27,028.04 | 3.9% |
| 7401 | Interest-Leased Assets | $25,323.39 | 3.7% |
| 4975 | Agency Program Related Services | $19,689.00 | 2.8% |
| 4301 | Telecom/Voice Usage | $8,415.78 | 1.2% |
| 4202 | Equipment Rental | $7,833.53 | 1.1% |

## Curator notes

Figures are aggregated from 95 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='834' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


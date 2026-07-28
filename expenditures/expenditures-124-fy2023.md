---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-124-fy2023
title: Licensed Social Workers Brd — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 124, FY2023
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
  - expenditures-124-fy2022
  - expenditures-124-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-124
- licensed-social-workers-brd
agency_code: '124'
agency_name: LICENSED SOCIAL WORKERS BRD
fiscal_year: 2023
total_expense: '292163.95'
transaction_count: 32
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Licensed Social Workers Brd — FY2023 expenditures

## At a glance

Licensed Social Workers Brd (agency code 124, recorded upstream as `LICENSED SOCIAL WORKERS BRD`) spent **$292,163.95** in fiscal year 2023, across 32 transaction records. That is down 3.7% from $303,356.20 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **71 of 77** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $73,557.03 (25.2% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $73,557.03 | 25.2% | 5 |
| 4575 | Agency Program Related Svcs & Supp | $68,030.35 | 23.3% | 2 |
| 4425 | Lease Payments & Taxes | $52,146.88 | 17.8% | 3 |
| 4225 | State Government Service Charges | $28,534.31 | 9.8% | 4 |
| 4250 | Data Processing | $20,852.03 | 7.1% | 3 |
| 4300 | Professional Services | $16,094.13 | 5.5% | 2 |
| 4325 | Attorney General Legal Fees | $15,439.60 | 5.3% | 1 |
| 4315 | It Professional Services | $7,050.00 | 2.4% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $4,666.59 | 1.6% | 4 |
| 4175 | Office Expenses | $3,465.51 | 1.2% | 2 |
| 4715 | It Expendable Property | $1,342.88 | 0.5% | 1 |
| 4275 | Publicity & Publications | $759.38 | 0.3% | 1 |
| 4100 | Instate Travel | $225.26 | 0.1% | 2 |

## Largest expenditure classes

The 12 largest of 22 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $68,030.35 | 23.3% |
| 4701 | Other Services | $56,334.61 | 19.3% |
| 4800 | Interagency Lease Payments | $47,889.99 | 16.4% |
| 4600 | State Government Service Charges | $28,534.31 | 9.8% |
| 4730 | Merchant Fees | $17,122.92 | 5.9% |
| 4367 | Computer Technology Pc Support | $16,500.00 | 5.6% |
| 4500 | Professional Services Non-It | $16,094.13 | 5.5% |
| 4550 | Attorney General Legal Fees | $15,439.60 | 5.3% |
| 4515 | Professional Services Application Maint | $6,000.00 | 2.1% |
| 4375 | Computer Technology Computer Processing | $4,352.03 | 1.5% |
| 7007 | Lease Pmt For Buildings | $3,867.49 | 1.3% |
| 4301 | Telecom/Voice Usage | $2,955.93 | 1.0% |

## Curator notes

Figures are aggregated from 32 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='124' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


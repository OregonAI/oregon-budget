---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-124-fy2024
title: Licensed Social Workers Brd — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 124, FY2024
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
  - expenditures-124-fy2023
  - expenditures-124-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-124
- licensed-social-workers-brd
agency_code: '124'
agency_name: LICENSED SOCIAL WORKERS BRD
fiscal_year: 2024
total_expense: '337260.86'
transaction_count: 39
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Licensed Social Workers Brd — FY2024 expenditures

## At a glance

Licensed Social Workers Brd (agency code 124, recorded upstream as `LICENSED SOCIAL WORKERS BRD`) spent **$337,260.86** in fiscal year 2024, across 39 transaction records. That is up 15.4% from $292,163.95 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **70 of 80** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $70,149.53 (20.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $70,149.53 | 20.8% | 5 |
| 4575 | Agency Program Related Svcs & Supp | $67,351.50 | 20.0% | 1 |
| 4425 | Lease Payments & Taxes | $53,450.52 | 15.8% | 1 |
| 4225 | State Government Service Charges | $46,939.42 | 13.9% | 4 |
| 4325 | Attorney General Legal Fees | $40,103.05 | 11.9% | 1 |
| 4250 | Data Processing | $24,186.85 | 7.2% | 4 |
| 4315 | It Professional Services | $18,582.00 | 5.5% | 2 |
| 4715 | It Expendable Property | $5,682.94 | 1.7% | 3 |
| 4100 | Instate Travel | $5,082.21 | 1.5% | 8 |
| 4200 | Telecomm/Tech Svc And Supplies | $4,076.80 | 1.2% | 4 |
| 4175 | Office Expenses | $1,204.56 | 0.4% | 4 |
| 4300 | Professional Services | $290.70 | 0.1% | 1 |
| 4275 | Publicity & Publications | $160.78 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 22 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $67,351.50 | 20.0% |
| 4701 | Other Services | $54,430.95 | 16.1% |
| 4800 | Interagency Lease Payments | $53,450.52 | 15.8% |
| 4600 | State Government Service Charges | $46,939.42 | 13.9% |
| 4550 | Attorney General Legal Fees | $40,103.05 | 11.9% |
| 4367 | Computer Technology Pc Support | $19,649.54 | 5.8% |
| 4515 | Professional Services Application Maint | $18,000.00 | 5.3% |
| 4730 | Merchant Fees | $15,718.58 | 4.7% |
| 4365 | Computer Technology Pc Equipment<$5K | $4,739.32 | 1.4% |
| 4375 | Computer Technology Computer Processing | $4,537.31 | 1.3% |
| 4111 | Instate Mileage Reimbursmnt-Volunteers | $4,093.96 | 1.2% |
| 4301 | Telecom/Voice Usage | $2,835.08 | 0.8% |

## Curator notes

Figures are aggregated from 39 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='124' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


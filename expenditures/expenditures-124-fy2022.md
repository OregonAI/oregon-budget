---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-124-fy2022
title: Licensed Social Workers Brd — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 124, FY2022
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
  - expenditures-124-fy2021
  - expenditures-124-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-124
- licensed-social-workers-brd
agency_code: '124'
agency_name: LICENSED SOCIAL WORKERS BRD
fiscal_year: 2022
total_expense: '303356.20'
transaction_count: 29
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Licensed Social Workers Brd — FY2022 expenditures

## At a glance

Licensed Social Workers Brd (agency code 124, recorded upstream as `LICENSED SOCIAL WORKERS BRD`) spent **$303,356.20** in fiscal year 2022, across 29 transaction records. That is up 16.3% from $260,830.39 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **68 of 76** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $73,804.74 (24.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $73,804.74 | 24.3% | 4 |
| 4225 | State Government Service Charges | $66,158.75 | 21.8% | 4 |
| 4425 | Lease Payments & Taxes | $50,875.02 | 16.8% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $45,154.25 | 14.9% | 1 |
| 4250 | Data Processing | $17,101.70 | 5.6% | 2 |
| 4325 | Attorney General Legal Fees | $16,286.00 | 5.4% | 1 |
| 4315 | It Professional Services | $14,600.00 | 4.8% | 2 |
| 4300 | Professional Services | $11,078.42 | 3.7% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $5,945.35 | 2.0% | 4 |
| 4175 | Office Expenses | $2,069.47 | 0.7% | 2 |
| 4100 | Instate Travel | $221.25 | 0.1% | 4 |
| 4715 | It Expendable Property | $61.25 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 17 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $66,158.75 | 21.8% |
| 4701 | Other Services | $56,900.84 | 18.8% |
| 4800 | Interagency Lease Payments | $50,875.02 | 16.8% |
| 4975 | Agency Program Related Services | $45,154.25 | 14.9% |
| 4730 | Merchant Fees | $16,903.90 | 5.6% |
| 4367 | Computer Technology Pc Support | $16,500.00 | 5.4% |
| 4550 | Attorney General Legal Fees | $16,286.00 | 5.4% |
| 4515 | Professional Services Application Maint | $14,000.00 | 4.6% |
| 4500 | Professional Services Non-It | $11,078.42 | 3.7% |
| 4301 | Telecom/Voice Usage | $4,829.85 | 1.6% |
| 4201 | Office Services | $1,741.87 | 0.6% |
| 4305 | Telecom/Network Services | $1,115.50 | 0.4% |

## Curator notes

Figures are aggregated from 29 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='124' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


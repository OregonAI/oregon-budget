---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-124-fy2020
title: Licensed Social Workers Brd — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 124, FY2020
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: b73d59a16a10ad7f6ae4f4b415cba8d78894a3ead0e3928fe994cc49b9b11284
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
  - expenditures-124-fy2019
  - expenditures-124-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-124
- licensed-social-workers-brd
agency_code: '124'
agency_name: LICENSED SOCIAL WORKERS BRD
fiscal_year: 2020
total_expense: '264601.18'
transaction_count: 52
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Licensed Social Workers Brd — FY2020 expenditures

## At a glance

Licensed Social Workers Brd (agency code 124, recorded upstream as `LICENSED SOCIAL WORKERS BRD`) spent **$264,601.18** in fiscal year 2020, across 52 transaction records. That is down 4.0% from $275,564.83 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **66 of 77** agencies reporting that year.

The largest budget category was **Facilities Rent & Taxes** at $48,565.44 (18.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Facilities Rent & Taxes | $48,565.44 | 18.4% | 1 |
| 4650 | Other Services And Supplies | $42,957.01 | 16.2% | 4 |
| 4325 | Attorney General Legal Fees | $35,118.36 | 13.3% | 1 |
| 4225 | State Government Service Charges | $32,757.01 | 12.4% | 5 |
| 4315 | It Professional Services | $31,053.73 | 11.7% | 3 |
| 4575 | Agency Program Related Svcs & Supp | $29,918.25 | 11.3% | 1 |
| 4300 | Professional Services | $14,848.46 | 5.6% | 3 |
| 4250 | Data Processing | $14,400.71 | 5.4% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $5,832.20 | 2.2% | 4 |
| 4175 | Office Expenses | $5,060.33 | 1.9% | 2 |
| 4100 | Instate Travel | $2,931.88 | 1.1% | 22 |
| 4275 | Publicity & Publications | $1,003.76 | 0.4% | 1 |
| 4150 | Employee Training | $129.05 | 0.0% | 2 |
| 4715 | It Expendable Property | $24.99 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 22 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Facilities Rent | $48,565.44 | 18.4% |
| 4550 | Attorney General Legal Fees | $35,118.36 | 13.3% |
| 4701 | Other Services | $33,374.88 | 12.6% |
| 4600 | State Government Service Charges | $32,757.01 | 12.4% |
| 4975 | Agency Program Related Services | $29,918.25 | 11.3% |
| 4519 | Professional Serv/Managed Serv Provider | $25,553.73 | 9.7% |
| 4500 | Professional Services Non-It | $14,848.46 | 5.6% |
| 4371 | Computer Technology Peripheral Support | $13,194.00 | 5.0% |
| 4730 | Merchant Fees | $9,582.13 | 3.6% |
| 4515 | Professional Services Application Maint | $5,500.00 | 2.1% |
| 4201 | Office Services | $3,813.65 | 1.4% |
| 4305 | Telecom/Network Services | $3,595.36 | 1.4% |

## Curator notes

Figures are aggregated from 52 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='124' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


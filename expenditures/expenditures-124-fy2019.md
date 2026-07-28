---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-124-fy2019
title: Licensed Social Workers Brd — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 124, FY2019
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 3900810723066d4651c7227ef0c74a8b9c41ff76c2e4bcebbbb6f2268e443d34
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
  - expenditures-124-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-124
- licensed-social-workers-brd
agency_code: '124'
agency_name: LICENSED SOCIAL WORKERS BRD
fiscal_year: 2019
total_expense: '275564.83'
transaction_count: 38
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Licensed Social Workers Brd — FY2019 expenditures

## At a glance

Licensed Social Workers Brd (agency code 124, recorded upstream as `LICENSED SOCIAL WORKERS BRD`) spent **$275,564.83** in fiscal year 2019, across 38 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **69 of 78** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $59,439.04 (21.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $59,439.04 | 21.6% | 4 |
| 4425 | Facilities Rent & Taxes | $51,198.00 | 18.6% | 1 |
| 4325 | Attorney General Legal Fees | $42,962.48 | 15.6% | 1 |
| 4315 | It Professional Services | $29,380.63 | 10.7% | 4 |
| 4575 | Agency Program Related Svcs & Supp | $24,767.25 | 9.0% | 2 |
| 4225 | State Government Service Charges | $21,178.75 | 7.7% | 4 |
| 4300 | Professional Services | $18,454.01 | 6.7% | 3 |
| 4250 | Data Processing | $10,761.59 | 3.9% | 1 |
| 4175 | Office Expenses | $7,595.11 | 2.8% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $6,747.67 | 2.4% | 4 |
| 4100 | Instate Travel | $2,439.77 | 0.9% | 8 |
| 4150 | Employee Training | $450.00 | 0.2% | 1 |
| 4275 | Publicity & Publications | $168.93 | 0.1% | 1 |
| 4125 | Out-Of-State Travel | $21.60 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 20 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Facilities Rent | $51,198.00 | 18.6% |
| 4701 | Other Services | $51,032.67 | 18.5% |
| 4550 | Attorney General Legal Fees | $42,962.48 | 15.6% |
| 4975 | Agency Program Related Services | $24,767.25 | 9.0% |
| 4600 | State Government Service Charges | $21,178.75 | 7.7% |
| 4519 | Professional Serv/Managed Serv Provider | $19,480.63 | 7.1% |
| 4500 | Professional Services Non-It | $18,454.01 | 6.7% |
| 4375 | Computer Technology Computer Processing | $10,761.59 | 3.9% |
| 4515 | Professional Services Application Maint | $9,900.00 | 3.6% |
| 4730 | Merchant Fees | $8,406.37 | 3.1% |
| 4201 | Office Services | $4,546.39 | 1.6% |
| 4305 | Telecom/Network Services | $3,859.07 | 1.4% |

## Curator notes

Figures are aggregated from 38 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='124' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


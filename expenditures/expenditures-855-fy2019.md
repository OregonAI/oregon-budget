---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-855-fy2019
title: Pharmacy, Oregon Brd of — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 855, FY2019
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
  - expenditures-855-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-855
- pharmacy-oregon-brd-of
agency_code: '855'
agency_name: PHARMACY, OREGON BRD OF
fiscal_year: 2019
total_expense: '914280.85'
transaction_count: 139
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Pharmacy, Oregon Brd of — FY2019 expenditures

## At a glance

Pharmacy, Oregon Brd of (agency code 855, recorded upstream as `PHARMACY, OREGON BRD OF`) spent **$914,280.85** in fiscal year 2019, across 139 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **55 of 78** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $207,378.11 (22.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $207,378.11 | 22.7% | 1 |
| 4650 | Other Services And Supplies | $141,869.94 | 15.5% | 7 |
| 4300 | Professional Services | $121,244.72 | 13.3% | 7 |
| 4575 | Agency Program Related Svcs & Supp | $96,874.07 | 10.6% | 5 |
| 4425 | Facilities Rent & Taxes | $94,986.60 | 10.4% | 1 |
| 4225 | State Government Service Charges | $73,395.69 | 8.0% | 4 |
| 4175 | Office Expenses | $53,225.54 | 5.8% | 6 |
| 4250 | Data Processing | $35,130.13 | 3.8% | 3 |
| 4100 | Instate Travel | $24,175.76 | 2.6% | 56 |
| 4315 | It Professional Services | $23,414.00 | 2.6% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $13,680.38 | 1.5% | 4 |
| 3110 | Class/Unclass Salary & Per Diem | $10,340.37 | 1.1% | 1 |
| 4150 | Employee Training | $5,627.05 | 0.6% | 11 |
| 4275 | Publicity & Publications | $3,510.19 | 0.4% | 2 |
| 3240 | Unemployment Assessment | $1,869.13 | 0.2% | 1 |
| 4525 | Medical Supplies And Services | $1,541.50 | 0.2% | 1 |
| 4125 | Out-Of-State Travel | $1,533.83 | 0.2% | 17 |
| 3270 | Flexible Benefits | $1,365.43 | 0.1% | 1 |
| 3220 | Public Employes' Retirement System | $1,242.81 | 0.1% | 4 |
| 4475 | Facilities Maintenance | $867.52 | 0.1% | 1 |
| 3221 | Pension Bond Contribution | $459.20 | 0.1% | 1 |
| 3230 | Social Security Tax | $447.40 | 0.0% | 1 |
| 4400 | Dues And Subscriptions | $100.00 | 0.0% | 1 |
| 3250 | Workers' Compensation Assessment | $1.48 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 50 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $207,378.11 | 22.7% |
| 4500 | Professional Services Non-It | $121,244.72 | 13.3% |
| 4975 | Agency Program Related Services | $96,803.75 | 10.6% |
| 4800 | Facilities Rent | $94,986.60 | 10.4% |
| 4701 | Other Services | $91,680.12 | 10.0% |
| 4600 | State Government Service Charges | $73,395.69 | 8.0% |
| 4730 | Merchant Fees | $50,137.08 | 5.5% |
| 4200 | Office Supplies | $35,953.93 | 3.9% |
| 4375 | Computer Technology Computer Processing | $34,878.13 | 3.8% |
| 4519 | Professional Serv/Managed Serv Provider | $23,414.00 | 2.6% |
| 4201 | Office Services | $17,271.61 | 1.9% |
| 4108 | Instate Ground Transportation | $11,350.13 | 1.2% |

## Curator notes

Figures are aggregated from 139 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='855' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


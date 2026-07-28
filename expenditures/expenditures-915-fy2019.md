---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-915-fy2019
title: Construction Ctr Brd — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 915, FY2019
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
  - expenditures-915-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-915
- construction-ctr-brd
agency_code: '915'
agency_name: CONSTRUCTION CTR BRD
fiscal_year: 2019
total_expense: '1862070.56'
transaction_count: 182
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Construction Ctr Brd — FY2019 expenditures

## At a glance

Construction Ctr Brd (agency code 915, recorded upstream as `CONSTRUCTION CTR BRD`) spent **$1,862,070.56** in fiscal year 2019, across 182 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.01% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **51 of 78** agencies reporting that year.

The largest budget category was **Facilities Rent & Taxes** at $352,999.94 (19.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Facilities Rent & Taxes | $352,999.94 | 19.0% | 3 |
| 4650 | Other Services And Supplies | $246,088.28 | 13.2% | 9 |
| 4175 | Office Expenses | $229,872.13 | 12.3% | 8 |
| 4225 | State Government Service Charges | $193,497.09 | 10.4% | 5 |
| 4300 | Professional Services | $182,208.63 | 9.8% | 8 |
| 4100 | Instate Travel | $144,679.86 | 7.8% | 83 |
| 3110 | Class/Unclass Salary & Per Diem | $138,784.46 | 7.5% | 3 |
| 4325 | Attorney General Legal Fees | $69,855.08 | 3.8% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $59,724.93 | 3.2% | 6 |
| 4315 | It Professional Services | $59,422.53 | 3.2% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $44,848.90 | 2.4% | 8 |
| 4275 | Publicity & Publications | $32,756.91 | 1.8% | 9 |
| 3220 | Public Employes' Retirement System | $30,682.43 | 1.6% | 9 |
| 4715 | It Expendable Property | $17,243.66 | 0.9% | 1 |
| 5550 | Data Processing Software | $15,640.50 | 0.8% | 1 |
| 3230 | Social Security Tax | $10,440.59 | 0.6% | 2 |
| 3270 | Flexible Benefits | $9,435.91 | 0.5% | 2 |
| 4250 | Data Processing | $8,569.15 | 0.5% | 5 |
| 3221 | Pension Bond Contribution | $8,491.09 | 0.5% | 2 |
| 4150 | Employee Training | $4,677.70 | 0.3% | 7 |
| 4125 | Out-Of-State Travel | $1,178.70 | 0.1% | 5 |
| 4475 | Facilities Maintenance | $604.25 | 0.0% | 1 |
| 4700 | Expendable Property $250-$5000 | $338.80 | 0.0% | 1 |
| 3250 | Workers' Compensation Assessment | $29.04 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 51 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Facilities Rent | $352,999.94 | 19.0% |
| 4600 | State Government Service Charges | $193,497.09 | 10.4% |
| 4500 | Professional Services Non-It | $182,208.63 | 9.8% |
| 4201 | Office Services | $177,268.63 | 9.5% |
| 3111 | Regular Employees | $138,784.46 | 7.5% |
| 4701 | Other Services | $127,455.00 | 6.8% |
| 4108 | Instate Ground Transportation | $95,102.05 | 5.1% |
| 4730 | Merchant Fees | $78,229.99 | 4.2% |
| 4550 | Attorney General Legal Fees | $69,855.08 | 3.8% |
| 4975 | Agency Program Related Services | $59,612.23 | 3.2% |
| 4515 | Professional Services Application Maint | $59,422.53 | 3.2% |
| 4200 | Office Supplies | $52,603.50 | 2.8% |

## Curator notes

Figures are aggregated from 182 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='915' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


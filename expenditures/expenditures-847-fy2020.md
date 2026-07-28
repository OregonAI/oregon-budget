---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-847-fy2020
title: Medical Brd, OR — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 847, FY2020
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
  - expenditures-847-fy2019
  - expenditures-847-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-847
- medical-brd-or
agency_code: '847'
agency_name: MEDICAL BRD, OR
fiscal_year: 2020
total_expense: '1897698.37'
transaction_count: 196
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Medical Brd, OR — FY2020 expenditures

## At a glance

Medical Brd, OR (agency code 847, recorded upstream as `MEDICAL BRD, OR`) spent **$1,897,698.37** in fiscal year 2020, across 196 transaction records. That is down 4.5% from $1,986,437.18 in FY2019. The agency accounts for 0.01% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **48 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $505,598.26 (26.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $505,598.26 | 26.6% | 30 |
| 4425 | Facilities Rent & Taxes | $364,047.36 | 19.2% | 1 |
| 4325 | Attorney General Legal Fees | $277,708.66 | 14.6% | 1 |
| 4650 | Other Services And Supplies | $263,016.55 | 13.9% | 13 |
| 4225 | State Government Service Charges | $147,766.86 | 7.8% | 3 |
| 4175 | Office Expenses | $100,699.53 | 5.3% | 24 |
| 4575 | Agency Program Related Svcs & Supp | $89,475.09 | 4.7% | 6 |
| 4200 | Telecomm/Tech Svc And Supplies | $28,564.86 | 1.5% | 3 |
| 4100 | Instate Travel | $27,858.42 | 1.5% | 50 |
| 4150 | Employee Training | $22,559.89 | 1.2% | 39 |
| 4315 | It Professional Services | $19,943.69 | 1.1% | 6 |
| 3110 | Class/Unclass Salary & Per Diem | $18,570.45 | 1.0% | 1 |
| 4250 | Data Processing | $6,904.04 | 0.4% | 3 |
| 4700 | Expendable Property $250-$5000 | $6,319.73 | 0.3% | 2 |
| 3270 | Flexible Benefits | $5,040.80 | 0.3% | 1 |
| 4375 | Employee Recruitment And Development | $4,920.00 | 0.3% | 1 |
| 3220 | Public Employes' Retirement System | $2,533.14 | 0.1% | 3 |
| 3240 | Unemployment Assessment | $2,077.65 | 0.1% | 1 |
| 3230 | Social Security Tax | $1,401.96 | 0.1% | 1 |
| 4715 | It Expendable Property | $1,167.96 | 0.1% | 2 |
| 3221 | Pension Bond Contribution | $1,151.37 | 0.1% | 1 |
| 4275 | Publicity & Publications | $215.00 | 0.0% | 1 |
| 3260 | Mass Transit | $141.83 | 0.0% | 1 |
| 3210 | Erb Assessment | $8.96 | 0.0% | 1 |
| 3250 | Workers' Compensation Assessment | $6.31 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 56 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $505,598.26 | 26.6% |
| 4800 | Facilities Rent | $364,047.36 | 19.2% |
| 4550 | Attorney General Legal Fees | $277,708.66 | 14.6% |
| 4730 | Merchant Fees | $227,260.02 | 12.0% |
| 4600 | State Government Service Charges | $147,766.86 | 7.8% |
| 4975 | Agency Program Related Services | $86,793.75 | 4.6% |
| 4200 | Office Supplies | $85,501.93 | 4.5% |
| 4301 | Telecom/Voice Usage | $28,229.41 | 1.5% |
| 4685 | Liabity Expenditure-Attorney Settlement | $25,000.00 | 1.3% |
| 3111 | Regular Employees | $18,570.45 | 1.0% |
| 4106 | Instate Lodging | $10,425.00 | 0.5% |
| 4202 | Equipment Rental | $9,738.61 | 0.5% |

## Curator notes

Figures are aggregated from 196 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='847' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


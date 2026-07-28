---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-143-fy2019
title: Legislative Pol & Research Cmte — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 143, FY2019
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
  - expenditures-143-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-143
- legislative-pol-research-cmte
agency_code: '143'
agency_name: LEGISLATIVE POL & RESEARCH CMTE
fiscal_year: 2019
total_expense: '555546.78'
transaction_count: 108
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Pol & Research Cmte — FY2019 expenditures

## At a glance

Legislative Pol & Research Cmte (agency code 143, recorded upstream as `LEGISLATIVE POL & RESEARCH CMTE`) spent **$555,546.78** in fiscal year 2019, across 108 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **61 of 78** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $126,101.24 (22.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $126,101.24 | 22.7% | 2 |
| 3110 | Class/Unclass Salary & Per Diem | $121,212.43 | 21.8% | 1 |
| 4300 | Professional Services | $105,007.26 | 18.9% | 4 |
| 4715 | It Expendable Property | $69,494.10 | 12.5% | 9 |
| 4175 | Office Expenses | $21,795.60 | 3.9% | 7 |
| 3220 | Public Employes' Retirement System | $18,444.24 | 3.3% | 4 |
| 3270 | Flexible Benefits | $17,722.52 | 3.2% | 1 |
| 4150 | Employee Training | $15,937.19 | 2.9% | 31 |
| 4100 | Instate Travel | $12,814.06 | 2.3% | 27 |
| 3190 | All Other Differential | $12,424.37 | 2.2% | 1 |
| 3221 | Pension Bond Contribution | $8,285.50 | 1.5% | 1 |
| 3230 | Social Security Tax | $8,274.75 | 1.5% | 1 |
| 4700 | Expendable Property $250-$5000 | $6,046.84 | 1.1% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $4,746.51 | 0.9% | 3 |
| 4400 | Dues And Subscriptions | $2,899.63 | 0.5% | 3 |
| 4275 | Publicity & Publications | $2,197.99 | 0.4% | 1 |
| 4250 | Data Processing | $605.36 | 0.1% | 1 |
| 4125 | Out-Of-State Travel | $456.90 | 0.1% | 1 |
| 4475 | Facilities Maintenance | $388.67 | 0.1% | 1 |
| 4375 | Employee Recruitment And Development | $360.00 | 0.1% | 1 |
| 4650 | Other Services And Supplies | $292.50 | 0.1% | 3 |
| 3250 | Workers' Compensation Assessment | $19.86 | 0.0% | 1 |
| 3210 | Erb Assessment | $19.26 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 47 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $126,101.24 | 22.7% |
| 3111 | Regular Employees | $121,212.43 | 21.8% |
| 4500 | Professional Services Non-It | $105,007.26 | 18.9% |
| 4365 | Computer Technology Pc Equipment<$5K | $49,000.91 | 8.8% |
| 3263 | Medical,Dental,Life Insurance | $17,722.52 | 3.2% |
| 3210 | Public Employees Retirement Contribution | $14,012.41 | 2.5% |
| 3194 | O/Class, Leadwork, Sp Qual | $12,424.37 | 2.2% |
| 4200 | Office Supplies | $11,721.24 | 2.1% |
| 3212 | Pension Bond Assessment | $8,285.50 | 1.5% |
| 3221 | Social Security Taxes | $8,274.75 | 1.5% |
| 4302 | Telecom/Voice Equip Rental | $7,134.00 | 1.3% |
| 4999 | Expendable Property Non-It<$5K | $6,046.84 | 1.1% |

## Curator notes

Figures are aggregated from 108 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='143' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-524-fy2019
title: Chief Edu Office — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 524, FY2019
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
  - expenditures-524-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-524
- chief-edu-office
agency_code: '524'
agency_name: CHIEF EDU OFFICE
fiscal_year: 2019
total_expense: '1902400.10'
transaction_count: 116
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Chief Edu Office — FY2019 expenditures

## At a glance

Chief Edu Office (agency code 524, recorded upstream as `CHIEF EDU OFFICE`) spent **$1,902,400.10** in fiscal year 2019, across 116 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.01% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **49 of 78** agencies reporting that year.

The largest budget category was **It Professional Services** at $811,352.00 (42.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4315 | It Professional Services | $811,352.00 | 42.6% | 4 |
| 4250 | Data Processing | $587,857.58 | 30.9% | 4 |
| 3110 | Class/Unclass Salary & Per Diem | $144,347.92 | 7.6% | 2 |
| 4650 | Other Services And Supplies | $76,223.75 | 4.0% | 2 |
| 4425 | Facilities Rent & Taxes | $60,082.20 | 3.2% | 1 |
| 4225 | State Government Service Charges | $37,339.64 | 2.0% | 5 |
| 3270 | Flexible Benefits | $31,647.64 | 1.7% | 2 |
| 4300 | Professional Services | $29,589.55 | 1.6% | 10 |
| 4325 | Attorney General Legal Fees | $25,771.20 | 1.4% | 1 |
| 3220 | Public Employes' Retirement System | $25,305.82 | 1.3% | 8 |
| 4275 | Publicity & Publications | $11,688.18 | 0.6% | 2 |
| 3230 | Social Security Tax | $11,635.70 | 0.6% | 2 |
| 3190 | All Other Differential | $9,949.12 | 0.5% | 3 |
| 3221 | Pension Bond Contribution | $9,420.82 | 0.5% | 2 |
| 4175 | Office Expenses | $9,122.62 | 0.5% | 6 |
| 4150 | Employee Training | $7,076.24 | 0.4% | 32 |
| 4200 | Telecomm/Tech Svc And Supplies | $5,983.33 | 0.3% | 2 |
| 4100 | Instate Travel | $3,478.57 | 0.2% | 13 |
| 4125 | Out-Of-State Travel | $3,055.09 | 0.2% | 8 |
| 3260 | Mass Transit | $866.08 | 0.0% | 2 |
| 3170 | Overtime Payments | $464.77 | 0.0% | 1 |
| 4715 | It Expendable Property | $79.00 | 0.0% | 1 |
| 3250 | Workers' Compensation Assessment | $33.29 | 0.0% | 2 |
| 4575 | Agency Program Related Svcs & Supp | $29.99 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 50 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4513 | Professional Services Application New | $596,696.00 | 31.4% |
| 4357 | Computer Technology Mainframe Support | $311,812.96 | 16.4% |
| 4375 | Computer Technology Computer Processing | $276,044.62 | 14.5% |
| 4515 | Professional Services Application Maint | $214,656.00 | 11.3% |
| 3111 | Regular Employees | $144,347.92 | 7.6% |
| 4701 | Other Services | $76,223.75 | 4.0% |
| 4800 | Facilities Rent | $60,082.20 | 3.2% |
| 4600 | State Government Service Charges | $37,339.64 | 2.0% |
| 3263 | Medical,Dental,Life Insurance | $31,647.64 | 1.7% |
| 4500 | Professional Services Non-It | $29,589.55 | 1.6% |
| 4550 | Attorney General Legal Fees | $25,771.20 | 1.4% |
| 3210 | Public Employees Retirement Contribution | $15,148.37 | 0.8% |

## Curator notes

Figures are aggregated from 116 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='524' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


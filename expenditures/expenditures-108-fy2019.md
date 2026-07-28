---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-108-fy2019
title: Mental Health Regulatory Agy — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 108, FY2019
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
  - expenditures-108-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-108
- mental-health-regulatory-agy
agency_code: '108'
agency_name: MENTAL HEALTH REGULATORY AGY
fiscal_year: 2019
total_expense: '724027.26'
transaction_count: 95
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Mental Health Regulatory Agy — FY2019 expenditures

## At a glance

Mental Health Regulatory Agy (agency code 108, recorded upstream as `MENTAL HEALTH REGULATORY AGY`) spent **$724,027.26** in fiscal year 2019, across 95 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **57 of 78** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $202,494.15 (28.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $202,494.15 | 28.0% | 1 |
| 4650 | Other Services And Supplies | $122,142.84 | 16.9% | 5 |
| 4300 | Professional Services | $119,914.38 | 16.6% | 4 |
| 4425 | Facilities Rent & Taxes | $86,016.30 | 11.9% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $34,523.75 | 4.8% | 1 |
| 4225 | State Government Service Charges | $34,166.45 | 4.7% | 5 |
| 4315 | It Professional Services | $29,347.28 | 4.1% | 5 |
| 4250 | Data Processing | $28,673.79 | 4.0% | 3 |
| 4175 | Office Expenses | $23,657.00 | 3.3% | 2 |
| 3240 | Unemployment Assessment | $14,976.00 | 2.1% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $10,584.43 | 1.5% | 6 |
| 4100 | Instate Travel | $6,848.81 | 0.9% | 37 |
| 4150 | Employee Training | $5,876.51 | 0.8% | 12 |
| 4275 | Publicity & Publications | $2,409.81 | 0.3% | 2 |
| 4125 | Out-Of-State Travel | $1,561.16 | 0.2% | 8 |
| 4400 | Dues And Subscriptions | $500.00 | 0.1% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $334.60 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 34 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $202,494.15 | 28.0% |
| 4500 | Professional Services Non-It | $119,914.38 | 16.6% |
| 4701 | Other Services | $108,153.44 | 14.9% |
| 4800 | Facilities Rent | $86,016.30 | 11.9% |
| 4975 | Agency Program Related Services | $34,523.75 | 4.8% |
| 4600 | State Government Service Charges | $34,166.45 | 4.7% |
| 4519 | Professional Serv/Managed Serv Provider | $29,347.28 | 4.1% |
| 4362 | Computer Technology Server Support | $27,156.60 | 3.8% |
| 3231 | Unemployment Compensation & Assessment | $14,976.00 | 2.1% |
| 4200 | Office Supplies | $12,675.21 | 1.8% |
| 4730 | Merchant Fees | $11,955.01 | 1.7% |
| 4201 | Office Services | $10,981.79 | 1.5% |

## Curator notes

Figures are aggregated from 95 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='108' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


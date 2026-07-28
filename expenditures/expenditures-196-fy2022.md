---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-196-fy2022
title: Dist Attorneys/Deputies — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 196, FY2022
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
  - expenditures-196-fy2021
  - expenditures-196-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-196
- dist-attorneys-deputies
agency_code: '196'
agency_name: DIST ATTORNEYS/DEPUTIES
fiscal_year: 2022
total_expense: '536075.15'
transaction_count: 62
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dist Attorneys/Deputies — FY2022 expenditures

## At a glance

Dist Attorneys/Deputies (agency code 196, recorded upstream as `DIST ATTORNEYS/DEPUTIES`) spent **$536,075.15** in fiscal year 2022, across 62 transaction records. That is up 101.9% from $265,576.36 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **61 of 76** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $345,428.02 (64.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $345,428.02 | 64.4% | 4 |
| 3110 | Class/Unclass Salary & Per Diem | $41,896.90 | 7.8% | 5 |
| 4250 | Data Processing | $31,984.00 | 6.0% | 1 |
| 4300 | Professional Services | $22,507.40 | 4.2% | 2 |
| 3160 | Temporary Appointments | $19,918.15 | 3.7% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $15,867.20 | 3.0% | 2 |
| 4715 | It Expendable Property | $13,298.48 | 2.5% | 1 |
| 3220 | Public Employes' Retirement System | $11,123.65 | 2.1% | 13 |
| 3270 | Flexible Benefits | $9,948.33 | 1.9% | 6 |
| 4325 | Attorney General Legal Fees | $7,253.80 | 1.4% | 2 |
| 4650 | Other Services And Supplies | $6,823.10 | 1.3% | 1 |
| 3230 | Social Security Tax | $4,892.81 | 0.9% | 6 |
| 3221 | Pension Bond Contribution | $3,291.39 | 0.6% | 5 |
| 3190 | All Other Differential | $1,760.23 | 0.3% | 1 |
| 4175 | Office Expenses | $58.98 | 0.0% | 1 |
| 3250 | Workers' Compensation Assessment | $11.84 | 0.0% | 6 |
| 3210 | Erb Assessment | $10.87 | 0.0% | 5 |

## Largest expenditure classes

The 12 largest of 19 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $345,428.02 | 64.4% |
| 3111 | Regular Employees | $41,896.90 | 7.8% |
| 4362 | Computer Technology Server Support | $31,984.00 | 6.0% |
| 4500 | Professional Services Non-It | $22,507.40 | 4.2% |
| 3121 | Temporary Employees | $19,918.15 | 3.7% |
| 4975 | Agency Program Related Services | $15,867.20 | 3.0% |
| 4361 | Computer Technology Server Software<$5K | $13,298.48 | 2.5% |
| 3210 | Public Employees Retirement Contribution | $10,987.34 | 2.0% |
| 3263 | Medical,Dental,Life Insurance | $9,948.33 | 1.9% |
| 4550 | Attorney General Legal Fees | $7,253.80 | 1.4% |
| 4701 | Other Services | $6,823.10 | 1.3% |
| 3221 | Social Security Taxes | $4,892.81 | 0.9% |

## Curator notes

Figures are aggregated from 62 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='196' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


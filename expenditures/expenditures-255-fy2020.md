---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-255-fy2020
title: Parole/Post Prison Supv, Brd — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 255, FY2020
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
  - expenditures-255-fy2019
  - expenditures-255-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-255
- parole-post-prison-supv-brd
agency_code: '255'
agency_name: PAROLE/POST PRISON SUPV, BRD
fiscal_year: 2020
total_expense: '1748800.39'
transaction_count: 158
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Parole/Post Prison Supv, Brd — FY2020 expenditures

## At a glance

Parole/Post Prison Supv, Brd (agency code 255, recorded upstream as `PAROLE/POST PRISON SUPV, BRD`) spent **$1,748,800.39** in fiscal year 2020, across 158 transaction records. That is down 21.9% from $2,240,031.08 in FY2019. The agency accounts for 0.01% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **50 of 77** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $512,453.65 (29.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $512,453.65 | 29.3% | 2 |
| 4300 | Professional Services | $288,704.23 | 16.5% | 21 |
| 4425 | Facilities Rent & Taxes | $218,580.30 | 12.5% | 2 |
| 6025 | Distribution To Other Govts | $205,757.85 | 11.8% | 11 |
| 4225 | State Government Service Charges | $147,881.28 | 8.5% | 5 |
| 4525 | Medical Supplies And Services | $133,208.04 | 7.6% | 5 |
| 4650 | Other Services And Supplies | $80,048.70 | 4.6% | 9 |
| 3110 | Class/Unclass Salary & Per Diem | $44,487.57 | 2.5% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $40,322.34 | 2.3% | 4 |
| 4175 | Office Expenses | $27,822.20 | 1.6% | 19 |
| 4715 | It Expendable Property | $11,409.77 | 0.7% | 5 |
| 4100 | Instate Travel | $8,585.89 | 0.5% | 30 |
| 4700 | Expendable Property $250-$5000 | $7,542.11 | 0.4% | 2 |
| 4125 | Out-Of-State Travel | $7,373.46 | 0.4% | 6 |
| 4250 | Data Processing | $5,348.88 | 0.3% | 3 |
| 4150 | Employee Training | $5,032.53 | 0.3% | 24 |
| 4275 | Publicity & Publications | $2,089.02 | 0.1% | 3 |
| 4400 | Dues And Subscriptions | $1,886.00 | 0.1% | 3 |
| 4475 | Facilities Maintenance | $171.00 | 0.0% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $59.07 | 0.0% | 1 |
| 4375 | Employee Recruitment And Development | $36.50 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 41 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $512,453.65 | 29.3% |
| 4500 | Professional Services Non-It | $284,986.53 | 16.3% |
| 4800 | Facilities Rent | $218,580.30 | 12.5% |
| 6700 | Distribution To Other Governments | $205,757.85 | 11.8% |
| 4600 | State Government Service Charges | $147,881.28 | 8.5% |
| 4901 | Medical Services | $133,208.04 | 7.6% |
| 4701 | Other Services | $80,048.70 | 4.6% |
| 3111 | Regular Employees | $44,487.57 | 2.5% |
| 4305 | Telecom/Network Services | $22,269.11 | 1.3% |
| 4301 | Telecom/Voice Usage | $18,053.23 | 1.0% |
| 4202 | Equipment Rental | $11,849.38 | 0.7% |
| 4200 | Office Supplies | $11,390.12 | 0.7% |

## Curator notes

Figures are aggregated from 158 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='255' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


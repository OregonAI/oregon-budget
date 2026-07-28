---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-255-fy2021
title: Parole/Post Prison Supv, Brd — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 255, FY2021
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 81c90c241c212dba4cc304dd132bb03379de0003138cc2451899f8f95b1dcc97
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
  - expenditures-255-fy2020
  - expenditures-255-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-255
- parole-post-prison-supv-brd
agency_code: '255'
agency_name: PAROLE/POST PRISON SUPV, BRD
fiscal_year: 2021
total_expense: '1228148.16'
transaction_count: 43
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Parole/Post Prison Supv, Brd — FY2021 expenditures

## At a glance

Parole/Post Prison Supv, Brd (agency code 255, recorded upstream as `PAROLE/POST PRISON SUPV, BRD`) spent **$1,228,148.16** in fiscal year 2021, across 43 transaction records. That is down 29.8% from $1,748,800.39 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **50 of 76** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $381,347.25 (31.1% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $381,347.25 | 31.1% | 1 |
| 4425 | Lease Payments & Taxes | $241,074.70 | 19.6% | 1 |
| 4225 | State Government Service Charges | $150,842.18 | 12.3% | 4 |
| 4650 | Other Services And Supplies | $131,107.60 | 10.7% | 4 |
| 4525 | Medical Supplies And Services | $121,180.00 | 9.9% | 2 |
| 4300 | Professional Services | $114,378.96 | 9.3% | 9 |
| 4200 | Telecomm/Tech Svc And Supplies | $39,812.79 | 3.2% | 4 |
| 3240 | Unemployment Assessment | $19,097.70 | 1.6% | 1 |
| 4715 | It Expendable Property | $13,816.18 | 1.1% | 4 |
| 4175 | Office Expenses | $11,428.64 | 0.9% | 7 |
| 4400 | Dues And Subscriptions | $1,851.00 | 0.2% | 3 |
| 3220 | Public Employes' Retirement System | $1,277.88 | 0.1% | 1 |
| 4250 | Data Processing | $648.96 | 0.1% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $284.32 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 18 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $381,347.25 | 31.1% |
| 4800 | Facilities Rent | $241,074.70 | 19.6% |
| 4600 | State Government Service Charges | $150,842.18 | 12.3% |
| 4701 | Other Services | $131,107.60 | 10.7% |
| 4901 | Medical Services | $121,180.00 | 9.9% |
| 4500 | Professional Services Non-It | $114,378.96 | 9.3% |
| 4305 | Telecom/Network Services | $30,768.51 | 2.5% |
| 3231 | Unemployment Compensation & Assessment | $19,097.70 | 1.6% |
| 4372 | Computer Technology Peripheral Equip<$5K | $9,300.16 | 0.8% |
| 4301 | Telecom/Voice Usage | $9,044.28 | 0.7% |
| 4202 | Equipment Rental | $6,838.61 | 0.6% |
| 4366 | Computer Technology Pc Software<$5K | $4,516.02 | 0.4% |

## Curator notes

Figures are aggregated from 43 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='255' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


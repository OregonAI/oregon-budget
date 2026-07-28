---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-145-fy2023
title: Legislative Fiscal Officer — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 145, FY2023
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 6400163010ab2f341831c864272a89c5e9f2a261fad3fd9572b230042f26e3d5
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
  - expenditures-145-fy2022
  - expenditures-145-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-145
- legislative-fiscal-officer
agency_code: '145'
agency_name: LEGISLATIVE FISCAL OFFICER
fiscal_year: 2023
total_expense: '165465.35'
transaction_count: 101
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Fiscal Officer — FY2023 expenditures

## At a glance

Legislative Fiscal Officer (agency code 145, recorded upstream as `LEGISLATIVE FISCAL OFFICER`) spent **$165,465.35** in fiscal year 2023, across 101 transaction records. That is down 8.3% from $180,490.99 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **73 of 77** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $72,991.59 (44.1% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $72,991.59 | 44.1% | 4 |
| 4150 | Employee Training | $39,783.13 | 24.0% | 29 |
| 4175 | Office Expenses | $12,308.49 | 7.4% | 10 |
| 5150 | Telecommunications | $9,479.17 | 5.7% | 1 |
| 4700 | Expendable Property $250-$5000 | $7,155.52 | 4.3% | 5 |
| 4125 | Out-Of-State Travel | $6,845.80 | 4.1% | 15 |
| 4715 | It Expendable Property | $6,122.42 | 3.7% | 5 |
| 4100 | Instate Travel | $6,083.23 | 3.7% | 23 |
| 4650 | Other Services And Supplies | $1,610.35 | 1.0% | 6 |
| 4250 | Data Processing | $1,601.15 | 1.0% | 1 |
| 3240 | Unemployment Assessment | $1,219.99 | 0.7% | 1 |
| 4400 | Dues And Subscriptions | $264.51 | 0.2% | 1 |

## Largest expenditure classes

The 12 largest of 38 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $72,991.59 | 44.1% |
| 4437 | Prof Dev Dues/Membership | $27,101.06 | 16.4% |
| 5203 | Telecom/Teleconference Equipment>=$5K | $9,479.17 | 5.7% |
| 4201 | Office Services | $7,469.96 | 4.5% |
| 4999 | Expendable Property Non-It<$5K | $7,155.52 | 4.3% |
| 4200 | Office Supplies | $4,838.53 | 2.9% |
| 4365 | Computer Technology Pc Equipment<$5K | $4,695.25 | 2.8% |
| 4401 | Training, Education Or Instruction Srvc | $3,587.50 | 2.2% |
| 4159 | Out-Of-State Air Transportation | $3,258.59 | 2.0% |
| 4150 | Out-Of-State Lodging | $2,687.52 | 1.6% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $2,575.35 | 1.6% |
| 4440 | Prof Dev Out-Of-State Air Transportation | $2,560.79 | 1.5% |

## Curator notes

Figures are aggregated from 101 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='145' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


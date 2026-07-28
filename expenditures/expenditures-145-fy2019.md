---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-145-fy2019
title: Legislative Fiscal Officer — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 145, FY2019
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
  - expenditures-145-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-145
- legislative-fiscal-officer
agency_code: '145'
agency_name: LEGISLATIVE FISCAL OFFICER
fiscal_year: 2019
total_expense: '143325.71'
transaction_count: 75
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Fiscal Officer — FY2019 expenditures

## At a glance

Legislative Fiscal Officer (agency code 145, recorded upstream as `LEGISLATIVE FISCAL OFFICER`) spent **$143,325.71** in fiscal year 2019, across 75 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **72 of 78** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $53,012.35 (37.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $53,012.35 | 37.0% | 4 |
| 4150 | Employee Training | $44,506.67 | 31.1% | 18 |
| 4175 | Office Expenses | $11,508.83 | 8.0% | 7 |
| 4715 | It Expendable Property | $10,839.84 | 7.6% | 3 |
| 4300 | Professional Services | $10,052.75 | 7.0% | 2 |
| 4100 | Instate Travel | $5,182.77 | 3.6% | 31 |
| 4650 | Other Services And Supplies | $4,133.79 | 2.9% | 2 |
| 4250 | Data Processing | $1,816.08 | 1.3% | 1 |
| 4125 | Out-Of-State Travel | $1,040.92 | 0.7% | 3 |
| 4700 | Expendable Property $250-$5000 | $534.60 | 0.4% | 1 |
| 4400 | Dues And Subscriptions | $350.00 | 0.2% | 1 |
| 4375 | Employee Recruitment And Development | $270.00 | 0.2% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $77.11 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 28 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $53,012.35 | 37.0% |
| 4437 | Prof Dev Dues/Membership | $40,221.00 | 28.1% |
| 4365 | Computer Technology Pc Equipment<$5K | $10,569.89 | 7.4% |
| 4500 | Professional Services Non-It | $10,052.75 | 7.0% |
| 4201 | Office Services | $8,299.87 | 5.8% |
| 4701 | Other Services | $4,133.79 | 2.9% |
| 4200 | Office Supplies | $3,208.96 | 2.2% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $3,151.54 | 2.2% |
| 4367 | Computer Technology Pc Support | $1,816.08 | 1.3% |
| 4106 | Instate Lodging | $1,537.50 | 1.1% |
| 4406 | Prof Dev Instate Tuition/Registration | $1,508.00 | 1.1% |
| 4434 | Prof Dev Out-Of-State Lodging | $684.42 | 0.5% |

## Curator notes

Figures are aggregated from 75 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='145' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


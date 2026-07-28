---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-145-fy2020
title: Legislative Fiscal Officer — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 145, FY2020
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
  - expenditures-145-fy2019
  - expenditures-145-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-145
- legislative-fiscal-officer
agency_code: '145'
agency_name: LEGISLATIVE FISCAL OFFICER
fiscal_year: 2020
total_expense: '139331.19'
transaction_count: 72
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Fiscal Officer — FY2020 expenditures

## At a glance

Legislative Fiscal Officer (agency code 145, recorded upstream as `LEGISLATIVE FISCAL OFFICER`) spent **$139,331.19** in fiscal year 2020, across 72 transaction records. That is down 2.8% from $143,325.71 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **71 of 77** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $55,432.48 (39.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $55,432.48 | 39.8% | 3 |
| 4150 | Employee Training | $44,496.23 | 31.9% | 12 |
| 4175 | Office Expenses | $12,899.44 | 9.3% | 8 |
| 4715 | It Expendable Property | $8,092.35 | 5.8% | 3 |
| 4100 | Instate Travel | $5,938.26 | 4.3% | 30 |
| 4650 | Other Services And Supplies | $3,774.20 | 2.7% | 3 |
| 4125 | Out-Of-State Travel | $3,521.17 | 2.5% | 6 |
| 4700 | Expendable Property $250-$5000 | $2,975.16 | 2.1% | 2 |
| 4250 | Data Processing | $1,115.49 | 0.8% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $683.61 | 0.5% | 1 |
| 4400 | Dues And Subscriptions | $294.80 | 0.2% | 2 |
| 4300 | Professional Services | $108.00 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 30 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $55,432.48 | 39.8% |
| 4437 | Prof Dev Dues/Membership | $31,903.00 | 22.9% |
| 4201 | Office Services | $10,473.45 | 7.5% |
| 4365 | Computer Technology Pc Equipment<$5K | $7,079.75 | 5.1% |
| 4411 | Prof Dev Out-Of-State Tuition/Regist | $6,850.00 | 4.9% |
| 4401 | Training, Education Or Instruction Srvc | $5,250.00 | 3.8% |
| 4701 | Other Services | $3,774.20 | 2.7% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $3,606.40 | 2.6% |
| 4999 | Expendable Property Non-It<$5K | $2,975.16 | 2.1% |
| 4150 | Out-Of-State Lodging | $2,702.47 | 1.9% |
| 4200 | Office Supplies | $2,184.55 | 1.6% |
| 4106 | Instate Lodging | $1,841.40 | 1.3% |

## Curator notes

Figures are aggregated from 72 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='145' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


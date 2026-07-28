---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-145-fy2022
title: Legislative Fiscal Officer — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 145, FY2022
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
  - expenditures-145-fy2021
  - expenditures-145-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-145
- legislative-fiscal-officer
agency_code: '145'
agency_name: LEGISLATIVE FISCAL OFFICER
fiscal_year: 2022
total_expense: '180490.99'
transaction_count: 38
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Fiscal Officer — FY2022 expenditures

## At a glance

Legislative Fiscal Officer (agency code 145, recorded upstream as `LEGISLATIVE FISCAL OFFICER`) spent **$180,490.99** in fiscal year 2022, across 38 transaction records. That is up 44.1% from $125,283.97 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **72 of 76** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $76,457.80 (42.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $76,457.80 | 42.4% | 4 |
| 4150 | Employee Training | $43,978.08 | 24.4% | 12 |
| 4715 | It Expendable Property | $42,002.83 | 23.3% | 4 |
| 4250 | Data Processing | $7,545.38 | 4.2% | 1 |
| 4175 | Office Expenses | $7,244.84 | 4.0% | 6 |
| 4300 | Professional Services | $1,068.75 | 0.6% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $947.90 | 0.5% | 1 |
| 4100 | Instate Travel | $390.17 | 0.2% | 3 |
| 4275 | Publicity & Publications | $325.00 | 0.2% | 1 |
| 4700 | Expendable Property $250-$5000 | $225.92 | 0.1% | 1 |
| 4650 | Other Services And Supplies | $158.92 | 0.1% | 1 |
| 4400 | Dues And Subscriptions | $144.72 | 0.1% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $0.68 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 25 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $76,457.80 | 42.4% |
| 4365 | Computer Technology Pc Equipment<$5K | $38,383.89 | 21.3% |
| 4437 | Prof Dev Dues/Membership | $33,880.00 | 18.8% |
| 4367 | Computer Technology Pc Support | $7,545.38 | 4.2% |
| 4201 | Office Services | $6,658.14 | 3.7% |
| 4401 | Training, Education Or Instruction Srvc | $5,644.00 | 3.1% |
| 4366 | Computer Technology Pc Software<$5K | $3,560.96 | 2.0% |
| 4411 | Prof Dev Out-Of-State Tuition/Regist | $3,355.00 | 1.9% |
| 4500 | Professional Services Non-It | $1,068.75 | 0.6% |
| 4975 | Agency Program Related Services | $947.90 | 0.5% |
| 4406 | Prof Dev Instate Tuition/Registration | $825.00 | 0.5% |
| 4200 | Office Supplies | $345.26 | 0.2% |

## Curator notes

Figures are aggregated from 38 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='145' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


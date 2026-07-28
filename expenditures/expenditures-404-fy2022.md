---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-404-fy2022
title: Public Defense Services — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 404, FY2022
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
  - expenditures-404-fy2021
  - expenditures-404-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-404
- public-defense-services
agency_code: '404'
agency_name: PUBLIC DEFENSE SERVICES
fiscal_year: 2022
total_expense: '173872567.66'
transaction_count: 1600
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Public Defense Services — FY2022 expenditures

## At a glance

Public Defense Services (agency code 404, recorded upstream as `PUBLIC DEFENSE SERVICES`) spent **$173,872,567.66** in fiscal year 2022, across 1,600 transaction records. That is up 8.2% from $160,714,252.25 in FY2021. The agency accounts for 0.56% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **16 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $164,344,327.81 (94.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $164,344,327.81 | 94.5% | 689 |
| 4575 | Agency Program Related Svcs & Supp | $3,325,777.08 | 1.9% | 267 |
| 6100 | Distribution To Dept Of Human Services | $2,148,871.30 | 1.2% | 1 |
| 6198 | Dist To Judicial | $1,102,598.06 | 0.6% | 1 |
| 4100 | Instate Travel | $876,259.40 | 0.5% | 544 |
| 4425 | Lease Payments & Taxes | $586,791.64 | 0.3% | 9 |
| 4225 | State Government Service Charges | $468,519.00 | 0.3% | 4 |
| 4315 | It Professional Services | $372,852.00 | 0.2% | 2 |
| 4715 | It Expendable Property | $246,784.14 | 0.1% | 12 |
| 4650 | Other Services And Supplies | $76,106.54 | 0.0% | 5 |
| 4150 | Employee Training | $74,732.57 | 0.0% | 23 |
| 4325 | Attorney General Legal Fees | $61,299.30 | 0.0% | 2 |
| 4175 | Office Expenses | $60,693.64 | 0.0% | 17 |
| 4250 | Data Processing | $52,941.88 | 0.0% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $35,112.56 | 0.0% | 5 |
| 4400 | Dues And Subscriptions | $9,751.70 | 0.0% | 6 |
| 3240 | Unemployment Assessment | $9,379.81 | 0.0% | 1 |
| 4700 | Expendable Property $250-$5000 | $7,418.26 | 0.0% | 3 |
| 5900 | Other Capital Outlay | $6,513.00 | 0.0% | 1 |
| 4275 | Publicity & Publications | $3,700.64 | 0.0% | 1 |
| 3270 | Flexible Benefits | $1,911.90 | 0.0% | 1 |
| 4375 | Employee Recruitment And Development | $225.43 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 52 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $164,344,327.81 | 94.5% |
| 4977 | Agency Program Related Reimbursements | $3,322,032.40 | 1.9% |
| 6082 | Distribution To Dhs Agy 100 | $2,148,871.30 | 1.2% |
| 6132 | Distribution To Judicial 198 | $1,102,598.06 | 0.6% |
| 4112 | Instate Mileage Reimbursmnt-Nonemployee | $659,259.06 | 0.4% |
| 7007 | Lease Pmt For Buildings | $474,107.44 | 0.3% |
| 4600 | State Government Service Charges | $468,519.00 | 0.3% |
| 4519 | Professional Serv/Managed Serv Provider | $372,852.00 | 0.2% |
| 4104 | Instate Travel Miscellaneous Expenses | $143,726.47 | 0.1% |
| 4366 | Computer Technology Pc Software<$5K | $101,780.81 | 0.1% |
| 4365 | Computer Technology Pc Equipment<$5K | $95,832.80 | 0.1% |
| 4701 | Other Services | $76,065.55 | 0.0% |

## Curator notes

Figures are aggregated from 1,600 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='404' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


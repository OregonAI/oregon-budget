---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-404-fy2020
title: Public Defense Services — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 404, FY2020
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
  - expenditures-404-fy2019
  - expenditures-404-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-404
- public-defense-services
agency_code: '404'
agency_name: PUBLIC DEFENSE SERVICES
fiscal_year: 2020
total_expense: '150109933.22'
transaction_count: 1938
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Public Defense Services — FY2020 expenditures

## At a glance

Public Defense Services (agency code 404, recorded upstream as `PUBLIC DEFENSE SERVICES`) spent **$150,109,933.22** in fiscal year 2020, across 1,938 transaction records. That is up 13.7% from $132,060,047.55 in FY2019. The agency accounts for 0.64% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **15 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $141,906,175.03 (94.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $141,906,175.03 | 94.5% | 711 |
| 4575 | Agency Program Related Svcs & Supp | $3,497,919.30 | 2.3% | 341 |
| 6198 | Dist To Judicial | $1,641,553.92 | 1.1% | 1 |
| 4100 | Instate Travel | $1,004,277.04 | 0.7% | 743 |
| 4425 | Facilities Rent & Taxes | $531,447.96 | 0.4% | 3 |
| 4315 | It Professional Services | $393,906.50 | 0.3% | 3 |
| 4225 | State Government Service Charges | $369,277.92 | 0.2% | 5 |
| 4715 | It Expendable Property | $325,433.74 | 0.2% | 14 |
| 4700 | Expendable Property $250-$5000 | $79,477.14 | 0.1% | 5 |
| 4175 | Office Expenses | $78,309.40 | 0.1% | 19 |
| 4150 | Employee Training | $76,548.52 | 0.1% | 56 |
| 4650 | Other Services And Supplies | $72,019.90 | 0.0% | 5 |
| 4250 | Data Processing | $50,667.95 | 0.0% | 6 |
| 5550 | Data Processing Software | $26,329.68 | 0.0% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $14,730.54 | 0.0% | 5 |
| 4400 | Dues And Subscriptions | $14,024.06 | 0.0% | 6 |
| 3240 | Unemployment Assessment | $9,620.43 | 0.0% | 1 |
| 3270 | Flexible Benefits | $6,409.35 | 0.0% | 1 |
| 4475 | Facilities Maintenance | $5,562.25 | 0.0% | 1 |
| 4275 | Publicity & Publications | $2,666.69 | 0.0% | 5 |
| 4325 | Attorney General Legal Fees | $1,510.60 | 0.0% | 1 |
| 4525 | Medical Supplies And Services | $1,367.00 | 0.0% | 1 |
| 4125 | Out-Of-State Travel | $698.30 | 0.0% | 3 |

## Largest expenditure classes

The 12 largest of 52 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $141,906,175.03 | 94.5% |
| 4977 | Agency Program Related Reimbursements | $3,497,919.30 | 2.3% |
| 6132 | Distribution To Judicial 198 | $1,641,553.92 | 1.1% |
| 4112 | Instate Mileage Reimbursmnt-Nonemployee | $807,563.49 | 0.5% |
| 4800 | Facilities Rent | $531,447.96 | 0.4% |
| 4519 | Professional Serv/Managed Serv Provider | $393,906.50 | 0.3% |
| 4600 | State Government Service Charges | $369,277.92 | 0.2% |
| 4365 | Computer Technology Pc Equipment<$5K | $180,805.20 | 0.1% |
| 4366 | Computer Technology Pc Software<$5K | $122,433.33 | 0.1% |
| 4106 | Instate Lodging | $121,886.70 | 0.1% |
| 4999 | Expendable Property Non-It<$5K | $79,477.14 | 0.1% |
| 4701 | Other Services | $72,019.90 | 0.0% |

## Curator notes

Figures are aggregated from 1,938 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='404' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


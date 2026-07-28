---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-404-fy2019
title: Public Defense Services — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 404, FY2019
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
  - expenditures-404-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-404
- public-defense-services
agency_code: '404'
agency_name: PUBLIC DEFENSE SERVICES
fiscal_year: 2019
total_expense: '132060047.55'
transaction_count: 1956
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Public Defense Services — FY2019 expenditures

## At a glance

Public Defense Services (agency code 404, recorded upstream as `PUBLIC DEFENSE SERVICES`) spent **$132,060,047.55** in fiscal year 2019, across 1,956 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.64% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **15 of 78** agencies reporting that year.

The largest budget category was **Professional Services** at $124,824,654.15 (94.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $124,824,654.15 | 94.5% | 680 |
| 4575 | Agency Program Related Svcs & Supp | $3,544,324.44 | 2.7% | 358 |
| 6198 | Dist To Judicial | $1,589,033.09 | 1.2% | 1 |
| 4100 | Instate Travel | $991,614.94 | 0.8% | 779 |
| 4425 | Facilities Rent & Taxes | $341,146.12 | 0.3% | 1 |
| 4225 | State Government Service Charges | $216,941.09 | 0.2% | 5 |
| 4315 | It Professional Services | $128,865.68 | 0.1% | 3 |
| 4150 | Employee Training | $93,191.86 | 0.1% | 69 |
| 4175 | Office Expenses | $76,217.39 | 0.1% | 23 |
| 4715 | It Expendable Property | $53,389.62 | 0.0% | 11 |
| 4650 | Other Services And Supplies | $52,840.91 | 0.0% | 1 |
| 4250 | Data Processing | $46,551.66 | 0.0% | 6 |
| 4325 | Attorney General Legal Fees | $21,022.45 | 0.0% | 2 |
| 3240 | Unemployment Assessment | $18,755.66 | 0.0% | 1 |
| 4700 | Expendable Property $250-$5000 | $16,458.61 | 0.0% | 3 |
| 5600 | Data Processing Hardware | $15,506.13 | 0.0% | 1 |
| 5150 | Telecommunications | $10,933.34 | 0.0% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $9,540.83 | 0.0% | 4 |
| 4400 | Dues And Subscriptions | $5,601.50 | 0.0% | 2 |
| 4275 | Publicity & Publications | $3,458.08 | 0.0% | 5 |

## Largest expenditure classes

The 12 largest of 48 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $124,824,654.15 | 94.5% |
| 4977 | Agency Program Related Reimbursements | $3,541,574.44 | 2.7% |
| 6132 | Distribution To Judicial 198 | $1,589,033.09 | 1.2% |
| 4112 | Instate Mileage Reimbursmnt-Nonemployee | $796,262.49 | 0.6% |
| 4800 | Facilities Rent | $341,146.12 | 0.3% |
| 4600 | State Government Service Charges | $216,941.09 | 0.2% |
| 4519 | Professional Serv/Managed Serv Provider | $128,865.68 | 0.1% |
| 4106 | Instate Lodging | $126,626.68 | 0.1% |
| 4101 | Instate Meals With Overnight Stay | $59,952.82 | 0.0% |
| 4437 | Prof Dev Dues/Membership | $53,077.75 | 0.0% |
| 4701 | Other Services | $52,840.91 | 0.0% |
| 4375 | Computer Technology Computer Processing | $44,931.66 | 0.0% |

## Curator notes

Figures are aggregated from 1,956 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='404' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


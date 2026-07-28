---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-250-fy2022
title: Marine Board — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 250, FY2022
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
  - expenditures-250-fy2021
  - expenditures-250-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-250
- marine-board
agency_code: '250'
agency_name: MARINE BOARD
fiscal_year: 2022
total_expense: '10855739.38'
transaction_count: 262
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Marine Board — FY2022 expenditures

## At a glance

Marine Board (agency code 250, recorded upstream as `MARINE BOARD`) spent **$10,855,739.38** in fiscal year 2022, across 262 transaction records. That is down 7.4% from $11,728,984.34 in FY2021. The agency accounts for 0.04% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **37 of 76** agencies reporting that year.

The largest budget category was **Distribution To Counties** at $6,807,108.14 (62.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6020 | Distribution To Counties | $6,807,108.14 | 62.7% | 45 |
| 6257 | Dist To State Police | $1,083,934.64 | 10.0% | 1 |
| 6025 | Distribution To Other Govts | $459,933.31 | 4.2% | 6 |
| 6635 | Dist To Fish And Wildlife | $440,468.87 | 4.1% | 1 |
| 4650 | Other Services And Supplies | $357,262.94 | 3.3% | 40 |
| 4225 | State Government Service Charges | $281,470.04 | 2.6% | 6 |
| 4425 | Lease Payments & Taxes | $273,338.91 | 2.5% | 5 |
| 4300 | Professional Services | $246,832.98 | 2.3% | 12 |
| 4175 | Office Expenses | $123,729.84 | 1.1% | 23 |
| 6634 | Dist To Parks And Recreation | $111,886.62 | 1.0% | 1 |
| 6030 | Distribution To Non-Governments | $101,458.50 | 0.9% | 2 |
| 4275 | Publicity & Publications | $101,138.36 | 0.9% | 15 |
| 4100 | Instate Travel | $91,122.89 | 0.8% | 51 |
| 6015 | Distribution To Cities | $74,796.64 | 0.7% | 3 |
| 6048 | Special Payment To Public Universities | $68,215.24 | 0.6% | 1 |
| 4315 | It Professional Services | $67,856.12 | 0.6% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $41,777.01 | 0.4% | 9 |
| 4715 | It Expendable Property | $33,118.46 | 0.3% | 5 |
| 4250 | Data Processing | $28,037.99 | 0.3% | 1 |
| 4400 | Dues And Subscriptions | $25,388.00 | 0.2% | 12 |
| 6085 | Other Special Payments | $15,719.00 | 0.1% | 1 |
| 4150 | Employee Training | $8,271.32 | 0.1% | 11 |
| 4325 | Attorney General Legal Fees | $8,217.40 | 0.1% | 1 |
| 4125 | Out-Of-State Travel | $4,656.16 | 0.0% | 9 |

## Largest expenditure classes

The 12 largest of 45 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6300 | Distribution To Counties | $6,807,108.14 | 62.7% |
| 6136 | Distribution To State Police | $1,083,934.64 | 10.0% |
| 6700 | Distribution To Other Governments | $459,933.31 | 4.2% |
| 6179 | Distribution To Fish And Wildlife | $440,468.87 | 4.1% |
| 4600 | State Government Service Charges | $281,470.04 | 2.6% |
| 4800 | Interagency Lease Payments | $273,338.91 | 2.5% |
| 4500 | Professional Services Non-It | $246,832.98 | 2.3% |
| 4701 | Other Services | $230,096.63 | 2.1% |
| 6182 | Distribution To Parks And Recreation | $111,886.62 | 1.0% |
| 4201 | Office Services | $102,554.46 | 0.9% |
| 6725 | Distribution To Non-Governments | $101,458.50 | 0.9% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $101,138.36 | 0.9% |

## Curator notes

Figures are aggregated from 262 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='250' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


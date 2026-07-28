---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-250-fy2021
title: Marine Board — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 250, FY2021
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
  - expenditures-250-fy2020
  - expenditures-250-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-250
- marine-board
agency_code: '250'
agency_name: MARINE BOARD
fiscal_year: 2021
total_expense: '11728984.34'
transaction_count: 284
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Marine Board — FY2021 expenditures

## At a glance

Marine Board (agency code 250, recorded upstream as `MARINE BOARD`) spent **$11,728,984.34** in fiscal year 2021, across 284 transaction records. That is up 4.8% from $11,191,429.81 in FY2020. The agency accounts for 0.04% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **36 of 76** agencies reporting that year.

The largest budget category was **Distribution To Counties** at $6,275,748.69 (53.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6020 | Distribution To Counties | $6,275,748.69 | 53.5% | 45 |
| 6257 | Dist To State Police | $1,131,962.34 | 9.7% | 1 |
| 6025 | Distribution To Other Govts | $1,065,556.77 | 9.1% | 24 |
| 6635 | Dist To Fish And Wildlife | $586,171.95 | 5.0% | 1 |
| 6015 | Distribution To Cities | $476,231.02 | 4.1% | 33 |
| 6634 | Dist To Parks And Recreation | $356,502.50 | 3.0% | 1 |
| 4300 | Professional Services | $286,493.92 | 2.4% | 10 |
| 4425 | Lease Payments & Taxes | $268,946.12 | 2.3% | 3 |
| 4650 | Other Services And Supplies | $258,741.01 | 2.2% | 39 |
| 4225 | State Government Service Charges | $233,283.29 | 2.0% | 5 |
| 4175 | Office Expenses | $117,938.71 | 1.0% | 21 |
| 6048 | Special Payment To Public Universities | $117,117.36 | 1.0% | 1 |
| 4100 | Instate Travel | $108,184.23 | 0.9% | 30 |
| 4275 | Publicity & Publications | $102,961.29 | 0.9% | 18 |
| 4315 | It Professional Services | $66,672.00 | 0.6% | 1 |
| 6085 | Other Special Payments | $57,509.00 | 0.5% | 2 |
| 4715 | It Expendable Property | $54,161.02 | 0.5% | 9 |
| 4200 | Telecomm/Tech Svc And Supplies | $54,135.55 | 0.5% | 7 |
| 4250 | Data Processing | $48,548.53 | 0.4% | 1 |
| 4150 | Employee Training | $36,008.30 | 0.3% | 15 |
| 4400 | Dues And Subscriptions | $11,091.00 | 0.1% | 9 |
| 6030 | Distribution To Non-Governments | $7,340.54 | 0.1% | 4 |
| 4325 | Attorney General Legal Fees | $5,432.14 | 0.0% | 1 |
| 4700 | Expendable Property $250-$5000 | $1,179.06 | 0.0% | 2 |
| 3280 | Other Payroll Expenses | $1,068.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 44 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6300 | Distribution To Counties | $6,275,748.69 | 53.5% |
| 6136 | Distribution To State Police | $1,131,962.34 | 9.7% |
| 6700 | Distribution To Other Governments | $1,065,556.77 | 9.1% |
| 6179 | Distribution To Fish And Wildlife | $586,171.95 | 5.0% |
| 6400 | Distribution To Cities | $476,231.02 | 4.1% |
| 6182 | Distribution To Parks And Recreation | $356,502.50 | 3.0% |
| 4500 | Professional Services Non-It | $286,493.92 | 2.4% |
| 4800 | Facilities Rent | $268,946.12 | 2.3% |
| 4600 | State Government Service Charges | $233,283.29 | 2.0% |
| 6451 | Distribution To Oregon State University | $117,117.36 | 1.0% |
| 4101 | Instate Meals With Overnight Stay | $106,700.53 | 0.9% |
| 4253 | Advertise Publicity Publish/Print Srvs | $102,961.29 | 0.9% |

## Curator notes

Figures are aggregated from 284 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='250' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


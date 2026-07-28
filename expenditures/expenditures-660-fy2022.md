---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-660-fy2022
title: Land Conserv & Dev, Dept of — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 660, FY2022
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
  - expenditures-660-fy2021
  - expenditures-660-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-660
- land-conserv-dev-dept-of
agency_code: '660'
agency_name: LAND CONSERV & DEV, DEPT OF
fiscal_year: 2022
total_expense: '4859742.84'
transaction_count: 284
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Land Conserv & Dev, Dept of — FY2022 expenditures

## At a glance

Land Conserv & Dev, Dept of (agency code 660, recorded upstream as `LAND CONSERV & DEV, DEPT OF`) spent **$4,859,742.84** in fiscal year 2022, across 284 transaction records. That is up 10.9% from $4,382,947.74 in FY2021. The agency accounts for 0.02% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **39 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $1,698,771.09 (35.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $1,698,771.09 | 35.0% | 31 |
| 6015 | Distribution To Cities | $1,047,481.97 | 21.6% | 87 |
| 6020 | Distribution To Counties | $504,517.99 | 10.4% | 24 |
| 4425 | Lease Payments & Taxes | $460,593.12 | 9.5% | 2 |
| 4325 | Attorney General Legal Fees | $326,771.20 | 6.7% | 1 |
| 4225 | State Government Service Charges | $296,703.98 | 6.1% | 7 |
| 6048 | Special Payment To Public Universities | $245,168.92 | 5.0% | 2 |
| 4315 | It Professional Services | $72,415.39 | 1.5% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $60,586.40 | 1.2% | 12 |
| 4715 | It Expendable Property | $50,297.29 | 1.0% | 8 |
| 4400 | Dues And Subscriptions | $21,721.79 | 0.4% | 13 |
| 4175 | Office Expenses | $20,065.36 | 0.4% | 15 |
| 4150 | Employee Training | $16,751.13 | 0.3% | 5 |
| 4100 | Instate Travel | $15,219.47 | 0.3% | 46 |
| 4125 | Out-Of-State Travel | $5,302.77 | 0.1% | 7 |
| 3240 | Unemployment Assessment | $4,628.25 | 0.1% | 1 |
| 4250 | Data Processing | $3,361.37 | 0.1% | 4 |
| 4275 | Publicity & Publications | $3,309.97 | 0.1% | 5 |
| 4650 | Other Services And Supplies | $2,439.77 | 0.1% | 6 |
| 4575 | Agency Program Related Svcs & Supp | $2,288.65 | 0.0% | 1 |
| 4700 | Expendable Property $250-$5000 | $1,150.96 | 0.0% | 1 |
| 4475 | Facilities Maintenance | $196.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 48 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $1,698,771.09 | 35.0% |
| 6400 | Distribution To Cities | $1,047,481.97 | 21.6% |
| 6300 | Distribution To Counties | $504,517.99 | 10.4% |
| 4800 | Interagency Lease Payments | $460,593.12 | 9.5% |
| 4550 | Attorney General Legal Fees | $326,771.20 | 6.7% |
| 4600 | State Government Service Charges | $296,703.98 | 6.1% |
| 6452 | Distribution To Portland State Universit | $241,538.93 | 5.0% |
| 4515 | Professional Services Application Maint | $63,280.75 | 1.3% |
| 4301 | Telecom/Voice Usage | $53,514.53 | 1.1% |
| 4365 | Computer Technology Pc Equipment<$5K | $16,152.09 | 0.3% |
| 4366 | Computer Technology Pc Software<$5K | $16,144.52 | 0.3% |
| 4201 | Office Services | $14,717.72 | 0.3% |

## Curator notes

Figures are aggregated from 284 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='660' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


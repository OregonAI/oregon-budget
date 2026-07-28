---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-660-fy2021
title: Land Conserv & Dev, Dept of — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 660, FY2021
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
  - expenditures-660-fy2020
  - expenditures-660-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-660
- land-conserv-dev-dept-of
agency_code: '660'
agency_name: LAND CONSERV & DEV, DEPT OF
fiscal_year: 2021
total_expense: '4382947.74'
transaction_count: 176
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Land Conserv & Dev, Dept of — FY2021 expenditures

## At a glance

Land Conserv & Dev, Dept of (agency code 660, recorded upstream as `LAND CONSERV & DEV, DEPT OF`) spent **$4,382,947.74** in fiscal year 2021, across 176 transaction records. That is up 47.9% from $2,963,178.12 in FY2020. The agency accounts for 0.02% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **40 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $1,697,294.72 (38.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $1,697,294.72 | 38.7% | 34 |
| 6015 | Distribution To Cities | $941,069.77 | 21.5% | 27 |
| 4425 | Lease Payments & Taxes | $364,317.04 | 8.3% | 2 |
| 6020 | Distribution To Counties | $346,835.94 | 7.9% | 12 |
| 4325 | Attorney General Legal Fees | $328,834.46 | 7.5% | 1 |
| 4225 | State Government Service Charges | $217,396.37 | 5.0% | 7 |
| 6048 | Special Payment To Public Universities | $208,440.84 | 4.8% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $65,005.18 | 1.5% | 10 |
| 6085 | Other Special Payments | $50,639.75 | 1.2% | 3 |
| 4150 | Employee Training | $36,635.20 | 0.8% | 5 |
| 4715 | It Expendable Property | $32,788.24 | 0.7% | 8 |
| 4100 | Instate Travel | $28,185.32 | 0.6% | 16 |
| 4400 | Dues And Subscriptions | $20,459.57 | 0.5% | 17 |
| 4175 | Office Expenses | $14,698.23 | 0.3% | 16 |
| 4315 | It Professional Services | $10,680.73 | 0.2% | 5 |
| 3240 | Unemployment Assessment | $9,304.02 | 0.2% | 1 |
| 4250 | Data Processing | $4,858.98 | 0.1% | 2 |
| 4650 | Other Services And Supplies | $4,020.93 | 0.1% | 6 |
| 4700 | Expendable Property $250-$5000 | $963.00 | 0.0% | 1 |
| 4125 | Out-Of-State Travel | $519.45 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 44 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $1,697,294.72 | 38.7% |
| 6400 | Distribution To Cities | $941,069.77 | 21.5% |
| 4800 | Interagency Lease Payments | $364,317.04 | 8.3% |
| 6300 | Distribution To Counties | $346,835.94 | 7.9% |
| 4550 | Attorney General Legal Fees | $328,834.46 | 7.5% |
| 4600 | State Government Service Charges | $217,396.37 | 5.0% |
| 6452 | Distribution To Portland State Universit | $208,440.84 | 4.8% |
| 4301 | Telecom/Voice Usage | $57,360.08 | 1.3% |
| 6900 | Other Special Payments | $50,639.75 | 1.2% |
| 4437 | Prof Dev Dues/Membership | $34,432.00 | 0.8% |
| 4366 | Computer Technology Pc Software<$5K | $23,078.08 | 0.5% |
| 4108 | Instate Ground Transportation | $16,170.78 | 0.4% |

## Curator notes

Figures are aggregated from 176 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='660' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


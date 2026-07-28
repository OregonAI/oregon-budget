---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-255-fy2022
title: Parole/Post Prison Supv, Brd — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 255, FY2022
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
  - expenditures-255-fy2021
  - expenditures-255-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-255
- parole-post-prison-supv-brd
agency_code: '255'
agency_name: PAROLE/POST PRISON SUPV, BRD
fiscal_year: 2022
total_expense: '1560182.69'
transaction_count: 69
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Parole/Post Prison Supv, Brd — FY2022 expenditures

## At a glance

Parole/Post Prison Supv, Brd (agency code 255, recorded upstream as `PAROLE/POST PRISON SUPV, BRD`) spent **$1,560,182.69** in fiscal year 2022, across 69 transaction records. That is up 27.0% from $1,228,148.16 in FY2021. The agency accounts for 0.01% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **51 of 76** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $432,443.40 (27.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $432,443.40 | 27.7% | 1 |
| 4225 | State Government Service Charges | $251,302.32 | 16.1% | 4 |
| 4425 | Lease Payments & Taxes | $245,079.31 | 15.7% | 1 |
| 4300 | Professional Services | $168,462.84 | 10.8% | 10 |
| 4525 | Medical Supplies And Services | $145,139.00 | 9.3% | 1 |
| 6025 | Distribution To Other Govts | $127,522.14 | 8.2% | 9 |
| 4650 | Other Services And Supplies | $96,531.48 | 6.2% | 4 |
| 4715 | It Expendable Property | $44,963.41 | 2.9% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $27,558.42 | 1.8% | 6 |
| 4175 | Office Expenses | $8,821.38 | 0.6% | 5 |
| 3240 | Unemployment Assessment | $4,909.27 | 0.3% | 1 |
| 4150 | Employee Training | $2,984.00 | 0.2% | 8 |
| 4100 | Instate Travel | $1,614.55 | 0.1% | 8 |
| 4125 | Out-Of-State Travel | $1,507.67 | 0.1% | 3 |
| 4400 | Dues And Subscriptions | $1,230.00 | 0.1% | 2 |
| 4275 | Publicity & Publications | $91.10 | 0.0% | 2 |
| 3220 | Public Employes' Retirement System | $22.40 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 31 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $432,443.40 | 27.7% |
| 4600 | State Government Service Charges | $251,302.32 | 16.1% |
| 4800 | Interagency Lease Payments | $245,079.31 | 15.7% |
| 4500 | Professional Services Non-It | $168,462.84 | 10.8% |
| 4901 | Medical Services | $145,139.00 | 9.3% |
| 6700 | Distribution To Other Governments | $127,522.14 | 8.2% |
| 4701 | Other Services | $96,531.48 | 6.2% |
| 4365 | Computer Technology Pc Equipment<$5K | $25,770.76 | 1.7% |
| 4305 | Telecom/Network Services | $19,570.57 | 1.3% |
| 4372 | Computer Technology Peripheral Equip<$5K | $18,389.73 | 1.2% |
| 4301 | Telecom/Voice Usage | $7,987.85 | 0.5% |
| 3231 | Unemployment Compensation & Assessment | $4,909.27 | 0.3% |

## Curator notes

Figures are aggregated from 69 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='255' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


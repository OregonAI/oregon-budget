---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-255-fy2019
title: Parole/Post Prison Supv, Brd — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 255, FY2019
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
  - expenditures-255-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-255
- parole-post-prison-supv-brd
agency_code: '255'
agency_name: PAROLE/POST PRISON SUPV, BRD
fiscal_year: 2019
total_expense: '2240031.08'
transaction_count: 145
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Parole/Post Prison Supv, Brd — FY2019 expenditures

## At a glance

Parole/Post Prison Supv, Brd (agency code 255, recorded upstream as `PAROLE/POST PRISON SUPV, BRD`) spent **$2,240,031.08** in fiscal year 2019, across 145 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.01% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **47 of 78** agencies reporting that year.

The largest budget category was **Buildings And Structures** at $713,616.18 (31.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 5700 | Buildings And Structures | $713,616.18 | 31.9% | 1 |
| 4300 | Professional Services | $504,313.12 | 22.5% | 24 |
| 4325 | Attorney General Legal Fees | $372,257.59 | 16.6% | 1 |
| 5100 | Office Furniture And Fixtures | $149,205.60 | 6.7% | 1 |
| 4425 | Facilities Rent & Taxes | $143,585.00 | 6.4% | 1 |
| 4225 | State Government Service Charges | $105,920.39 | 4.7% | 5 |
| 4525 | Medical Supplies And Services | $97,747.02 | 4.4% | 3 |
| 4175 | Office Expenses | $60,895.78 | 2.7% | 16 |
| 4715 | It Expendable Property | $35,828.72 | 1.6% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $14,817.00 | 0.7% | 3 |
| 4100 | Instate Travel | $10,267.28 | 0.5% | 41 |
| 4650 | Other Services And Supplies | $7,590.18 | 0.3% | 4 |
| 4125 | Out-Of-State Travel | $7,408.51 | 0.3% | 12 |
| 4150 | Employee Training | $6,488.84 | 0.3% | 17 |
| 4700 | Expendable Property $250-$5000 | $3,748.05 | 0.2% | 2 |
| 4275 | Publicity & Publications | $2,500.00 | 0.1% | 1 |
| 4400 | Dues And Subscriptions | $1,527.00 | 0.1% | 2 |
| 4600 | Intra-Inter Agency Charges | $1,036.00 | 0.0% | 1 |
| 4475 | Facilities Maintenance | $708.62 | 0.0% | 1 |
| 4250 | Data Processing | $323.99 | 0.0% | 1 |
| 6035 | Distribution To Individuals | $102.31 | 0.0% | 1 |
| 3260 | Mass Transit | $95.54 | 0.0% | 1 |
| 3190 | All Other Differential | $48.36 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 50 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 5805 | Buildings & Improvements>=$5K | $713,616.18 | 31.9% |
| 4550 | Attorney General Legal Fees | $372,257.59 | 16.6% |
| 4505 | Professional Services Non-It>$75K | $284,470.94 | 12.7% |
| 4500 | Professional Services Non-It | $219,842.18 | 9.8% |
| 5100 | Office Furniture And Fixtures>=$5K | $149,205.60 | 6.7% |
| 4800 | Facilities Rent | $143,585.00 | 6.4% |
| 4600 | State Government Service Charges | $105,920.39 | 4.7% |
| 4901 | Medical Services | $97,747.02 | 4.4% |
| 4200 | Office Supplies | $51,082.79 | 2.3% |
| 4365 | Computer Technology Pc Equipment<$5K | $30,006.67 | 1.3% |
| 4301 | Telecom/Voice Usage | $11,459.40 | 0.5% |
| 4202 | Equipment Rental | $8,942.41 | 0.4% |

## Curator notes

Figures are aggregated from 145 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='255' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


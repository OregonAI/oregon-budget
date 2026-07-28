---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-350-fy2021
title: Columbia River Gorge Cmsn — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 350, FY2021
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
  - expenditures-350-fy2020
  - expenditures-350-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-350
- columbia-river-gorge-cmsn
agency_code: '350'
agency_name: COLUMBIA RIVER GORGE CMSN
fiscal_year: 2021
total_expense: '609903.52'
transaction_count: 13
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Columbia River Gorge Cmsn — FY2021 expenditures

## At a glance

Columbia River Gorge Cmsn (agency code 350, recorded upstream as `COLUMBIA RIVER GORGE CMSN`) spent **$609,903.52** in fiscal year 2021, across 13 transaction records. That is up 10.3% from $553,101.14 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **58 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $604,228.86 (99.1% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $604,228.86 | 99.1% | 1 |
| 4225 | State Government Service Charges | $3,749.50 | 0.6% | 3 |
| 4715 | It Expendable Property | $601.74 | 0.1% | 1 |
| 4325 | Attorney General Legal Fees | $527.71 | 0.1% | 1 |
| 4650 | Other Services And Supplies | $486.75 | 0.1% | 2 |
| 4275 | Publicity & Publications | $146.73 | 0.0% | 1 |
| 4100 | Instate Travel | $91.15 | 0.0% | 2 |
| 4125 | Out-Of-State Travel | $46.36 | 0.0% | 1 |
| 4175 | Office Expenses | $24.72 | 0.0% | 1 |

## Largest expenditure classes

The 11 largest of 11 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $604,228.86 | 99.1% |
| 4600 | State Government Service Charges | $3,749.50 | 0.6% |
| 4366 | Computer Technology Pc Software<$5K | $601.74 | 0.1% |
| 4550 | Attorney General Legal Fees | $527.71 | 0.1% |
| 4255 | Prizes And Awards | $390.00 | 0.1% |
| 4253 | Advertise Publicity Publish/Print Srvs | $146.73 | 0.0% |
| 4704 | Other Supplies | $96.75 | 0.0% |
| 4111 | Instate Mileage Reimbursmnt-Volunteers | $71.15 | 0.0% |
| 4164 | Out-Of-State Mileage Reimb-Volunteers | $46.36 | 0.0% |
| 4201 | Office Services | $24.72 | 0.0% |
| 4108 | Instate Ground Transportation | $20.00 | 0.0% |

## Curator notes

Figures are aggregated from 13 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='350' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


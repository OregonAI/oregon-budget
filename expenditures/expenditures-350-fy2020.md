---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-350-fy2020
title: Columbia River Gorge Cmsn — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 350, FY2020
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
  - expenditures-350-fy2019
  - expenditures-350-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-350
- columbia-river-gorge-cmsn
agency_code: '350'
agency_name: COLUMBIA RIVER GORGE CMSN
fiscal_year: 2020
total_expense: '553101.14'
transaction_count: 33
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Columbia River Gorge Cmsn — FY2020 expenditures

## At a glance

Columbia River Gorge Cmsn (agency code 350, recorded upstream as `COLUMBIA RIVER GORGE CMSN`) spent **$553,101.14** in fiscal year 2020, across 33 transaction records. That is up 9.1% from $507,159.73 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **59 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $543,575.43 (98.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $543,575.43 | 98.3% | 1 |
| 4225 | State Government Service Charges | $3,750.00 | 0.7% | 3 |
| 4125 | Out-Of-State Travel | $2,330.36 | 0.4% | 13 |
| 4575 | Agency Program Related Svcs & Supp | $1,238.99 | 0.2% | 2 |
| 4100 | Instate Travel | $945.47 | 0.2% | 8 |
| 4715 | It Expendable Property | $706.92 | 0.1% | 1 |
| 4425 | Facilities Rent & Taxes | $237.50 | 0.0% | 2 |
| 4325 | Attorney General Legal Fees | $203.48 | 0.0% | 1 |
| 4150 | Employee Training | $100.00 | 0.0% | 1 |
| 4175 | Office Expenses | $12.99 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 17 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $543,575.43 | 98.3% |
| 4600 | State Government Service Charges | $3,750.00 | 0.7% |
| 4164 | Out-Of-State Mileage Reimb-Volunteers | $1,790.19 | 0.3% |
| 4206 | Catering Services | $1,238.99 | 0.2% |
| 4111 | Instate Mileage Reimbursmnt-Volunteers | $779.56 | 0.1% |
| 4366 | Computer Technology Pc Software<$5K | $706.92 | 0.1% |
| 4150 | Out-Of-State Lodging | $263.42 | 0.0% |
| 4800 | Facilities Rent | $237.50 | 0.0% |
| 4550 | Attorney General Legal Fees | $203.48 | 0.0% |
| 4151 | Out-Of-State Meals With Overnight Stay | $137.25 | 0.0% |
| 4160 | Out-Of-State Ground Transportation | $112.00 | 0.0% |
| 4106 | Instate Lodging | $105.41 | 0.0% |

## Curator notes

Figures are aggregated from 33 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='350' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-120-fy2020
title: Accountancy, Oregon Brd of — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 120, FY2020
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
  - expenditures-120-fy2019
  - expenditures-120-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-120
- accountancy-oregon-brd-of
agency_code: '120'
agency_name: ACCOUNTANCY, OREGON BRD OF
fiscal_year: 2020
total_expense: '468925.67'
transaction_count: 57
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Accountancy, Oregon Brd of — FY2020 expenditures

## At a glance

Accountancy, Oregon Brd of (agency code 120, recorded upstream as `ACCOUNTANCY, OREGON BRD OF`) spent **$468,925.67** in fiscal year 2020, across 57 transaction records. That is up 16.8% from $401,496.26 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **61 of 77** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $226,292.50 (48.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $226,292.50 | 48.3% | 1 |
| 4650 | Other Services And Supplies | $67,394.46 | 14.4% | 4 |
| 4425 | Facilities Rent & Taxes | $63,743.60 | 13.6% | 2 |
| 4225 | State Government Service Charges | $49,332.95 | 10.5% | 5 |
| 4175 | Office Expenses | $21,795.88 | 4.6% | 2 |
| 4250 | Data Processing | $19,174.71 | 4.1% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $7,069.07 | 1.5% | 4 |
| 4150 | Employee Training | $5,447.36 | 1.2% | 16 |
| 4700 | Expendable Property $250-$5000 | $3,404.73 | 0.7% | 1 |
| 4100 | Instate Travel | $2,504.15 | 0.5% | 14 |
| 4300 | Professional Services | $2,477.16 | 0.5% | 3 |
| 4575 | Agency Program Related Svcs & Supp | $289.10 | 0.1% | 3 |

## Largest expenditure classes

The 12 largest of 25 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $226,292.50 | 48.3% |
| 4800 | Facilities Rent | $63,743.60 | 13.6% |
| 4600 | State Government Service Charges | $49,332.95 | 10.5% |
| 4701 | Other Services | $46,608.31 | 9.9% |
| 4730 | Merchant Fees | $19,464.00 | 4.2% |
| 4201 | Office Services | $18,184.00 | 3.9% |
| 4362 | Computer Technology Server Support | $17,592.00 | 3.8% |
| 4440 | Prof Dev Out-Of-State Air Transportation | $3,955.18 | 0.8% |
| 4200 | Office Supplies | $3,611.88 | 0.8% |
| 4301 | Telecom/Voice Usage | $3,608.53 | 0.8% |
| 4305 | Telecom/Network Services | $3,460.54 | 0.7% |
| 4999 | Expendable Property Non-It<$5K | $3,404.73 | 0.7% |

## Curator notes

Figures are aggregated from 57 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='120' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


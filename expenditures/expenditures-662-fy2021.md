---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-662-fy2021
title: Land Use Brd of Appeals — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 662, FY2021
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
  - expenditures-662-fy2020
  - expenditures-662-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-662
- land-use-brd-of-appeals
agency_code: '662'
agency_name: LAND USE BRD OF APPEALS
fiscal_year: 2021
total_expense: '169112.83'
transaction_count: 42
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Land Use Brd of Appeals — FY2021 expenditures

## At a glance

Land Use Brd of Appeals (agency code 662, recorded upstream as `LAND USE BRD OF APPEALS`) spent **$169,112.83** in fiscal year 2021, across 42 transaction records. That is up 31.3% from $128,828.27 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **70 of 76** agencies reporting that year.

The largest budget category was **Lease Payments & Taxes** at $46,053.60 (27.2% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Lease Payments & Taxes | $46,053.60 | 27.2% | 1 |
| 4225 | State Government Service Charges | $32,970.83 | 19.5% | 5 |
| 4650 | Other Services And Supplies | $18,998.02 | 11.2% | 3 |
| 4175 | Office Expenses | $14,891.41 | 8.8% | 10 |
| 4250 | Data Processing | $14,668.50 | 8.7% | 2 |
| 4300 | Professional Services | $13,379.51 | 7.9% | 4 |
| 4275 | Publicity & Publications | $8,557.27 | 5.1% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $8,124.24 | 4.8% | 4 |
| 4715 | It Expendable Property | $3,996.44 | 2.4% | 1 |
| 3240 | Unemployment Assessment | $3,710.00 | 2.2% | 1 |
| 4700 | Expendable Property $250-$5000 | $2,197.25 | 1.3% | 2 |
| 4400 | Dues And Subscriptions | $1,283.60 | 0.8% | 3 |
| 4375 | Employee Recruitment And Development | $196.56 | 0.1% | 1 |
| 4325 | Attorney General Legal Fees | $85.60 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 18 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Interagency Lease Payments | $46,053.60 | 27.2% |
| 4600 | State Government Service Charges | $32,970.83 | 19.5% |
| 4701 | Other Services | $18,998.02 | 11.2% |
| 4371 | Computer Technology Peripheral Support | $14,668.50 | 8.7% |
| 4500 | Professional Services Non-It | $13,379.51 | 7.9% |
| 4200 | Office Supplies | $11,600.55 | 6.9% |
| 4253 | Advertise Publicity Publish/Print Srvs | $8,557.27 | 5.1% |
| 4301 | Telecom/Voice Usage | $7,719.36 | 4.6% |
| 4365 | Computer Technology Pc Equipment<$5K | $3,996.44 | 2.4% |
| 3231 | Unemployment Compensation & Assessment | $3,710.00 | 2.2% |
| 4202 | Equipment Rental | $2,315.51 | 1.4% |
| 4999 | Expendable Property Non-It<$5K | $2,197.25 | 1.3% |

## Curator notes

Figures are aggregated from 42 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='662' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


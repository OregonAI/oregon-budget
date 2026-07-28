---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-919-fy2020
title: Real Estate Agy — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 919, FY2020
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
  - expenditures-919-fy2019
  - expenditures-919-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-919
- real-estate-agy
agency_code: '919'
agency_name: REAL ESTATE AGY
fiscal_year: 2020
total_expense: '718405.62'
transaction_count: 140
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Real Estate Agy — FY2020 expenditures

## At a glance

Real Estate Agy (agency code 919, recorded upstream as `REAL ESTATE AGY`) spent **$718,405.62** in fiscal year 2020, across 140 transaction records. That is up 15.7% from $620,689.13 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **56 of 77** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $147,052.47 (20.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $147,052.47 | 20.5% | 5 |
| 4425 | Facilities Rent & Taxes | $130,670.62 | 18.2% | 2 |
| 4325 | Attorney General Legal Fees | $86,572.66 | 12.1% | 1 |
| 4650 | Other Services And Supplies | $82,599.58 | 11.5% | 5 |
| 4300 | Professional Services | $49,882.86 | 6.9% | 4 |
| 4315 | It Professional Services | $31,551.25 | 4.4% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $25,924.76 | 3.6% | 6 |
| 4250 | Data Processing | $24,102.88 | 3.4% | 2 |
| 5100 | Office Furniture And Fixtures | $23,506.00 | 3.3% | 1 |
| 4100 | Instate Travel | $22,092.60 | 3.1% | 60 |
| 4175 | Office Expenses | $20,302.22 | 2.8% | 10 |
| 4575 | Agency Program Related Svcs & Supp | $19,376.09 | 2.7% | 1 |
| 4125 | Out-Of-State Travel | $16,767.51 | 2.3% | 19 |
| 4715 | It Expendable Property | $13,085.18 | 1.8% | 8 |
| 4150 | Employee Training | $10,858.34 | 1.5% | 5 |
| 4700 | Expendable Property $250-$5000 | $5,786.03 | 0.8% | 1 |
| 4475 | Facilities Maintenance | $3,531.06 | 0.5% | 1 |
| 4400 | Dues And Subscriptions | $3,530.00 | 0.5% | 2 |
| 4275 | Publicity & Publications | $486.57 | 0.1% | 3 |
| 3220 | Public Employes' Retirement System | $437.94 | 0.1% | 1 |
| 4525 | Medical Supplies And Services | $289.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 43 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $147,052.47 | 20.5% |
| 4800 | Facilities Rent | $130,670.62 | 18.2% |
| 4550 | Attorney General Legal Fees | $86,572.66 | 12.1% |
| 4730 | Merchant Fees | $75,390.54 | 10.5% |
| 4500 | Professional Services Non-It | $49,882.86 | 6.9% |
| 4514 | Professional Services Application Mod | $29,350.00 | 4.1% |
| 4375 | Computer Technology Computer Processing | $24,102.88 | 3.4% |
| 5100 | Office Furniture And Fixtures>=$5K | $23,506.00 | 3.3% |
| 4301 | Telecom/Voice Usage | $19,774.15 | 2.8% |
| 4975 | Agency Program Related Services | $19,376.09 | 2.7% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $9,876.11 | 1.4% |
| 4200 | Office Supplies | $9,605.15 | 1.3% |

## Curator notes

Figures are aggregated from 140 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='919' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-862-fy2020
title: Racing Cmsn — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 862, FY2020
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
  - expenditures-862-fy2019
  - expenditures-862-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-862
- racing-cmsn
agency_code: '862'
agency_name: RACING CMSN
fiscal_year: 2020
total_expense: '1455315.29'
transaction_count: 183
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Racing Cmsn — FY2020 expenditures

## At a glance

Racing Cmsn (agency code 862, recorded upstream as `RACING CMSN`) spent **$1,455,315.29** in fiscal year 2020, across 183 transaction records. That is down 23.1% from $1,893,085.01 in FY2019. The agency accounts for 0.01% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **51 of 77** agencies reporting that year.

The largest budget category was **Distribution To Non-Governments** at $1,026,975.49 (70.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6030 | Distribution To Non-Governments | $1,026,975.49 | 70.6% | 7 |
| 4100 | Instate Travel | $112,806.51 | 7.8% | 63 |
| 4225 | State Government Service Charges | $57,429.06 | 3.9% | 6 |
| 4650 | Other Services And Supplies | $53,840.32 | 3.7% | 9 |
| 4425 | Facilities Rent & Taxes | $41,938.60 | 2.9% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $40,361.13 | 2.8% | 6 |
| 4325 | Attorney General Legal Fees | $24,057.80 | 1.7% | 1 |
| 4250 | Data Processing | $20,387.37 | 1.4% | 3 |
| 3240 | Unemployment Assessment | $14,249.38 | 1.0% | 1 |
| 4125 | Out-Of-State Travel | $13,841.91 | 1.0% | 33 |
| 4200 | Telecomm/Tech Svc And Supplies | $13,094.81 | 0.9% | 7 |
| 4175 | Office Expenses | $10,456.12 | 0.7% | 16 |
| 4150 | Employee Training | $9,673.78 | 0.7% | 8 |
| 4300 | Professional Services | $6,635.48 | 0.5% | 5 |
| 4715 | It Expendable Property | $6,001.06 | 0.4% | 5 |
| 4700 | Expendable Property $250-$5000 | $1,937.05 | 0.1% | 3 |
| 4525 | Medical Supplies And Services | $782.98 | 0.1% | 3 |
| 4400 | Dues And Subscriptions | $695.00 | 0.0% | 4 |
| 4275 | Publicity & Publications | $151.44 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 48 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6725 | Distribution To Non-Governments | $1,026,975.49 | 70.6% |
| 4600 | State Government Service Charges | $57,429.06 | 3.9% |
| 4701 | Other Services | $51,646.66 | 3.5% |
| 4106 | Instate Lodging | $49,343.27 | 3.4% |
| 4800 | Facilities Rent | $41,938.60 | 2.9% |
| 4975 | Agency Program Related Services | $40,261.25 | 2.8% |
| 4101 | Instate Meals With Overnight Stay | $29,248.25 | 2.0% |
| 4108 | Instate Ground Transportation | $28,742.93 | 2.0% |
| 4550 | Attorney General Legal Fees | $24,057.80 | 1.7% |
| 4375 | Computer Technology Computer Processing | $17,744.37 | 1.2% |
| 3231 | Unemployment Compensation & Assessment | $14,249.38 | 1.0% |
| 4301 | Telecom/Voice Usage | $8,868.70 | 0.6% |

## Curator notes

Figures are aggregated from 183 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='862' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


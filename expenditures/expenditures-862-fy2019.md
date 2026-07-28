---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-862-fy2019
title: Racing Cmsn — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 862, FY2019
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
  - expenditures-862-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-862
- racing-cmsn
agency_code: '862'
agency_name: RACING CMSN
fiscal_year: 2019
total_expense: '1893085.01'
transaction_count: 184
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Racing Cmsn — FY2019 expenditures

## At a glance

Racing Cmsn (agency code 862, recorded upstream as `RACING CMSN`) spent **$1,893,085.01** in fiscal year 2019, across 184 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.01% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **50 of 78** agencies reporting that year.

The largest budget category was **Distribution To Non-Governments** at $1,300,301.02 (68.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6030 | Distribution To Non-Governments | $1,300,301.02 | 68.7% | 9 |
| 6025 | Distribution To Other Govts | $144,924.50 | 7.7% | 2 |
| 4100 | Instate Travel | $73,694.35 | 3.9% | 64 |
| 4650 | Other Services And Supplies | $73,633.55 | 3.9% | 10 |
| 4575 | Agency Program Related Svcs & Supp | $70,587.69 | 3.7% | 6 |
| 4225 | State Government Service Charges | $50,762.81 | 2.7% | 5 |
| 4425 | Facilities Rent & Taxes | $38,297.40 | 2.0% | 1 |
| 4250 | Data Processing | $35,989.90 | 1.9% | 4 |
| 4325 | Attorney General Legal Fees | $33,133.80 | 1.8% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $17,167.93 | 0.9% | 6 |
| 4150 | Employee Training | $13,187.79 | 0.7% | 14 |
| 4125 | Out-Of-State Travel | $10,580.10 | 0.6% | 19 |
| 4300 | Professional Services | $6,822.48 | 0.4% | 5 |
| 3240 | Unemployment Assessment | $6,405.00 | 0.3% | 1 |
| 4175 | Office Expenses | $5,351.46 | 0.3% | 16 |
| 6035 | Distribution To Individuals | $4,590.00 | 0.2% | 3 |
| 4715 | It Expendable Property | $4,219.13 | 0.2% | 6 |
| 4525 | Medical Supplies And Services | $1,888.50 | 0.1% | 3 |
| 4275 | Publicity & Publications | $853.44 | 0.0% | 4 |
| 4700 | Expendable Property $250-$5000 | $453.07 | 0.0% | 2 |
| 4400 | Dues And Subscriptions | $241.09 | 0.0% | 3 |

## Largest expenditure classes

The 12 largest of 48 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6725 | Distribution To Non-Governments | $1,300,301.02 | 68.7% |
| 6700 | Distribution To Other Governments | $144,924.50 | 7.7% |
| 4701 | Other Services | $72,015.10 | 3.8% |
| 4975 | Agency Program Related Services | $70,508.50 | 3.7% |
| 4600 | State Government Service Charges | $50,762.81 | 2.7% |
| 4800 | Facilities Rent | $38,297.40 | 2.0% |
| 4550 | Attorney General Legal Fees | $33,133.80 | 1.8% |
| 4106 | Instate Lodging | $30,147.96 | 1.6% |
| 4108 | Instate Ground Transportation | $19,987.53 | 1.1% |
| 4375 | Computer Technology Computer Processing | $18,139.90 | 1.0% |
| 4367 | Computer Technology Pc Support | $17,850.00 | 0.9% |
| 4101 | Instate Meals With Overnight Stay | $17,832.75 | 0.9% |

## Curator notes

Figures are aggregated from 184 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='862' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


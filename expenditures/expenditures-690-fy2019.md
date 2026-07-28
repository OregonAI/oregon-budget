---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-690-fy2019
title: Water Resources, Dept of — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 690, FY2019
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
  - expenditures-690-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-690
- water-resources-dept-of
agency_code: '690'
agency_name: WATER RESOURCES, DEPT OF
fiscal_year: 2019
total_expense: '8057296.01'
transaction_count: 607
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Water Resources, Dept of — FY2019 expenditures

## At a glance

Water Resources, Dept of (agency code 690, recorded upstream as `WATER RESOURCES, DEPT OF`) spent **$8,057,296.01** in fiscal year 2019, across 607 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.04% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **37 of 78** agencies reporting that year.

The largest budget category was **Distribution To Other Govts** at $3,574,372.89 (44.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6025 | Distribution To Other Govts | $3,574,372.89 | 44.4% | 17 |
| 4325 | Attorney General Legal Fees | $769,692.69 | 9.6% | 1 |
| 4425 | Facilities Rent & Taxes | $769,038.47 | 9.5% | 19 |
| 4650 | Other Services And Supplies | $704,545.42 | 8.7% | 92 |
| 4575 | Agency Program Related Svcs & Supp | $507,406.35 | 6.3% | 3 |
| 4225 | State Government Service Charges | $480,466.94 | 6.0% | 7 |
| 4100 | Instate Travel | $160,990.51 | 2.0% | 184 |
| 4250 | Data Processing | $155,598.39 | 1.9% | 4 |
| 4175 | Office Expenses | $140,475.07 | 1.7% | 38 |
| 4715 | It Expendable Property | $135,640.29 | 1.7% | 9 |
| 4150 | Employee Training | $107,912.26 | 1.3% | 107 |
| 4200 | Telecomm/Tech Svc And Supplies | $104,966.87 | 1.3% | 20 |
| 5200 | Technical Equipment | $100,205.00 | 1.2% | 1 |
| 6030 | Distribution To Non-Governments | $96,200.06 | 1.2% | 5 |
| 4700 | Expendable Property $250-$5000 | $92,894.92 | 1.2% | 6 |
| 4400 | Dues And Subscriptions | $77,542.63 | 1.0% | 21 |
| 4275 | Publicity & Publications | $31,089.62 | 0.4% | 32 |
| 4125 | Out-Of-State Travel | $17,700.08 | 0.2% | 26 |
| 4300 | Professional Services | $13,154.13 | 0.2% | 5 |
| 4450 | Fuels And Utilities | $12,123.02 | 0.2% | 5 |
| 4475 | Facilities Maintenance | $4,655.90 | 0.1% | 3 |
| 3110 | Class/Unclass Salary & Per Diem | $477.10 | 0.0% | 1 |
| 3240 | Unemployment Assessment | $147.40 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 65 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6700 | Distribution To Other Governments | $3,574,372.89 | 44.4% |
| 4550 | Attorney General Legal Fees | $769,692.69 | 9.6% |
| 4800 | Facilities Rent | $769,038.47 | 9.5% |
| 4701 | Other Services | $519,901.00 | 6.5% |
| 4975 | Agency Program Related Services | $507,406.35 | 6.3% |
| 4600 | State Government Service Charges | $480,466.94 | 6.0% |
| 5250 | Technical Equipment>=$5K | $100,205.00 | 1.2% |
| 4301 | Telecom/Voice Usage | $98,031.54 | 1.2% |
| 6725 | Distribution To Non-Governments | $96,200.06 | 1.2% |
| 4999 | Expendable Property Non-It<$5K | $92,894.92 | 1.2% |
| 4375 | Computer Technology Computer Processing | $89,853.01 | 1.1% |
| 4106 | Instate Lodging | $89,416.62 | 1.1% |

## Curator notes

Figures are aggregated from 607 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='690' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


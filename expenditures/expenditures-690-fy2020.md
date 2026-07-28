---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-690-fy2020
title: Water Resources, Dept of — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 690, FY2020
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
  - expenditures-690-fy2019
  - expenditures-690-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-690
- water-resources-dept-of
agency_code: '690'
agency_name: WATER RESOURCES, DEPT OF
fiscal_year: 2020
total_expense: '19858662.97'
transaction_count: 569
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Water Resources, Dept of — FY2020 expenditures

## At a glance

Water Resources, Dept of (agency code 690, recorded upstream as `WATER RESOURCES, DEPT OF`) spent **$19,858,662.97** in fiscal year 2020, across 569 transaction records. That is up 146.5% from $8,057,296.01 in FY2019. The agency accounts for 0.09% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **32 of 77** agencies reporting that year.

The largest budget category was **Distribution To Non-Governments** at $11,542,991.65 (58.1% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6030 | Distribution To Non-Governments | $11,542,991.65 | 58.1% | 8 |
| 6025 | Distribution To Other Govts | $3,744,269.56 | 18.9% | 18 |
| 4425 | Facilities Rent & Taxes | $924,574.09 | 4.7% | 17 |
| 4325 | Attorney General Legal Fees | $889,364.39 | 4.5% | 1 |
| 4650 | Other Services And Supplies | $798,267.66 | 4.0% | 92 |
| 4225 | State Government Service Charges | $660,753.67 | 3.3% | 7 |
| 4575 | Agency Program Related Svcs & Supp | $425,484.00 | 2.1% | 3 |
| 4700 | Expendable Property $250-$5000 | $162,350.63 | 0.8% | 12 |
| 4175 | Office Expenses | $121,239.46 | 0.6% | 54 |
| 4200 | Telecomm/Tech Svc And Supplies | $119,025.13 | 0.6% | 19 |
| 4100 | Instate Travel | $105,306.60 | 0.5% | 166 |
| 4250 | Data Processing | $105,231.97 | 0.5% | 4 |
| 5200 | Technical Equipment | $104,764.00 | 0.5% | 6 |
| 4150 | Employee Training | $39,251.87 | 0.2% | 71 |
| 4300 | Professional Services | $34,502.01 | 0.2% | 4 |
| 4715 | It Expendable Property | $29,075.27 | 0.1% | 6 |
| 4275 | Publicity & Publications | $26,904.56 | 0.1% | 28 |
| 4450 | Fuels And Utilities | $11,057.74 | 0.1% | 6 |
| 4125 | Out-Of-State Travel | $5,664.32 | 0.0% | 24 |
| 4400 | Dues And Subscriptions | $5,140.95 | 0.0% | 20 |
| 3110 | Class/Unclass Salary & Per Diem | $1,769.62 | 0.0% | 1 |
| 4475 | Facilities Maintenance | $1,673.82 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 54 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6725 | Distribution To Non-Governments | $11,542,991.65 | 58.1% |
| 6700 | Distribution To Other Governments | $3,744,269.56 | 18.9% |
| 4800 | Facilities Rent | $924,574.09 | 4.7% |
| 4550 | Attorney General Legal Fees | $889,364.39 | 4.5% |
| 4701 | Other Services | $669,058.12 | 3.4% |
| 4600 | State Government Service Charges | $660,753.67 | 3.3% |
| 4975 | Agency Program Related Services | $425,484.00 | 2.1% |
| 4999 | Expendable Property Non-It<$5K | $162,350.63 | 0.8% |
| 4301 | Telecom/Voice Usage | $113,534.09 | 0.6% |
| 5250 | Technical Equipment>=$5K | $104,764.00 | 0.5% |
| 4704 | Other Supplies | $81,479.13 | 0.4% |
| 4200 | Office Supplies | $72,349.93 | 0.4% |

## Curator notes

Figures are aggregated from 569 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='690' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


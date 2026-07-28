---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-632-fy2021
title: Geology & Mineral Ind, Dept of — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 632, FY2021
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
  - expenditures-632-fy2020
  - expenditures-632-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-632
- geology-mineral-ind-dept-of
agency_code: '632'
agency_name: GEOLOGY & MINERAL IND, DEPT OF
fiscal_year: 2021
total_expense: '3535953.79'
transaction_count: 88
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Geology & Mineral Ind, Dept of — FY2021 expenditures

## At a glance

Geology & Mineral Ind, Dept of (agency code 632, recorded upstream as `GEOLOGY & MINERAL IND, DEPT OF`) spent **$3,535,953.79** in fiscal year 2021, across 88 transaction records. That is up 29.4% from $2,732,772.20 in FY2020. The agency accounts for 0.01% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **43 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $2,454,683.69 (69.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $2,454,683.69 | 69.4% | 12 |
| 4425 | Lease Payments & Taxes | $206,183.55 | 5.8% | 2 |
| 4225 | State Government Service Charges | $205,944.99 | 5.8% | 4 |
| 4715 | It Expendable Property | $133,863.89 | 3.8% | 7 |
| 4250 | Data Processing | $133,023.24 | 3.8% | 3 |
| 5600 | Data Processing Hardware | $92,220.46 | 2.6% | 3 |
| 4650 | Other Services And Supplies | $86,960.55 | 2.5% | 6 |
| 4325 | Attorney General Legal Fees | $56,647.94 | 1.6% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $51,822.60 | 1.5% | 8 |
| 4100 | Instate Travel | $33,174.74 | 0.9% | 16 |
| 5200 | Technical Equipment | $24,300.00 | 0.7% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $20,032.15 | 0.6% | 3 |
| 4175 | Office Expenses | $16,298.75 | 0.5% | 10 |
| 4700 | Expendable Property $250-$5000 | $9,060.96 | 0.3% | 1 |
| 4475 | Facilities Maintenance | $5,483.54 | 0.2% | 1 |
| 4450 | Fuels And Utilities | $5,288.99 | 0.1% | 5 |
| 4400 | Dues And Subscriptions | $750.00 | 0.0% | 3 |
| 4150 | Employee Training | $180.00 | 0.0% | 1 |
| 4315 | It Professional Services | $33.75 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 38 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $2,454,683.69 | 69.4% |
| 4800 | Interagency Lease Payments | $206,183.55 | 5.8% |
| 4600 | State Government Service Charges | $205,944.99 | 5.8% |
| 4375 | Computer Technology Computer Processing | $126,276.53 | 3.6% |
| 4701 | Other Services | $86,924.57 | 2.5% |
| 4361 | Computer Technology Server Software<$5K | $71,056.31 | 2.0% |
| 4550 | Attorney General Legal Fees | $56,647.94 | 1.6% |
| 5350 | Computer Technology Mainframe Equip>=$5K | $53,640.00 | 1.5% |
| 4365 | Computer Technology Pc Equipment<$5K | $52,691.16 | 1.5% |
| 4301 | Telecom/Voice Usage | $33,036.75 | 0.9% |
| 5351 | Computer Technology Server Equip>=$5K | $32,281.46 | 0.9% |
| 4108 | Instate Ground Transportation | $29,877.47 | 0.8% |

## Curator notes

Figures are aggregated from 88 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='632' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


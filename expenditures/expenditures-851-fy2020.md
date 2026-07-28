---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-851-fy2020
title: Nursing, Brd of — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 851, FY2020
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
  - expenditures-851-fy2019
  - expenditures-851-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-851
- nursing-brd-of
agency_code: '851'
agency_name: NURSING, BRD OF
fiscal_year: 2020
total_expense: '3928529.71'
transaction_count: 235
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Nursing, Brd of — FY2020 expenditures

## At a glance

Nursing, Brd of (agency code 851, recorded upstream as `NURSING, BRD OF`) spent **$3,928,529.71** in fiscal year 2020, across 235 transaction records. That is up 11.1% from $3,536,841.43 in FY2019. The agency accounts for 0.02% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **40 of 77** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $1,015,251.58 (25.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $1,015,251.58 | 25.8% | 20 |
| 4300 | Professional Services | $685,265.57 | 17.4% | 7 |
| 4325 | Attorney General Legal Fees | $675,725.73 | 17.2% | 2 |
| 6050 | Distribution To Non-Profit Org | $349,443.00 | 8.9% | 1 |
| 4425 | Facilities Rent & Taxes | $265,114.75 | 6.7% | 2 |
| 4225 | State Government Service Charges | $230,541.66 | 5.9% | 7 |
| 4715 | It Expendable Property | $141,715.17 | 3.6% | 13 |
| 4650 | Other Services And Supplies | $115,751.18 | 2.9% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $76,829.39 | 2.0% | 9 |
| 5600 | Data Processing Hardware | $71,603.41 | 1.8% | 1 |
| 4450 | Fuels And Utilities | $60,561.82 | 1.5% | 5 |
| 4315 | It Professional Services | $44,458.25 | 1.1% | 3 |
| 4175 | Office Expenses | $36,343.12 | 0.9% | 17 |
| 4700 | Expendable Property $250-$5000 | $35,632.98 | 0.9% | 5 |
| 4125 | Out-Of-State Travel | $26,656.93 | 0.7% | 53 |
| 4100 | Instate Travel | $24,907.25 | 0.6% | 64 |
| 4150 | Employee Training | $21,088.88 | 0.5% | 7 |
| 4250 | Data Processing | $19,423.61 | 0.5% | 9 |
| 5900 | Other Capital Outlay | $17,010.00 | 0.4% | 1 |
| 5550 | Data Processing Software | $14,712.50 | 0.4% | 1 |
| 4375 | Employee Recruitment And Development | $257.03 | 0.0% | 2 |
| 4475 | Facilities Maintenance | $235.90 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 55 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $1,014,859.24 | 25.8% |
| 4500 | Professional Services Non-It | $685,265.57 | 17.4% |
| 4550 | Attorney General Legal Fees | $675,725.73 | 17.2% |
| 6735 | Distribution To Non-Profit Org | $349,443.00 | 8.9% |
| 4800 | Facilities Rent | $265,114.75 | 6.7% |
| 4600 | State Government Service Charges | $230,541.66 | 5.9% |
| 4730 | Merchant Fees | $108,900.81 | 2.8% |
| 5351 | Computer Technology Server Equip>=$5K | $71,603.41 | 1.8% |
| 4825 | Fuels And Utilities | $60,561.82 | 1.5% |
| 4301 | Telecom/Voice Usage | $54,099.25 | 1.4% |
| 4366 | Computer Technology Pc Software<$5K | $45,780.33 | 1.2% |
| 4514 | Professional Services Application Mod | $40,113.75 | 1.0% |

## Curator notes

Figures are aggregated from 235 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='851' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


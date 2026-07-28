---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-851-fy2021
title: Nursing, Brd of — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 851, FY2021
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
  - expenditures-851-fy2020
  - expenditures-851-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-851
- nursing-brd-of
agency_code: '851'
agency_name: NURSING, BRD OF
fiscal_year: 2021
total_expense: '4042938.28'
transaction_count: 116
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Nursing, Brd of — FY2021 expenditures

## At a glance

Nursing, Brd of (agency code 851, recorded upstream as `NURSING, BRD OF`) spent **$4,042,938.28** in fiscal year 2021, across 116 transaction records. That is up 2.9% from $3,928,529.71 in FY2020. The agency accounts for 0.01% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **42 of 76** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $973,495.56 (24.1% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $973,495.56 | 24.1% | 7 |
| 4325 | Attorney General Legal Fees | $751,828.53 | 18.6% | 2 |
| 4300 | Professional Services | $693,323.50 | 17.1% | 8 |
| 6050 | Distribution To Non-Profit Org | $373,617.00 | 9.2% | 1 |
| 4715 | It Expendable Property | $305,036.55 | 7.5% | 13 |
| 4425 | Lease Payments & Taxes | $280,029.99 | 6.9% | 2 |
| 4225 | State Government Service Charges | $216,270.34 | 5.3% | 8 |
| 4650 | Other Services And Supplies | $139,024.39 | 3.4% | 9 |
| 4250 | Data Processing | $104,748.20 | 2.6% | 11 |
| 4200 | Telecomm/Tech Svc And Supplies | $93,252.44 | 2.3% | 12 |
| 4450 | Fuels And Utilities | $57,530.10 | 1.4% | 5 |
| 4175 | Office Expenses | $31,276.15 | 0.8% | 21 |
| 4700 | Expendable Property $250-$5000 | $9,177.28 | 0.2% | 3 |
| 4100 | Instate Travel | $6,248.90 | 0.2% | 5 |
| 4150 | Employee Training | $5,672.50 | 0.1% | 3 |
| 5550 | Data Processing Software | $1,007.50 | 0.0% | 1 |
| 3240 | Unemployment Assessment | $626.90 | 0.0% | 1 |
| 4375 | Employee Recruitment And Development | $581.35 | 0.0% | 1 |
| 4400 | Dues And Subscriptions | $75.00 | 0.0% | 1 |
| 4315 | It Professional Services | $65.00 | 0.0% | 1 |
| 3220 | Public Employes' Retirement System | $51.10 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 41 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $973,014.06 | 24.1% |
| 4550 | Attorney General Legal Fees | $751,828.53 | 18.6% |
| 4500 | Professional Services Non-It | $693,323.50 | 17.1% |
| 6735 | Distribution To Non-Profit Org | $373,617.00 | 9.2% |
| 4800 | Interagency Lease Payments | $280,029.99 | 6.9% |
| 4600 | State Government Service Charges | $216,270.34 | 5.3% |
| 4302 | Telecom/Voice Equip Rental | $147,238.51 | 3.6% |
| 4366 | Computer Technology Pc Software<$5K | $138,344.67 | 3.4% |
| 4730 | Merchant Fees | $137,703.05 | 3.4% |
| 4375 | Computer Technology Computer Processing | $82,551.73 | 2.0% |
| 4301 | Telecom/Voice Usage | $59,280.98 | 1.5% |
| 4825 | Fuels And Utilities | $57,530.10 | 1.4% |

## Curator notes

Figures are aggregated from 116 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='851' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


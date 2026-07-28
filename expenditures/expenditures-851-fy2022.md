---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-851-fy2022
title: Nursing, Brd of — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 851, FY2022
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5378b32aad5d54d03160dd49832cc5c4f45e517dde8ba96c7e5b8bbb6e3a99f4
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
  - expenditures-851-fy2021
  - expenditures-851-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-851
- nursing-brd-of
agency_code: '851'
agency_name: NURSING, BRD OF
fiscal_year: 2022
total_expense: '4519737.62'
transaction_count: 133
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Nursing, Brd of — FY2022 expenditures

## At a glance

Nursing, Brd of (agency code 851, recorded upstream as `NURSING, BRD OF`) spent **$4,519,737.62** in fiscal year 2022, across 133 transaction records. That is up 11.8% from $4,042,938.28 in FY2021. The agency accounts for 0.01% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **40 of 76** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $1,338,533.77 (29.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $1,338,533.77 | 29.6% | 8 |
| 6050 | Distribution To Non-Profit Org | $684,396.00 | 15.1% | 2 |
| 4325 | Attorney General Legal Fees | $646,138.94 | 14.3% | 1 |
| 4300 | Professional Services | $577,290.77 | 12.8% | 7 |
| 4225 | State Government Service Charges | $323,339.55 | 7.2% | 7 |
| 4425 | Lease Payments & Taxes | $317,509.21 | 7.0% | 2 |
| 4650 | Other Services And Supplies | $223,765.39 | 5.0% | 5 |
| 4715 | It Expendable Property | $132,299.22 | 2.9% | 12 |
| 4315 | It Professional Services | $106,300.00 | 2.4% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $66,369.29 | 1.5% | 11 |
| 4250 | Data Processing | $30,734.78 | 0.7% | 12 |
| 4450 | Fuels And Utilities | $29,862.00 | 0.7% | 5 |
| 4175 | Office Expenses | $21,314.67 | 0.5% | 19 |
| 4150 | Employee Training | $8,087.26 | 0.2% | 3 |
| 4125 | Out-Of-State Travel | $4,953.90 | 0.1% | 15 |
| 4700 | Expendable Property $250-$5000 | $3,764.75 | 0.1% | 2 |
| 4100 | Instate Travel | $3,464.25 | 0.1% | 17 |
| 4400 | Dues And Subscriptions | $1,465.19 | 0.0% | 2 |
| 3240 | Unemployment Assessment | $101.08 | 0.0% | 1 |
| 3220 | Public Employes' Retirement System | $47.60 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 44 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $1,338,407.17 | 29.6% |
| 6735 | Distribution To Non-Profit Org | $684,396.00 | 15.1% |
| 4550 | Attorney General Legal Fees | $646,138.94 | 14.3% |
| 4500 | Professional Services Non-It | $577,290.77 | 12.8% |
| 4600 | State Government Service Charges | $323,339.55 | 7.2% |
| 4800 | Interagency Lease Payments | $317,509.21 | 7.0% |
| 4730 | Merchant Fees | $221,769.32 | 4.9% |
| 4515 | Professional Services Application Maint | $106,300.00 | 2.4% |
| 4366 | Computer Technology Pc Software<$5K | $82,590.36 | 1.8% |
| 4301 | Telecom/Voice Usage | $51,685.68 | 1.1% |
| 4825 | Fuels And Utilities | $29,862.00 | 0.7% |
| 4302 | Telecom/Voice Equip Rental | $26,607.59 | 0.6% |

## Curator notes

Figures are aggregated from 133 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='851' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


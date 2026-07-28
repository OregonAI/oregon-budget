---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-847-fy2024
title: Medical Brd, OR — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 847, FY2024
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: decef95a644d748f5c62eca57f2ec65a1ac01802ec192ae6fe9a4da7eed2a7c0
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
  - expenditures-847-fy2023
  - expenditures-847-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-847
- medical-brd-or
agency_code: '847'
agency_name: MEDICAL BRD, OR
fiscal_year: 2024
total_expense: '3087966.36'
transaction_count: 144
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Medical Brd, OR — FY2024 expenditures

## At a glance

Medical Brd, OR (agency code 847, recorded upstream as `MEDICAL BRD, OR`) spent **$3,087,966.36** in fiscal year 2024, across 144 transaction records. That is up 20.7% from $2,559,012.31 in FY2023. The agency accounts for 0.01% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **50 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $647,734.34 (21.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $647,734.34 | 21.0% | 20 |
| 4325 | Attorney General Legal Fees | $587,932.84 | 19.0% | 2 |
| 4425 | Lease Payments & Taxes | $395,713.45 | 12.8% | 3 |
| 4650 | Other Services And Supplies | $321,273.08 | 10.4% | 7 |
| 4400 | Dues And Subscriptions | $296,145.72 | 9.6% | 2 |
| 4315 | It Professional Services | $268,678.71 | 8.7% | 3 |
| 4225 | State Government Service Charges | $267,620.02 | 8.7% | 3 |
| 4575 | Agency Program Related Svcs & Supp | $121,608.25 | 3.9% | 2 |
| 4175 | Office Expenses | $89,955.45 | 2.9% | 17 |
| 4150 | Employee Training | $32,238.32 | 1.0% | 44 |
| 4200 | Telecomm/Tech Svc And Supplies | $29,731.80 | 1.0% | 4 |
| 4100 | Instate Travel | $9,944.04 | 0.3% | 30 |
| 4715 | It Expendable Property | $7,914.69 | 0.3% | 2 |
| 3240 | Unemployment Assessment | $6,721.00 | 0.2% | 1 |
| 4700 | Expendable Property $250-$5000 | $3,205.89 | 0.1% | 2 |
| 4250 | Data Processing | $1,548.76 | 0.1% | 2 |

## Largest expenditure classes

The 12 largest of 46 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $587,932.84 | 19.0% |
| 4500 | Professional Services Non-It | $522,734.34 | 16.9% |
| 4251 | Subscriptions And Publications | $296,145.72 | 9.6% |
| 7007 | Lease Pmt For Buildings | $295,590.96 | 9.6% |
| 4730 | Merchant Fees | $291,989.19 | 9.5% |
| 4600 | State Government Service Charges | $267,620.02 | 8.7% |
| 4513 | Professional Services Application New | $257,300.00 | 8.3% |
| 4505 | Professional Services Non-It>$75K | $125,000.00 | 4.0% |
| 4975 | Agency Program Related Services | $121,608.25 | 3.9% |
| 4200 | Office Supplies | $70,892.57 | 2.3% |
| 7401 | Interest-Leased Assets | $61,248.56 | 2.0% |
| 4800 | Interagency Lease Payments | $38,873.93 | 1.3% |

## Curator notes

Figures are aggregated from 144 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='847' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


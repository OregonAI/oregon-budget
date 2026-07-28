---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-119-fy2024
title: Tax Practitioners, St Brd of — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 119, FY2024
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
  - expenditures-119-fy2023
  - expenditures-119-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-119
- tax-practitioners-st-brd-of
agency_code: '119'
agency_name: TAX PRACTITIONERS, ST BRD OF
fiscal_year: 2024
total_expense: '155942.45'
transaction_count: 30
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Tax Practitioners, St Brd of — FY2024 expenditures

## At a glance

Tax Practitioners, St Brd of (agency code 119, recorded upstream as `TAX PRACTITIONERS, ST BRD OF`) spent **$155,942.45** in fiscal year 2024, across 30 transaction records. That is down 52.5% from $328,352.39 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **75 of 80** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $58,729.11 (37.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $58,729.11 | 37.7% | 5 |
| 4325 | Attorney General Legal Fees | $42,016.48 | 26.9% | 1 |
| 4315 | It Professional Services | $20,826.00 | 13.4% | 2 |
| 4225 | State Government Service Charges | $18,910.72 | 12.1% | 4 |
| 4250 | Data Processing | $6,997.94 | 4.5% | 2 |
| 4715 | It Expendable Property | $2,966.18 | 1.9% | 2 |
| 4300 | Professional Services | $2,550.00 | 1.6% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $1,623.78 | 1.0% | 5 |
| 4100 | Instate Travel | $985.58 | 0.6% | 6 |
| 4175 | Office Expenses | $300.85 | 0.2% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $35.81 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 17 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4701 | Other Services | $45,303.21 | 29.1% |
| 4550 | Attorney General Legal Fees | $42,016.48 | 26.9% |
| 4600 | State Government Service Charges | $18,910.72 | 12.1% |
| 4515 | Professional Services Application Maint | $18,000.00 | 11.5% |
| 4730 | Merchant Fees | $12,463.88 | 8.0% |
| 4367 | Computer Technology Pc Support | $5,532.50 | 3.5% |
| 4519 | Professional Serv/Managed Serv Provider | $2,826.00 | 1.8% |
| 4500 | Professional Services Non-It | $2,550.00 | 1.6% |
| 4365 | Computer Technology Pc Equipment<$5K | $1,974.20 | 1.3% |
| 4375 | Computer Technology Computer Processing | $1,465.44 | 0.9% |
| 4305 | Telecom/Network Services | $1,083.30 | 0.7% |
| 4372 | Computer Technology Peripheral Equip<$5K | $991.98 | 0.6% |

## Curator notes

Figures are aggregated from 30 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='119' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


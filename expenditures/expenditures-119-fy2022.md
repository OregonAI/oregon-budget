---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-119-fy2022
title: Tax Practitioners, St Brd of — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 119, FY2022
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
  - expenditures-119-fy2021
  - expenditures-119-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-119
- tax-practitioners-st-brd-of
agency_code: '119'
agency_name: TAX PRACTITIONERS, ST BRD OF
fiscal_year: 2022
total_expense: '267207.76'
transaction_count: 25
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Tax Practitioners, St Brd of — FY2022 expenditures

## At a glance

Tax Practitioners, St Brd of (agency code 119, recorded upstream as `TAX PRACTITIONERS, ST BRD OF`) spent **$267,207.76** in fiscal year 2022, across 25 transaction records. That is up 71.8% from $155,524.62 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **69 of 76** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $89,952.30 (33.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $89,952.30 | 33.7% | 5 |
| 4225 | State Government Service Charges | $52,331.20 | 19.6% | 4 |
| 4325 | Attorney General Legal Fees | $49,134.80 | 18.4% | 1 |
| 4425 | Lease Payments & Taxes | $35,527.25 | 13.3% | 2 |
| 4315 | It Professional Services | $21,956.00 | 8.2% | 2 |
| 4250 | Data Processing | $11,190.00 | 4.2% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $2,795.56 | 1.0% | 5 |
| 4300 | Professional Services | $2,255.15 | 0.8% | 1 |
| 4175 | Office Expenses | $1,973.66 | 0.7% | 1 |
| 4100 | Instate Travel | $91.84 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 15 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4701 | Other Services | $64,516.78 | 24.1% |
| 4600 | State Government Service Charges | $52,331.20 | 19.6% |
| 4550 | Attorney General Legal Fees | $49,134.80 | 18.4% |
| 4800 | Interagency Lease Payments | $35,527.25 | 13.3% |
| 4515 | Professional Services Application Maint | $18,000.00 | 6.7% |
| 4720 | Collection Fees - Dor | $15,269.26 | 5.7% |
| 4730 | Merchant Fees | $10,166.26 | 3.8% |
| 4367 | Computer Technology Pc Support | $8,250.00 | 3.1% |
| 4519 | Professional Serv/Managed Serv Provider | $3,956.00 | 1.5% |
| 4375 | Computer Technology Computer Processing | $2,940.00 | 1.1% |
| 4500 | Professional Services Non-It | $2,255.15 | 0.8% |
| 4201 | Office Services | $1,973.66 | 0.7% |

## Curator notes

Figures are aggregated from 25 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='119' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


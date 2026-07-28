---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-833-fy2024
title: Health Related Licensing Brds — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 833, FY2024
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
  - expenditures-833-fy2023
  - expenditures-833-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-833
- health-related-licensing-brds
agency_code: '833'
agency_name: HEALTH RELATED LICENSING BRDs
fiscal_year: 2024
total_expense: '1408584.51'
transaction_count: 294
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Health Related Licensing Brds — FY2024 expenditures

## At a glance

Health Related Licensing Brds (agency code 833, recorded upstream as `HEALTH RELATED LICENSING BRDs`) spent **$1,408,584.51** in fiscal year 2024, across 294 transaction records. That is up 23.7% from $1,139,034.90 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **56 of 80** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $426,302.50 (30.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $426,302.50 | 30.3% | 65 |
| 4650 | Other Services And Supplies | $255,125.61 | 18.1% | 16 |
| 4325 | Attorney General Legal Fees | $251,329.15 | 17.8% | 7 |
| 4425 | Lease Payments & Taxes | $189,770.57 | 13.5% | 6 |
| 4225 | State Government Service Charges | $122,602.92 | 8.7% | 23 |
| 4315 | It Professional Services | $35,176.50 | 2.5% | 7 |
| 4200 | Telecomm/Tech Svc And Supplies | $34,477.67 | 2.4% | 33 |
| 4175 | Office Expenses | $22,832.94 | 1.6% | 22 |
| 4300 | Professional Services | $22,742.47 | 1.6% | 11 |
| 4715 | It Expendable Property | $15,116.81 | 1.1% | 7 |
| 4100 | Instate Travel | $14,848.21 | 1.1% | 77 |
| 4250 | Data Processing | $11,478.56 | 0.8% | 7 |
| 4400 | Dues And Subscriptions | $4,100.00 | 0.3% | 1 |
| 4150 | Employee Training | $1,409.08 | 0.1% | 3 |
| 4275 | Publicity & Publications | $523.58 | 0.0% | 4 |
| 4125 | Out-Of-State Travel | $461.25 | 0.0% | 3 |
| 4475 | Facilities Maintenance | $212.50 | 0.0% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $74.19 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 34 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $426,302.50 | 30.3% |
| 4550 | Attorney General Legal Fees | $251,329.15 | 17.8% |
| 4800 | Interagency Lease Payments | $189,770.57 | 13.5% |
| 4701 | Other Services | $160,026.12 | 11.4% |
| 4600 | State Government Service Charges | $122,602.92 | 8.7% |
| 4730 | Merchant Fees | $93,100.92 | 6.6% |
| 4519 | Professional Serv/Managed Serv Provider | $35,176.50 | 2.5% |
| 4500 | Professional Services Non-It | $22,742.47 | 1.6% |
| 4301 | Telecom/Voice Usage | $20,116.21 | 1.4% |
| 4366 | Computer Technology Pc Software<$5K | $13,848.63 | 1.0% |
| 4200 | Office Supplies | $13,245.21 | 0.9% |
| 4375 | Computer Technology Computer Processing | $11,478.56 | 0.8% |

## Curator notes

Figures are aggregated from 294 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='833' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


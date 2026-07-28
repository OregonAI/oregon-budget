---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-584-fy2025
title: Teacher Standards & Practices — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 584, FY2025
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5e9f0c30287913ac0bfff8d74a1225d0c2816ca6a307f2141ebb35602c5a91ed
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
  - expenditures-584-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-584
- teacher-standards-practices
agency_code: '584'
agency_name: TEACHER STANDARDS & PRACTICES
fiscal_year: 2025
total_expense: '2506425.39'
transaction_count: 129
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Teacher Standards & Practices — FY2025 expenditures

## At a glance

Teacher Standards & Practices (agency code 584, recorded upstream as `TEACHER STANDARDS & PRACTICES`) spent **$2,506,425.39** in fiscal year 2025, across 129 transaction records. That is up 18.7% from $2,111,127.07 in FY2024. The agency accounts for 0.01% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **51 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $687,971.32 (27.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $687,971.32 | 27.4% | 15 |
| 4325 | Attorney General Legal Fees | $325,605.85 | 13.0% | 1 |
| 4225 | State Government Service Charges | $312,530.64 | 12.5% | 4 |
| 4575 | Agency Program Related Svcs & Supp | $285,685.00 | 11.4% | 1 |
| 4315 | It Professional Services | $266,550.00 | 10.6% | 2 |
| 4425 | Lease Payments & Taxes | $196,053.40 | 7.8% | 1 |
| 4650 | Other Services And Supplies | $163,593.48 | 6.5% | 8 |
| 4250 | Data Processing | $106,337.79 | 4.2% | 3 |
| 4715 | It Expendable Property | $42,719.04 | 1.7% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $40,732.21 | 1.6% | 5 |
| 4400 | Dues And Subscriptions | $29,923.75 | 1.2% | 4 |
| 4175 | Office Expenses | $23,685.31 | 0.9% | 8 |
| 4150 | Employee Training | $14,144.88 | 0.6% | 65 |
| 3240 | Unemployment Assessment | $8,932.00 | 0.4% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $869.02 | 0.0% | 1 |
| 4100 | Instate Travel | $800.50 | 0.0% | 7 |
| 4275 | Publicity & Publications | $291.20 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 33 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $687,971.32 | 27.4% |
| 4550 | Attorney General Legal Fees | $325,605.85 | 13.0% |
| 4600 | State Government Service Charges | $312,530.64 | 12.5% |
| 4975 | Agency Program Related Services | $285,685.00 | 11.4% |
| 4516 | Professional Services Servers | $266,550.00 | 10.6% |
| 4800 | Interagency Lease Payments | $196,053.40 | 7.8% |
| 4701 | Other Services | $89,431.97 | 3.6% |
| 4367 | Computer Technology Pc Support | $82,987.00 | 3.3% |
| 4730 | Merchant Fees | $74,161.51 | 3.0% |
| 4301 | Telecom/Voice Usage | $30,326.45 | 1.2% |
| 4365 | Computer Technology Pc Equipment<$5K | $23,819.38 | 1.0% |
| 4375 | Computer Technology Computer Processing | $23,350.79 | 0.9% |

## Curator notes

Figures are aggregated from 129 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='584' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


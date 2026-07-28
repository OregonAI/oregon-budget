---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-115-fy2024
title: Employment Relations Brd — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 115, FY2024
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
  - expenditures-115-fy2023
  - expenditures-115-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-115
- employment-relations-brd
agency_code: '115'
agency_name: EMPLOYMENT RELATIONS BRD
fiscal_year: 2024
total_expense: '320984.15'
transaction_count: 37
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Employment Relations Brd — FY2024 expenditures

## At a glance

Employment Relations Brd (agency code 115, recorded upstream as `EMPLOYMENT RELATIONS BRD`) spent **$320,984.15** in fiscal year 2024, across 37 transaction records. That is down 17.2% from $387,590.95 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **71 of 80** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $76,639.95 (23.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $76,639.95 | 23.9% | 4 |
| 4315 | It Professional Services | $65,000.00 | 20.3% | 1 |
| 4650 | Other Services And Supplies | $64,884.60 | 20.2% | 2 |
| 4425 | Lease Payments & Taxes | $39,249.24 | 12.2% | 1 |
| 4250 | Data Processing | $37,377.59 | 11.6% | 2 |
| 4715 | It Expendable Property | $15,722.38 | 4.9% | 2 |
| 4100 | Instate Travel | $13,478.86 | 4.2% | 14 |
| 4125 | Out-Of-State Travel | $5,594.64 | 1.7% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $1,233.00 | 0.4% | 2 |
| 4275 | Publicity & Publications | $812.15 | 0.3% | 1 |
| 4175 | Office Expenses | $807.73 | 0.3% | 1 |
| 4400 | Dues And Subscriptions | $75.25 | 0.0% | 1 |
| 4325 | Attorney General Legal Fees | $48.40 | 0.0% | 1 |
| 4300 | Professional Services | $45.36 | 0.0% | 1 |
| 3220 | Public Employes' Retirement System | $15.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 24 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $76,639.95 | 23.9% |
| 4515 | Professional Services Application Maint | $65,000.00 | 20.3% |
| 4701 | Other Services | $64,884.60 | 20.2% |
| 4800 | Interagency Lease Payments | $39,249.24 | 12.2% |
| 4367 | Computer Technology Pc Support | $35,961.00 | 11.2% |
| 4365 | Computer Technology Pc Equipment<$5K | $15,433.04 | 4.8% |
| 4101 | Instate Meals With Overnight Stay | $6,247.75 | 1.9% |
| 4159 | Out-Of-State Air Transportation | $4,101.11 | 1.3% |
| 4108 | Instate Ground Transportation | $3,039.86 | 0.9% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $1,824.08 | 0.6% |
| 4375 | Computer Technology Computer Processing | $1,416.59 | 0.4% |
| 4110 | Instate Mileage Reimbursmnt-Reduced Rate | $1,412.92 | 0.4% |

## Curator notes

Figures are aggregated from 37 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='115' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


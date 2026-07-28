---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-404-fy2024
title: Public Defense Services — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 404, FY2024
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
  - expenditures-404-fy2023
  - expenditures-404-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-404
- public-defense-services
agency_code: '404'
agency_name: PUBLIC DEFENSE SERVICES
fiscal_year: 2024
total_expense: '234822311.92'
transaction_count: 1887
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Public Defense Services — FY2024 expenditures

## At a glance

Public Defense Services (agency code 404, recorded upstream as `PUBLIC DEFENSE SERVICES`) spent **$234,822,311.92** in fiscal year 2024, across 1,887 transaction records. That is up 13.1% from $207,705,135.47 in FY2023. The agency accounts for 0.74% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **14 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $225,472,706.16 (96.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $225,472,706.16 | 96.0% | 708 |
| 4575 | Agency Program Related Svcs & Supp | $3,393,542.59 | 1.4% | 267 |
| 4100 | Instate Travel | $1,451,697.99 | 0.6% | 640 |
| 4425 | Lease Payments & Taxes | $1,026,018.70 | 0.4% | 13 |
| 6198 | Dist To Judicial | $860,313.08 | 0.4% | 1 |
| 4315 | It Professional Services | $632,251.80 | 0.3% | 4 |
| 4225 | State Government Service Charges | $554,187.50 | 0.2% | 4 |
| 4715 | It Expendable Property | $454,056.89 | 0.2% | 16 |
| 4150 | Employee Training | $193,367.74 | 0.1% | 166 |
| 4325 | Attorney General Legal Fees | $186,130.15 | 0.1% | 3 |
| 5900 | Other Capital Outlay | $158,170.73 | 0.1% | 2 |
| 4250 | Data Processing | $99,218.37 | 0.0% | 7 |
| 4650 | Other Services And Supplies | $96,200.25 | 0.0% | 11 |
| 4200 | Telecomm/Tech Svc And Supplies | $69,313.63 | 0.0% | 6 |
| 4175 | Office Expenses | $65,038.09 | 0.0% | 16 |
| 4700 | Expendable Property $250-$5000 | $49,262.67 | 0.0% | 2 |
| 4475 | Facilities Maintenance | $28,880.36 | 0.0% | 8 |
| 4400 | Dues And Subscriptions | $24,077.75 | 0.0% | 7 |
| 3220 | Public Employes' Retirement System | $3,229.32 | 0.0% | 1 |
| 4275 | Publicity & Publications | $2,691.35 | 0.0% | 3 |
| 4125 | Out-Of-State Travel | $1,956.80 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 67 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $225,472,706.16 | 96.0% |
| 4977 | Agency Program Related Reimbursements | $3,379,549.76 | 1.4% |
| 4112 | Instate Mileage Reimbursmnt-Nonemployee | $1,045,132.91 | 0.4% |
| 6132 | Distribution To Judicial 198 | $860,313.08 | 0.4% |
| 7007 | Lease Pmt For Buildings | $701,594.86 | 0.3% |
| 4519 | Professional Serv/Managed Serv Provider | $632,251.80 | 0.3% |
| 4600 | State Government Service Charges | $554,187.50 | 0.2% |
| 4104 | Instate Travel Miscellaneous Expenses | $248,685.65 | 0.1% |
| 4550 | Attorney General Legal Fees | $186,130.15 | 0.1% |
| 4800 | Interagency Lease Payments | $178,144.12 | 0.1% |
| 4365 | Computer Technology Pc Equipment<$5K | $170,242.48 | 0.1% |
| 5755 | Leasehold Improvements>=$5K | $158,170.73 | 0.1% |

## Curator notes

Figures are aggregated from 1,887 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='404' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


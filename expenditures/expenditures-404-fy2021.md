---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-404-fy2021
title: Public Defense Services — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 404, FY2021
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
  - expenditures-404-fy2020
  - expenditures-404-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-404
- public-defense-services
agency_code: '404'
agency_name: PUBLIC DEFENSE SERVICES
fiscal_year: 2021
total_expense: '160714252.25'
transaction_count: 1479
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Public Defense Services — FY2021 expenditures

## At a glance

Public Defense Services (agency code 404, recorded upstream as `PUBLIC DEFENSE SERVICES`) spent **$160,714,252.25** in fiscal year 2021, across 1,479 transaction records. That is up 7.1% from $150,109,933.22 in FY2020. The agency accounts for 0.60% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **15 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $153,067,176.77 (95.2% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $153,067,176.77 | 95.2% | 706 |
| 4575 | Agency Program Related Svcs & Supp | $2,749,919.08 | 1.7% | 278 |
| 6198 | Dist To Judicial | $1,598,462.90 | 1.0% | 1 |
| 4315 | It Professional Services | $1,173,482.99 | 0.7% | 3 |
| 4100 | Instate Travel | $617,148.82 | 0.4% | 404 |
| 4425 | Lease Payments & Taxes | $550,224.22 | 0.3% | 6 |
| 4225 | State Government Service Charges | $355,103.92 | 0.2% | 5 |
| 4700 | Expendable Property $250-$5000 | $123,779.05 | 0.1% | 4 |
| 4715 | It Expendable Property | $103,625.18 | 0.1% | 8 |
| 4175 | Office Expenses | $77,536.36 | 0.0% | 15 |
| 4150 | Employee Training | $71,058.74 | 0.0% | 21 |
| 4650 | Other Services And Supplies | $64,311.30 | 0.0% | 4 |
| 4250 | Data Processing | $53,767.25 | 0.0% | 6 |
| 5550 | Data Processing Software | $26,334.21 | 0.0% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $22,374.95 | 0.0% | 4 |
| 4325 | Attorney General Legal Fees | $16,455.60 | 0.0% | 1 |
| 5600 | Data Processing Hardware | $16,099.34 | 0.0% | 1 |
| 4400 | Dues And Subscriptions | $12,458.56 | 0.0% | 7 |
| 3240 | Unemployment Assessment | $11,847.25 | 0.0% | 1 |
| 4275 | Publicity & Publications | $1,635.78 | 0.0% | 1 |
| 4525 | Medical Supplies And Services | $1,449.98 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 39 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $153,067,176.77 | 95.2% |
| 4977 | Agency Program Related Reimbursements | $2,749,919.08 | 1.7% |
| 6132 | Distribution To Judicial 198 | $1,598,462.90 | 1.0% |
| 4519 | Professional Serv/Managed Serv Provider | $1,173,482.99 | 0.7% |
| 4112 | Instate Mileage Reimbursmnt-Nonemployee | $587,011.92 | 0.4% |
| 4800 | Facilities Rent | $550,224.22 | 0.3% |
| 4600 | State Government Service Charges | $355,103.92 | 0.2% |
| 4999 | Expendable Property Non-It<$5K | $123,779.05 | 0.1% |
| 4701 | Other Services | $64,234.23 | 0.0% |
| 4437 | Prof Dev Dues/Membership | $58,165.49 | 0.0% |
| 4375 | Computer Technology Computer Processing | $53,072.61 | 0.0% |
| 4366 | Computer Technology Pc Software<$5K | $51,169.73 | 0.0% |

## Curator notes

Figures are aggregated from 1,479 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='404' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


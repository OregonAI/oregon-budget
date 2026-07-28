---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-115-fy2023
title: Employment Relations Brd — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 115, FY2023
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 6400163010ab2f341831c864272a89c5e9f2a261fad3fd9572b230042f26e3d5
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
  - expenditures-115-fy2022
  - expenditures-115-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-115
- employment-relations-brd
agency_code: '115'
agency_name: EMPLOYMENT RELATIONS BRD
fiscal_year: 2023
total_expense: '387590.95'
transaction_count: 49
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Employment Relations Brd — FY2023 expenditures

## At a glance

Employment Relations Brd (agency code 115, recorded upstream as `EMPLOYMENT RELATIONS BRD`) spent **$387,590.95** in fiscal year 2023, across 49 transaction records. That is down 12.2% from $441,261.33 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **67 of 77** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $91,661.97 (23.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $91,661.97 | 23.6% | 1 |
| 4315 | It Professional Services | $65,000.00 | 16.8% | 1 |
| 4425 | Lease Payments & Taxes | $61,055.40 | 15.8% | 2 |
| 4225 | State Government Service Charges | $60,056.52 | 15.5% | 4 |
| 4250 | Data Processing | $37,820.90 | 9.8% | 4 |
| 4715 | It Expendable Property | $25,130.43 | 6.5% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $17,618.53 | 4.5% | 6 |
| 4175 | Office Expenses | $13,360.95 | 3.4% | 8 |
| 4100 | Instate Travel | $10,321.57 | 2.7% | 14 |
| 3220 | Public Employes' Retirement System | $2,848.77 | 0.7% | 1 |
| 4125 | Out-Of-State Travel | $1,478.82 | 0.4% | 1 |
| 4275 | Publicity & Publications | $640.48 | 0.2% | 1 |
| 4400 | Dues And Subscriptions | $584.25 | 0.2% | 2 |
| 4300 | Professional Services | $12.36 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 27 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4701 | Other Services | $91,661.97 | 23.6% |
| 4515 | Professional Services Application Maint | $65,000.00 | 16.8% |
| 4800 | Interagency Lease Payments | $61,055.40 | 15.8% |
| 4600 | State Government Service Charges | $60,056.52 | 15.5% |
| 4367 | Computer Technology Pc Support | $35,751.00 | 9.2% |
| 4366 | Computer Technology Pc Software<$5K | $14,179.84 | 3.7% |
| 4201 | Office Services | $13,030.95 | 3.4% |
| 4365 | Computer Technology Pc Equipment<$5K | $10,950.59 | 2.8% |
| 4305 | Telecom/Network Services | $8,735.69 | 2.3% |
| 4301 | Telecom/Voice Usage | $5,327.23 | 1.4% |
| 4108 | Instate Ground Transportation | $4,681.72 | 1.2% |
| 4101 | Instate Meals With Overnight Stay | $4,381.42 | 1.1% |

## Curator notes

Figures are aggregated from 49 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='115' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


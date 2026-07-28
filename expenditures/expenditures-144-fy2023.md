---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-144-fy2023
title: Legislative Rev Office — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 144, FY2023
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
  - expenditures-144-fy2022
  - expenditures-144-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-144
- legislative-rev-office
agency_code: '144'
agency_name: LEGISLATIVE REV OFFICE
fiscal_year: 2023
total_expense: '64934.50'
transaction_count: 37
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Rev Office — FY2023 expenditures

## At a glance

Legislative Rev Office (agency code 144, recorded upstream as `LEGISLATIVE REV OFFICE`) spent **$64,934.50** in fiscal year 2023, across 37 transaction records. That is down 39.8% from $107,840.89 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **75 of 77** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $20,779.53 (32.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $20,779.53 | 32.0% | 3 |
| 4715 | It Expendable Property | $15,952.22 | 24.6% | 6 |
| 4300 | Professional Services | $10,500.00 | 16.2% | 1 |
| 4400 | Dues And Subscriptions | $5,445.96 | 8.4% | 3 |
| 4175 | Office Expenses | $4,162.50 | 6.4% | 9 |
| 4275 | Publicity & Publications | $2,943.00 | 4.5% | 2 |
| 4125 | Out-Of-State Travel | $2,296.23 | 3.5% | 7 |
| 4150 | Employee Training | $1,390.00 | 2.1% | 2 |
| 4650 | Other Services And Supplies | $1,226.28 | 1.9% | 3 |
| 4250 | Data Processing | $238.78 | 0.4% | 1 |

## Largest expenditure classes

The 12 largest of 20 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $20,779.53 | 32.0% |
| 4366 | Computer Technology Pc Software<$5K | $13,477.39 | 20.8% |
| 4500 | Professional Services Non-It | $10,500.00 | 16.2% |
| 4251 | Subscriptions And Publications | $5,445.96 | 8.4% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $2,943.00 | 4.5% |
| 4202 | Equipment Rental | $2,681.49 | 4.1% |
| 4365 | Computer Technology Pc Equipment<$5K | $2,297.53 | 3.5% |
| 4150 | Out-Of-State Lodging | $1,267.45 | 2.0% |
| 4411 | Prof Dev Out-Of-State Tuition/Regist | $1,215.00 | 1.9% |
| 4704 | Other Supplies | $1,211.28 | 1.9% |
| 4201 | Office Services | $840.16 | 1.3% |
| 4200 | Office Supplies | $640.85 | 1.0% |

## Curator notes

Figures are aggregated from 37 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='144' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


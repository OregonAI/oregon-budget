---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-143-fy2021
title: Legislative Pol & Research Cmte — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 143, FY2021
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
  - expenditures-143-fy2020
  - expenditures-143-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-143
- legislative-pol-research-cmte
agency_code: '143'
agency_name: LEGISLATIVE POL & RESEARCH CMTE
fiscal_year: 2021
total_expense: '223683.39'
transaction_count: 57
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Pol & Research Cmte — FY2021 expenditures

## At a glance

Legislative Pol & Research Cmte (agency code 143, recorded upstream as `LEGISLATIVE POL & RESEARCH CMTE`) spent **$223,683.39** in fiscal year 2021, across 57 transaction records. That is down 20.3% from $280,722.07 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **68 of 76** agencies reporting that year.

The largest budget category was **It Expendable Property** at $84,341.50 (37.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4715 | It Expendable Property | $84,341.50 | 37.7% | 3 |
| 4225 | State Government Service Charges | $75,559.90 | 33.8% | 4 |
| 4150 | Employee Training | $16,681.00 | 7.5% | 6 |
| 4250 | Data Processing | $15,153.74 | 6.8% | 1 |
| 4175 | Office Expenses | $11,901.03 | 5.3% | 16 |
| 3240 | Unemployment Assessment | $5,903.95 | 2.6% | 1 |
| 4650 | Other Services And Supplies | $3,844.70 | 1.7% | 6 |
| 4300 | Professional Services | $3,324.00 | 1.5% | 2 |
| 4400 | Dues And Subscriptions | $2,833.00 | 1.3% | 2 |
| 4375 | Employee Recruitment And Development | $1,424.70 | 0.6% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $1,019.15 | 0.5% | 5 |
| 3160 | Temporary Appointments | $990.00 | 0.4% | 1 |
| 4100 | Instate Travel | $497.99 | 0.2% | 4 |
| 4275 | Publicity & Publications | $130.00 | 0.1% | 1 |
| 3230 | Social Security Tax | $75.73 | 0.0% | 1 |
| 3210 | Erb Assessment | $2.34 | 0.0% | 1 |
| 3250 | Workers' Compensation Assessment | $0.66 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 27 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4365 | Computer Technology Pc Equipment<$5K | $78,994.14 | 35.3% |
| 4600 | State Government Service Charges | $75,559.90 | 33.8% |
| 4367 | Computer Technology Pc Support | $15,153.74 | 6.8% |
| 4411 | Prof Dev Out-Of-State Tuition/Regist | $6,950.00 | 3.1% |
| 3231 | Unemployment Compensation & Assessment | $5,903.95 | 2.6% |
| 4406 | Prof Dev Instate Tuition/Registration | $5,889.00 | 2.6% |
| 4200 | Office Supplies | $5,730.12 | 2.6% |
| 4202 | Equipment Rental | $5,357.76 | 2.4% |
| 4366 | Computer Technology Pc Software<$5K | $5,347.36 | 2.4% |
| 4701 | Other Services | $3,844.70 | 1.7% |
| 4437 | Prof Dev Dues/Membership | $3,802.00 | 1.7% |
| 4500 | Professional Services Non-It | $3,324.00 | 1.5% |

## Curator notes

Figures are aggregated from 57 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='143' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


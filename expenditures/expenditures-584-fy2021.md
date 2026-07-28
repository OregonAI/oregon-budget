---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-584-fy2021
title: Teacher Standards & Practices — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 584, FY2021
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
  - expenditures-584-fy2020
  - expenditures-584-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-584
- teacher-standards-practices
agency_code: '584'
agency_name: TEACHER STANDARDS & PRACTICES
fiscal_year: 2021
total_expense: '905797.04'
transaction_count: 43
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Teacher Standards & Practices — FY2021 expenditures

## At a glance

Teacher Standards & Practices (agency code 584, recorded upstream as `TEACHER STANDARDS & PRACTICES`) spent **$905,797.04** in fiscal year 2021, across 43 transaction records. That is down 15.6% from $1,073,159.32 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **55 of 76** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $188,260.00 (20.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $188,260.00 | 20.8% | 1 |
| 4425 | Lease Payments & Taxes | $169,726.86 | 18.7% | 1 |
| 4325 | Attorney General Legal Fees | $154,850.24 | 17.1% | 1 |
| 4225 | State Government Service Charges | $130,165.38 | 14.4% | 4 |
| 4650 | Other Services And Supplies | $94,630.66 | 10.4% | 4 |
| 4250 | Data Processing | $69,492.45 | 7.7% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $34,880.89 | 3.9% | 4 |
| 4175 | Office Expenses | $25,660.49 | 2.8% | 7 |
| 4300 | Professional Services | $16,436.46 | 1.8% | 5 |
| 4400 | Dues And Subscriptions | $8,750.00 | 1.0% | 1 |
| 4715 | It Expendable Property | $5,857.94 | 0.6% | 2 |
| 3110 | Class/Unclass Salary & Per Diem | $2,692.50 | 0.3% | 1 |
| 4475 | Facilities Maintenance | $2,367.50 | 0.3% | 1 |
| 4275 | Publicity & Publications | $1,448.63 | 0.2% | 2 |
| 4100 | Instate Travel | $333.56 | 0.0% | 2 |
| 4125 | Out-Of-State Travel | $133.48 | 0.0% | 2 |
| 4150 | Employee Training | $110.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 26 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $188,260.00 | 20.8% |
| 4800 | Interagency Lease Payments | $169,726.86 | 18.7% |
| 4550 | Attorney General Legal Fees | $154,850.24 | 17.1% |
| 4600 | State Government Service Charges | $130,165.38 | 14.4% |
| 4367 | Computer Technology Pc Support | $57,935.52 | 6.4% |
| 4730 | Merchant Fees | $57,880.72 | 6.4% |
| 4701 | Other Services | $36,726.59 | 4.1% |
| 4301 | Telecom/Voice Usage | $21,240.23 | 2.3% |
| 4200 | Office Supplies | $19,475.99 | 2.2% |
| 4500 | Professional Services Non-It | $16,436.46 | 1.8% |
| 4305 | Telecom/Network Services | $13,640.66 | 1.5% |
| 4375 | Computer Technology Computer Processing | $11,556.93 | 1.3% |

## Curator notes

Figures are aggregated from 43 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='584' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-811-fy2024
title: Chiropractic Exam, Brd of — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 811, FY2024
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
  - expenditures-811-fy2023
  - expenditures-811-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-811
- chiropractic-exam-brd-of
agency_code: '811'
agency_name: CHIROPRACTIC EXAM, BRD OF
fiscal_year: 2024
total_expense: '481826.46'
transaction_count: 86
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Chiropractic Exam, Brd of — FY2024 expenditures

## At a glance

Chiropractic Exam, Brd of (agency code 811, recorded upstream as `CHIROPRACTIC EXAM, BRD OF`) spent **$481,826.46** in fiscal year 2024, across 86 transaction records. That is up 39.8% from $344,580.76 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **67 of 80** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $190,223.51 (39.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $190,223.51 | 39.5% | 1 |
| 4650 | Other Services And Supplies | $80,689.22 | 16.7% | 5 |
| 4425 | Lease Payments & Taxes | $55,282.79 | 11.5% | 1 |
| 4225 | State Government Service Charges | $40,617.00 | 8.4% | 6 |
| 4300 | Professional Services | $36,109.19 | 7.5% | 8 |
| 4575 | Agency Program Related Svcs & Supp | $25,126.25 | 5.2% | 1 |
| 4315 | It Professional Services | $15,992.00 | 3.3% | 1 |
| 4250 | Data Processing | $11,774.23 | 2.4% | 2 |
| 4100 | Instate Travel | $5,731.31 | 1.2% | 28 |
| 4150 | Employee Training | $5,412.18 | 1.1% | 19 |
| 4125 | Out-Of-State Travel | $5,385.19 | 1.1% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $3,607.02 | 0.7% | 3 |
| 4175 | Office Expenses | $2,464.86 | 0.5% | 4 |
| 4400 | Dues And Subscriptions | $1,872.00 | 0.4% | 1 |
| 4275 | Publicity & Publications | $1,378.89 | 0.3% | 4 |
| 4715 | It Expendable Property | $160.82 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 32 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $190,223.51 | 39.5% |
| 4701 | Other Services | $56,950.18 | 11.8% |
| 4800 | Interagency Lease Payments | $55,282.79 | 11.5% |
| 4600 | State Government Service Charges | $40,617.00 | 8.4% |
| 4500 | Professional Services Non-It | $36,109.19 | 7.5% |
| 4975 | Agency Program Related Services | $25,126.25 | 5.2% |
| 4730 | Merchant Fees | $23,739.04 | 4.9% |
| 4516 | Professional Services Servers | $15,992.00 | 3.3% |
| 4375 | Computer Technology Computer Processing | $11,774.23 | 2.4% |
| 4159 | Out-Of-State Air Transportation | $5,385.19 | 1.1% |
| 4301 | Telecom/Voice Usage | $2,748.76 | 0.6% |
| 4440 | Prof Dev Out-Of-State Air Transportation | $2,480.35 | 0.5% |

## Curator notes

Figures are aggregated from 86 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='811' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


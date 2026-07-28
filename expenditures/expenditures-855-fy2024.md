---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-855-fy2024
title: Pharmacy, Oregon Brd of — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 855, FY2024
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
  - expenditures-855-fy2023
  - expenditures-855-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-855
- pharmacy-oregon-brd-of
agency_code: '855'
agency_name: PHARMACY, OREGON BRD OF
fiscal_year: 2024
total_expense: '1347905.20'
transaction_count: 129
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Pharmacy, Oregon Brd of — FY2024 expenditures

## At a glance

Pharmacy, Oregon Brd of (agency code 855, recorded upstream as `PHARMACY, OREGON BRD OF`) spent **$1,347,905.20** in fiscal year 2024, across 129 transaction records. That is up 15.9% from $1,162,645.87 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **57 of 80** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $353,069.25 (26.2% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $353,069.25 | 26.2% | 1 |
| 4650 | Other Services And Supplies | $202,228.73 | 15.0% | 6 |
| 4300 | Professional Services | $187,397.63 | 13.9% | 11 |
| 4425 | Lease Payments & Taxes | $158,998.46 | 11.8% | 2 |
| 4225 | State Government Service Charges | $133,203.00 | 9.9% | 4 |
| 4575 | Agency Program Related Svcs & Supp | $114,314.93 | 8.5% | 3 |
| 4250 | Data Processing | $109,425.53 | 8.1% | 5 |
| 4100 | Instate Travel | $33,035.24 | 2.5% | 59 |
| 4175 | Office Expenses | $25,226.79 | 1.9% | 7 |
| 4200 | Telecomm/Tech Svc And Supplies | $13,105.68 | 1.0% | 3 |
| 4275 | Publicity & Publications | $8,644.61 | 0.6% | 3 |
| 4150 | Employee Training | $7,008.43 | 0.5% | 18 |
| 4315 | It Professional Services | $1,620.00 | 0.1% | 1 |
| 4125 | Out-Of-State Travel | $516.42 | 0.0% | 5 |
| 4475 | Facilities Maintenance | $110.50 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 37 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $353,069.25 | 26.2% |
| 4500 | Professional Services Non-It | $187,397.63 | 13.9% |
| 4800 | Interagency Lease Payments | $158,998.46 | 11.8% |
| 4600 | State Government Service Charges | $133,203.00 | 9.9% |
| 4975 | Agency Program Related Services | $111,638.25 | 8.3% |
| 4375 | Computer Technology Computer Processing | $109,425.53 | 8.1% |
| 4701 | Other Services | $107,517.00 | 8.0% |
| 4730 | Merchant Fees | $91,636.60 | 6.8% |
| 4201 | Office Services | $25,176.24 | 1.9% |
| 4108 | Instate Ground Transportation | $13,982.41 | 1.0% |
| 4301 | Telecom/Voice Usage | $9,612.77 | 0.7% |
| 4101 | Instate Meals With Overnight Stay | $9,332.35 | 0.7% |

## Curator notes

Figures are aggregated from 129 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='855' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


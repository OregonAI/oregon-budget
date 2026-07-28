---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-399-fy2024
title: Psychiatric Security Rev Brd — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 399, FY2024
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
  - expenditures-399-fy2023
  - expenditures-399-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-399
- psychiatric-security-rev-brd
agency_code: '399'
agency_name: PSYCHIATRIC SECURITY REV BRD
fiscal_year: 2024
total_expense: '460577.23'
transaction_count: 33
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Psychiatric Security Rev Brd — FY2024 expenditures

## At a glance

Psychiatric Security Rev Brd (agency code 399, recorded upstream as `PSYCHIATRIC SECURITY REV BRD`) spent **$460,577.23** in fiscal year 2024, across 33 transaction records. That is up 8.2% from $425,585.29 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **68 of 80** agencies reporting that year.

The largest budget category was **Office Expenses** at $141,589.40 (30.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4175 | Office Expenses | $141,589.40 | 30.7% | 3 |
| 4325 | Attorney General Legal Fees | $104,996.10 | 22.8% | 1 |
| 4225 | State Government Service Charges | $91,438.92 | 19.9% | 4 |
| 4650 | Other Services And Supplies | $45,280.18 | 9.8% | 3 |
| 4425 | Lease Payments & Taxes | $31,953.03 | 6.9% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $16,794.09 | 3.6% | 4 |
| 4250 | Data Processing | $13,402.35 | 2.9% | 4 |
| 4715 | It Expendable Property | $7,225.07 | 1.6% | 1 |
| 4300 | Professional Services | $3,974.70 | 0.9% | 3 |
| 4475 | Facilities Maintenance | $1,945.00 | 0.4% | 1 |
| 4700 | Expendable Property $250-$5000 | $1,000.00 | 0.2% | 1 |
| 4100 | Instate Travel | $575.57 | 0.1% | 4 |
| 4275 | Publicity & Publications | $402.82 | 0.1% | 2 |

## Largest expenditure classes

The 12 largest of 16 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4201 | Office Services | $141,558.58 | 30.7% |
| 4550 | Attorney General Legal Fees | $104,996.10 | 22.8% |
| 4600 | State Government Service Charges | $91,438.92 | 19.9% |
| 4701 | Other Services | $45,280.18 | 9.8% |
| 4800 | Interagency Lease Payments | $31,953.03 | 6.9% |
| 4305 | Telecom/Network Services | $14,687.58 | 3.2% |
| 4375 | Computer Technology Computer Processing | $13,402.35 | 2.9% |
| 4365 | Computer Technology Pc Equipment<$5K | $7,225.07 | 1.6% |
| 4500 | Professional Services Non-It | $3,974.70 | 0.9% |
| 4301 | Telecom/Voice Usage | $2,106.51 | 0.5% |
| 4850 | Facilities Maintenance | $1,945.00 | 0.4% |
| 4999 | Expendable Property Non-It<$5K | $1,000.00 | 0.2% |

## Curator notes

Figures are aggregated from 33 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='399' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-172-fy2024
title: Facilites Auth, Oregon — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 172, FY2024
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: decef95a644d748f5c62eca57f2ec65a1ac01802ec192ae6fe9a4da7eed2a7c0
snapshot_policy: hash-only
source_data_file: data/expenditures/expenditures-2024.parquet
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
  - expenditures-172-fy2023
  - expenditures-172-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-172
- facilites-auth-oregon
agency_code: '172'
agency_name: FACILITES AUTH, OREGON
fiscal_year: 2024
total_expense: '285405.94'
transaction_count: 15
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Facilites Auth, Oregon — FY2024 expenditures

## At a glance

Facilites Auth, Oregon (agency code 172, recorded upstream as `FACILITES AUTH, OREGON`) spent **$285,405.94** in fiscal year 2024, across 15 transaction records. That is down 4.6% from $299,166.49 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **72 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $268,185.29 (94.0% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $285,405.94 | 100.0% | 5 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4300 | Professional Services | Services and supplies | $268,185.29 | 94.0% | 8 |
| 4650 | Other Services And Supplies | Services and supplies | $12,018.77 | 4.2% | 2 |
| 4400 | Dues And Subscriptions | Services and supplies | $3,250.00 | 1.1% | 1 |
| 4325 | Attorney General Legal Fees | Services and supplies | $1,636.80 | 0.6% | 2 |
| 4225 | State Government Service Charges | Services and supplies | $315.08 | 0.1% | 2 |

## Largest expenditure classes

The 5 largest of 5 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $268,185.29 | 94.0% |
| 4701 | Other Services | $12,018.77 | 4.2% |
| 4250 | Dues/Memberships | $3,250.00 | 1.1% |
| 4550 | Attorney General Legal Fees | $1,636.80 | 0.6% |
| 4600 | State Government Service Charges | $315.08 | 0.1% |

## Largest vendors

The 9 largest of 9 payees this agency recorded payments to in FY2024, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| TONKON TORP LLP | $212,091.93 | 74.3% | 1 |
| OREGON STATE TREASURY | $60,279.00 | 21.1% | 4 |
| STATE OF OREGON DEPARTMENT OF JUSTICE | $5,735.05 | 2.0% | 2 |
| NCHFFA | $3,250.00 | 1.1% | 1 |
| WILLIAM GRANT WADHAMS | $2,463.48 | 0.9% | 1 |
| FIRST TRYON ADVISORS | $850.00 | 0.3% | 1 |
| SECRETARY OF STATE | $531.52 | 0.2% | 2 |
| STATE OF OREGON SECRETARY OF STATE | $160.00 | 0.1% | 1 |
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $44.96 | 0.0% | 2 |

## Curator notes

Figures are aggregated from 15 vendor-level transaction records covering 9 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='172' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


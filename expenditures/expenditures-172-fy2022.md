---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-172-fy2022
title: Facilites Auth, Oregon — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 172, FY2022
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5378b32aad5d54d03160dd49832cc5c4f45e517dde8ba96c7e5b8bbb6e3a99f4
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: ''
verified_by: ''
maintainer: '@dzinck'
conversion_notes: Title is the source agency name title-cased for reading; the verbatim string is `agency_name`.
  Abbreviations are not expanded. Figures are aggregated, not extracted text.
relationships:
  implements: []
  implemented_by: []
  references_external: []
  related:
  - expenditures-172-fy2021
  - expenditures-172-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-172
- facilites-auth-oregon
agency_code: '172'
agency_name: FACILITES AUTH, OREGON
fiscal_year: 2022
total_expense: '230194.92'
transaction_count: 12
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Facilites Auth, Oregon — FY2022 expenditures

## At a glance

Facilites Auth, Oregon (agency code 172, recorded upstream as `FACILITES AUTH, OREGON`) spent **$230,194.92** in fiscal year 2022, across 12 transaction records. That is up 9.8% from $209,656.65 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **70 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $192,487.24 (83.6% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $230,194.92 | 100.0% | 5 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4300 | Professional Services | Services and supplies | $192,487.24 | 83.6% | 5 |
| 4650 | Other Services And Supplies | Services and supplies | $30,517.58 | 13.3% | 2 |
| 4325 | Attorney General Legal Fees | Services and supplies | $3,702.60 | 1.6% | 1 |
| 4400 | Dues And Subscriptions | Services and supplies | $3,000.00 | 1.3% | 1 |
| 4225 | State Government Service Charges | Services and supplies | $487.50 | 0.2% | 3 |

## Largest expenditure classes

The 5 largest of 5 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $192,487.24 | 83.6% |
| 4701 | Other Services | $30,517.58 | 13.3% |
| 4550 | Attorney General Legal Fees | $3,702.60 | 1.6% |
| 4250 | Dues/Memberships | $3,000.00 | 1.3% |
| 4600 | State Government Service Charges | $487.50 | 0.2% |

## Largest vendors

The 10 largest of 10 payees this agency recorded payments to in FY2022, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| TONKON TORP LLP | $179,570.74 | 78.0% | 1 |
| OREGON STATE TREASURY | $30,662.00 | 13.3% | 2 |
| WESTERN FINANCIAL GROUP | $10,400.00 | 4.5% | 1 |
| STATE OF OREGON DEPARTMENT OF JUSTICE | $4,428.60 | 1.9% | 2 |
| NCHFFA | $3,000.00 | 1.3% | 1 |
| PFM FINANCIAL ADVISORS LLC | $1,200.00 | 0.5% | 1 |
| HAWKINS DELAFIELD & WOOD | $590.50 | 0.3% | 1 |
| STATE OF OREGON SECRETARY OF STATE | $193.00 | 0.1% | 1 |
| SECRETARY OF STATE | $112.50 | 0.0% | 1 |
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $37.58 | 0.0% | 1 |

## Curator notes

Figures are aggregated from 12 vendor-level transaction records covering 10 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='172' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


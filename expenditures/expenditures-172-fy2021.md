---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-172-fy2021
title: Facilites Auth, Oregon — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 172, FY2021
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
  - expenditures-172-fy2020
  - expenditures-172-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-172
- facilites-auth-oregon
agency_code: '172'
agency_name: FACILITES AUTH, OREGON
fiscal_year: 2021
total_expense: '209656.65'
transaction_count: 9
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Facilites Auth, Oregon — FY2021 expenditures

## At a glance

Facilites Auth, Oregon (agency code 172, recorded upstream as `FACILITES AUTH, OREGON`) spent **$209,656.65** in fiscal year 2021, across 9 transaction records. That is down 2.2% from $214,327.92 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **69 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $154,266.07 (73.6% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $209,656.65 | 100.0% | 5 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4300 | Professional Services | Services and supplies | $154,266.07 | 73.6% | 3 |
| 4650 | Other Services And Supplies | Services and supplies | $48,499.42 | 23.1% | 2 |
| 4325 | Attorney General Legal Fees | Services and supplies | $3,607.60 | 1.7% | 1 |
| 4400 | Dues And Subscriptions | Services and supplies | $3,000.00 | 1.4% | 1 |
| 4225 | State Government Service Charges | Services and supplies | $283.56 | 0.1% | 2 |

## Largest expenditure classes

The 5 largest of 5 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $154,266.07 | 73.6% |
| 4701 | Other Services | $48,499.42 | 23.1% |
| 4550 | Attorney General Legal Fees | $3,607.60 | 1.7% |
| 4250 | Dues/Memberships | $3,000.00 | 1.4% |
| 4600 | State Government Service Charges | $283.56 | 0.1% |

## Largest vendors

The 8 largest of 8 payees this agency recorded payments to in FY2021, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| TONKON TORP LLP | $146,403.07 | 69.8% | 1 |
| OREGON STATE TREASURY | $46,146.00 | 22.0% | 2 |
| WESTERN FINANCIAL GROUP | $4,400.00 | 2.1% | 1 |
| STATE OF OREGON DEPARTMENT OF JUSTICE | $3,607.60 | 1.7% | 1 |
| HAWKINS DELAFIELD & WOOD | $3,463.00 | 1.7% | 1 |
| NCHFFA | $3,000.00 | 1.4% | 1 |
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $2,521.42 | 1.2% | 1 |
| SECRETARY OF STATE | $115.56 | 0.1% | 1 |

## Curator notes

Figures are aggregated from 9 vendor-level transaction records covering 8 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='172' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-172-fy2019
title: Facilites Auth, Oregon — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 172, FY2019
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 3900810723066d4651c7227ef0c74a8b9c41ff76c2e4bcebbbb6f2268e443d34
snapshot_policy: hash-only
source_data_file: data/expenditures/expenditures-2019.parquet
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
  - expenditures-172-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-172
- facilites-auth-oregon
agency_code: '172'
agency_name: FACILITES AUTH, OREGON
fiscal_year: 2019
total_expense: '230709.61'
transaction_count: 14
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Facilites Auth, Oregon — FY2019 expenditures

## At a glance

Facilites Auth, Oregon (agency code 172, recorded upstream as `FACILITES AUTH, OREGON`) spent **$230,709.61** in fiscal year 2019, across 14 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **70 of 78** agencies reporting that year.

The largest budget category was **Professional Services** at $178,810.26 (77.5% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $230,709.61 | 100.0% | 9 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4300 | Professional Services | Services and supplies | $178,810.26 | 77.5% | 3 |
| 4650 | Other Services And Supplies | Services and supplies | $37,520.41 | 16.3% | 2 |
| 4325 | Attorney General Legal Fees | Services and supplies | $9,773.40 | 4.2% | 1 |
| 4400 | Dues And Subscriptions | Services and supplies | $3,000.00 | 1.3% | 1 |
| 4275 | Publicity & Publications | Services and supplies | $660.51 | 0.3% | 1 |
| 4225 | State Government Service Charges | Services and supplies | $438.96 | 0.2% | 3 |
| 4425 | Facilities Rent & Taxes | Services and supplies | $300.00 | 0.1% | 1 |
| 4100 | Instate Travel | Services and supplies | $165.00 | 0.1% | 1 |
| 4175 | Office Expenses | Services and supplies | $41.07 | 0.0% | 1 |

## Largest expenditure classes

The 9 largest of 9 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $178,810.26 | 77.5% |
| 4701 | Other Services | $37,520.41 | 16.3% |
| 4550 | Attorney General Legal Fees | $9,773.40 | 4.2% |
| 4250 | Dues/Memberships | $3,000.00 | 1.3% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $660.51 | 0.3% |
| 4600 | State Government Service Charges | $438.96 | 0.2% |
| 4800 | Facilities Rent | $300.00 | 0.1% |
| 4108 | Instate Ground Transportation | $165.00 | 0.1% |
| 4201 | Office Services | $41.07 | 0.0% |

## Largest vendors

The 11 largest of 11 payees this agency recorded payments to in FY2019, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| TONKON TORP LLP | $166,810.26 | 72.3% | 1 |
| OREGON STATE TREASURY | $33,598.00 | 14.6% | 2 |
| WESTERN FINANCIAL GROUP | $11,200.00 | 4.9% | 1 |
| STATE OF OREGON DEPARTMENT OF JUSTICE | $9,773.40 | 4.2% | 1 |
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $4,790.92 | 2.1% | 2 |
| NCHFFA | $3,000.00 | 1.3% | 1 |
| PFM FINANCIAL ADVISORS LLC | $800.00 | 0.3% | 1 |
| HAWKINS DELAFIELD & WOOD | $465.00 | 0.2% | 2 |
| SECRETARY OF STATE | $173.22 | 0.1% | 1 |
| STATE OF OREGON - SECRETARY OF STATE | $57.74 | 0.0% | 1 |
| UNITED PARCEL SERVICE | $41.07 | 0.0% | 1 |

## Curator notes

Figures are aggregated from 14 vendor-level transaction records covering 11 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='172' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


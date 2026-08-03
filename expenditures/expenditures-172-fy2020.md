---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-172-fy2020
title: Facilites Auth, Oregon — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 172, FY2020
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: b73d59a16a10ad7f6ae4f4b415cba8d78894a3ead0e3928fe994cc49b9b11284
snapshot_policy: hash-only
source_data_file: data/expenditures/expenditures-2020.parquet
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
  - expenditures-172-fy2019
  - expenditures-172-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-172
- facilites-auth-oregon
agency_code: '172'
agency_name: FACILITES AUTH, OREGON
fiscal_year: 2020
total_expense: '214327.92'
transaction_count: 12
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Facilites Auth, Oregon — FY2020 expenditures

## At a glance

Facilites Auth, Oregon (agency code 172, recorded upstream as `FACILITES AUTH, OREGON`) spent **$214,327.92** in fiscal year 2020, across 12 transaction records. That is down 7.1% from $230,709.61 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **69 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $155,964.65 (72.8% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $214,327.92 | 100.0% | 7 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4300 | Professional Services | Services and supplies | $155,964.65 | 72.8% | 3 |
| 4650 | Other Services And Supplies | Services and supplies | $48,857.38 | 22.8% | 2 |
| 4325 | Attorney General Legal Fees | Services and supplies | $5,208.00 | 2.4% | 1 |
| 4400 | Dues And Subscriptions | Services and supplies | $3,000.00 | 1.4% | 1 |
| 4275 | Publicity & Publications | Services and supplies | $772.98 | 0.4% | 1 |
| 4225 | State Government Service Charges | Services and supplies | $518.56 | 0.2% | 3 |
| 4175 | Office Expenses | Services and supplies | $6.35 | 0.0% | 1 |

## Largest expenditure classes

The 7 largest of 7 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $155,964.65 | 72.8% |
| 4701 | Other Services | $48,857.38 | 22.8% |
| 4550 | Attorney General Legal Fees | $5,208.00 | 2.4% |
| 4250 | Dues/Memberships | $3,000.00 | 1.4% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $772.98 | 0.4% |
| 4600 | State Government Service Charges | $518.56 | 0.2% |
| 4201 | Office Services | $6.35 | 0.0% |

## Largest vendors

The 10 largest of 10 payees this agency recorded payments to in FY2020, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| TONKON TORP LLP | $148,364.65 | 69.2% | 1 |
| OREGON STATE TREASURY | $45,676.00 | 21.3% | 2 |
| PFM FINANCIAL ADVISORS LLC | $6,400.00 | 3.0% | 1 |
| STATE OF OREGON DEPARTMENT OF JUSTICE | $5,208.00 | 2.4% | 1 |
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $4,114.36 | 1.9% | 2 |
| NCHFFA | $3,000.00 | 1.4% | 1 |
| WESTERN FINANCIAL GROUP | $1,200.00 | 0.6% | 1 |
| STATE OF OREGON SECRETARY OF STATE | $243.00 | 0.1% | 1 |
| SECRETARY OF STATE | $115.56 | 0.1% | 1 |
| UNITED PARCEL SERVICE | $6.35 | 0.0% | 1 |

## Curator notes

Figures are aggregated from 12 vendor-level transaction records covering 10 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='172' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


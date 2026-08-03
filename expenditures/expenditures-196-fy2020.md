---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-196-fy2020
title: Dist Attorneys/Deputies — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 196, FY2020
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
  - expenditures-196-fy2019
  - expenditures-196-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-196
- dist-attorneys-deputies
agency_code: '196'
agency_name: DIST ATTORNEYS/DEPUTIES
fiscal_year: 2020
total_expense: '260093.79'
transaction_count: 6
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dist Attorneys/Deputies — FY2020 expenditures

## At a glance

Dist Attorneys/Deputies (agency code 196, recorded upstream as `DIST ATTORNEYS/DEPUTIES`) spent **$260,093.79** in fiscal year 2020, across 6 transaction records. That is down 67.3% from $794,593.15 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **67 of 77** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $258,014.02 (99.2% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $260,066.49 | 100.0% | 2 |
| Personnel services | $27.30 | 0.0% | 1 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | Services and supplies | $258,014.02 | 99.2% | 4 |
| 4650 | Other Services And Supplies | Services and supplies | $2,052.47 | 0.8% | 1 |
| 3220 | Public Employes' Retirement System | Personnel services | $27.30 | 0.0% | 1 |

## Largest expenditure classes

The 3 largest of 3 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $258,014.02 | 99.2% |
| 4701 | Other Services | $2,052.47 | 0.8% |
| 3210 | Public Employees Retirement Contribution | $27.30 | 0.0% |

## Largest vendors

The 5 largest of 5 payees this agency recorded payments to in FY2020, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $250,089.47 | 96.2% | 2 |
| STATE OF OREGON SECRETARY OF STATE | $6,524.00 | 2.5% | 1 |
| STATE OF OREGON - SECRETARY OF STATE | $3,073.52 | 1.2% | 1 |
| OREGON GOVERNMENT ETHICS COMMISSION | $379.50 | 0.1% | 1 |
| OREGON PUBLIC EMPLOYEES RETIREMENT SYSTEM | $27.30 | 0.0% | 1 |

## Curator notes

Figures are aggregated from 6 vendor-level transaction records covering 5 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='196' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-196-fy2021
title: Dist Attorneys/Deputies — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 196, FY2021
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 81c90c241c212dba4cc304dd132bb03379de0003138cc2451899f8f95b1dcc97
snapshot_policy: hash-only
source_data_file: data/expenditures/expenditures-2021.parquet
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
  - expenditures-196-fy2020
  - expenditures-196-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-196
- dist-attorneys-deputies
agency_code: '196'
agency_name: DIST ATTORNEYS/DEPUTIES
fiscal_year: 2021
total_expense: '265576.36'
transaction_count: 6
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dist Attorneys/Deputies — FY2021 expenditures

## At a glance

Dist Attorneys/Deputies (agency code 196, recorded upstream as `DIST ATTORNEYS/DEPUTIES`) spent **$265,576.36** in fiscal year 2021, across 6 transaction records. That is up 2.1% from $260,093.79 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **66 of 76** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $258,175.12 (97.2% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $259,887.36 | 97.9% | 2 |
| Personnel services | $5,689.00 | 2.1% | 1 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | Services and supplies | $258,175.12 | 97.2% | 4 |
| 3240 | Unemployment Assessment | Personnel services | $5,689.00 | 2.1% | 1 |
| 4650 | Other Services And Supplies | Services and supplies | $1,712.24 | 0.6% | 1 |

## Largest expenditure classes

The 3 largest of 3 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $258,175.12 | 97.2% |
| 3231 | Unemployment Compensation & Assessment | $5,689.00 | 2.1% |
| 4701 | Other Services | $1,712.24 | 0.6% |

## Largest vendors

The 5 largest of 5 payees this agency recorded payments to in FY2021, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $249,910.34 | 94.1% | 2 |
| STATE OF OREGON SECRETARY OF STATE | $6,524.00 | 2.5% | 1 |
| EMPLOYMENT DEPARTMENT | $5,689.00 | 2.1% | 1 |
| STATE OF OREGON - SECRETARY OF STATE | $3,073.52 | 1.2% | 1 |
| OREGON GOVERNMENT ETHICS COMMISSION | $379.50 | 0.1% | 1 |

## Curator notes

Figures are aggregated from 6 vendor-level transaction records covering 5 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='196' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-196-fy2019
title: Dist Attorneys/Deputies — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 196, FY2019
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 3900810723066d4651c7227ef0c74a8b9c41ff76c2e4bcebbbb6f2268e443d34
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
  - expenditures-196-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-196
- dist-attorneys-deputies
agency_code: '196'
agency_name: DIST ATTORNEYS/DEPUTIES
fiscal_year: 2019
total_expense: '794593.15'
transaction_count: 9
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dist Attorneys/Deputies — FY2019 expenditures

## At a glance

Dist Attorneys/Deputies (agency code 196, recorded upstream as `DIST ATTORNEYS/DEPUTIES`) spent **$794,593.15** in fiscal year 2019, across 9 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **56 of 78** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $406,900.46 (51.2% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $406,900.46 | 51.2% | 4 |
| 6085 | Other Special Payments | $386,107.00 | 48.6% | 3 |
| 4650 | Other Services And Supplies | $1,559.79 | 0.2% | 1 |
| 3220 | Public Employes' Retirement System | $25.90 | 0.0% | 1 |

## Largest expenditure classes

The 4 largest of 4 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $406,900.46 | 51.2% |
| 6900 | Other Special Payments | $386,107.00 | 48.6% |
| 4701 | Other Services | $1,559.79 | 0.2% |
| 3210 | Public Employees Retirement Contribution | $25.90 | 0.0% |

## Largest vendors

The 8 largest of 8 payees this agency recorded payments to in FY2019, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $399,549.79 | 50.3% | 2 |
| COUNTY OF MULTNOMAH | $186,238.00 | 23.4% | 1 |
| JACKSON COUNTY DISTRICT ATTORNEYS OFFICE | $129,027.00 | 16.2% | 1 |
| DESCHUTES COUNTY DISTRICT ATTORNEY | $70,842.00 | 8.9% | 1 |
| STATE OF OREGON SECRETARY OF STATE | $5,722.00 | 0.7% | 1 |
| STATE OF OREGON - SECRETARY OF STATE | $2,853.00 | 0.4% | 1 |
| OREGON GOVERNMENT ETHICS COMMISSION | $335.46 | 0.0% | 1 |
| OREGON PUBLIC EMPLOYEES RETIREMENT SYSTEM | $25.90 | 0.0% | 1 |

## Curator notes

Figures are aggregated from 9 vendor-level transaction records covering 8 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='196' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


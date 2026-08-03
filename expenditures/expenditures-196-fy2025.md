---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-196-fy2025
title: Dist Attorneys/Deputies — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 196, FY2025
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5e9f0c30287913ac0bfff8d74a1225d0c2816ca6a307f2141ebb35602c5a91ed
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
  - expenditures-196-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-196
- dist-attorneys-deputies
agency_code: '196'
agency_name: DIST ATTORNEYS/DEPUTIES
fiscal_year: 2025
total_expense: '1641970.27'
transaction_count: 16
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dist Attorneys/Deputies — FY2025 expenditures

## At a glance

Dist Attorneys/Deputies (agency code 196, recorded upstream as `DIST ATTORNEYS/DEPUTIES`) spent **$1,641,970.27** in fiscal year 2025, across 16 transaction records. That is up 66.1% from $988,345.42 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **56 of 80** agencies reporting that year.

The largest budget category was **Distribution To Counties** at $1,000,000.00 (60.9% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Distributions | $1,000,000.00 | 60.9% | 1 |
| Services and supplies | $641,935.71 | 39.1% | 5 |
| Personnel services | $34.56 | 0.0% | 1 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 6020 | Distribution To Counties | Distributions | $1,000,000.00 | 60.9% | 6 |
| 4225 | State Government Service Charges | Services and supplies | $594,367.50 | 36.2% | 4 |
| 4300 | Professional Services | Services and supplies | $46,808.00 | 2.9% | 2 |
| 4325 | Attorney General Legal Fees | Services and supplies | $495.00 | 0.0% | 1 |
| 4650 | Other Services And Supplies | Services and supplies | $134.17 | 0.0% | 1 |
| 4575 | Agency Program Related Svcs & Supp | Services and supplies | $131.04 | 0.0% | 1 |
| 3220 | Public Employes' Retirement System | Personnel services | $34.56 | 0.0% | 1 |

## Largest expenditure classes

The 7 largest of 7 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6300 | Distribution To Counties | $1,000,000.00 | 60.9% |
| 4600 | State Government Service Charges | $594,367.50 | 36.2% |
| 4500 | Professional Services Non-It | $46,808.00 | 2.9% |
| 4550 | Attorney General Legal Fees | $495.00 | 0.0% |
| 4701 | Other Services | $134.17 | 0.0% |
| 4975 | Agency Program Related Services | $131.04 | 0.0% |
| 3210 | Public Employees Retirement Contribution | $34.56 | 0.0% |

## Largest vendors

The 14 largest of 14 payees this agency recorded payments to in FY2025, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $579,383.21 | 35.3% | 3 |
| COUNTY OF MULTNOMAH | $397,750.00 | 24.2% | 1 |
| WASHINGTON COUNTY DISTRICT ATTORNEY | $372,750.00 | 22.7% | 1 |
| MARION COUNTY DISTRICT ATTORNEY'S OFFICE | $138,700.00 | 8.4% | 1 |
| CLACKAMAS COUNTY DISTRICT ATTORNEY | $80,900.00 | 4.9% | 1 |
| FREE STATE REPORTING INC | $36,199.05 | 2.2% | 1 |
| ESCRIBERS LLC | $10,608.95 | 0.6% | 1 |
| STATE OF OREGON SECRETARY OF STATE | $8,244.00 | 0.5% | 1 |
| DESCHUTES COUNTY DISTRICT ATTORNEY | $8,100.00 | 0.5% | 1 |
| STATE OF OREGON - SECRETARY OF STATE | $6,375.00 | 0.4% | 1 |
| LINN COUNTY DISTRICT ATTORNEY'S OFFICE | $1,800.00 | 0.1% | 1 |
| OREGON GOVERNMENT ETHICS COMMISSION | $630.50 | 0.0% | 1 |
| STATE OF OREGON DEPARTMENT OF JUSTICE | $495.00 | 0.0% | 1 |
| OREGON PUBLIC EMPLOYEES RETIREMENT SYSTEM | $34.56 | 0.0% | 1 |

## Curator notes

Figures are aggregated from 16 vendor-level transaction records covering 14 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='196' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


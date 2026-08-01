---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-425-fy2021
title: Indian Services Cmsn — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 425, FY2021
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
  - expenditures-425-fy2020
  - expenditures-425-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-425
- indian-services-cmsn
agency_code: '425'
agency_name: INDIAN SERVICES CMSN
fiscal_year: 2021
total_expense: '9556.29'
transaction_count: 7
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Indian Services Cmsn — FY2021 expenditures

## At a glance

Indian Services Cmsn (agency code 425, recorded upstream as `INDIAN SERVICES CMSN`) spent **$9,556.29** in fiscal year 2021, across 7 transaction records. That is down 53.3% from $20,461.86 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **76 of 76** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $6,917.59 (72.4% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $7,030.21 | 73.6% | 3 |
| Personnel services | $2,526.08 | 26.4% | 1 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | Services and supplies | $6,917.59 | 72.4% | 4 |
| 3220 | Public Employes' Retirement System | Personnel services | $2,526.08 | 26.4% | 1 |
| 4715 | It Expendable Property | Services and supplies | $97.62 | 1.0% | 1 |
| 4650 | Other Services And Supplies | Services and supplies | $15.00 | 0.2% | 1 |

## Largest expenditure classes

The 4 largest of 4 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $6,917.59 | 72.4% |
| 3210 | Public Employees Retirement Contribution | $2,526.08 | 26.4% |
| 4366 | Computer Technology Pc Software<$5K | $97.62 | 1.0% |
| 4701 | Other Services | $15.00 | 0.2% |

## Largest vendors

The 6 largest of 6 payees this agency recorded payments to in FY2021, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $6,605.59 | 69.1% | 1 |
| OREGON PUBLIC EMPLOYEES RETIREMENT SYSTEM | $2,541.08 | 26.6% | 2 |
| STATE OF OREGON SECRETARY OF STATE | $171.00 | 1.8% | 1 |
| OREGON STATE TREASURY | $120.00 | 1.3% | 1 |
| SHI INTERNATIONAL CORP | $97.62 | 1.0% | 1 |
| OREGON GOVERNMENT ETHICS COMMISSION | $21.00 | 0.2% | 1 |

## Curator notes

Figures are aggregated from 7 vendor-level transaction records covering 6 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='425' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


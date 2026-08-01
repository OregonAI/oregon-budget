---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-175-fy2019
title: Judicial Fitness & Disability — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 175, FY2019
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
  - expenditures-175-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-175
- judicial-fitness-disability
agency_code: '175'
agency_name: JUDICIAL FITNESS & DISABILITY
fiscal_year: 2019
total_expense: '32913.99'
transaction_count: 26
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Judicial Fitness & Disability — FY2019 expenditures

## At a glance

Judicial Fitness & Disability (agency code 175, recorded upstream as `JUDICIAL FITNESS & DISABILITY`) spent **$32,913.99** in fiscal year 2019, across 26 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **76 of 78** agencies reporting that year.

The largest budget category was **Professional Services** at $13,665.10 (41.5% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $32,913.99 | 100.0% | 6 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4300 | Professional Services | Services and supplies | $13,665.10 | 41.5% | 3 |
| 4425 | Facilities Rent & Taxes | Services and supplies | $6,600.00 | 20.1% | 1 |
| 4225 | State Government Service Charges | Services and supplies | $5,516.13 | 16.8% | 4 |
| 4175 | Office Expenses | Services and supplies | $4,071.52 | 12.4% | 8 |
| 4200 | Telecomm/Tech Svc And Supplies | Services and supplies | $2,187.34 | 6.6% | 5 |
| 4100 | Instate Travel | Services and supplies | $873.90 | 2.7% | 5 |

## Largest expenditure classes

The 11 largest of 11 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $13,665.10 | 41.5% |
| 4800 | Facilities Rent | $6,600.00 | 20.1% |
| 4600 | State Government Service Charges | $5,516.13 | 16.8% |
| 4201 | Office Services | $3,224.14 | 9.8% |
| 4301 | Telecom/Voice Usage | $2,008.41 | 6.1% |
| 4200 | Office Supplies | $847.38 | 2.6% |
| 4106 | Instate Lodging | $531.10 | 1.6% |
| 4103 | Instate Mileage Reimbursement | $260.06 | 0.8% |
| 4315 | Telecom/Teleconference Usage | $178.93 | 0.5% |
| 4105 | Instate Meals-No Overnight Stay | $77.74 | 0.2% |
| 4108 | Instate Ground Transportation | $5.00 | 0.0% |

## Largest vendors

The 15 largest of 15 payees this agency recorded payments to in FY2019, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| TIM VOLPERT PC | $8,560.00 | 26.0% | 1 |
| SUSAN D ISAACS | $8,238.67 | 25.0% | 4 |
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $5,350.95 | 16.3% | 1 |
| SAMUELS YOELIN KANTOR LLP | $3,612.70 | 11.0% | 1 |
| US BANK CORPORATE PAYMENT SYSTEMS | $3,102.54 | 9.4% | 6 |
| STATE OF OREGON DEPARTMENT OF JUSTICE | $1,492.40 | 4.5% | 1 |
| COCKLE LEGAL BRIEFS | $890.18 | 2.7% | 1 |
| ACCESS INFORMATION HOLDINGS LLC | $496.96 | 1.5% | 2 |
| MONTE S CAMPBELL | $319.80 | 1.0% | 2 |
| UNITED TELEPHONE COMPANY OF THE NORTHWEST | $319.20 | 1.0% | 2 |
| OREGON CORRECTIONS ENTERPRISES | $207.71 | 0.6% | 1 |
| COMCAST | $157.70 | 0.5% | 1 |
| OREGON STATE TREASURY | $121.00 | 0.4% | 1 |
| STATE OF OREGON SECRETARY OF STATE | $39.52 | 0.1% | 1 |
| OREGON GOVERNMENT ETHICS COMMISSION | $4.66 | 0.0% | 1 |

## Curator notes

Figures are aggregated from 26 vendor-level transaction records covering 15 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='175' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


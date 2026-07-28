---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-839-fy2025
title: Labor & Ind, Bureau of — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 839, FY2025
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5e9f0c30287913ac0bfff8d74a1225d0c2816ca6a307f2141ebb35602c5a91ed
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
  - expenditures-839-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-839
- labor-ind-bureau-of
agency_code: '839'
agency_name: LABOR & IND, BUREAU OF
fiscal_year: 2025
total_expense: '10276446.94'
transaction_count: 337
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Labor & Ind, Bureau of — FY2025 expenditures

## At a glance

Labor & Ind, Bureau of (agency code 839, recorded upstream as `LABOR & IND, BUREAU OF`) spent **$10,276,446.94** in fiscal year 2025, across 337 transaction records. That is up 55.2% from $6,621,671.19 in FY2024. The agency accounts for 0.03% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **42 of 80** agencies reporting that year.

The largest budget category was **Distribution To Individuals** at $4,575,016.80 (44.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6035 | Distribution To Individuals | $4,575,016.80 | 44.5% | 6 |
| 4300 | Professional Services | $2,118,178.22 | 20.6% | 65 |
| 6588 | Distribution To Or Dept Of Early Lrn | $928,167.41 | 9.0% | 1 |
| 4225 | State Government Service Charges | $633,229.02 | 6.2% | 3 |
| 4325 | Attorney General Legal Fees | $408,677.20 | 4.0% | 1 |
| 4715 | It Expendable Property | $291,491.19 | 2.8% | 7 |
| 4175 | Office Expenses | $223,690.49 | 2.2% | 35 |
| 4200 | Telecomm/Tech Svc And Supplies | $214,757.58 | 2.1% | 4 |
| 4425 | Lease Payments & Taxes | $167,694.46 | 1.6% | 6 |
| 4315 | It Professional Services | $161,502.79 | 1.6% | 5 |
| 4250 | Data Processing | $123,916.73 | 1.2% | 6 |
| 4650 | Other Services And Supplies | $106,919.09 | 1.0% | 16 |
| 4100 | Instate Travel | $89,748.26 | 0.9% | 124 |
| 4600 | Intra-Inter Agency Charges | $71,375.16 | 0.7% | 1 |
| 4400 | Dues And Subscriptions | $65,753.87 | 0.6% | 6 |
| 4150 | Employee Training | $40,027.28 | 0.4% | 9 |
| 4125 | Out-Of-State Travel | $29,888.51 | 0.3% | 39 |
| 5550 | Data Processing Software | $13,365.00 | 0.1% | 1 |
| 3240 | Unemployment Assessment | $12,682.58 | 0.1% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $365.30 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 55 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6800 | Distribution To Individuals | $4,575,016.80 | 44.5% |
| 4500 | Professional Services Non-It | $2,118,178.22 | 20.6% |
| 6143 | Distribution To Or Dept Of Early Lrn | $928,167.41 | 9.0% |
| 4600 | State Government Service Charges | $633,229.02 | 6.2% |
| 4550 | Attorney General Legal Fees | $408,677.20 | 4.0% |
| 4301 | Telecom/Voice Usage | $205,397.02 | 2.0% |
| 4200 | Office Supplies | $121,350.99 | 1.2% |
| 4361 | Computer Technology Server Software<$5K | $118,973.65 | 1.2% |
| 7007 | Lease Pmt For Buildings | $114,797.71 | 1.1% |
| 4365 | Computer Technology Pc Equipment<$5K | $114,361.14 | 1.1% |
| 4515 | Professional Services Application Maint | $101,524.00 | 1.0% |
| 4650 | Intra-Inter Agency Charges | $71,375.16 | 0.7% |

## Curator notes

Figures are aggregated from 337 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='839' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


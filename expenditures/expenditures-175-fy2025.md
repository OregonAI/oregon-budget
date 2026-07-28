---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-175-fy2025
title: Judicial Fitness & Disability — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 175, FY2025
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
  - expenditures-175-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-175
- judicial-fitness-disability
agency_code: '175'
agency_name: JUDICIAL FITNESS & DISABILITY
fiscal_year: 2025
total_expense: '84121.56'
transaction_count: 30
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Judicial Fitness & Disability — FY2025 expenditures

## At a glance

Judicial Fitness & Disability (agency code 175, recorded upstream as `JUDICIAL FITNESS & DISABILITY`) spent **$84,121.56** in fiscal year 2025, across 30 transaction records. That is up 23.6% from $68,038.35 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **78 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $57,139.71 (67.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $57,139.71 | 67.9% | 6 |
| 4225 | State Government Service Charges | $10,102.85 | 12.0% | 5 |
| 4425 | Lease Payments & Taxes | $6,600.00 | 7.8% | 1 |
| 4400 | Dues And Subscriptions | $3,583.00 | 4.3% | 4 |
| 4175 | Office Expenses | $2,579.56 | 3.1% | 4 |
| 4150 | Employee Training | $2,556.00 | 3.0% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $897.79 | 1.1% | 1 |
| 4100 | Instate Travel | $662.65 | 0.8% | 5 |

## Largest expenditure classes

The 12 largest of 16 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $57,139.71 | 67.9% |
| 4600 | State Government Service Charges | $10,102.85 | 12.0% |
| 4804 | Other Lease Payments | $6,600.00 | 7.8% |
| 4250 | Dues/Memberships | $3,483.00 | 4.1% |
| 4200 | Office Supplies | $1,556.66 | 1.9% |
| 4440 | Prof Dev Out-Of-State Air Transportation | $1,176.20 | 1.4% |
| 4201 | Office Services | $1,022.90 | 1.2% |
| 4301 | Telecom/Voice Usage | $897.79 | 1.1% |
| 4434 | Prof Dev Out-Of-State Lodging | $707.30 | 0.8% |
| 4411 | Prof Dev Out-Of-State Tuition/Regist | $475.00 | 0.6% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $457.36 | 0.5% |
| 4432 | Prof Dev Out-Of-State Meal W/Overnite | $197.50 | 0.2% |

## Curator notes

Figures are aggregated from 30 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='175' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


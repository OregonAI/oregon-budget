---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-175-fy2020
title: Judicial Fitness & Disability — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 175, FY2020
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: b73d59a16a10ad7f6ae4f4b415cba8d78894a3ead0e3928fe994cc49b9b11284
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
  - expenditures-175-fy2019
  - expenditures-175-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-175
- judicial-fitness-disability
agency_code: '175'
agency_name: JUDICIAL FITNESS & DISABILITY
fiscal_year: 2020
total_expense: '48379.01'
transaction_count: 35
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Judicial Fitness & Disability — FY2020 expenditures

## At a glance

Judicial Fitness & Disability (agency code 175, recorded upstream as `JUDICIAL FITNESS & DISABILITY`) spent **$48,379.01** in fiscal year 2020, across 35 transaction records. That is up 47.0% from $32,913.99 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **75 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $21,648.40 (44.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $21,648.40 | 44.7% | 5 |
| 4225 | State Government Service Charges | $10,670.31 | 22.1% | 4 |
| 4175 | Office Expenses | $6,037.47 | 12.5% | 9 |
| 4425 | Facilities Rent & Taxes | $4,950.00 | 10.2% | 2 |
| 4150 | Employee Training | $1,965.51 | 4.1% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $1,926.01 | 4.0% | 3 |
| 4400 | Dues And Subscriptions | $592.00 | 1.2% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $338.36 | 0.7% | 1 |
| 4100 | Instate Travel | $237.85 | 0.5% | 4 |
| 4125 | Out-Of-State Travel | $13.10 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 18 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $21,648.40 | 44.7% |
| 4600 | State Government Service Charges | $10,670.31 | 22.1% |
| 4800 | Facilities Rent | $4,950.00 | 10.2% |
| 4201 | Office Services | $4,457.39 | 9.2% |
| 4301 | Telecom/Voice Usage | $1,815.55 | 3.8% |
| 4200 | Office Supplies | $1,580.08 | 3.3% |
| 4440 | Prof Dev Out-Of-State Air Transportation | $1,008.00 | 2.1% |
| 4250 | Dues/Memberships | $592.00 | 1.2% |
| 4411 | Prof Dev Out-Of-State Tuition/Regist | $425.00 | 0.9% |
| 4434 | Prof Dev Out-Of-State Lodging | $361.85 | 0.7% |
| 4206 | Catering Services | $338.36 | 0.7% |
| 4441 | Prof Dev Out-Of-State Ground Transprtatn | $155.97 | 0.3% |

## Curator notes

Figures are aggregated from 35 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='175' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


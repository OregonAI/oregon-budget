---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-175-fy2023
title: Judicial Fitness & Disability — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 175, FY2023
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 6400163010ab2f341831c864272a89c5e9f2a261fad3fd9572b230042f26e3d5
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
  - expenditures-175-fy2022
  - expenditures-175-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-175
- judicial-fitness-disability
agency_code: '175'
agency_name: JUDICIAL FITNESS & DISABILITY
fiscal_year: 2023
total_expense: '33712.40'
transaction_count: 24
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Judicial Fitness & Disability — FY2023 expenditures

## At a glance

Judicial Fitness & Disability (agency code 175, recorded upstream as `JUDICIAL FITNESS & DISABILITY`) spent **$33,712.40** in fiscal year 2023, across 24 transaction records. That is down 40.3% from $56,507.27 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **76 of 77** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $10,272.40 (30.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $10,272.40 | 30.5% | 1 |
| 4425 | Lease Payments & Taxes | $6,600.00 | 19.6% | 1 |
| 4225 | State Government Service Charges | $4,707.22 | 14.0% | 5 |
| 4300 | Professional Services | $4,433.27 | 13.2% | 3 |
| 4400 | Dues And Subscriptions | $3,513.00 | 10.4% | 4 |
| 4175 | Office Expenses | $2,832.94 | 8.4% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $809.14 | 2.4% | 3 |
| 4150 | Employee Training | $475.00 | 1.4% | 1 |
| 4100 | Instate Travel | $69.43 | 0.2% | 1 |

## Largest expenditure classes

The 12 largest of 12 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $10,272.40 | 30.5% |
| 4804 | Other Lease Payments | $6,600.00 | 19.6% |
| 4600 | State Government Service Charges | $4,707.22 | 14.0% |
| 4500 | Professional Services Non-It | $4,433.27 | 13.2% |
| 4250 | Dues/Memberships | $3,438.00 | 10.2% |
| 4201 | Office Services | $2,247.10 | 6.7% |
| 4200 | Office Supplies | $585.84 | 1.7% |
| 4301 | Telecom/Voice Usage | $539.43 | 1.6% |
| 4411 | Prof Dev Out-Of-State Tuition/Regist | $475.00 | 1.4% |
| 4315 | Telecom/Teleconference Usage | $269.71 | 0.8% |
| 4251 | Subscriptions And Publications | $75.00 | 0.2% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $69.43 | 0.2% |

## Curator notes

Figures are aggregated from 24 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='175' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-131-fy2025
title: Advocacy Commissions, OR — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 131, FY2025
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
  - expenditures-131-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-131
- advocacy-commissions-or
agency_code: '131'
agency_name: ADVOCACY COMMISSIONS, OR
fiscal_year: 2025
total_expense: '144684.93'
transaction_count: 63
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Advocacy Commissions, OR — FY2025 expenditures

## At a glance

Advocacy Commissions, OR (agency code 131, recorded upstream as `ADVOCACY COMMISSIONS, OR`) spent **$144,684.93** in fiscal year 2025, across 63 transaction records. That is down 5.8% from $153,633.76 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **77 of 80** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $29,237.79 (20.2% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $29,237.79 | 20.2% | 4 |
| 4650 | Other Services And Supplies | $22,868.94 | 15.8% | 4 |
| 3240 | Unemployment Assessment | $21,112.00 | 14.6% | 1 |
| 4325 | Attorney General Legal Fees | $20,405.00 | 14.1% | 1 |
| 4250 | Data Processing | $15,127.05 | 10.5% | 4 |
| 4300 | Professional Services | $10,712.92 | 7.4% | 7 |
| 4150 | Employee Training | $7,343.28 | 5.1% | 7 |
| 3110 | Class/Unclass Salary & Per Diem | $5,448.27 | 3.8% | 1 |
| 4100 | Instate Travel | $4,533.13 | 3.1% | 20 |
| 3220 | Public Employes' Retirement System | $4,309.07 | 3.0% | 2 |
| 4715 | It Expendable Property | $1,573.49 | 1.1% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $852.18 | 0.6% | 2 |
| 3230 | Social Security Tax | $416.80 | 0.3% | 1 |
| 3221 | Pension Bond Contribution | $261.52 | 0.2% | 1 |
| 3270 | Flexible Benefits | $207.28 | 0.1% | 1 |
| 4275 | Publicity & Publications | $205.45 | 0.1% | 3 |
| 4425 | Lease Payments & Taxes | $45.00 | 0.0% | 1 |
| 3241 | Paid Family Medical Leave Insurance | $21.79 | 0.0% | 1 |
| 4175 | Office Expenses | $3.97 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 29 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $29,237.79 | 20.2% |
| 4701 | Other Services | $22,107.86 | 15.3% |
| 3231 | Unemployment Compensation & Assessment | $21,112.00 | 14.6% |
| 4550 | Attorney General Legal Fees | $20,405.00 | 14.1% |
| 4367 | Computer Technology Pc Support | $11,208.02 | 7.7% |
| 4500 | Professional Services Non-It | $10,712.92 | 7.4% |
| 4406 | Prof Dev Instate Tuition/Registration | $6,516.40 | 4.5% |
| 3111 | Regular Employees | $5,448.27 | 3.8% |
| 3210 | Public Employees Retirement Contribution | $4,309.07 | 3.0% |
| 4375 | Computer Technology Computer Processing | $3,919.03 | 2.7% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $1,655.08 | 1.1% |
| 4111 | Instate Mileage Reimbursmnt-Volunteers | $1,633.19 | 1.1% |

## Curator notes

Figures are aggregated from 63 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='131' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


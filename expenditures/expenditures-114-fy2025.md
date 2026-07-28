---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-114-fy2025
title: Long Term Care Ombud — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 114, FY2025
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
  - expenditures-114-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-114
- long-term-care-ombud
agency_code: '114'
agency_name: LONG TERM CARE OMBUD
fiscal_year: 2025
total_expense: '1136601.32'
transaction_count: 209
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Long Term Care Ombud — FY2025 expenditures

## At a glance

Long Term Care Ombud (agency code 114, recorded upstream as `LONG TERM CARE OMBUD`) spent **$1,136,601.32** in fiscal year 2025, across 209 transaction records. That is up 29.1% from $880,263.26 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **61 of 80** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $462,122.71 (40.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $462,122.71 | 40.7% | 1 |
| 4225 | State Government Service Charges | $227,665.92 | 20.0% | 4 |
| 4100 | Instate Travel | $141,797.74 | 12.5% | 91 |
| 4650 | Other Services And Supplies | $92,039.45 | 8.1% | 5 |
| 4425 | Lease Payments & Taxes | $55,344.57 | 4.9% | 3 |
| 4275 | Publicity & Publications | $36,884.55 | 3.2% | 10 |
| 3110 | Class/Unclass Salary & Per Diem | $27,143.62 | 2.4% | 1 |
| 4315 | It Professional Services | $21,775.00 | 1.9% | 2 |
| 4250 | Data Processing | $18,855.82 | 1.7% | 3 |
| 4300 | Professional Services | $16,494.88 | 1.5% | 9 |
| 4175 | Office Expenses | $14,668.20 | 1.3% | 14 |
| 4150 | Employee Training | $8,633.35 | 0.8% | 36 |
| 4575 | Agency Program Related Svcs & Supp | $3,866.24 | 0.3% | 9 |
| 4200 | Telecomm/Tech Svc And Supplies | $3,860.68 | 0.3% | 2 |
| 4125 | Out-Of-State Travel | $3,489.12 | 0.3% | 11 |
| 4400 | Dues And Subscriptions | $1,015.44 | 0.1% | 2 |
| 4715 | It Expendable Property | $542.71 | 0.0% | 2 |
| 4550 | Other Care Of Residents & Patients | $401.32 | 0.0% | 4 |

## Largest expenditure classes

The 12 largest of 50 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $462,122.71 | 40.7% |
| 4600 | State Government Service Charges | $227,665.92 | 20.0% |
| 4701 | Other Services | $89,534.41 | 7.9% |
| 4108 | Instate Ground Transportation | $74,201.20 | 6.5% |
| 4800 | Interagency Lease Payments | $55,344.57 | 4.9% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $40,694.57 | 3.6% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $36,884.55 | 3.2% |
| 3111 | Regular Employees | $27,143.62 | 2.4% |
| 4514 | Professional Services Application Mod | $16,915.00 | 1.5% |
| 4500 | Professional Services Non-It | $16,494.88 | 1.5% |
| 4101 | Instate Meals With Overnight Stay | $15,337.51 | 1.3% |
| 4367 | Computer Technology Pc Support | $11,950.63 | 1.1% |

## Curator notes

Figures are aggregated from 209 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='114' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


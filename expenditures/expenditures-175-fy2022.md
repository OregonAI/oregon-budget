---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-175-fy2022
title: Judicial Fitness & Disability — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 175, FY2022
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5378b32aad5d54d03160dd49832cc5c4f45e517dde8ba96c7e5b8bbb6e3a99f4
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
  - expenditures-175-fy2021
  - expenditures-175-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-175
- judicial-fitness-disability
agency_code: '175'
agency_name: JUDICIAL FITNESS & DISABILITY
fiscal_year: 2022
total_expense: '56507.27'
transaction_count: 22
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Judicial Fitness & Disability — FY2022 expenditures

## At a glance

Judicial Fitness & Disability (agency code 175, recorded upstream as `JUDICIAL FITNESS & DISABILITY`) spent **$56,507.27** in fiscal year 2022, across 22 transaction records. That is up 169.4% from $20,975.62 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **75 of 76** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $38,424.85 (68.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $38,424.85 | 68.0% | 3 |
| 4425 | Lease Payments & Taxes | $6,600.00 | 11.7% | 2 |
| 4300 | Professional Services | $4,106.21 | 7.3% | 1 |
| 4400 | Dues And Subscriptions | $3,363.00 | 6.0% | 3 |
| 4175 | Office Expenses | $2,606.27 | 4.6% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $991.39 | 1.8% | 3 |
| 4100 | Instate Travel | $415.55 | 0.7% | 5 |

## Largest expenditure classes

The 12 largest of 12 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $38,424.85 | 68.0% |
| 4804 | Other Lease Payments | $6,050.00 | 10.7% |
| 4500 | Professional Services Non-It | $4,106.21 | 7.3% |
| 4250 | Dues/Memberships | $3,363.00 | 6.0% |
| 4201 | Office Services | $1,879.58 | 3.3% |
| 4301 | Telecom/Voice Usage | $875.04 | 1.5% |
| 4200 | Office Supplies | $726.69 | 1.3% |
| 4800 | Interagency Lease Payments | $550.00 | 1.0% |
| 4106 | Instate Lodging | $198.45 | 0.4% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $174.16 | 0.3% |
| 4315 | Telecom/Teleconference Usage | $116.35 | 0.2% |
| 4101 | Instate Meals With Overnight Stay | $42.94 | 0.1% |

## Curator notes

Figures are aggregated from 22 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='175' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


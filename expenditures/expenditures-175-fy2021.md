---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-175-fy2021
title: Judicial Fitness & Disability — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 175, FY2021
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
  - expenditures-175-fy2020
  - expenditures-175-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-175
- judicial-fitness-disability
agency_code: '175'
agency_name: JUDICIAL FITNESS & DISABILITY
fiscal_year: 2021
total_expense: '20975.62'
transaction_count: 18
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Judicial Fitness & Disability — FY2021 expenditures

## At a glance

Judicial Fitness & Disability (agency code 175, recorded upstream as `JUDICIAL FITNESS & DISABILITY`) spent **$20,975.62** in fiscal year 2021, across 18 transaction records. That is down 56.6% from $48,379.01 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **75 of 76** agencies reporting that year.

The largest budget category was **Office Expenses** at $10,761.96 (51.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4175 | Office Expenses | $10,761.96 | 51.3% | 7 |
| 4425 | Lease Payments & Taxes | $7,700.00 | 36.7% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $813.46 | 3.9% | 3 |
| 4715 | It Expendable Property | $769.00 | 3.7% | 1 |
| 4400 | Dues And Subscriptions | $667.00 | 3.2% | 2 |
| 4225 | State Government Service Charges | $135.00 | 0.6% | 2 |
| 4150 | Employee Training | $65.00 | 0.3% | 1 |
| 4300 | Professional Services | $64.20 | 0.3% | 1 |

## Largest expenditure classes

The 9 largest of 9 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4201 | Office Services | $10,761.96 | 51.3% |
| 4800 | Facilities Rent | $7,700.00 | 36.7% |
| 4365 | Computer Technology Pc Equipment<$5K | $769.00 | 3.7% |
| 4250 | Dues/Memberships | $667.00 | 3.2% |
| 4301 | Telecom/Voice Usage | $619.22 | 3.0% |
| 4315 | Telecom/Teleconference Usage | $194.24 | 0.9% |
| 4600 | State Government Service Charges | $135.00 | 0.6% |
| 4406 | Prof Dev Instate Tuition/Registration | $65.00 | 0.3% |
| 4500 | Professional Services Non-It | $64.20 | 0.3% |

## Curator notes

Figures are aggregated from 18 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='175' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


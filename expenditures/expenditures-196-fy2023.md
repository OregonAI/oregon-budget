---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-196-fy2023
title: Dist Attorneys/Deputies — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 196, FY2023
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
  - expenditures-196-fy2022
  - expenditures-196-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-196
- dist-attorneys-deputies
agency_code: '196'
agency_name: DIST ATTORNEYS/DEPUTIES
fiscal_year: 2023
total_expense: '423098.04'
transaction_count: 12
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dist Attorneys/Deputies — FY2023 expenditures

## At a glance

Dist Attorneys/Deputies (agency code 196, recorded upstream as `DIST ATTORNEYS/DEPUTIES`) spent **$423,098.04** in fiscal year 2023, across 12 transaction records. That is down 21.1% from $536,075.15 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **66 of 77** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $345,339.12 (81.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $345,339.12 | 81.6% | 4 |
| 4300 | Professional Services | $36,980.30 | 8.7% | 2 |
| 4715 | It Expendable Property | $24,841.50 | 5.9% | 2 |
| 4650 | Other Services And Supplies | $8,502.90 | 2.0% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $7,363.11 | 1.7% | 1 |
| 4175 | Office Expenses | $43.11 | 0.0% | 1 |
| 3220 | Public Employes' Retirement System | $28.00 | 0.0% | 1 |

## Largest expenditure classes

The 8 largest of 8 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $345,339.12 | 81.6% |
| 4500 | Professional Services Non-It | $36,980.30 | 8.7% |
| 4306 | Telecom/Network Equipment<$5K | $20,790.00 | 4.9% |
| 4701 | Other Services | $8,502.90 | 2.0% |
| 4975 | Agency Program Related Services | $7,363.11 | 1.7% |
| 4361 | Computer Technology Server Software<$5K | $4,051.50 | 1.0% |
| 4201 | Office Services | $43.11 | 0.0% |
| 3210 | Public Employees Retirement Contribution | $28.00 | 0.0% |

## Curator notes

Figures are aggregated from 12 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='196' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


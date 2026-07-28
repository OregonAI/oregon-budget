---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-131-fy2021
title: Advocacy Commissions, OR — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 131, FY2021
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
  - expenditures-131-fy2020
  - expenditures-131-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-131
- advocacy-commissions-or
agency_code: '131'
agency_name: ADVOCACY COMMISSIONS, OR
fiscal_year: 2021
total_expense: '35837.43'
transaction_count: 30
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Advocacy Commissions, OR — FY2021 expenditures

## At a glance

Advocacy Commissions, OR (agency code 131, recorded upstream as `ADVOCACY COMMISSIONS, OR`) spent **$35,837.43** in fiscal year 2021, across 30 transaction records. That is down 51.9% from $74,472.90 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **74 of 76** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $13,694.37 (38.2% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $13,694.37 | 38.2% | 3 |
| 4225 | State Government Service Charges | $10,335.60 | 28.8% | 4 |
| 4250 | Data Processing | $7,297.01 | 20.4% | 2 |
| 4715 | It Expendable Property | $2,167.68 | 6.0% | 1 |
| 4150 | Employee Training | $675.00 | 1.9% | 1 |
| 4100 | Instate Travel | $581.48 | 1.6% | 14 |
| 4300 | Professional Services | $500.30 | 1.4% | 2 |
| 4325 | Attorney General Legal Fees | $321.00 | 0.9% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $250.00 | 0.7% | 1 |
| 4175 | Office Expenses | $14.99 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 14 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4701 | Other Services | $13,650.60 | 38.1% |
| 4600 | State Government Service Charges | $10,335.60 | 28.8% |
| 4375 | Computer Technology Computer Processing | $7,002.34 | 19.5% |
| 4365 | Computer Technology Pc Equipment<$5K | $2,167.68 | 6.0% |
| 4406 | Prof Dev Instate Tuition/Registration | $675.00 | 1.9% |
| 4111 | Instate Mileage Reimbursmnt-Volunteers | $502.98 | 1.4% |
| 4500 | Professional Services Non-It | $500.30 | 1.4% |
| 4550 | Attorney General Legal Fees | $321.00 | 0.9% |
| 4367 | Computer Technology Pc Support | $294.67 | 0.8% |
| 4975 | Agency Program Related Services | $250.00 | 0.7% |
| 4108 | Instate Ground Transportation | $78.50 | 0.2% |
| 4255 | Prizes And Awards | $43.69 | 0.1% |

## Curator notes

Figures are aggregated from 30 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='131' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


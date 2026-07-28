---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-104-fy2024
title: Public Records Advocate, Office of — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 104, FY2024
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: decef95a644d748f5c62eca57f2ec65a1ac01802ec192ae6fe9a4da7eed2a7c0
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
  - expenditures-104-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-104
- public-records-advocate-office-of
agency_code: '104'
agency_name: PUBLIC RECORDS ADVOCATE, OFFICE OF
fiscal_year: 2024
total_expense: '47687.22'
transaction_count: 11
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Public Records Advocate, Office of — FY2024 expenditures

## At a glance

Public Records Advocate, Office of (agency code 104, recorded upstream as `PUBLIC RECORDS ADVOCATE, OFFICE OF`) spent **$47,687.22** in fiscal year 2024, across 11 transaction records. No spending is recorded for this agency in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **79 of 80** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $20,976.87 (44.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $20,976.87 | 44.0% | 1 |
| 4225 | State Government Service Charges | $20,204.10 | 42.4% | 3 |
| 4250 | Data Processing | $5,532.50 | 11.6% | 1 |
| 4715 | It Expendable Property | $732.27 | 1.5% | 3 |
| 4100 | Instate Travel | $199.48 | 0.4% | 2 |
| 4300 | Professional Services | $42.00 | 0.1% | 1 |

## Largest expenditure classes

The 9 largest of 9 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4701 | Other Services | $20,976.87 | 44.0% |
| 4600 | State Government Service Charges | $20,204.10 | 42.4% |
| 4367 | Computer Technology Pc Support | $5,532.50 | 11.6% |
| 4372 | Computer Technology Peripheral Equip<$5K | $369.91 | 0.8% |
| 4304 | Telecom/Voice Equipment<$5K | $208.46 | 0.4% |
| 4366 | Computer Technology Pc Software<$5K | $153.90 | 0.3% |
| 4108 | Instate Ground Transportation | $130.48 | 0.3% |
| 4101 | Instate Meals With Overnight Stay | $69.00 | 0.1% |
| 4500 | Professional Services Non-It | $42.00 | 0.1% |

## Curator notes

Figures are aggregated from 11 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='104' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


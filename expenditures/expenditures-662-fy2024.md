---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-662-fy2024
title: Land Use Brd of Appeals — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 662, FY2024
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
  - expenditures-662-fy2023
  - expenditures-662-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-662
- land-use-brd-of-appeals
agency_code: '662'
agency_name: LAND USE BRD OF APPEALS
fiscal_year: 2024
total_expense: '188424.41'
transaction_count: 37
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Land Use Brd of Appeals — FY2024 expenditures

## At a glance

Land Use Brd of Appeals (agency code 662, recorded upstream as `LAND USE BRD OF APPEALS`) spent **$188,424.41** in fiscal year 2024, across 37 transaction records. That is down 5.4% from $199,279.77 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **73 of 80** agencies reporting that year.

The largest budget category was **Lease Payments & Taxes** at $60,315.36 (32.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Lease Payments & Taxes | $60,315.36 | 32.0% | 1 |
| 4225 | State Government Service Charges | $45,573.79 | 24.2% | 5 |
| 4650 | Other Services And Supplies | $43,998.34 | 23.4% | 3 |
| 4250 | Data Processing | $21,406.82 | 11.4% | 3 |
| 4300 | Professional Services | $6,231.08 | 3.3% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $5,099.67 | 2.7% | 3 |
| 4175 | Office Expenses | $4,037.15 | 2.1% | 4 |
| 4150 | Employee Training | $881.66 | 0.5% | 8 |
| 4325 | Attorney General Legal Fees | $338.80 | 0.2% | 1 |
| 4275 | Publicity & Publications | $225.68 | 0.1% | 1 |
| 4400 | Dues And Subscriptions | $200.00 | 0.1% | 1 |
| 4100 | Instate Travel | $116.06 | 0.1% | 4 |

## Largest expenditure classes

The 12 largest of 22 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Interagency Lease Payments | $60,315.36 | 32.0% |
| 4600 | State Government Service Charges | $45,573.79 | 24.2% |
| 4701 | Other Services | $43,968.34 | 23.3% |
| 4367 | Computer Technology Pc Support | $19,363.50 | 10.3% |
| 4500 | Professional Services Non-It | $6,231.08 | 3.3% |
| 4201 | Office Services | $3,096.44 | 1.6% |
| 4301 | Telecom/Voice Usage | $2,947.99 | 1.6% |
| 4305 | Telecom/Network Services | $2,151.68 | 1.1% |
| 4375 | Computer Technology Computer Processing | $2,043.32 | 1.1% |
| 4202 | Equipment Rental | $908.92 | 0.5% |
| 4450 | Prof Dev Instate Mile Reimb-Full Rate | $450.66 | 0.2% |
| 4550 | Attorney General Legal Fees | $338.80 | 0.2% |

## Curator notes

Figures are aggregated from 37 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='662' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-199-fy2023
title: Government Ethics Cmsn — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 199, FY2023
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
  - expenditures-199-fy2022
  - expenditures-199-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-199
- government-ethics-cmsn
agency_code: '199'
agency_name: GOVERNMENT ETHICS CMSN
fiscal_year: 2023
total_expense: '549803.59'
transaction_count: 39
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Government Ethics Cmsn — FY2023 expenditures

## At a glance

Government Ethics Cmsn (agency code 199, recorded upstream as `GOVERNMENT ETHICS CMSN`) spent **$549,803.59** in fiscal year 2023, across 39 transaction records. That is up 20.2% from $457,517.49 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **63 of 77** agencies reporting that year.

The largest budget category was **It Professional Services** at $183,336.00 (33.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4315 | It Professional Services | $183,336.00 | 33.3% | 1 |
| 4325 | Attorney General Legal Fees | $110,794.20 | 20.2% | 1 |
| 4650 | Other Services And Supplies | $90,630.82 | 16.5% | 3 |
| 4425 | Lease Payments & Taxes | $44,520.26 | 8.1% | 1 |
| 4250 | Data Processing | $39,195.58 | 7.1% | 3 |
| 4225 | State Government Service Charges | $35,575.90 | 6.5% | 4 |
| 4300 | Professional Services | $18,197.18 | 3.3% | 3 |
| 4715 | It Expendable Property | $11,974.41 | 2.2% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $9,540.00 | 1.7% | 5 |
| 4100 | Instate Travel | $2,725.68 | 0.5% | 9 |
| 4175 | Office Expenses | $1,640.04 | 0.3% | 4 |
| 4150 | Employee Training | $1,216.18 | 0.2% | 2 |
| 4275 | Publicity & Publications | $457.34 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 22 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4515 | Professional Services Application Maint | $183,336.00 | 33.3% |
| 4550 | Attorney General Legal Fees | $110,794.20 | 20.2% |
| 4701 | Other Services | $90,531.32 | 16.5% |
| 4800 | Interagency Lease Payments | $44,520.26 | 8.1% |
| 4600 | State Government Service Charges | $35,575.90 | 6.5% |
| 4367 | Computer Technology Pc Support | $24,750.00 | 4.5% |
| 4500 | Professional Services Non-It | $18,197.18 | 3.3% |
| 4375 | Computer Technology Computer Processing | $14,445.58 | 2.6% |
| 4365 | Computer Technology Pc Equipment<$5K | $11,074.41 | 2.0% |
| 4305 | Telecom/Network Services | $6,044.78 | 1.1% |
| 4301 | Telecom/Voice Usage | $3,495.22 | 0.6% |
| 4108 | Instate Ground Transportation | $1,725.92 | 0.3% |

## Curator notes

Figures are aggregated from 39 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='199' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


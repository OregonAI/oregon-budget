---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-199-fy2021
title: Government Ethics Cmsn — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 199, FY2021
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
  - expenditures-199-fy2020
  - expenditures-199-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-199
- government-ethics-cmsn
agency_code: '199'
agency_name: GOVERNMENT ETHICS CMSN
fiscal_year: 2021
total_expense: '441931.23'
transaction_count: 28
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Government Ethics Cmsn — FY2021 expenditures

## At a glance

Government Ethics Cmsn (agency code 199, recorded upstream as `GOVERNMENT ETHICS CMSN`) spent **$441,931.23** in fiscal year 2021, across 28 transaction records. That is up 1.0% from $437,393.51 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **60 of 76** agencies reporting that year.

The largest budget category was **It Professional Services** at $151,700.00 (34.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4315 | It Professional Services | $151,700.00 | 34.3% | 2 |
| 4325 | Attorney General Legal Fees | $124,029.52 | 28.1% | 1 |
| 4425 | Lease Payments & Taxes | $46,133.10 | 10.4% | 1 |
| 4650 | Other Services And Supplies | $35,135.58 | 8.0% | 2 |
| 4225 | State Government Service Charges | $33,823.11 | 7.7% | 3 |
| 4250 | Data Processing | $20,394.32 | 4.6% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $14,844.86 | 3.4% | 5 |
| 4715 | It Expendable Property | $7,885.11 | 1.8% | 4 |
| 4300 | Professional Services | $5,846.80 | 1.3% | 2 |
| 4175 | Office Expenses | $1,483.25 | 0.3% | 3 |
| 4100 | Instate Travel | $655.58 | 0.1% | 3 |

## Largest expenditure classes

The 12 largest of 15 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4515 | Professional Services Application Maint | $151,700.00 | 34.3% |
| 4550 | Attorney General Legal Fees | $124,029.52 | 28.1% |
| 4800 | Facilities Rent | $46,133.10 | 10.4% |
| 4701 | Other Services | $35,135.58 | 8.0% |
| 4600 | State Government Service Charges | $33,823.11 | 7.7% |
| 4375 | Computer Technology Computer Processing | $20,394.32 | 4.6% |
| 4305 | Telecom/Network Services | $9,029.92 | 2.0% |
| 4500 | Professional Services Non-It | $5,846.80 | 1.3% |
| 4365 | Computer Technology Pc Equipment<$5K | $4,935.15 | 1.1% |
| 4301 | Telecom/Voice Usage | $4,631.62 | 1.0% |
| 4366 | Computer Technology Pc Software<$5K | $1,950.00 | 0.4% |
| 4201 | Office Services | $1,483.25 | 0.3% |

## Curator notes

Figures are aggregated from 28 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='199' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-144-fy2022
title: Legislative Rev Office — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 144, FY2022
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
  - expenditures-144-fy2021
  - expenditures-144-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-144
- legislative-rev-office
agency_code: '144'
agency_name: LEGISLATIVE REV OFFICE
fiscal_year: 2022
total_expense: '107840.89'
transaction_count: 43
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Rev Office — FY2022 expenditures

## At a glance

Legislative Rev Office (agency code 144, recorded upstream as `LEGISLATIVE REV OFFICE`) spent **$107,840.89** in fiscal year 2022, across 43 transaction records. That is up 57.4% from $68,531.02 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **74 of 76** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $31,909.52 (29.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $31,909.52 | 29.6% | 4 |
| 4300 | Professional Services | $21,000.00 | 19.5% | 1 |
| 4715 | It Expendable Property | $19,040.49 | 17.7% | 6 |
| 4400 | Dues And Subscriptions | $15,447.88 | 14.3% | 5 |
| 4175 | Office Expenses | $6,390.97 | 5.9% | 7 |
| 4275 | Publicity & Publications | $4,935.00 | 4.6% | 3 |
| 4650 | Other Services And Supplies | $4,013.43 | 3.7% | 2 |
| 4150 | Employee Training | $2,579.09 | 2.4% | 6 |
| 4250 | Data Processing | $1,312.24 | 1.2% | 1 |
| 4100 | Instate Travel | $656.06 | 0.6% | 3 |
| 4700 | Expendable Property $250-$5000 | $386.96 | 0.4% | 1 |
| 4125 | Out-Of-State Travel | $167.42 | 0.2% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $1.83 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 24 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $31,909.52 | 29.6% |
| 4500 | Professional Services Non-It | $21,000.00 | 19.5% |
| 4251 | Subscriptions And Publications | $15,447.88 | 14.3% |
| 4366 | Computer Technology Pc Software<$5K | $12,451.64 | 11.5% |
| 4365 | Computer Technology Pc Equipment<$5K | $6,588.85 | 6.1% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $4,935.00 | 4.6% |
| 4701 | Other Services | $4,013.43 | 3.7% |
| 4202 | Equipment Rental | $2,891.46 | 2.7% |
| 4201 | Office Services | $2,783.08 | 2.6% |
| 4367 | Computer Technology Pc Support | $1,312.24 | 1.2% |
| 4406 | Prof Dev Instate Tuition/Registration | $975.00 | 0.9% |
| 4200 | Office Supplies | $716.43 | 0.7% |

## Curator notes

Figures are aggregated from 43 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='144' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


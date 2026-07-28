---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-144-fy2019
title: Legislative Rev Office — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 144, FY2019
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 3900810723066d4651c7227ef0c74a8b9c41ff76c2e4bcebbbb6f2268e443d34
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
  - expenditures-144-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-144
- legislative-rev-office
agency_code: '144'
agency_name: LEGISLATIVE REV OFFICE
fiscal_year: 2019
total_expense: '62063.69'
transaction_count: 39
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Rev Office — FY2019 expenditures

## At a glance

Legislative Rev Office (agency code 144, recorded upstream as `LEGISLATIVE REV OFFICE`) spent **$62,063.69** in fiscal year 2019, across 39 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **75 of 78** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $19,452.38 (31.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $19,452.38 | 31.3% | 3 |
| 4300 | Professional Services | $14,396.20 | 23.2% | 2 |
| 4175 | Office Expenses | $6,555.94 | 10.6% | 7 |
| 4250 | Data Processing | $6,147.68 | 9.9% | 2 |
| 4400 | Dues And Subscriptions | $4,371.02 | 7.0% | 4 |
| 4275 | Publicity & Publications | $3,769.99 | 6.1% | 2 |
| 4715 | It Expendable Property | $3,699.20 | 6.0% | 4 |
| 4700 | Expendable Property $250-$5000 | $1,609.23 | 2.6% | 1 |
| 4150 | Employee Training | $1,154.54 | 1.9% | 6 |
| 4100 | Instate Travel | $608.75 | 1.0% | 6 |
| 4200 | Telecomm/Tech Svc And Supplies | $298.76 | 0.5% | 2 |

## Largest expenditure classes

The 12 largest of 23 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $19,452.38 | 31.3% |
| 4500 | Professional Services Non-It | $14,396.20 | 23.2% |
| 4367 | Computer Technology Pc Support | $6,147.68 | 9.9% |
| 4251 | Subscriptions And Publications | $4,371.02 | 7.0% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $3,769.99 | 6.1% |
| 4200 | Office Supplies | $3,087.33 | 5.0% |
| 4202 | Equipment Rental | $2,891.46 | 4.7% |
| 4366 | Computer Technology Pc Software<$5K | $2,114.98 | 3.4% |
| 4999 | Expendable Property Non-It<$5K | $1,609.23 | 2.6% |
| 4365 | Computer Technology Pc Equipment<$5K | $1,584.22 | 2.6% |
| 4406 | Prof Dev Instate Tuition/Registration | $950.00 | 1.5% |
| 4201 | Office Services | $577.15 | 0.9% |

## Curator notes

Figures are aggregated from 39 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='144' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


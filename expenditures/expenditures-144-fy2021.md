---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-144-fy2021
title: Legislative Rev Office — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 144, FY2021
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
  - expenditures-144-fy2020
  - expenditures-144-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-144
- legislative-rev-office
agency_code: '144'
agency_name: LEGISLATIVE REV OFFICE
fiscal_year: 2021
total_expense: '68531.02'
transaction_count: 23
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Rev Office — FY2021 expenditures

## At a glance

Legislative Rev Office (agency code 144, recorded upstream as `LEGISLATIVE REV OFFICE`) spent **$68,531.02** in fiscal year 2021, across 23 transaction records. That is up 2.7% from $66,705.65 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **73 of 76** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $27,007.57 (39.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $27,007.57 | 39.4% | 3 |
| 4715 | It Expendable Property | $24,281.83 | 35.4% | 7 |
| 4400 | Dues And Subscriptions | $10,493.79 | 15.3% | 4 |
| 4175 | Office Expenses | $4,129.57 | 6.0% | 5 |
| 4275 | Publicity & Publications | $2,560.00 | 3.7% | 1 |
| 4150 | Employee Training | $36.36 | 0.1% | 1 |
| 4650 | Other Services And Supplies | $15.00 | 0.0% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $6.90 | 0.0% | 1 |

## Largest expenditure classes

The 11 largest of 11 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $27,007.57 | 39.4% |
| 4366 | Computer Technology Pc Software<$5K | $21,808.70 | 31.8% |
| 4251 | Subscriptions And Publications | $10,493.79 | 15.3% |
| 4202 | Equipment Rental | $2,669.04 | 3.9% |
| 4253 | Advertise Publicity Publish/Print Srvs | $2,560.00 | 3.7% |
| 4365 | Computer Technology Pc Equipment<$5K | $2,473.13 | 3.6% |
| 4200 | Office Supplies | $1,298.11 | 1.9% |
| 4201 | Office Services | $162.42 | 0.2% |
| 4426 | Prof Dev Training Materials | $36.36 | 0.1% |
| 4701 | Other Services | $15.00 | 0.0% |
| 4315 | Telecom/Teleconference Usage | $6.90 | 0.0% |

## Curator notes

Figures are aggregated from 23 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='144' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


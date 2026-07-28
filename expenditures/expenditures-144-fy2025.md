---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-144-fy2025
title: Legislative Rev Office — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 144, FY2025
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5e9f0c30287913ac0bfff8d74a1225d0c2816ca6a307f2141ebb35602c5a91ed
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
  - expenditures-144-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-144
- legislative-rev-office
agency_code: '144'
agency_name: LEGISLATIVE REV OFFICE
fiscal_year: 2025
total_expense: '159270.61'
transaction_count: 31
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Rev Office — FY2025 expenditures

## At a glance

Legislative Rev Office (agency code 144, recorded upstream as `LEGISLATIVE REV OFFICE`) spent **$159,270.61** in fiscal year 2025, across 31 transaction records. That is up 125.0% from $70,775.20 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **76 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $90,500.00 (56.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $90,500.00 | 56.8% | 1 |
| 4715 | It Expendable Property | $27,001.78 | 17.0% | 3 |
| 4225 | State Government Service Charges | $23,653.27 | 14.9% | 3 |
| 4400 | Dues And Subscriptions | $4,889.00 | 3.1% | 2 |
| 4175 | Office Expenses | $2,996.63 | 1.9% | 10 |
| 4275 | Publicity & Publications | $2,800.00 | 1.8% | 1 |
| 4650 | Other Services And Supplies | $2,653.50 | 1.7% | 3 |
| 4150 | Employee Training | $2,205.00 | 1.4% | 5 |
| 4250 | Data Processing | $1,722.06 | 1.1% | 1 |
| 4100 | Instate Travel | $849.37 | 0.5% | 2 |

## Largest expenditure classes

The 12 largest of 19 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $90,500.00 | 56.8% |
| 4600 | State Government Service Charges | $23,653.27 | 14.9% |
| 4365 | Computer Technology Pc Equipment<$5K | $23,625.70 | 14.8% |
| 4251 | Subscriptions And Publications | $4,889.00 | 3.1% |
| 4366 | Computer Technology Pc Software<$5K | $3,376.08 | 2.1% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $2,800.00 | 1.8% |
| 4202 | Equipment Rental | $2,446.62 | 1.5% |
| 4701 | Other Services | $1,818.70 | 1.1% |
| 4367 | Computer Technology Pc Support | $1,722.06 | 1.1% |
| 4434 | Prof Dev Out-Of-State Lodging | $1,185.68 | 0.7% |
| 4704 | Other Supplies | $834.80 | 0.5% |
| 4106 | Instate Lodging | $653.73 | 0.4% |

## Curator notes

Figures are aggregated from 31 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='144' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


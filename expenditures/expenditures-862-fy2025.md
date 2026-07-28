---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-862-fy2025
title: Racing Cmsn — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 862, FY2025
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
  - expenditures-862-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-862
- racing-cmsn
agency_code: '862'
agency_name: RACING CMSN
fiscal_year: 2025
total_expense: '2609403.54'
transaction_count: 156
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Racing Cmsn — FY2025 expenditures

## At a glance

Racing Cmsn (agency code 862, recorded upstream as `RACING CMSN`) spent **$2,609,403.54** in fiscal year 2025, across 156 transaction records. That is up 29.9% from $2,008,842.26 in FY2024. The agency accounts for 0.01% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **50 of 80** agencies reporting that year.

The largest budget category was **Distribution To Non-Governments** at $2,257,118.65 (86.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6030 | Distribution To Non-Governments | $2,257,118.65 | 86.5% | 9 |
| 4100 | Instate Travel | $72,957.01 | 2.8% | 56 |
| 4650 | Other Services And Supplies | $71,615.63 | 2.7% | 14 |
| 4225 | State Government Service Charges | $52,368.54 | 2.0% | 4 |
| 4575 | Agency Program Related Svcs & Supp | $35,898.75 | 1.4% | 4 |
| 4125 | Out-Of-State Travel | $28,908.17 | 1.1% | 18 |
| 4325 | Attorney General Legal Fees | $25,355.00 | 1.0% | 1 |
| 4250 | Data Processing | $18,141.27 | 0.7% | 2 |
| 4150 | Employee Training | $16,970.31 | 0.7% | 23 |
| 4300 | Professional Services | $15,034.21 | 0.6% | 6 |
| 4715 | It Expendable Property | $4,437.68 | 0.2% | 1 |
| 3240 | Unemployment Assessment | $3,952.00 | 0.2% | 1 |
| 4175 | Office Expenses | $2,747.76 | 0.1% | 11 |
| 4425 | Lease Payments & Taxes | $1,923.00 | 0.1% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $1,069.19 | 0.0% | 1 |
| 4275 | Publicity & Publications | $666.63 | 0.0% | 2 |
| 3115 | Board Member Stipends | $155.00 | 0.0% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $84.74 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 46 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6725 | Distribution To Non-Governments | $2,257,118.65 | 86.5% |
| 4600 | State Government Service Charges | $52,368.54 | 2.0% |
| 4701 | Other Services | $52,057.28 | 2.0% |
| 4106 | Instate Lodging | $39,618.15 | 1.5% |
| 4975 | Agency Program Related Services | $34,881.75 | 1.3% |
| 4550 | Attorney General Legal Fees | $25,355.00 | 1.0% |
| 4375 | Computer Technology Computer Processing | $17,801.27 | 0.7% |
| 4704 | Other Supplies | $15,612.07 | 0.6% |
| 4500 | Professional Services Non-It | $15,034.21 | 0.6% |
| 4159 | Out-Of-State Air Transportation | $14,284.50 | 0.5% |
| 4101 | Instate Meals With Overnight Stay | $12,429.75 | 0.5% |
| 4108 | Instate Ground Transportation | $9,998.19 | 0.4% |

## Curator notes

Figures are aggregated from 156 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='862' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


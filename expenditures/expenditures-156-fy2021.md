---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-156-fy2021
title: Legislative Admin Cmte — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 156, FY2021
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
  - expenditures-156-fy2020
  - expenditures-156-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-156
- legislative-admin-cmte
agency_code: '156'
agency_name: LEGISLATIVE ADMIN CMTE
fiscal_year: 2021
total_expense: '26681673.49'
transaction_count: 289
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Admin Cmte — FY2021 expenditures

## At a glance

Legislative Admin Cmte (agency code 156, recorded upstream as `LEGISLATIVE ADMIN CMTE`) spent **$26,681,673.49** in fiscal year 2021, across 289 transaction records. That is up 6.1% from $25,139,856.83 in FY2020. The agency accounts for 0.10% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **30 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $11,996,481.58 (45.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $11,996,481.58 | 45.0% | 27 |
| 7100 | Principal - Bonds | $5,024,343.29 | 18.8% | 1 |
| 7150 | Interest - Bonds | $3,232,897.01 | 12.1% | 1 |
| 6257 | Dist To State Police | $2,105,886.48 | 7.9% | 1 |
| 4715 | It Expendable Property | $1,309,028.72 | 4.9% | 50 |
| 4650 | Other Services And Supplies | $1,173,897.35 | 4.4% | 48 |
| 4225 | State Government Service Charges | $439,065.96 | 1.6% | 4 |
| 4450 | Fuels And Utilities | $363,672.86 | 1.4% | 7 |
| 4475 | Facilities Maintenance | $269,609.02 | 1.0% | 56 |
| 4250 | Data Processing | $212,828.65 | 0.8% | 13 |
| 4315 | It Professional Services | $195,270.43 | 0.7% | 9 |
| 4200 | Telecomm/Tech Svc And Supplies | $185,380.63 | 0.7% | 16 |
| 4175 | Office Expenses | $51,516.32 | 0.2% | 25 |
| 4150 | Employee Training | $45,328.12 | 0.2% | 18 |
| 4700 | Expendable Property $250-$5000 | $32,667.81 | 0.1% | 5 |
| 4425 | Lease Payments & Taxes | $23,682.26 | 0.1% | 2 |
| 4325 | Attorney General Legal Fees | $11,128.00 | 0.0% | 1 |
| 3240 | Unemployment Assessment | $7,471.20 | 0.0% | 1 |
| 3270 | Flexible Benefits | $877.24 | 0.0% | 1 |
| 4400 | Dues And Subscriptions | $488.02 | 0.0% | 2 |
| 4275 | Publicity & Publications | $152.54 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 45 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $11,996,481.58 | 45.0% |
| 7100 | Principal-Bonds | $5,024,343.29 | 18.8% |
| 7250 | Interest-Bonds | $3,232,897.01 | 12.1% |
| 6136 | Distribution To State Police | $2,105,886.48 | 7.9% |
| 4701 | Other Services | $749,266.17 | 2.8% |
| 4366 | Computer Technology Pc Software<$5K | $608,475.62 | 2.3% |
| 4600 | State Government Service Charges | $439,065.96 | 1.6% |
| 4825 | Fuels And Utilities | $363,672.86 | 1.4% |
| 4050 | Bond Costs | $319,266.98 | 1.2% |
| 4361 | Computer Technology Server Software<$5K | $243,805.35 | 0.9% |
| 4365 | Computer Technology Pc Equipment<$5K | $190,897.05 | 0.7% |
| 4519 | Professional Serv/Managed Serv Provider | $186,473.43 | 0.7% |

## Curator notes

Figures are aggregated from 289 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='156' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


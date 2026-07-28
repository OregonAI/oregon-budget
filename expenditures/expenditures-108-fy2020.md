---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-108-fy2020
title: Mental Health Regulatory Agy — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 108, FY2020
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: b73d59a16a10ad7f6ae4f4b415cba8d78894a3ead0e3928fe994cc49b9b11284
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
  - expenditures-108-fy2019
  - expenditures-108-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-108
- mental-health-regulatory-agy
agency_code: '108'
agency_name: MENTAL HEALTH REGULATORY AGY
fiscal_year: 2020
total_expense: '727932.46'
transaction_count: 104
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Mental Health Regulatory Agy — FY2020 expenditures

## At a glance

Mental Health Regulatory Agy (agency code 108, recorded upstream as `MENTAL HEALTH REGULATORY AGY`) spent **$727,932.46** in fiscal year 2020, across 104 transaction records. That is up 0.5% from $724,027.26 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **55 of 77** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $257,404.45 (35.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $257,404.45 | 35.4% | 1 |
| 4300 | Professional Services | $93,121.53 | 12.8% | 5 |
| 4425 | Facilities Rent & Taxes | $88,375.80 | 12.1% | 1 |
| 4650 | Other Services And Supplies | $84,778.30 | 11.6% | 6 |
| 4225 | State Government Service Charges | $50,634.62 | 7.0% | 5 |
| 4575 | Agency Program Related Svcs & Supp | $47,305.25 | 6.5% | 3 |
| 4250 | Data Processing | $31,435.87 | 4.3% | 5 |
| 4315 | It Professional Services | $25,517.07 | 3.5% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $13,779.74 | 1.9% | 5 |
| 4175 | Office Expenses | $11,055.56 | 1.5% | 3 |
| 4100 | Instate Travel | $7,293.37 | 1.0% | 33 |
| 4125 | Out-Of-State Travel | $6,041.13 | 0.8% | 15 |
| 4715 | It Expendable Property | $4,233.63 | 0.6% | 3 |
| 4150 | Employee Training | $2,605.89 | 0.4% | 12 |
| 4275 | Publicity & Publications | $2,564.81 | 0.4% | 3 |
| 3240 | Unemployment Assessment | $1,285.44 | 0.2% | 1 |
| 4400 | Dues And Subscriptions | $500.00 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 42 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $257,404.45 | 35.4% |
| 4500 | Professional Services Non-It | $93,121.53 | 12.8% |
| 4800 | Facilities Rent | $88,375.80 | 12.1% |
| 4701 | Other Services | $71,199.27 | 9.8% |
| 4600 | State Government Service Charges | $50,634.62 | 7.0% |
| 4975 | Agency Program Related Services | $47,305.25 | 6.5% |
| 4362 | Computer Technology Server Support | $28,188.00 | 3.9% |
| 4519 | Professional Serv/Managed Serv Provider | $25,517.07 | 3.5% |
| 4730 | Merchant Fees | $12,720.63 | 1.7% |
| 4201 | Office Services | $11,038.15 | 1.5% |
| 4305 | Telecom/Network Services | $5,427.79 | 0.7% |
| 4111 | Instate Mileage Reimbursmnt-Volunteers | $4,903.22 | 0.7% |

## Curator notes

Figures are aggregated from 104 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='108' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


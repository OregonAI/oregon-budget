---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-108-fy2025
title: Mental Health Regulatory Agy — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 108, FY2025
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
  - expenditures-108-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-108
- mental-health-regulatory-agy
agency_code: '108'
agency_name: MENTAL HEALTH REGULATORY AGY
fiscal_year: 2025
total_expense: '988856.19'
transaction_count: 62
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Mental Health Regulatory Agy — FY2025 expenditures

## At a glance

Mental Health Regulatory Agy (agency code 108, recorded upstream as `MENTAL HEALTH REGULATORY AGY`) spent **$988,856.19** in fiscal year 2025, across 62 transaction records. That is up 24.1% from $797,088.89 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **63 of 80** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $281,920.95 (28.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $281,920.95 | 28.5% | 2 |
| 4650 | Other Services And Supplies | $173,200.07 | 17.5% | 10 |
| 4425 | Lease Payments & Taxes | $129,283.98 | 13.1% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $117,485.25 | 11.9% | 1 |
| 4300 | Professional Services | $90,621.17 | 9.2% | 6 |
| 4225 | State Government Service Charges | $80,092.24 | 8.1% | 4 |
| 4250 | Data Processing | $42,461.73 | 4.3% | 3 |
| 4315 | It Professional Services | $30,000.00 | 3.0% | 1 |
| 4715 | It Expendable Property | $13,995.69 | 1.4% | 3 |
| 4175 | Office Expenses | $12,904.71 | 1.3% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $9,380.97 | 0.9% | 2 |
| 4400 | Dues And Subscriptions | $3,250.00 | 0.3% | 2 |
| 4275 | Publicity & Publications | $1,166.32 | 0.1% | 2 |
| 3110 | Class/Unclass Salary & Per Diem | $1,075.47 | 0.1% | 1 |
| 4150 | Employee Training | $817.20 | 0.1% | 4 |
| 4125 | Out-Of-State Travel | $808.66 | 0.1% | 9 |
| 4100 | Instate Travel | $391.78 | 0.0% | 6 |

## Largest expenditure classes

The 12 largest of 35 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $281,920.95 | 28.5% |
| 4800 | Interagency Lease Payments | $129,283.98 | 13.1% |
| 4701 | Other Services | $117,694.42 | 11.9% |
| 4975 | Agency Program Related Services | $117,485.25 | 11.9% |
| 4500 | Professional Services Non-It | $90,621.17 | 9.2% |
| 4600 | State Government Service Charges | $80,092.24 | 8.1% |
| 4730 | Merchant Fees | $53,986.01 | 5.5% |
| 4367 | Computer Technology Pc Support | $38,727.00 | 3.9% |
| 4519 | Professional Serv/Managed Serv Provider | $30,000.00 | 3.0% |
| 4201 | Office Services | $9,995.53 | 1.0% |
| 4365 | Computer Technology Pc Equipment<$5K | $5,905.63 | 0.6% |
| 4366 | Computer Technology Pc Software<$5K | $5,813.76 | 0.6% |

## Curator notes

Figures are aggregated from 62 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='108' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


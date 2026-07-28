---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-108-fy2024
title: Mental Health Regulatory Agy — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 108, FY2024
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: decef95a644d748f5c62eca57f2ec65a1ac01802ec192ae6fe9a4da7eed2a7c0
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
  - expenditures-108-fy2023
  - expenditures-108-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-108
- mental-health-regulatory-agy
agency_code: '108'
agency_name: MENTAL HEALTH REGULATORY AGY
fiscal_year: 2024
total_expense: '797088.89'
transaction_count: 63
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Mental Health Regulatory Agy — FY2024 expenditures

## At a glance

Mental Health Regulatory Agy (agency code 108, recorded upstream as `MENTAL HEALTH REGULATORY AGY`) spent **$797,088.89** in fiscal year 2024, across 63 transaction records. That is down 21.3% from $1,012,764.27 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **63 of 80** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $214,582.21 (26.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $214,582.21 | 26.9% | 2 |
| 4650 | Other Services And Supplies | $145,716.32 | 18.3% | 9 |
| 4425 | Lease Payments & Taxes | $126,130.66 | 15.8% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $96,149.54 | 12.1% | 2 |
| 4225 | State Government Service Charges | $80,326.84 | 10.1% | 4 |
| 4250 | Data Processing | $44,571.81 | 5.6% | 5 |
| 4300 | Professional Services | $36,838.31 | 4.6% | 4 |
| 4715 | It Expendable Property | $21,929.58 | 2.8% | 2 |
| 4175 | Office Expenses | $10,905.22 | 1.4% | 7 |
| 4200 | Telecomm/Tech Svc And Supplies | $8,612.46 | 1.1% | 3 |
| 4315 | It Professional Services | $6,000.00 | 0.8% | 1 |
| 4400 | Dues And Subscriptions | $1,760.00 | 0.2% | 3 |
| 4275 | Publicity & Publications | $1,305.35 | 0.2% | 1 |
| 4125 | Out-Of-State Travel | $1,132.18 | 0.1% | 6 |
| 4100 | Instate Travel | $1,128.41 | 0.1% | 13 |

## Largest expenditure classes

The 12 largest of 31 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $214,582.21 | 26.9% |
| 4800 | Interagency Lease Payments | $126,130.66 | 15.8% |
| 4701 | Other Services | $97,536.45 | 12.2% |
| 4975 | Agency Program Related Services | $96,053.25 | 12.1% |
| 4600 | State Government Service Charges | $80,326.84 | 10.1% |
| 4730 | Merchant Fees | $47,479.34 | 6.0% |
| 4367 | Computer Technology Pc Support | $39,299.58 | 4.9% |
| 4500 | Professional Services Non-It | $36,838.31 | 4.6% |
| 4365 | Computer Technology Pc Equipment<$5K | $20,635.33 | 2.6% |
| 4201 | Office Services | $9,376.50 | 1.2% |
| 4519 | Professional Serv/Managed Serv Provider | $6,000.00 | 0.8% |
| 4375 | Computer Technology Computer Processing | $5,272.23 | 0.7% |

## Curator notes

Figures are aggregated from 63 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='108' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


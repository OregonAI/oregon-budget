---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-860-fy2025
title: Public Utility Cmsn — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 860, FY2025
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
  - expenditures-860-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-860
- public-utility-cmsn
agency_code: '860'
agency_name: PUBLIC UTILITY CMSN
fiscal_year: 2025
total_expense: '39168728.61'
transaction_count: 430
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Public Utility Cmsn — FY2025 expenditures

## At a glance

Public Utility Cmsn (agency code 860, recorded upstream as `PUBLIC UTILITY CMSN`) spent **$39,168,728.61** in fiscal year 2025, across 430 transaction records. That is up 4.7% from $37,399,129.28 in FY2024. The agency accounts for 0.11% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **33 of 80** agencies reporting that year.

The largest budget category was **Distribution To Non-Governments** at $27,080,142.00 (69.1% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6030 | Distribution To Non-Governments | $27,080,142.00 | 69.1% | 34 |
| 4575 | Agency Program Related Svcs & Supp | $4,896,896.47 | 12.5% | 54 |
| 4325 | Attorney General Legal Fees | $2,851,481.77 | 7.3% | 1 |
| 4425 | Lease Payments & Taxes | $1,171,801.73 | 3.0% | 6 |
| 4300 | Professional Services | $792,326.24 | 2.0% | 19 |
| 4225 | State Government Service Charges | $697,213.42 | 1.8% | 5 |
| 4315 | It Professional Services | $505,859.85 | 1.3% | 5 |
| 4175 | Office Expenses | $224,698.49 | 0.6% | 18 |
| 4250 | Data Processing | $220,565.67 | 0.6% | 6 |
| 4715 | It Expendable Property | $154,212.58 | 0.4% | 11 |
| 4650 | Other Services And Supplies | $151,663.50 | 0.4% | 18 |
| 4200 | Telecomm/Tech Svc And Supplies | $146,382.95 | 0.4% | 9 |
| 4100 | Instate Travel | $103,130.08 | 0.3% | 89 |
| 4400 | Dues And Subscriptions | $70,097.20 | 0.2% | 16 |
| 4125 | Out-Of-State Travel | $67,071.16 | 0.2% | 107 |
| 4150 | Employee Training | $10,487.64 | 0.0% | 21 |
| 4275 | Publicity & Publications | $9,764.48 | 0.0% | 6 |
| 6055 | Distribution To Contract Svc Provider | $7,681.81 | 0.0% | 1 |
| 4700 | Expendable Property $250-$5000 | $6,955.57 | 0.0% | 2 |
| 4475 | Facilities Maintenance | $296.00 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 65 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6725 | Distribution To Non-Governments | $27,080,142.00 | 69.1% |
| 4975 | Agency Program Related Services | $3,708,555.99 | 9.5% |
| 4550 | Attorney General Legal Fees | $2,851,481.77 | 7.3% |
| 4976 | Agency Program Related Supplies | $1,188,207.08 | 3.0% |
| 7007 | Lease Pmt For Buildings | $1,048,294.11 | 2.7% |
| 4500 | Professional Services Non-It | $792,326.24 | 2.0% |
| 4600 | State Government Service Charges | $697,213.42 | 1.8% |
| 4513 | Professional Services Application New | $472,312.27 | 1.2% |
| 4367 | Computer Technology Pc Support | $196,881.17 | 0.5% |
| 4201 | Office Services | $189,784.12 | 0.5% |
| 4701 | Other Services | $149,586.00 | 0.4% |
| 4301 | Telecom/Voice Usage | $108,207.10 | 0.3% |

## Curator notes

Figures are aggregated from 430 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='860' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-862-fy2023
title: Racing Cmsn — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 862, FY2023
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 6400163010ab2f341831c864272a89c5e9f2a261fad3fd9572b230042f26e3d5
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
  - expenditures-862-fy2022
  - expenditures-862-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-862
- racing-cmsn
agency_code: '862'
agency_name: RACING CMSN
fiscal_year: 2023
total_expense: '2531808.65'
transaction_count: 129
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Racing Cmsn — FY2023 expenditures

## At a glance

Racing Cmsn (agency code 862, recorded upstream as `RACING CMSN`) spent **$2,531,808.65** in fiscal year 2023, across 129 transaction records. That is up 5.1% from $2,409,697.30 in FY2022. The agency accounts for 0.01% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **49 of 77** agencies reporting that year.

The largest budget category was **Distribution To Non-Governments** at $2,153,965.24 (85.1% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6030 | Distribution To Non-Governments | $2,153,965.24 | 85.1% | 10 |
| 4650 | Other Services And Supplies | $75,042.05 | 3.0% | 7 |
| 4325 | Attorney General Legal Fees | $67,881.00 | 2.7% | 1 |
| 4100 | Instate Travel | $49,285.87 | 1.9% | 39 |
| 4425 | Lease Payments & Taxes | $41,353.76 | 1.6% | 2 |
| 4225 | State Government Service Charges | $28,913.02 | 1.1% | 4 |
| 4575 | Agency Program Related Svcs & Supp | $23,853.45 | 0.9% | 5 |
| 4125 | Out-Of-State Travel | $20,802.48 | 0.8% | 16 |
| 4300 | Professional Services | $17,471.57 | 0.7% | 4 |
| 4250 | Data Processing | $13,049.32 | 0.5% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $12,965.18 | 0.5% | 6 |
| 4150 | Employee Training | $11,304.71 | 0.4% | 12 |
| 4175 | Office Expenses | $7,864.76 | 0.3% | 8 |
| 4700 | Expendable Property $250-$5000 | $4,496.19 | 0.2% | 4 |
| 3110 | Class/Unclass Salary & Per Diem | $1,530.33 | 0.1% | 1 |
| 4715 | It Expendable Property | $1,494.72 | 0.1% | 4 |
| 4275 | Publicity & Publications | $351.24 | 0.0% | 2 |
| 4400 | Dues And Subscriptions | $183.76 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 43 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6725 | Distribution To Non-Governments | $2,153,965.24 | 85.1% |
| 4701 | Other Services | $68,275.76 | 2.7% |
| 4550 | Attorney General Legal Fees | $67,881.00 | 2.7% |
| 4800 | Interagency Lease Payments | $41,353.76 | 1.6% |
| 4600 | State Government Service Charges | $28,913.02 | 1.1% |
| 4106 | Instate Lodging | $26,554.06 | 1.0% |
| 4975 | Agency Program Related Services | $23,774.00 | 0.9% |
| 4500 | Professional Services Non-It | $17,471.57 | 0.7% |
| 4375 | Computer Technology Computer Processing | $11,669.32 | 0.5% |
| 4159 | Out-Of-State Air Transportation | $10,636.08 | 0.4% |
| 4301 | Telecom/Voice Usage | $9,543.57 | 0.4% |
| 4108 | Instate Ground Transportation | $9,390.69 | 0.4% |

## Curator notes

Figures are aggregated from 129 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='862' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


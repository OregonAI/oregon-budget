---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-862-fy2021
title: Racing Cmsn — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 862, FY2021
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
  - expenditures-862-fy2020
  - expenditures-862-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-862
- racing-cmsn
agency_code: '862'
agency_name: RACING CMSN
fiscal_year: 2021
total_expense: '2593232.98'
transaction_count: 89
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Racing Cmsn — FY2021 expenditures

## At a glance

Racing Cmsn (agency code 862, recorded upstream as `RACING CMSN`) spent **$2,593,232.98** in fiscal year 2021, across 89 transaction records. That is up 78.2% from $1,455,315.29 in FY2020. The agency accounts for 0.01% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **45 of 76** agencies reporting that year.

The largest budget category was **Distribution To Non-Governments** at $2,197,890.00 (84.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6030 | Distribution To Non-Governments | $2,197,890.00 | 84.8% | 8 |
| 4225 | State Government Service Charges | $148,131.19 | 5.7% | 5 |
| 4325 | Attorney General Legal Fees | $45,266.14 | 1.7% | 1 |
| 4425 | Lease Payments & Taxes | $37,527.05 | 1.4% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $32,238.50 | 1.2% | 3 |
| 4650 | Other Services And Supplies | $31,090.55 | 1.2% | 11 |
| 4100 | Instate Travel | $19,468.27 | 0.8% | 27 |
| 4175 | Office Expenses | $14,679.22 | 0.6% | 10 |
| 4300 | Professional Services | $14,630.03 | 0.6% | 4 |
| 3240 | Unemployment Assessment | $13,401.26 | 0.5% | 1 |
| 4250 | Data Processing | $13,310.40 | 0.5% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $12,669.95 | 0.5% | 4 |
| 4150 | Employee Training | $8,315.90 | 0.3% | 3 |
| 4125 | Out-Of-State Travel | $3,021.77 | 0.1% | 3 |
| 4715 | It Expendable Property | $852.25 | 0.0% | 2 |
| 4700 | Expendable Property $250-$5000 | $529.00 | 0.0% | 1 |
| 4525 | Medical Supplies And Services | $112.50 | 0.0% | 1 |
| 4400 | Dues And Subscriptions | $99.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 30 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6725 | Distribution To Non-Governments | $2,197,890.00 | 84.8% |
| 4600 | State Government Service Charges | $148,131.19 | 5.7% |
| 4550 | Attorney General Legal Fees | $45,266.14 | 1.7% |
| 4800 | Interagency Lease Payments | $37,527.05 | 1.4% |
| 4975 | Agency Program Related Services | $32,238.50 | 1.2% |
| 4701 | Other Services | $26,375.39 | 1.0% |
| 4500 | Professional Services Non-It | $14,630.03 | 0.6% |
| 3231 | Unemployment Compensation & Assessment | $13,401.26 | 0.5% |
| 4375 | Computer Technology Computer Processing | $12,375.40 | 0.5% |
| 4200 | Office Supplies | $11,859.31 | 0.5% |
| 4301 | Telecom/Voice Usage | $10,369.31 | 0.4% |
| 4411 | Prof Dev Out-Of-State Tuition/Regist | $7,700.00 | 0.3% |

## Curator notes

Figures are aggregated from 89 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='862' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


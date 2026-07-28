---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-114-fy2020
title: Long Term Care Ombud — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 114, FY2020
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
  - expenditures-114-fy2019
  - expenditures-114-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-114
- long-term-care-ombud
agency_code: '114'
agency_name: LONG TERM CARE OMBUD
fiscal_year: 2020
total_expense: '551670.94'
transaction_count: 162
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Long Term Care Ombud — FY2020 expenditures

## At a glance

Long Term Care Ombud (agency code 114, recorded upstream as `LONG TERM CARE OMBUD`) spent **$551,670.94** in fiscal year 2020, across 162 transaction records. That is down 5.7% from $584,910.16 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **60 of 77** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $136,330.28 (24.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $136,330.28 | 24.7% | 1 |
| 4425 | Facilities Rent & Taxes | $103,562.07 | 18.8% | 2 |
| 4225 | State Government Service Charges | $79,481.36 | 14.4% | 5 |
| 4100 | Instate Travel | $66,817.95 | 12.1% | 84 |
| 4650 | Other Services And Supplies | $56,947.37 | 10.3% | 3 |
| 4250 | Data Processing | $31,485.01 | 5.7% | 4 |
| 6055 | Distribution To Contract Svc Provider | $20,060.00 | 3.6% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $16,647.78 | 3.0% | 6 |
| 4175 | Office Expenses | $12,990.04 | 2.4% | 10 |
| 4300 | Professional Services | $10,983.32 | 2.0% | 7 |
| 4150 | Employee Training | $6,291.36 | 1.1% | 14 |
| 4275 | Publicity & Publications | $5,083.85 | 0.9% | 10 |
| 4550 | Other Care Of Residents & Patients | $2,804.80 | 0.5% | 6 |
| 4715 | It Expendable Property | $716.64 | 0.1% | 2 |
| 4315 | It Professional Services | $575.00 | 0.1% | 1 |
| 4125 | Out-Of-State Travel | $496.59 | 0.1% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $395.28 | 0.1% | 4 |
| 4525 | Medical Supplies And Services | $2.24 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 40 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $136,330.28 | 24.7% |
| 4800 | Facilities Rent | $103,562.07 | 18.8% |
| 4600 | State Government Service Charges | $79,481.36 | 14.4% |
| 4701 | Other Services | $56,917.62 | 10.3% |
| 4108 | Instate Ground Transportation | $32,379.64 | 5.9% |
| 4375 | Computer Technology Computer Processing | $31,485.01 | 5.7% |
| 6910 | Distribution To Contract Svc Provider | $20,060.00 | 3.6% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $13,096.53 | 2.4% |
| 4305 | Telecom/Network Services | $11,333.66 | 2.1% |
| 4101 | Instate Meals With Overnight Stay | $11,196.75 | 2.0% |
| 4500 | Professional Services Non-It | $10,983.32 | 2.0% |
| 4202 | Equipment Rental | $7,312.27 | 1.3% |

## Curator notes

Figures are aggregated from 162 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='114' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


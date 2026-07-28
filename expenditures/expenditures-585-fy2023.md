---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-585-fy2023
title: Blind, Cmsn for the — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 585, FY2023
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
  - expenditures-585-fy2022
  - expenditures-585-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-585
- blind-cmsn-for-the
agency_code: '585'
agency_name: BLIND, CMSN FOR THE
fiscal_year: 2023
total_expense: '5907023.03'
transaction_count: 397
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Blind, Cmsn for the — FY2023 expenditures

## At a glance

Blind, Cmsn for the (agency code 585, recorded upstream as `BLIND, CMSN FOR THE`) spent **$5,907,023.03** in fiscal year 2023, across 397 transaction records. That is up 38.0% from $4,281,299.72 in FY2022. The agency accounts for 0.02% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **42 of 77** agencies reporting that year.

The largest budget category was **Other Special Payments** at $2,100,947.98 (35.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6085 | Other Special Payments | $2,100,947.98 | 35.6% | 120 |
| 4575 | Agency Program Related Svcs & Supp | $1,539,549.82 | 26.1% | 45 |
| 4650 | Other Services And Supplies | $435,539.71 | 7.4% | 27 |
| 4425 | Lease Payments & Taxes | $310,781.22 | 5.3% | 8 |
| 4225 | State Government Service Charges | $294,798.12 | 5.0% | 4 |
| 4315 | It Professional Services | $241,318.00 | 4.1% | 2 |
| 6040 | Distribution To Local School Dist | $238,253.67 | 4.0% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $141,023.56 | 2.4% | 19 |
| 4715 | It Expendable Property | $133,122.20 | 2.3% | 12 |
| 4325 | Attorney General Legal Fees | $130,171.43 | 2.2% | 1 |
| 4100 | Instate Travel | $106,583.15 | 1.8% | 69 |
| 4475 | Facilities Maintenance | $51,697.85 | 0.9% | 16 |
| 4250 | Data Processing | $40,700.55 | 0.7% | 2 |
| 4150 | Employee Training | $40,285.12 | 0.7% | 12 |
| 4175 | Office Expenses | $36,904.72 | 0.6% | 16 |
| 4125 | Out-Of-State Travel | $31,398.70 | 0.5% | 31 |
| 4400 | Dues And Subscriptions | $30,500.00 | 0.5% | 1 |
| 4300 | Professional Services | $1,952.17 | 0.0% | 5 |
| 4450 | Fuels And Utilities | $850.56 | 0.0% | 3 |
| 6035 | Distribution To Individuals | $450.00 | 0.0% | 1 |
| 4275 | Publicity & Publications | $194.50 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 51 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6900 | Other Special Payments | $2,100,947.98 | 35.6% |
| 4976 | Agency Program Related Supplies | $1,064,697.02 | 18.0% |
| 4975 | Agency Program Related Services | $474,852.80 | 8.0% |
| 4800 | Interagency Lease Payments | $310,781.22 | 5.3% |
| 4600 | State Government Service Charges | $294,798.12 | 5.0% |
| 4704 | Other Supplies | $292,742.77 | 5.0% |
| 4515 | Professional Services Application Maint | $241,318.00 | 4.1% |
| 6823 | Payments To Local School Districts | $238,253.67 | 4.0% |
| 4701 | Other Services | $130,213.34 | 2.2% |
| 4550 | Attorney General Legal Fees | $130,171.43 | 2.2% |
| 4108 | Instate Ground Transportation | $86,029.55 | 1.5% |
| 4301 | Telecom/Voice Usage | $72,138.29 | 1.2% |

## Curator notes

Figures are aggregated from 397 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='585' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


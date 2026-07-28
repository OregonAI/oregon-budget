---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-855-fy2023
title: Pharmacy, Oregon Brd of — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 855, FY2023
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
  - expenditures-855-fy2022
  - expenditures-855-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-855
- pharmacy-oregon-brd-of
agency_code: '855'
agency_name: PHARMACY, OREGON BRD OF
fiscal_year: 2023
total_expense: '1162645.87'
transaction_count: 115
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Pharmacy, Oregon Brd of — FY2023 expenditures

## At a glance

Pharmacy, Oregon Brd of (agency code 855, recorded upstream as `PHARMACY, OREGON BRD OF`) spent **$1,162,645.87** in fiscal year 2023, across 115 transaction records. That is down 5.1% from $1,224,483.76 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **54 of 77** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $251,808.08 (21.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $251,808.08 | 21.7% | 1 |
| 4650 | Other Services And Supplies | $223,782.44 | 19.2% | 6 |
| 4250 | Data Processing | $165,753.32 | 14.3% | 4 |
| 4425 | Lease Payments & Taxes | $141,216.96 | 12.1% | 2 |
| 4300 | Professional Services | $107,598.95 | 9.3% | 7 |
| 4575 | Agency Program Related Svcs & Supp | $104,037.90 | 8.9% | 7 |
| 4225 | State Government Service Charges | $97,659.90 | 8.4% | 4 |
| 4100 | Instate Travel | $28,595.12 | 2.5% | 40 |
| 4275 | Publicity & Publications | $15,331.22 | 1.3% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $13,112.13 | 1.1% | 3 |
| 4150 | Employee Training | $7,197.54 | 0.6% | 22 |
| 4175 | Office Expenses | $4,699.82 | 0.4% | 3 |
| 4315 | It Professional Services | $680.00 | 0.1% | 1 |
| 4715 | It Expendable Property | $479.52 | 0.0% | 1 |
| 4125 | Out-Of-State Travel | $429.04 | 0.0% | 8 |
| 3240 | Unemployment Assessment | $132.70 | 0.0% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $131.23 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 37 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $251,808.08 | 21.7% |
| 4375 | Computer Technology Computer Processing | $165,753.32 | 14.3% |
| 4800 | Interagency Lease Payments | $141,216.96 | 12.1% |
| 4701 | Other Services | $121,180.52 | 10.4% |
| 4500 | Professional Services Non-It | $107,598.95 | 9.3% |
| 4975 | Agency Program Related Services | $103,637.00 | 8.9% |
| 4600 | State Government Service Charges | $97,659.90 | 8.4% |
| 4730 | Merchant Fees | $95,798.93 | 8.2% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $15,331.22 | 1.3% |
| 4108 | Instate Ground Transportation | $12,382.95 | 1.1% |
| 4301 | Telecom/Voice Usage | $9,529.23 | 0.8% |
| 4101 | Instate Meals With Overnight Stay | $8,033.00 | 0.7% |

## Curator notes

Figures are aggregated from 115 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='855' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


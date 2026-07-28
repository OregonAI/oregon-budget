---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-855-fy2021
title: Pharmacy, Oregon Brd of — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 855, FY2021
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
  - expenditures-855-fy2020
  - expenditures-855-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-855
- pharmacy-oregon-brd-of
agency_code: '855'
agency_name: PHARMACY, OREGON BRD OF
fiscal_year: 2021
total_expense: '1032164.21'
transaction_count: 62
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Pharmacy, Oregon Brd of — FY2021 expenditures

## At a glance

Pharmacy, Oregon Brd of (agency code 855, recorded upstream as `PHARMACY, OREGON BRD OF`) spent **$1,032,164.21** in fiscal year 2021, across 62 transaction records. That is down 24.3% from $1,362,801.01 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **53 of 76** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $262,457.42 (25.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $262,457.42 | 25.4% | 1 |
| 4250 | Data Processing | $173,376.65 | 16.8% | 6 |
| 4650 | Other Services And Supplies | $138,169.17 | 13.4% | 7 |
| 4300 | Professional Services | $132,368.40 | 12.8% | 7 |
| 4425 | Lease Payments & Taxes | $93,075.95 | 9.0% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $82,792.25 | 8.0% | 1 |
| 4225 | State Government Service Charges | $81,571.28 | 7.9% | 4 |
| 4175 | Office Expenses | $19,952.53 | 1.9% | 6 |
| 4315 | It Professional Services | $16,297.35 | 1.6% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $14,160.48 | 1.4% | 3 |
| 4100 | Instate Travel | $8,645.22 | 0.8% | 15 |
| 4275 | Publicity & Publications | $6,945.25 | 0.7% | 4 |
| 4700 | Expendable Property $250-$5000 | $1,694.00 | 0.2% | 1 |
| 3240 | Unemployment Assessment | $329.26 | 0.0% | 1 |
| 4715 | It Expendable Property | $229.00 | 0.0% | 1 |
| 4400 | Dues And Subscriptions | $100.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 29 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $262,457.42 | 25.4% |
| 4375 | Computer Technology Computer Processing | $173,124.65 | 16.8% |
| 4500 | Professional Services Non-It | $132,368.40 | 12.8% |
| 4800 | Interagency Lease Payments | $93,075.95 | 9.0% |
| 4730 | Merchant Fees | $92,001.02 | 8.9% |
| 4975 | Agency Program Related Services | $82,792.25 | 8.0% |
| 4600 | State Government Service Charges | $81,571.28 | 7.9% |
| 4701 | Other Services | $45,433.10 | 4.4% |
| 4201 | Office Services | $17,699.82 | 1.7% |
| 4516 | Professional Services Servers | $10,500.00 | 1.0% |
| 4301 | Telecom/Voice Usage | $10,439.88 | 1.0% |
| 4108 | Instate Ground Transportation | $7,206.94 | 0.7% |

## Curator notes

Figures are aggregated from 62 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='855' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


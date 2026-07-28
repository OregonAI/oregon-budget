---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-834-fy2021
title: Dentistry, Brd of — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 834, FY2021
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
  - expenditures-834-fy2020
  - expenditures-834-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-834
- dentistry-brd-of
agency_code: '834'
agency_name: DENTISTRY, BRD OF
fiscal_year: 2021
total_expense: '615550.82'
transaction_count: 77
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dentistry, Brd of — FY2021 expenditures

## At a glance

Dentistry, Brd of (agency code 834, recorded upstream as `DENTISTRY, BRD OF`) spent **$615,550.82** in fiscal year 2021, across 77 transaction records. That is down 8.5% from $672,420.71 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **57 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $113,208.57 (18.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $113,208.57 | 18.4% | 7 |
| 4325 | Attorney General Legal Fees | $108,783.77 | 17.7% | 1 |
| 4425 | Lease Payments & Taxes | $89,735.59 | 14.6% | 1 |
| 4225 | State Government Service Charges | $81,330.09 | 13.2% | 4 |
| 4250 | Data Processing | $67,597.12 | 11.0% | 5 |
| 4650 | Other Services And Supplies | $47,204.33 | 7.7% | 7 |
| 4715 | It Expendable Property | $34,299.22 | 5.6% | 5 |
| 4575 | Agency Program Related Svcs & Supp | $21,514.08 | 3.5% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $16,043.50 | 2.6% | 7 |
| 4175 | Office Expenses | $15,489.04 | 2.5% | 10 |
| 4100 | Instate Travel | $8,221.73 | 1.3% | 19 |
| 4315 | It Professional Services | $4,500.00 | 0.7% | 1 |
| 4400 | Dues And Subscriptions | $4,490.13 | 0.7% | 3 |
| 4275 | Publicity & Publications | $1,690.38 | 0.3% | 3 |
| 4150 | Employee Training | $1,425.00 | 0.2% | 1 |
| 3240 | Unemployment Assessment | $18.27 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 32 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $113,208.57 | 18.4% |
| 4550 | Attorney General Legal Fees | $108,783.77 | 17.7% |
| 4800 | Interagency Lease Payments | $89,735.59 | 14.6% |
| 4600 | State Government Service Charges | $81,330.09 | 13.2% |
| 4375 | Computer Technology Computer Processing | $67,092.12 | 10.9% |
| 4701 | Other Services | $25,598.44 | 4.2% |
| 4366 | Computer Technology Pc Software<$5K | $23,109.00 | 3.8% |
| 4730 | Merchant Fees | $21,596.03 | 3.5% |
| 4975 | Agency Program Related Services | $19,324.25 | 3.1% |
| 4365 | Computer Technology Pc Equipment<$5K | $10,497.05 | 1.7% |
| 4301 | Telecom/Voice Usage | $8,480.36 | 1.4% |
| 4202 | Equipment Rental | $7,814.87 | 1.3% |

## Curator notes

Figures are aggregated from 77 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='834' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


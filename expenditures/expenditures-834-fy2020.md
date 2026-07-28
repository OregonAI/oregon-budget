---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-834-fy2020
title: Dentistry, Brd of — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 834, FY2020
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
  - expenditures-834-fy2019
  - expenditures-834-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-834
- dentistry-brd-of
agency_code: '834'
agency_name: DENTISTRY, BRD OF
fiscal_year: 2020
total_expense: '672420.71'
transaction_count: 120
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dentistry, Brd of — FY2020 expenditures

## At a glance

Dentistry, Brd of (agency code 834, recorded upstream as `DENTISTRY, BRD OF`) spent **$672,420.71** in fiscal year 2020, across 120 transaction records. That is up 6.3% from $632,790.30 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **57 of 77** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $143,350.85 (21.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $143,350.85 | 21.3% | 1 |
| 4300 | Professional Services | $120,639.74 | 17.9% | 8 |
| 4425 | Facilities Rent & Taxes | $87,121.98 | 13.0% | 1 |
| 4225 | State Government Service Charges | $81,582.39 | 12.1% | 4 |
| 5550 | Data Processing Software | $59,970.00 | 8.9% | 1 |
| 4650 | Other Services And Supplies | $48,862.53 | 7.3% | 6 |
| 4175 | Office Expenses | $27,965.80 | 4.2% | 12 |
| 4250 | Data Processing | $21,316.94 | 3.2% | 5 |
| 4150 | Employee Training | $19,324.54 | 2.9% | 34 |
| 4575 | Agency Program Related Svcs & Supp | $18,080.46 | 2.7% | 2 |
| 4100 | Instate Travel | $13,752.47 | 2.0% | 30 |
| 4200 | Telecomm/Tech Svc And Supplies | $12,915.80 | 1.9% | 6 |
| 4315 | It Professional Services | $6,000.00 | 0.9% | 1 |
| 4400 | Dues And Subscriptions | $5,626.39 | 0.8% | 3 |
| 4275 | Publicity & Publications | $2,823.52 | 0.4% | 3 |
| 4700 | Expendable Property $250-$5000 | $2,221.56 | 0.3% | 1 |
| 4715 | It Expendable Property | $865.74 | 0.1% | 2 |

## Largest expenditure classes

The 12 largest of 41 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $143,350.85 | 21.3% |
| 4500 | Professional Services Non-It | $120,639.74 | 17.9% |
| 4800 | Facilities Rent | $87,121.98 | 13.0% |
| 4600 | State Government Service Charges | $81,582.39 | 12.1% |
| 5303 | Information Tech Pc Software>=$5K | $59,970.00 | 8.9% |
| 4701 | Other Services | $25,998.23 | 3.9% |
| 4730 | Merchant Fees | $22,864.30 | 3.4% |
| 4375 | Computer Technology Computer Processing | $19,193.94 | 2.9% |
| 4975 | Agency Program Related Services | $14,769.00 | 2.2% |
| 4200 | Office Supplies | $13,107.11 | 1.9% |
| 4202 | Equipment Rental | $9,123.84 | 1.4% |
| 4305 | Telecom/Network Services | $7,810.30 | 1.2% |

## Curator notes

Figures are aggregated from 120 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='834' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


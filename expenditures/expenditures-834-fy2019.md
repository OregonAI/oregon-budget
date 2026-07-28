---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-834-fy2019
title: Dentistry, Brd of — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 834, FY2019
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 3900810723066d4651c7227ef0c74a8b9c41ff76c2e4bcebbbb6f2268e443d34
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
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-834
- dentistry-brd-of
agency_code: '834'
agency_name: DENTISTRY, BRD OF
fiscal_year: 2019
total_expense: '632790.30'
transaction_count: 134
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dentistry, Brd of — FY2019 expenditures

## At a glance

Dentistry, Brd of (agency code 834, recorded upstream as `DENTISTRY, BRD OF`) spent **$632,790.30** in fiscal year 2019, across 134 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **58 of 78** agencies reporting that year.

The largest budget category was **Professional Services** at $138,283.33 (21.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $138,283.33 | 21.9% | 10 |
| 4325 | Attorney General Legal Fees | $133,468.75 | 21.1% | 1 |
| 4425 | Facilities Rent & Taxes | $84,584.40 | 13.4% | 1 |
| 4225 | State Government Service Charges | $60,964.35 | 9.6% | 4 |
| 4650 | Other Services And Supplies | $44,900.79 | 7.1% | 6 |
| 4175 | Office Expenses | $37,776.67 | 6.0% | 12 |
| 4315 | It Professional Services | $26,100.00 | 4.1% | 1 |
| 4250 | Data Processing | $22,150.03 | 3.5% | 5 |
| 4575 | Agency Program Related Svcs & Supp | $21,642.49 | 3.4% | 2 |
| 4100 | Instate Travel | $17,342.93 | 2.7% | 41 |
| 4150 | Employee Training | $15,994.38 | 2.5% | 32 |
| 4200 | Telecomm/Tech Svc And Supplies | $11,851.69 | 1.9% | 6 |
| 4715 | It Expendable Property | $6,703.47 | 1.1% | 3 |
| 4400 | Dues And Subscriptions | $6,662.67 | 1.1% | 4 |
| 4275 | Publicity & Publications | $3,915.19 | 0.6% | 3 |
| 4125 | Out-Of-State Travel | $449.16 | 0.1% | 3 |

## Largest expenditure classes

The 12 largest of 43 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $138,283.33 | 21.9% |
| 4550 | Attorney General Legal Fees | $133,468.75 | 21.1% |
| 4800 | Facilities Rent | $84,584.40 | 13.4% |
| 4600 | State Government Service Charges | $60,964.35 | 9.6% |
| 4519 | Professional Serv/Managed Serv Provider | $26,100.00 | 4.1% |
| 4200 | Office Supplies | $24,842.55 | 3.9% |
| 4701 | Other Services | $23,180.57 | 3.7% |
| 4730 | Merchant Fees | $21,720.22 | 3.4% |
| 4375 | Computer Technology Computer Processing | $20,350.03 | 3.2% |
| 4975 | Agency Program Related Services | $18,108.25 | 2.9% |
| 4202 | Equipment Rental | $9,672.38 | 1.5% |
| 4305 | Telecom/Network Services | $7,318.13 | 1.2% |

## Curator notes

Figures are aggregated from 134 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='834' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


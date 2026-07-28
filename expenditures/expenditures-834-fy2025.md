---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-834-fy2025
title: Dentistry, Brd of — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 834, FY2025
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
  - expenditures-834-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-834
- dentistry-brd-of
agency_code: '834'
agency_name: DENTISTRY, BRD OF
fiscal_year: 2025
total_expense: '624972.04'
transaction_count: 70
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dentistry, Brd of — FY2025 expenditures

## At a glance

Dentistry, Brd of (agency code 834, recorded upstream as `DENTISTRY, BRD OF`) spent **$624,972.04** in fiscal year 2025, across 70 transaction records. That is down 9.8% from $692,709.74 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **65 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $183,759.54 (29.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $183,759.54 | 29.4% | 7 |
| 4650 | Other Services And Supplies | $109,477.00 | 17.5% | 5 |
| 4425 | Lease Payments & Taxes | $92,392.74 | 14.8% | 3 |
| 4325 | Attorney General Legal Fees | $75,117.40 | 12.0% | 2 |
| 4250 | Data Processing | $63,414.81 | 10.1% | 4 |
| 4225 | State Government Service Charges | $47,709.04 | 7.6% | 4 |
| 4575 | Agency Program Related Svcs & Supp | $18,308.36 | 2.9% | 2 |
| 4475 | Facilities Maintenance | $12,435.92 | 2.0% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $9,064.82 | 1.5% | 4 |
| 4100 | Instate Travel | $4,381.30 | 0.7% | 19 |
| 4150 | Employee Training | $3,801.12 | 0.6% | 9 |
| 4175 | Office Expenses | $2,890.99 | 0.5% | 5 |
| 4315 | It Professional Services | $1,196.00 | 0.2% | 1 |
| 4275 | Publicity & Publications | $648.00 | 0.1% | 2 |
| 4400 | Dues And Subscriptions | $375.00 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 30 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $183,759.54 | 29.4% |
| 4701 | Other Services | $79,711.61 | 12.8% |
| 4550 | Attorney General Legal Fees | $75,117.40 | 12.0% |
| 7007 | Lease Pmt For Buildings | $67,720.31 | 10.8% |
| 4375 | Computer Technology Computer Processing | $63,054.81 | 10.1% |
| 4600 | State Government Service Charges | $47,709.04 | 7.6% |
| 4730 | Merchant Fees | $29,765.39 | 4.8% |
| 7401 | Interest-Leased Assets | $24,672.43 | 3.9% |
| 4975 | Agency Program Related Services | $17,653.25 | 2.8% |
| 4850 | Facilities Maintenance | $12,435.92 | 2.0% |
| 4305 | Telecom/Network Services | $4,699.35 | 0.8% |
| 4301 | Telecom/Voice Usage | $4,365.47 | 0.7% |

## Curator notes

Figures are aggregated from 70 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='834' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-120-fy2025
title: Accountancy, Oregon Brd of — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 120, FY2025
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
  - expenditures-120-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-120
- accountancy-oregon-brd-of
agency_code: '120'
agency_name: ACCOUNTANCY, OREGON BRD OF
fiscal_year: 2025
total_expense: '513456.85'
transaction_count: 68
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Accountancy, Oregon Brd of — FY2025 expenditures

## At a glance

Accountancy, Oregon Brd of (agency code 120, recorded upstream as `ACCOUNTANCY, OREGON BRD OF`) spent **$513,456.85** in fiscal year 2025, across 68 transaction records. That is up 17.1% from $438,581.71 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **67 of 80** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $127,539.30 (24.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $127,539.30 | 24.8% | 1 |
| 4650 | Other Services And Supplies | $84,652.95 | 16.5% | 8 |
| 4425 | Lease Payments & Taxes | $69,047.92 | 13.4% | 2 |
| 4315 | It Professional Services | $56,160.75 | 10.9% | 3 |
| 4225 | State Government Service Charges | $51,273.05 | 10.0% | 4 |
| 4250 | Data Processing | $29,404.59 | 5.7% | 4 |
| 4175 | Office Expenses | $22,929.80 | 4.5% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $21,694.60 | 4.2% | 4 |
| 4300 | Professional Services | $20,360.05 | 4.0% | 5 |
| 4150 | Employee Training | $12,018.78 | 2.3% | 15 |
| 4475 | Facilities Maintenance | $5,966.39 | 1.2% | 2 |
| 4715 | It Expendable Property | $5,093.20 | 1.0% | 4 |
| 3240 | Unemployment Assessment | $4,121.85 | 0.8% | 1 |
| 4275 | Publicity & Publications | $1,893.89 | 0.4% | 2 |
| 4100 | Instate Travel | $979.12 | 0.2% | 7 |
| 4575 | Agency Program Related Svcs & Supp | $233.45 | 0.0% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $87.16 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 41 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $127,539.30 | 24.8% |
| 7007 | Lease Pmt For Buildings | $53,843.20 | 10.5% |
| 4701 | Other Services | $51,847.12 | 10.1% |
| 4600 | State Government Service Charges | $51,273.05 | 10.0% |
| 4515 | Professional Services Application Maint | $42,693.75 | 8.3% |
| 4730 | Merchant Fees | $22,556.97 | 4.4% |
| 4367 | Computer Technology Pc Support | $22,273.02 | 4.3% |
| 4500 | Professional Services Non-It | $20,360.05 | 4.0% |
| 4200 | Office Supplies | $16,037.18 | 3.1% |
| 7401 | Interest-Leased Assets | $15,204.72 | 3.0% |
| 4305 | Telecom/Network Services | $12,759.22 | 2.5% |
| 4720 | Collection Fees - Dor | $10,192.36 | 2.0% |

## Curator notes

Figures are aggregated from 68 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='120' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


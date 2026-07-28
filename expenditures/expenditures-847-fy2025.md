---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-847-fy2025
title: Medical Brd, OR — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 847, FY2025
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
  - expenditures-847-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-847
- medical-brd-or
agency_code: '847'
agency_name: MEDICAL BRD, OR
fiscal_year: 2025
total_expense: '2210201.35'
transaction_count: 139
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Medical Brd, OR — FY2025 expenditures

## At a glance

Medical Brd, OR (agency code 847, recorded upstream as `MEDICAL BRD, OR`) spent **$2,210,201.35** in fiscal year 2025, across 139 transaction records. That is down 28.4% from $3,087,966.36 in FY2024. The agency accounts for 0.01% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **53 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $701,630.14 (31.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $701,630.14 | 31.7% | 19 |
| 4325 | Attorney General Legal Fees | $448,014.55 | 20.3% | 1 |
| 4425 | Lease Payments & Taxes | $353,569.77 | 16.0% | 3 |
| 4225 | State Government Service Charges | $266,882.02 | 12.1% | 3 |
| 4575 | Agency Program Related Svcs & Supp | $156,446.30 | 7.1% | 5 |
| 4650 | Other Services And Supplies | $79,716.69 | 3.6% | 8 |
| 4175 | Office Expenses | $75,122.03 | 3.4% | 10 |
| 4400 | Dues And Subscriptions | $38,922.44 | 1.8% | 2 |
| 4150 | Employee Training | $30,818.42 | 1.4% | 47 |
| 4200 | Telecomm/Tech Svc And Supplies | $27,677.01 | 1.3% | 3 |
| 4100 | Instate Travel | $10,443.66 | 0.5% | 32 |
| 5550 | Data Processing Software | $7,197.39 | 0.3% | 1 |
| 4315 | It Professional Services | $5,924.57 | 0.3% | 1 |
| 4700 | Expendable Property $250-$5000 | $3,163.62 | 0.1% | 1 |
| 3240 | Unemployment Assessment | $2,444.00 | 0.1% | 1 |
| 4250 | Data Processing | $2,228.74 | 0.1% | 2 |

## Largest expenditure classes

The 12 largest of 45 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $576,630.14 | 26.1% |
| 4550 | Attorney General Legal Fees | $448,014.55 | 20.3% |
| 7007 | Lease Pmt For Buildings | $267,480.90 | 12.1% |
| 4600 | State Government Service Charges | $266,882.02 | 12.1% |
| 4975 | Agency Program Related Services | $155,851.25 | 7.1% |
| 4505 | Professional Services Non-It>$75K | $125,000.00 | 5.7% |
| 4730 | Merchant Fees | $75,967.96 | 3.4% |
| 4200 | Office Supplies | $62,584.07 | 2.8% |
| 7401 | Interest-Leased Assets | $44,089.92 | 2.0% |
| 4800 | Interagency Lease Payments | $41,998.95 | 1.9% |
| 4251 | Subscriptions And Publications | $38,922.44 | 1.8% |
| 4301 | Telecom/Voice Usage | $25,836.13 | 1.2% |

## Curator notes

Figures are aggregated from 139 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='847' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


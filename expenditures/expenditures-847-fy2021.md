---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-847-fy2021
title: Medical Brd, OR — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 847, FY2021
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
  - expenditures-847-fy2020
  - expenditures-847-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-847
- medical-brd-or
agency_code: '847'
agency_name: MEDICAL BRD, OR
fiscal_year: 2021
total_expense: '2141533.62'
transaction_count: 92
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Medical Brd, OR — FY2021 expenditures

## At a glance

Medical Brd, OR (agency code 847, recorded upstream as `MEDICAL BRD, OR`) spent **$2,141,533.62** in fiscal year 2021, across 92 transaction records. That is up 12.8% from $1,897,698.37 in FY2020. The agency accounts for 0.01% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **47 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $838,746.18 (39.2% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $838,746.18 | 39.2% | 25 |
| 4325 | Attorney General Legal Fees | $448,941.10 | 21.0% | 1 |
| 4425 | Lease Payments & Taxes | $327,491.92 | 15.3% | 1 |
| 4225 | State Government Service Charges | $147,511.76 | 6.9% | 3 |
| 4400 | Dues And Subscriptions | $87,067.91 | 4.1% | 2 |
| 4575 | Agency Program Related Svcs & Supp | $80,905.25 | 3.8% | 2 |
| 4175 | Office Expenses | $66,100.63 | 3.1% | 17 |
| 4650 | Other Services And Supplies | $43,902.14 | 2.1% | 7 |
| 4315 | It Professional Services | $43,274.98 | 2.0% | 6 |
| 4200 | Telecomm/Tech Svc And Supplies | $30,458.10 | 1.4% | 3 |
| 3240 | Unemployment Assessment | $8,169.77 | 0.4% | 1 |
| 4250 | Data Processing | $5,119.25 | 0.2% | 2 |
| 4100 | Instate Travel | $3,838.10 | 0.2% | 12 |
| 4700 | Expendable Property $250-$5000 | $3,811.00 | 0.2% | 2 |
| 4150 | Employee Training | $3,080.38 | 0.1% | 5 |
| 4375 | Employee Recruitment And Development | $1,560.00 | 0.1% | 1 |
| 4715 | It Expendable Property | $1,555.15 | 0.1% | 2 |

## Largest expenditure classes

The 12 largest of 33 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $588,746.18 | 27.5% |
| 4550 | Attorney General Legal Fees | $448,941.10 | 21.0% |
| 4800 | Interagency Lease Payments | $327,491.92 | 15.3% |
| 4505 | Professional Services Non-It>$75K | $250,000.00 | 11.7% |
| 4600 | State Government Service Charges | $147,511.76 | 6.9% |
| 4251 | Subscriptions And Publications | $87,067.91 | 4.1% |
| 4975 | Agency Program Related Services | $80,905.25 | 3.8% |
| 4200 | Office Supplies | $56,165.35 | 2.6% |
| 4730 | Merchant Fees | $35,913.16 | 1.7% |
| 4301 | Telecom/Voice Usage | $28,047.76 | 1.3% |
| 4513 | Professional Services Application New | $24,746.16 | 1.2% |
| 4517 | Professional Services It Security | $11,186.92 | 0.5% |

## Curator notes

Figures are aggregated from 92 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='847' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


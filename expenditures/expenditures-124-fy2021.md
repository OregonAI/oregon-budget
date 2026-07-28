---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-124-fy2021
title: Licensed Social Workers Brd — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 124, FY2021
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
  - expenditures-124-fy2020
  - expenditures-124-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-124
- licensed-social-workers-brd
agency_code: '124'
agency_name: LICENSED SOCIAL WORKERS BRD
fiscal_year: 2021
total_expense: '260830.39'
transaction_count: 35
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Licensed Social Workers Brd — FY2021 expenditures

## At a glance

Licensed Social Workers Brd (agency code 124, recorded upstream as `LICENSED SOCIAL WORKERS BRD`) spent **$260,830.39** in fiscal year 2021, across 35 transaction records. That is down 1.4% from $264,601.18 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **67 of 76** agencies reporting that year.

The largest budget category was **Lease Payments & Taxes** at $54,872.65 (21.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Lease Payments & Taxes | $54,872.65 | 21.0% | 2 |
| 4650 | Other Services And Supplies | $40,339.61 | 15.5% | 5 |
| 4575 | Agency Program Related Svcs & Supp | $36,321.00 | 13.9% | 1 |
| 4325 | Attorney General Legal Fees | $34,957.00 | 13.4% | 1 |
| 4225 | State Government Service Charges | $30,606.80 | 11.7% | 5 |
| 4250 | Data Processing | $18,306.32 | 7.0% | 3 |
| 4315 | It Professional Services | $14,600.00 | 5.6% | 2 |
| 4300 | Professional Services | $12,846.19 | 4.9% | 2 |
| 4715 | It Expendable Property | $9,755.48 | 3.7% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $4,193.77 | 1.6% | 3 |
| 4175 | Office Expenses | $3,173.50 | 1.2% | 3 |
| 4275 | Publicity & Publications | $545.00 | 0.2% | 1 |
| 4100 | Instate Travel | $313.07 | 0.1% | 3 |

## Largest expenditure classes

The 12 largest of 20 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Facilities Rent | $54,872.65 | 21.0% |
| 4975 | Agency Program Related Services | $36,321.00 | 13.9% |
| 4550 | Attorney General Legal Fees | $34,957.00 | 13.4% |
| 4600 | State Government Service Charges | $30,606.80 | 11.7% |
| 4701 | Other Services | $25,588.04 | 9.8% |
| 4375 | Computer Technology Computer Processing | $17,718.96 | 6.8% |
| 4730 | Merchant Fees | $14,751.57 | 5.7% |
| 4500 | Professional Services Non-It | $12,846.19 | 4.9% |
| 4519 | Professional Serv/Managed Serv Provider | $8,900.00 | 3.4% |
| 4365 | Computer Technology Pc Equipment<$5K | $8,465.66 | 3.2% |
| 4515 | Professional Services Application Maint | $5,700.00 | 2.2% |
| 4301 | Telecom/Voice Usage | $2,537.05 | 1.0% |

## Curator notes

Figures are aggregated from 35 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='124' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


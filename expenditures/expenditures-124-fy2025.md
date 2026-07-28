---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-124-fy2025
title: Licensed Social Workers Brd — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 124, FY2025
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
  - expenditures-124-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-124
- licensed-social-workers-brd
agency_code: '124'
agency_name: LICENSED SOCIAL WORKERS BRD
fiscal_year: 2025
total_expense: '361804.92'
transaction_count: 39
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Licensed Social Workers Brd — FY2025 expenditures

## At a glance

Licensed Social Workers Brd (agency code 124, recorded upstream as `LICENSED SOCIAL WORKERS BRD`) spent **$361,804.92** in fiscal year 2025, across 39 transaction records. That is up 7.3% from $337,260.86 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **70 of 80** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $74,097.29 (20.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $74,097.29 | 20.5% | 4 |
| 4325 | Attorney General Legal Fees | $63,676.85 | 17.6% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $63,611.75 | 17.6% | 2 |
| 4425 | Lease Payments & Taxes | $54,786.78 | 15.1% | 1 |
| 4225 | State Government Service Charges | $44,145.27 | 12.2% | 4 |
| 4250 | Data Processing | $26,030.90 | 7.2% | 4 |
| 4315 | It Professional Services | $15,926.00 | 4.4% | 2 |
| 4715 | It Expendable Property | $4,643.36 | 1.3% | 4 |
| 4275 | Publicity & Publications | $4,579.74 | 1.3% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $4,516.01 | 1.2% | 4 |
| 4175 | Office Expenses | $3,347.50 | 0.9% | 2 |
| 4100 | Instate Travel | $2,148.27 | 0.6% | 7 |
| 4300 | Professional Services | $295.20 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 22 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $63,676.85 | 17.6% |
| 4975 | Agency Program Related Services | $63,611.75 | 17.6% |
| 4800 | Interagency Lease Payments | $54,786.78 | 15.1% |
| 4701 | Other Services | $51,910.49 | 14.3% |
| 4600 | State Government Service Charges | $44,145.27 | 12.2% |
| 4730 | Merchant Fees | $22,186.80 | 6.1% |
| 4367 | Computer Technology Pc Support | $19,650.01 | 5.4% |
| 4515 | Professional Services Application Maint | $15,375.00 | 4.2% |
| 4375 | Computer Technology Computer Processing | $6,380.89 | 1.8% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $4,579.74 | 1.3% |
| 4365 | Computer Technology Pc Equipment<$5K | $4,259.04 | 1.2% |
| 4301 | Telecom/Voice Usage | $3,291.51 | 0.9% |

## Curator notes

Figures are aggregated from 39 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='124' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


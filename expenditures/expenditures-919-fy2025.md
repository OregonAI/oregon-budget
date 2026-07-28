---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-919-fy2025
title: Real Estate Agy — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 919, FY2025
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
  - expenditures-919-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-919
- real-estate-agy
agency_code: '919'
agency_name: REAL ESTATE AGY
fiscal_year: 2025
total_expense: '1345997.15'
transaction_count: 107
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Real Estate Agy — FY2025 expenditures

## At a glance

Real Estate Agy (agency code 919, recorded upstream as `REAL ESTATE AGY`) spent **$1,345,997.15** in fiscal year 2025, across 107 transaction records. That is up 36.8% from $984,111.22 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **59 of 80** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $370,914.61 (27.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $370,914.61 | 27.6% | 4 |
| 4225 | State Government Service Charges | $227,312.99 | 16.9% | 5 |
| 4315 | It Professional Services | $181,079.00 | 13.5% | 1 |
| 4425 | Lease Payments & Taxes | $130,787.60 | 9.7% | 3 |
| 4325 | Attorney General Legal Fees | $91,369.06 | 6.8% | 1 |
| 4650 | Other Services And Supplies | $88,611.09 | 6.6% | 5 |
| 4250 | Data Processing | $55,771.41 | 4.1% | 4 |
| 4715 | It Expendable Property | $49,818.89 | 3.7% | 8 |
| 4150 | Employee Training | $37,543.15 | 2.8% | 9 |
| 4200 | Telecomm/Tech Svc And Supplies | $33,324.57 | 2.5% | 3 |
| 4300 | Professional Services | $32,539.50 | 2.4% | 3 |
| 4400 | Dues And Subscriptions | $13,197.00 | 1.0% | 2 |
| 4700 | Expendable Property $250-$5000 | $10,361.45 | 0.8% | 2 |
| 4125 | Out-Of-State Travel | $8,848.39 | 0.7% | 25 |
| 5100 | Office Furniture And Fixtures | $6,734.96 | 0.5% | 1 |
| 4100 | Instate Travel | $3,821.05 | 0.3% | 25 |
| 4175 | Office Expenses | $3,759.09 | 0.3% | 4 |
| 5550 | Data Processing Software | $160.74 | 0.0% | 1 |
| 4275 | Publicity & Publications | $42.60 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 44 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $370,914.61 | 27.6% |
| 4600 | State Government Service Charges | $227,312.99 | 16.9% |
| 4515 | Professional Services Application Maint | $181,079.00 | 13.5% |
| 7007 | Lease Pmt For Buildings | $122,504.14 | 9.1% |
| 4550 | Attorney General Legal Fees | $91,369.06 | 6.8% |
| 4730 | Merchant Fees | $79,455.57 | 5.9% |
| 4375 | Computer Technology Computer Processing | $55,771.41 | 4.1% |
| 4500 | Professional Services Non-It | $32,539.50 | 2.4% |
| 4301 | Telecom/Voice Usage | $29,982.81 | 2.2% |
| 4372 | Computer Technology Peripheral Equip<$5K | $17,629.77 | 1.3% |
| 4366 | Computer Technology Pc Software<$5K | $16,223.63 | 1.2% |
| 4406 | Prof Dev Instate Tuition/Registration | $12,557.00 | 0.9% |

## Curator notes

Figures are aggregated from 107 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='919' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


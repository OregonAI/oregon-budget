---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-855-fy2025
title: Pharmacy, Oregon Brd of — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 855, FY2025
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
  - expenditures-855-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-855
- pharmacy-oregon-brd-of
agency_code: '855'
agency_name: PHARMACY, OREGON BRD OF
fiscal_year: 2025
total_expense: '1433212.01'
transaction_count: 109
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Pharmacy, Oregon Brd of — FY2025 expenditures

## At a glance

Pharmacy, Oregon Brd of (agency code 855, recorded upstream as `PHARMACY, OREGON BRD OF`) spent **$1,433,212.01** in fiscal year 2025, across 109 transaction records. That is up 6.3% from $1,347,905.20 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **58 of 80** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $322,615.23 (22.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $322,615.23 | 22.5% | 5 |
| 4325 | Attorney General Legal Fees | $265,011.17 | 18.5% | 1 |
| 4250 | Data Processing | $247,069.78 | 17.2% | 4 |
| 4425 | Lease Payments & Taxes | $173,804.54 | 12.1% | 1 |
| 4225 | State Government Service Charges | $144,507.80 | 10.1% | 4 |
| 4575 | Agency Program Related Svcs & Supp | $103,919.25 | 7.3% | 2 |
| 4300 | Professional Services | $61,775.65 | 4.3% | 8 |
| 4175 | Office Expenses | $55,595.57 | 3.9% | 5 |
| 4100 | Instate Travel | $29,375.34 | 2.0% | 52 |
| 4275 | Publicity & Publications | $14,551.59 | 1.0% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $5,960.08 | 0.4% | 3 |
| 4150 | Employee Training | $4,334.41 | 0.3% | 11 |
| 4315 | It Professional Services | $3,600.00 | 0.3% | 1 |
| 4125 | Out-Of-State Travel | $520.80 | 0.0% | 6 |
| 4400 | Dues And Subscriptions | $295.00 | 0.0% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $275.80 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 30 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $265,011.17 | 18.5% |
| 4375 | Computer Technology Computer Processing | $247,069.78 | 17.2% |
| 4701 | Other Services | $224,647.73 | 15.7% |
| 4800 | Interagency Lease Payments | $173,804.54 | 12.1% |
| 4600 | State Government Service Charges | $144,507.80 | 10.1% |
| 4975 | Agency Program Related Services | $103,919.25 | 7.3% |
| 4730 | Merchant Fees | $96,967.60 | 6.8% |
| 4500 | Professional Services Non-It | $61,775.65 | 4.3% |
| 4201 | Office Services | $36,362.62 | 2.5% |
| 4200 | Office Supplies | $19,232.95 | 1.3% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $14,551.59 | 1.0% |
| 4108 | Instate Ground Transportation | $13,191.57 | 0.9% |

## Curator notes

Figures are aggregated from 109 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='855' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


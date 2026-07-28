---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-915-fy2025
title: Construction Ctr Brd — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 915, FY2025
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
  - expenditures-915-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-915
- construction-ctr-brd
agency_code: '915'
agency_name: CONSTRUCTION CTR BRD
fiscal_year: 2025
total_expense: '1854670.88'
transaction_count: 81
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Construction Ctr Brd — FY2025 expenditures

## At a glance

Construction Ctr Brd (agency code 915, recorded upstream as `CONSTRUCTION CTR BRD`) spent **$1,854,670.88** in fiscal year 2025, across 81 transaction records. That is up 10.2% from $1,683,009.91 in FY2024. The agency accounts for 0.01% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **55 of 80** agencies reporting that year.

The largest budget category was **Lease Payments & Taxes** at $444,082.32 (23.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Lease Payments & Taxes | $444,082.32 | 23.9% | 4 |
| 4650 | Other Services And Supplies | $379,372.60 | 20.5% | 10 |
| 4225 | State Government Service Charges | $299,996.52 | 16.2% | 5 |
| 4175 | Office Expenses | $186,634.81 | 10.1% | 8 |
| 4325 | Attorney General Legal Fees | $152,035.22 | 8.2% | 1 |
| 4100 | Instate Travel | $106,403.92 | 5.7% | 23 |
| 4700 | Expendable Property $250-$5000 | $81,911.24 | 4.4% | 1 |
| 4250 | Data Processing | $71,578.49 | 3.9% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $45,301.53 | 2.4% | 3 |
| 4275 | Publicity & Publications | $31,493.40 | 1.7% | 3 |
| 4300 | Professional Services | $28,714.89 | 1.5% | 3 |
| 4315 | It Professional Services | $12,896.93 | 0.7% | 4 |
| 3220 | Public Employes' Retirement System | $6,935.78 | 0.4% | 1 |
| 4150 | Employee Training | $3,910.06 | 0.2% | 4 |
| 4475 | Facilities Maintenance | $2,432.26 | 0.1% | 3 |
| 4125 | Out-Of-State Travel | $642.96 | 0.0% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $216.78 | 0.0% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $111.17 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 34 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 7007 | Lease Pmt For Buildings | $392,115.48 | 21.1% |
| 4600 | State Government Service Charges | $299,996.52 | 16.2% |
| 4730 | Merchant Fees | $174,600.18 | 9.4% |
| 4201 | Office Services | $165,658.52 | 8.9% |
| 4701 | Other Services | $157,724.14 | 8.5% |
| 4550 | Attorney General Legal Fees | $152,035.22 | 8.2% |
| 4108 | Instate Ground Transportation | $91,453.93 | 4.9% |
| 4999 | Expendable Property Non-It<$5K | $81,911.24 | 4.4% |
| 4375 | Computer Technology Computer Processing | $71,578.49 | 3.9% |
| 4720 | Collection Fees - Dor | $46,766.28 | 2.5% |
| 4800 | Interagency Lease Payments | $46,624.65 | 2.5% |
| 4301 | Telecom/Voice Usage | $39,396.96 | 2.1% |

## Curator notes

Figures are aggregated from 81 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='915' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


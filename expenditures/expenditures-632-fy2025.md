---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-632-fy2025
title: Geology & Mineral Ind, Dept of — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 632, FY2025
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
  - expenditures-632-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-632
- geology-mineral-ind-dept-of
agency_code: '632'
agency_name: GEOLOGY & MINERAL IND, DEPT OF
fiscal_year: 2025
total_expense: '3474629.27'
transaction_count: 248
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Geology & Mineral Ind, Dept of — FY2025 expenditures

## At a glance

Geology & Mineral Ind, Dept of (agency code 632, recorded upstream as `GEOLOGY & MINERAL IND, DEPT OF`) spent **$3,474,629.27** in fiscal year 2025, across 248 transaction records. That is down 37.0% from $5,513,798.83 in FY2024. The agency accounts for 0.01% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **48 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $1,552,898.34 (44.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $1,552,898.34 | 44.7% | 23 |
| 4250 | Data Processing | $316,949.18 | 9.1% | 7 |
| 4425 | Lease Payments & Taxes | $297,615.60 | 8.6% | 3 |
| 4715 | It Expendable Property | $267,364.81 | 7.7% | 5 |
| 4225 | State Government Service Charges | $260,193.52 | 7.5% | 4 |
| 4650 | Other Services And Supplies | $195,570.48 | 5.6% | 6 |
| 5200 | Technical Equipment | $191,663.52 | 5.5% | 1 |
| 4325 | Attorney General Legal Fees | $137,279.30 | 4.0% | 1 |
| 4100 | Instate Travel | $86,615.45 | 2.5% | 67 |
| 4150 | Employee Training | $44,630.47 | 1.3% | 79 |
| 4575 | Agency Program Related Svcs & Supp | $36,671.00 | 1.1% | 2 |
| 4125 | Out-Of-State Travel | $30,112.44 | 0.9% | 21 |
| 4200 | Telecomm/Tech Svc And Supplies | $16,320.67 | 0.5% | 4 |
| 3110 | Class/Unclass Salary & Per Diem | $13,078.83 | 0.4% | 1 |
| 4475 | Facilities Maintenance | $9,541.30 | 0.3% | 2 |
| 4175 | Office Expenses | $8,898.32 | 0.3% | 14 |
| 5900 | Other Capital Outlay | $6,717.50 | 0.2% | 1 |
| 4275 | Publicity & Publications | $1,928.54 | 0.1% | 4 |
| 4400 | Dues And Subscriptions | $580.00 | 0.0% | 3 |

## Largest expenditure classes

The 12 largest of 56 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $1,552,898.34 | 44.7% |
| 4800 | Interagency Lease Payments | $262,389.60 | 7.6% |
| 4600 | State Government Service Charges | $260,193.52 | 7.5% |
| 4375 | Computer Technology Computer Processing | $236,239.10 | 6.8% |
| 4701 | Other Services | $195,346.01 | 5.6% |
| 5250 | Technical Equipment>=$5K | $191,663.52 | 5.5% |
| 4361 | Computer Technology Server Software<$5K | $159,996.26 | 4.6% |
| 4550 | Attorney General Legal Fees | $137,279.30 | 4.0% |
| 4365 | Computer Technology Pc Equipment<$5K | $93,146.91 | 2.7% |
| 4362 | Computer Technology Server Support | $79,560.99 | 2.3% |
| 4108 | Instate Ground Transportation | $62,761.52 | 1.8% |
| 4976 | Agency Program Related Supplies | $36,671.00 | 1.1% |

## Curator notes

Figures are aggregated from 248 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='632' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


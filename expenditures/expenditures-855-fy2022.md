---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-855-fy2022
title: Pharmacy, Oregon Brd of — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 855, FY2022
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5378b32aad5d54d03160dd49832cc5c4f45e517dde8ba96c7e5b8bbb6e3a99f4
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
  - expenditures-855-fy2021
  - expenditures-855-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-855
- pharmacy-oregon-brd-of
agency_code: '855'
agency_name: PHARMACY, OREGON BRD OF
fiscal_year: 2022
total_expense: '1224483.76'
transaction_count: 65
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Pharmacy, Oregon Brd of — FY2022 expenditures

## At a glance

Pharmacy, Oregon Brd of (agency code 855, recorded upstream as `PHARMACY, OREGON BRD OF`) spent **$1,224,483.76** in fiscal year 2022, across 65 transaction records. That is up 18.6% from $1,032,164.21 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **54 of 76** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $255,918.28 (20.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $255,918.28 | 20.9% | 1 |
| 4650 | Other Services And Supplies | $199,019.16 | 16.3% | 5 |
| 4250 | Data Processing | $161,473.88 | 13.2% | 5 |
| 4300 | Professional Services | $140,295.60 | 11.5% | 10 |
| 4425 | Lease Payments & Taxes | $137,415.33 | 11.2% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $128,227.50 | 10.5% | 3 |
| 4225 | State Government Service Charges | $105,480.20 | 8.6% | 4 |
| 4175 | Office Expenses | $41,943.66 | 3.4% | 4 |
| 4315 | It Professional Services | $13,850.00 | 1.1% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $13,495.69 | 1.1% | 5 |
| 4100 | Instate Travel | $9,860.80 | 0.8% | 10 |
| 4275 | Publicity & Publications | $7,717.85 | 0.6% | 4 |
| 4475 | Facilities Maintenance | $4,117.13 | 0.3% | 2 |
| 4150 | Employee Training | $1,960.77 | 0.2% | 4 |
| 3110 | Class/Unclass Salary & Per Diem | $1,511.56 | 0.1% | 1 |
| 4700 | Expendable Property $250-$5000 | $1,195.69 | 0.1% | 1 |
| 3240 | Unemployment Assessment | $745.96 | 0.1% | 1 |
| 4125 | Out-Of-State Travel | $254.70 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 31 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $255,918.28 | 20.9% |
| 4375 | Computer Technology Computer Processing | $161,221.88 | 13.2% |
| 4500 | Professional Services Non-It | $140,295.60 | 11.5% |
| 4800 | Interagency Lease Payments | $137,415.33 | 11.2% |
| 4975 | Agency Program Related Services | $128,227.50 | 10.5% |
| 4701 | Other Services | $117,675.08 | 9.6% |
| 4600 | State Government Service Charges | $105,480.20 | 8.6% |
| 4730 | Merchant Fees | $79,551.35 | 6.5% |
| 4200 | Office Supplies | $21,114.20 | 1.7% |
| 4201 | Office Services | $20,829.46 | 1.7% |
| 4513 | Professional Services Application New | $13,000.00 | 1.1% |
| 4301 | Telecom/Voice Usage | $9,930.34 | 0.8% |

## Curator notes

Figures are aggregated from 65 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='855' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


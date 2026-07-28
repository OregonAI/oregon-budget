---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-811-fy2023
title: Chiropractic Exam, Brd of — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 811, FY2023
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 6400163010ab2f341831c864272a89c5e9f2a261fad3fd9572b230042f26e3d5
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
  - expenditures-811-fy2022
  - expenditures-811-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-811
- chiropractic-exam-brd-of
agency_code: '811'
agency_name: CHIROPRACTIC EXAM, BRD OF
fiscal_year: 2023
total_expense: '344580.76'
transaction_count: 104
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Chiropractic Exam, Brd of — FY2023 expenditures

## At a glance

Chiropractic Exam, Brd of (agency code 811, recorded upstream as `CHIROPRACTIC EXAM, BRD OF`) spent **$344,580.76** in fiscal year 2023, across 104 transaction records. That is down 8.8% from $377,797.94 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **68 of 77** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $89,627.67 (26.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | $89,627.67 | 26.0% | 3 |
| 4325 | Attorney General Legal Fees | $78,819.96 | 22.9% | 1 |
| 4425 | Lease Payments & Taxes | $49,353.91 | 14.3% | 3 |
| 4225 | State Government Service Charges | $28,743.68 | 8.3% | 6 |
| 4315 | It Professional Services | $24,487.75 | 7.1% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $23,256.00 | 6.7% | 1 |
| 4100 | Instate Travel | $13,528.66 | 3.9% | 39 |
| 4125 | Out-Of-State Travel | $7,407.47 | 2.1% | 10 |
| 4300 | Professional Services | $6,666.99 | 1.9% | 8 |
| 4200 | Telecomm/Tech Svc And Supplies | $5,331.43 | 1.5% | 3 |
| 4150 | Employee Training | $5,246.68 | 1.5% | 15 |
| 4250 | Data Processing | $4,364.53 | 1.3% | 3 |
| 4175 | Office Expenses | $2,797.82 | 0.8% | 3 |
| 4400 | Dues And Subscriptions | $2,625.00 | 0.8% | 2 |
| 4275 | Publicity & Publications | $2,306.22 | 0.7% | 5 |
| 4715 | It Expendable Property | $16.99 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 30 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $78,819.96 | 22.9% |
| 4701 | Other Services | $73,090.38 | 21.2% |
| 4800 | Interagency Lease Payments | $49,353.91 | 14.3% |
| 4600 | State Government Service Charges | $28,743.68 | 8.3% |
| 4516 | Professional Services Servers | $24,487.75 | 7.1% |
| 4975 | Agency Program Related Services | $23,256.00 | 6.7% |
| 4730 | Merchant Fees | $16,537.29 | 4.8% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $7,064.42 | 2.1% |
| 4159 | Out-Of-State Air Transportation | $6,802.60 | 2.0% |
| 4500 | Professional Services Non-It | $6,666.99 | 1.9% |
| 4101 | Instate Meals With Overnight Stay | $4,668.50 | 1.4% |
| 4375 | Computer Technology Computer Processing | $4,364.53 | 1.3% |

## Curator notes

Figures are aggregated from 104 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='811' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


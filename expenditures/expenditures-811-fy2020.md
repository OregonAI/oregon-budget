---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-811-fy2020
title: Chiropractic Exam, Brd of — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 811, FY2020
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: b73d59a16a10ad7f6ae4f4b415cba8d78894a3ead0e3928fe994cc49b9b11284
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
  - expenditures-811-fy2019
  - expenditures-811-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-811
- chiropractic-exam-brd-of
agency_code: '811'
agency_name: CHIROPRACTIC EXAM, BRD OF
fiscal_year: 2020
total_expense: '311299.02'
transaction_count: 87
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Chiropractic Exam, Brd of — FY2020 expenditures

## At a glance

Chiropractic Exam, Brd of (agency code 811, recorded upstream as `CHIROPRACTIC EXAM, BRD OF`) spent **$311,299.02** in fiscal year 2020, across 87 transaction records. That is down 11.8% from $353,042.84 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **64 of 77** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $99,907.55 (32.1% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $99,907.55 | 32.1% | 1 |
| 4425 | Facilities Rent & Taxes | $55,157.87 | 17.7% | 2 |
| 4650 | Other Services And Supplies | $51,050.96 | 16.4% | 5 |
| 4225 | State Government Service Charges | $30,945.19 | 9.9% | 5 |
| 4575 | Agency Program Related Svcs & Supp | $23,377.14 | 7.5% | 4 |
| 4300 | Professional Services | $12,746.93 | 4.1% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $10,376.85 | 3.3% | 4 |
| 4250 | Data Processing | $10,266.81 | 3.3% | 2 |
| 4100 | Instate Travel | $7,017.49 | 2.3% | 40 |
| 4175 | Office Expenses | $4,325.86 | 1.4% | 4 |
| 4400 | Dues And Subscriptions | $2,355.00 | 0.8% | 2 |
| 4275 | Publicity & Publications | $1,494.95 | 0.5% | 2 |
| 4125 | Out-Of-State Travel | $1,322.61 | 0.4% | 4 |
| 4150 | Employee Training | $923.83 | 0.3% | 7 |
| 4715 | It Expendable Property | $29.98 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 34 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $99,907.55 | 32.1% |
| 4800 | Facilities Rent | $55,157.87 | 17.7% |
| 4701 | Other Services | $36,480.76 | 11.7% |
| 4600 | State Government Service Charges | $30,945.19 | 9.9% |
| 4975 | Agency Program Related Services | $23,132.75 | 7.4% |
| 4730 | Merchant Fees | $14,348.96 | 4.6% |
| 4500 | Professional Services Non-It | $12,746.93 | 4.1% |
| 4375 | Computer Technology Computer Processing | $10,266.81 | 3.3% |
| 4305 | Telecom/Network Services | $7,557.71 | 2.4% |
| 4201 | Office Services | $4,198.95 | 1.3% |
| 4301 | Telecom/Voice Usage | $2,819.14 | 0.9% |
| 4111 | Instate Mileage Reimbursmnt-Volunteers | $2,666.93 | 0.9% |

## Curator notes

Figures are aggregated from 87 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='811' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


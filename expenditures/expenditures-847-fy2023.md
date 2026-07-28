---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-847-fy2023
title: Medical Brd, OR — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 847, FY2023
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
  - expenditures-847-fy2022
  - expenditures-847-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-847
- medical-brd-or
agency_code: '847'
agency_name: MEDICAL BRD, OR
fiscal_year: 2023
total_expense: '2559012.31'
transaction_count: 169
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Medical Brd, OR — FY2023 expenditures

## At a glance

Medical Brd, OR (agency code 847, recorded upstream as `MEDICAL BRD, OR`) spent **$2,559,012.31** in fiscal year 2023, across 169 transaction records. That is up 23.0% from $2,081,140.32 in FY2022. The agency accounts for 0.01% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **48 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $714,528.66 (27.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $714,528.66 | 27.9% | 24 |
| 4325 | Attorney General Legal Fees | $490,018.64 | 19.1% | 2 |
| 4425 | Lease Payments & Taxes | $345,615.29 | 13.5% | 3 |
| 4400 | Dues And Subscriptions | $219,831.63 | 8.6% | 3 |
| 4650 | Other Services And Supplies | $169,282.48 | 6.6% | 10 |
| 4225 | State Government Service Charges | $167,358.62 | 6.5% | 3 |
| 4315 | It Professional Services | $164,072.78 | 6.4% | 5 |
| 4575 | Agency Program Related Svcs & Supp | $129,149.25 | 5.0% | 2 |
| 4175 | Office Expenses | $74,135.85 | 2.9% | 18 |
| 4200 | Telecomm/Tech Svc And Supplies | $26,074.77 | 1.0% | 2 |
| 5150 | Telecommunications | $21,880.70 | 0.9% | 2 |
| 4100 | Instate Travel | $10,431.47 | 0.4% | 57 |
| 4150 | Employee Training | $9,291.43 | 0.4% | 27 |
| 4250 | Data Processing | $5,590.90 | 0.2% | 3 |
| 4700 | Expendable Property $250-$5000 | $4,576.40 | 0.2% | 1 |
| 3220 | Public Employes' Retirement System | $4,053.52 | 0.2% | 1 |
| 4715 | It Expendable Property | $1,823.89 | 0.1% | 4 |
| 3110 | Class/Unclass Salary & Per Diem | $718.73 | 0.0% | 1 |
| 5900 | Other Capital Outlay | $577.30 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 48 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $544,528.66 | 21.3% |
| 4550 | Attorney General Legal Fees | $490,018.64 | 19.1% |
| 7007 | Lease Pmt For Buildings | $255,092.18 | 10.0% |
| 4251 | Subscriptions And Publications | $219,831.63 | 8.6% |
| 4505 | Professional Services Non-It>$75K | $170,000.00 | 6.6% |
| 4600 | State Government Service Charges | $167,358.62 | 6.5% |
| 4513 | Professional Services Application New | $132,500.00 | 5.2% |
| 4975 | Agency Program Related Services | $129,149.25 | 5.0% |
| 4701 | Other Services | $115,339.71 | 4.5% |
| 7401 | Interest-Leased Assets | $64,769.91 | 2.5% |
| 4200 | Office Supplies | $61,160.00 | 2.4% |
| 4730 | Merchant Fees | $51,612.01 | 2.0% |

## Curator notes

Figures are aggregated from 169 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='847' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


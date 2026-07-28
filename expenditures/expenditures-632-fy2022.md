---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-632-fy2022
title: Geology & Mineral Ind, Dept of — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 632, FY2022
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
  - expenditures-632-fy2021
  - expenditures-632-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-632
- geology-mineral-ind-dept-of
agency_code: '632'
agency_name: GEOLOGY & MINERAL IND, DEPT OF
fiscal_year: 2022
total_expense: '2778677.23'
transaction_count: 109
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Geology & Mineral Ind, Dept of — FY2022 expenditures

## At a glance

Geology & Mineral Ind, Dept of (agency code 632, recorded upstream as `GEOLOGY & MINERAL IND, DEPT OF`) spent **$2,778,677.23** in fiscal year 2022, across 109 transaction records. That is down 21.4% from $3,535,953.79 in FY2021. The agency accounts for 0.01% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **45 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $1,419,506.44 (51.1% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $1,419,506.44 | 51.1% | 13 |
| 4425 | Lease Payments & Taxes | $266,034.05 | 9.6% | 3 |
| 4250 | Data Processing | $231,325.29 | 8.3% | 2 |
| 4650 | Other Services And Supplies | $225,668.62 | 8.1% | 3 |
| 4225 | State Government Service Charges | $182,208.80 | 6.6% | 4 |
| 4715 | It Expendable Property | $99,837.00 | 3.6% | 4 |
| 4325 | Attorney General Legal Fees | $56,353.68 | 2.0% | 1 |
| 4315 | It Professional Services | $56,317.50 | 2.0% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $45,053.39 | 1.6% | 8 |
| 5900 | Other Capital Outlay | $45,000.00 | 1.6% | 1 |
| 4100 | Instate Travel | $40,768.89 | 1.5% | 32 |
| 5400 | Automotive & Aircraft | $33,900.00 | 1.2% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $24,667.80 | 0.9% | 2 |
| 4175 | Office Expenses | $14,027.44 | 0.5% | 12 |
| 4275 | Publicity & Publications | $13,023.38 | 0.5% | 3 |
| 4700 | Expendable Property $250-$5000 | $9,917.73 | 0.4% | 4 |
| 4475 | Facilities Maintenance | $5,435.30 | 0.2% | 2 |
| 4150 | Employee Training | $4,969.02 | 0.2% | 5 |
| 3110 | Class/Unclass Salary & Per Diem | $1,737.05 | 0.1% | 1 |
| 4400 | Dues And Subscriptions | $1,620.00 | 0.1% | 3 |
| 4450 | Fuels And Utilities | $1,305.85 | 0.0% | 4 |

## Largest expenditure classes

The 12 largest of 37 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $1,419,506.44 | 51.1% |
| 4800 | Interagency Lease Payments | $266,034.05 | 9.6% |
| 4701 | Other Services | $225,633.63 | 8.1% |
| 4375 | Computer Technology Computer Processing | $187,979.72 | 6.8% |
| 4600 | State Government Service Charges | $182,208.80 | 6.6% |
| 4361 | Computer Technology Server Software<$5K | $95,283.36 | 3.4% |
| 4550 | Attorney General Legal Fees | $56,353.68 | 2.0% |
| 4513 | Professional Services Application New | $56,317.50 | 2.0% |
| 5150 | Equipment And Machinery>=$5K | $45,000.00 | 1.6% |
| 4362 | Computer Technology Server Support | $43,345.57 | 1.6% |
| 5170 | Motor Vehicles>=$5K | $33,900.00 | 1.2% |
| 4108 | Instate Ground Transportation | $33,169.35 | 1.2% |

## Curator notes

Figures are aggregated from 109 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='632' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


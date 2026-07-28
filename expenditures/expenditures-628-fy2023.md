---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-628-fy2023
title: Forest Resources Inst, OR — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 628, FY2023
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
  - expenditures-628-fy2022
  - expenditures-628-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-628
- forest-resources-inst-or
agency_code: '628'
agency_name: FOREST RESOURCES INST, OR
fiscal_year: 2023
total_expense: '2685920.74'
transaction_count: 184
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Forest Resources Inst, OR — FY2023 expenditures

## At a glance

Forest Resources Inst, OR (agency code 628, recorded upstream as `FOREST RESOURCES INST, OR`) spent **$2,685,920.74** in fiscal year 2023, across 184 transaction records. That is up 2.3% from $2,626,086.52 in FY2022. The agency accounts for 0.01% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **47 of 77** agencies reporting that year.

The largest budget category was **Publicity & Publications** at $1,147,431.43 (42.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4275 | Publicity & Publications | $1,147,431.43 | 42.7% | 11 |
| 4300 | Professional Services | $1,058,142.28 | 39.4% | 25 |
| 4575 | Agency Program Related Svcs & Supp | $160,705.13 | 6.0% | 65 |
| 4425 | Lease Payments & Taxes | $119,663.34 | 4.5% | 7 |
| 4315 | It Professional Services | $72,628.45 | 2.7% | 2 |
| 4100 | Instate Travel | $37,198.69 | 1.4% | 40 |
| 4175 | Office Expenses | $25,124.18 | 0.9% | 8 |
| 4715 | It Expendable Property | $17,410.95 | 0.6% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $17,021.11 | 0.6% | 3 |
| 4325 | Attorney General Legal Fees | $9,244.40 | 0.3% | 1 |
| 4225 | State Government Service Charges | $5,515.33 | 0.2% | 3 |
| 4150 | Employee Training | $5,000.00 | 0.2% | 1 |
| 4400 | Dues And Subscriptions | $4,478.28 | 0.2% | 2 |
| 4125 | Out-Of-State Travel | $4,301.63 | 0.2% | 10 |
| 4375 | Employee Recruitment And Development | $1,130.80 | 0.0% | 1 |
| 4650 | Other Services And Supplies | $618.47 | 0.0% | 1 |
| 4250 | Data Processing | $306.27 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 34 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4253 | Advertise, Publicity, Publish/Print Srvs | $1,147,431.43 | 42.7% |
| 4505 | Professional Services Non-It>$75K | $866,754.97 | 32.3% |
| 4500 | Professional Services Non-It | $191,387.31 | 7.1% |
| 4975 | Agency Program Related Services | $130,834.68 | 4.9% |
| 4800 | Interagency Lease Payments | $119,663.34 | 4.5% |
| 4516 | Professional Services Servers | $72,628.45 | 2.7% |
| 4206 | Catering Services | $23,779.05 | 0.9% |
| 4108 | Instate Ground Transportation | $11,473.42 | 0.4% |
| 4106 | Instate Lodging | $10,411.98 | 0.4% |
| 4365 | Computer Technology Pc Equipment<$5K | $9,845.24 | 0.4% |
| 4201 | Office Services | $9,456.89 | 0.4% |
| 4550 | Attorney General Legal Fees | $9,244.40 | 0.3% |

## Curator notes

Figures are aggregated from 184 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='628' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


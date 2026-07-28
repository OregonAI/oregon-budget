---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-662-fy2022
title: Land Use Brd of Appeals — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 662, FY2022
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
  - expenditures-662-fy2021
  - expenditures-662-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-662
- land-use-brd-of-appeals
agency_code: '662'
agency_name: LAND USE BRD OF APPEALS
fiscal_year: 2022
total_expense: '220585.01'
transaction_count: 53
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Land Use Brd of Appeals — FY2022 expenditures

## At a glance

Land Use Brd of Appeals (agency code 662, recorded upstream as `LAND USE BRD OF APPEALS`) spent **$220,585.01** in fiscal year 2022, across 53 transaction records. That is up 30.4% from $169,112.83 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **71 of 76** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $69,797.52 (31.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $69,797.52 | 31.6% | 4 |
| 4425 | Lease Payments & Taxes | $52,887.36 | 24.0% | 1 |
| 4650 | Other Services And Supplies | $42,045.21 | 19.1% | 2 |
| 4250 | Data Processing | $21,930.39 | 9.9% | 4 |
| 4175 | Office Expenses | $9,703.49 | 4.4% | 10 |
| 4200 | Telecomm/Tech Svc And Supplies | $7,010.68 | 3.2% | 7 |
| 4700 | Expendable Property $250-$5000 | $5,253.73 | 2.4% | 3 |
| 4150 | Employee Training | $4,722.00 | 2.1% | 5 |
| 4715 | It Expendable Property | $2,095.00 | 0.9% | 7 |
| 4275 | Publicity & Publications | $1,937.85 | 0.9% | 3 |
| 3230 | Social Security Tax | $1,722.50 | 0.8% | 1 |
| 4400 | Dues And Subscriptions | $735.00 | 0.3% | 3 |
| 4300 | Professional Services | $614.28 | 0.3% | 2 |
| 4315 | It Professional Services | $130.00 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 25 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $69,797.52 | 31.6% |
| 4800 | Interagency Lease Payments | $52,887.36 | 24.0% |
| 4701 | Other Services | $42,030.21 | 19.1% |
| 4367 | Computer Technology Pc Support | $18,719.00 | 8.5% |
| 4301 | Telecom/Voice Usage | $6,642.14 | 3.0% |
| 4999 | Expendable Property Non-It<$5K | $5,253.73 | 2.4% |
| 4406 | Prof Dev Instate Tuition/Registration | $4,416.00 | 2.0% |
| 4200 | Office Supplies | $3,960.80 | 1.8% |
| 4201 | Office Services | $3,480.40 | 1.6% |
| 4375 | Computer Technology Computer Processing | $3,211.39 | 1.5% |
| 4202 | Equipment Rental | $2,262.29 | 1.0% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $1,937.85 | 0.9% |

## Curator notes

Figures are aggregated from 53 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='662' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


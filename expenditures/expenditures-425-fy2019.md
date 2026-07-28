---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-425-fy2019
title: Indian Services Cmsn — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 425, FY2019
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 3900810723066d4651c7227ef0c74a8b9c41ff76c2e4bcebbbb6f2268e443d34
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
  - expenditures-425-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-425
- indian-services-cmsn
agency_code: '425'
agency_name: INDIAN SERVICES CMSN
fiscal_year: 2019
total_expense: '11122.74'
transaction_count: 24
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Indian Services Cmsn — FY2019 expenditures

## At a glance

Indian Services Cmsn (agency code 425, recorded upstream as `INDIAN SERVICES CMSN`) spent **$11,122.74** in fiscal year 2019, across 24 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **77 of 78** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $5,939.81 (53.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $5,939.81 | 53.4% | 4 |
| 4100 | Instate Travel | $2,521.97 | 22.7% | 10 |
| 4700 | Expendable Property $250-$5000 | $1,236.59 | 11.1% | 2 |
| 4175 | Office Expenses | $733.43 | 6.6% | 2 |
| 4715 | It Expendable Property | $323.02 | 2.9% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $267.92 | 2.4% | 3 |
| 4650 | Other Services And Supplies | $100.00 | 0.9% | 1 |

## Largest expenditure classes

The 12 largest of 13 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $5,939.81 | 53.4% |
| 4999 | Expendable Property Non-It<$5K | $1,236.59 | 11.1% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $1,021.86 | 9.2% |
| 4105 | Instate Meals-No Overnight Stay | $821.81 | 7.4% |
| 4200 | Office Supplies | $693.80 | 6.2% |
| 4106 | Instate Lodging | $609.76 | 5.5% |
| 4365 | Computer Technology Pc Equipment<$5K | $323.02 | 2.9% |
| 4301 | Telecom/Voice Usage | $258.05 | 2.3% |
| 4701 | Other Services | $100.00 | 0.9% |
| 4101 | Instate Meals With Overnight Stay | $60.54 | 0.5% |
| 4201 | Office Services | $39.63 | 0.4% |
| 4315 | Telecom/Teleconference Usage | $9.87 | 0.1% |

## Curator notes

Figures are aggregated from 24 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='425' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-425-fy2020
title: Indian Services Cmsn — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 425, FY2020
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
  - expenditures-425-fy2019
  - expenditures-425-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-425
- indian-services-cmsn
agency_code: '425'
agency_name: INDIAN SERVICES CMSN
fiscal_year: 2020
total_expense: '20461.86'
transaction_count: 26
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Indian Services Cmsn — FY2020 expenditures

## At a glance

Indian Services Cmsn (agency code 425, recorded upstream as `INDIAN SERVICES CMSN`) spent **$20,461.86** in fiscal year 2020, across 26 transaction records. That is up 84.0% from $11,122.74 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **77 of 77** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $7,632.29 (37.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $7,632.29 | 37.3% | 4 |
| 4100 | Instate Travel | $5,793.68 | 28.3% | 7 |
| 4715 | It Expendable Property | $2,518.77 | 12.3% | 3 |
| 4175 | Office Expenses | $1,477.19 | 7.2% | 5 |
| 4475 | Facilities Maintenance | $1,472.00 | 7.2% | 1 |
| 4700 | Expendable Property $250-$5000 | $636.35 | 3.1% | 1 |
| 4250 | Data Processing | $605.36 | 3.0% | 1 |
| 4650 | Other Services And Supplies | $175.50 | 0.9% | 2 |
| 4275 | Publicity & Publications | $150.00 | 0.7% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $0.72 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 15 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $7,632.29 | 37.3% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $2,999.79 | 14.7% |
| 4365 | Computer Technology Pc Equipment<$5K | $2,402.06 | 11.7% |
| 4850 | Facilities Maintenance | $1,472.00 | 7.2% |
| 4200 | Office Supplies | $1,432.19 | 7.0% |
| 4105 | Instate Meals-No Overnight Stay | $1,299.78 | 6.4% |
| 4106 | Instate Lodging | $1,246.88 | 6.1% |
| 4999 | Expendable Property Non-It<$5K | $636.35 | 3.1% |
| 4367 | Computer Technology Pc Support | $605.36 | 3.0% |
| 4101 | Instate Meals With Overnight Stay | $247.23 | 1.2% |
| 4701 | Other Services | $175.50 | 0.9% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $150.00 | 0.7% |

## Curator notes

Figures are aggregated from 26 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='425' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-662-fy2019
title: Land Use Brd of Appeals — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 662, FY2019
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
  - expenditures-662-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-662
- land-use-brd-of-appeals
agency_code: '662'
agency_name: LAND USE BRD OF APPEALS
fiscal_year: 2019
total_expense: '125110.67'
transaction_count: 35
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Land Use Brd of Appeals — FY2019 expenditures

## At a glance

Land Use Brd of Appeals (agency code 662, recorded upstream as `LAND USE BRD OF APPEALS`) spent **$125,110.67** in fiscal year 2019, across 35 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **73 of 78** agencies reporting that year.

The largest budget category was **Facilities Rent & Taxes** at $43,082.40 (34.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Facilities Rent & Taxes | $43,082.40 | 34.4% | 1 |
| 4225 | State Government Service Charges | $19,904.07 | 15.9% | 5 |
| 6141 | Dist To State Lands | $13,619.52 | 10.9% | 1 |
| 4300 | Professional Services | $12,685.60 | 10.1% | 1 |
| 4275 | Publicity & Publications | $11,228.79 | 9.0% | 3 |
| 4175 | Office Expenses | $10,800.15 | 8.6% | 9 |
| 4700 | Expendable Property $250-$5000 | $2,949.82 | 2.4% | 3 |
| 4715 | It Expendable Property | $2,908.45 | 2.3% | 1 |
| 4400 | Dues And Subscriptions | $2,863.00 | 2.3% | 2 |
| 4600 | Intra-Inter Agency Charges | $2,695.00 | 2.2% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $1,847.07 | 1.5% | 3 |
| 4150 | Employee Training | $199.12 | 0.2% | 2 |
| 4125 | Out-Of-State Travel | $180.00 | 0.1% | 1 |
| 4375 | Employee Recruitment And Development | $74.88 | 0.1% | 1 |
| 4325 | Attorney General Legal Fees | $72.80 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 19 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Facilities Rent | $43,082.40 | 34.4% |
| 4600 | State Government Service Charges | $19,904.07 | 15.9% |
| 6127 | Distribution To State Lands | $13,619.52 | 10.9% |
| 4500 | Professional Services Non-It | $12,685.60 | 10.1% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $11,228.79 | 9.0% |
| 4200 | Office Supplies | $5,794.78 | 4.6% |
| 4202 | Equipment Rental | $3,533.49 | 2.8% |
| 4999 | Expendable Property Non-It<$5K | $2,949.82 | 2.4% |
| 4365 | Computer Technology Pc Equipment<$5K | $2,908.45 | 2.3% |
| 4251 | Subscriptions And Publications | $2,863.00 | 2.3% |
| 4650 | Intra-Inter Agency Charges | $2,695.00 | 2.2% |
| 4301 | Telecom/Voice Usage | $1,834.73 | 1.5% |

## Curator notes

Figures are aggregated from 35 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='662' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


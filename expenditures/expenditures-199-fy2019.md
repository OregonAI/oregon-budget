---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-199-fy2019
title: Government Ethics Cmsn — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 199, FY2019
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
  - expenditures-199-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-199
- government-ethics-cmsn
agency_code: '199'
agency_name: GOVERNMENT ETHICS CMSN
fiscal_year: 2019
total_expense: '441195.17'
transaction_count: 37
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Government Ethics Cmsn — FY2019 expenditures

## At a glance

Government Ethics Cmsn (agency code 199, recorded upstream as `GOVERNMENT ETHICS CMSN`) spent **$441,195.17** in fiscal year 2019, across 37 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **63 of 78** agencies reporting that year.

The largest budget category was **It Professional Services** at $151,700.00 (34.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4315 | It Professional Services | $151,700.00 | 34.4% | 1 |
| 4325 | Attorney General Legal Fees | $92,887.51 | 21.1% | 2 |
| 4650 | Other Services And Supplies | $84,165.59 | 19.1% | 2 |
| 4425 | Facilities Rent & Taxes | $43,942.82 | 10.0% | 1 |
| 4225 | State Government Service Charges | $23,077.75 | 5.2% | 2 |
| 4250 | Data Processing | $15,292.88 | 3.5% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $12,202.64 | 2.8% | 4 |
| 4715 | It Expendable Property | $7,228.01 | 1.6% | 5 |
| 4100 | Instate Travel | $5,635.77 | 1.3% | 10 |
| 4175 | Office Expenses | $3,750.44 | 0.9% | 4 |
| 4300 | Professional Services | $1,060.21 | 0.2% | 2 |
| 4275 | Publicity & Publications | $251.55 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 20 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4515 | Professional Services Application Maint | $151,700.00 | 34.4% |
| 4550 | Attorney General Legal Fees | $92,887.51 | 21.1% |
| 4701 | Other Services | $84,165.59 | 19.1% |
| 4800 | Facilities Rent | $43,942.82 | 10.0% |
| 4600 | State Government Service Charges | $23,077.75 | 5.2% |
| 4375 | Computer Technology Computer Processing | $15,150.32 | 3.4% |
| 4305 | Telecom/Network Services | $8,490.31 | 1.9% |
| 4365 | Computer Technology Pc Equipment<$5K | $4,789.82 | 1.1% |
| 4301 | Telecom/Voice Usage | $3,712.33 | 0.8% |
| 4111 | Instate Mileage Reimbursmnt-Volunteers | $3,060.64 | 0.7% |
| 4200 | Office Supplies | $2,297.04 | 0.5% |
| 4108 | Instate Ground Transportation | $2,280.29 | 0.5% |

## Curator notes

Figures are aggregated from 37 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='199' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


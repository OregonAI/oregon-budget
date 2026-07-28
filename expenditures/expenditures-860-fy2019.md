---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-860-fy2019
title: Public Utility Cmsn — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 860, FY2019
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
  - expenditures-860-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-860
- public-utility-cmsn
agency_code: '860'
agency_name: PUBLIC UTILITY CMSN
fiscal_year: 2019
total_expense: '38376654.56'
transaction_count: 474
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Public Utility Cmsn — FY2019 expenditures

## At a glance

Public Utility Cmsn (agency code 860, recorded upstream as `PUBLIC UTILITY CMSN`) spent **$38,376,654.56** in fiscal year 2019, across 474 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.18% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **27 of 78** agencies reporting that year.

The largest budget category was **Distribution To Non-Governments** at $30,123,449.88 (78.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6030 | Distribution To Non-Governments | $30,123,449.88 | 78.5% | 33 |
| 4575 | Agency Program Related Svcs & Supp | $3,332,611.72 | 8.7% | 51 |
| 4325 | Attorney General Legal Fees | $1,788,655.56 | 4.7% | 2 |
| 4425 | Facilities Rent & Taxes | $874,832.40 | 2.3% | 5 |
| 4300 | Professional Services | $669,826.76 | 1.7% | 16 |
| 4225 | State Government Service Charges | $406,852.43 | 1.1% | 6 |
| 4175 | Office Expenses | $245,446.53 | 0.6% | 14 |
| 4650 | Other Services And Supplies | $119,623.14 | 0.3% | 19 |
| 4250 | Data Processing | $116,844.53 | 0.3% | 10 |
| 4400 | Dues And Subscriptions | $103,791.00 | 0.3% | 20 |
| 4200 | Telecomm/Tech Svc And Supplies | $98,658.31 | 0.3% | 8 |
| 4100 | Instate Travel | $94,647.22 | 0.2% | 85 |
| 4315 | It Professional Services | $94,378.24 | 0.2% | 6 |
| 4715 | It Expendable Property | $93,257.14 | 0.2% | 9 |
| 4125 | Out-Of-State Travel | $68,273.46 | 0.2% | 104 |
| 5100 | Office Furniture And Fixtures | $45,369.48 | 0.1% | 1 |
| 4150 | Employee Training | $40,525.60 | 0.1% | 57 |
| 4700 | Expendable Property $250-$5000 | $28,615.23 | 0.1% | 8 |
| 4275 | Publicity & Publications | $17,641.38 | 0.0% | 13 |
| 4475 | Facilities Maintenance | $11,882.95 | 0.0% | 2 |
| 5900 | Other Capital Outlay | $1,174.00 | 0.0% | 1 |
| 4375 | Employee Recruitment And Development | $297.60 | 0.0% | 4 |

## Largest expenditure classes

The 12 largest of 74 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6725 | Distribution To Non-Governments | $30,123,449.88 | 78.5% |
| 4975 | Agency Program Related Services | $2,371,508.16 | 6.2% |
| 4550 | Attorney General Legal Fees | $1,788,655.56 | 4.7% |
| 4976 | Agency Program Related Supplies | $960,647.62 | 2.5% |
| 4800 | Facilities Rent | $874,832.40 | 2.3% |
| 4500 | Professional Services Non-It | $669,826.76 | 1.7% |
| 4600 | State Government Service Charges | $406,852.43 | 1.1% |
| 4200 | Office Supplies | $157,717.53 | 0.4% |
| 4701 | Other Services | $119,497.84 | 0.3% |
| 4301 | Telecom/Voice Usage | $87,262.64 | 0.2% |
| 4367 | Computer Technology Pc Support | $82,576.39 | 0.2% |
| 4108 | Instate Ground Transportation | $73,459.30 | 0.2% |

## Curator notes

Figures are aggregated from 474 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='860' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


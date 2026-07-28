---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-833-fy2019
title: Health Related Licensing Brds — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 833, FY2019
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
  - expenditures-833-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-833
- health-related-licensing-brds
agency_code: '833'
agency_name: HEALTH RELATED LICENSING BRDs
fiscal_year: 2019
total_expense: '1003016.85'
transaction_count: 597
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Health Related Licensing Brds — FY2019 expenditures

## At a glance

Health Related Licensing Brds (agency code 833, recorded upstream as `HEALTH RELATED LICENSING BRDs`) spent **$1,003,016.85** in fiscal year 2019, across 597 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **54 of 78** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $288,584.46 (28.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $288,584.46 | 28.8% | 124 |
| 4325 | Attorney General Legal Fees | $175,373.40 | 17.5% | 9 |
| 4425 | Facilities Rent & Taxes | $111,103.00 | 11.1% | 8 |
| 4100 | Instate Travel | $85,332.31 | 8.5% | 160 |
| 4650 | Other Services And Supplies | $80,409.43 | 8.0% | 27 |
| 4225 | State Government Service Charges | $77,863.05 | 7.8% | 34 |
| 4300 | Professional Services | $45,705.17 | 4.6% | 32 |
| 4175 | Office Expenses | $41,213.29 | 4.1% | 63 |
| 4200 | Telecomm/Tech Svc And Supplies | $31,400.99 | 3.1% | 42 |
| 4315 | It Professional Services | $23,532.00 | 2.3% | 6 |
| 4250 | Data Processing | $9,334.27 | 0.9% | 16 |
| 4150 | Employee Training | $8,135.12 | 0.8% | 22 |
| 3240 | Unemployment Assessment | $8,112.00 | 0.8% | 6 |
| 4125 | Out-Of-State Travel | $4,812.66 | 0.5% | 18 |
| 4275 | Publicity & Publications | $4,658.18 | 0.5% | 10 |
| 4400 | Dues And Subscriptions | $4,086.00 | 0.4% | 6 |
| 4715 | It Expendable Property | $1,856.52 | 0.2% | 5 |
| 4700 | Expendable Property $250-$5000 | $859.00 | 0.1% | 1 |
| 4375 | Employee Recruitment And Development | $596.00 | 0.1% | 7 |
| 4475 | Facilities Maintenance | $50.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 56 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $282,502.00 | 28.2% |
| 4550 | Attorney General Legal Fees | $175,373.40 | 17.5% |
| 4800 | Facilities Rent | $111,103.00 | 11.1% |
| 4600 | State Government Service Charges | $77,863.05 | 7.8% |
| 4701 | Other Services | $51,205.99 | 5.1% |
| 4500 | Professional Services Non-It | $45,705.17 | 4.6% |
| 4200 | Office Supplies | $32,644.27 | 3.3% |
| 4730 | Merchant Fees | $26,072.30 | 2.6% |
| 4301 | Telecom/Voice Usage | $24,638.40 | 2.5% |
| 4515 | Professional Services Application Maint | $23,532.00 | 2.3% |
| 4107 | Instate Air Transportation | $21,166.79 | 2.1% |
| 4106 | Instate Lodging | $19,567.09 | 2.0% |

## Curator notes

Figures are aggregated from 597 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='833' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


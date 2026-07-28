---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-114-fy2019
title: Long Term Care Ombud — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 114, FY2019
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
  - expenditures-114-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-114
- long-term-care-ombud
agency_code: '114'
agency_name: LONG TERM CARE OMBUD
fiscal_year: 2019
total_expense: '584910.16'
transaction_count: 175
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Long Term Care Ombud — FY2019 expenditures

## At a glance

Long Term Care Ombud (agency code 114, recorded upstream as `LONG TERM CARE OMBUD`) spent **$584,910.16** in fiscal year 2019, across 175 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **60 of 78** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $143,901.64 (24.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $143,901.64 | 24.6% | 3 |
| 4425 | Facilities Rent & Taxes | $99,950.39 | 17.1% | 1 |
| 4650 | Other Services And Supplies | $80,923.07 | 13.8% | 3 |
| 4100 | Instate Travel | $80,537.00 | 13.8% | 91 |
| 4225 | State Government Service Charges | $53,079.86 | 9.1% | 5 |
| 4175 | Office Expenses | $50,584.53 | 8.6% | 13 |
| 4300 | Professional Services | $20,373.82 | 3.5% | 4 |
| 6055 | Distribution To Contract Svc Provider | $16,795.00 | 2.9% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $16,466.42 | 2.8% | 7 |
| 4275 | Publicity & Publications | $11,723.91 | 2.0% | 10 |
| 4250 | Data Processing | $5,061.31 | 0.9% | 2 |
| 4715 | It Expendable Property | $1,427.50 | 0.2% | 5 |
| 4150 | Employee Training | $1,360.35 | 0.2% | 9 |
| 4315 | It Professional Services | $1,175.00 | 0.2% | 2 |
| 4575 | Agency Program Related Svcs & Supp | $769.80 | 0.1% | 11 |
| 4125 | Out-Of-State Travel | $448.79 | 0.1% | 2 |
| 4550 | Other Care Of Residents & Patients | $331.77 | 0.1% | 6 |

## Largest expenditure classes

The 12 largest of 38 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $143,901.64 | 24.6% |
| 4800 | Facilities Rent | $99,950.39 | 17.1% |
| 4701 | Other Services | $80,923.07 | 13.8% |
| 4600 | State Government Service Charges | $53,079.86 | 9.1% |
| 4200 | Office Supplies | $38,896.77 | 6.7% |
| 4108 | Instate Ground Transportation | $37,662.06 | 6.4% |
| 4500 | Professional Services Non-It | $20,373.82 | 3.5% |
| 6910 | Distribution To Contract Svc Provider | $16,795.00 | 2.9% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $14,836.88 | 2.5% |
| 4101 | Instate Meals With Overnight Stay | $13,503.50 | 2.3% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $11,723.91 | 2.0% |
| 4106 | Instate Lodging | $8,849.50 | 1.5% |

## Curator notes

Figures are aggregated from 175 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='114' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


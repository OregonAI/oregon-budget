---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-585-fy2019
title: Blind, Cmsn for the — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 585, FY2019
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
  - expenditures-585-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-585
- blind-cmsn-for-the
agency_code: '585'
agency_name: BLIND, CMSN FOR THE
fiscal_year: 2019
total_expense: '4245648.22'
transaction_count: 511
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Blind, Cmsn for the — FY2019 expenditures

## At a glance

Blind, Cmsn for the (agency code 585, recorded upstream as `BLIND, CMSN FOR THE`) spent **$4,245,648.22** in fiscal year 2019, across 511 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.02% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **41 of 78** agencies reporting that year.

The largest budget category was **Other Special Payments** at $1,647,999.99 (38.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6085 | Other Special Payments | $1,647,999.99 | 38.8% | 171 |
| 6040 | Distribution To Local School Dist | $782,666.50 | 18.4% | 4 |
| 4575 | Agency Program Related Svcs & Supp | $324,893.81 | 7.7% | 47 |
| 4650 | Other Services And Supplies | $318,882.21 | 7.5% | 37 |
| 4425 | Facilities Rent & Taxes | $303,491.82 | 7.1% | 5 |
| 4315 | It Professional Services | $165,073.91 | 3.9% | 5 |
| 4225 | State Government Service Charges | $159,249.52 | 3.8% | 8 |
| 4200 | Telecomm/Tech Svc And Supplies | $116,723.57 | 2.7% | 10 |
| 4100 | Instate Travel | $113,332.52 | 2.7% | 124 |
| 4325 | Attorney General Legal Fees | $96,724.56 | 2.3% | 3 |
| 4475 | Facilities Maintenance | $43,279.34 | 1.0% | 15 |
| 4175 | Office Expenses | $42,332.57 | 1.0% | 21 |
| 4150 | Employee Training | $33,708.98 | 0.8% | 14 |
| 4715 | It Expendable Property | $31,229.22 | 0.7% | 8 |
| 4125 | Out-Of-State Travel | $21,403.36 | 0.5% | 25 |
| 4300 | Professional Services | $13,081.18 | 0.3% | 2 |
| 5600 | Data Processing Hardware | $10,227.04 | 0.2% | 1 |
| 4250 | Data Processing | $9,543.39 | 0.2% | 1 |
| 4700 | Expendable Property $250-$5000 | $7,040.99 | 0.2% | 6 |
| 3240 | Unemployment Assessment | $2,973.81 | 0.1% | 1 |
| 4275 | Publicity & Publications | $1,789.93 | 0.0% | 3 |

## Largest expenditure classes

The 12 largest of 50 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6900 | Other Special Payments | $1,647,999.99 | 38.8% |
| 6823 | Payments To Local School Districts | $782,666.50 | 18.4% |
| 4800 | Facilities Rent | $303,491.82 | 7.1% |
| 4704 | Other Supplies | $219,329.91 | 5.2% |
| 4975 | Agency Program Related Services | $175,578.14 | 4.1% |
| 4600 | State Government Service Charges | $159,249.52 | 3.8% |
| 4519 | Professional Serv/Managed Serv Provider | $150,015.91 | 3.5% |
| 4976 | Agency Program Related Supplies | $149,315.67 | 3.5% |
| 4550 | Attorney General Legal Fees | $96,724.56 | 2.3% |
| 4701 | Other Services | $89,271.91 | 2.1% |
| 4301 | Telecom/Voice Usage | $83,985.17 | 2.0% |
| 4108 | Instate Ground Transportation | $66,596.00 | 1.6% |

## Curator notes

Figures are aggregated from 511 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='585' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


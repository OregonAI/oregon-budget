---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-213-fy2022
title: Criminal Justice Cmsn — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 213, FY2022
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
  - expenditures-213-fy2021
  - expenditures-213-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-213
- criminal-justice-cmsn
agency_code: '213'
agency_name: CRIMINAL JUSTICE CMSN
fiscal_year: 2022
total_expense: '42470703.76'
transaction_count: 111
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Criminal Justice Cmsn — FY2022 expenditures

## At a glance

Criminal Justice Cmsn (agency code 213, recorded upstream as `CRIMINAL JUSTICE CMSN`) spent **$42,470,703.76** in fiscal year 2022, across 111 transaction records. That is down 10.5% from $47,456,015.86 in FY2021. The agency accounts for 0.14% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **27 of 76** agencies reporting that year.

The largest budget category was **Distribution To Counties** at $36,737,092.92 (86.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6020 | Distribution To Counties | $36,737,092.92 | 86.5% | 40 |
| 6198 | Dist To Judicial | $2,045,956.28 | 4.8% | 1 |
| 6025 | Distribution To Other Govts | $1,199,846.91 | 2.8% | 5 |
| 6085 | Other Special Payments | $825,000.00 | 1.9% | 2 |
| 4300 | Professional Services | $386,883.76 | 0.9% | 6 |
| 4315 | It Professional Services | $300,400.00 | 0.7% | 2 |
| 4250 | Data Processing | $204,743.35 | 0.5% | 6 |
| 6291 | Dist To Corrections | $174,918.12 | 0.4% | 1 |
| 4650 | Other Services And Supplies | $152,806.84 | 0.4% | 4 |
| 4425 | Lease Payments & Taxes | $130,370.90 | 0.3% | 1 |
| 4225 | State Government Service Charges | $118,992.40 | 0.3% | 5 |
| 6257 | Dist To State Police | $91,393.69 | 0.2% | 1 |
| 4325 | Attorney General Legal Fees | $45,762.80 | 0.1% | 1 |
| 4715 | It Expendable Property | $34,154.73 | 0.1% | 5 |
| 4400 | Dues And Subscriptions | $8,462.00 | 0.0% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $8,065.91 | 0.0% | 5 |
| 4100 | Instate Travel | $2,044.77 | 0.0% | 8 |
| 4150 | Employee Training | $1,869.80 | 0.0% | 13 |
| 4700 | Expendable Property $250-$5000 | $1,630.20 | 0.0% | 1 |
| 4275 | Publicity & Publications | $260.98 | 0.0% | 1 |
| 4175 | Office Expenses | $47.40 | 0.0% | 2 |

## Largest expenditure classes

The 12 largest of 36 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6300 | Distribution To Counties | $36,737,092.92 | 86.5% |
| 6132 | Distribution To Judicial 198 | $2,045,956.28 | 4.8% |
| 6700 | Distribution To Other Governments | $1,199,846.91 | 2.8% |
| 6900 | Other Special Payments | $825,000.00 | 1.9% |
| 4500 | Professional Services Non-It | $386,883.76 | 0.9% |
| 4515 | Professional Services Application Maint | $250,000.00 | 0.6% |
| 6139 | Distribution To Corrections | $174,918.12 | 0.4% |
| 4701 | Other Services | $152,628.84 | 0.4% |
| 4375 | Computer Technology Computer Processing | $141,009.89 | 0.3% |
| 4800 | Interagency Lease Payments | $130,370.90 | 0.3% |
| 4600 | State Government Service Charges | $118,992.40 | 0.3% |
| 6136 | Distribution To State Police | $91,393.69 | 0.2% |

## Curator notes

Figures are aggregated from 111 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='213' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


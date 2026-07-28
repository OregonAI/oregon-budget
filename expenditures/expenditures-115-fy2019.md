---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-115-fy2019
title: Employment Relations Brd — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 115, FY2019
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
  - expenditures-115-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-115
- employment-relations-brd
agency_code: '115'
agency_name: EMPLOYMENT RELATIONS BRD
fiscal_year: 2019
total_expense: '354095.93'
transaction_count: 59
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Employment Relations Brd — FY2019 expenditures

## At a glance

Employment Relations Brd (agency code 115, recorded upstream as `EMPLOYMENT RELATIONS BRD`) spent **$354,095.93** in fiscal year 2019, across 59 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **65 of 78** agencies reporting that year.

The largest budget category was **Facilities Rent & Taxes** at $118,217.76 (33.4% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Facilities Rent & Taxes | $118,217.76 | 33.4% | 1 |
| 4650 | Other Services And Supplies | $55,832.03 | 15.8% | 5 |
| 4315 | It Professional Services | $48,750.00 | 13.8% | 1 |
| 4225 | State Government Service Charges | $39,949.14 | 11.3% | 5 |
| 4715 | It Expendable Property | $30,590.12 | 8.6% | 2 |
| 4250 | Data Processing | $21,511.79 | 6.1% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $14,137.04 | 4.0% | 5 |
| 4100 | Instate Travel | $9,079.99 | 2.6% | 20 |
| 4175 | Office Expenses | $4,595.33 | 1.3% | 2 |
| 4125 | Out-Of-State Travel | $3,300.62 | 0.9% | 3 |
| 4400 | Dues And Subscriptions | $2,115.00 | 0.6% | 4 |
| 4150 | Employee Training | $1,830.00 | 0.5% | 2 |
| 4300 | Professional Services | $1,818.47 | 0.5% | 3 |
| 4275 | Publicity & Publications | $1,468.82 | 0.4% | 2 |
| 4700 | Expendable Property $250-$5000 | $396.00 | 0.1% | 1 |
| 3280 | Other Payroll Expenses | $347.57 | 0.1% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $156.25 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 30 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Facilities Rent | $118,217.76 | 33.4% |
| 4701 | Other Services | $55,823.56 | 15.8% |
| 4515 | Professional Services Application Maint | $48,750.00 | 13.8% |
| 4600 | State Government Service Charges | $39,949.14 | 11.3% |
| 4375 | Computer Technology Computer Processing | $21,511.79 | 6.1% |
| 4365 | Computer Technology Pc Equipment<$5K | $16,604.30 | 4.7% |
| 4366 | Computer Technology Pc Software<$5K | $13,985.82 | 3.9% |
| 4301 | Telecom/Voice Usage | $8,653.16 | 2.4% |
| 4305 | Telecom/Network Services | $5,483.88 | 1.5% |
| 4200 | Office Supplies | $4,122.67 | 1.2% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $3,540.50 | 1.0% |
| 4101 | Instate Meals With Overnight Stay | $3,213.87 | 0.9% |

## Curator notes

Figures are aggregated from 59 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='115' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


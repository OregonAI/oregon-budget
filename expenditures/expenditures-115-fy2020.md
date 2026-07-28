---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-115-fy2020
title: Employment Relations Brd — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 115, FY2020
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
  - expenditures-115-fy2019
  - expenditures-115-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-115
- employment-relations-brd
agency_code: '115'
agency_name: EMPLOYMENT RELATIONS BRD
fiscal_year: 2020
total_expense: '364971.52'
transaction_count: 49
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Employment Relations Brd — FY2020 expenditures

## At a glance

Employment Relations Brd (agency code 115, recorded upstream as `EMPLOYMENT RELATIONS BRD`) spent **$364,971.52** in fiscal year 2020, across 49 transaction records. That is up 3.1% from $354,095.93 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **63 of 77** agencies reporting that year.

The largest budget category was **Facilities Rent & Taxes** at $120,582.12 (33.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Facilities Rent & Taxes | $120,582.12 | 33.0% | 1 |
| 4315 | It Professional Services | $60,000.00 | 16.4% | 1 |
| 4225 | State Government Service Charges | $59,612.02 | 16.3% | 5 |
| 4650 | Other Services And Supplies | $53,265.94 | 14.6% | 1 |
| 4250 | Data Processing | $30,152.14 | 8.3% | 3 |
| 4100 | Instate Travel | $14,514.67 | 4.0% | 18 |
| 4715 | It Expendable Property | $13,287.59 | 3.6% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $9,625.12 | 2.6% | 3 |
| 4475 | Facilities Maintenance | $969.00 | 0.3% | 1 |
| 4125 | Out-Of-State Travel | $656.29 | 0.2% | 2 |
| 4150 | Employee Training | $655.54 | 0.2% | 3 |
| 4325 | Attorney General Legal Fees | $577.80 | 0.2% | 1 |
| 4175 | Office Expenses | $499.61 | 0.1% | 2 |
| 4300 | Professional Services | $302.48 | 0.1% | 4 |
| 4400 | Dues And Subscriptions | $150.00 | 0.0% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $121.20 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 28 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Facilities Rent | $120,582.12 | 33.0% |
| 4515 | Professional Services Application Maint | $60,000.00 | 16.4% |
| 4600 | State Government Service Charges | $59,612.02 | 16.3% |
| 4701 | Other Services | $53,265.94 | 14.6% |
| 4367 | Computer Technology Pc Support | $29,166.45 | 8.0% |
| 4365 | Computer Technology Pc Equipment<$5K | $8,156.33 | 2.2% |
| 4301 | Telecom/Voice Usage | $5,630.92 | 1.5% |
| 4101 | Instate Meals With Overnight Stay | $5,336.50 | 1.5% |
| 4366 | Computer Technology Pc Software<$5K | $5,131.26 | 1.4% |
| 4108 | Instate Ground Transportation | $4,606.56 | 1.3% |
| 4305 | Telecom/Network Services | $3,994.20 | 1.1% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $2,956.51 | 0.8% |

## Curator notes

Figures are aggregated from 49 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='115' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-170-fy2021
title: Treasury, Oregon St — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 170, FY2021
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 81c90c241c212dba4cc304dd132bb03379de0003138cc2451899f8f95b1dcc97
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
  - expenditures-170-fy2020
  - expenditures-170-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-170
- treasury-oregon-st
agency_code: '170'
agency_name: TREASURY, OREGON ST
fiscal_year: 2021
total_expense: '15553815.46'
transaction_count: 193
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Treasury, Oregon St — FY2021 expenditures

## At a glance

Treasury, Oregon St (agency code 170, recorded upstream as `TREASURY, OREGON ST`) spent **$15,553,815.46** in fiscal year 2021, across 193 transaction records. That is up 34.9% from $11,525,930.48 in FY2020. The agency accounts for 0.06% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **32 of 76** agencies reporting that year.

The largest budget category was **Professional Services** at $4,167,841.15 (26.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $4,167,841.15 | 26.8% | 28 |
| 5900 | Other Capital Outlay | $3,500,000.00 | 22.5% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $1,990,723.45 | 12.8% | 12 |
| 4425 | Lease Payments & Taxes | $1,277,228.00 | 8.2% | 4 |
| 4225 | State Government Service Charges | $1,036,336.06 | 6.7% | 6 |
| 4715 | It Expendable Property | $758,134.64 | 4.9% | 11 |
| 4250 | Data Processing | $691,378.57 | 4.4% | 13 |
| 5150 | Telecommunications | $497,797.40 | 3.2% | 1 |
| 4315 | It Professional Services | $397,412.83 | 2.6% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $379,718.46 | 2.4% | 14 |
| 4400 | Dues And Subscriptions | $201,184.28 | 1.3% | 18 |
| 4650 | Other Services And Supplies | $139,767.71 | 0.9% | 9 |
| 4325 | Attorney General Legal Fees | $125,833.40 | 0.8% | 1 |
| 4175 | Office Expenses | $121,550.04 | 0.8% | 21 |
| 4275 | Publicity & Publications | $65,214.54 | 0.4% | 12 |
| 4375 | Employee Recruitment And Development | $57,044.30 | 0.4% | 7 |
| 5550 | Data Processing Software | $55,089.82 | 0.4% | 2 |
| 4150 | Employee Training | $41,303.50 | 0.3% | 7 |
| 4100 | Instate Travel | $13,930.69 | 0.1% | 12 |
| 4475 | Facilities Maintenance | $11,555.92 | 0.1% | 4 |
| 4700 | Expendable Property $250-$5000 | $10,261.63 | 0.1% | 3 |
| 3280 | Other Payroll Expenses | $8,120.74 | 0.1% | 1 |
| 3240 | Unemployment Assessment | $6,388.33 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 47 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $4,167,841.15 | 26.8% |
| 5755 | Leasehold Improvements>=$5K | $3,500,000.00 | 22.5% |
| 4975 | Agency Program Related Services | $1,990,723.45 | 12.8% |
| 4800 | Facilities Rent | $1,277,228.00 | 8.2% |
| 4600 | State Government Service Charges | $1,036,336.06 | 6.7% |
| 4375 | Computer Technology Computer Processing | $627,907.44 | 4.0% |
| 5201 | Telecom/Network Equipment>=$5K | $497,797.40 | 3.2% |
| 4515 | Professional Services Application Maint | $344,022.95 | 2.2% |
| 4306 | Telecom/Network Equipment<$5K | $323,090.21 | 2.1% |
| 4307 | Telecom/Network Support | $201,468.33 | 1.3% |
| 4365 | Computer Technology Pc Equipment<$5K | $167,113.28 | 1.1% |
| 4366 | Computer Technology Pc Software<$5K | $142,015.24 | 0.9% |

## Curator notes

Figures are aggregated from 193 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='170' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


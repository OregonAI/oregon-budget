---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-121-fy2020
title: Governor, Office of the — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 121, FY2020
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
  - expenditures-121-fy2019
  - expenditures-121-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-121
- governor-office-of-the
agency_code: '121'
agency_name: GOVERNOR, OFFICE OF THE
fiscal_year: 2020
total_expense: '2476088.52'
transaction_count: 481
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Governor, Office of the — FY2020 expenditures

## At a glance

Governor, Office of the (agency code 121, recorded upstream as `GOVERNOR, OFFICE OF THE`) spent **$2,476,088.52** in fiscal year 2020, across 481 transaction records. That is down 49.0% from $4,852,901.64 in FY2019. The agency accounts for 0.01% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **47 of 77** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $805,871.66 (32.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $805,871.66 | 32.5% | 7 |
| 4425 | Facilities Rent & Taxes | $331,018.35 | 13.4% | 5 |
| 4125 | Out-Of-State Travel | $266,335.12 | 10.8% | 106 |
| 4650 | Other Services And Supplies | $253,470.19 | 10.2% | 11 |
| 4300 | Professional Services | $223,018.27 | 9.0% | 9 |
| 4400 | Dues And Subscriptions | $148,862.00 | 6.0% | 9 |
| 4100 | Instate Travel | $102,423.35 | 4.1% | 186 |
| 4250 | Data Processing | $87,768.45 | 3.5% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $69,503.98 | 2.8% | 10 |
| 4175 | Office Expenses | $37,823.19 | 1.5% | 16 |
| 4150 | Employee Training | $34,540.84 | 1.4% | 68 |
| 4575 | Agency Program Related Svcs & Supp | $32,008.86 | 1.3% | 30 |
| 4325 | Attorney General Legal Fees | $29,681.48 | 1.2% | 2 |
| 4715 | It Expendable Property | $24,709.27 | 1.0% | 6 |
| 3240 | Unemployment Assessment | $16,224.00 | 0.7% | 1 |
| 4275 | Publicity & Publications | $6,903.68 | 0.3% | 7 |
| 4700 | Expendable Property $250-$5000 | $5,675.83 | 0.2% | 2 |
| 4375 | Employee Recruitment And Development | $250.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 60 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $805,871.66 | 32.5% |
| 4800 | Facilities Rent | $331,018.35 | 13.4% |
| 4701 | Other Services | $250,819.43 | 10.1% |
| 4500 | Professional Services Non-It | $223,018.27 | 9.0% |
| 4159 | Out-Of-State Air Transportation | $150,548.56 | 6.1% |
| 4250 | Dues/Memberships | $148,722.00 | 6.0% |
| 4375 | Computer Technology Computer Processing | $86,522.94 | 3.5% |
| 4161 | Foreign Air Transportation | $50,869.80 | 2.1% |
| 4108 | Instate Ground Transportation | $46,690.42 | 1.9% |
| 4301 | Telecom/Voice Usage | $42,094.13 | 1.7% |
| 4550 | Attorney General Legal Fees | $29,681.48 | 1.2% |
| 4106 | Instate Lodging | $29,464.06 | 1.2% |

## Curator notes

Figures are aggregated from 481 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='121' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


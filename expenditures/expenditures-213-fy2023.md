---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-213-fy2023
title: Criminal Justice Cmsn — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 213, FY2023
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 6400163010ab2f341831c864272a89c5e9f2a261fad3fd9572b230042f26e3d5
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
  - expenditures-213-fy2022
  - expenditures-213-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-213
- criminal-justice-cmsn
agency_code: '213'
agency_name: CRIMINAL JUSTICE CMSN
fiscal_year: 2023
total_expense: '81518517.14'
transaction_count: 139
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Criminal Justice Cmsn — FY2023 expenditures

## At a glance

Criminal Justice Cmsn (agency code 213, recorded upstream as `CRIMINAL JUSTICE CMSN`) spent **$81,518,517.14** in fiscal year 2023, across 139 transaction records. That is up 91.9% from $42,470,703.76 in FY2022. The agency accounts for 0.27% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **25 of 77** agencies reporting that year.

The largest budget category was **Distribution To Counties** at $58,142,177.39 (71.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6020 | Distribution To Counties | $58,142,177.39 | 71.3% | 39 |
| 6085 | Other Special Payments | $17,227,942.39 | 21.1% | 13 |
| 6198 | Dist To Judicial | $3,184,169.42 | 3.9% | 1 |
| 6025 | Distribution To Other Govts | $651,489.36 | 0.8% | 4 |
| 4300 | Professional Services | $607,863.53 | 0.7% | 6 |
| 4250 | Data Processing | $571,310.99 | 0.7% | 7 |
| 4315 | It Professional Services | $246,236.30 | 0.3% | 2 |
| 6257 | Dist To State Police | $214,547.07 | 0.3% | 2 |
| 4650 | Other Services And Supplies | $168,595.16 | 0.2% | 6 |
| 4425 | Lease Payments & Taxes | $157,669.90 | 0.2% | 3 |
| 6415 | Dist To Oregon Youth Authority | $119,537.63 | 0.1% | 1 |
| 4225 | State Government Service Charges | $82,174.40 | 0.1% | 5 |
| 6291 | Dist To Corrections | $80,879.63 | 0.1% | 1 |
| 4715 | It Expendable Property | $34,179.25 | 0.0% | 5 |
| 4325 | Attorney General Legal Fees | $9,510.60 | 0.0% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $7,549.32 | 0.0% | 4 |
| 4100 | Instate Travel | $3,773.27 | 0.0% | 14 |
| 4150 | Employee Training | $2,621.39 | 0.0% | 18 |
| 4275 | Publicity & Publications | $2,496.96 | 0.0% | 2 |
| 4375 | Employee Recruitment And Development | $1,960.00 | 0.0% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $1,566.21 | 0.0% | 1 |
| 4175 | Office Expenses | $266.97 | 0.0% | 3 |

## Largest expenditure classes

The 12 largest of 44 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6300 | Distribution To Counties | $58,142,177.39 | 71.3% |
| 6900 | Other Special Payments | $17,227,942.39 | 21.1% |
| 6132 | Distribution To Judicial 198 | $3,184,169.42 | 3.9% |
| 6700 | Distribution To Other Governments | $651,489.36 | 0.8% |
| 4500 | Professional Services Non-It | $607,863.53 | 0.7% |
| 4375 | Computer Technology Computer Processing | $295,932.20 | 0.4% |
| 4367 | Computer Technology Pc Support | $275,378.79 | 0.3% |
| 4515 | Professional Services Application Maint | $236,986.30 | 0.3% |
| 6136 | Distribution To State Police | $214,547.07 | 0.3% |
| 4701 | Other Services | $168,239.16 | 0.2% |
| 4800 | Interagency Lease Payments | $156,009.88 | 0.2% |
| 6096 | Distribution To Oregon Youth Authority | $119,537.63 | 0.1% |

## Curator notes

Figures are aggregated from 139 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='213' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


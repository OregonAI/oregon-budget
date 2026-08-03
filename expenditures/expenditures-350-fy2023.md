---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-350-fy2023
title: Columbia River Gorge Cmsn — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 350, FY2023
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 6400163010ab2f341831c864272a89c5e9f2a261fad3fd9572b230042f26e3d5
snapshot_policy: hash-only
source_data_file: data/expenditures/expenditures-2023.parquet
status: current
content_mode: summary
last_verified: ''
verified_by: ''
maintainer: '@dzinck'
conversion_notes: Title is the source agency name title-cased for reading; the verbatim string is `agency_name`.
  Abbreviations are not expanded. Figures are aggregated, not extracted text.
relationships:
  implements: []
  implemented_by: []
  references_external: []
  related:
  - expenditures-350-fy2022
  - expenditures-350-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-350
- columbia-river-gorge-cmsn
agency_code: '350'
agency_name: COLUMBIA RIVER GORGE CMSN
fiscal_year: 2023
total_expense: '693463.94'
transaction_count: 13
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Columbia River Gorge Cmsn — FY2023 expenditures

## At a glance

Columbia River Gorge Cmsn (agency code 350, recorded upstream as `COLUMBIA RIVER GORGE CMSN`) spent **$693,463.94** in fiscal year 2023, across 13 transaction records. That is up 10.7% from $626,525.69 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **60 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $687,764.10 (99.2% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $693,463.94 | 100.0% | 6 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4300 | Professional Services | Services and supplies | $687,764.10 | 99.2% | 1 |
| 4225 | State Government Service Charges | Services and supplies | $3,366.00 | 0.5% | 1 |
| 4100 | Instate Travel | Services and supplies | $1,164.67 | 0.2% | 8 |
| 4715 | It Expendable Property | Services and supplies | $662.20 | 0.1% | 1 |
| 4575 | Agency Program Related Svcs & Supp | Services and supplies | $331.97 | 0.0% | 1 |
| 4425 | Lease Payments & Taxes | Services and supplies | $175.00 | 0.0% | 1 |

## Largest expenditure classes

The 9 largest of 9 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $687,764.10 | 99.2% |
| 4600 | State Government Service Charges | $3,366.00 | 0.5% |
| 4111 | Instate Mileage Reimbursmnt-Volunteers | $783.29 | 0.1% |
| 4366 | Computer Technology Pc Software<$5K | $662.20 | 0.1% |
| 4106 | Instate Lodging | $369.38 | 0.1% |
| 4206 | Catering Services | $331.97 | 0.0% |
| 4800 | Interagency Lease Payments | $175.00 | 0.0% |
| 4104 | Instate Travel Miscellaneous Expenses | $6.00 | 0.0% |
| 4108 | Instate Ground Transportation | $6.00 | 0.0% |

## Largest vendors

The 7 largest of 7 payees this agency recorded payments to in FY2023, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| COLUMBIA RIVER GORGE COMMISSION | $691,130.10 | 99.7% | 2 |
| US BANK CORPORATE PAYMENT SYSTEMS | $1,538.55 | 0.2% | 4 |
| CARINA MILLER | $438.34 | 0.1% | 2 |
| ROBERT LIBERTY | $126.53 | 0.0% | 2 |
| JAMES MORGAN | $94.87 | 0.0% | 1 |
| RODGER NICHOLS | $84.46 | 0.0% | 1 |
| MICHAEL MILLS | $51.09 | 0.0% | 1 |

## Curator notes

Figures are aggregated from 13 vendor-level transaction records covering 7 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='350' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


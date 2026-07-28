---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-839-fy2019
title: Labor & Ind, Bureau of — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 839, FY2019
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
  - expenditures-839-fy2020
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-839
- labor-ind-bureau-of
agency_code: '839'
agency_name: LABOR & IND, BUREAU OF
fiscal_year: 2019
total_expense: '3654558.77'
transaction_count: 336
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Labor & Ind, Bureau of — FY2019 expenditures

## At a glance

Labor & Ind, Bureau of (agency code 839, recorded upstream as `LABOR & IND, BUREAU OF`) spent **$3,654,558.77** in fiscal year 2019, across 336 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.02% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **43 of 78** agencies reporting that year.

The largest budget category was **Professional Services** at $1,417,693.09 (38.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $1,417,693.09 | 38.8% | 63 |
| 4425 | Facilities Rent & Taxes | $516,671.44 | 14.1% | 3 |
| 4650 | Other Services And Supplies | $354,336.26 | 9.7% | 31 |
| 4225 | State Government Service Charges | $315,601.99 | 8.6% | 7 |
| 4175 | Office Expenses | $312,100.68 | 8.5% | 61 |
| 6100 | Distribution To Dept Of Human Services | $215,315.28 | 5.9% | 1 |
| 4315 | It Professional Services | $98,161.41 | 2.7% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $70,837.53 | 1.9% | 4 |
| 4100 | Instate Travel | $63,043.64 | 1.7% | 89 |
| 4600 | Intra-Inter Agency Charges | $57,178.76 | 1.6% | 1 |
| 6035 | Distribution To Individuals | $54,990.05 | 1.5% | 3 |
| 4715 | It Expendable Property | $54,255.63 | 1.5% | 8 |
| 4250 | Data Processing | $40,221.99 | 1.1% | 4 |
| 4400 | Dues And Subscriptions | $20,468.10 | 0.6% | 4 |
| 3240 | Unemployment Assessment | $18,635.07 | 0.5% | 1 |
| 4150 | Employee Training | $16,018.81 | 0.4% | 16 |
| 4700 | Expendable Property $250-$5000 | $11,819.67 | 0.3% | 6 |
| 4125 | Out-Of-State Travel | $11,488.07 | 0.3% | 26 |
| 4275 | Publicity & Publications | $5,263.10 | 0.1% | 2 |
| 4375 | Employee Recruitment And Development | $458.20 | 0.0% | 3 |

## Largest expenditure classes

The 12 largest of 52 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $1,417,693.09 | 38.8% |
| 4800 | Facilities Rent | $516,671.44 | 14.1% |
| 4600 | State Government Service Charges | $315,601.99 | 8.6% |
| 4701 | Other Services | $242,749.74 | 6.6% |
| 6082 | Distribution To Dhs Agy 100 | $215,315.28 | 5.9% |
| 4201 | Office Services | $136,270.36 | 3.7% |
| 4704 | Other Supplies | $111,547.52 | 3.1% |
| 4200 | Office Supplies | $110,220.37 | 3.0% |
| 4202 | Equipment Rental | $65,609.95 | 1.8% |
| 4301 | Telecom/Voice Usage | $57,397.77 | 1.6% |
| 4650 | Intra-Inter Agency Charges | $57,178.76 | 1.6% |
| 6800 | Distribution To Individuals | $54,990.05 | 1.5% |

## Curator notes

Figures are aggregated from 336 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='839' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


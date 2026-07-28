---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-851-fy2025
title: Nursing, Brd of — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 851, FY2025
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5e9f0c30287913ac0bfff8d74a1225d0c2816ca6a307f2141ebb35602c5a91ed
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
  - expenditures-851-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-851
- nursing-brd-of
agency_code: '851'
agency_name: NURSING, BRD OF
fiscal_year: 2025
total_expense: '4940710.16'
transaction_count: 160
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Nursing, Brd of — FY2025 expenditures

## At a glance

Nursing, Brd of (agency code 851, recorded upstream as `NURSING, BRD OF`) spent **$4,940,710.16** in fiscal year 2025, across 160 transaction records. That is down 1.4% from $5,008,896.12 in FY2024. The agency accounts for 0.01% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **45 of 80** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $1,606,669.83 (32.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $1,606,669.83 | 32.5% | 6 |
| 4325 | Attorney General Legal Fees | $629,259.45 | 12.7% | 1 |
| 4300 | Professional Services | $567,529.61 | 11.5% | 8 |
| 6050 | Distribution To Non-Profit Org | $487,314.00 | 9.9% | 1 |
| 4225 | State Government Service Charges | $460,925.69 | 9.3% | 7 |
| 4425 | Lease Payments & Taxes | $349,432.40 | 7.1% | 3 |
| 4650 | Other Services And Supplies | $261,687.14 | 5.3% | 4 |
| 4715 | It Expendable Property | $219,891.30 | 4.5% | 11 |
| 4200 | Telecomm/Tech Svc And Supplies | $108,006.36 | 2.2% | 8 |
| 4250 | Data Processing | $71,403.75 | 1.4% | 6 |
| 4150 | Employee Training | $38,128.90 | 0.8% | 9 |
| 4175 | Office Expenses | $34,924.40 | 0.7% | 21 |
| 4450 | Fuels And Utilities | $31,469.17 | 0.6% | 7 |
| 4100 | Instate Travel | $21,676.65 | 0.4% | 39 |
| 4700 | Expendable Property $250-$5000 | $18,804.61 | 0.4% | 3 |
| 4125 | Out-Of-State Travel | $15,571.29 | 0.3% | 22 |
| 3240 | Unemployment Assessment | $15,098.26 | 0.3% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $1,796.40 | 0.0% | 1 |
| 3220 | Public Employes' Retirement System | $823.69 | 0.0% | 1 |
| 4375 | Employee Recruitment And Development | $297.26 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 46 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $1,605,724.00 | 32.5% |
| 4550 | Attorney General Legal Fees | $629,259.45 | 12.7% |
| 4500 | Professional Services Non-It | $567,529.61 | 11.5% |
| 6735 | Distribution To Non-Profit Org | $487,314.00 | 9.9% |
| 4600 | State Government Service Charges | $460,925.69 | 9.3% |
| 7007 | Lease Pmt For Buildings | $349,432.40 | 7.1% |
| 4730 | Merchant Fees | $255,723.97 | 5.2% |
| 4365 | Computer Technology Pc Equipment<$5K | $87,303.51 | 1.8% |
| 4366 | Computer Technology Pc Software<$5K | $78,726.71 | 1.6% |
| 4301 | Telecom/Voice Usage | $67,866.65 | 1.4% |
| 4375 | Computer Technology Computer Processing | $64,593.36 | 1.3% |
| 4361 | Computer Technology Server Software<$5K | $49,805.78 | 1.0% |

## Curator notes

Figures are aggregated from 160 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='851' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-632-fy2023
title: Geology & Mineral Ind, Dept of — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 632, FY2023
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
  - expenditures-632-fy2022
  - expenditures-632-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-632
- geology-mineral-ind-dept-of
agency_code: '632'
agency_name: GEOLOGY & MINERAL IND, DEPT OF
fiscal_year: 2023
total_expense: '3144869.90'
transaction_count: 197
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Geology & Mineral Ind, Dept of — FY2023 expenditures

## At a glance

Geology & Mineral Ind, Dept of (agency code 632, recorded upstream as `GEOLOGY & MINERAL IND, DEPT OF`) spent **$3,144,869.90** in fiscal year 2023, across 197 transaction records. That is up 13.2% from $2,778,677.23 in FY2022. The agency accounts for 0.01% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **46 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $1,494,225.44 (47.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $1,494,225.44 | 47.5% | 19 |
| 4250 | Data Processing | $377,134.80 | 12.0% | 7 |
| 4425 | Lease Payments & Taxes | $266,300.29 | 8.5% | 8 |
| 4650 | Other Services And Supplies | $236,625.60 | 7.5% | 8 |
| 4715 | It Expendable Property | $173,615.38 | 5.5% | 5 |
| 4225 | State Government Service Charges | $149,200.77 | 4.7% | 4 |
| 5200 | Technical Equipment | $127,125.00 | 4.0% | 3 |
| 4325 | Attorney General Legal Fees | $74,185.10 | 2.4% | 1 |
| 4100 | Instate Travel | $58,444.29 | 1.9% | 44 |
| 4200 | Telecomm/Tech Svc And Supplies | $30,469.01 | 1.0% | 6 |
| 4575 | Agency Program Related Svcs & Supp | $29,195.49 | 0.9% | 6 |
| 4275 | Publicity & Publications | $28,423.05 | 0.9% | 3 |
| 4700 | Expendable Property $250-$5000 | $27,553.07 | 0.9% | 7 |
| 4150 | Employee Training | $25,322.42 | 0.8% | 54 |
| 5550 | Data Processing Software | $16,875.00 | 0.5% | 1 |
| 3220 | Public Employes' Retirement System | $12,134.61 | 0.4% | 1 |
| 4175 | Office Expenses | $7,751.19 | 0.2% | 11 |
| 4475 | Facilities Maintenance | $5,870.96 | 0.2% | 3 |
| 4125 | Out-Of-State Travel | $4,009.03 | 0.1% | 5 |
| 4450 | Fuels And Utilities | $409.40 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 57 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $1,494,225.44 | 47.5% |
| 4375 | Computer Technology Computer Processing | $350,648.46 | 11.1% |
| 4800 | Interagency Lease Payments | $233,578.60 | 7.4% |
| 4701 | Other Services | $231,921.17 | 7.4% |
| 4600 | State Government Service Charges | $149,200.77 | 4.7% |
| 5250 | Technical Equipment>=$5K | $127,125.00 | 4.0% |
| 4361 | Computer Technology Server Software<$5K | $108,613.66 | 3.5% |
| 4550 | Attorney General Legal Fees | $74,185.10 | 2.4% |
| 4365 | Computer Technology Pc Equipment<$5K | $56,738.55 | 1.8% |
| 4108 | Instate Ground Transportation | $45,392.04 | 1.4% |
| 7007 | Lease Pmt For Buildings | $29,511.37 | 0.9% |
| 4976 | Agency Program Related Supplies | $28,985.63 | 0.9% |

## Curator notes

Figures are aggregated from 197 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='632' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


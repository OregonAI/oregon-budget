---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-833-fy2022
title: Health Related Licensing Brds — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 833, FY2022
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
  - expenditures-833-fy2021
  - expenditures-833-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-833
- health-related-licensing-brds
agency_code: '833'
agency_name: HEALTH RELATED LICENSING BRDs
fiscal_year: 2022
total_expense: '1261653.89'
transaction_count: 310
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Health Related Licensing Brds — FY2022 expenditures

## At a glance

Health Related Licensing Brds (agency code 833, recorded upstream as `HEALTH RELATED LICENSING BRDs`) spent **$1,261,653.89** in fiscal year 2022, across 310 transaction records. That is up 30.3% from $968,548.81 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **53 of 76** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $322,011.62 (25.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $322,011.62 | 25.5% | 6 |
| 4575 | Agency Program Related Svcs & Supp | $305,062.00 | 24.2% | 86 |
| 4425 | Lease Payments & Taxes | $158,697.79 | 12.6% | 16 |
| 4650 | Other Services And Supplies | $144,941.76 | 11.5% | 20 |
| 4225 | State Government Service Charges | $123,469.42 | 9.8% | 24 |
| 3110 | Class/Unclass Salary & Per Diem | $45,177.04 | 3.6% | 2 |
| 4315 | It Professional Services | $37,766.47 | 3.0% | 20 |
| 4200 | Telecomm/Tech Svc And Supplies | $36,561.38 | 2.9% | 41 |
| 4300 | Professional Services | $15,817.73 | 1.3% | 15 |
| 4250 | Data Processing | $15,731.91 | 1.2% | 17 |
| 4175 | Office Expenses | $13,778.24 | 1.1% | 28 |
| 3270 | Flexible Benefits | $9,697.97 | 0.8% | 2 |
| 3220 | Public Employes' Retirement System | $8,467.79 | 0.7% | 4 |
| 4715 | It Expendable Property | $6,277.25 | 0.5% | 3 |
| 4150 | Employee Training | $5,225.00 | 0.4% | 4 |
| 3190 | All Other Differential | $4,019.23 | 0.3% | 1 |
| 3230 | Social Security Tax | $3,705.44 | 0.3% | 2 |
| 3221 | Pension Bond Contribution | $2,741.14 | 0.2% | 2 |
| 4275 | Publicity & Publications | $1,191.59 | 0.1% | 3 |
| 4100 | Instate Travel | $778.53 | 0.1% | 8 |
| 3260 | Mass Transit | $275.95 | 0.0% | 2 |
| 4400 | Dues And Subscriptions | $250.00 | 0.0% | 1 |
| 3250 | Workers' Compensation Assessment | $8.56 | 0.0% | 2 |
| 3210 | Erb Assessment | $0.08 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 41 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $322,011.62 | 25.5% |
| 4975 | Agency Program Related Services | $305,062.00 | 24.2% |
| 4800 | Interagency Lease Payments | $156,518.88 | 12.4% |
| 4600 | State Government Service Charges | $123,469.42 | 9.8% |
| 4701 | Other Services | $74,392.96 | 5.9% |
| 4730 | Merchant Fees | $70,362.86 | 5.6% |
| 3111 | Regular Employees | $45,177.04 | 3.6% |
| 4519 | Professional Serv/Managed Serv Provider | $32,376.00 | 2.6% |
| 4301 | Telecom/Voice Usage | $22,657.03 | 1.8% |
| 4500 | Professional Services Non-It | $15,817.73 | 1.3% |
| 4375 | Computer Technology Computer Processing | $15,731.91 | 1.2% |
| 4200 | Office Supplies | $12,290.65 | 1.0% |

## Curator notes

Figures are aggregated from 310 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='833' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


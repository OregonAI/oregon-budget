---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-833-fy2021
title: Health Related Licensing Brds — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 833, FY2021
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
  - expenditures-833-fy2020
  - expenditures-833-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-833
- health-related-licensing-brds
agency_code: '833'
agency_name: HEALTH RELATED LICENSING BRDs
fiscal_year: 2021
total_expense: '968548.81'
transaction_count: 295
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Health Related Licensing Brds — FY2021 expenditures

## At a glance

Health Related Licensing Brds (agency code 833, recorded upstream as `HEALTH RELATED LICENSING BRDs`) spent **$968,548.81** in fiscal year 2021, across 295 transaction records. That is down 16.5% from $1,159,296.99 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **54 of 76** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $229,485.66 (23.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $229,485.66 | 23.7% | 80 |
| 4325 | Attorney General Legal Fees | $215,529.18 | 22.3% | 6 |
| 4425 | Lease Payments & Taxes | $117,919.20 | 12.2% | 6 |
| 4650 | Other Services And Supplies | $117,031.92 | 12.1% | 29 |
| 4315 | It Professional Services | $94,718.04 | 9.8% | 19 |
| 4225 | State Government Service Charges | $74,630.57 | 7.7% | 24 |
| 3110 | Class/Unclass Salary & Per Diem | $27,979.04 | 2.9% | 4 |
| 4175 | Office Expenses | $20,823.88 | 2.2% | 28 |
| 4200 | Telecomm/Tech Svc And Supplies | $18,984.40 | 2.0% | 29 |
| 4250 | Data Processing | $13,630.12 | 1.4% | 12 |
| 4715 | It Expendable Property | $8,560.85 | 0.9% | 6 |
| 4150 | Employee Training | $5,821.16 | 0.6% | 11 |
| 3270 | Flexible Benefits | $5,485.93 | 0.6% | 2 |
| 3220 | Public Employes' Retirement System | $4,028.06 | 0.4% | 4 |
| 3190 | All Other Differential | $3,537.79 | 0.4% | 1 |
| 4300 | Professional Services | $3,095.23 | 0.3% | 7 |
| 3230 | Social Security Tax | $2,045.47 | 0.2% | 2 |
| 4100 | Instate Travel | $1,866.71 | 0.2% | 9 |
| 3221 | Pension Bond Contribution | $1,514.75 | 0.2% | 2 |
| 4700 | Expendable Property $250-$5000 | $981.32 | 0.1% | 2 |
| 4275 | Publicity & Publications | $711.94 | 0.1% | 7 |
| 3260 | Mass Transit | $162.29 | 0.0% | 2 |
| 3250 | Workers' Compensation Assessment | $5.08 | 0.0% | 2 |
| 3210 | Erb Assessment | $0.22 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 46 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $229,485.66 | 23.7% |
| 4550 | Attorney General Legal Fees | $215,529.18 | 22.3% |
| 4800 | Interagency Lease Payments | $117,919.20 | 12.2% |
| 4701 | Other Services | $84,379.43 | 8.7% |
| 4600 | State Government Service Charges | $74,630.57 | 7.7% |
| 4515 | Professional Services Application Maint | $53,004.04 | 5.5% |
| 4519 | Professional Serv/Managed Serv Provider | $41,714.00 | 4.3% |
| 4730 | Merchant Fees | $32,469.42 | 3.4% |
| 3111 | Regular Employees | $27,979.04 | 2.9% |
| 4200 | Office Supplies | $16,061.18 | 1.7% |
| 4375 | Computer Technology Computer Processing | $13,630.12 | 1.4% |
| 4301 | Telecom/Voice Usage | $11,715.25 | 1.2% |

## Curator notes

Figures are aggregated from 295 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='833' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


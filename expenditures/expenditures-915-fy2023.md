---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-915-fy2023
title: Construction Ctr Brd — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 915, FY2023
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
  - expenditures-915-fy2022
  - expenditures-915-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-915
- construction-ctr-brd
agency_code: '915'
agency_name: CONSTRUCTION CTR BRD
fiscal_year: 2023
total_expense: '1655971.34'
transaction_count: 86
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Construction Ctr Brd — FY2023 expenditures

## At a glance

Construction Ctr Brd (agency code 915, recorded upstream as `CONSTRUCTION CTR BRD`) spent **$1,655,971.34** in fiscal year 2023, across 86 transaction records. That is up 5.1% from $1,574,967.58 in FY2022. The agency accounts for 0.01% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **52 of 77** agencies reporting that year.

The largest budget category was **Lease Payments & Taxes** at $378,492.97 (22.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Lease Payments & Taxes | $378,492.97 | 22.9% | 2 |
| 4650 | Other Services And Supplies | $348,991.68 | 21.1% | 6 |
| 4225 | State Government Service Charges | $333,649.92 | 20.1% | 5 |
| 4175 | Office Expenses | $188,744.78 | 11.4% | 5 |
| 4100 | Instate Travel | $130,996.79 | 7.9% | 36 |
| 4325 | Attorney General Legal Fees | $106,838.53 | 6.5% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $46,733.07 | 2.8% | 5 |
| 4275 | Publicity & Publications | $37,993.22 | 2.3% | 5 |
| 4315 | It Professional Services | $26,013.66 | 1.6% | 3 |
| 4250 | Data Processing | $21,401.72 | 1.3% | 5 |
| 4300 | Professional Services | $18,764.03 | 1.1% | 4 |
| 4715 | It Expendable Property | $11,608.48 | 0.7% | 2 |
| 4150 | Employee Training | $1,753.48 | 0.1% | 2 |
| 3110 | Class/Unclass Salary & Per Diem | $1,502.54 | 0.1% | 2 |
| 4475 | Facilities Maintenance | $1,471.49 | 0.1% | 1 |
| 4125 | Out-Of-State Travel | $539.98 | 0.0% | 1 |
| 4400 | Dues And Subscriptions | $475.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 30 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 7007 | Lease Pmt For Buildings | $356,962.95 | 21.6% |
| 4600 | State Government Service Charges | $333,649.92 | 20.1% |
| 4201 | Office Services | $172,741.07 | 10.4% |
| 4701 | Other Services | $162,305.29 | 9.8% |
| 4730 | Merchant Fees | $141,985.09 | 8.6% |
| 4108 | Instate Ground Transportation | $111,852.36 | 6.8% |
| 4550 | Attorney General Legal Fees | $106,838.53 | 6.5% |
| 4720 | Collection Fees - Dor | $44,701.30 | 2.7% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $37,993.22 | 2.3% |
| 4301 | Telecom/Voice Usage | $36,970.05 | 2.2% |
| 4515 | Professional Services Application Maint | $25,713.66 | 1.6% |
| 7401 | Interest-Leased Assets | $21,530.02 | 1.3% |

## Curator notes

Figures are aggregated from 86 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='915' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


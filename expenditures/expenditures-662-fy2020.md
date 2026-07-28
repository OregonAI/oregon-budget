---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-662-fy2020
title: Land Use Brd of Appeals — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 662, FY2020
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
  - expenditures-662-fy2019
  - expenditures-662-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-662
- land-use-brd-of-appeals
agency_code: '662'
agency_name: LAND USE BRD OF APPEALS
fiscal_year: 2020
total_expense: '128828.27'
transaction_count: 47
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Land Use Brd of Appeals — FY2020 expenditures

## At a glance

Land Use Brd of Appeals (agency code 662, recorded upstream as `LAND USE BRD OF APPEALS`) spent **$128,828.27** in fiscal year 2020, across 47 transaction records. That is up 3.0% from $125,110.67 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **72 of 77** agencies reporting that year.

The largest budget category was **Facilities Rent & Taxes** at $45,350.40 (35.2% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Facilities Rent & Taxes | $45,350.40 | 35.2% | 1 |
| 4225 | State Government Service Charges | $30,196.97 | 23.4% | 5 |
| 4175 | Office Expenses | $14,051.65 | 10.9% | 12 |
| 6141 | Dist To State Lands | $13,619.52 | 10.6% | 1 |
| 4275 | Publicity & Publications | $6,487.05 | 5.0% | 3 |
| 4300 | Professional Services | $5,401.00 | 4.2% | 2 |
| 4400 | Dues And Subscriptions | $4,522.00 | 3.5% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $2,440.13 | 1.9% | 2 |
| 4715 | It Expendable Property | $2,059.23 | 1.6% | 2 |
| 4700 | Expendable Property $250-$5000 | $1,899.37 | 1.5% | 3 |
| 3110 | Class/Unclass Salary & Per Diem | $937.15 | 0.7% | 1 |
| 4150 | Employee Training | $821.66 | 0.6% | 4 |
| 6025 | Distribution To Other Govts | $688.00 | 0.5% | 1 |
| 4650 | Other Services And Supplies | $130.00 | 0.1% | 1 |
| 4100 | Instate Travel | $91.46 | 0.1% | 2 |
| 4375 | Employee Recruitment And Development | $74.88 | 0.1% | 1 |
| 4325 | Attorney General Legal Fees | $42.80 | 0.0% | 1 |
| 3220 | Public Employes' Retirement System | $15.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 24 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Facilities Rent | $45,350.40 | 35.2% |
| 4600 | State Government Service Charges | $30,196.97 | 23.4% |
| 6127 | Distribution To State Lands | $13,619.52 | 10.6% |
| 4200 | Office Supplies | $10,373.96 | 8.1% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $6,487.05 | 5.0% |
| 4500 | Professional Services Non-It | $5,401.00 | 4.2% |
| 4250 | Dues/Memberships | $2,653.00 | 2.1% |
| 4301 | Telecom/Voice Usage | $2,440.13 | 1.9% |
| 4201 | Office Services | $2,129.42 | 1.7% |
| 4999 | Expendable Property Non-It<$5K | $1,899.37 | 1.5% |
| 4365 | Computer Technology Pc Equipment<$5K | $1,892.55 | 1.5% |
| 4251 | Subscriptions And Publications | $1,869.00 | 1.5% |

## Curator notes

Figures are aggregated from 47 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='662' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


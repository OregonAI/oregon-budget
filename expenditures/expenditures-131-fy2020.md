---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-131-fy2020
title: Advocacy Commissions, OR — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 131, FY2020
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
  - expenditures-131-fy2019
  - expenditures-131-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-131
- advocacy-commissions-or
agency_code: '131'
agency_name: ADVOCACY COMMISSIONS, OR
fiscal_year: 2020
total_expense: '74472.90'
transaction_count: 56
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Advocacy Commissions, OR — FY2020 expenditures

## At a glance

Advocacy Commissions, OR (agency code 131, recorded upstream as `ADVOCACY COMMISSIONS, OR`) spent **$74,472.90** in fiscal year 2020, across 56 transaction records. That is up 18.1% from $63,041.88 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **73 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $22,130.44 (29.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $22,130.44 | 29.7% | 2 |
| 4650 | Other Services And Supplies | $16,055.81 | 21.6% | 2 |
| 4225 | State Government Service Charges | $9,790.63 | 13.1% | 3 |
| 4100 | Instate Travel | $8,589.34 | 11.5% | 36 |
| 4250 | Data Processing | $7,424.73 | 10.0% | 2 |
| 4715 | It Expendable Property | $5,728.37 | 7.7% | 2 |
| 4325 | Attorney General Legal Fees | $2,204.20 | 3.0% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $1,172.42 | 1.6% | 3 |
| 4175 | Office Expenses | $752.86 | 1.0% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $395.94 | 0.5% | 1 |
| 4150 | Employee Training | $188.26 | 0.3% | 2 |
| 4375 | Employee Recruitment And Development | $39.90 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 20 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $22,130.44 | 29.7% |
| 4701 | Other Services | $16,054.15 | 21.6% |
| 4600 | State Government Service Charges | $9,790.63 | 13.1% |
| 4375 | Computer Technology Computer Processing | $6,845.28 | 9.2% |
| 4365 | Computer Technology Pc Equipment<$5K | $4,983.40 | 6.7% |
| 4111 | Instate Mileage Reimbursmnt-Volunteers | $4,926.47 | 6.6% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $3,146.07 | 4.2% |
| 4550 | Attorney General Legal Fees | $2,204.20 | 3.0% |
| 4200 | Office Supplies | $752.86 | 1.0% |
| 4366 | Computer Technology Pc Software<$5K | $744.97 | 1.0% |
| 4206 | Catering Services | $703.93 | 0.9% |
| 4367 | Computer Technology Pc Support | $579.45 | 0.8% |

## Curator notes

Figures are aggregated from 56 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='131' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-172-fy2023
title: Facilites Auth, Oregon — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 172, FY2023
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
  - expenditures-172-fy2022
  - expenditures-172-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-172
- facilites-auth-oregon
agency_code: '172'
agency_name: FACILITES AUTH, OREGON
fiscal_year: 2023
total_expense: '299166.49'
transaction_count: 12
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Facilites Auth, Oregon — FY2023 expenditures

## At a glance

Facilites Auth, Oregon (agency code 172, recorded upstream as `FACILITES AUTH, OREGON`) spent **$299,166.49** in fiscal year 2023, across 12 transaction records. That is up 30.0% from $230,194.92 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **70 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $237,277.63 (79.3% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $237,277.63 | 79.3% | 4 |
| 4650 | Other Services And Supplies | $55,464.97 | 18.5% | 2 |
| 4400 | Dues And Subscriptions | $3,250.00 | 1.1% | 1 |
| 4325 | Attorney General Legal Fees | $2,697.20 | 0.9% | 1 |
| 4225 | State Government Service Charges | $399.69 | 0.1% | 3 |
| 4275 | Publicity & Publications | $77.00 | 0.0% | 1 |

## Largest expenditure classes

The 6 largest of 6 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $237,277.63 | 79.3% |
| 4701 | Other Services | $55,464.97 | 18.5% |
| 4250 | Dues/Memberships | $3,250.00 | 1.1% |
| 4550 | Attorney General Legal Fees | $2,697.20 | 0.9% |
| 4600 | State Government Service Charges | $399.69 | 0.1% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $77.00 | 0.0% |

## Curator notes

Figures are aggregated from 12 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='172' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


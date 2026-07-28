---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-425-fy2022
title: Indian Services Cmsn — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 425, FY2022
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
  - expenditures-425-fy2021
  - expenditures-425-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-425
- indian-services-cmsn
agency_code: '425'
agency_name: INDIAN SERVICES CMSN
fiscal_year: 2022
total_expense: '9738.81'
transaction_count: 9
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Indian Services Cmsn — FY2022 expenditures

## At a glance

Indian Services Cmsn (agency code 425, recorded upstream as `INDIAN SERVICES CMSN`) spent **$9,738.81** in fiscal year 2022, across 9 transaction records. That is up 1.9% from $9,556.29 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **76 of 76** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $7,772.55 (79.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $7,772.55 | 79.8% | 4 |
| 4100 | Instate Travel | $1,196.30 | 12.3% | 3 |
| 4150 | Employee Training | $633.00 | 6.5% | 1 |
| 4715 | It Expendable Property | $136.96 | 1.4% | 1 |

## Largest expenditure classes

The 5 largest of 5 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $7,772.55 | 79.8% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $821.52 | 8.4% |
| 4437 | Prof Dev Dues/Membership | $633.00 | 6.5% |
| 4106 | Instate Lodging | $374.78 | 3.8% |
| 4366 | Computer Technology Pc Software<$5K | $136.96 | 1.4% |

## Curator notes

Figures are aggregated from 9 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='425' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


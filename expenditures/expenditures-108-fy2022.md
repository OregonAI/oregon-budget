---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-108-fy2022
title: Mental Health Regulatory Agy — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 108, FY2022
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
  - expenditures-108-fy2021
  - expenditures-108-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-108
- mental-health-regulatory-agy
agency_code: '108'
agency_name: MENTAL HEALTH REGULATORY AGY
fiscal_year: 2022
total_expense: '703269.53'
transaction_count: 49
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Mental Health Regulatory Agy — FY2022 expenditures

## At a glance

Mental Health Regulatory Agy (agency code 108, recorded upstream as `MENTAL HEALTH REGULATORY AGY`) spent **$703,269.53** in fiscal year 2022, across 49 transaction records. That is down 10.3% from $783,890.01 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **58 of 76** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $181,189.00 (25.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $181,189.00 | 25.8% | 1 |
| 4650 | Other Services And Supplies | $147,816.23 | 21.0% | 5 |
| 4425 | Lease Payments & Taxes | $129,853.22 | 18.5% | 1 |
| 4225 | State Government Service Charges | $89,966.64 | 12.8% | 4 |
| 4575 | Agency Program Related Svcs & Supp | $71,054.00 | 10.1% | 1 |
| 4250 | Data Processing | $34,117.89 | 4.9% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $11,928.77 | 1.7% | 5 |
| 4300 | Professional Services | $11,430.02 | 1.6% | 4 |
| 4175 | Office Expenses | $11,239.96 | 1.6% | 3 |
| 4125 | Out-Of-State Travel | $4,478.73 | 0.6% | 12 |
| 4150 | Employee Training | $3,900.00 | 0.6% | 1 |
| 4715 | It Expendable Property | $3,236.77 | 0.5% | 3 |
| 4400 | Dues And Subscriptions | $2,400.00 | 0.3% | 3 |
| 4275 | Publicity & Publications | $529.53 | 0.1% | 2 |
| 4100 | Instate Travel | $128.77 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 27 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $181,189.00 | 25.8% |
| 4800 | Interagency Lease Payments | $129,853.22 | 18.5% |
| 4701 | Other Services | $109,712.25 | 15.6% |
| 4600 | State Government Service Charges | $89,966.64 | 12.8% |
| 4975 | Agency Program Related Services | $71,054.00 | 10.1% |
| 4730 | Merchant Fees | $38,028.75 | 5.4% |
| 4367 | Computer Technology Pc Support | $33,000.00 | 4.7% |
| 4500 | Professional Services Non-It | $11,430.02 | 1.6% |
| 4301 | Telecom/Voice Usage | $9,525.29 | 1.4% |
| 4200 | Office Supplies | $6,009.82 | 0.9% |
| 4201 | Office Services | $5,230.14 | 0.7% |
| 4406 | Prof Dev Instate Tuition/Registration | $3,900.00 | 0.6% |

## Curator notes

Figures are aggregated from 49 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='108' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


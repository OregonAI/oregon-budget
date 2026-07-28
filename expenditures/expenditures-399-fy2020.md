---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-399-fy2020
title: Psychiatric Security Rev Brd — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 399, FY2020
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
  - expenditures-399-fy2019
  - expenditures-399-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-399
- psychiatric-security-rev-brd
agency_code: '399'
agency_name: PSYCHIATRIC SECURITY REV BRD
fiscal_year: 2020
total_expense: '255802.31'
transaction_count: 61
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Psychiatric Security Rev Brd — FY2020 expenditures

## At a glance

Psychiatric Security Rev Brd (agency code 399, recorded upstream as `PSYCHIATRIC SECURITY REV BRD`) spent **$255,802.31** in fiscal year 2020, across 61 transaction records. That is down 11.4% from $288,614.17 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **68 of 77** agencies reporting that year.

The largest budget category was **Facilities Rent & Taxes** at $62,850.42 (24.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Facilities Rent & Taxes | $62,850.42 | 24.6% | 1 |
| 4225 | State Government Service Charges | $54,660.20 | 21.4% | 5 |
| 4325 | Attorney General Legal Fees | $43,223.30 | 16.9% | 1 |
| 4650 | Other Services And Supplies | $19,489.82 | 7.6% | 3 |
| 4250 | Data Processing | $17,663.28 | 6.9% | 3 |
| 4715 | It Expendable Property | $15,324.92 | 6.0% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $11,353.90 | 4.4% | 4 |
| 4175 | Office Expenses | $8,291.65 | 3.2% | 12 |
| 4100 | Instate Travel | $6,881.94 | 2.7% | 13 |
| 4300 | Professional Services | $3,895.56 | 1.5% | 4 |
| 4315 | It Professional Services | $3,721.20 | 1.5% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $3,558.23 | 1.4% | 2 |
| 4700 | Expendable Property $250-$5000 | $2,352.00 | 0.9% | 1 |
| 4150 | Employee Training | $1,516.35 | 0.6% | 6 |
| 4275 | Publicity & Publications | $905.34 | 0.4% | 2 |
| 3220 | Public Employes' Retirement System | $114.20 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 29 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Facilities Rent | $62,850.42 | 24.6% |
| 4600 | State Government Service Charges | $54,660.20 | 21.4% |
| 4550 | Attorney General Legal Fees | $43,223.30 | 16.9% |
| 4701 | Other Services | $19,438.04 | 7.6% |
| 4365 | Computer Technology Pc Equipment<$5K | $15,094.92 | 5.9% |
| 4375 | Computer Technology Computer Processing | $14,058.75 | 5.5% |
| 4305 | Telecom/Network Services | $6,690.85 | 2.6% |
| 4200 | Office Supplies | $5,010.65 | 2.0% |
| 4301 | Telecom/Voice Usage | $4,663.05 | 1.8% |
| 4500 | Professional Services Non-It | $3,895.56 | 1.5% |
| 4515 | Professional Services Application Maint | $3,721.20 | 1.5% |
| 4108 | Instate Ground Transportation | $3,653.83 | 1.4% |

## Curator notes

Figures are aggregated from 61 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='399' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


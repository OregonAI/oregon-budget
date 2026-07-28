---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-811-fy2025
title: Chiropractic Exam, Brd of — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 811, FY2025
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5e9f0c30287913ac0bfff8d74a1225d0c2816ca6a307f2141ebb35602c5a91ed
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
  - expenditures-811-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-811
- chiropractic-exam-brd-of
agency_code: '811'
agency_name: CHIROPRACTIC EXAM, BRD OF
fiscal_year: 2025
total_expense: '485825.43'
transaction_count: 54
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Chiropractic Exam, Brd of — FY2025 expenditures

## At a glance

Chiropractic Exam, Brd of (agency code 811, recorded upstream as `CHIROPRACTIC EXAM, BRD OF`) spent **$485,825.43** in fiscal year 2025, across 54 transaction records. That is up 0.8% from $481,826.46 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **69 of 80** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $232,209.35 (47.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $232,209.35 | 47.8% | 1 |
| 4650 | Other Services And Supplies | $79,358.97 | 16.3% | 7 |
| 4425 | Lease Payments & Taxes | $55,072.62 | 11.3% | 1 |
| 4225 | State Government Service Charges | $38,266.40 | 7.9% | 5 |
| 4250 | Data Processing | $29,923.75 | 6.2% | 4 |
| 4575 | Agency Program Related Svcs & Supp | $22,856.75 | 4.7% | 1 |
| 4300 | Professional Services | $11,618.27 | 2.4% | 8 |
| 3220 | Public Employes' Retirement System | $3,363.56 | 0.7% | 1 |
| 4715 | It Expendable Property | $2,938.04 | 0.6% | 3 |
| 4150 | Employee Training | $2,654.48 | 0.5% | 8 |
| 4175 | Office Expenses | $2,586.73 | 0.5% | 5 |
| 4100 | Instate Travel | $2,516.27 | 0.5% | 7 |
| 4200 | Telecomm/Tech Svc And Supplies | $2,460.24 | 0.5% | 3 |

## Largest expenditure classes

The 12 largest of 26 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $232,209.35 | 47.8% |
| 4701 | Other Services | $55,100.56 | 11.3% |
| 4800 | Interagency Lease Payments | $55,072.62 | 11.3% |
| 4600 | State Government Service Charges | $38,266.40 | 7.9% |
| 4367 | Computer Technology Pc Support | $27,895.54 | 5.7% |
| 4730 | Merchant Fees | $24,258.41 | 5.0% |
| 4975 | Agency Program Related Services | $22,856.75 | 4.7% |
| 4500 | Professional Services Non-It | $11,618.27 | 2.4% |
| 3210 | Public Employees Retirement Contribution | $3,363.56 | 0.7% |
| 4365 | Computer Technology Pc Equipment<$5K | $2,258.74 | 0.5% |
| 4375 | Computer Technology Computer Processing | $2,028.21 | 0.4% |
| 4301 | Telecom/Voice Usage | $1,922.32 | 0.4% |

## Curator notes

Figures are aggregated from 54 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='811' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-811-fy2021
title: Chiropractic Exam, Brd of — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 811, FY2021
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
  - expenditures-811-fy2020
  - expenditures-811-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-811
- chiropractic-exam-brd-of
agency_code: '811'
agency_name: CHIROPRACTIC EXAM, BRD OF
fiscal_year: 2021
total_expense: '297517.42'
transaction_count: 41
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Chiropractic Exam, Brd of — FY2021 expenditures

## At a glance

Chiropractic Exam, Brd of (agency code 811, recorded upstream as `CHIROPRACTIC EXAM, BRD OF`) spent **$297,517.42** in fiscal year 2021, across 41 transaction records. That is down 4.4% from $311,299.02 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **64 of 76** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $98,770.58 (33.2% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $98,770.58 | 33.2% | 1 |
| 4425 | Lease Payments & Taxes | $50,848.86 | 17.1% | 1 |
| 4650 | Other Services And Supplies | $45,312.45 | 15.2% | 4 |
| 4225 | State Government Service Charges | $28,901.18 | 9.7% | 5 |
| 4575 | Agency Program Related Svcs & Supp | $27,988.50 | 9.4% | 1 |
| 4315 | It Professional Services | $16,991.50 | 5.7% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $9,077.95 | 3.1% | 4 |
| 4300 | Professional Services | $8,232.46 | 2.8% | 9 |
| 4250 | Data Processing | $5,140.18 | 1.7% | 2 |
| 4400 | Dues And Subscriptions | $2,423.00 | 0.8% | 2 |
| 4175 | Office Expenses | $2,342.35 | 0.8% | 2 |
| 4275 | Publicity & Publications | $783.65 | 0.3% | 3 |
| 4150 | Employee Training | $500.00 | 0.2% | 1 |
| 4100 | Instate Travel | $204.76 | 0.1% | 4 |

## Largest expenditure classes

The 12 largest of 20 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $98,770.58 | 33.2% |
| 4800 | Interagency Lease Payments | $50,848.86 | 17.1% |
| 4701 | Other Services | $30,631.98 | 10.3% |
| 4600 | State Government Service Charges | $28,901.18 | 9.7% |
| 4975 | Agency Program Related Services | $27,988.50 | 9.4% |
| 4730 | Merchant Fees | $14,680.47 | 4.9% |
| 4513 | Professional Services Application New | $12,493.75 | 4.2% |
| 4500 | Professional Services Non-It | $8,232.46 | 2.8% |
| 4305 | Telecom/Network Services | $6,246.99 | 2.1% |
| 4375 | Computer Technology Computer Processing | $5,140.18 | 1.7% |
| 4516 | Professional Services Servers | $4,497.75 | 1.5% |
| 4301 | Telecom/Voice Usage | $2,830.96 | 1.0% |

## Curator notes

Figures are aggregated from 41 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='811' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


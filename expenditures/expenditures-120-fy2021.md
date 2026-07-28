---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-120-fy2021
title: Accountancy, Oregon Brd of — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 120, FY2021
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
  - expenditures-120-fy2020
  - expenditures-120-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-120
- accountancy-oregon-brd-of
agency_code: '120'
agency_name: ACCOUNTANCY, OREGON BRD OF
fiscal_year: 2021
total_expense: '473590.45'
transaction_count: 37
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Accountancy, Oregon Brd of — FY2021 expenditures

## At a glance

Accountancy, Oregon Brd of (agency code 120, recorded upstream as `ACCOUNTANCY, OREGON BRD OF`) spent **$473,590.45** in fiscal year 2021, across 37 transaction records. That is up 1.0% from $468,925.67 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **59 of 76** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $225,538.41 (47.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $225,538.41 | 47.6% | 1 |
| 4425 | Lease Payments & Taxes | $62,554.05 | 13.2% | 1 |
| 4650 | Other Services And Supplies | $53,143.41 | 11.2% | 6 |
| 4225 | State Government Service Charges | $42,239.61 | 8.9% | 4 |
| 4300 | Professional Services | $21,160.27 | 4.5% | 4 |
| 4200 | Telecomm/Tech Svc And Supplies | $20,046.53 | 4.2% | 5 |
| 4250 | Data Processing | $18,428.04 | 3.9% | 2 |
| 4715 | It Expendable Property | $15,457.27 | 3.3% | 4 |
| 4175 | Office Expenses | $10,661.49 | 2.3% | 3 |
| 4275 | Publicity & Publications | $3,709.20 | 0.8% | 2 |
| 4100 | Instate Travel | $652.17 | 0.1% | 5 |

## Largest expenditure classes

The 12 largest of 22 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $225,538.41 | 47.6% |
| 4800 | Facilities Rent | $62,554.05 | 13.2% |
| 4600 | State Government Service Charges | $42,239.61 | 8.9% |
| 4701 | Other Services | $32,750.94 | 6.9% |
| 4500 | Professional Services Non-It | $21,160.27 | 4.5% |
| 4730 | Merchant Fees | $19,081.14 | 4.0% |
| 4367 | Computer Technology Pc Support | $17,592.00 | 3.7% |
| 4301 | Telecom/Voice Usage | $16,439.63 | 3.5% |
| 4365 | Computer Technology Pc Equipment<$5K | $11,055.58 | 2.3% |
| 4201 | Office Services | $8,940.85 | 1.9% |
| 4253 | Advertise Publicity Publish/Print Srvs | $3,709.20 | 0.8% |
| 4303 | Telecom/Voice Maintenance | $2,277.72 | 0.5% |

## Curator notes

Figures are aggregated from 37 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='120' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


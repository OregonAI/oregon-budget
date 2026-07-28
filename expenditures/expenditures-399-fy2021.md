---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-399-fy2021
title: Psychiatric Security Rev Brd — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 399, FY2021
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
  - expenditures-399-fy2020
  - expenditures-399-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-399
- psychiatric-security-rev-brd
agency_code: '399'
agency_name: PSYCHIATRIC SECURITY REV BRD
fiscal_year: 2021
total_expense: '272684.02'
transaction_count: 34
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Psychiatric Security Rev Brd — FY2021 expenditures

## At a glance

Psychiatric Security Rev Brd (agency code 399, recorded upstream as `PSYCHIATRIC SECURITY REV BRD`) spent **$272,684.02** in fiscal year 2021, across 34 transaction records. That is up 6.6% from $255,802.31 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **65 of 76** agencies reporting that year.

The largest budget category was **Lease Payments & Taxes** at $73,311.78 (26.9% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Lease Payments & Taxes | $73,311.78 | 26.9% | 1 |
| 4325 | Attorney General Legal Fees | $63,880.40 | 23.4% | 1 |
| 4225 | State Government Service Charges | $54,479.90 | 20.0% | 6 |
| 4250 | Data Processing | $28,916.08 | 10.6% | 5 |
| 4650 | Other Services And Supplies | $15,359.80 | 5.6% | 4 |
| 4715 | It Expendable Property | $12,861.10 | 4.7% | 1 |
| 3240 | Unemployment Assessment | $9,952.00 | 3.6% | 1 |
| 4175 | Office Expenses | $6,231.28 | 2.3% | 8 |
| 4200 | Telecomm/Tech Svc And Supplies | $5,102.35 | 1.9% | 3 |
| 4300 | Professional Services | $1,807.32 | 0.7% | 2 |
| 4100 | Instate Travel | $782.01 | 0.3% | 2 |

## Largest expenditure classes

The 12 largest of 16 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Facilities Rent | $73,311.78 | 26.9% |
| 4550 | Attorney General Legal Fees | $63,880.40 | 23.4% |
| 4600 | State Government Service Charges | $54,479.90 | 20.0% |
| 4375 | Computer Technology Computer Processing | $25,756.03 | 9.4% |
| 4701 | Other Services | $15,359.80 | 5.6% |
| 4365 | Computer Technology Pc Equipment<$5K | $12,861.10 | 4.7% |
| 3231 | Unemployment Compensation & Assessment | $9,952.00 | 3.6% |
| 4301 | Telecom/Voice Usage | $4,457.29 | 1.6% |
| 4200 | Office Supplies | $4,279.39 | 1.6% |
| 4367 | Computer Technology Pc Support | $3,160.05 | 1.2% |
| 4500 | Professional Services Non-It | $1,807.32 | 0.7% |
| 4202 | Equipment Rental | $1,681.96 | 0.6% |

## Curator notes

Figures are aggregated from 34 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='399' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


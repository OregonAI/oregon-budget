---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-662-fy2023
title: Land Use Brd of Appeals — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 662, FY2023
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
  - expenditures-662-fy2022
  - expenditures-662-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-662
- land-use-brd-of-appeals
agency_code: '662'
agency_name: LAND USE BRD OF APPEALS
fiscal_year: 2023
total_expense: '199279.77'
transaction_count: 46
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Land Use Brd of Appeals — FY2023 expenditures

## At a glance

Land Use Brd of Appeals (agency code 662, recorded upstream as `LAND USE BRD OF APPEALS`) spent **$199,279.77** in fiscal year 2023, across 46 transaction records. That is down 9.7% from $220,585.01 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **72 of 77** agencies reporting that year.

The largest budget category was **Lease Payments & Taxes** at $52,887.36 (26.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Lease Payments & Taxes | $52,887.36 | 26.5% | 1 |
| 4650 | Other Services And Supplies | $42,573.14 | 21.4% | 2 |
| 4225 | State Government Service Charges | $33,640.41 | 16.9% | 5 |
| 4250 | Data Processing | $23,490.87 | 11.8% | 6 |
| 4715 | It Expendable Property | $16,038.41 | 8.0% | 5 |
| 4175 | Office Expenses | $10,801.16 | 5.4% | 5 |
| 4200 | Telecomm/Tech Svc And Supplies | $7,577.89 | 3.8% | 4 |
| 4275 | Publicity & Publications | $5,383.44 | 2.7% | 2 |
| 3240 | Unemployment Assessment | $4,548.04 | 2.3% | 1 |
| 4150 | Employee Training | $1,698.01 | 0.9% | 10 |
| 4400 | Dues And Subscriptions | $315.00 | 0.2% | 3 |
| 4325 | Attorney General Legal Fees | $199.20 | 0.1% | 1 |
| 4300 | Professional Services | $126.84 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 21 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Interagency Lease Payments | $52,887.36 | 26.5% |
| 4701 | Other Services | $42,573.14 | 21.4% |
| 4600 | State Government Service Charges | $33,640.41 | 16.9% |
| 4367 | Computer Technology Pc Support | $17,501.14 | 8.8% |
| 4365 | Computer Technology Pc Equipment<$5K | $13,356.05 | 6.7% |
| 4201 | Office Services | $7,995.70 | 4.0% |
| 4375 | Computer Technology Computer Processing | $5,989.73 | 3.0% |
| 4301 | Telecom/Voice Usage | $5,897.33 | 3.0% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $5,383.44 | 2.7% |
| 3231 | Unemployment Compensation & Assessment | $4,548.04 | 2.3% |
| 4372 | Computer Technology Peripheral Equip<$5K | $2,682.36 | 1.3% |
| 4202 | Equipment Rental | $1,834.27 | 0.9% |

## Curator notes

Figures are aggregated from 46 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='662' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


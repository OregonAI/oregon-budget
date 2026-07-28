---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-662-fy2025
title: Land Use Brd of Appeals — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 662, FY2025
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
  - expenditures-662-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-662
- land-use-brd-of-appeals
agency_code: '662'
agency_name: LAND USE BRD OF APPEALS
fiscal_year: 2025
total_expense: '206937.86'
transaction_count: 36
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Land Use Brd of Appeals — FY2025 expenditures

## At a glance

Land Use Brd of Appeals (agency code 662, recorded upstream as `LAND USE BRD OF APPEALS`) spent **$206,937.86** in fiscal year 2025, across 36 transaction records. That is up 9.8% from $188,424.41 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **75 of 80** agencies reporting that year.

The largest budget category was **Lease Payments & Taxes** at $65,831.44 (31.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4425 | Lease Payments & Taxes | $65,831.44 | 31.8% | 2 |
| 4650 | Other Services And Supplies | $48,232.33 | 23.3% | 2 |
| 4225 | State Government Service Charges | $45,111.84 | 21.8% | 6 |
| 4250 | Data Processing | $21,652.70 | 10.5% | 3 |
| 4300 | Professional Services | $8,376.13 | 4.0% | 4 |
| 4700 | Expendable Property $250-$5000 | $6,740.04 | 3.3% | 2 |
| 3220 | Public Employes' Retirement System | $3,957.12 | 1.9% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $2,977.00 | 1.4% | 3 |
| 4175 | Office Expenses | $2,411.97 | 1.2% | 4 |
| 4150 | Employee Training | $1,099.12 | 0.5% | 7 |
| 4275 | Publicity & Publications | $405.39 | 0.2% | 1 |
| 4715 | It Expendable Property | $142.78 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 17 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4800 | Interagency Lease Payments | $65,831.44 | 31.8% |
| 4701 | Other Services | $48,232.33 | 23.3% |
| 4600 | State Government Service Charges | $45,111.84 | 21.8% |
| 4367 | Computer Technology Pc Support | $19,363.00 | 9.4% |
| 4500 | Professional Services Non-It | $8,376.13 | 4.0% |
| 4999 | Expendable Property Non-It<$5K | $6,740.04 | 3.3% |
| 3210 | Public Employees Retirement Contribution | $3,957.12 | 1.9% |
| 4201 | Office Services | $2,370.87 | 1.1% |
| 4301 | Telecom/Voice Usage | $2,323.24 | 1.1% |
| 4375 | Computer Technology Computer Processing | $2,289.70 | 1.1% |
| 4305 | Telecom/Network Services | $653.76 | 0.3% |
| 4437 | Prof Dev Dues/Membership | $533.00 | 0.3% |

## Curator notes

Figures are aggregated from 36 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='662' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


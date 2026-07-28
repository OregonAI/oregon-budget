---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-199-fy2025
title: Government Ethics Cmsn — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 199, FY2025
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
  - expenditures-199-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-199
- government-ethics-cmsn
agency_code: '199'
agency_name: GOVERNMENT ETHICS CMSN
fiscal_year: 2025
total_expense: '696465.11'
transaction_count: 45
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Government Ethics Cmsn — FY2025 expenditures

## At a glance

Government Ethics Cmsn (agency code 199, recorded upstream as `GOVERNMENT ETHICS CMSN`) spent **$696,465.11** in fiscal year 2025, across 45 transaction records. That is down 18.8% from $858,176.49 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **64 of 80** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $254,045.00 (36.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $254,045.00 | 36.5% | 1 |
| 4315 | It Professional Services | $170,473.00 | 24.5% | 2 |
| 4650 | Other Services And Supplies | $71,545.80 | 10.3% | 2 |
| 4425 | Lease Payments & Taxes | $61,888.53 | 8.9% | 1 |
| 4225 | State Government Service Charges | $43,395.92 | 6.2% | 3 |
| 4250 | Data Processing | $41,191.73 | 5.9% | 4 |
| 4715 | It Expendable Property | $21,309.40 | 3.1% | 2 |
| 4300 | Professional Services | $7,484.13 | 1.1% | 3 |
| 4100 | Instate Travel | $7,052.87 | 1.0% | 10 |
| 4200 | Telecomm/Tech Svc And Supplies | $6,720.77 | 1.0% | 3 |
| 4575 | Agency Program Related Svcs & Supp | $5,626.23 | 0.8% | 1 |
| 4175 | Office Expenses | $2,283.84 | 0.3% | 3 |
| 4150 | Employee Training | $2,080.02 | 0.3% | 7 |
| 4700 | Expendable Property $250-$5000 | $632.80 | 0.1% | 1 |
| 3110 | Class/Unclass Salary & Per Diem | $399.02 | 0.1% | 1 |
| 4275 | Publicity & Publications | $336.05 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 26 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $254,045.00 | 36.5% |
| 4515 | Professional Services Application Maint | $160,700.00 | 23.1% |
| 4701 | Other Services | $71,545.80 | 10.3% |
| 4800 | Interagency Lease Payments | $61,888.53 | 8.9% |
| 4600 | State Government Service Charges | $43,395.92 | 6.2% |
| 4367 | Computer Technology Pc Support | $24,896.00 | 3.6% |
| 4375 | Computer Technology Computer Processing | $16,295.73 | 2.3% |
| 4366 | Computer Technology Pc Software<$5K | $15,115.07 | 2.2% |
| 4513 | Professional Services Application New | $9,773.00 | 1.4% |
| 4500 | Professional Services Non-It | $7,484.13 | 1.1% |
| 4365 | Computer Technology Pc Equipment<$5K | $6,194.33 | 0.9% |
| 4301 | Telecom/Voice Usage | $5,735.74 | 0.8% |

## Curator notes

Figures are aggregated from 45 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='199' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


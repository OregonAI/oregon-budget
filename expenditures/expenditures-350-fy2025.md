---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-350-fy2025
title: Columbia River Gorge Cmsn — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 350, FY2025
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5e9f0c30287913ac0bfff8d74a1225d0c2816ca6a307f2141ebb35602c5a91ed
snapshot_policy: hash-only
source_data_file: data/expenditures/expenditures-2025.parquet
status: current
content_mode: summary
last_verified: ''
verified_by: ''
maintainer: '@dzinck'
conversion_notes: Title is the source agency name title-cased for reading; the verbatim string is `agency_name`.
  Abbreviations are not expanded. Figures are aggregated, not extracted text.
relationships:
  implements: []
  implemented_by: []
  references_external: []
  related:
  - expenditures-350-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-350
- columbia-river-gorge-cmsn
agency_code: '350'
agency_name: COLUMBIA RIVER GORGE CMSN
fiscal_year: 2025
total_expense: '1100669.06'
transaction_count: 18
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Columbia River Gorge Cmsn — FY2025 expenditures

## At a glance

Columbia River Gorge Cmsn (agency code 350, recorded upstream as `COLUMBIA RIVER GORGE CMSN`) spent **$1,100,669.06** in fiscal year 2025, across 18 transaction records. That is up 13.2% from $972,087.17 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **62 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $942,702.92 (85.6% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $1,100,669.06 | 100.0% | 11 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4300 | Professional Services | Services and supplies | $942,702.92 | 85.6% | 1 |
| 4225 | State Government Service Charges | Services and supplies | $150,335.67 | 13.7% | 2 |
| 4325 | Attorney General Legal Fees | Services and supplies | $4,620.00 | 0.4% | 1 |
| 4425 | Lease Payments & Taxes | Services and supplies | $845.51 | 0.1% | 1 |
| 4250 | Data Processing | Services and supplies | $705.43 | 0.1% | 1 |
| 4100 | Instate Travel | Services and supplies | $591.58 | 0.1% | 1 |
| 4650 | Other Services And Supplies | Services and supplies | $439.02 | 0.0% | 2 |
| 4125 | Out-Of-State Travel | Services and supplies | $257.86 | 0.0% | 6 |
| 4575 | Agency Program Related Svcs & Supp | Services and supplies | $100.05 | 0.0% | 1 |
| 4275 | Publicity & Publications | Services and supplies | $53.80 | 0.0% | 1 |
| 4175 | Office Expenses | Services and supplies | $17.22 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 13 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $942,702.92 | 85.6% |
| 4600 | State Government Service Charges | $150,335.67 | 13.7% |
| 4550 | Attorney General Legal Fees | $4,620.00 | 0.4% |
| 4800 | Interagency Lease Payments | $845.51 | 0.1% |
| 4375 | Computer Technology Computer Processing | $705.43 | 0.1% |
| 4106 | Instate Lodging | $591.58 | 0.1% |
| 4255 | Prizes And Awards | $368.00 | 0.0% |
| 4164 | Out-Of-State Mileage Reimb-Volunteers | $239.86 | 0.0% |
| 4977 | Agency Program Related Reimbursements | $100.05 | 0.0% |
| 4704 | Other Supplies | $71.02 | 0.0% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $53.80 | 0.0% |
| 4160 | Out-Of-State Ground Transportation | $18.00 | 0.0% |

## Largest vendors

The 8 largest of 8 payees this agency recorded payments to in FY2025, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| COLUMBIA RIVER GORGE COMMISSION | $1,089,620.59 | 99.0% | 2 |
| STATE OF OREGON DEPARTMENT OF JUSTICE | $4,620.00 | 0.4% | 1 |
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $3,418.00 | 0.3% | 1 |
| US BANK CORPORATE PAYMENT SYSTEMS | $2,610.57 | 0.2% | 5 |
| CARINA MILLER | $149.38 | 0.0% | 2 |
| PRINT IT INC | $142.04 | 0.0% | 3 |
| ASHLEY THOMSON | $66.30 | 0.0% | 2 |
| JAMES MORGAN | $42.18 | 0.0% | 2 |

## Curator notes

Figures are aggregated from 18 vendor-level transaction records covering 8 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='350' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


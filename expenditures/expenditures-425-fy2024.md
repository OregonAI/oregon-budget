---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-425-fy2024
title: Indian Services Cmsn — FY2024 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 425, FY2024
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: decef95a644d748f5c62eca57f2ec65a1ac01802ec192ae6fe9a4da7eed2a7c0
snapshot_policy: hash-only
source_data_file: data/expenditures/expenditures-2024.parquet
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
  - expenditures-425-fy2023
  - expenditures-425-fy2025
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2024
- agency-425
- indian-services-cmsn
agency_code: '425'
agency_name: INDIAN SERVICES CMSN
fiscal_year: 2024
total_expense: '41851.33'
transaction_count: 33
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Indian Services Cmsn — FY2024 expenditures

## At a glance

Indian Services Cmsn (agency code 425, recorded upstream as `INDIAN SERVICES CMSN`) spent **$41,851.33** in fiscal year 2024, across 33 transaction records. That is up 101.8% from $20,738.25 in FY2023. The agency accounts for 0.00% of the $31,836,364,350.07 in statewide agency spending recorded for FY2024, ranking **80 of 80** agencies reporting that year.

The largest budget category was **It Expendable Property** at $15,778.33 (37.7% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $41,851.33 | 100.0% | 10 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4715 | It Expendable Property | Services and supplies | $15,778.33 | 37.7% | 3 |
| 4225 | State Government Service Charges | Services and supplies | $12,783.73 | 30.5% | 3 |
| 4100 | Instate Travel | Services and supplies | $7,116.49 | 17.0% | 12 |
| 4150 | Employee Training | Services and supplies | $2,451.63 | 5.9% | 6 |
| 4200 | Telecomm/Tech Svc And Supplies | Services and supplies | $1,951.16 | 4.7% | 1 |
| 4250 | Data Processing | Services and supplies | $477.54 | 1.1% | 1 |
| 4500 | Food And Kitchen Supplies | Services and supplies | $366.00 | 0.9% | 2 |
| 4650 | Other Services And Supplies | Services and supplies | $352.97 | 0.8% | 1 |
| 4175 | Office Expenses | Services and supplies | $297.95 | 0.7% | 3 |
| 4700 | Expendable Property $250-$5000 | Services and supplies | $275.53 | 0.7% | 1 |

## Largest expenditure classes

The 12 largest of 19 expenditure classes used by this agency in FY2024.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $12,783.73 | 30.5% |
| 4366 | Computer Technology Pc Software<$5K | $12,668.93 | 30.3% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $4,887.70 | 11.7% |
| 4365 | Computer Technology Pc Equipment<$5K | $3,109.40 | 7.4% |
| 4301 | Telecom/Voice Usage | $1,951.16 | 4.7% |
| 4106 | Instate Lodging | $1,854.66 | 4.4% |
| 4437 | Prof Dev Dues/Membership | $902.00 | 2.2% |
| 4406 | Prof Dev Instate Tuition/Registration | $608.76 | 1.5% |
| 4450 | Prof Dev Instate Mile Reimb-Full Rate | $587.18 | 1.4% |
| 4367 | Computer Technology Pc Support | $477.54 | 1.1% |
| 4875 | Food And Kitchen Supplies | $366.00 | 0.9% |
| 4433 | Prof Dev Instate Lodging | $353.69 | 0.8% |

## Largest vendors

The 10 largest of 10 payees this agency recorded payments to in FY2024, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $23,925.48 | 57.2% | 2 |
| ELISSA BULLION | $6,742.09 | 16.1% | 13 |
| CDW GOVERNMENT INC | $3,586.94 | 8.6% | 2 |
| PATRICK A FLANAGAN | $3,457.31 | 8.3% | 8 |
| VERIZON WIRELESS | $1,951.16 | 4.7% | 1 |
| STATE OF OREGON SECRETARY OF STATE | $1,223.25 | 2.9% | 1 |
| ADRIENNE FISCHER | $593.50 | 1.4% | 3 |
| SHI INTERNATIONAL CORP | $268.93 | 0.6% | 1 |
| OREGON CORRECTIONS ENTERPRISES | $67.67 | 0.2% | 1 |
| OREGON GOVERNMENT ETHICS COMMISSION | $35.00 | 0.1% | 1 |

## Curator notes

Figures are aggregated from 33 vendor-level transaction records covering 10 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='425' AND fiscal_year='2024'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2024.parquet`, the file these figures were computed from.


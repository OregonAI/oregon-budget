---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-425-fy2025
title: Indian Services Cmsn — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 425, FY2025
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
  - expenditures-425-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-425
- indian-services-cmsn
agency_code: '425'
agency_name: INDIAN SERVICES CMSN
fiscal_year: 2025
total_expense: '23671.22'
transaction_count: 27
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Indian Services Cmsn — FY2025 expenditures

## At a glance

Indian Services Cmsn (agency code 425, recorded upstream as `INDIAN SERVICES CMSN`) spent **$23,671.22** in fiscal year 2025, across 27 transaction records. That is down 43.4% from $41,851.33 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **80 of 80** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $11,966.97 (50.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | $11,966.97 | 50.6% | 3 |
| 4100 | Instate Travel | $5,057.26 | 21.4% | 10 |
| 4150 | Employee Training | $2,319.98 | 9.8% | 6 |
| 4715 | It Expendable Property | $1,883.34 | 8.0% | 3 |
| 4200 | Telecomm/Tech Svc And Supplies | $1,859.79 | 7.9% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $406.20 | 1.7% | 2 |
| 4175 | Office Expenses | $162.68 | 0.7% | 1 |
| 4650 | Other Services And Supplies | $15.00 | 0.1% | 1 |

## Largest expenditure classes

The 12 largest of 17 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $11,966.97 | 50.6% |
| 4109 | Instate Mileage Reimbursement-Full Rate | $3,832.34 | 16.2% |
| 4301 | Telecom/Voice Usage | $1,859.79 | 7.9% |
| 4106 | Instate Lodging | $1,122.83 | 4.7% |
| 4450 | Prof Dev Instate Mile Reimb-Full Rate | $998.28 | 4.2% |
| 4316 | Telecom/Teleconference Equipment<$5K | $964.65 | 4.1% |
| 4437 | Prof Dev Dues/Membership | $703.00 | 3.0% |
| 4366 | Computer Technology Pc Software<$5K | $600.00 | 2.5% |
| 4433 | Prof Dev Instate Lodging | $496.35 | 2.1% |
| 4976 | Agency Program Related Supplies | $406.20 | 1.7% |
| 4365 | Computer Technology Pc Equipment<$5K | $318.69 | 1.3% |
| 4200 | Office Supplies | $162.68 | 0.7% |

## Largest vendors

The 12 largest of 12 payees this agency recorded payments to in FY2025, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $11,923.22 | 50.4% | 2 |
| ELISSA BULLION | $4,443.04 | 18.8% | 7 |
| PATRICK A FLANAGAN | $2,561.78 | 10.8% | 7 |
| VERIZON WIRELESS | $1,859.79 | 7.9% | 1 |
| CDW GOVERNMENT INC | $964.65 | 4.1% | 1 |
| ADRIENNE FISCHER | $637.62 | 2.7% | 3 |
| STATE OF OREGON SECRETARY OF STATE | $608.75 | 2.6% | 1 |
| SHI INTERNATIONAL CORP | $318.69 | 1.3% | 1 |
| SISTERS DEPOT LLC | $220.20 | 0.9% | 1 |
| COQUILLE INDIAN TRIBE | $83.48 | 0.4% | 1 |
| OREGON GOVERNMENT ETHICS COMMISSION | $35.00 | 0.1% | 1 |
| OREGON PUBLIC EMPLOYEES RETIREMENT SYSTEM | $15.00 | 0.1% | 1 |

## Curator notes

Figures are aggregated from 27 vendor-level transaction records covering 12 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='425' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


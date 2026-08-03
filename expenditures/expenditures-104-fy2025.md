---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-104-fy2025
title: Public Records Advocate, Office of — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 104, FY2025
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5e9f0c30287913ac0bfff8d74a1225d0c2816ca6a307f2141ebb35602c5a91ed
snapshot_policy: hash-only
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
  - expenditures-104-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-104
- public-records-advocate-office-of
agency_code: '104'
agency_name: PUBLIC RECORDS ADVOCATE, OFFICE OF
fiscal_year: 2025
total_expense: '49580.73'
transaction_count: 13
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Public Records Advocate, Office of — FY2025 expenditures

## At a glance

Public Records Advocate, Office of (agency code 104, recorded upstream as `PUBLIC RECORDS ADVOCATE, OFFICE OF`) spent **$49,580.73** in fiscal year 2025, across 13 transaction records. That is up 4.0% from $47,687.22 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **79 of 80** agencies reporting that year.

The largest budget category was **Other Services And Supplies** at $20,904.80 (42.2% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $49,580.73 | 100.0% | 7 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4650 | Other Services And Supplies | Services and supplies | $20,904.80 | 42.2% | 1 |
| 4225 | State Government Service Charges | Services and supplies | $20,148.00 | 40.6% | 3 |
| 4250 | Data Processing | Services and supplies | $5,935.38 | 12.0% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | Services and supplies | $1,411.04 | 2.8% | 2 |
| 4150 | Employee Training | Services and supplies | $728.00 | 1.5% | 1 |
| 4715 | It Expendable Property | Services and supplies | $261.18 | 0.5% | 2 |
| 4300 | Professional Services | Services and supplies | $192.33 | 0.4% | 2 |

## Largest expenditure classes

The 10 largest of 10 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4701 | Other Services | $20,904.80 | 42.2% |
| 4600 | State Government Service Charges | $20,148.00 | 40.6% |
| 4367 | Computer Technology Pc Support | $5,532.00 | 11.2% |
| 4301 | Telecom/Voice Usage | $1,321.40 | 2.7% |
| 4437 | Prof Dev Dues/Membership | $728.00 | 1.5% |
| 4375 | Computer Technology Computer Processing | $403.38 | 0.8% |
| 4500 | Professional Services Non-It | $192.33 | 0.4% |
| 4372 | Computer Technology Peripheral Equip<$5K | $184.23 | 0.4% |
| 4305 | Telecom/Network Services | $89.64 | 0.2% |
| 4366 | Computer Technology Pc Software<$5K | $76.95 | 0.2% |

## Largest vendors

The 7 largest of 7 payees this agency recorded payments to in FY2025, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $47,935.63 | 96.7% | 7 |
| US BANK NATIONAL ASSOCIATION ND | $728.00 | 1.5% | 1 |
| STATE OF OREGON SECRETARY OF STATE | $354.00 | 0.7% | 1 |
| CDW GOVERNMENT INC | $184.23 | 0.4% | 1 |
| CASCADE CENTERS INC | $169.92 | 0.3% | 1 |
| OREGON STATE TREASURY | $132.00 | 0.3% | 1 |
| SHI INTERNATIONAL CORP | $76.95 | 0.2% | 1 |

## Curator notes

Figures are aggregated from 13 vendor-level transaction records covering 7 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='104' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


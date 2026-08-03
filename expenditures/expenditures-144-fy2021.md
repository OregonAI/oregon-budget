---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-144-fy2021
title: Legislative Rev Office — FY2021 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 144, FY2021
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 81c90c241c212dba4cc304dd132bb03379de0003138cc2451899f8f95b1dcc97
snapshot_policy: hash-only
source_data_file: data/expenditures/expenditures-2021.parquet
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
  - expenditures-144-fy2020
  - expenditures-144-fy2022
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2021
- agency-144
- legislative-rev-office
agency_code: '144'
agency_name: LEGISLATIVE REV OFFICE
fiscal_year: 2021
total_expense: '68531.02'
transaction_count: 23
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Legislative Rev Office — FY2021 expenditures

## At a glance

Legislative Rev Office (agency code 144, recorded upstream as `LEGISLATIVE REV OFFICE`) spent **$68,531.02** in fiscal year 2021, across 23 transaction records. That is up 2.7% from $66,705.65 in FY2020. The agency accounts for 0.00% of the $27,010,059,496.47 in statewide agency spending recorded for FY2021, ranking **73 of 76** agencies reporting that year.

The largest budget category was **State Government Service Charges** at $27,007.57 (39.4% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $68,531.02 | 100.0% | 8 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4225 | State Government Service Charges | Services and supplies | $27,007.57 | 39.4% | 3 |
| 4715 | It Expendable Property | Services and supplies | $24,281.83 | 35.4% | 7 |
| 4400 | Dues And Subscriptions | Services and supplies | $10,493.79 | 15.3% | 4 |
| 4175 | Office Expenses | Services and supplies | $4,129.57 | 6.0% | 5 |
| 4275 | Publicity & Publications | Services and supplies | $2,560.00 | 3.7% | 1 |
| 4150 | Employee Training | Services and supplies | $36.36 | 0.1% | 1 |
| 4650 | Other Services And Supplies | Services and supplies | $15.00 | 0.0% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | Services and supplies | $6.90 | 0.0% | 1 |

## Largest expenditure classes

The 11 largest of 11 expenditure classes used by this agency in FY2021.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4600 | State Government Service Charges | $27,007.57 | 39.4% |
| 4366 | Computer Technology Pc Software<$5K | $21,808.70 | 31.8% |
| 4251 | Subscriptions And Publications | $10,493.79 | 15.3% |
| 4202 | Equipment Rental | $2,669.04 | 3.9% |
| 4253 | Advertise Publicity Publish/Print Srvs | $2,560.00 | 3.7% |
| 4365 | Computer Technology Pc Equipment<$5K | $2,473.13 | 3.6% |
| 4200 | Office Supplies | $1,298.11 | 1.9% |
| 4201 | Office Services | $162.42 | 0.2% |
| 4426 | Prof Dev Training Materials | $36.36 | 0.1% |
| 4701 | Other Services | $15.00 | 0.0% |
| 4315 | Telecom/Teleconference Usage | $6.90 | 0.0% |

## Largest vendors

The 16 largest of 16 payees this agency recorded payments to in FY2021, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $24,796.07 | 36.2% | 1 |
| SAS INSTITUTE INC | $16,772.50 | 24.5% | 1 |
| CCH INCORPORATED | $9,392.70 | 13.7% | 2 |
| US BANK NATIONAL ASSOCIATION ND | $5,411.82 | 7.9% | 5 |
| PACIFIC OFFICE AUTOMATION INC | $2,831.46 | 4.1% | 2 |
| GAMS DEVELOPMENT CORPORATION | $2,560.00 | 3.7% | 1 |
| STATE OF OREGON SECRETARY OF STATE | $2,127.00 | 3.1% | 1 |
| IMPLAN GROUP LLC | $1,500.00 | 2.2% | 1 |
| SHI INTERNATIONAL CORP | $976.20 | 1.4% | 1 |
| CDW GOVERNMENT INC | $702.74 | 1.0% | 1 |
| SIERRA SPRINGS | $449.01 | 0.7% | 1 |
| LEGISLATIVE ADMIN COMMITTEE | $420.04 | 0.6% | 2 |
| MICROSOFT CORPORATION | $351.98 | 0.5% | 1 |
| UNIVERSITY OF ILLINOIS | $140.00 | 0.2% | 1 |
| OREGON GOVERNMENT ETHICS COMMISSION | $84.50 | 0.1% | 1 |
| OREGON PUBLIC EMPLOYEES RETIREMENT SYSTEM | $15.00 | 0.0% | 1 |

## Curator notes

Figures are aggregated from 23 vendor-level transaction records covering 16 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='144' AND fiscal_year='2021'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2021.parquet`, the file these figures were computed from.


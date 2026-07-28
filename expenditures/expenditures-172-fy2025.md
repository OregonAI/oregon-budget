---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-172-fy2025
title: Facilites Auth, Oregon — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 172, FY2025
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
  - expenditures-172-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-172
- facilites-auth-oregon
agency_code: '172'
agency_name: FACILITES AUTH, OREGON
fiscal_year: 2025
total_expense: '209463.71'
transaction_count: 9
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Facilites Auth, Oregon — FY2025 expenditures

## At a glance

Facilites Auth, Oregon (agency code 172, recorded upstream as `FACILITES AUTH, OREGON`) spent **$209,463.71** in fiscal year 2025, across 9 transaction records. That is down 26.6% from $285,405.94 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **74 of 80** agencies reporting that year.

The largest budget category was **Professional Services** at $196,367.83 (93.7% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $196,367.83 | 93.7% | 6 |
| 4325 | Attorney General Legal Fees | $12,430.00 | 5.9% | 1 |
| 4275 | Publicity & Publications | $478.88 | 0.2% | 1 |
| 4225 | State Government Service Charges | $187.00 | 0.1% | 1 |

## Largest expenditure classes

The 4 largest of 4 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $196,367.83 | 93.7% |
| 4550 | Attorney General Legal Fees | $12,430.00 | 5.9% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $478.88 | 0.2% |
| 4600 | State Government Service Charges | $187.00 | 0.1% |

## Largest vendors

The 8 largest of 8 payees this agency recorded payments to in FY2025, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| TONKON TORP LLP | $142,137.83 | 67.9% | 1 |
| OREGON STATE TREASURY | $48,187.00 | 23.0% | 2 |
| STATE OF OREGON DEPARTMENT OF JUSTICE | $12,430.00 | 5.9% | 1 |
| NCHFFA | $3,250.00 | 1.6% | 1 |
| SPERRY CAPITAL INC | $2,000.00 | 1.0% | 1 |
| FIRST TRYON ADVISORS | $800.00 | 0.4% | 1 |
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $478.88 | 0.2% | 1 |
| WILLIAM GRANT WADHAMS | $180.00 | 0.1% | 1 |

## Curator notes

Figures are aggregated from 9 vendor-level transaction records covering 8 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='172' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


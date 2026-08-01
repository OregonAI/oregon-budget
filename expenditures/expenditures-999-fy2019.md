---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-999-fy2019
title: Cntrl Agy/St General Fund/B-Up Wh — FY2019 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 999, FY2019
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 3900810723066d4651c7227ef0c74a8b9c41ff76c2e4bcebbbb6f2268e443d34
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
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2019
- agency-999
- cntrl-agy-st-general-fund-b-up-wh
agency_code: '999'
agency_name: CNTRL AGY/ST GENERAL FUND/B-UP WH
fiscal_year: 2019
total_expense: '1946.74'
transaction_count: 2
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Cntrl Agy/St General Fund/B-Up Wh — FY2019 expenditures

## At a glance

Cntrl Agy/St General Fund/B-Up Wh (agency code 999, recorded upstream as `CNTRL AGY/ST GENERAL FUND/B-UP WH`) spent **$1,946.74** in fiscal year 2019, across 2 transaction records. FY2018 is outside the range this dataset covers. The agency accounts for 0.00% of the $20,745,841,274.19 in statewide agency spending recorded for FY2019, ranking **78 of 78** agencies reporting that year.

The largest budget category was **Default** at $1,946.74 (100.0% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Reversions | $1,946.74 | 100.0% | 1 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 9999 | Default | Reversions | $1,946.74 | 100.0% | 2 |

## Largest expenditure classes

The 1 largest of 1 expenditure classes used by this agency in FY2019.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4045 | Tan Costs | $1,946.74 | 100.0% |

## Largest vendors

The 2 largest of 2 payees this agency recorded payments to in FY2019, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| HAWKINS DELAFIELD & WOOD | $1,500.00 | 77.1% | 1 |
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $446.74 | 22.9% | 1 |

## Curator notes

Figures are aggregated from 2 vendor-level transaction records covering 2 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='999' AND fiscal_year='2019'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2019.parquet`, the file these figures were computed from.


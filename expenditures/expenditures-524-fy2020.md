---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-524-fy2020
title: Chief Edu Office — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 524, FY2020
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: b73d59a16a10ad7f6ae4f4b415cba8d78894a3ead0e3928fe994cc49b9b11284
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
  - expenditures-524-fy2019
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-524
- chief-edu-office
agency_code: '524'
agency_name: CHIEF EDU OFFICE
fiscal_year: 2020
total_expense: '26057.96'
transaction_count: 8
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Chief Edu Office — FY2020 expenditures

## At a glance

Chief Edu Office (agency code 524, recorded upstream as `CHIEF EDU OFFICE`) spent **$26,057.96** in fiscal year 2020, across 8 transaction records. That is down 98.6% from $1,902,400.10 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **76 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $24,000.00 (92.1% of the agency's total).

## Spending by band

The leading digit of a budget class encodes its category. This grouping is a convention of Oregon's budget structure, not a line in the source data — see [the account code reference](../datasets/account-code-structure.md).

| Band | Amount | Share | Codes |
|---|---:|---:|---:|
| Services and supplies | $26,057.96 | 100.0% | 5 |

## Spending by budget class

| Code | Budget class | Band | Amount | Share | Records |
|---|---|---|---:|---:|---:|
| 4300 | Professional Services | Services and supplies | $24,000.00 | 92.1% | 1 |
| 4175 | Office Expenses | Services and supplies | $692.52 | 2.7% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | Services and supplies | $681.81 | 2.6% | 3 |
| 4650 | Other Services And Supplies | Services and supplies | $643.53 | 2.5% | 1 |
| 4225 | State Government Service Charges | Services and supplies | $40.10 | 0.2% | 1 |

## Largest expenditure classes

The 6 largest of 6 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $24,000.00 | 92.1% |
| 4301 | Telecom/Voice Usage | $681.81 | 2.6% |
| 4202 | Equipment Rental | $646.52 | 2.5% |
| 4701 | Other Services | $643.53 | 2.5% |
| 4201 | Office Services | $46.00 | 0.2% |
| 4600 | State Government Service Charges | $40.10 | 0.2% |

## Largest vendors

The 6 largest of 6 payees this agency recorded payments to in FY2020, accounting for 100.0% of its spending. Names are reproduced exactly as the state records them.

| Vendor | Amount | Share | Records |
|---|---:|---:|---:|
| PORTLAND STATE UNIVERSITY | $24,000.00 | 92.1% | 1 |
| DEPARTMENT OF ADMINISTRATIVE SERVICES | $945.99 | 3.6% | 3 |
| RICOH USA INC | $646.52 | 2.5% | 1 |
| IBM CORPORATION | $229.06 | 0.9% | 1 |
| AT&T MOBILITY | $196.29 | 0.8% | 1 |
| OREGON STATE TREASURY | $40.10 | 0.2% | 1 |

## Curator notes

Figures are aggregated from 8 vendor-level transaction records covering 6 distinct payees. The vendor table above is the state's own published data, reproduced rather than summarised: a payee string is whatever was entered in the statewide financial system, so the same organisation can appear under several spellings and is not de-duplicated here. Treating each row as a distinct organisation will undercount the large ones.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='524' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


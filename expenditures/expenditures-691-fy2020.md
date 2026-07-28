---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-691-fy2020
title: Watershed Enh Brd — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 691, FY2020
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
  - expenditures-691-fy2019
  - expenditures-691-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-691
- watershed-enh-brd
agency_code: '691'
agency_name: WATERSHED ENH BRD
fiscal_year: 2020
total_expense: '49924915.44'
transaction_count: 432
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Watershed Enh Brd — FY2020 expenditures

## At a glance

Watershed Enh Brd (agency code 691, recorded upstream as `WATERSHED ENH BRD`) spent **$49,924,915.44** in fiscal year 2020, across 432 transaction records. That is up 16.2% from $42,966,528.19 in FY2019. The agency accounts for 0.21% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **24 of 77** agencies reporting that year.

The largest budget category was **Distribution To Non-Governments** at $27,724,496.29 (55.5% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 6030 | Distribution To Non-Governments | $27,724,496.29 | 55.5% | 119 |
| 6025 | Distribution To Other Govts | $14,301,751.21 | 28.6% | 69 |
| 6635 | Dist To Fish And Wildlife | $6,984,155.25 | 14.0% | 1 |
| 4300 | Professional Services | $156,884.59 | 0.3% | 8 |
| 4425 | Facilities Rent & Taxes | $141,280.47 | 0.3% | 19 |
| 4225 | State Government Service Charges | $140,372.54 | 0.3% | 5 |
| 6690 | Dist To Water Resources | $89,648.48 | 0.2% | 1 |
| 6048 | Special Payment To Public Universities | $74,966.26 | 0.2% | 1 |
| 4325 | Attorney General Legal Fees | $69,255.22 | 0.1% | 1 |
| 4100 | Instate Travel | $45,407.20 | 0.1% | 103 |
| 4575 | Agency Program Related Svcs & Supp | $39,218.71 | 0.1% | 2 |
| 4650 | Other Services And Supplies | $32,327.04 | 0.1% | 12 |
| 4250 | Data Processing | $23,738.75 | 0.0% | 5 |
| 6580 | Dist To Higher Education | $23,385.21 | 0.0% | 1 |
| 4175 | Office Expenses | $23,082.10 | 0.0% | 12 |
| 4200 | Telecomm/Tech Svc And Supplies | $19,779.30 | 0.0% | 7 |
| 4150 | Employee Training | $15,392.80 | 0.0% | 37 |
| 4715 | It Expendable Property | $6,933.12 | 0.0% | 4 |
| 4125 | Out-Of-State Travel | $5,538.07 | 0.0% | 11 |
| 4275 | Publicity & Publications | $4,114.33 | 0.0% | 11 |
| 4400 | Dues And Subscriptions | $3,188.50 | 0.0% | 3 |

## Largest expenditure classes

The 12 largest of 52 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 6725 | Distribution To Non-Governments | $26,886,161.29 | 53.9% |
| 6700 | Distribution To Other Governments | $14,301,751.21 | 28.6% |
| 6179 | Distribution To Fish And Wildlife | $6,984,155.25 | 14.0% |
| 6826 | Payments To Non-Governments | $838,335.00 | 1.7% |
| 4500 | Professional Services Non-It | $156,884.59 | 0.3% |
| 4800 | Facilities Rent | $141,280.47 | 0.3% |
| 4600 | State Government Service Charges | $140,372.54 | 0.3% |
| 6451 | Distribution To Oregon State University | $98,351.47 | 0.2% |
| 6181 | Distribution To Water Resources | $89,648.48 | 0.2% |
| 4550 | Attorney General Legal Fees | $69,255.22 | 0.1% |
| 4975 | Agency Program Related Services | $39,218.71 | 0.1% |
| 4704 | Other Supplies | $23,783.51 | 0.0% |

## Curator notes

Figures are aggregated from 432 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='691' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


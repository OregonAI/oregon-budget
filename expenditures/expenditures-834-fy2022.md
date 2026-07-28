---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-834-fy2022
title: Dentistry, Brd of — FY2022 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 834, FY2022
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 5378b32aad5d54d03160dd49832cc5c4f45e517dde8ba96c7e5b8bbb6e3a99f4
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
  - expenditures-834-fy2021
  - expenditures-834-fy2023
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2022
- agency-834
- dentistry-brd-of
agency_code: '834'
agency_name: DENTISTRY, BRD OF
fiscal_year: 2022
total_expense: '611765.45'
transaction_count: 87
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dentistry, Brd of — FY2022 expenditures

## At a glance

Dentistry, Brd of (agency code 834, recorded upstream as `DENTISTRY, BRD OF`) spent **$611,765.45** in fiscal year 2022, across 87 transaction records. That is down 0.6% from $615,550.82 in FY2021. The agency accounts for 0.00% of the $30,846,521,641.15 in statewide agency spending recorded for FY2022, ranking **60 of 76** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $159,214.45 (26.0% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $159,214.45 | 26.0% | 1 |
| 4300 | Professional Services | $121,066.06 | 19.8% | 10 |
| 4425 | Lease Payments & Taxes | $72,926.97 | 11.9% | 5 |
| 4250 | Data Processing | $43,337.99 | 7.1% | 5 |
| 4225 | State Government Service Charges | $41,746.42 | 6.8% | 4 |
| 4715 | It Expendable Property | $40,923.64 | 6.7% | 3 |
| 4650 | Other Services And Supplies | $39,793.47 | 6.5% | 7 |
| 4175 | Office Expenses | $27,490.04 | 4.5% | 12 |
| 4575 | Agency Program Related Svcs & Supp | $22,732.39 | 3.7% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $14,335.89 | 2.3% | 8 |
| 4100 | Instate Travel | $12,654.14 | 2.1% | 19 |
| 4150 | Employee Training | $7,090.54 | 1.2% | 3 |
| 4400 | Dues And Subscriptions | $5,448.78 | 0.9% | 4 |
| 4315 | It Professional Services | $1,800.00 | 0.3% | 1 |
| 4275 | Publicity & Publications | $1,204.67 | 0.2% | 3 |

## Largest expenditure classes

The 12 largest of 33 expenditure classes used by this agency in FY2022.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $159,214.45 | 26.0% |
| 4500 | Professional Services Non-It | $121,066.06 | 19.8% |
| 4600 | State Government Service Charges | $41,746.42 | 6.8% |
| 4375 | Computer Technology Computer Processing | $40,177.99 | 6.6% |
| 7007 | Lease Pmt For Buildings | $32,759.52 | 5.4% |
| 4366 | Computer Technology Pc Software<$5K | $29,400.97 | 4.8% |
| 4800 | Interagency Lease Payments | $26,599.89 | 4.3% |
| 4730 | Merchant Fees | $23,371.61 | 3.8% |
| 4975 | Agency Program Related Services | $17,034.25 | 2.8% |
| 4701 | Other Services | $16,421.86 | 2.7% |
| 7401 | Interest-Leased Assets | $13,567.56 | 2.2% |
| 4200 | Office Supplies | $13,509.21 | 2.2% |

## Curator notes

Figures are aggregated from 87 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='834' AND fiscal_year='2022'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2022.parquet`, the file these figures were computed from.


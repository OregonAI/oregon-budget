---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-834-fy2023
title: Dentistry, Brd of — FY2023 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 834, FY2023
issuing_body: Oregon Department of Administrative Services
source_url: https://data.oregon.gov/d/y9g9-xsxs
source_format: soda
retrieved: '2026-07-28'
source_sha256: 6400163010ab2f341831c864272a89c5e9f2a261fad3fd9572b230042f26e3d5
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
  - expenditures-834-fy2022
  - expenditures-834-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2023
- agency-834
- dentistry-brd-of
agency_code: '834'
agency_name: DENTISTRY, BRD OF
fiscal_year: 2023
total_expense: '642345.27'
transaction_count: 97
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Dentistry, Brd of — FY2023 expenditures

## At a glance

Dentistry, Brd of (agency code 834, recorded upstream as `DENTISTRY, BRD OF`) spent **$642,345.27** in fiscal year 2023, across 97 transaction records. That is up 5.0% from $611,765.45 in FY2022. The agency accounts for 0.00% of the $30,726,070,119.27 in statewide agency spending recorded for FY2023, ranking **61 of 77** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $126,005.54 (19.6% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $126,005.54 | 19.6% | 1 |
| 4300 | Professional Services | $120,185.05 | 18.7% | 7 |
| 4425 | Lease Payments & Taxes | $94,970.46 | 14.8% | 2 |
| 4650 | Other Services And Supplies | $73,179.34 | 11.4% | 6 |
| 4250 | Data Processing | $70,445.82 | 11.0% | 5 |
| 4225 | State Government Service Charges | $33,083.77 | 5.2% | 4 |
| 4715 | It Expendable Property | $30,202.10 | 4.7% | 3 |
| 4175 | Office Expenses | $27,149.68 | 4.2% | 14 |
| 4575 | Agency Program Related Svcs & Supp | $24,075.69 | 3.7% | 2 |
| 4200 | Telecomm/Tech Svc And Supplies | $16,251.30 | 2.5% | 5 |
| 4150 | Employee Training | $13,190.66 | 2.1% | 20 |
| 4100 | Instate Travel | $6,529.65 | 1.0% | 22 |
| 4400 | Dues And Subscriptions | $4,239.89 | 0.7% | 3 |
| 4275 | Publicity & Publications | $2,836.32 | 0.4% | 3 |

## Largest expenditure classes

The 12 largest of 37 expenditure classes used by this agency in FY2023.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $126,005.54 | 19.6% |
| 4500 | Professional Services Non-It | $120,185.05 | 18.7% |
| 7007 | Lease Pmt For Buildings | $69,352.44 | 10.8% |
| 4375 | Computer Technology Computer Processing | $59,615.82 | 9.3% |
| 4701 | Other Services | $48,098.16 | 7.5% |
| 4600 | State Government Service Charges | $33,083.77 | 5.2% |
| 4366 | Computer Technology Pc Software<$5K | $29,986.32 | 4.7% |
| 7401 | Interest-Leased Assets | $25,618.02 | 4.0% |
| 4730 | Merchant Fees | $25,081.18 | 3.9% |
| 4975 | Agency Program Related Services | $20,726.25 | 3.2% |
| 4200 | Office Supplies | $13,637.24 | 2.1% |
| 4367 | Computer Technology Pc Support | $10,830.00 | 1.7% |

## Curator notes

Figures are aggregated from 97 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='834' AND fiscal_year='2023'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2023.parquet`, the file these figures were computed from.


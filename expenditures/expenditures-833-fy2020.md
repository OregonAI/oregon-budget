---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-833-fy2020
title: Health Related Licensing Brds — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 833, FY2020
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
  - expenditures-833-fy2019
  - expenditures-833-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-833
- health-related-licensing-brds
agency_code: '833'
agency_name: HEALTH RELATED LICENSING BRDs
fiscal_year: 2020
total_expense: '1159296.99'
transaction_count: 482
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Health Related Licensing Brds — FY2020 expenditures

## At a glance

Health Related Licensing Brds (agency code 833, recorded upstream as `HEALTH RELATED LICENSING BRDs`) spent **$1,159,296.99** in fiscal year 2020, across 482 transaction records. That is up 15.6% from $1,003,016.85 in FY2019. The agency accounts for 0.00% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **53 of 77** agencies reporting that year.

The largest budget category was **Agency Program Related Svcs & Supp** at $299,309.62 (25.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4575 | Agency Program Related Svcs & Supp | $299,309.62 | 25.8% | 105 |
| 4325 | Attorney General Legal Fees | $204,233.01 | 17.6% | 6 |
| 4650 | Other Services And Supplies | $158,257.90 | 13.7% | 29 |
| 4425 | Facilities Rent & Taxes | $119,582.10 | 10.3% | 6 |
| 4315 | It Professional Services | $80,491.65 | 6.9% | 18 |
| 4225 | State Government Service Charges | $70,354.20 | 6.1% | 24 |
| 4700 | Expendable Property $250-$5000 | $58,145.89 | 5.0% | 4 |
| 4175 | Office Expenses | $42,539.85 | 3.7% | 45 |
| 4100 | Instate Travel | $35,742.53 | 3.1% | 110 |
| 4200 | Telecomm/Tech Svc And Supplies | $27,055.43 | 2.3% | 37 |
| 4300 | Professional Services | $15,014.73 | 1.3% | 21 |
| 3240 | Unemployment Assessment | $8,794.04 | 0.8% | 6 |
| 4275 | Publicity & Publications | $8,383.53 | 0.7% | 13 |
| 4150 | Employee Training | $8,207.15 | 0.7% | 22 |
| 4715 | It Expendable Property | $6,326.58 | 0.5% | 10 |
| 4125 | Out-Of-State Travel | $6,274.59 | 0.5% | 10 |
| 4250 | Data Processing | $5,154.49 | 0.4% | 10 |
| 4475 | Facilities Maintenance | $4,514.70 | 0.4% | 2 |
| 4400 | Dues And Subscriptions | $915.00 | 0.1% | 4 |

## Largest expenditure classes

The 12 largest of 53 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4975 | Agency Program Related Services | $297,029.50 | 25.6% |
| 4550 | Attorney General Legal Fees | $204,233.01 | 17.6% |
| 4800 | Facilities Rent | $119,582.10 | 10.3% |
| 4701 | Other Services | $114,041.47 | 9.8% |
| 4600 | State Government Service Charges | $70,354.20 | 6.1% |
| 4515 | Professional Services Application Maint | $65,116.65 | 5.6% |
| 4999 | Expendable Property Non-It<$5K | $58,145.89 | 5.0% |
| 4730 | Merchant Fees | $43,205.11 | 3.7% |
| 4301 | Telecom/Voice Usage | $20,077.90 | 1.7% |
| 4200 | Office Supplies | $19,344.33 | 1.7% |
| 4201 | Office Services | $18,967.36 | 1.6% |
| 4519 | Professional Serv/Managed Serv Provider | $15,375.00 | 1.3% |

## Curator notes

Figures are aggregated from 482 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='833' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


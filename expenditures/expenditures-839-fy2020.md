---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-839-fy2020
title: Labor & Ind, Bureau of — FY2020 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 839, FY2020
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
  - expenditures-839-fy2019
  - expenditures-839-fy2021
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2020
- agency-839
- labor-ind-bureau-of
agency_code: '839'
agency_name: LABOR & IND, BUREAU OF
fiscal_year: 2020
total_expense: '3351614.10'
transaction_count: 328
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Labor & Ind, Bureau of — FY2020 expenditures

## At a glance

Labor & Ind, Bureau of (agency code 839, recorded upstream as `LABOR & IND, BUREAU OF`) spent **$3,351,614.10** in fiscal year 2020, across 328 transaction records. That is down 8.3% from $3,654,558.77 in FY2019. The agency accounts for 0.01% of the $23,315,251,234.06 in statewide agency spending recorded for FY2020, ranking **42 of 77** agencies reporting that year.

The largest budget category was **Professional Services** at $864,424.05 (25.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4300 | Professional Services | $864,424.05 | 25.8% | 47 |
| 4425 | Facilities Rent & Taxes | $556,990.22 | 16.6% | 5 |
| 4225 | State Government Service Charges | $468,782.34 | 14.0% | 4 |
| 4175 | Office Expenses | $284,188.15 | 8.5% | 46 |
| 4715 | It Expendable Property | $220,341.38 | 6.6% | 12 |
| 4650 | Other Services And Supplies | $126,210.36 | 3.8% | 22 |
| 6100 | Distribution To Dept Of Human Services | $119,602.07 | 3.6% | 1 |
| 4575 | Agency Program Related Svcs & Supp | $116,295.13 | 3.5% | 4 |
| 4325 | Attorney General Legal Fees | $111,209.08 | 3.3% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $86,562.07 | 2.6% | 7 |
| 4315 | It Professional Services | $82,045.50 | 2.4% | 2 |
| 4250 | Data Processing | $76,906.62 | 2.3% | 10 |
| 4100 | Instate Travel | $76,246.33 | 2.3% | 119 |
| 4600 | Intra-Inter Agency Charges | $39,238.45 | 1.2% | 1 |
| 4400 | Dues And Subscriptions | $29,945.67 | 0.9% | 11 |
| 5550 | Data Processing Software | $22,391.24 | 0.7% | 1 |
| 6035 | Distribution To Individuals | $22,155.25 | 0.7% | 4 |
| 4125 | Out-Of-State Travel | $20,193.53 | 0.6% | 17 |
| 3240 | Unemployment Assessment | $14,547.49 | 0.4% | 1 |
| 4700 | Expendable Property $250-$5000 | $6,408.50 | 0.2% | 5 |
| 4150 | Employee Training | $6,281.88 | 0.2% | 6 |
| 4275 | Publicity & Publications | $518.79 | 0.0% | 1 |
| 4475 | Facilities Maintenance | $130.00 | 0.0% | 1 |

## Largest expenditure classes

The 12 largest of 53 expenditure classes used by this agency in FY2020.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4500 | Professional Services Non-It | $864,424.05 | 25.8% |
| 4800 | Facilities Rent | $556,990.22 | 16.6% |
| 4600 | State Government Service Charges | $468,782.34 | 14.0% |
| 4365 | Computer Technology Pc Equipment<$5K | $165,349.39 | 4.9% |
| 4201 | Office Services | $125,074.83 | 3.7% |
| 6082 | Distribution To Dhs Agy 100 | $119,602.07 | 3.6% |
| 4206 | Catering Services | $116,295.13 | 3.5% |
| 4550 | Attorney General Legal Fees | $111,209.08 | 3.3% |
| 4200 | Office Supplies | $106,249.33 | 3.2% |
| 4701 | Other Services | $96,771.22 | 2.9% |
| 4515 | Professional Services Application Maint | $73,613.00 | 2.2% |
| 4362 | Computer Technology Server Support | $60,916.06 | 1.8% |

## Curator notes

Figures are aggregated from 328 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='839' AND fiscal_year='2020'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2020.parquet`, the file these figures were computed from.


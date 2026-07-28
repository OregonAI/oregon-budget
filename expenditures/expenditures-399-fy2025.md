---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: expenditures-399-fy2025
title: Psychiatric Security Rev Brd — FY2025 expenditures
doc_type: dataset_doc
citation: Oregon Agency Expenditures, agency 399, FY2025
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
  - expenditures-399-fy2024
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- expenditures
- fy2025
- agency-399
- psychiatric-security-rev-brd
agency_code: '399'
agency_name: PSYCHIATRIC SECURITY REV BRD
fiscal_year: 2025
total_expense: '489392.90'
transaction_count: 28
---

> **NON-AUTHORITATIVE — AI-friendly reference only.** These are aggregates derived
> from a state dataset, not the official text of any budget or audit. Figures
> are as mirrored on 2026-07-28; the live dataset may have been revised since.
> Verify against the official source: `https://data.oregon.gov/d/y9g9-xsxs`

# Psychiatric Security Rev Brd — FY2025 expenditures

## At a glance

Psychiatric Security Rev Brd (agency code 399, recorded upstream as `PSYCHIATRIC SECURITY REV BRD`) spent **$489,392.90** in fiscal year 2025, across 28 transaction records. That is up 6.3% from $460,577.23 in FY2024. The agency accounts for 0.00% of the $35,121,392,355.76 in statewide agency spending recorded for FY2025, ranking **68 of 80** agencies reporting that year.

The largest budget category was **Attorney General Legal Fees** at $150,929.90 (30.8% of the agency's total).

## Spending by budget class

| Code | Budget class | Amount | Share | Records |
|---|---|---:|---:|---:|
| 4325 | Attorney General Legal Fees | $150,929.90 | 30.8% | 1 |
| 4225 | State Government Service Charges | $91,553.09 | 18.7% | 4 |
| 4250 | Data Processing | $81,349.98 | 16.6% | 6 |
| 4425 | Lease Payments & Taxes | $75,778.62 | 15.5% | 1 |
| 4650 | Other Services And Supplies | $50,271.33 | 10.3% | 2 |
| 4715 | It Expendable Property | $13,711.10 | 2.8% | 1 |
| 4300 | Professional Services | $11,952.68 | 2.4% | 3 |
| 4175 | Office Expenses | $5,112.48 | 1.0% | 4 |
| 4150 | Employee Training | $4,099.16 | 0.8% | 2 |
| 4275 | Publicity & Publications | $2,950.00 | 0.6% | 1 |
| 4200 | Telecomm/Tech Svc And Supplies | $1,684.56 | 0.3% | 3 |

## Largest expenditure classes

The 12 largest of 15 expenditure classes used by this agency in FY2025.

| Code | Expenditure class | Amount | Share |
|---|---|---:|---:|
| 4550 | Attorney General Legal Fees | $150,929.90 | 30.8% |
| 4600 | State Government Service Charges | $91,553.09 | 18.7% |
| 4800 | Interagency Lease Payments | $75,778.62 | 15.5% |
| 4367 | Computer Technology Pc Support | $66,389.76 | 13.6% |
| 4701 | Other Services | $50,271.33 | 10.3% |
| 4375 | Computer Technology Computer Processing | $14,960.22 | 3.1% |
| 4365 | Computer Technology Pc Equipment<$5K | $13,711.10 | 2.8% |
| 4500 | Professional Services Non-It | $11,952.68 | 2.4% |
| 4201 | Office Services | $4,784.48 | 1.0% |
| 4401 | Training, Education Or Instruction Srvc | $4,000.00 | 0.8% |
| 4253 | Advertise, Publicity, Publish/Print Srvs | $2,950.00 | 0.6% |
| 4305 | Telecom/Network Services | $1,124.24 | 0.2% |

## Curator notes

Figures are aggregated from 28 vendor-level transaction records. This document deliberately reports no vendor-level detail: roughly 5% of the 98,933 vendors in the source are individual people, and this corpus does not republish named individuals' payments as indexed, agent-searchable text. Vendor detail remains available from the live source, which is where the state publishes it.

Oregon budgets by **biennium**; this dataset reports by **fiscal year**. The two do not line up, and no mapping between them is applied here. Comparing these figures to a biennial appropriation requires stating that mapping explicitly — it is the single most likely source of a plausible wrong number.

## Verification

Every figure above is reproducible from the live API. The agency total:

```
https://data.oregon.gov/resource/y9g9-xsxs.json?$select=sum(expense)&$where=agency='399' AND fiscal_year='2025'
```

`src/build_documents.py --check` re-derives every number in this document from the committed Parquet mirror, and `src/ingest_expenditures.py --check` reconciles that mirror against the live API. Both run in CI. The recorded `source_sha256` is the hash of `expenditures-2025.parquet`, the file these figures were computed from.


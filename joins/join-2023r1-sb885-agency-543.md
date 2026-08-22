---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: join-2023r1-sb885-agency-543
title: 2023 Regular Session Senate Bill 885 → agency 543 spending, FY2024–FY2025
doc_type: dataset_doc
citation: 'Join: 2023 Regular Session Senate Bill 885 to Oregon Agency Expenditures agency 543'
issuing_body: Oregon Department of Administrative Services
source_url: https://olis.oregonlegislature.gov/liz/2023R1/Downloads/MeasureDocument/SB885/Introduced
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: ''
verified_by: ''
maintainer: '@dzinck'
human_reviewed: false
joins:
- document_id: expenditures-543-fy2024
  dataset: expenditures
  key: agency=543;fiscal_year=2024
- document_id: expenditures-543-fy2025
  dataset: expenditures
  key: agency=543;fiscal_year=2025
relationships:
  implements: []
  implemented_by: []
  references_external:
  - 2023 Regular Session Senate Bill 885
  related:
  - appropriations-2023r1-sb885
  - expenditures-543-fy2024
  - expenditures-543-fy2025
  supersedes: []
tags:
- oregon-budget
- join
- agency-543
- unreviewed
appropriation_document: appropriations-2023r1-sb885
sibling_corpus: oregon-legislature
sibling_document_id: measure-2023r1-sb885
agency_code: '543'
agency_registry_slug: oregon-state-library
agency_registry_basis: das_number
agency_registry_corpus: executive-regulatory-frameworks
biennium: beginning 2023
fiscal_years:
- 2024
- 2025
biennium_to_fiscal_year_assumption: Oregon's fiscal year runs 1 July to 30 June and is named for the calendar
  year it ends in, so a biennium ending 30 June 2025 covers FY2024 and FY2025. This is a stated convention,
  not something the expenditure dataset asserts about itself.
---

> **NON-AUTHORITATIVE — UNREVIEWED.** This document links an appropriation to an
> agency's spending records. The spending figures **do not account for** the
> appropriation — see below. Neither side has been checked by a person.

# 2023 Regular Session Senate Bill 885 → agency 543

## At a glance

2023 Regular Session Senate Bill 885 appropriates to **Oregon State Library** (budget agency code `543`, registry slug `oregon-state-library`) for the **biennium beginning 2023**, which on the stated fiscal-year convention covers **FY2024–FY2025**.

In those fiscal years that agency recorded **$8,624,561.12** of spending across 791 transactions and 306 distinct payees.

## What this join does and does not say

**It links an entity and a period, not dollars.** The appropriation was made to this agency for a purpose stated in the bill. The figure above is that agency's *total* recorded spending from *every* funding source, at vendor-transaction grain. It is not the appropriation being spent, it is not a superset of it in any traceable way, and the two numbers must not be compared as though one accounts for the other.

Answering "was this appropriation spent?" needs an expenditure record carrying the appropriation's own identifier. This dataset has no such column, so that question cannot be answered from this corpus, and this document does not pretend otherwise.

## Agency spending by fiscal year

| Fiscal year | Recorded spending |
|---|---:|
| FY2024 | $4,163,659.17 |
| FY2025 | $4,460,901.95 |

## Provenance

- Appropriation figures: `appropriations-2023r1-sb885` in this corpus — machine-extracted from bill text and **not human-reviewed**.
- Bill text: `measure-2023r1-sb885` in the `oregon-legislature` corpus, referenced not copied.
- Agency identity: `oregon-state-library` in the `executive-regulatory-frameworks` corpus, whose registry carries the hand-reviewed `budget_agency_code: 543`.
- Spending: the committed Parquet mirror, reconciled against live SODA weekly.

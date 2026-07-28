---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: join-2021r1-hb5026-agency-255
title: 2021 Regular Session House Bill 5026 → agency 255 spending, FY2022–FY2023
doc_type: dataset_doc
citation: 'Join: 2021 Regular Session House Bill 5026 to Oregon Agency Expenditures agency 255'
issuing_body: Oregon Department of Administrative Services
source_url: https://olis.oregonlegislature.gov/liz/2021R1/Downloads/MeasureDocument/HB5026/Enrolled
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: '2026-07-28'
verified_by: '@dzinck'
maintainer: '@dzinck'
human_reviewed: false
joins:
- document_id: expenditures-255-fy2022
  dataset: expenditures
  key: agency=255;fiscal_year=2022
- document_id: expenditures-255-fy2023
  dataset: expenditures
  key: agency=255;fiscal_year=2023
relationships:
  implements: []
  implemented_by: []
  references_external:
  - 2021 Regular Session House Bill 5026
  related:
  - appropriations-2021r1-hb5026
  - expenditures-255-fy2022
  - expenditures-255-fy2023
  supersedes: []
tags:
- oregon-budget
- join
- agency-255
- unreviewed
appropriation_document: appropriations-2021r1-hb5026
sibling_corpus: oregon-legislature
sibling_document_id: measure-2021r1-hb5026
agency_code: '255'
agency_registry_slug: board-of-parole-and-post-prison-supervision
agency_registry_corpus: executive-regulatory-frameworks
biennium: beginning 2021
fiscal_years:
- 2022
- 2023
biennium_to_fiscal_year_assumption: Oregon's fiscal year runs 1 July to 30 June and is named for the calendar
  year it ends in, so a biennium ending 30 June 2025 covers FY2024 and FY2025. This is a stated convention,
  not something the expenditure dataset asserts about itself.
---

> **NON-AUTHORITATIVE — UNREVIEWED.** This document links an appropriation to an
> agency's spending records. The spending figures **do not account for** the
> appropriation — see below. Neither side has been checked by a person.

# 2021 Regular Session House Bill 5026 → agency 255

## At a glance

2021 Regular Session House Bill 5026 appropriates to **Board of Parole and Post-Prison Supervision** (budget agency code `255`, registry slug `board-of-parole-and-post-prison-supervision`) for the **biennium beginning 2021**, which on the stated fiscal-year convention covers **FY2022–FY2023**.

In those fiscal years that agency recorded **$2,953,559.02** of spending across 184 transactions and 65 distinct payees.

## What this join does and does not say

**It links an entity and a period, not dollars.** The appropriation was made to this agency for a purpose stated in the bill. The figure above is that agency's *total* recorded spending from *every* funding source, at vendor-transaction grain. It is not the appropriation being spent, it is not a superset of it in any traceable way, and the two numbers must not be compared as though one accounts for the other.

Answering "was this appropriation spent?" needs an expenditure record carrying the appropriation's own identifier. This dataset has no such column, so that question cannot be answered from this corpus, and this document does not pretend otherwise.

## Agency spending by fiscal year

| Fiscal year | Recorded spending |
|---|---:|
| FY2022 | $1,560,182.69 |
| FY2023 | $1,393,376.33 |

## Provenance

- Appropriation figures: `appropriations-2021r1-hb5026` in this corpus — machine-extracted from bill text and **not human-reviewed**.
- Bill text: `measure-2021r1-hb5026` in the `oregon-legislature` corpus, referenced not copied.
- Agency identity: `board-of-parole-and-post-prison-supervision` in the `executive-regulatory-frameworks` corpus, whose registry carries the hand-reviewed `budget_agency_code: 255`.
- Spending: the committed Parquet mirror, reconciled against live SODA weekly.

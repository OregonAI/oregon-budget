---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: join-2019r1-hb2383-agency-150
title: 2019 Regular Session House Bill 2383 → agency 150 spending, FY2020–FY2021
doc_type: dataset_doc
citation: 'Join: 2019 Regular Session House Bill 2383 to Oregon Agency Expenditures agency 150'
issuing_body: Oregon Department of Administrative Services
source_url: https://olis.oregonlegislature.gov/liz/2019R1/Downloads/MeasureDocument/HB2383/Introduced
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: '2026-07-28'
verified_by: '@dzinck'
maintainer: '@dzinck'
human_reviewed: false
joins:
- document_id: expenditures-150-fy2020
  dataset: expenditures
  key: agency=150;fiscal_year=2020
- document_id: expenditures-150-fy2021
  dataset: expenditures
  key: agency=150;fiscal_year=2021
relationships:
  implements: []
  implemented_by: []
  references_external:
  - 2019 Regular Session House Bill 2383
  related:
  - appropriations-2019r1-hb2383
  - expenditures-150-fy2020
  - expenditures-150-fy2021
  supersedes: []
tags:
- oregon-budget
- join
- agency-150
- unreviewed
appropriation_document: appropriations-2019r1-hb2383
sibling_corpus: oregon-legislature
sibling_document_id: measure-2019r1-hb2383
agency_code: '150'
agency_registry_slug: department-of-revenue
agency_registry_corpus: executive-regulatory-frameworks
biennium: beginning 2019
fiscal_years:
- 2020
- 2021
biennium_to_fiscal_year_assumption: Oregon's fiscal year runs 1 July to 30 June and is named for the calendar
  year it ends in, so a biennium ending 30 June 2025 covers FY2024 and FY2025. This is a stated convention,
  not something the expenditure dataset asserts about itself.
---

> **NON-AUTHORITATIVE — UNREVIEWED.** This document links an appropriation to an
> agency's spending records. The spending figures **do not account for** the
> appropriation — see below. Neither side has been checked by a person.

# 2019 Regular Session House Bill 2383 → agency 150

## At a glance

2019 Regular Session House Bill 2383 appropriates to **Department of Revenue** (budget agency code `150`, registry slug `department-of-revenue`) for the **biennium beginning 2019**, which on the stated fiscal-year convention covers **FY2020–FY2021**.

In those fiscal years that agency recorded **$73,184,358.96** of spending across 1,524 transactions and 623 distinct payees.

## What this join does and does not say

**It links an entity and a period, not dollars.** The appropriation was made to this agency for a purpose stated in the bill. The figure above is that agency's *total* recorded spending from *every* funding source, at vendor-transaction grain. It is not the appropriation being spent, it is not a superset of it in any traceable way, and the two numbers must not be compared as though one accounts for the other.

Answering "was this appropriation spent?" needs an expenditure record carrying the appropriation's own identifier. This dataset has no such column, so that question cannot be answered from this corpus, and this document does not pretend otherwise.

## Agency spending by fiscal year

| Fiscal year | Recorded spending |
|---|---:|
| FY2020 | $35,783,161.00 |
| FY2021 | $37,401,197.96 |

## Provenance

- Appropriation figures: `appropriations-2019r1-hb2383` in this corpus — machine-extracted from bill text and **not human-reviewed**.
- Bill text: `measure-2019r1-hb2383` in the `oregon-legislature` corpus, referenced not copied.
- Agency identity: `department-of-revenue` in the `executive-regulatory-frameworks` corpus, whose registry carries the hand-reviewed `budget_agency_code: 150`.
- Spending: the committed Parquet mirror, reconciled against live SODA weekly.

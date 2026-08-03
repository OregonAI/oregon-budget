---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: join-2023r1-sb5516-agency-156
title: 2023 Regular Session Senate Bill 5516 → agency 156 spending, FY2024–FY2025
doc_type: dataset_doc
citation: 'Join: 2023 Regular Session Senate Bill 5516 to Oregon Agency Expenditures agency 156'
issuing_body: Oregon Department of Administrative Services
source_url: https://olis.oregonlegislature.gov/liz/2023R1/Downloads/MeasureDocument/SB5516/Enrolled
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: ''
verified_by: ''
maintainer: '@dzinck'
human_reviewed: false
joins:
- document_id: expenditures-156-fy2024
  dataset: expenditures
  key: agency=156;fiscal_year=2024
- document_id: expenditures-156-fy2025
  dataset: expenditures
  key: agency=156;fiscal_year=2025
relationships:
  implements: []
  implemented_by: []
  references_external:
  - 2023 Regular Session Senate Bill 5516
  related:
  - appropriations-2023r1-sb5516
  - expenditures-156-fy2024
  - expenditures-156-fy2025
  supersedes: []
tags:
- oregon-budget
- join
- agency-156
- unreviewed
appropriation_document: appropriations-2023r1-sb5516
sibling_corpus: oregon-legislature
sibling_document_id: measure-2023r1-sb5516
agency_code: '156'
agency_registry_slug: legislative-administration-committee
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

# 2023 Regular Session Senate Bill 5516 → agency 156

## At a glance

2023 Regular Session Senate Bill 5516 appropriates to **Legislative Administration Committee** (budget agency code `156`, registry slug `legislative-administration-committee`) for the **biennium beginning 2023**, which on the stated fiscal-year convention covers **FY2024–FY2025**.

In those fiscal years that agency recorded **$339,094,406.67** of spending across 725 transactions and 274 distinct payees.

## What this join does and does not say

**It links an entity and a period, not dollars.** The appropriation was made to this agency for a purpose stated in the bill. The figure above is that agency's *total* recorded spending from *every* funding source, at vendor-transaction grain. It is not the appropriation being spent, it is not a superset of it in any traceable way, and the two numbers must not be compared as though one accounts for the other.

Answering "was this appropriation spent?" needs an expenditure record carrying the appropriation's own identifier. This dataset has no such column, so that question cannot be answered from this corpus, and this document does not pretend otherwise.

## Agency spending by fiscal year

| Fiscal year | Recorded spending |
|---|---:|
| FY2024 | $160,181,183.52 |
| FY2025 | $178,913,223.15 |

## Provenance

- Appropriation figures: `appropriations-2023r1-sb5516` in this corpus — machine-extracted from bill text and **not human-reviewed**.
- Bill text: `measure-2023r1-sb5516` in the `oregon-legislature` corpus, referenced not copied.
- Agency identity: `legislative-administration-committee` in the `executive-regulatory-frameworks` corpus, whose registry carries the hand-reviewed `budget_agency_code: 156`.
- Spending: the committed Parquet mirror, reconciled against live SODA weekly.

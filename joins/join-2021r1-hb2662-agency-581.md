---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: join-2021r1-hb2662-agency-581
title: 2021 Regular Session House Bill 2662 → agency 581 spending, FY2022–FY2023
doc_type: dataset_doc
citation: 'Join: 2021 Regular Session House Bill 2662 to Oregon Agency Expenditures agency 581'
issuing_body: Oregon Department of Administrative Services
source_url: https://olis.oregonlegislature.gov/liz/2021R1/Downloads/MeasureDocument/HB2662/Introduced
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: '2026-08-02'
verified_by: '@dzinck'
maintainer: '@dzinck'
human_reviewed: false
joins:
- document_id: expenditures-581-fy2022
  dataset: expenditures
  key: agency=581;fiscal_year=2022
- document_id: expenditures-581-fy2023
  dataset: expenditures
  key: agency=581;fiscal_year=2023
relationships:
  implements: []
  implemented_by: []
  references_external:
  - 2021 Regular Session House Bill 2662
  related:
  - appropriations-2021r1-hb2662
  - expenditures-581-fy2022
  - expenditures-581-fy2023
  supersedes: []
tags:
- oregon-budget
- join
- agency-581
- unreviewed
appropriation_document: appropriations-2021r1-hb2662
sibling_corpus: oregon-legislature
sibling_document_id: measure-2021r1-hb2662
agency_code: '581'
agency_registry_slug: oregon-department-of-education
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

# 2021 Regular Session House Bill 2662 → agency 581

## At a glance

2021 Regular Session House Bill 2662 appropriates to **Oregon Department of Education** (budget agency code `581`, registry slug `oregon-department-of-education`) for the **biennium beginning 2021**, which on the stated fiscal-year convention covers **FY2022–FY2023**.

In those fiscal years that agency recorded **$24,046,343,779.24** of spending across 6,379 transactions and 2,917 distinct payees.

## What this join does and does not say

**It links an entity and a period, not dollars.** The appropriation was made to this agency for a purpose stated in the bill. The figure above is that agency's *total* recorded spending from *every* funding source, at vendor-transaction grain. It is not the appropriation being spent, it is not a superset of it in any traceable way, and the two numbers must not be compared as though one accounts for the other.

Answering "was this appropriation spent?" needs an expenditure record carrying the appropriation's own identifier. This dataset has no such column, so that question cannot be answered from this corpus, and this document does not pretend otherwise.

## Agency spending by fiscal year

| Fiscal year | Recorded spending |
|---|---:|
| FY2022 | $11,666,797,730.47 |
| FY2023 | $12,379,546,048.77 |

## Provenance

- Appropriation figures: `appropriations-2021r1-hb2662` in this corpus — machine-extracted from bill text and **not human-reviewed**.
- Bill text: `measure-2021r1-hb2662` in the `oregon-legislature` corpus, referenced not copied.
- Agency identity: `oregon-department-of-education` in the `executive-regulatory-frameworks` corpus, whose registry carries the hand-reviewed `budget_agency_code: 581`.
- Spending: the committed Parquet mirror, reconciled against live SODA weekly.

---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: join-2021r1-hb5042-agency-629
title: 2021 Regular Session House Bill 5042 → agency 629 spending, FY2020–FY2021
doc_type: dataset_doc
citation: 'Join: 2021 Regular Session House Bill 5042 to Oregon Agency Expenditures agency 629'
issuing_body: Oregon Department of Administrative Services
source_url: https://olis.oregonlegislature.gov/liz/2021R1/Downloads/MeasureDocument/HB5042/Enrolled
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: '2026-08-02'
verified_by: '@dzinck'
maintainer: '@dzinck'
human_reviewed: false
joins:
- document_id: expenditures-629-fy2020
  dataset: expenditures
  key: agency=629;fiscal_year=2020
- document_id: expenditures-629-fy2021
  dataset: expenditures
  key: agency=629;fiscal_year=2021
relationships:
  implements: []
  implemented_by: []
  references_external:
  - 2021 Regular Session House Bill 5042
  related:
  - appropriations-2021r1-hb5042
  - expenditures-629-fy2020
  - expenditures-629-fy2021
  supersedes: []
tags:
- oregon-budget
- join
- agency-629
- unreviewed
appropriation_document: appropriations-2021r1-hb5042
sibling_corpus: oregon-legislature
sibling_document_id: measure-2021r1-hb5042
agency_code: '629'
agency_registry_slug: department-of-forestry
agency_registry_corpus: executive-regulatory-frameworks
biennium: ending 2021
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

# 2021 Regular Session House Bill 5042 → agency 629

## At a glance

2021 Regular Session House Bill 5042 appropriates to **Department of Forestry** (budget agency code `629`, registry slug `department-of-forestry`) for the **biennium ending 2021**, which on the stated fiscal-year convention covers **FY2020–FY2021**.

In those fiscal years that agency recorded **$253,597,284.22** of spending across 6,205 transactions and 3,002 distinct payees.

## What this join does and does not say

**It links an entity and a period, not dollars.** The appropriation was made to this agency for a purpose stated in the bill. The figure above is that agency's *total* recorded spending from *every* funding source, at vendor-transaction grain. It is not the appropriation being spent, it is not a superset of it in any traceable way, and the two numbers must not be compared as though one accounts for the other.

Answering "was this appropriation spent?" needs an expenditure record carrying the appropriation's own identifier. This dataset has no such column, so that question cannot be answered from this corpus, and this document does not pretend otherwise.

## Agency spending by fiscal year

| Fiscal year | Recorded spending |
|---|---:|
| FY2020 | $101,727,153.04 |
| FY2021 | $151,870,131.18 |

## Provenance

- Appropriation figures: `appropriations-2021r1-hb5042` in this corpus — machine-extracted from bill text and **not human-reviewed**.
- Bill text: `measure-2021r1-hb5042` in the `oregon-legislature` corpus, referenced not copied.
- Agency identity: `department-of-forestry` in the `executive-regulatory-frameworks` corpus, whose registry carries the hand-reviewed `budget_agency_code: 629`.
- Spending: the committed Parquet mirror, reconciled against live SODA weekly.

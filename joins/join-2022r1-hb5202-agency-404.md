---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: join-2022r1-hb5202-agency-404
title: 2022 Regular Session House Bill 5202 → agency 404 spending, FY2022–FY2023
doc_type: dataset_doc
citation: 'Join: 2022 Regular Session House Bill 5202 to Oregon Agency Expenditures agency 404'
issuing_body: Oregon Department of Administrative Services
source_url: https://olis.oregonlegislature.gov/liz/2022R1/Downloads/MeasureDocument/HB5202/Enrolled
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: ''
verified_by: ''
maintainer: '@dzinck'
human_reviewed: false
joins:
- document_id: expenditures-404-fy2022
  dataset: expenditures
  key: agency=404;fiscal_year=2022
- document_id: expenditures-404-fy2023
  dataset: expenditures
  key: agency=404;fiscal_year=2023
relationships:
  implements: []
  implemented_by: []
  references_external:
  - 2022 Regular Session House Bill 5202
  related:
  - appropriations-2022r1-hb5202
  - expenditures-404-fy2022
  - expenditures-404-fy2023
  supersedes: []
tags:
- oregon-budget
- join
- agency-404
- unreviewed
appropriation_document: appropriations-2022r1-hb5202
sibling_corpus: oregon-legislature
sibling_document_id: measure-2022r1-hb5202
agency_code: '404'
agency_registry_slug: office-of-public-defense-services
agency_registry_corpus: executive-regulatory-frameworks
biennium: ending 2023
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

# 2022 Regular Session House Bill 5202 → agency 404

## At a glance

2022 Regular Session House Bill 5202 appropriates to **Office of Public Defense Services** (budget agency code `404`, registry slug `office-of-public-defense-services`) for the **biennium ending 2023**, which on the stated fiscal-year convention covers **FY2022–FY2023**.

In those fiscal years that agency recorded **$381,577,703.13** of spending across 3,231 transactions and 1,064 distinct payees.

## What this join does and does not say

**It links an entity and a period, not dollars.** The appropriation was made to this agency for a purpose stated in the bill. The figure above is that agency's *total* recorded spending from *every* funding source, at vendor-transaction grain. It is not the appropriation being spent, it is not a superset of it in any traceable way, and the two numbers must not be compared as though one accounts for the other.

Answering "was this appropriation spent?" needs an expenditure record carrying the appropriation's own identifier. This dataset has no such column, so that question cannot be answered from this corpus, and this document does not pretend otherwise.

## Agency spending by fiscal year

| Fiscal year | Recorded spending |
|---|---:|
| FY2022 | $173,872,567.66 |
| FY2023 | $207,705,135.47 |

## Provenance

- Appropriation figures: `appropriations-2022r1-hb5202` in this corpus — machine-extracted from bill text and **not human-reviewed**.
- Bill text: `measure-2022r1-hb5202` in the `oregon-legislature` corpus, referenced not copied.
- Agency identity: `office-of-public-defense-services` in the `executive-regulatory-frameworks` corpus, whose registry carries the hand-reviewed `budget_agency_code: 404`.
- Spending: the committed Parquet mirror, reconciled against live SODA weekly.

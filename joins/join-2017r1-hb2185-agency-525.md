---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: join-2017r1-hb2185-agency-525
title: 2017 Regular Session House Bill 2185 → agency 525 spending, FY2019–FY2019
doc_type: dataset_doc
citation: 'Join: 2017 Regular Session House Bill 2185 to Oregon Agency Expenditures agency 525'
issuing_body: Oregon Department of Administrative Services
source_url: https://olis.oregonlegislature.gov/liz/2017R1/Downloads/MeasureDocument/HB2185/Introduced
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: ''
verified_by: ''
maintainer: '@dzinck'
human_reviewed: false
joins:
- document_id: expenditures-525-fy2019
  dataset: expenditures
  key: agency=525;fiscal_year=2019
relationships:
  implements: []
  implemented_by: []
  references_external:
  - 2017 Regular Session House Bill 2185
  related:
  - appropriations-2017r1-hb2185
  - expenditures-525-fy2019
  supersedes: []
tags:
- oregon-budget
- join
- agency-525
- unreviewed
appropriation_document: appropriations-2017r1-hb2185
sibling_corpus: oregon-legislature
sibling_document_id: measure-2017r1-hb2185
agency_code: '525'
agency_registry_slug: higher-education-coordinating-commission
agency_registry_basis: das_number
agency_registry_basis_key: HI-ED COORD CMSN
agency_registry_corpus: executive-regulatory-frameworks
biennium: beginning 2017
fiscal_years:
- 2019
biennium_to_fiscal_year_assumption: Oregon's fiscal year runs 1 July to 30 June and is named for the calendar
  year it ends in, so a biennium ending 30 June 2025 covers FY2024 and FY2025. This is a stated convention,
  not something the expenditure dataset asserts about itself.
---

> **NON-AUTHORITATIVE — UNREVIEWED.** This document links an appropriation to an
> agency's spending records. The spending figures **do not account for** the
> appropriation — see below. Neither side has been checked by a person.

# 2017 Regular Session House Bill 2185 → agency 525

## At a glance

2017 Regular Session House Bill 2185 appropriates to **Higher Education Coordinating Commission** (budget agency code `525`, registry slug `higher-education-coordinating-commission`) for the **biennium beginning 2017**, which on the stated fiscal-year convention covers **FY2019–FY2019**.

In those fiscal years that agency recorded **$1,324,012,851.11** of spending across 833 transactions and 314 distinct payees.

## What this join does and does not say

**It links an entity and a period, not dollars.** The appropriation was made to this agency for a purpose stated in the bill. The figure above is that agency's *total* recorded spending from *every* funding source, at vendor-transaction grain. It is not the appropriation being spent, it is not a superset of it in any traceable way, and the two numbers must not be compared as though one accounts for the other.

Answering "was this appropriation spent?" needs an expenditure record carrying the appropriation's own identifier. This dataset has no such column, so that question cannot be answered from this corpus, and this document does not pretend otherwise.

## Agency spending by fiscal year

| Fiscal year | Recorded spending |
|---|---:|
| FY2019 | $1,324,012,851.11 |

## Provenance

- Appropriation figures: `appropriations-2017r1-hb2185` in this corpus — machine-extracted from bill text and **not human-reviewed**.
- Bill text: `measure-2017r1-hb2185` in the `oregon-legislature` corpus, referenced not copied.
- Agency identity: `higher-education-coordinating-commission` in the `executive-regulatory-frameworks` corpus, whose registry carries the hand-reviewed `budget_agency_code: 525`. Resolved here by matching this bill's `appropriated_to` string against that registry, exact-only.
- Agency identity, independently: `_meta/agency-crosswalk.yml` resolves the expenditure feed's own name for this body, `HI-ED COORD CMSN`, to the same slug on basis `das_number`. The `agency_registry_basis` in this document's frontmatter is THAT claim, about THAT string — not a description of how the bill's wording matched.
- Spending: the committed Parquet mirror, reconciled against live SODA weekly.

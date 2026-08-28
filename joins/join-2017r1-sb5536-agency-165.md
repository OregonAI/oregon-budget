---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: join-2017r1-sb5536-agency-165
title: 2017 Regular Session Senate Bill 5536 → agency 165 spending, FY2019–FY2019
doc_type: dataset_doc
citation: 'Join: 2017 Regular Session Senate Bill 5536 to Oregon Agency Expenditures agency 165'
issuing_body: Oregon Department of Administrative Services
source_url: https://olis.oregonlegislature.gov/liz/2017R1/Downloads/MeasureDocument/SB5536/Enrolled
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: ''
verified_by: ''
maintainer: '@dzinck'
human_reviewed: false
joins:
- document_id: expenditures-165-fy2019
  dataset: expenditures
  key: agency=165;fiscal_year=2019
relationships:
  implements: []
  implemented_by: []
  references_external:
  - 2017 Regular Session Senate Bill 5536
  related:
  - appropriations-2017r1-sb5536
  - expenditures-165-fy2019
  supersedes: []
tags:
- oregon-budget
- join
- agency-165
- unreviewed
appropriation_document: appropriations-2017r1-sb5536
sibling_corpus: oregon-legislature
sibling_document_id: measure-2017r1-sb5536
agency_code: '165'
agency_registry_slug: secretary-of-state
agency_registry_basis: exact
agency_registry_basis_key: SECRETARY OF STATE
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

# 2017 Regular Session Senate Bill 5536 → agency 165

## At a glance

2017 Regular Session Senate Bill 5536 appropriates to **Secretary of State** (budget agency code `165`, registry slug `secretary-of-state`) for the **biennium beginning 2017**, which on the stated fiscal-year convention covers **FY2019–FY2019**.

In those fiscal years that agency recorded **$11,415,405.87** of spending across 523 transactions and 255 distinct payees.

## What this join does and does not say

**It links an entity and a period, not dollars.** The appropriation was made to this agency for a purpose stated in the bill. The figure above is that agency's *total* recorded spending from *every* funding source, at vendor-transaction grain. It is not the appropriation being spent, it is not a superset of it in any traceable way, and the two numbers must not be compared as though one accounts for the other.

Answering "was this appropriation spent?" needs an expenditure record carrying the appropriation's own identifier. This dataset has no such column, so that question cannot be answered from this corpus, and this document does not pretend otherwise.

## Agency spending by fiscal year

| Fiscal year | Recorded spending |
|---|---:|
| FY2019 | $11,415,405.87 |

## Provenance

- Appropriation figures: `appropriations-2017r1-sb5536` in this corpus — machine-extracted from bill text and **not human-reviewed**.
- Bill text: `measure-2017r1-sb5536` in the `oregon-legislature` corpus, referenced not copied.
- Agency identity: `secretary-of-state` in the `executive-regulatory-frameworks` corpus, whose registry carries the hand-reviewed `das_agency_number: 165`. Resolved here by matching this bill's `appropriated_to` string against that registry, exact-only.
- Agency identity, independently: `_meta/agency-crosswalk.yml` resolves the expenditure feed's own name for this body, `SECRETARY OF STATE`, to the same slug on basis `exact`. The `agency_registry_basis` in this document's frontmatter is THAT claim, about THAT string — not a description of how the bill's wording matched.
- Spending: the committed Parquet mirror, reconciled against live SODA weekly.

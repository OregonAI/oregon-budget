---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: join-2021r1-hb3288-agency-107
title: 2021 Regular Session House Bill 3288 → agency 107 spending, FY2022–FY2023
doc_type: dataset_doc
citation: 'Join: 2021 Regular Session House Bill 3288 to Oregon Agency Expenditures agency 107'
issuing_body: Oregon Department of Administrative Services
source_url: https://olis.oregonlegislature.gov/liz/2021R1/Downloads/MeasureDocument/HB3288/Introduced
source_format: soda
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: ''
verified_by: ''
maintainer: '@dzinck'
human_reviewed: false
joins:
- document_id: expenditures-107-fy2022
  dataset: expenditures
  key: agency=107;fiscal_year=2022
- document_id: expenditures-107-fy2023
  dataset: expenditures
  key: agency=107;fiscal_year=2023
relationships:
  implements: []
  implemented_by: []
  references_external:
  - 2021 Regular Session House Bill 3288
  related:
  - appropriations-2021r1-hb3288
  - expenditures-107-fy2022
  - expenditures-107-fy2023
  supersedes: []
tags:
- oregon-budget
- join
- agency-107
- unreviewed
appropriation_document: appropriations-2021r1-hb3288
sibling_corpus: oregon-legislature
sibling_document_id: measure-2021r1-hb3288
agency_code: '107'
agency_registry_slug: department-of-administrative-services
agency_registry_basis: das_number
agency_registry_basis_key: ADMINISTRATIVE SRVCS, DEPT OF
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

# 2021 Regular Session House Bill 3288 → agency 107

## At a glance

2021 Regular Session House Bill 3288 appropriates to **Department of Administrative Services** (budget agency code `107`, registry slug `department-of-administrative-services`) for the **biennium beginning 2021**, which on the stated fiscal-year convention covers **FY2022–FY2023**.

In those fiscal years that agency recorded **$4,981,678,029.94** of spending across 4,779 transactions and 2,281 distinct payees.

## What this join does and does not say

**It links an entity and a period, not dollars.** The appropriation was made to this agency for a purpose stated in the bill. The figure above is that agency's *total* recorded spending from *every* funding source, at vendor-transaction grain. It is not the appropriation being spent, it is not a superset of it in any traceable way, and the two numbers must not be compared as though one accounts for the other.

Answering "was this appropriation spent?" needs an expenditure record carrying the appropriation's own identifier. This dataset has no such column, so that question cannot be answered from this corpus, and this document does not pretend otherwise.

## Agency spending by fiscal year

| Fiscal year | Recorded spending |
|---|---:|
| FY2022 | $3,501,528,244.90 |
| FY2023 | $1,480,149,785.04 |

## Provenance

- Appropriation figures: `appropriations-2021r1-hb3288` in this corpus — machine-extracted from bill text and **not human-reviewed**.
- Bill text: `measure-2021r1-hb3288` in the `oregon-legislature` corpus, referenced not copied.
- Agency identity: `department-of-administrative-services` in the `executive-regulatory-frameworks` corpus, whose registry carries the hand-reviewed `das_agency_number: 107`. Resolved here by matching this bill's `appropriated_to` string against that registry, exact-only.
- Agency identity, independently: `_meta/agency-crosswalk.yml` resolves the expenditure feed's own name for this body, `ADMINISTRATIVE SRVCS, DEPT OF`, to the same slug on basis `das_number`. The `agency_registry_basis` in this document's frontmatter is THAT claim, about THAT string — not a description of how the bill's wording matched.
- Spending: the committed Parquet mirror, reconciled against live SODA weekly.

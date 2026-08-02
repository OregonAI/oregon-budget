---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: appropriations-2023r1-hb2983
title: Appropriations in 2023 Regular Session House Bill 2983
doc_type: dataset_doc
citation: 2023 Regular Session House Bill 2983
issuing_body: Oregon State Legislature
source_url: https://olis.oregonlegislature.gov/liz/2023R1/Downloads/MeasureDocument/HB2983/Introduced
source_format: pdf
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: '2026-08-02'
verified_by: '@dzinck'
maintainer: '@dzinck'
human_reviewed: false
relationships:
  implements: []
  implemented_by: []
  references_external:
  - 2023 Regular Session House Bill 2983
  related: []
  supersedes: []
tags:
- oregon-budget
- appropriations
- 2023r1
- unreviewed
sibling_corpus: oregon-legislature
sibling_document_id: measure-2023r1-hb2983
sibling_snapshot_id: measure-2023r1-hb2983-introduced
sibling_source_sha256: 8e448975b838c1977aab2859916f099f946ad9f15a993b1cf550513f9c92cdee
extraction_status: subsections-not-itemized
appropriated_to: null
fund: General Fund
biennium: beginning 2023
biennium_fiscal_years:
- 2024
- 2025
blank_amounts: 0
blank_recipient: false
modifies_prior_appropriations: 0
amends_prior_law: 0
recipients_in_itemization:
- Housing and Community Services Department
- Department of Land Conservation and Development
---

> **NON-AUTHORITATIVE — UNREVIEWED MACHINE EXTRACTION.** Every figure on this
> page was read out of bill prose by a parser and has **not** been checked by
> a person. It is not the text of any bill and must not be quoted as an
> appropriation. The authoritative text is `https://olis.oregonlegislature.gov/liz/2023R1/Downloads/MeasureDocument/HB2983/Introduced`.

# Appropriations in 2023 Regular Session House Bill 2983

## At a glance

HB 2983 (2023R1): Appropriates moneys from General Fund to Department of Land Conservation and Development and Housing and Community Services Department to support manufactured dwellings and manufactured dwelling parks.

Parsed context: out of the **General Fund**, for the biennium **beginning 2023** (fiscal years 2024–2025).

Extraction status: **subsections-not-itemized**. No itemization to reconcile against.

The full text of this bill lives in the `oregon-legislature` corpus as `measure-2023r1-hb2983` and is referenced, not copied.

**Stated appropriation**

| Amount | Verbatim source line |
|---:|---|
| $250,000 | (2) To the Department of Land Conservation and Development, the amount of $250,000 to develop: |

**Other amounts in this section** — separate statutory provisions (a further appropriation, a spending cap, an expenditure limitation). They are **not** components of the appropriation above and must never be summed with it or with each other.

| Subsection | Text (parsed) | Amount | Verbatim source line |
|---|---|---:|---|
| (1) | To the Housing and Community Services Department: (a) | $35,000,000 | (a) $35,000,000 for deposit in the Manufactured Home  Preservation Fund under ORS 458.366 to be used to provide loans under ORS 458.352. |
| (2) | To the Department of Land Conservation and Development, the amount of | $250,000 | (2) To the Department of Land Conservation and Development, the amount of $250,000 to develop: |

## Curator notes

**This bill appropriates to MULTIPLE recipients in one itemization** — **Housing and Community Services Department**, **Department of Land Conservation and Development**. A single `appropriated_to` field cannot carry that without attributing the whole bill to one of them, so it is left null and the recipients are listed here. Per-recipient joins are future work; an honest none beats a wrong one.

Summing every dollar figure in an appropriation bill **double-counts**: a bill states an appropriation and then itemizes the same money. The stated appropriation and the line items are separate tables above for exactly that reason, and must never be added together.

The 'purpose' column is a parser's reading of the surrounding prose, not the bill's own words. The verbatim source line beside it is the bill's own words, and is the column to trust.

---
schema_version: 1
corpus: oregon-budget
jurisdiction: oregon
id: account-code-structure
title: 'Dataset doc: ORBITS/SFMA account code structure'
doc_type: entity_doc
citation: DAS ORBITS to SFMA Account Crosswalk
issuing_body: Oregon Department of Administrative Services
source_url: https://www.oregon.gov/das/Financial/Documents/ORBITS-SFMA-ACCOUNT-CROSSWALK.pdf
source_format: pdf
snapshot_policy: hash-only
status: current
content_mode: summary
last_verified: ''
verified_by: ''
maintainer: '@dzinck'
conversion_notes: Codes and titles are transcribed from the source crosswalk. The BAND taxonomy is NOT
  stated in the source — it is the convention that the leading digit encodes a category, recorded here
  because nothing else in this corpus carries it.
relationships:
  implements: []
  implemented_by: []
  references_external: []
  related:
  - agency-expenditures
  supersedes: []
tags:
- oregon-budget
- reference
- account-codes
---

## At a glance

**481 ORBITS budget accounts.** 373 map to 689 R*STARS (SFMA) comparative objects beneath them; **108 have no SFMA counterpart at all** — budget-side concepts such as Beginning Balance and General Fund Appropriation, which can never appear in expenditure data.

This is what the `budget_class` and `expend_class` columns of the mirrored expenditure data contain: `budget_class` is the ORBITS account, `expend_class` is the comparative object beneath it.

_NON-AUTHORITATIVE. Verify at the source URL._


## The leading digit is a category

The source crosswalk never states this. It is a convention, and it is what makes a bare four-digit code readable.


| Range | Band | Accounts | Monetary |
|---|---|---:|---|
| 0000–0999 | Revenue | 81 | yes |
| 1000–2999 | Transfers | 188 | yes |
| 3000–3999 | Personnel services | 36 | yes |
| 4000–4999 | Services and supplies | 29 | yes |
| 5000–5999 | Capital outlay | 20 | yes |
| 6000–6999 | Distributions | 103 | yes |
| 7000–7999 | Debt service | 11 | yes |
| 8000–8999 | Positions and FTE | 12 | **no — counts, not dollars** |
| 9000–9999 | Reversions | 1 | yes |

### The 8000 band is not money

`8150`–`8195` are position counts and `8250`–`8295` are FTE — authority to employ people, denominated in people, sharing a code space with dollars. A total taken over codes without excluding them adds headcount to money and yields a figure that is not money and looks like it.

No expenditure row in this corpus carries an 8000-series code, so no total here is currently wrong. That is a fact about SFMA actuals rather than about the code space: the band exists in ORBITS, and anything that later ingests budget-side data will meet it.

### Two things the bands make visible

- `5800 Professional Services` (capital outlay) and `4300 Professional Services` (services and supplies) are the same words in different bands, and are different things.
- `x90` and `x95` recur across bands as Budget and Management and Legislative Fiscal Office analyst adjustments — `5990`/`5995`, `8190`/`8195`, `8290`/`8295`. A sub-convention, not separate concepts.


## Where the mirrored data disagrees with the crosswalk

Of 379 distinct `(budget_class, expend_class)` pairings in the mirrored expenditure data, **366 agree** with this crosswalk, **8 disagree**, and **5 comparative objects do not appear in it at all**.

Reported, not corrected. The crosswalk is a point-in-time snapshot and the mirror spans FY2019–FY2025, so applying it to historical rows would silently re-attribute spending. The disagreements are also not purely chronological — some comparative objects appear under two different accounts *within the same fiscal year*, which the crosswalk cannot express and which is a property of the source data.


| Comparative object | Data says | Crosswalk says |
|---|---|---|
| `3120` | `3110` | `3115` |
| `6450` | `6580` | `6048` |
| `6451` | `6580` | `6048` |
| `6452` | `6580` | `6048` |
| `6453` | `6580` | `6048` |
| `6454` | `6580` | `6048` |
| `6455` | `6580` | `6048` |
| `6456` | `6580` | `6048` |

## Accounts

Full machine-readable table, with every comparative object: [`_meta/catalog/account-codes.yml`](../_meta/catalog/account-codes.yml).


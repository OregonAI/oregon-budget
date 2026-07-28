# Unresolved agencies

_Generated 2026-07-28 by `python3 src/build_joins.py --unresolved-report`. Do not edit by hand._

**76 appropriations** across **13 distinct names** overlap the FY2019–FY2025 expenditure mirror but name an agency that does not resolve against the sibling registry's `budget_agency_code`, so no join was built.

Resolution is deliberately exact-only. A near-match attaches an appropriation to the wrong agency and the result reads as a finding — which is how the *Legislative* Revenue Office once got matched to the Department of Revenue. Everything below stays unjoined until a human confirms it.

## 1. Extraction failed — the parser, not the registry

**59 appropriations.** `appropriated_to` is empty or too truncated to identify. These are NOT missing registry mappings: the bill names an agency and `APPROPRIATED_TO` failed to capture it. Fixing them is parser work in `src/extract_appropriations.py`, and it is the largest single category — curating registry data would not help.

| captured value | appropriations | example bill |
|---|---:|---|
| `(empty)` | 55 | `appropriations-2017r1-hb5046` |
| `Commission` | 4 | `appropriations-2017r1-hb5003` |

## 2. Probable name variant — needs a human to confirm

**0 appropriations.** A registry entry with a budget code looks like the same body, usually differing only in word order ("State Forestry Department" vs "Department of Forestry"). **Suggestions are unverified** and were produced by exactly the fuzzy matching `resolve_agency` refuses to apply. Confirm one by recording it in the sibling's registry, not by loosening the matcher.

| bill says | appropriations | suggested registry entry | code | overlap |
|---|---:|---|---:|---:|

## 3. In the registry, but no budget code — cannot join

**4 appropriations.** The body has a registry entry, so this is NOT a missing agency. It carries no `budget_agency_code` because the expenditure data records no separate spending line for it — typically a sub-unit funded through its parent. Nothing to join to; adding a code would mean inventing one.

| bill says | appropriations | registry entry (no budget code) |
|---|---:|---|
| Youth Development Division | 2 | `oregon-department-of-education-youth-development-division` |
| Oregon Patient Safety Commission | 1 | `oregon-patient-safety-commission` |
| Invasive Species Council | 1 | `department-of-agriculture-oregon-invasive-species-council` |

## 4. No registry counterpart — correctly unresolved

**13 appropriations.** These bodies issue no administrative rules, so they hold no OAR chapter and do not appear in a registry keyed on chapter assignment. The Emergency Board is a contingency fund that disburses through other agencies; the Governor's office and the legislative-branch bodies are outside the executive rulemaking scheme entirely. Absence here is a fact about the registry's scope, not a gap to fill.

| bill says | appropriations | closest registry entry (no code / low overlap) |
|---|---:|---|
| Emergency Board | 6 | — |
| State Workforce Investment Board | 1 | — |
| Oregon Ocean Science Trust | 1 | — |
| Oregon Climate Authority | 1 | — |
| State Workforce and Talent Development Board | 1 | — |
| Office of Child Care | 1 | — |
| Elliott State Research Forest Authority | 1 | — |
| Oregon Business Development Department to carry | 1 | `oregon-business-development-department` (0.50) |

---

Appropriations whose biennium falls OUTSIDE FY2019–FY2025 are not listed here — they cannot be joined regardless of agency, because the expenditure mirror does not reach those years. See the README's coverage table.

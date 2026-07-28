# Unresolved agencies

_Generated 2026-07-28 by `python3 src/build_joins.py --unresolved-report`. Do not edit by hand._

**71 appropriations** across **11 distinct names** overlap the FY2019–FY2025 expenditure mirror but name an agency that does not resolve against the sibling registry's `budget_agency_code`, so no join was built.

Resolution is deliberately exact-only. A near-match attaches an appropriation to the wrong agency and the result reads as a finding — which is how the *Legislative* Revenue Office once got matched to the Department of Revenue. Everything below stays unjoined until a human confirms it.

## 1. The BILL leaves the recipient blank — nothing to fix

**51 appropriations.** The text reads `appropriated to ______`. These are HB 5000-series budget templates whose agency has not been filled in yet, so no agency could be extracted because **the bill names none**. Not a parser defect and not a registry gap — there is no fix, only accurate reporting.

| captured value | appropriations | example bill |
|---|---:|---|
| `(empty)` | 51 | `appropriations-2017r1-hb5046` |

## 1b. Extraction genuinely failed — the parser

**4 appropriations.** The bill names an agency and `APPROPRIATED_TO` failed to capture it. This is parser work in `src/extract_appropriations.py`.

| captured value | appropriations | example bill |
|---|---:|---|
| `(empty)` | 4 | `appropriations-2020r1-hb5204` |

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

**12 appropriations.** These bodies issue no administrative rules, so they hold no OAR chapter and do not appear in a registry keyed on chapter assignment. The Emergency Board is a contingency fund that disburses through other agencies; the Governor's office and the legislative-branch bodies are outside the executive rulemaking scheme entirely. Absence here is a fact about the registry's scope, not a gap to fill.

| bill says | appropriations | closest registry entry (no code / low overlap) |
|---|---:|---|
| Emergency Board | 6 | — |
| State Workforce Investment Board | 1 | — |
| Oregon Ocean Science Trust | 1 | — |
| Oregon Climate Authority | 1 | — |
| State Workforce and Talent Development Board | 1 | — |
| Office of Child Care | 1 | — |
| Elliott State Research Forest Authority | 1 | — |

---

Appropriations whose biennium falls OUTSIDE FY2019–FY2025 are not listed here — they cannot be joined regardless of agency, because the expenditure mirror does not reach those years. See the README's coverage table.

# Unresolved agencies

_Generated 2026-08-31 by `python3 src/build_joins.py --unresolved-report`. Do not edit by hand._

**70 appropriations** across **11 distinct names** overlap the FY2019–FY2025 expenditure mirror but name an agency that does not resolve against the sibling registry's `das_agency_number`, so no join was built.

Resolution is deliberately exact-only. A near-match attaches an appropriation to the wrong agency and the result reads as a finding — which is how the *Legislative* Revenue Office once got matched to the Department of Revenue. Everything below stays unjoined until a human confirms it.

## 1. The BILL leaves the recipient blank — nothing to fix

**51 appropriations.** The text reads `appropriated to ______`. These are HB 5000-series budget templates whose agency has not been filled in yet, so no agency could be extracted because **the bill names none**. Not a parser defect and not a registry gap — there is no fix, only accurate reporting.

| captured value | appropriations | example bill |
|---|---:|---|
| `(empty)` | 51 | `appropriations-2017r1-hb5046` |

## 1b. Extraction genuinely failed — the parser

**0 appropriations.** The bill names an agency and `APPROPRIATED_TO` failed to capture it. This is parser work in `src/extract_appropriations.py`.

_None._

## 1c. The bill only MODIFIES prior session laws — the null is accurate

**2 appropriations.** These bills increase, decrease or amend amounts appropriated by earlier session laws ("is increased by $X", "Section 3, chapter 598, Oregon Laws 2023, is amended to read"). The recipient of each amount lives in the amended chapter, not in this bill's own text — no agency name exists here to extract. Joining these means resolving the amended chapter first, which is future work, not parser work.

| appropriations | example bill |
|---:|---|
| 2 | `appropriations-2020r1-hb5204` |

## 1d. Multi-recipient itemization — no single recipient exists

**1 appropriations.** The bill appropriates to several bodies in one itemized list ("(1) To the Housing and Community Services Department: ..."). A single `appropriated_to` cannot carry that without attributing the whole bill to one recipient; the names are recorded per document under `recipients_in_itemization`. Per-recipient joins need the join model to carry them — an honest none beats a wrong one.

| recipients (from the bill) | appropriations | example bill |
|---|---:|---|
| Housing and Community Services Department; Department of Land Conservation and Development | 1 | `appropriations-2023r1-hb2983` |

## 2. Probable name variant — needs a human to confirm

**0 appropriations.** A registry entry with a `das_agency_number` looks like the same body, usually differing only in word order ("State Forestry Department" vs "Department of Forestry"). **Suggestions are unverified** and were produced by exactly the fuzzy matching `resolve_agency` refuses to apply. Confirm one by recording it in the sibling's registry, not by loosening the matcher.

| bill says | appropriations | suggested registry entry | code | overlap |
|---|---:|---|---:|---:|

## 3. In the registry, but no `das_agency_number` — cannot join

**4 appropriations.** The body has a registry entry, so this is NOT a missing agency. It carries no `das_agency_number` — ERF does not track it as a distinct body in the state's financial administration, typically because it is a sub-unit funded through its parent rather than because it fails to appear in the expenditure mirror. Nothing to join to; adding one would mean inventing it.

| bill says | appropriations | registry entry (no `das_agency_number`) |
|---|---:|---|
| Youth Development Division | 2 | `oregon-department-of-education-youth-development-division` |
| Oregon Patient Safety Commission | 1 | `oregon-patient-safety-commission` |
| Invasive Species Council | 1 | `department-of-agriculture-oregon-invasive-species-council` |

## 4. No registry counterpart

**12 appropriations.** The exact-only matcher resolved none of these names against the registry, and the content-word suggester below found nothing close enough to propose. THAT IS ALL THIS SECTION MEASURES. Whether a body is absent because it issues no administrative rules and so holds no OAR chapter — the registry is keyed on chapter assignment — or because nobody has looked, is a decision, and decisions live in `_meta/agency-crosswalk.yml`. The last column is that file's, rendered here rather than restated: `reviewed` means somebody established why there is no counterpart, `not-reviewed` means the mechanical check found none and nobody has established why.

| bill says | appropriations | closest registry entry (no code / low overlap) | recorded decision (`_meta/agency-crosswalk.yml`) |
|---|---:|---|---|
| Emergency Board | 6 | — | `reviewed` — The Emergency Board is a contingency fund that disburses through other agencies, so it issues no administrative rules, holds no OAR chapter, and does not appear in a registry keyed on chapter assignment. Absence here is a fact about the registry's scope, not a gap to fill. |
| State Workforce Investment Board | 1 | — | `not-reviewed` — NOT REVIEWED. The only thing on record about this body is the `checked` field of this entry: the exact-only matcher resolved it to nothing and the report's suggester found no registry entry close enough to propose. Whether it holds no OAR chapter — which would make its absence correct by construction — or holds one the registry has not recorded, nobody has established. |
| Oregon Ocean Science Trust | 1 | — | `not-reviewed` — NOT REVIEWED. The only thing on record is the `checked` field of this entry. Whether this body holds no OAR chapter, or holds one the registry has not recorded, nobody has established. |
| Oregon Climate Authority | 1 | — | `not-reviewed` — NOT REVIEWED. The only thing on record is the `checked` field of this entry. A name appearing in a bill is not by itself evidence that the body was created, so even "this body exists" is unestablished here, let alone why the registry has no entry for it. |
| State Workforce and Talent Development Board | 1 | — | `not-reviewed` — NOT REVIEWED. The only thing on record is the `checked` field of this entry. Whether this body holds no OAR chapter, or holds one the registry has not recorded, nobody has established. Note that "State Workforce Investment Board" is also recorded here, unreviewed, and whether the two names denote one body across a rename is part of what nobody has looked at. |
| Office of Child Care | 1 | — | `not-reviewed` — NOT REVIEWED. The only thing on record is the `checked` field of this entry. The registry does carry early-learning bodies (oregon-department-of-education-early- learning-division, DAS number 588), so whether this is a unit of one of them, a body the registry has not recorded, or correctly absent, is exactly the question nobody has answered. |
| Elliott State Research Forest Authority | 1 | — | `not-reviewed` — NOT REVIEWED. The only thing on record is the `checked` field of this entry. Whether this body holds no OAR chapter, or holds one the registry has not recorded, nobody has established. |

---

Appropriations whose biennium falls OUTSIDE FY2019–FY2025 are not listed here — they cannot be joined regardless of agency, because the expenditure mirror does not reach those years. See the README's coverage table.

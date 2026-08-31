# Changelog — Oregon Budget — Appropriations and Expenditures

Keep a Changelog format; ISO dates. Change types: Added, Source-Updated,
Superseded, Repealed, Removed, Verified, Fixed, Security.
Repo-curation dates only — official effective dates live in frontmatter.

## [Unreleased]

### Added
- 2026-08-22 — **`_meta/agency-crosswalk.yml`, and `src/link_agency_registry.py` to keep
  it honest** (OregonAI/oregon-budget#23). Before this, 474 documents carried an
  `agency_registry_slug` with no recorded warrant and the 83 agency name strings the
  expenditure feed publishes had no recorded resolution in either direction — an agency
  correctly absent from the registry by construction and one nobody had checked were the
  same state. Now: 81 of the 83 map to a registry slug with a stated `basis`, and 9
  strings are recorded as `unmapped`, each with a reason AND a `basis` of `reviewed` or
  `not-reviewed` so the two states cannot be read as one. **Of those 9, exactly 1 (the
  Emergency Board) carries a researched reason; the other 8 are recorded as NOT YET
  REVIEWED**, which is a different, honest state and is the whole point of the file.
  `--check` runs per-PR from committed data alone; `--verify-registry` resolves every slug
  and DAS number against the sibling and exits 2, never 0, when it is absent.
- 2026-08-22 — **`agency_registry_basis` and `agency_registry_basis_key` on all 474
  slugged join documents.** The slug said which agency; nothing said why that answer was
  right. `src/build_joins.py` now writes both at build time from the crosswalk and
  `--stamp` backfills documents built before it existed, so one file answers and both
  writers read it. `--check` fails if a stamped document and the crosswalk disagree,
  which is the gate that was missing while the same fact was asserted in two places.
  The KEY is there because two different resolutions of one body meet in a join: the
  document's slug came from matching the bill's `appropriated_to` wording against the
  registry, while the basis beside it is the crosswalk's warrant for the expenditure
  feed's spelling of the same body. They agree, and `--check` fails if they stop
  agreeing — but a basis carrying no key would read as a description of the resolution
  it is not about.

### Changed
- 2026-08-22 — **`_meta/unresolved-agencies.md` section 4 now renders the decision
  recorded in the crosswalk instead of stating a reason of its own** (the choice
  #23 asked to be made explicitly: the crosswalk is the source of record, the generated
  report reports against it). Its previous section text was one fixed paragraph printed
  over every name whose fuzzy overlap fell below the suggester's threshold, asserting that
  those bodies issue no administrative rules — a bucket label being read as a finding
  about each body in it, and it reasoned about "the Governor's office and the
  legislative-branch bodies", neither of which the bucket has contained since those names
  started resolving. The section now states only what it measures.
- 2026-08-27 — **All 474 published join documents' agency-identity line, and both code
  readers of ERF's registry in this repo, switch from `budget_agency_code` to
  `das_agency_number`** (OregonAI/oregon-budget#49). ERF's ADR 0003 renamed the registry's
  hand-reviewed budget code field because the number identifies a body in the state's
  financial administration and says nothing about whether it spends money, and deprecated
  the old name as an alias — writing both today and asserting them equal (measured on the
  real registry: 80 organizations carry both, zero disagree). oregon-budget was the last
  reader of the old name on the platform, so this is a hard switch with no fallback:
  `src/build_joins.py`'s `erf_agencies()`/`build()` and `src/link_agency_registry.py`'s
  `registry_index()` — a second, independent reader this ticket's own fleet survey missed
  on first pass — both now read `das_agency_number` only. Regenerated against the real ERF
  registry checkout: `grep -l budget_agency_code joins/*.md` goes 474 → 0,
  `grep -l das_agency_number` goes 0 → 474, one hunk per file, no document added or
  removed. `--check` is unaffected (474 documents, 854 join entries, clean) — it asserts
  referential integrity only and never reads the registry either way. The generated
  `_meta/unresolved-agencies.md` report's separate, non-CI-gated `budget_agency_code`
  reads are tracked as oregon-budget#53, out of this change's scope. The At-a-glance
  sentence's spaced English phrase "budget agency code `NNN`" is unchanged by design — the
  ticket's own Implementation Decision names only "the agency-identity template line",
  which is the `- Agency identity: ...` bullet, not this descriptive prose.
- 2026-08-30 — **`unresolved_report()`'s `suggest()` switches from `budget_agency_code` to
  `das_agency_number`, and `_meta/unresolved-agencies.md` is regenerated** (OregonAI/oregon-budget#53,
  the read #49 tracked as out of its own scope). `suggest()` reads the registry's raw YAML
  directly rather than through `erf_agencies()`, so it was the one reader #49's hard switch
  missed; on a registry carrying only `das_agency_number` (the post-migration shape), every
  truthy check on the retired key came back `None` and a genuine name variant fell out of
  "## 2. Probable name variant" into "## 3. ... cannot join". The report's own prose (module
  intro, section 2/3 headings and table headers, the stdout summary, and the
  `erf_agencies()` docstring) is switched too — all now read `das_agency_number`; the
  dual-key detection at lines 112/116 that intentionally still checks both names is
  untouched. Section 3's explanation was also reworded: it previously said a body carries no
  code "because the expenditure data records no separate spending line for it", a causal
  claim ADR 0003 rules out in general (`das_agency_number` "says nothing about whether it
  spends money" — thirteen semi-independent bodies carry one and are explicitly outside the
  state's accounting system). It now says the absence means ERF does not track the body as
  distinct in the state's financial administration, typically because it is a sub-unit
  funded through its parent. Regenerated against the real ERF registry: the diff is exactly
  the terminology/prose lines above, with `**70 appropriations**`, `**11 distinct names**`,
  and the `**4 appropriations**` in section 3 all unchanged, confirming a pure wording fix
  with zero effect on which appropriations land in which bucket. Two new tests
  (`tests/test_registry_join.py`) use a `das_agency_number`-only registry fixture, because
  the real registry dual-writes both keys today and would pass unfixed code too.

### Fixed
- 2026-08-02 — **Un-stamped fabricated `last_verified`/`verified_by` on all
  1,761 stamped content documents** across `expenditures/`, `bills/`,
  `datasets/`, and `joins/`. Every stamp was an ingestion date ('2026-07-28'
  or '2026-08-02', matching the bulk-write dates) with `verified_by: @dzinck`
  written by the pipeline, not by a human reviewer. AGENTS.md rule 6 is
  explicit: these fields are set only by the human reviewer at approval —
  "a fabricated verification stamp is worse than an obviously-empty one."
  Both fields are now empty strings: schema-valid, read downstream as "never
  verified", which is exactly true. The one already-empty doc
  (`datasets/account-code-structure.md`) is untouched. This is the honest
  baseline for the M4 verification pilot; STATUS.md's freshness table now
  reports all 1,762 documents overdue instead of a fiction of one.
- 2026-08-02 — README's CI-check table described `build_documents.py --check` as
  re-deriving "all 544 documents" — accurate only for the agency-year root, and
  reading as a corpus total in a corpus of 1,762 documents. Rephrased to "every
  agency-year document" so the sentence stays true as counts move. `llms.txt`
  `## Contents` was still the template's empty stub (corpus-template#16); filled
  with annotated entries for the four content roots and the authority graph.

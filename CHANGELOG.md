# Changelog — Oregon Budget — Appropriations and Expenditures

Keep a Changelog format; ISO dates. Change types: Added, Source-Updated,
Superseded, Repealed, Removed, Verified, Fixed, Security.
Repo-curation dates only — official effective dates live in frontmatter.

## [Unreleased]

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

# Changelog — Oregon Budget — Appropriations and Expenditures

Keep a Changelog format; ISO dates. Change types: Added, Source-Updated,
Superseded, Repealed, Removed, Verified, Fixed, Security.
Repo-curation dates only — official effective dates live in frontmatter.

## [Unreleased]

### Fixed
- 2026-08-02 — README's CI-check table described `build_documents.py --check` as
  re-deriving "all 544 documents" — accurate only for the agency-year root, and
  reading as a corpus total in a corpus of 1,762 documents. Rephrased to "every
  agency-year document" so the sentence stays true as counts move. `llms.txt`
  `## Contents` was still the template's empty stub (corpus-template#16); filled
  with annotated entries for the four content roots and the authority graph.

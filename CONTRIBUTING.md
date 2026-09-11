# Contributing

All changes via PR with CODEOWNER review. Before merge, the PR checklist
requires: pinned source URL reachable; retrieval date + hash recorded;
version/effective dates transcribed exactly as the source prints them;
`## Full text` verified verbatim (CI-diffed); relationships resolve;
disclaimer present; CHANGELOG updated. Reviewers set `last_verified` /
`verified_by` at approval. Agent-assisted commits carry a `Co-Authored-By:`
trailer naming the assisting model and a `Claude-Session:` trailer linking
the session transcript — re-measured 2026-09-10 against this repo's own
history (`git log --all --format=%B | grep -ic assisted-by` returns 0; every
credited commit since #67 uses `Co-authored-by:`/`Claude-Session:`), where
this line still named an `Assisted-by:` trailer nothing in the repo has ever
used.

# AGENTS.md — Oregon Budget — Appropriations and Expenditures

Corpus of the OregonAI civic corpus platform. Archetype: hybrid.
Read `_meta/corpus.yml` for configuration; the platform rules live in
OregonAI/corpus-toolkit `docs/`.

## Purpose
Non-authoritative, AI-friendly mirror of State agency expenditures from data.oregon.gov (Socrata), and the appropriation line items that authorised them. Budget bills themselves are referenced in oregon-legislature, never copied.
Never a source of truth — every answer must cite and link the
authoritative source.

## Hard rules (anti-fabrication)
1. Never write content that does not exist in the pinned source. Source
   unreachable or unparseable → insert
   `<!-- TODO: human verification required -->` and stop. Never
   reconstruct from model knowledge.
2. `## Full text` sections are verbatim only. Curator content is confined
   to `## At a glance`, `## Curator notes`, `## Cross-references`.
3. Third-party copyrighted material: summary + official link only.
4. Never invent or infer a citation. Unresolvable → say so.
5. Live-data answers (api/hybrid) must carry the executed query and
   timestamp.
6. All changes via PR. Do not set `last_verified`/`verified_by` to a real
   value — the human reviewer does that at approval. The schema REQUIRES both
   keys, so ingestion writes them as empty strings: schema-valid, and read
   downstream as "never verified", which is exactly true. Never write a date or
   a handle you did not earn; a fabricated verification stamp is worse than an
   obviously-empty one.
7. Update this knowledge body's CHANGELOG.md in the same PR as content
   changes.

## Found a defect? Fix it. Filing an issue is the exception, and it has a cost.

**The default is to fix it in the change you are already making.** You are in the file with
the context loaded, which is the cheapest this fix will ever be. Filing an issue converts a
ten-minute fix into a future session that has to rebuild everything you currently know.

**Open an issue only when one of these is true:**

1. **It needs a decision you are not allowed to make** — a judgement about what the corpus
   means, a trade-off with a real cost, anything a grilling session would have put to the
   operator. Label it `ready-for-human`.
2. **It is large enough to need its own review** — if fixing it would make this change's diff
   hard for a reviewer to follow, it is separate work.
3. **It is in a file this change does not touch**, and reaching into it would widen the change
   beyond what its own review covers.

**If none of those is true, fix it now.** "I noticed it while doing something else" is not a
reason to defer; it is the reason it is cheap.

### An issue must name its trigger

Every issue states **what would make this matter** — the condition under which it stops being
latent. "Nothing currently escapes this" with no trigger is not a ticket. It is a comment at
the site, where the next person who can act on it will actually be standing.

**A comment in the code beats a ticket in a queue** whenever the person who would fix it is
the next person reading that code. Reserve the queue for work that has to be found by someone
who is *not* already in that file.

### Review findings are not issues

A code-review finding applied in the same change is already tracked by that review. Do not
also file it. An issue opened and closed within the hour adds a row to the backlog and tells
nobody anything.

### At most two issues per task

If you found more than two things worth another person's attention, the finding is that this
module needs work — and that is **one** issue naming the pattern, not five naming instances.
Ranking is the point: the third-most-important thing you noticed is usually a comment.

### Why this replaced "open an issue, period"

Measured in `executive-regulatory-frameworks` on 2026-08-29: **49 issues opened in two days,
20 closed, the backlog 19 → 48.** Of the 20 closures, 8 were review findings filed and fixed
inside the same hour — tracked already, and pure ceremony. Of the 29 left open, 3 needed a
human decision and roughly 12 were things the agent could have fixed while it was already in
the file.

The old rule's justification was that "nobody greps closed PRs six months later." True — and
nobody greps a 48-issue backlog either. A backlog nobody works is not a record; it is where a
defect goes to be forgotten with a clear conscience, and it buries the few issues that
genuinely need a person.

These all count as a defect, not just crashes:

- a check that passes without checking anything
- a documented command, flag, or path that does not exist or does not work
- a claim in a README, docstring, or catalog note that is no longer true
- data known to be wrong, stale, or incomplete
- a guard that cannot fire, or fires on the wrong condition
- something you worked around instead of fixing

**File it in the repo that owns the fix, which may not be the repo you are in.** A parser
defect here, a registry gap in a sibling corpus, and a validator gap in `corpus-toolkit`
are three different issues in three different repos. Say plainly in each which repo the
work belongs to.

An issue must answer four things, because an issue that only says "X is broken" costs the
next person the whole investigation again:

1. **What is wrong** — the specific behaviour, not a category
2. **How it was found** — the command, the data, the failing case
3. **What it breaks** — who or what gets a wrong answer, and how silently
4. **What would fix it**, or what still needs measuring before anyone can know

Prefer counts and reproductions over adjectives. "126 appropriations unjoined, of which 59
are an extraction gap and 41 are correct" is actionable; "agency matching needs work" is
not, and will be re-derived by someone else.

If you genuinely cannot open one — no network, no permission — say so explicitly in your
final message to the user and hand them the text to file. Silently dropping it is the one
outcome that is never acceptable.

## Workflow
Discovery → human-approved source manifest → ingestion → human-reviewed
PR. See toolkit `docs/replication-guide.md`.

## Setting up this corpus (delete this section once done)

1. **Fill every placeholder.** `grep -rno '{{[A-Z_]*}}' .` must come back empty.
2. **Name the content root.** Rename `documents/` to whatever this corpus holds
   and make `content_roots` in `_meta/corpus.yml` agree. A `doc_type` may only
   live in the directory routed to it — the validator fails both ways (wrong
   type under a root, and a type placed outside its root).
3. **Set a real CODEOWNER.** `.github/CODEOWNERS` ships a placeholder. GitHub
   silently ignores an owner it cannot resolve, so a wrong entry enforces
   nothing while looking like it does.
4. **Write an ingester** under `src/`. It must satisfy the hashing contract in
   `_meta/templates/document.md` — call `corpus_toolkit.repo.hash_snapshot`
   rather than hashing anything yourself.
5. **Build the graph**: `python3 src/build_graph.py`. Nothing in the toolkit
   writes `_meta/graph.json`; without it citation resolution silently returns
   nothing. The `generated` CI job keeps it honest.
6. **Add a `--check` CI step for every generated file you commit.** A gate that
   exists but is not wired is worse than no gate: it reads as covered.
7. **Declare siblings** in `_meta/corpus.yml` if this corpus cites documents in
   another one, and mark those citation schemes with
   `register_scheme(..., corpus="<sibling id>")`. Reference across corpora;
   never copy documents between them.

## Generated files — never hand-edit

| file | generated by | gate |
|---|---|---|
| `_meta/graph.json` | `src/build_graph.py` | `generated` job, every PR |
| `STATUS.md` | `corpus-generate-status` | weekly `drift` job |
| `_meta/line-items.json` | `src/build_story_exports.py` | `generated` job, every PR |
| `_meta/vendor-concentration.json` | `src/build_story_exports.py` | `generated` job, every PR |
| `_meta/unresolved-agencies.md` | `src/build_joins.py --unresolved-report` | not in CI (needs the sibling registry); its section 4 must name only bodies `_meta/agency-crosswalk.yml` has decided, and THAT is gated by `link_agency_registry.py --check` |

`_meta/agency-crosswalk.yml` is the exception that proves the table: it is **committed
source of record, not generated**. Nothing rewrites it. Its `das_number` entries were
seeded once by composing two committed facts (the expenditure feed publishes the DAS
number beside the agency name; ERF records that number on the organization, hand-reviewed
there), and `--verify-registry` re-tests every one of them against ERF rather than
trusting what is written in it. Edit it by hand; that is the point of it.

Regenerate at the source and commit the result.

## Agent skills

### Issue tracker

GitHub Issues on `OregonAI/oregon-budget`, via the `gh` CLI. See
`docs/agents/issue-tracker.md`.

### Triage labels

The five canonical roles, each label string equal to its name. See
`docs/agents/triage-labels.md`.

### Domain docs

Single-context — `CONTEXT.md` and `docs/adr/` at the repo root. See
`docs/agents/domain.md`.

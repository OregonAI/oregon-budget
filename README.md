# Oregon Budget — Appropriations and Expenditures

> ## ⚠️ NON-AUTHORITATIVE — AI-friendly reference only
> Curated copies/summaries, not official text. Always verify at the
> authoritative source linked in each document. See [DISCLAIMER.md](DISCLAIMER.md).

Part of the OregonAI civic corpus platform
([reference architecture](https://github.com/OregonAI/corpus-toolkit)).
Archetype: **hybrid**. MCP interface: contract v1.

| Entry point | For |
|---|---|
| [llms.txt](llms.txt) | Machine-readable index — AI agents start here |
| [AGENTS.md](AGENTS.md) | Agent rules and anti-fabrication requirements |
| [STATUS.md](STATUS.md) | Generated health: freshness, coverage, drift |
| `_meta/corpus.yml` | Corpus configuration |

## What is here

Oregon state spending and budget data, as documents an AI agent can read and as a
queryable mirror.

| | |
|---|---|
| Agency-year documents | **544** — one per agency per fiscal year, FY2019–FY2025 |
| Dataset docs | 3 — the shape, keys, and quirks of each upstream Socrata dataset |
| Mirrored rows | **668,906**, totalling **$199,601,500,470.97** |
| Mirror format | Parquet, one file per fiscal year (5.9 MB total) |

544, not 574: 82 agencies × 7 years is an upper bound, but 30 of those agency-years have
no spending at all. Emitting documents for them would invent years that never happened.

### Two provenance clocks, never one

This is a **hybrid** corpus, and its two halves are dated differently. The mirrored data
carries a git commit and a `retrieved:` date; anything read live from the API carries an
`executed_at` timestamp and the exact query that produced it. An answer that draws on both
must show both. Presenting one as-of date for the pair is how a stale number acquires a
fresh-looking citation.

## Rebuilding

```
pip install -r requirements.txt
python3 src/ingest_expenditures.py      # mirror SODA -> data/expenditures/*.parquet
python3 src/build_documents.py          # 544 agency-year documents
python3 src/build_dataset_docs.py       # 3 dataset docs
python3 src/build_graph.py              # _meta/graph.json
```

Every one of those has a `--check` that verifies rather than regenerates, and each is
wired into CI. The split is deliberate:

| Check | Runs | Why there |
|---|---|---|
| `build_documents.py --check` | every PR | offline; re-derives all 544 documents' figures from the Parquet |
| `build_graph.py --check` | every PR | offline; catches a document added without rebuilding the graph |
| `ingest_expenditures.py --check` | weekly | needs the live API; compares row count **and** summed expense per year |
| `build_dataset_docs.py --check` | weekly | needs the live API; detects upstream schema drift |

The live checks are deliberately not per-PR. A gate that depends on a third party being up
goes red for reasons unrelated to the change, and a gate that cries wolf is one people
learn to ignore.

`build_documents.py --check` exists because `corpus-verify-provenance` structurally cannot
check these documents: they are derived aggregates, not extracted source text, so it
reports "0 full-text sections verified" — honestly, and usefully, but it is not a content
check. Recording a hash and calling that verified would be a check that passes because it
is not running.

## Known traps in the source data

Measured, not assumed. The full detail is in `datasets/*.md`.

- **`mwsa-rpk9` contains its own `Totals` row.** Summing all 80 rows reports
  $281,553,047,958 against a true $140,776,523,979 — exactly double Oregon's 2025–27
  budget, with no error to signal it. Filter `dept_no = 'Totals'` before any aggregate.
- **Socrata returns 1000 rows by default and emits no continuation token.** A single
  request looks complete and is not; `$limit=60000` against a 101,178-row year returns
  exactly 60,000. Every paged fetch here reconciles against a separate `count(*)`.
- **Three datasets, three agency identifier systems, and the names never match.** Zero
  exact string matches between the 83 agency names in expenditures and the 79 in budgeted
  revenue. Join on `dept_no / 100`, never on a name.
- **Budgets are biennial; expenditures are by fiscal year.** No mapping between them is
  applied anywhere in this repo. Stating it per join is required, and it is the single
  most likely source of a plausible wrong number.

## A note on vendors

The source names 98,933 distinct payees, and the documents report the largest per
agency-year alongside budget and expenditure classes. This is public record published by
the State of Oregon under `USGOV_WORKS`, and who the state pays is the substance of the
transparency question rather than an incidental detail of it. Nothing is masked or
withheld.

One caveat that is a data-quality point, not a privacy one: a payee string is whatever was
entered in the statewide financial system, so the same organisation can appear under
several spellings and is **not** de-duplicated here. Treating each distinct string as a
distinct organisation will undercount the large ones.

## License
Content (curated government material): CC0-1.0. Tooling, structure,
metadata: MIT. See [LICENSE](LICENSE).

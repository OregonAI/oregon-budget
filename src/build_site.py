#!/usr/bin/env python3
"""Build the GitHub Pages site into ./site/ (gitignored; produced at deploy time).

    python3 src/build_site.py

Chrome, CSS and the cross-corpus contracts live in `corpus_toolkit.site`. This file owns
only what is specific to this corpus.

THIS REPLACES the reusable publish-index workflow — the two must never both exist here,
because they fight over the `pages` concurrency group.
"""
import json
import pathlib
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from corpus_toolkit import config as config_mod                       # noqa: E402
from corpus_toolkit.site import Page, Section, Tile, build            # noqa: E402

REPO = pathlib.Path(__file__).resolve().parent.parent


def stats() -> dict:
    fy, total, tx = set(), 0.0, 0
    counts = {}
    for root in ("expenditures", "bills", "datasets", "joins"):
        counts[root] = sum(1 for _ in (REPO / root).rglob("*.md"))
        for p in (REPO / root).rglob("*.md"):
            fm = yaml.safe_load(p.read_text().split("---", 2)[1]) or {}
            if fm.get("fiscal_year"):
                fy.add(str(fm["fiscal_year"]))
            total += float(fm.get("total_expense") or 0)
            tx += int(fm.get("transaction_count") or 0)
    g = json.loads((REPO / "_meta/graph.json").read_text())
    return {"docs": g["n_nodes"], "edges": g["n_edges"],
            "external": g.get("n_edges_external", 0),
            "first": min(fy), "last": max(fy), "billions": total / 1e9,
            "transactions": tx, **counts}


def main() -> int:
    s = stats()
    out = build(Page(
        config=config_mod.load(REPO / "_meta/corpus.yml"),
        repo="oregon-budget",
        title="Oregon Budget & Expenditure — where the money authorized actually went",
        description=("A non-authoritative, machine-readable mirror of Oregon state "
                     "expenditures and budget-bill appropriations, joined to the "
                     "legislation that authorized them."),
        eyebrow="Oregon · statewide",
        headline="Where the money the Legislature authorized actually went",
        lede_html=(
            f"<b>{s['expenditures']} agency-year expenditure summaries</b> over a mirror of "
            f"<b>{s['transactions']:,} transactions</b> and <b>${s['billions']:.0f} billion</b>, "
            f"fiscal {s['first']} to {s['last']}, plus {s['bills']} appropriation line items "
            "referenced back to the bills that made them."),
        disclaimer=("NON-AUTHORITATIVE reference — not the official financial record. "
                    "Always verify against data.oregon.gov and the Legislature."),
        tiles=[
            Tile("Agency-year summaries", f"{s['expenditures']}",
                 f"fiscal {s['first']} to {s['last']}"),
            Tile("Transactions mirrored", f"{s['transactions']:,}",
                 f"${s['billions']:.0f}B of state spending"),
            Tile("Appropriation line items", f"{s['bills']}",
                 "extracted from budget bills, linked to the measure"),
            Tile("Referential joins", f"{s['joins']}",
                 "agency and fund codes reconciled across sources"),
        ],
        sections=[
            Section("A summary is not the ledger", """
    <ul class="plain">
      <li>The documents here are <b>summaries derived from a mirror</b> of the state's
        published expenditure data. They are the grain a question is usually asked at —
        agency by year — and they are not the transaction record itself.</li>
      <li>Live queries against the source dataset are available through the MCP server, so
        a question the summaries cannot answer does not have to be answered by guessing at
        them.</li>
      <li><b>A truncation guard is enforced.</b> The published API silently caps result
        sets; a capped read that looked complete would produce a total that is simply
        wrong, so a query that hits the cap is reported as capped rather than returned.</li>
    </ul>"""),
            Section("The dollars node of the graph", """
    <ul class="plain">
      <li>Appropriation line items reference the measures that authorized them in
        <a href="https://oregonai.github.io/oregon-legislature/">Legislative Measures</a> —
        bill → appropriation → spending.</li>
      <li>What an agency then <em>claimed</em> it achieved with the money is a different
        corpus: <a href="https://oregonai.github.io/oregon-kpm/">Key Performance
        Measures</a>. Whether the spending was proper is
        <a href="https://oregonai.github.io/oregon-audits/">Audits</a>. This corpus asserts
        none of that.</li>
    </ul>"""),
            Section("For agents", """
    <ul class="plain">
      <li><b>MCP server</b> — the document tools plus <code>list_datasets</code>,
        <code>query_dataset</code> and <code>join_lookup</code> for live queries against
        the source data.</li>
      <li><b>Every document carries provenance</b> — source URL, retrieval date and a
        content hash.</li>
    </ul>"""),
        ],
        footer_note=("Unofficial and non-authoritative; not affiliated with the State of "
                     "Oregon."),
    ))
    print(f"built site/ — {s['docs']:,} documents, fiscal {s['first']}-{s['last']}")
    print(f"  corpus-index.json: {out['index']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

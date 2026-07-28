#!/usr/bin/env python3
"""Corpus-specific MCP tools, registered via `plugins.tools_module` (toolkit >= 1.6.0).

Implements the API-corpus extensions that docs/mcp-interface-contract.md has promised
since it was written: `list_datasets()` and `query_dataset()`. `join_lookup()` is the
third, and lands in Stage 4 with the `joins/` documents it reads — registering a stub now
would answer "no joins" to every question, which reads as "no relationship exists".

WHAT THESE TOOLS WILL NOT DO. `query_dataset` takes named, typed filters and builds the
SoQL itself. It does not accept a `$where` string. Passing raw SoQL through would let a
caller reshape the query into something whose `executed_query` no longer describes what
was asked, and the contract requires that field to be auditable. Equality filters over
caller-named columns cover the questions this corpus exists to answer, and anything richer
belongs in a reviewed tool rather than in a passthrough.

The aggregate path is capped and the row path is capped, separately and for different
reasons — see MAX_ROWS.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import soda  # noqa: E402

MAX_ROWS = 500          # a tool response is read by a model; 668,906 rows is not an answer
MAX_GROUPS = 200

# The datasets this corpus will query, and the columns callers may filter or group on.
# An allow-list rather than a passthrough: a column name reaching SoQL unchecked is the
# same class of hole as a raw $where, and the readable failure ("no such column, here are
# the ones there are") is better than a 400 from Socrata.
DATASETS = {
    "expenditures": {
        "id": "y9g9-xsxs",
        "title": "Agency Expenditures – Multi-Year Report",
        "doc": "agency-expenditures",
        "measure": "expense",
        "columns": ["fiscal_year", "agency", "agency_1", "budget_class", "budget_class_1",
                    "expend_class", "expend_class_1", "vendor", "vendor_st"],
        "mirrored": True,
    },
    "budgeted_revenue": {
        "id": "mwsa-rpk9",
        "title": "Budgeted Revenue (2025-27 biennium)",
        "doc": "budgeted-revenue",
        "measure": "grand_total",
        "columns": ["dept_no", "dept_description"],
        "mirrored": False,
        # See datasets/budgeted-revenue.md. Summing all 80 rows reports $281,553,047,958
        # against a true $140,776,523,979 — exactly double the biennial budget, with
        # nothing in the response to signal it.
        "exclude_where": "dept_no != 'Totals'",
        "warning": ("This dataset contains its own Totals row. Every query issued here "
                    "excludes it automatically; a query written by hand against the raw "
                    "endpoint must filter `dept_no != 'Totals'` or it double-counts."),
    },
    "lottery": {
        "id": "anxj-teqh",
        "title": "Lottery Expenditures – Multi-Year Report",
        "doc": "lottery-expenditures",
        "measure": "amount",
        "columns": ["fiscal_year", "department", "acct_name", "vendor_name", "state",
                    "gl_acct"],
        "mirrored": False,
        "warning": ("Lottery spending is NOT part of the statewide agency expenditure "
                    "total — agency code 177 does not appear in that dataset at all — so "
                    "these figures are additional to it, not a subset. This dataset also "
                    "contains negative amounts (reversals); the agency dataset does not, "
                    "so totals are net here and gross there."),
    },
}


def _combine(*clauses) -> str:
    return " AND ".join(c for c in clauses if c)


def _load_joins():
    """Every committed join document, indexed both ways.

    Read from disk at registration rather than through the retrieval backend: the join
    block lives in frontmatter, and FileBackend.get() returns a fixed field set that drops
    corpus-specific keys — the same gap that made total_expense invisible to HybridBackend.
    """
    import yaml
    from pathlib import Path
    by_doc, by_key = {}, {}
    joins_dir = Path(__file__).resolve().parent.parent / "joins"
    for p in sorted(joins_dir.glob("*.md")):
        fm = yaml.safe_load(p.read_text().split("---\n", 2)[1])
        rec = {"join_document": fm["id"], "title": fm.get("title"),
               "appropriation_document": fm.get("appropriation_document"),
               "sibling_corpus": fm.get("sibling_corpus"),
               "sibling_document_id": fm.get("sibling_document_id"),
               "agency_code": fm.get("agency_code"),
               "agency_registry_slug": fm.get("agency_registry_slug"),
               "agency_registry_corpus": fm.get("agency_registry_corpus"),
               "biennium": fm.get("biennium"), "fiscal_years": fm.get("fiscal_years"),
               "human_reviewed": fm.get("human_reviewed", False),
               "joins": fm.get("joins") or [],
               "biennium_to_fiscal_year_assumption":
                   fm.get("biennium_to_fiscal_year_assumption")}
        for d in {fm.get("appropriation_document"), fm["id"],
                  fm.get("sibling_document_id")} | {j["document_id"] for j in rec["joins"]}:
            if d:
                by_doc.setdefault(d, []).append(rec)
        for j in rec["joins"]:
            by_key.setdefault(j["key"], []).append(rec)
    return by_doc, by_key


def register(mcp, framework):
    """Called by corpus-mcp-serve after every built-in tool."""
    joins_by_doc, joins_by_key = _load_joins()

    @mcp.tool()
    def join_lookup(document_id: str = "", dataset_key: str = "") -> dict:
        """Find the appropriation↔spending links for a document id or a dataset key.

        The hybrid half of the MCP contract. Pass a document_id (an appropriation, a join,
        an agency-year expenditure summary, or a bill id in the legislature corpus) OR a
        dataset_key of the form `agency=107;fiscal_year=2024`. Returns the mapped
        counterparts on the other side, or an explicit empty result naming what was
        searched — never a bare empty list."""
        if not document_id and not dataset_key:
            return {"error": "pass document_id or dataset_key",
                    "example_key": "agency=107;fiscal_year=2024"}
        hits = joins_by_doc.get(document_id, []) if document_id \
            else joins_by_key.get(dataset_key, [])
        if not hits:
            # "No mapping recorded" is NOT "no relationship exists". 150 of 170
            # appropriations fall outside the mirrored fiscal years and can never be
            # joined; a caller must be able to tell that from a missing document.
            return {"found": False, "searched": document_id or dataset_key,
                    "join_documents": 0,
                    "note": ("No join is recorded for this. That is not evidence no "
                             "relationship exists: joins are only built where an "
                             "appropriation's biennium overlaps the mirrored fiscal years "
                             "FY2019-FY2025, which excludes 150 of the 170 extracted "
                             "appropriation documents, and where the agency name resolves "
                             "exactly against the sibling registry."),
                    "disclaimer": "non-authoritative"}
        return {"found": True, "searched": document_id or dataset_key,
                "join_documents": len(hits), "joins": hits,
                "warning": ("These links pair an ENTITY and a PERIOD, never dollars with "
                            "dollars. Agency spending totals do not account for a given "
                            "appropriation and must not be presented as though they do. "
                            "Every join is human_reviewed: false."),
                "disclaimer": "non-authoritative"}

    @mcp.tool()
    def list_datasets() -> dict:
        """The live Socrata datasets this corpus can query, with their filterable
        columns, whether each is also mirrored locally, and the known traps in each.
        Call this before query_dataset."""
        out = []
        for key, d in DATASETS.items():
            entry = {"dataset": key, "socrata_id": d["id"], "title": d["title"],
                     "measure_column": d["measure"], "filterable_columns": d["columns"],
                     "mirrored_locally": d["mirrored"],
                     "dataset_doc": d["doc"],
                     "endpoint": f"https://{soda.DOMAIN}/resource/{d['id']}.json"}
            if d.get("warning"):
                entry["warning"] = d["warning"]
            out.append(entry)
        return {"datasets": out,
                "note": ("Figures returned by query_dataset are LIVE and carry their own "
                         "executed_at. They are not covered by the corpus's git commit, "
                         "which dates the mirrored documents only."),
                "disclaimer": "non-authoritative; verify at the endpoint shown"}

    @mcp.tool()
    def query_dataset(dataset: str, group_by: str = "", limit: int = 50,
                      fiscal_year: str = "", agency: str = "", budget_class: str = "",
                      expend_class: str = "", vendor: str = "", dept_no: str = "",
                      acct_name: str = "", gl_acct: str = "") -> dict:
        """Query a live dataset with equality filters, optionally aggregating.

        `dataset` is a key from list_datasets. With `group_by` set to a column name the
        result is that column's totals (sum of the dataset's measure, plus a row count),
        largest first; without it, the total for the whole filtered set. Filters are
        combined with AND and only non-empty ones apply. Every response carries the exact
        SoQL executed, the endpoint, and executed_at."""
        d = DATASETS.get(dataset)
        if not d:
            return {"error": f"no dataset {dataset!r}",
                    "available": sorted(DATASETS),
                    "hint": "call list_datasets() for columns and caveats"}

        supplied = {"fiscal_year": fiscal_year, "agency": agency,
                    "budget_class": budget_class, "expend_class": expend_class,
                    "vendor": vendor, "dept_no": dept_no, "acct_name": acct_name,
                    "gl_acct": gl_acct}
        active = {k: v for k, v in supplied.items() if v}
        bad = [k for k in active if k not in d["columns"]]
        if bad:
            return {"error": f"{d['title']} has no column(s): {', '.join(sorted(bad))}",
                    "filterable_columns": d["columns"]}
        if group_by and group_by not in d["columns"]:
            return {"error": f"cannot group by {group_by!r}",
                    "filterable_columns": d["columns"]}

        where = _combine(soda.build_where(**active), d.get("exclude_where"))
        measure = d["measure"]

        if group_by:
            n = max(1, min(int(limit or 50), MAX_GROUPS))
            params = {"$select": f"{group_by}, sum({measure}) AS total, count(*) AS n",
                      "$group": group_by, "$order": "total DESC", "$limit": n}
        else:
            params = {"$select": f"sum({measure}) AS total, count(*) AS n"}
        if where:
            params["$where"] = where

        r = soda.fetch(d["id"], params)
        if not r.ok:
            return {**r.envelope(), "dataset": dataset,
                    "note": "the live API could not be queried — this is NOT a result of "
                            "zero, and must not be reported as one"}

        out = {**r.envelope(), "dataset": dataset, "socrata_id": d["id"],
               "filters_applied": active or None,
               "disclaimer": "non-authoritative; verify at the endpoint shown"}
        if d.get("warning"):
            out["warning"] = d["warning"]
        if group_by:
            out["group_by"] = group_by
            out["groups"] = [{group_by: row.get(group_by), "total": row.get("total"),
                              "records": int(row.get("n") or 0)} for row in r.rows]
            if len(r.rows) == params["$limit"]:
                out["truncated"] = True
                out["note"] = (f"showing the top {params['$limit']} groups; there may be "
                               f"more, and these do NOT sum to the dataset total")
        else:
            row = r.rows[0] if r.rows else {}
            out["total"] = row.get("total")
            out["records"] = int(row.get("n") or 0)
        return out

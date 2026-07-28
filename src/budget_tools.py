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


def register(mcp, framework):
    """Called by corpus-mcp-serve after every built-in tool."""

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

#!/usr/bin/env python3
"""HybridBackend — mirrored documents, with live actuals attached but never merged.

Subclasses FileBackend and overrides exactly three methods. Search, existence probes, and
the FTS index are inherited unchanged: the 547 documents are ordinary markdown and there
is no reason for a hybrid corpus to reimplement retrieval.

THE ONE RULE THIS FILE EXISTS TO ENFORCE
----------------------------------------
Live figures go under a separate top-level `live` key and are NEVER merged into the
mirrored fields. A hybrid corpus has two provenance clocks — the mirror carries a git
commit and a `retrieved:` date, the API carries an `executed_at` and the query that
produced it — and an answer drawing on both must be able to show both. The moment a live
number is written into `total_expense`, the document's own `retrieved` date starts
vouching for a figure it never saw, and a stale citation acquires a fresh-looking
timestamp. That is the most damaging thing this corpus could do, because the result still
looks perfectly well-sourced.

The same rule is why an unreachable API is `live: {upstream_status: "unavailable"}` rather
than an omitted key. Omission is indistinguishable from "this document has no live
counterpart", and silently reads as "no spending recorded" — an API outage rendered as a
fiscal fact.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from corpus_toolkit.mcp.backends import FileBackend

sys.path.insert(0, str(Path(__file__).parent))
import soda  # noqa: E402

EXPENDITURE_DOC = re.compile(r"^expenditures-(\d{3})-fy(\d{4})$")
DATASET = "y9g9-xsxs"


class HybridBackend(FileBackend):
    """FileBackend + a live SODA proxy for the figures the documents mirror."""

    name = "hybrid"

    # Fiscal frontmatter FileBackend does not return. Its `get()` emits a fixed field set
    # drawn from the FTS index — id, title, citation, status, source_url, retrieved and
    # so on — and drops every corpus-specific key. Without these the mirrored figure is
    # invisible to a caller, and `matches_mirror` below has nothing to compare against.
    MIRRORED_FIELDS = ("agency_code", "agency_name", "fiscal_year", "total_expense",
                       "transaction_count")

    def get(self, doc_id: str, *, part: str = "auto") -> dict:
        doc = super().get(doc_id, part=part)
        if "error" in doc:
            return doc
        m = EXPENDITURE_DOC.match(doc_id)
        if not m:
            return doc

        for key, value in self._mirrored_fields(doc.get("path")).items():
            doc.setdefault(key, value)
        doc["live"] = self._live_agency_year(*m.groups(),
                                             mirrored=doc.get("total_expense"))
        return doc

    def _mirrored_fields(self, rel_path) -> dict:
        if not rel_path:
            return {}
        from corpus_toolkit.repo import parse_frontmatter
        fm, _ = parse_frontmatter(self.config.root / rel_path)
        return {k: fm[k] for k in self.MIRRORED_FIELDS if k in fm}

    def _live_agency_year(self, agency: str, year: str, mirrored=None) -> dict:
        """Current API figures for one agency-year, beside the mirrored ones."""
        where = soda.build_where(agency=agency, fiscal_year=year)
        r = soda.fetch(DATASET, {"$select": "sum(expense) AS total, count(*) AS n",
                                 "$where": where})
        if not r.ok:
            # NOT an omitted key and NOT zero. "We could not ask" must stay
            # distinguishable from "the answer is nothing".
            return {**r.envelope(),
                    "note": "live figures unavailable — the mirrored values above stand "
                            "as of their own retrieved date, and have NOT been confirmed "
                            "against the API in this response"}
        row = r.rows[0] if r.rows else {}
        out = {**r.envelope(), "total_expense": row.get("total"),
               "transaction_count": int(row.get("n") or 0)}
        # Restating the upstream figure is not enough; whether it still MATCHES is the
        # thing a reader actually needs, and computing it here means no caller has to.
        if mirrored is not None and row.get("total") is not None:
            from decimal import Decimal
            delta = Decimal(str(row["total"])) - Decimal(str(mirrored))
            out["matches_mirror"] = delta == 0
            if delta:
                out["delta_vs_mirror"] = str(delta)
                out["note"] = ("upstream has been restated since this document was "
                               "generated — the mirrored figure is no longer current")
        return out

    def health(self) -> dict:
        """Both halves, separately.

        A hybrid corpus can be half-broken, and reporting one number hides which half.
        The documents are servable with the API down; they are not servable with an empty
        index, and the two failures need different responses from whoever is paged.
        """
        h = super().health()
        live = soda.count(DATASET)
        h["live"] = {"reachable": live.ok, "dataset": DATASET,
                     "detail": (f"{live.total_count:,} rows" if live.ok else live.detail)}
        if not live.ok:
            h["detail"] = f"{h.get('detail', '')}; live API unreachable ({live.detail})"
        return h

    def overview(self) -> dict:
        o = super().overview()
        o["live_datasets"] = [
            {"dataset": DATASET, "domain": soda.DOMAIN, "protocol": "soda",
             "mirrored": True, "note": "expenditure figures are also mirrored to Parquet"},
        ]
        # `commit` from FileBackend dates the MIRROR. Saying so stops it being read as an
        # as-of date for the live half too.
        o["provenance_note"] = (
            "`commit` dates the mirrored documents only. Live figures carry their own "
            "`executed_at` in each response and are never covered by it.")
        return o

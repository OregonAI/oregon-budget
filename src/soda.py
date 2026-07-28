#!/usr/bin/env python3
"""Socrata SODA client for data.oregon.gov.

Adapted from oregon-legislature's src/odata.py. The protocol differs; the discipline does
not, and the discipline is the part that matters.

THE TRAP, RE-DERIVED FOR SOCRATA (measured 2026-07-28, not assumed):

    GET /resource/y9g9-xsxs.json?$where=fiscal_year='2025'
      -> 1000 rows, HTTP 200, NO Link header
    true count for that filter: 101,178

A single request looks complete and is not. Asking for more does not save you: `$limit=60000`
returns exactly 60,000 of the 101,178. This is the same failure that made the Legislature
spec publish a wrong "66% of measures have a document" figure — 4,000 of 6,178 rows read as
the whole set.

So `fetch_all` reconciles the row count against a separate `count(*)` and RAISES rather than
returning a short list. A truncated ingest is worse than a failed one: it produces a corpus
that looks finished and is quietly missing a third of the money.

A SECOND TRAP, SPECIFIC TO SOCRATA: paging with $offset and no $order is undefined. The
server may return rows in any order, so pages can overlap or skip. Every paged call here
sends an explicit $order, defaulting to :id, which is stable and always present.

THE THREE OUTCOMES ARE NOT TWO. `unavailable` (we could not ask), `found: False` (we asked,
there is nothing), and a result are distinct, and callers must branch on the status rather
than on len(rows). Collapsing "the API is down" into "no spending recorded" is the fiscal
equivalent of the citation bug this platform keeps designing against.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone

DOMAIN = "data.oregon.gov"
BASE = f"https://{DOMAIN}/resource"
USER_AGENT = "oregon-budget corpus (github.com/OregonAI/oregon-budget)"

# Anonymous requests share a low throttle pool; a token raises the ceiling and is free.
# Absent is fine — the ingest is polite and re-runnable.
APP_TOKEN_ENV = "SOCRATA_APP_TOKEN"

PAGE_SIZE = 50_000        # honoured; measured against a 101,178-row year
TIMEOUT_S = 90
MAX_RETRIES = 1
DEFAULT_ROW_CAP = 1_000_000   # above the 668,906-row full corpus, so a normal run is uncapped


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class IncompleteFetch(RuntimeError):
    """Pagination returned fewer rows than the dataset reports, below the cap.

    Deliberately fatal. The alternative is a silently short corpus.
    """


@dataclass
class SodaResult:
    """One SODA call, with everything needed to reproduce and date it.

    The mirrored half of a hybrid corpus has a git commit; this half does not, and says so
    per call. A reader must never be able to assume one as-of date covers both.
    """
    rows: list
    executed_query: str
    executed_at: str
    source: str = DOMAIN
    upstream_status: str = "live"     # live | unavailable | capped
    total_count: int | None = None
    truncated: bool = False
    detail: str = ""
    extra: dict = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return self.upstream_status != "unavailable"

    def envelope(self) -> dict:
        e = {"executed_query": self.executed_query, "executed_at": self.executed_at,
             "source": self.source, "upstream_status": self.upstream_status}
        if self.total_count is not None:
            e["total_count"] = self.total_count
        if self.truncated:
            e["truncated"] = True
        if self.detail:
            e["detail"] = self.detail
        return e


def _quote(v) -> str:
    """SoQL string literal. Doubling the quote is the whole escape."""
    return "'" + str(v).replace("'", "''") + "'"


def build_where(**equals) -> str:
    """AND of equality clauses over caller-named fields.

    Equality only, and the caller names the fields — user text never becomes a SoQL
    expression. That is both the injection guard and the reason `executed_query` is
    something a human can audit in a response envelope.
    """
    return " AND ".join(f"{k} = {_quote(v)}" for k, v in sorted(equals.items()) if v is not None)


def _request(url: str, timeout: int = TIMEOUT_S):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                               "Accept": "application/json"})
    token = os.environ.get(APP_TOKEN_ENV)
    if token:
        req.add_header("X-App-Token", token)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def _url(dataset: str, params: dict) -> str:
    return f"{BASE}/{dataset}.json?" + urllib.parse.urlencode(params)


def fetch(dataset: str, params: dict, timeout: int = TIMEOUT_S) -> SodaResult:
    """One request. Never raises for upstream problems — returns an unavailable result."""
    url = _url(dataset, params)
    started = _utc_now()                     # before the call: a failure still carries a clock
    last = ""
    for attempt in range(MAX_RETRIES + 1):
        try:
            return SodaResult(rows=_request(url, timeout), executed_query=url,
                              executed_at=started)
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            # 429 means the server is asking us to stop; retrying is the wrong answer.
            # Other 4xx are our bug (bad SoQL) and will fail identically next time.
            if e.code == 429 or 400 <= e.code < 500:
                break
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as e:
            last = f"{type(e).__name__}: {e}"
        if attempt < MAX_RETRIES:
            time.sleep(2)
    return SodaResult(rows=[], executed_query=url, executed_at=started,
                      upstream_status="unavailable", detail=last)


def count(dataset: str, where: str = "") -> SodaResult:
    """count(*) for a filter — the number fetch_all reconciles against."""
    p = {"$select": "count(*) AS n"}
    if where:
        p["$where"] = where
    r = fetch(dataset, p)
    if r.ok and r.rows:
        r.total_count = int(r.rows[0].get("n") or r.rows[0].get("count") or 0)
    return r


def fetch_all(dataset: str, where: str = "", select: str = "", order: str = ":id",
              row_cap: int = DEFAULT_ROW_CAP, progress=None) -> SodaResult:
    """Every row matching `where`, or an exception. See the module docstring.

    `order` defaults to `:id` because $offset paging without an explicit sort is undefined
    in SoQL — pages may overlap or skip rows, and nothing in the response says so.
    """
    c = count(dataset, where)
    if not c.ok:
        return SodaResult(rows=[], executed_query=c.executed_query, executed_at=c.executed_at,
                          upstream_status="unavailable",
                          detail=f"could not read count: {c.detail}")
    total = c.total_count or 0

    rows, offset, started = [], 0, _utc_now()
    last_url = c.executed_query
    while offset < min(total, row_cap):
        p = {"$limit": PAGE_SIZE, "$offset": offset, "$order": order,
             "$$exclude_system_fields": "false" if order == ":id" else "true"}
        if where:
            p["$where"] = where
        if select:
            p["$select"] = select
        r = fetch(dataset, p)
        last_url = r.executed_query
        if not r.ok:
            return SodaResult(rows=[], executed_query=last_url, executed_at=started,
                              upstream_status="unavailable",
                              detail=f"page at offset {offset} failed: {r.detail}")
        if not r.rows:
            break
        rows.extend(r.rows)
        offset += len(r.rows)
        if progress:
            progress(len(rows), total)

    if len(rows) >= row_cap and len(rows) < total:
        return SodaResult(rows=rows[:row_cap], executed_query=last_url, executed_at=started,
                          upstream_status="capped", total_count=total, truncated=True,
                          detail=f"stopped at row_cap={row_cap} of {total}")

    if len(rows) != total:
        raise IncompleteFetch(
            f"{dataset}: paged {len(rows)} rows but count(*) reports {total} for "
            f"where={where!r}. Refusing to return a short list — a truncated ingest "
            f"produces a corpus that looks finished and is quietly missing rows. "
            f"(Socrata sends no continuation token; this reconciliation is the only signal.)")

    return SodaResult(rows=rows, executed_query=last_url, executed_at=started,
                      total_count=total)


def schema(dataset: str) -> SodaResult:
    """Dataset metadata — columns, types, update time. Backs `live_schema_hash`."""
    url = f"https://{DOMAIN}/api/views/{dataset}.json"
    started = _utc_now()
    try:
        return SodaResult(rows=[_request(url, 45)], executed_query=url, executed_at=started)
    except Exception as e:
        return SodaResult(rows=[], executed_query=url, executed_at=started,
                          upstream_status="unavailable", detail=f"{type(e).__name__}: {e}")


def schema_hash(view: dict) -> str:
    """sha256 over sorted `fieldName:dataTypeName` pairs, joined with '|'.

    Deliberately excludes width, position, and description: a renamed label or a reordered
    column should not trip drift, while an added, removed, renamed or retyped FIELD should.
    The recipe is stated here and in each dataset doc so it can be reproduced by hand.
    """
    import hashlib
    pairs = sorted(f"{c.get('fieldName')}:{c.get('dataTypeName')}"
                   for c in (view.get("columns") or []))
    return hashlib.sha256("|".join(pairs).encode("utf-8")).hexdigest()


def health(dataset: str) -> dict:
    """Cheap reachability probe for the MCP server's startup line."""
    r = count(dataset)
    return {"reachable": r.ok, "detail": r.detail or f"{r.total_count:,} rows"
            if r.total_count is not None else r.detail, **r.envelope()}

"""The hybrid seam's disciplines, pinned.

These are OFFLINE tests. Every one that needs the API monkeypatches `soda.fetch`, because
a test suite that reaches data.oregon.gov fails when a third party has a bad afternoon and
teaches everyone to ignore it. Live reconciliation is a weekly job, not a per-PR gate.

Two rules are worth a test each, and both are about what must NOT happen:

  1. Live figures never merge into mirrored fields. This corpus has two provenance clocks,
     and the moment a live number lands in `total_expense` the document's own `retrieved`
     date starts vouching for a figure it never saw — a stale citation wearing a fresh
     timestamp, which still looks perfectly well-sourced.

  2. An unavailable API is never a zero. `unavailable`, `found: false`, and a result are
     three outcomes, and collapsing the first into the second turns an outage into the
     fiscal claim "no spending recorded".
"""
import asyncio
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

pytest.importorskip("mcp", reason="needs corpus-toolkit[mcp]")

import soda                                                     # noqa: E402
from corpus_toolkit import config as config_mod                 # noqa: E402
from corpus_toolkit.mcp.framework import CorpusFramework        # noqa: E402
from corpus_toolkit.mcp.server import build_server              # noqa: E402

CONFIG = str(ROOT / "_meta" / "corpus.yml")
DOC = "expenditures-107-fy2024"


@pytest.fixture(scope="module")
def config():
    return config_mod.load(CONFIG)


@pytest.fixture
def offline(monkeypatch):
    """Every SODA call fails, as if the API were down."""
    def dead(dataset, params, timeout=90):
        return soda.SodaResult(rows=[], executed_query="offline", executed_at="now",
                               upstream_status="unavailable", detail="simulated outage")
    monkeypatch.setattr(soda, "fetch", dead)


@pytest.fixture
def canned(monkeypatch):
    """SODA returns a figure that DIFFERS from the mirror, simulating a restatement."""
    def fake(dataset, params, timeout=90):
        return soda.SodaResult(rows=[{"total": "999.99", "n": "7"}],
                               executed_query="canned", executed_at="2026-01-01T00:00:00Z")
    monkeypatch.setattr(soda, "fetch", fake)


def call(mcp, name, **kw):
    return asyncio.run(mcp._tool_manager.call_tool(name, kw))


# ---------------------------------------------------------------- registration

def test_corpus_tools_are_registered(config):
    names = {t.name for t in build_server(config)._tool_manager.list_tools()}
    assert {"list_datasets", "query_dataset"} <= names
    # The seam must ADD to the built-ins, never replace them.
    assert {"search_corpus", "get_document", "corpus_overview"} <= names


def test_backend_is_the_hybrid_one(config):
    assert CorpusFramework(config).backend.name == "hybrid"


# ------------------------------------------------- rule 1: never merge clocks

def test_live_figures_never_overwrite_mirrored_ones(config, canned):
    """The regression. Upstream says 999.99; the mirrored field must be untouched."""
    doc = CorpusFramework(config).get_document(DOC)
    assert doc["total_expense"] != "999.99", (
        "a live figure was written into a mirrored field — the document's `retrieved` "
        "date now vouches for a number it never saw")
    assert doc["live"]["total_expense"] == "999.99"
    assert doc["retrieved"] != doc["live"]["executed_at"], "the two clocks must differ"


def test_a_restatement_is_reported_not_hidden(config, canned):
    live = CorpusFramework(config).get_document(DOC)["live"]
    assert live["matches_mirror"] is False
    assert "delta_vs_mirror" in live
    assert "restated" in live["note"]


def test_matching_upstream_says_so(config, monkeypatch):
    fw = CorpusFramework(config)
    mirrored = fw.get_document(DOC)["total_expense"]
    monkeypatch.setattr(soda, "fetch", lambda d, p, timeout=90: soda.SodaResult(
        rows=[{"total": str(mirrored), "n": "1"}], executed_query="c", executed_at="t"))
    live = CorpusFramework(config).get_document(DOC)["live"]
    assert live["matches_mirror"] is True
    assert "delta_vs_mirror" not in live


# --------------------------------------------- rule 2: unavailable is not zero

def test_outage_is_not_a_zero_in_get_document(config, offline):
    doc = CorpusFramework(config).get_document(DOC)
    assert doc["live"]["upstream_status"] == "unavailable"
    assert "total_expense" not in doc["live"], "an outage was rendered as a figure"
    # The mirrored half must still be servable — that is the point of mirroring.
    assert doc["total_expense"]


def test_outage_is_not_a_zero_in_query_dataset(config, offline):
    r = call(build_server(config), "query_dataset", dataset="expenditures", agency="107")
    assert r["upstream_status"] == "unavailable"
    assert "total" not in r, "an outage was rendered as a total"
    assert "NOT a result of zero" in r["note"]


def test_health_reports_both_halves_separately(config, offline):
    h = CorpusFramework(config).backend.health()
    assert h["reachable"] is True, "documents stay servable when the API is down"
    assert h["live"]["reachable"] is False, "a half-broken corpus must say which half"


# ----------------------------------------------------- the totals-row trap

def test_budgeted_revenue_always_excludes_its_own_totals_row(config, monkeypatch):
    """Summing all 80 rows reports exactly double the biennial budget. Every query this
    tool issues must carry the exclusion, whatever else the caller asked for."""
    seen = {}

    def capture(dataset, params, timeout=90):
        seen.update(params)
        return soda.SodaResult(rows=[{"total": "1", "n": "1"}], executed_query="c",
                               executed_at="t")

    monkeypatch.setattr(soda, "fetch", capture)
    mcp = build_server(config)

    call(mcp, "query_dataset", dataset="budgeted_revenue")
    assert "dept_no != 'Totals'" in seen["$where"]

    seen.clear()
    call(mcp, "query_dataset", dataset="budgeted_revenue", dept_no="10700")
    assert "dept_no != 'Totals'" in seen["$where"], "exclusion dropped once a filter was added"


# ------------------------------------------------------------- input handling

def test_unknown_dataset_lists_the_real_ones(config):
    r = call(build_server(config), "query_dataset", dataset="nope")
    assert "error" in r and set(r["available"]) == {"expenditures", "budgeted_revenue",
                                                    "lottery"}


def test_unknown_column_is_refused_rather_than_passed_to_soql(config):
    r = call(build_server(config), "query_dataset", dataset="lottery", agency="107")
    assert "error" in r and "agency" in r["error"]
    assert "fiscal_year" in r["filterable_columns"]


def test_quotes_in_a_filter_cannot_break_out_of_the_literal(config):
    assert soda.build_where(vendor="O'BRIEN") == "vendor = 'O''BRIEN'"
    assert soda.build_where(vendor="x' OR '1'='1") == "vendor = 'x'' OR ''1''=''1'"


def test_truncated_groups_say_they_do_not_sum(config, monkeypatch):
    def fake(dataset, params, timeout=90):
        # build_server() calls health() first, which is an unlimited count(*) — assuming
        # every call carries $limit is what made the first version of this test fail.
        n = params.get("$limit")
        rows = ([{"agency": str(i), "total": "1", "n": "1"} for i in range(n)] if n
                else [{"n": "1"}])
        return soda.SodaResult(rows=rows, executed_query="c", executed_at="t")

    monkeypatch.setattr(soda, "fetch", fake)
    r = call(build_server(config), "query_dataset", dataset="expenditures",
             group_by="agency", limit=5)
    assert r["truncated"] is True and "do NOT sum" in r["note"]


def test_list_datasets_carries_the_warnings(config):
    by_key = {d["dataset"]: d for d in call(build_server(config), "list_datasets")["datasets"]}
    assert "Totals row" in by_key["budgeted_revenue"]["warning"]
    assert "NOT part of the statewide" in by_key["lottery"]["warning"]


# ------------------------------------------------ unreviewed extractions

def test_unreviewed_appropriations_are_flagged_not_served_as_fact(config):
    """Stage 3 figures are read out of bill prose by a regex. A misparse wearing a real
    bill citation is the most credible-looking wrong answer this corpus could produce, so
    every response must carry a block an agent cannot mistake for provenance."""
    doc = CorpusFramework(config).get_document("appropriations-2025r1-hb2408")
    r = doc["review_status"]
    assert r["human_reviewed"] is False
    assert r["servable_as_fact"] is False
    assert "UNREVIEWED" in r["warning"]
    # It must point at text a caller can actually trust instead.
    assert r["authoritative_text"] == "measure-2025r1-hb2408"


def test_mirrored_documents_carry_no_review_block(config):
    """The flag must mean something. Attaching it to everything would make it noise."""
    assert "review_status" not in CorpusFramework(config).get_document(DOC)

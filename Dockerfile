# MCP server for the oregon-budget corpus (HTTP transport).
#
#   docker build -t oregon-budget-mcp .
#   docker run -p 8000:8000 oregon-budget-mcp
#
# The mirrored corpus is baked in at build time; rebuild the image to pick up new commits.
#
# BUILD FROM A SHALLOW CLONE, not your working tree. `.git` cannot be excluded — it is a
# RUNTIME dependency, because the FTS cache key is `git rev-parse HEAD` plus a hash of
# `git status --porcelain`, and corpus_overview() shells out to `git log -1`. A depth-1
# clone keeps git working and the image small:
#
#   git clone --depth 1 --branch main https://github.com/OregonAI/oregon-budget build/
#   docker build -t oregon-budget-mcp build/
#
# HYBRID ARCHETYPE — this container needs NETWORK EGRESS at runtime.
# plugins.retrieval_module is src.budget_backend:HybridBackend and plugins.tools_module
# registers query_dataset/list_datasets/join_lookup, all of which reach data.oregon.gov.
# With egress blocked the server still starts and every mirrored document still serves;
# only the live half degrades — and it degrades HONESTLY, reporting
# upstream_status: "unavailable" rather than a zero. That distinction is tested
# (tests/test_hybrid.py) precisely because an outage rendered as $0 would be a fabricated
# fiscal claim.
#
# WHY requirements.txt AND NOT requirements-build.txt: the server never reads the Parquet.
# pyarrow and duckdb are the mirror/analysis stack and would add ~60 MB of wheels that no
# request touches. The committed data/ Parquet is still in the image because it is in the
# repo and git must stay clean — it just is not read at runtime.
FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /repo
# Deps BEFORE content: a content-only change must not re-run pip. With these two steps the
# other way round -- how this read until 2026-07-30 -- every edited document invalidated the
# COPY layer and forced a full reinstall.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Pre-build the FTS index so the first request is instant, and fail the BUILD if content is
# missing rather than shipping an image that starts fine and answers nothing.
#
# NOTE this runs HybridBackend, which subclasses FileBackend and so inherits
# ensure_index() unchanged — it overrides only get/health/overview. If the build host has
# no egress this still succeeds: indexing reads the committed markdown, not the API.
RUN python3 -c "\
from corpus_toolkit import config as config_mod; \
from corpus_toolkit.mcp.framework import CorpusFramework; \
CorpusFramework(config_mod.load('_meta/corpus.yml')).ensure_index()"
EXPOSE 8000

# --path and --public-hostname both matter behind the tunnel and are easy to omit:
#   * A Cloudflare Tunnel matches on path but does NOT strip it. Routing /oregon-budget
#     here forwards the whole path, so the server must mount at that same prefix or every
#     request 404s.
#   * Without --public-hostname the SDK's DNS-rebinding guard rejects the forwarded Host
#     header with 421 Invalid Host header.
# Override either at `docker run` for a different hostname or a dedicated-host deployment
# (in which case pass --path /mcp).
CMD ["corpus-mcp-serve", "--config", "_meta/corpus.yml", "--http", \
     "--host", "0.0.0.0", "--port", "8000", \
     "--path", "/oregon-budget/mcp", \
     "--public-hostname", "oregonai.morficflux.com"]

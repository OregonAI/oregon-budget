#!/usr/bin/env python3
"""ORBITS/SFMA account codes: what a `budget_class` and an `expend_class` actually are.

  python3 src/build_account_codes.py --refresh   # ONLINE: re-read DAS's PDF, rewrite both
  python3 src/build_account_codes.py             # OFFLINE: rebuild the doc from the catalog
  python3 src/build_account_codes.py --check     # OFFLINE: exit 1 if the doc would change

WHAT THIS ADDS THAT THE DATA DOES NOT ALREADY CARRY. `budget_class` and `expend_class` are
both already columns in the mirrored expenditure data, so this is not a new dimension. What
was missing is the AUTHORITY for how they relate: the data shows which pairs co-occur, the
crosswalk states which pairing DAS intends. Those are different claims, and the difference
is where the findings are -- see disagreements().

THE BAND TAXONOMY IS NOT IN THE SOURCE. The crosswalk PDF is three columns of codes and
titles; nowhere does it say that the leading digit is a category. It is a convention you
either know or do not, and encoding it is most of the value here:

    0000-0999  revenue            beginning balance, taxes, fees, federal funds
    1000-2999  transfers          transfers in and out
    3000-3999  personnel          salaries, per diem, benefits
    4000-4999  services_supplies  the ordinary operating budget
    5000-5999  capital_outlay     durable assets -- named by 5900 "Other Capital Outlay"
    6000-6999  distributions      payments out to cities, counties, individuals
    7000-7999  debt_service       bonds, COPs, principal and interest
    8000-8999  positions_fte      POSITION COUNTS AND FTE -- NOT DOLLARS
    9000-9999  reversions         9900, unspent appropriation returning

THE 8000 BAND IS THE REASON THIS IS WORTH ENCODING. 8150-8195 are position counts and
8250-8295 are FTE: authority to employ people, denominated in people, sharing a code space
with dollars. A total taken over codes without excluding them adds headcount to money and
produces a number that is not money and looks like it.

Measured against the mirrored data: ZERO expenditure rows carry an 8000-series budget_class,
so no total in this corpus is currently wrong. That is a fact about SFMA actuals, not a
property of the code space -- the band exists in ORBITS, and anything that later ingests
budget-side data will meet it. `monetary: false` is recorded so the guard outlives the
person who knew.

WHY --refresh AND --check ARE SEPARATE, AND WHY THE SPLIT IS NOT COSMETIC. The `generated`
job in ci.yml installs pyyaml and duckdb and nothing else, and says of itself that its
checks are "deliberately OFFLINE". `_meta/.cache/` is gitignored, so in CI there is no
cached PDF. An earlier draft of this file had one build path: --check re-fetched the
crosswalk and imported pypdf. That would either fail in CI or make a green build depend on
oregon.gov being reachable that minute.

So the COMMITTED CATALOGUE is the source of truth for codes, and the document is derived
from it. Only --refresh touches the network or pypdf. Drift from DAS is caught in review by
running --refresh, never by CI reaching out mid-build. build_joins.py makes the same split
for the same reason: it needs a sibling checkout to build and deliberately does not to
check.

Two distinctions the band structure makes visible, both invisible in a flat code list:

  * 5800 "Professional Services" (capital outlay) and 4300 "Professional Services" (services
    and supplies) are the same words in different bands, and are different things.
  * `x90`/`x95` recur across bands as BAM and LFO analyst adjustments -- 5990/5995,
    8190/8195, 8290/8295. A sub-convention, not separate concepts.
"""
from __future__ import annotations

import argparse
import glob
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "_meta" / "catalog" / "account-codes.yml"
DOC = ROOT / "datasets" / "account-code-structure.md"
CACHE = ROOT / "_meta" / ".cache" / "orbits-sfma-crosswalk.pdf"

SOURCE_URL = ("https://www.oregon.gov/das/Financial/Documents/"
              "ORBITS-SFMA-ACCOUNT-CROSSWALK.pdf")

# (low, high, id, label, monetary)
BANDS = [
    (0, 999, "revenue", "Revenue", True),
    (1000, 2999, "transfers", "Transfers", True),
    (3000, 3999, "personnel", "Personnel services", True),
    (4000, 4999, "services_supplies", "Services and supplies", True),
    (5000, 5999, "capital_outlay", "Capital outlay", True),
    (6000, 6999, "distributions", "Distributions", True),
    (7000, 7999, "debt_service", "Debt service", True),
    # NOT DOLLARS. See the module docstring.
    (8000, 8999, "positions_fte", "Positions and FTE", False),
    (9000, 9999, "reversions", "Reversions", True),
]
BAND_LABEL = {b[2]: b[3] for b in BANDS}

# A full row: ORBITS account + description, its comparative source group, and one D10
# comparative object beneath it.
#
# ANCHORED ON THE CODES, NOT ON WHAT A TITLE MAY CONTAIN. An earlier version spelled the
# titles out as character classes and silently lost 12 of the 20 capital-outlay accounts,
# because SFMA titles carry a threshold: `TELECOM/VOICE EQUIPMENT>=$5K` contains `>`, `=`
# and `$`, none of which were in the class. The row then matched neither pattern and the
# account disappeared from the catalogue entirely -- no error, just a band that came out at
# 8 accounts instead of 20.
#
# Requiring WHITESPACE around each 4-digit code is what keeps the non-greedy titles honest:
# the `5000` inside `$5000` is not preceded by a space, so it cannot be mistaken for a code.
ROW = re.compile(r"^(\d{4})\s+(.+?)\s+(\d{4})\s+(.+?)\s+(\d{4})\s+(.+?)\s*$")
# An ORBITS account with NO R*STARS counterpart -- budget-side concepts such as Beginning
# Balance and General Fund Appropriation, which can never appear in expenditure data.
ACCT_ONLY = re.compile(r"^(\d{4})\s+([A-Za-z].*?)\s*$")
HEADER = ("orbits", "r*stars", "compt", "comp ", "account ", "d10 ")


def band_of(code: str) -> tuple[str, bool]:
    n = int(code)
    for lo, hi, bid, _label, monetary in BANDS:
        if lo <= n <= hi:
            return bid, monetary
    return "unknown", True


# --------------------------------------------------------------- ONLINE half (--refresh)

def crosswalk_text() -> str:
    """DAS's PDF as text. The ONLY function that needs the network or pypdf."""
    if not CACHE.is_file():
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "OregonAI-corpus"})
        with urllib.request.urlopen(req, timeout=180) as r:
            body = r.read()
        if not body.startswith(b"%PDF"):
            sys.exit(f"{SOURCE_URL} did not return a PDF ({len(body)} bytes)")
        CACHE.write_bytes(body)
    from pypdf import PdfReader                      # noqa: PLC0415 — deliberately local
    return "\n".join((p.extract_text() or "") for p in PdfReader(str(CACHE)).pages)


def parse(text: str) -> dict:
    accounts: dict[str, dict] = {}
    objects: dict[str, list] = defaultdict(list)
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.lower().startswith(HEADER):
            continue
        m = ROW.match(line)
        if m:
            acct, desc, csg, _csg_title, d10, d10_title = m.groups()
            accounts.setdefault(acct, {"title": desc.strip(), "csg": csg})
            objects[acct].append({"code": d10, "title": d10_title.strip()})
            continue
        m = ACCT_ONLY.match(line)
        if m:
            accounts.setdefault(m.group(1), {"title": m.group(2).strip(), "csg": None})

    out: dict[str, dict] = {}
    for code in sorted(accounts):
        bid, monetary = band_of(code)
        e: dict = {"title": accounts[code]["title"], "band": bid}
        if not monetary:
            e["monetary"] = False
        csg = accounts[code]["csg"]
        # 355 of 355 ORBITS accounts equal their comparative source group. Recorded only
        # where it DIFFERS, so the file does not restate the code 355 times and a future
        # divergence is visible instead of buried.
        if csg and csg != code:
            e["comp_source_group"] = csg
        if objects.get(code):
            e["comp_objects"] = sorted(objects[code], key=lambda o: o["code"])
        out[code] = e
    return out


def catalog_text(accounts: dict) -> str:
    counts: dict[str, int] = defaultdict(int)
    for e in accounts.values():
        counts[e["band"]] += 1
    return yaml.safe_dump({
        "note": (
            "ORBITS budget accounts and the R*STARS (SFMA) comparative objects beneath them, "
            "from DAS's published crosswalk. `band` is the category the LEADING DIGIT "
            "encodes -- a convention the source PDF never states, which is most of why this "
            "file exists. `monetary: false` marks the 8000 band: those are POSITION COUNTS "
            "AND FTE, not dollars, and summing them with money produces a figure that is not "
            "money. Generated by src/build_account_codes.py --refresh; do not hand-edit."),
        "source_url": SOURCE_URL,
        "bands": [{"id": bid, "label": label, "range": f"{lo:04d}-{hi:04d}",
                   "monetary": mon, "accounts": counts.get(bid, 0)}
                  for lo, hi, bid, label, mon in BANDS],
        "accounts": accounts,
    }, sort_keys=False, allow_unicode=True, width=98)


# -------------------------------------------------------- OFFLINE half (default, --check)

def load_catalog() -> dict:
    if not CATALOG.is_file():
        sys.exit(f"{CATALOG.relative_to(ROOT)} is missing — run --refresh (needs network)")
    return yaml.safe_load(CATALOG.read_text(encoding="utf-8")) or {}


def audit_catalog(cat: dict) -> list[str]:
    """The catalogue must still say what the code space says.

    Comparing the generated document against the committed one does NOT cover this: the
    document is a band-level summary, so a hand-edit that moves account 4100 into
    `capital_outlay`, or flips `monetary` on the 8000 band, changes no rendered line and
    passes silently. The band assignment is the whole claim this file makes, and it is
    derivable from the code itself, so it is checked rather than trusted.
    """
    bad = []
    accounts = cat.get("accounts") or {}
    counts: dict[str, int] = defaultdict(int)
    for code, e in accounts.items():
        if not re.fullmatch(r"\d{4}", code):
            bad.append(f"{code}: not a four-digit account code")
            continue
        want_band, want_monetary = band_of(code)
        counts[e.get("band")] += 1
        if e.get("band") != want_band:
            bad.append(f"{code}: band is {e.get('band')!r}, its number says {want_band!r}")
        # `monetary` is written only when False, so its presence and the band must agree in
        # both directions -- a stray `monetary: false` on a dollar account would quietly
        # exclude real spending from any total that honours the flag.
        if want_monetary and "monetary" in e:
            bad.append(f"{code}: carries `monetary` but band {want_band} IS monetary")
        if not want_monetary and e.get("monetary") is not False:
            bad.append(f"{code}: band {want_band} is not dollars and must say monetary: false")
    for b in cat.get("bands") or []:
        if counts.get(b["id"], 0) != b.get("accounts"):
            bad.append(f"band {b['id']}: header says {b.get('accounts')} accounts, "
                       f"{counts.get(b['id'], 0)} present")
    return bad


def disagreements(accounts: dict) -> dict:
    """Compare the authority against the pairings the mirrored data actually contains.

    Reported, never applied. The crosswalk is a point-in-time snapshot and the mirror spans
    FY2019-FY2025, so rewriting history to match it would silently re-attribute spending.
    Reads the COMMITTED Parquet, so this stays offline.
    """
    files = sorted(glob.glob(str(ROOT / "data" / "**" / "*.parquet"), recursive=True))
    if not files:
        return {}
    import duckdb                                     # noqa: PLC0415
    pairs = duckdb.connect().execute(
        f"select distinct budget_class, expend_class from read_parquet({files!r})").fetchall()
    owner = {o["code"]: code for code, e in accounts.items()
             for o in (e.get("comp_objects") or [])}

    # ZERO-PAD BEFORE COMPARING. Socrata returns some codes without their leading zero, so
    # the mirror holds `755` where the crosswalk holds `0755`. Compared raw, that reads as
    # the data and DAS disagreeing about which account a comparative object belongs to --
    # a finding, published in the document, and entirely an artefact of formatting. The
    # codes are fixed-width four-digit throughout both systems.
    def pad(c: str) -> str:
        return c.zfill(4) if c and c.isdigit() else c

    pairs = [(pad(bc), pad(ec)) for bc, ec in pairs]
    dis = sorted(({"expend_class": ec, "data": bc, "crosswalk": owner[ec]}
                  for bc, ec in pairs if ec in owner and owner[ec] != bc),
                 key=lambda d: d["expend_class"])
    return {"pairs": len(pairs),
            "agree": sum(1 for bc, ec in pairs if owner.get(ec) == bc),
            "disagree": dis,
            "absent": sorted({ec for _bc, ec in pairs if ec not in owner})}


def doc_text(cat: dict) -> str:
    accounts = cat.get("accounts") or {}
    counts: dict[str, int] = defaultdict(int)
    for e in accounts.values():
        counts[e["band"]] += 1
    n_obj = sum(len(e.get("comp_objects") or []) for e in accounts.values())
    n_leaf = sum(1 for e in accounts.values() if not e.get("comp_objects"))
    f = disagreements(accounts)

    fm = {
        "schema_version": 1, "corpus": "oregon-budget", "jurisdiction": "oregon",
        "id": "account-code-structure",
        "title": "Dataset doc: ORBITS/SFMA account code structure",
        "doc_type": "entity_doc",
        "citation": "DAS ORBITS to SFMA Account Crosswalk",
        "issuing_body": "Oregon Department of Administrative Services",
        "source_url": SOURCE_URL, "source_format": "pdf",
        "snapshot_policy": "hash-only", "status": "current", "content_mode": "summary",
        "last_verified": "", "verified_by": "", "maintainer": "@dzinck",
        "conversion_notes": (
            "Codes and titles are transcribed from the source crosswalk. The BAND taxonomy is "
            "NOT stated in the source — it is the convention that the leading digit encodes a "
            "category, recorded here because nothing else in this corpus carries it."),
        "relationships": {"implements": [], "implemented_by": [], "references_external": [],
                          "related": ["agency-expenditures"], "supersedes": []},
        "tags": ["oregon-budget", "reference", "account-codes"],
    }
    p = [f"---\n{yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100).rstrip()}\n---\n",
         "## At a glance\n",
         f"**{len(accounts)} ORBITS budget accounts.** {len(accounts) - n_leaf} map to "
         f"{n_obj} R*STARS (SFMA) comparative objects beneath them; **{n_leaf} have no SFMA "
         f"counterpart at all** — budget-side concepts such as Beginning Balance and General "
         f"Fund Appropriation, which can never appear in expenditure data.\n\n"
         "This is what the `budget_class` and `expend_class` columns of the mirrored "
         "expenditure data contain: `budget_class` is the ORBITS account, `expend_class` is "
         "the comparative object beneath it.\n\n"
         "_NON-AUTHORITATIVE. Verify at the source URL._\n",
         "\n## The leading digit is a category\n",
         "The source crosswalk never states this. It is a convention, and it is what makes a "
         "bare four-digit code readable.\n",
         "\n| Range | Band | Accounts | Monetary |\n|---|---|---:|---|"]
    for lo, hi, bid, label, mon in BANDS:
        p.append(f"| {lo:04d}–{hi:04d} | {label} | {counts.get(bid, 0)} | "
                 f"{'yes' if mon else '**no — counts, not dollars**'} |")
    p.append(
        "\n### The 8000 band is not money\n\n"
        "`8150`–`8195` are position counts and `8250`–`8295` are FTE — authority to employ "
        "people, denominated in people, sharing a code space with dollars. A total taken over "
        "codes without excluding them adds headcount to money and yields a figure that is not "
        "money and looks like it.\n\n"
        "No expenditure row in this corpus carries an 8000-series code, so no total here is "
        "currently wrong. That is a fact about SFMA actuals rather than about the code space: "
        "the band exists in ORBITS, and anything that later ingests budget-side data will "
        "meet it.\n\n"
        "### Two things the bands make visible\n\n"
        "- `5800 Professional Services` (capital outlay) and `4300 Professional Services` "
        "(services and supplies) are the same words in different bands, and are different "
        "things.\n"
        "- `x90` and `x95` recur across bands as Budget and Management and Legislative Fiscal "
        "Office analyst adjustments — `5990`/`5995`, `8190`/`8195`, `8290`/`8295`. A "
        "sub-convention, not separate concepts.\n")
    if f:
        p.append(
            "\n## Where the mirrored data disagrees with the crosswalk\n\n"
            f"Of {f['pairs']} distinct `(budget_class, expend_class)` pairings in the mirrored "
            f"expenditure data, **{f['agree']} agree** with this crosswalk, "
            f"**{len(f['disagree'])} disagree**, and **{len(f['absent'])} comparative objects "
            "do not appear in it at all**.\n\n"
            "Reported, not corrected. The crosswalk is a point-in-time snapshot and the mirror "
            "spans FY2019–FY2025, so applying it to historical rows would silently "
            "re-attribute spending. The disagreements are also not purely chronological — some "
            "comparative objects appear under two different accounts *within the same fiscal "
            "year*, which the crosswalk cannot express and which is a property of the source "
            "data.\n")
        if f["disagree"]:
            p.append("\n| Comparative object | Data says | Crosswalk says |\n|---|---|---|")
            p += [f"| `{d['expend_class']}` | `{d['data']}` | `{d['crosswalk']}` |"
                  for d in f["disagree"]]
    p.append("\n## Accounts\n\nFull machine-readable table, with every comparative object: "
             "[`_meta/catalog/account-codes.yml`](../_meta/catalog/account-codes.yml).\n")
    return "\n".join(p) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--refresh", action="store_true",
                    help="re-read DAS's crosswalk (NEEDS NETWORK) and rewrite the catalogue")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the document is stale (offline)")
    args = ap.parse_args()

    if args.refresh:
        accounts = parse(crosswalk_text())
        if len(accounts) < 300:
            sys.exit(f"only {len(accounts)} accounts parsed — the source layout has changed")
        CATALOG.parent.mkdir(parents=True, exist_ok=True)
        CATALOG.write_text(catalog_text(accounts), encoding="utf-8")
        print(f"wrote {CATALOG.relative_to(ROOT)}: {len(accounts)} accounts, "
              f"{sum(len(e.get('comp_objects') or []) for e in accounts.values())} "
              f"comparative objects")

    cat = load_catalog()
    problems = audit_catalog(cat)
    if problems:
        for p in problems:
            print(f"  FAIL {p}", file=sys.stderr)
        print(f"{len(problems)} problem(s) in {CATALOG.relative_to(ROOT)}", file=sys.stderr)
        return 1

    text = doc_text(cat)
    if args.check:
        if not DOC.exists() or DOC.read_text(encoding="utf-8") != text:
            print(f"{DOC.relative_to(ROOT)} is stale — run: "
                  f"python3 src/build_account_codes.py", file=sys.stderr)
            return 1
        print(f"{DOC.relative_to(ROOT)} is current "
              f"({len(cat.get('accounts') or {})} accounts).")
        return 0
    DOC.write_text(text, encoding="utf-8")
    print(f"wrote {DOC.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

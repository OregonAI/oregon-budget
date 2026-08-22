#!/usr/bin/env python3
"""Validate _meta/agency-crosswalk.yml — every agency string is a recorded DECISION.

  python3 src/link_agency_registry.py --check            # CI: committed data only
  python3 src/link_agency_registry.py --verify-registry  # local: slugs + numbers vs ERF
  python3 src/link_agency_registry.py --stamp            # write basis into joins/

Adapted from oregon-audits/src/link_agency_registry.py, which in turn adapts
oregon-kpm's. Same shape, same --check / --verify-registry split, same governing
principle: an entry under `unmapped` is a decision with a stated reason, never a blank.

WHAT IS DELIBERATELY DIFFERENT HERE. Those corpora crosswalk one name space; this one
records two. Expenditure documents carry `agency_name`, an abbreviated all-caps string
from the state feed, and it is the REQUIRED domain — a string in neither block is a
failure. Bill documents carry `appropriated_to`, resolved at build time by
src/build_joins.py and out of scope for #23, so those strings are PERMITTED but not
required. The orphan check runs against the union, which is what lets the bodies
_meta/unresolved-agencies.md finds no counterpart for be recorded here without being
reported as entries matching nothing.

CI MUST NOT NEED ERF. --check reads only what is committed in this repo.
--verify-registry is the sibling-dependent half, and it exits 2 — never 0 — when the
sibling is absent, because reporting "verified" for a comparison that never ran is the
failure this platform keeps rediscovering.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
EXPENDITURES = ROOT / "expenditures"
BILLS = ROOT / "bills"
JOINS = ROOT / "joins"
CROSSWALK = ROOT / "_meta" / "agency-crosswalk.yml"

REGISTRY_CORPUS = "executive-regulatory-frameworks"
REGISTRY_CANDIDATES = [
    ROOT.parent / "executive-regulatory-frameworks" / "_meta" / "catalog" / "agencies.yml",
    ROOT.parent / "oregon-policy-repo" / "_meta" / "catalog" / "agencies.yml",
]

MAPPING_BASES = {"exact", "das_number", "alias"}
UNMAPPED_BASES = {"reviewed", "not-reviewed"}
# Words that look like a reason and state none.
PLACEHOLDERS = {"todo", "tbd", "n/a", "na", "none", "-", "--", "?", "unknown",
                "fixme", "xxx", "tk", "pending", "see above"}


def frontmatter(path: Path) -> dict:
    parts = path.read_text(encoding="utf-8", errors="replace").split("---\n", 2)
    return yaml.safe_load(parts[1]) if len(parts) >= 3 else {}


def load_crosswalk(path: Path = CROSSWALK) -> dict:
    if not path.is_file():
        sys.exit(f"missing {path}")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def corpus_names(root: Path = EXPENDITURES) -> dict[str, int]:
    """{expenditure agency_name: document count}. The REQUIRED domain."""
    out: dict[str, int] = {}
    for p in sorted(root.glob("*.md")):
        name = frontmatter(p).get("agency_name")
        if name:
            out[name] = out.get(name, 0) + 1
    return out


def bill_names(root: Path = BILLS) -> dict[str, int]:
    """{bill appropriated_to: document count}. The PERMITTED domain."""
    out: dict[str, int] = {}
    for p in sorted(root.glob("*.md")):
        name = (frontmatter(p).get("appropriated_to") or "").strip()
        if name:
            out[name] = out.get(name, 0) + 1
    return out


SECTION_4_RE = re.compile(r"^## 4\..*$", re.M)


def report_bodies(text: str) -> list[str]:
    """The bodies named in section 4 of _meta/unresolved-agencies.md.

    Parsed from the COMMITTED markdown rather than recomputed, because recomputing that
    section means re-running the report's fuzzy suggester against ERF — and --check must
    pass with no sibling present. What is being gated is what the committed report SAYS,
    which is the thing a reader reads.
    """
    m = SECTION_4_RE.search(text)
    if not m:
        return []
    body = text[m.end():].split("\n## ", 1)[0].split("\n---", 1)[0]
    out = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        first = cells[0]
        if not first or set(first) <= set("-: ") or first.lower() == "bill says":
            continue
        out.append(first)
    return out


def check(cw: dict, names: dict[str, int], bills: dict[str, int],
          stamped: list[dict], section_4_bodies: list[str] = ()) -> list[str]:
    """Committed-data-only validation. Never touches the sibling.

    Returns a list of problems, each NAMING the offending string — a count alone sends
    the reader back to diff two files by hand.
    """
    mapping = cw.get("mapping") or {}
    unmapped = cw.get("unmapped") or {}
    bad: list[str] = []

    missing = sorted(set(names) - set(mapping) - set(unmapped))
    if missing:
        # An agency nobody has classified is the state this file exists to make impossible.
        bad.append(f"{len(missing)} expenditure agency_name string(s) in neither mapping "
                   f"nor unmapped: {missing[:5]}")

    both = sorted(set(mapping) & set(unmapped))
    if both:
        bad.append(f"{len(both)} string(s) are both mapped and unmapped: {both[:5]}")

    # The domain is the UNION: expenditure agency_name (required) plus bill
    # appropriated_to (permitted). An entry outside it names nothing in the corpus.
    domain = set(names) | set(bills)
    stale = sorted((set(mapping) | set(unmapped)) - domain)
    if stale:
        bad.append(f"{len(stale)} crosswalk entry/entries name a string no document "
                   f"contains: {stale[:5]}")

    for k, v in sorted(mapping.items()):
        if not isinstance(v, dict):
            bad.append(f"{k}: mapping entry is not a block")
            continue
        if not v.get("slug"):
            bad.append(f"{k}: mapping entry has no slug")
        basis = v.get("basis")
        if basis not in MAPPING_BASES:
            bad.append(f"{k}: basis={basis!r} (must be one of {sorted(MAPPING_BASES)})")
        # `das_number` asserts that a NUMBER joins the two sides. An entry claiming it
        # without naming the number asserts nothing --verify-registry can re-test.
        if basis == "das_number" and not v.get("das_agency_number"):
            bad.append(f"{k}: basis=das_number requires a das_agency_number")
        # An alias asserts an identity the names do not state and no number carries, so
        # it must say why and who accepted it. This is the rule that stops a fuzzy
        # suggestion being quietly promoted into a fact.
        if basis == "alias":
            for field in ("note", "reviewed_by", "reviewed_on"):
                if not v.get(field):
                    bad.append(f"{k}: basis=alias requires {field}")

    for k, v in sorted(unmapped.items()):
        if not isinstance(v, dict):
            bad.append(f"{k}: unmapped entry is not a block")
            continue
        reason = (v.get("reason") or "").strip()
        if not reason or reason.lower().rstrip(".") in PLACEHOLDERS:
            # "we looked and there is no counterpart" and "nobody has looked yet" must
            # not be the same state, and a blank makes them one.
            bad.append(f"{k}: unmapped entries require a reason "
                       f"(got {v.get('reason')!r})")
        if not (v.get("checked") or "").strip():
            # What was TESTED, kept apart from what was CONCLUDED.
            bad.append(f"{k}: unmapped entries require a `checked` line saying what was "
                       f"actually tested")
        basis = v.get("basis")
        if basis not in UNMAPPED_BASES:
            bad.append(f"{k}: basis={basis!r} (must be one of {sorted(UNMAPPED_BASES)})")
        # `reviewed` is the POSITIVE claim. Making it attributable is what stops it being
        # the default word for an absence nobody investigated.
        if basis == "reviewed" and not (v.get("source")
                                        or (v.get("reviewed_by") and v.get("reviewed_on"))):
            bad.append(f"{k}: basis=reviewed requires a `source` it was carried from, or "
                       f"a reviewed_by and reviewed_on")

    # Section 4 of the generated report may not name a body this file has not decided:
    # that is what makes the crosswalk the source of record for those reasons rather than
    # a second place they are written down.
    undecided = sorted({b for b in section_4_bodies
                        if b not in mapping and b not in unmapped})
    if undecided:
        bad.append(f"{len(undecided)} body/bodies in section 4 of "
                   f"_meta/unresolved-agencies.md have no crosswalk entry: {undecided[:5]}")

    bad += check_stamps(mapping, stamped)
    return bad


def by_das_number(mapping: dict) -> tuple[dict[str, dict], list[str]]:
    """{das_agency_number: entry}, plus the numbers two entries disagree about.

    The feed respells an agency without renumbering it — 845 appears as both "LIQUOR
    CONTROL CMSN" and "LIQUOR & CANNABIS COM, OR" — so several keys legitimately share a
    number. What is NOT legitimate is two of them resolving to different slugs: the number
    is the join key documents are stamped through, so it has to answer once.
    """
    out: dict[str, dict] = {}
    conflicts: list[str] = []
    for k, v in sorted(mapping.items()):
        n = str(v.get("das_agency_number") or "")
        if not n:
            continue
        prev = out.setdefault(n, v)
        if (prev.get("slug"), prev.get("basis")) != (v.get("slug"), v.get("basis")):
            conflicts.append(f"das_agency_number {n} resolves two ways: "
                             f"{prev.get('slug')}/{prev.get('basis')} and "
                             f"{v.get('slug')}/{v.get('basis')} ({k!r})")
    return out, conflicts


def check_stamps(mapping: dict, stamped: list[dict]) -> list[str]:
    """The gate between the crosswalk and the documents that repeat it.

    Both assert a registry slug. Nothing made them agree before this: a join document
    could carry a slug the crosswalk resolves differently, or none at all, and every gate
    in the repo stayed green. Each entry of `stamped` is one document's
    {id, agency_code, agency_registry_slug, agency_registry_basis}.

    GROUPED, one line per KIND of disagreement, naming up to five documents and the total.
    474 identical lines is not a more precise report than one line saying 474 — it is the
    same report with the count buried, and it is how a reader stops reading CI output.
    """
    index, bad = by_das_number(mapping)
    unknown, wrong_slug, no_basis, wrong_basis = [], [], [], []
    for doc in stamped:
        code = str(doc.get("agency_code") or "")
        entry = index.get(code)
        if entry is None:
            unknown.append(f"{doc.get('id')} (das number {code!r})")
            continue
        if doc.get("agency_registry_slug") != entry.get("slug"):
            wrong_slug.append(f"{doc.get('id')}: {doc.get('agency_registry_slug')!r} vs "
                              f"crosswalk {entry.get('slug')!r} for das number {code}")
        if not doc.get("agency_registry_basis"):
            no_basis.append(str(doc.get("id")))
        elif doc["agency_registry_basis"] != entry.get("basis"):
            wrong_basis.append(f"{doc.get('id')}: {doc['agency_registry_basis']!r} vs "
                               f"crosswalk {entry.get('basis')!r}")

    def line(items: list[str], msg: str) -> None:
        if items:
            bad.append(f"{len(items)} document(s) {msg}: {items[:5]}"
                       + (" ..." if len(items) > 5 else ""))

    line(unknown, "carry agency_registry_slug for an agency the crosswalk does not map")
    line(wrong_slug, "carry an agency_registry_slug the crosswalk disagrees with")
    line(no_basis, "carry agency_registry_slug but no agency_registry_basis — run "
                   "`python3 src/link_agency_registry.py --stamp`")
    line(wrong_basis, "carry an agency_registry_basis the crosswalk disagrees with — run "
                      "`python3 src/link_agency_registry.py --stamp`")
    return bad


# --- BEGIN VERBATIM SHARED BLOCK (norm_variants / names_agree) -------------------------
# Kept BYTE-IDENTICAL with the copies in oregon-kpm/src/link_agency_registry.py and
# oregon-audits/src/link_agency_registry.py, following the convention those files state:
# "copy it verbatim ... both sides then compute the same answers by construction instead
# of by agreement". All three corpora define `basis: exact` with the same permitted moves,
# so they must normalise identically or the same pair of names is exact in one repo and
# not the other.
def norm_variants(name: str) -> set[str]:
    """Every reading the crosswalk note permits `basis: exact` to use.

    The note lists the allowed moves as "case, punctuation, comma-inversion, a leading
    Oregon" -- a SET of moves, not a pipeline that must apply all of them. A comma does two
    different jobs in these strings: catalog inversion ("Administrative Services, Department
    of") and a parent/child qualifier ("Secretary of State, Audits Division"). Inverting the
    second is wrong and dropping the comma in the first is not enough, so both readings are
    produced and a match on either is a match.

    Written this way because forcing a single reading is a MEASURED bug, not a hypothetical:
    always-invert reported 'Secretary of State Audits Division' as failing to match an
    oar_name that is the same name with a comma in it.
    """
    n = name.strip().replace("’", "'")
    readings = {n.replace(",", " ")}
    if "," in n:
        head, tail = n.rsplit(",", 1)
        readings.add(f"{tail.strip()} {head.strip()}")
    out = set()
    for r in readings:
        r = " ".join(r.lower().replace(".", "").split())
        for pre in ("oregon ", "state of oregon "):
            if r.startswith(pre):
                r = r[len(pre):]
        out.add(r)
    return out


def names_agree(a: str, b: str) -> bool:
    """True when two names are the same name under any reading the note permits."""
    return bool(norm_variants(a) & norm_variants(b))
# --- END VERBATIM SHARED BLOCK ---------------------------------------------------------


def find_registry(explicit: str | None) -> Path | None:
    if explicit:
        p = Path(explicit)
        return p if p.is_file() else None
    return next((p for p in REGISTRY_CANDIDATES if p.is_file()), None)


def registry_index(path: Path) -> dict[str, dict]:
    """{slug: {oar_name, das_agency_number}} from ERF's committed registry.

    `das_agency_number` is read with `budget_agency_code` as a fallback: ERF's ADR 0003
    renamed the field and keeps the old key readable for one deprecation cycle, holding the
    same value. Reading only the new name would make this check silently pass nothing on a
    registry that has not migrated yet.
    """
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    out = {}
    for o in data.get("organizations") or []:
        if not o.get("slug"):
            continue
        code = o.get("das_agency_number") or o.get("budget_agency_code")
        out[o["slug"]] = {"oar_name": o.get("oar_name"),
                          "das_agency_number": str(code) if code else None}
    return out


def verify_registry(cw: dict, index: dict[str, dict]) -> list[str]:
    """Every claim this file makes ABOUT the registry, re-tested against the registry.

    Three claims, three checks. The slug must exist. A `das_number` basis must name the
    number ERF actually records, because that number IS the warrant. An `exact` basis must
    still match the registry's `oar_name` — the side of ADR 0003's name split that
    OAR-derived joins match — so an upstream chapter retitle surfaces as a failure instead
    of as a sentence that quietly stopped being true.
    """
    bad = []
    for k, v in sorted((cw.get("mapping") or {}).items()):
        if not isinstance(v, dict):
            continue
        slug = v.get("slug")
        entry = index.get(slug or "")
        if entry is None:
            bad.append(f"{k!r}: slug {slug!r} is not in the ERF registry")
            continue
        want = v.get("das_agency_number")
        if want and str(want) != (entry.get("das_agency_number") or ""):
            bad.append(f"{k!r}: das_agency_number {str(want)!r} but the registry records "
                       f"{entry.get('das_agency_number')!r} for {slug!r}")
        if v.get("basis") == "exact" and not names_agree(k, entry.get("oar_name") or ""):
            bad.append(f"{k!r}: claims basis: exact but the registry's oar_name for "
                       f"{slug!r} is {entry.get('oar_name')!r}")
    return bad


STAMP_RE = re.compile(r"^agency_registry_basis: .*\n", re.M)


def stamped_docs(roots=(JOINS, EXPENDITURES, BILLS)) -> list[dict]:
    """Every committed document carrying `agency_registry_slug`, as the four fields the
    stamp gate compares. Read across all content roots, not just joins/, so that stamping
    a new root later cannot slip past the gate by being somewhere nobody looked."""
    out = []
    for root in roots:
        for p in sorted(root.glob("*.md")):
            fm = frontmatter(p)
            if fm.get("agency_registry_slug"):
                out.append({"id": fm.get("id") or p.stem,
                            "path": p,
                            "agency_code": str(fm.get("agency_code") or ""),
                            "agency_registry_slug": fm.get("agency_registry_slug"),
                            "agency_registry_basis": fm.get("agency_registry_basis")})
    return out


def stamp(mapping: dict, docs: list[dict] | None = None) -> tuple[int, int]:
    """Write `agency_registry_basis` into each slugged document. (examined, changed).

    Inserts or corrects exactly that one line and touches nothing else, so a document
    built before the crosswalk existed is not re-ingested — which would re-stamp
    `retrieved` dates nothing else changed. Idempotent; a second run is a no-op.
    """
    index, _ = by_das_number(mapping)
    examined = changed = 0
    for doc in stamped_docs() if docs is None else docs:
        entry = index.get(doc["agency_code"])
        if not entry:
            continue
        examined += 1
        p = doc["path"]
        text = p.read_text(encoding="utf-8")
        head, body = text.split("---\n", 2)[1], text.split("---\n", 2)[2]
        want = f"agency_registry_basis: {entry['basis']}\n"
        head = STAMP_RE.sub("", head)
        # Immediately after the slug it qualifies, so the warrant sits beside the claim.
        anchor = re.compile(r"^(agency_registry_slug: .*\n)", re.M)
        if not anchor.search(head):
            print(f"SKIP {p.name}: no agency_registry_slug line to anchor on",
                  file=sys.stderr)
            continue
        new = f"---\n{anchor.sub(lambda m: m.group(1) + want, head, count=1)}---\n{body}"
        if new != text:
            p.write_text(new, encoding="utf-8")
            changed += 1
    return examined, changed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verify-registry", action="store_true")
    ap.add_argument("--stamp", action="store_true")
    ap.add_argument("--registry", help="path to ERF's _meta/catalog/agencies.yml")
    args = ap.parse_args()

    cw = load_crosswalk()
    mapping, unmapped = cw.get("mapping") or {}, cw.get("unmapped") or {}

    if args.check:
        names, bills, docs = corpus_names(), bill_names(), stamped_docs()
        report = ROOT / "_meta" / "unresolved-agencies.md"
        bodies = report_bodies(report.read_text(encoding="utf-8")) if report.is_file() else []
        problems = check(cw, names, bills, docs, bodies)
        for p in problems:
            print(f"FAIL  {p}", file=sys.stderr)
        reviewed = sum(1 for v in unmapped.values()
                       if isinstance(v, dict) and v.get("basis") == "reviewed")
        print(f"{len(names)} expenditure agency_name string(s); {len(mapping)} mapped, "
              f"{len(unmapped)} recorded as unmapped "
              f"({reviewed} with a reviewed reason, {len(unmapped) - reviewed} recorded "
              f"as NOT YET REVIEWED), {len(docs)} stamped document(s) checked.")
        return 1 if problems else 0

    if args.verify_registry:
        reg = find_registry(args.registry)
        if reg is None:
            # NOT a pass. A missing sibling means the check did not run, and exiting 0
            # would report "verified" for something nobody verified.
            print("SKIPPED: no ERF agency registry found. Checked:\n  " +
                  "\n  ".join(str(p) for p in REGISTRY_CANDIDATES) +
                  "\nClone executive-regulatory-frameworks beside this repo or pass "
                  "--registry. This is NOT a pass.", file=sys.stderr)
            return 2
        index = registry_index(reg)
        problems = verify_registry(cw, index)
        for p in problems:
            print(f"FAIL  {p}", file=sys.stderr)
        print(f"{len(mapping)} mapped slug(s) and DAS number(s) checked against "
              f"{len(index)} organizations in {reg}.")
        return 1 if problems else 0

    if args.stamp:
        examined, changed = stamp(mapping)
        print(f"{examined} slugged document(s) with a mapped agency; {changed} (re)stamped.")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Extract appropriation line items from oregon-legislature's mirrored bill text.

  python3 src/extract_appropriations.py --sibling ../oregon-legislature --session 2025R1
  python3 src/extract_appropriations.py --check    # re-verify every quoted line

THIS IS WHERE FABRICATION BECOMES POSSIBLE. Everything before this stage copied numbers
that already existed as numbers: a Socrata column of dollars became a Parquet column of
dollars, and a mismatch was catchable by reconciling against count(*) and sum(). Here a
number is being READ OUT OF PROSE, and a misparse produces a false fiscal claim with a
real bill citation attached to it — the most credible-looking wrong answer this platform
could emit.

So nothing this script produces is a finding. It produces CANDIDATES, every one marked
`human_reviewed: false`, each carrying the verbatim source line it came from so a reviewer
checks a quotation rather than trusting a regex.

THE MEASUREMENTS THAT SHAPED THE PARSER (207 bills, 2025R1, measured not assumed):

    96%  contain hyphenated line-wraps      <- the dominant hazard
    88%  say "biennium beginning"
    67%  say "the amount of $X"
    56%  say "out of the General Fund"
    34%  say "appropriated to the <Body>"   <- only a third; not a reliable anchor alone
    26%  carry numbered sub-items "(N) ... $X"

The 96% is why the text is reflowed before matching. PDF extraction breaks recipient names
mid-word — "distribution to the Carlson Col-\nlege of Veterinary Medicine" — and a
line-based regex records the recipient as "Carlson Col-". That is not a near-miss; it is a
different entity, and it would be indistinguishable from a real one in the output.

THE DOUBLE-COUNT, which is the same trap as budgeted-revenue's Totals row wearing new
clothes: a bill states an appropriation and then itemizes it.

    the amount of $22,500,000, which shall be allocated to Oregon State University
      (1) For the agricultural experiment station and branch stations, $12,000,000;
      (2) For the Oregon State University Extension Service, $8,800,000; and
      (3) For the Forest Research Laboratory, $1,700,000.

Summing every dollar figure gives $45,000,000 — exactly twice the appropriation. The
sub-items sum to the stated total exactly, and that reconciliation is BOTH the guard
against double-counting AND the evidence that the itemization was parsed completely. When
it fails, the bill is flagged rather than published with a plausible number.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "bills"
SIBLING_ID = "oregon-legislature"
MAINTAINER = "@dzinck"
DISCLAIMER = "NON-AUTHORITATIVE"

MARGIN_NUMBER = re.compile(r"\s*\d{1,2}\s*")
AMOUNT = re.compile(r"\$\s?(\d[\d,]*(?:\.\d{2})?)")
# The recipient of an appropriation.
#
# The article is OPTIONAL: bills write both "appropriated to the Department of Energy" and
# "appropriated to Oregon Health Authority".
#
# TERMINATORS, each one earned by a bill that the previous version got wrong:
#   ,                       the usual case
#   for                    stops the purpose clause: "appropriated to the Department of
#                           Education for the Educator Advancement Council" names the
#                           DEPARTMENT; the rest is what the money is for.
#                           EXCEPT for the three agency names that genuinely contain
#                           "for" — a bare terminator truncated "Commission for the Blind"
#                           to "Commission" in five separate biennia. The exception list is
#                           closed and derived from the registry (3 of 187 names), not
#                           guessed; widening `for` generally over-captured 3 bills.
#   out of                  "appropriated to X out of the General Fund"
#   to <lowercase>          "...Department to carry out section 2" over-ran into the verb.
#                           Requiring lowercase after `to` keeps "to the Commission" safe,
#                           since a name continues with a capital.
APPROPRIATED_TO = re.compile(
    r"appropriat(?:ed|ion)\s+to\s+(?:the\s+)?"
    r"([A-Z][A-Za-z’'&/.\- ]{3,70}?)"
    r"(?=,"
    r"|\s+for\s(?!the\s+Blind\b|Engineering\s+and\s+Land|Speech-Language)"
    r"|\s+out\s+of"
    r"|\s+to\s+[a-z])", re.I)

# A bill can leave the RECIPIENT blank too, not just the amount: the HB 5000-series budget
# templates read "is appropriated to ______, for the biennium beginning July 1, 2017, out
# of the General Fund, the amount of $___". 62 of the 68 documents with no captured agency
# are this, NOT a regex failure — the bill genuinely names nobody yet. Detected so the
# document can say so instead of looking like an extraction bug.
BLANK_RECIPIENT = re.compile(r"appropriat(?:ed|ion)\s+to\s+_{2,}", re.I)

# A bill that only MODIFIES appropriations made by prior session laws contains no
# "appropriated to <Body>" sentence in ANY form — the recipient lives in the amended
# chapter, not in this bill. Two shapes, both measured: amount amendments ("the amount
# ... is increased by $X" / "is decreased by $Y", 2017R1 SB 5508: 29 increases, 11
# decreases) and whole-section amendments ("Section 3, chapter 598, Oregon Laws 2023, is
# amended to read", 2024R1 HB 5203, an allocation schedule). An accurate null, previously
# reported as a parser failure; counted so the document (and build_joins' report) can say
# which it is.
MODIFIES_PRIOR = re.compile(r"is\s+(?:increased|decreased)\s+by", re.I)
AMENDS_PRIOR = re.compile(r"chapter\s+\d+,\s+Oregon\s+Laws\s+\d{4},\s+is\s+amended", re.I)

# The MULTI-RECIPIENT construction (2023R1 HB 2983): "there is appropriated: (1) To the
# Housing and Community Services Department: (a) $35,000,000 for deposit ...". A colon,
# an item number and a capital "To" stand between "appropriated" and every recipient, and
# there are SEVERAL recipients — a shape the single appropriated_to field cannot represent
# without attributing the whole bill to one of them. Recipients are captured as a list and
# reported; per-recipient joins are deliberately NOT built until the join model can carry
# them (a wrong single join is worse than an honest none). The terminator is a colon OR a
# comma: HB 2983's own two recipients split one each way ("To the Housing and Community
# Services Department:" / "To the Department of Land Conservation and Development, the
# amount of").
RECIPIENT_ITEM = re.compile(r"\(\d+\)\s+To\s+(?:the\s+)?([A-Z][A-Za-z’'&/.\- ]{3,70}?)[:,]")
AMOUNT_OF = re.compile(r"the\s+amount\s+of\s+\$\s?(\d[\d,]*(?:\.\d{2})?)")
SUBITEM = re.compile(r"\((\d+)\)\s*([^$]{0,160}?)\$\s?(\d[\d,]*(?:\.\d{2})?)")
FUND = re.compile(r"out\s+of\s+the\s+([A-Z][A-Za-z ]{2,40}?\s+Fund)", re.I)
BIENNIUM = re.compile(r"biennium\s+(beginning|ending)\s+\w+\s+\d{1,2},\s*(\d{4})", re.I)

# An APPROPRIATION WITH NO FIGURE YET. 2019R1 HB2020 reads, verbatim, "out of the General
# Fund, the amount of $ , which may be expended for compensation" — an introduced bill with
# the sum left blank. Every amount pattern above now requires a leading DIGIT, because
# `[\d,]+` matched the bare comma in "$ ," and money() then crashed on float(""). Declining
# to match it is necessary but not sufficient: a blank amount is an appropriation whose sum
# is UNSPECIFIED, which is a fact about the bill, and silently dropping it would let the
# document imply the bill appropriates nothing. Counted and reported instead.
BLANK_AMOUNT = re.compile(r"the\s+amount\s+of\s+\$\s*(?![\d])")


def biennium_fiscal_years(word: str, year: str | int) -> list[int]:
    """The two Oregon fiscal years a biennium covers.

    THE ASSUMPTION, STATED because the plan named it the single most likely source of a
    plausible wrong number: Oregon's fiscal year runs July 1 to June 30 and is NAMED for
    the calendar year it ends in, so FY2025 = 1 Jul 2024 - 30 Jun 2025. Therefore

        "biennium beginning July 1, 2025"  -> FY2026, FY2027
        "biennium ending  June 30, 2025"   -> FY2024, FY2025

    This is a convention, not something the expenditure dataset states about itself. It is
    recorded on every join that relies on it rather than applied silently, so a reader can
    reject the mapping without having to reverse-engineer it from the numbers.
    """
    year = int(year)   # re.groups() are strings; this silently type-errored on the first run
    if word.lower() == "beginning":
        return [year + 1, year + 2]
    return [year - 1, year]


def money(s: str) -> int | float:
    v = float(s.replace(",", ""))
    return int(v) if v == int(v) else v


def strip_margin(text: str) -> list[str]:
    """Drop the bill's left-margin line numbers, which extract as their own lines."""
    return [l for l in text.splitlines() if not MARGIN_NUMBER.fullmatch(l)]


# PAGE FURNITURE the PDF extraction injects at every page break: the drafting-office
# footer, the LC number, and the bill-number page header. It can land MID-WORD — 2025R1
# HB 3162 reads "there is appropri- NOTE: Matter in boldfaced type ... LC 3687 HB 3162
# ated to the Department of Education" — which defeats reflow()'s de-hyphenation and
# recorded the recipient as null in two bills (the other: 2023R1 HB 3274).
PAGE_FURNITURE = re.compile(
    r"NOTE:\s+Matter\s+in\s+boldfaced.*"
    r"|New\s+sections\s+are\s+in\s+boldfaced.*"
    r"|LC\s+\d{1,5}"
    r"|(?:HB|SB|HJR|SJR|HCR|SCR|HJM|SJM|HR|SR)\s+\d{1,4}[A-Z]?")


def strip_page_furniture(lines: list[str]) -> list[str]:
    """Drop page-break furniture from the PARSING text only.

    Applied to reflow()'s input and never to the raw evidence lines: a verbatim source
    line must stay quotable against the snapshot's own bytes, page furniture included,
    or --check would go hunting for a cleaned-up string the snapshot does not contain.
    """
    return [l for l in lines if not PAGE_FURNITURE.fullmatch(l.strip())]


def reflow(lines: list[str]) -> str:
    """Rejoin PDF-wrapped prose so a recipient name survives a line break.

    De-hyphenation is applied ONLY at a lowercase-to-lowercase break, which is where PDF
    wrapping puts it. A hyphen followed by an uppercase letter or a digit is left alone —
    those are real compounds and identifiers, not wrap artifacts.
    """
    raw = "\n".join(lines)
    raw = re.sub(r"(?<=[a-z])-\n(?=[a-z])", "", raw)
    raw = re.sub(r"\n(?!SECTION|\(\d)", " ", raw)
    return re.sub(r"[ \t]{2,}", " ", raw)


def verbatim_for(amount_text: str, lines: list[str], item_no: int | None = None
                 ) -> tuple[str, bool]:
    """The unreflowed source line(s) containing this amount, and whether it was ambiguous.

    Returned untouched. A reviewer must be able to compare the extracted figure against
    the bill's own words, not against this script's cleaned-up version of them — the whole
    point is to make a misparse visible.
    """
    needle = amount_text.replace(" ", "")
    hits = [i for i, l in enumerate(lines) if needle in l.replace(" ", "")]
    if not hits:
        return "", True
    # Two items in one bill can carry the SAME amount — HB2018 grants $3,000,000 to both
    # Beaverton and another city. Taking the first occurrence then quotes the wrong item's
    # line: right figure, wrong evidence, which is worse than no evidence because it reads
    # as confirmation. Prefer the line that opens with this item's own number.
    i = hits[0]
    if item_no is not None and len(hits) > 1:
        numbered = [h for h in hits if lines[h].lstrip().startswith(f"({item_no})")]
        if numbered:
            return _with_continuation(numbered[0], lines), False
    return _with_continuation(i, lines), len(hits) > 1


def _with_continuation(i: int, lines: list[str]) -> str:
    """A wrapped sentence needs its continuation to be legible as evidence."""
    quote = lines[i].strip()
    if i + 1 < len(lines) and (quote.endswith("-") or not quote.endswith((".", ";", ":"))):
        quote += "\n" + lines[i + 1].strip()
    return quote


SECTION_SPLIT = re.compile(r"(?=SECTION\s+\d+\.)")

# A bill only has an ITEMIZATION where it says it does. This is the lead-in that announces
# one, and sub-items are read only from AFTER it, inside the same section.
# The window to the colon is 200 chars, measured not guessed: HB2018 reads "the following
# amounts for distribution to the following entities for the following infrastructure
# projects to support the development of housing:" — 115 characters, and an 80-char window
# silently dropped a genuine 20-item list. `[^.]` still terminates at the first sentence
# end, so this stays tight despite the length.
ITEMIZATION_LEADIN = re.compile(
    r"(following amounts|as follows|following programs|following manner|allocated as)"
    r"[^.]{0,200}:", re.I)

# Phrasing that marks a "(N)" as a STATUTORY SUBSECTION rather than a line item. A
# subsection is an independent provision — another appropriation, a spending cap, an
# expenditure limitation — and adding it to a sibling subsection is meaningless.
SUBSECTION_PROSE = re.compile(
    r"there is appropriated|the amount of|of the moneys|notwithstanding|shall expend|"
    r"may withhold|is established|not to exceed", re.I)


def split_sections(flowed: str) -> list[str]:
    """One bill is not one appropriation.

    Agency budget bills (the HB 5000 / SB 5500 series) carry several independent SECTIONs,
    each appropriating separately and each itemizing with its OWN numbering restarting at
    (1). Parsing the bill as a single list flattens them: two different "(1) Fish Division"
    rows collide, and sub-items from one section get reconciled against another section's
    total. That produced 34 MISMATCHes on the first full run — the reconciliation guard
    correctly refusing to publish a bill this parser had misread.

    Sections are the unit of appropriation, so they are the unit of reconciliation.
    """
    parts = [p for p in SECTION_SPLIT.split(flowed) if p.strip()]
    return parts or [flowed]


def parse_bill(flowed: str, raw_lines: list[str]) -> dict:
    """Candidate appropriations from one bill. Structure only — no judgement."""
    body = APPROPRIATED_TO.search(flowed)
    fund = FUND.search(flowed)
    bien = BIENNIUM.search(flowed)
    fys = biennium_fiscal_years(*bien.groups()) if bien else None

    sections = []
    for n, chunk in enumerate(split_sections(flowed), 1):
        totals = []
        for m in AMOUNT_OF.finditer(chunk):
            quote, ambiguous = verbatim_for(m.group(0)[m.group(0).index("$"):], raw_lines)
            totals.append({"amount": money(m.group(1)), "source_line": quote,
                           "ambiguous_source": ambiguous})
        # ONLY read sub-items after an explicit itemization lead-in. Without this, "(1)"
        # and "(2)" statutory subsections were parsed as addends: HB3837's (1) IS the
        # appropriation and its (2) caps administration at $200,000 out of that same money;
        # HB5016 section 7's (1) and (2) are two separate appropriations, to the 83rd and
        # 84th Legislative Assemblies. Summing either pair is meaningless, and it produced
        # every remaining MISMATCH.
        lead = ITEMIZATION_LEADIN.search(chunk)
        items = []
        subsections = []
        for m in SUBITEM.finditer(chunk):
            quote, ambiguous = verbatim_for("$" + m.group(3), raw_lines, int(m.group(1)))
            # Dotted leaders are typographic filler in budget tables, not the purpose.
            purpose = re.sub(r"[.\s]{3,}", " ", m.group(2))
            purpose = re.sub(r"\s+", " ", purpose).strip(" ,;").removeprefix("For ").strip()
            if not purpose:
                # Amount-first phrasing: the recipient follows the figure, so read to the
                # end of the sentence instead. Without this the purpose column was blank
                # for every item in HB2018's 44-entry infrastructure list.
                tail = chunk[m.end():m.end() + 200].split("\n")[0]
                tail = re.split(r"(?<=[a-z0-9])\.\s", tail)[0]
                purpose = re.sub(r"\s+", " ", tail).strip(" .,;")
            entry = {"item": int(m.group(1)), "purpose": purpose,
                     "amount": money(m.group(3)), "source_line": quote,
                     "ambiguous_source": ambiguous}
            is_item = bool(lead) and m.start() >= lead.end() \
                and not SUBSECTION_PROSE.search(m.group(2))
            (items if is_item else subsections).append(entry)
        if totals or items or subsections:
            label = re.match(r"SECTION\s+(\d+)\.", chunk)
            sections.append({"section": label.group(1) if label else str(n),
                             "stated_totals": totals, "line_items": items,
                             "subsections": subsections})

    return {
        "appropriated_to": body.group(1).strip() if body else None,
        "fund": fund.group(1) if fund else None,
        "biennium": (f"{bien.group(1).lower()} {bien.group(2)}" if bien else None),
        "biennium_fiscal_years": fys,
        "sections": sections,
        "stated_totals": [t for s in sections for t in s["stated_totals"]],
        "line_items": [i for s in sections for i in s["line_items"]],
        "subsections": [x for s in sections for x in s["subsections"]],
        "distinct_amounts_in_text": len(AMOUNT.findall(flowed)),
        "blank_amounts": len(BLANK_AMOUNT.findall(flowed)),
        "blank_recipient": bool(BLANK_RECIPIENT.search(flowed)),
        "modifies_prior_appropriations": len(MODIFIES_PRIOR.findall(flowed)),
        "amends_prior_law": len(AMENDS_PRIOR.findall(flowed)),
        # Deduplicated in order of first appearance; a 6-item list naming one department
        # twice is two items to one recipient, not two recipients.
        "recipients_in_itemization": list(dict.fromkeys(
            m.strip() for m in RECIPIENT_ITEM.findall(flowed))),
    }


def reconcile(parsed: dict) -> dict:
    """Do the sub-items sum to the stated appropriation?

    Not a formality. It is simultaneously the double-count guard and the completeness
    proof: sub-items that sum to the total mean the itemization was parsed in full, and
    any other outcome means this bill must not be published as a set of figures.
    """
    per_section = []
    for s in parsed["sections"]:
        totals = [t["amount"] for t in s["stated_totals"]]
        items = [i["amount"] for i in s["line_items"]]
        e = {"section": s["section"]}
        if items and totals:
            e["items_sum"] = sum(items)
            e["reconciles"] = sum(items) in totals
            e["status"] = "reconciled" if e["reconciles"] else "MISMATCH"
        elif items:
            e["items_sum"] = sum(items)
            e["status"] = "items-without-stated-total"
        elif s["subsections"]:
            # Independent provisions, deliberately NOT summed. See SUBSECTION_PROSE.
            e["status"] = "subsections-not-itemized"
        else:
            e["status"] = ("single-appropriation" if len(totals) == 1
                           else "multiple-totals-no-itemization")
        per_section.append(e)

    r = {"sections": per_section}
    statuses = {e["status"] for e in per_section}
    if not per_section:
        # Distinguish "the bill states no amounts" from "the bill states amounts that are
        # BLANK". The second is an appropriation of an unspecified sum, and calling it
        # no-amounts would report unspecified as nothing.
        r["status"] = "amounts-left-blank" if parsed.get("blank_amounts") else "no-amounts"
    elif "MISMATCH" in statuses:
        bad = [e for e in per_section if e["status"] == "MISMATCH"]
        r["status"] = "MISMATCH"
        r["note"] = (f"{len(bad)} of {len(per_section)} section(s) do not reconcile: their "
                     f"sub-items sum to a figure matching no stated total in the same "
                     f"section. The itemization is incomplete or mis-parsed — NOT publishable.")
    elif statuses == {"reconciled"}:
        r["status"] = "reconciled"
    elif "reconciled" in statuses:
        r["status"] = "partly-reconciled"
    else:
        r["status"] = sorted(statuses)[0]
    return r


def _tables(L: list, sec: dict, e: dict) -> None:
    """The two tables for one section, kept SEPARATE on purpose.

    The stated appropriation and its line items are the same money described twice. Any
    layout that invites adding them together reintroduces the double-count this whole
    reconciliation exists to catch, so they never share a table.
    """
    if sec["stated_totals"]:
        L.append("**Stated appropriation**")
        L.append("")
        L.append("| Amount | Verbatim source line |")
        L.append("|---:|---|")
        for t in sec["stated_totals"]:
            q = t["source_line"].replace("\n", " ").replace("|", "\\|")
            flag = " ⚠ this amount appears more than once in the bill" if t["ambiguous_source"] else ""
            L.append(f"| ${t['amount']:,} | {q}{flag} |")
        L.append("")
    if sec["line_items"]:
        L.append("**Line items**")
        L.append("")
        L.append("| # | Purpose (parsed) | Amount | Verbatim source line |")
        L.append("|---|---|---:|---|")
        for it in sec["line_items"]:
            q = it["source_line"].replace("\n", " ").replace("|", "\\|")
            flag = " ⚠" if it["ambiguous_source"] else ""
            L.append(f"| {it['item']} | {it['purpose']} | ${it['amount']:,} | {q}{flag} |")
        L.append("")
        if e.get("items_sum") is not None:
            verdict = ("and that matches the stated appropriation above"
                       if e.get("reconciles") else
                       "which matches NO stated appropriation in this section")
            L.append(f"Line items sum to **${e['items_sum']:,}** — {verdict}.")
            L.append("")
    if sec.get("subsections"):
        L.append("**Other amounts in this section** — separate statutory provisions "
                 "(a further appropriation, a spending cap, an expenditure limitation). "
                 "They are **not** components of the appropriation above and must never "
                 "be summed with it or with each other.")
        L.append("")
        L.append("| Subsection | Text (parsed) | Amount | Verbatim source line |")
        L.append("|---|---|---:|---|")
        for it in sec["subsections"]:
            q = it["source_line"].replace("\n", " ").replace("|", "\\|")
            L.append(f"| ({it['item']}) | {it['purpose']} | ${it['amount']:,} | {q} |")
        L.append("")


def build_doc(measure: dict, parsed: dict, rec: dict, sibling_sha: str, today: str) -> str:
    mid = measure["id"]
    doc_id = f"appropriations-{mid.replace('measure-', '')}"
    fm = {
        "schema_version": 1, "corpus": "oregon-budget", "jurisdiction": "oregon",
        "id": doc_id,
        "title": f"Appropriations in {measure['citation']}",
        "doc_type": "dataset_doc",
        "citation": measure["citation"],
        "issuing_body": "Oregon State Legislature",
        "source_url": measure["source_url"],
        "source_format": "pdf",
        "snapshot_policy": "hash-only",
        "status": "current",
        "content_mode": "summary",
        "last_verified": "",  # rule 6: only corpus-verify writes this
        "verified_by": "",
        "maintainer": MAINTAINER,
        # FALSE UNTIL A HUMAN SAYS OTHERWISE. Every figure below was read out of prose by
        # a regex; none of it is servable as fact until someone has compared it to the
        # quoted source line. src/check_appropriations.py enforces this.
        "human_reviewed": False,
        "relationships": {"implements": [], "implemented_by": [],
                          "references_external": [measure["citation"]],
                          "related": [], "supersedes": []},
        "tags": ["oregon-budget", "appropriations", measure["session"].lower(),
                 "unreviewed"],
        "sibling_corpus": SIBLING_ID,
        "sibling_document_id": mid,
        "sibling_snapshot_id": measure["snapshot_id"],
        "sibling_source_sha256": sibling_sha,
        "extraction_status": rec["status"],
        "appropriated_to": parsed["appropriated_to"],
        "fund": parsed["fund"],
        "biennium": parsed["biennium"],
        "biennium_fiscal_years": parsed["biennium_fiscal_years"],
        "blank_amounts": parsed.get("blank_amounts", 0),
        "blank_recipient": parsed.get("blank_recipient", False),
        "modifies_prior_appropriations": parsed.get("modifies_prior_appropriations", 0),
        "amends_prior_law": parsed.get("amends_prior_law", 0),
        "recipients_in_itemization": parsed.get("recipients_in_itemization", []),
    }

    L = []
    L.append(f"> **{DISCLAIMER} — UNREVIEWED MACHINE EXTRACTION.** Every figure on this")
    L.append("> page was read out of bill prose by a parser and has **not** been checked by")
    L.append("> a person. It is not the text of any bill and must not be quoted as an")
    L.append(f"> appropriation. The authoritative text is `{measure['source_url']}`.")
    L.append("")
    L.append(f"# Appropriations in {measure['citation']}")
    L.append("")
    L.append("## At a glance")
    L.append("")
    L.append(f"{measure['title']}")
    L.append("")
    bits = []
    if parsed["appropriated_to"]:
        bits.append(f"appropriated to **{parsed['appropriated_to']}**")
    if parsed["fund"]:
        bits.append(f"out of the **{parsed['fund']}**")
    if parsed["biennium"]:
        fy = parsed["biennium_fiscal_years"]
        bits.append(f"for the biennium **{parsed['biennium']}** (fiscal years "
                    f"{fy[0]}\u2013{fy[1]})")
    if bits:
        L.append("Parsed context: " + ", ".join(bits) + ".")
        L.append("")
    detail = {"MISMATCH": rec.get("note", ""),
              "reconciled": "Every itemized section sums to its own stated appropriation.",
              "partly-reconciled": "Some sections reconcile; others state an amount with "
                                   "no itemization to check it against.",
              }.get(rec["status"], "No itemization to reconcile against.")
    L.append(f"Extraction status: **{rec['status']}**. {detail}")
    if len(parsed["sections"]) > 1:
        L.append("")
        L.append(f"This bill appropriates in **{len(parsed['sections'])} separate "
                 f"sections**. Each is reconciled on its own: item numbering restarts per "
                 f"section, so amounts must never be pooled across them.")
    L.append("")
    L.append("The full text of this bill lives in the "
             f"`{SIBLING_ID}` corpus as `{mid}` and is referenced, not copied.")
    L.append("")

    by_section = {e["section"]: e for e in rec["sections"]}
    for sec in parsed["sections"]:
        e = by_section.get(sec["section"], {})
        if len(parsed["sections"]) > 1:
            L.append(f"## Section {sec['section']} — {e.get('status','')}")
            L.append("")
        _tables(L, sec, e)

    L.append("## Curator notes")
    L.append("")
    if parsed.get("blank_recipient"):
        L.append("**This bill leaves the RECIPIENT blank** — the text reads \"appropriated "
                 "to ______\". It is a budget-bill template whose agency has not been "
                 "filled in yet. No agency could be extracted because the bill names none; "
                 "this is not an extraction failure.")
        L.append("")
    mods = parsed.get("modifies_prior_appropriations", 0)
    amends = parsed.get("amends_prior_law", 0)
    if (mods or amends) and not parsed.get("appropriated_to"):
        what = " and ".join(filter(None, [
            f"{mods} increase/decrease clause(s)" if mods else "",
            f"{amends} section(s) amending a prior chapter" if amends else ""]))
        L.append(f"**This bill MODIFIES prior session laws** — {what}. The recipient of "
                 "each amount lives in the amended chapter, not in this bill's own text, "
                 "so `appropriated_to` is accurately null: no agency name could be "
                 "extracted because this bill's appropriation sentences name none.")
        L.append("")
    if parsed.get("recipients_in_itemization"):
        names = ", ".join(f"**{n}**" for n in parsed["recipients_in_itemization"])
        L.append(f"**This bill appropriates to MULTIPLE recipients in one itemization** — "
                 f"{names}. A single `appropriated_to` field cannot carry that without "
                 "attributing the whole bill to one of them, so it is left null and the "
                 "recipients are listed here. Per-recipient joins are future work; an "
                 "honest none beats a wrong one.")
        L.append("")
    if parsed.get("blank_amounts"):
        L.append(f"**This bill contains {parsed['blank_amounts']} appropriation(s) with the "
                 f"dollar figure LEFT BLANK** — the text reads \"the amount of $\" with no "
                 f"number. Those are appropriations whose sum is unspecified in this "
                 f"version of the bill, not appropriations of zero, and they are counted "
                 f"here rather than in the tables above because there is no figure to "
                 f"report.")
        L.append("")
    L.append("Summing every dollar figure in an appropriation bill **double-counts**: a "
             "bill states an appropriation and then itemizes the same money. The stated "
             "appropriation and the line items are separate tables above for exactly that "
             "reason, and must never be added together.")
    L.append("")
    L.append("The 'purpose' column is a parser's reading of the surrounding prose, not the "
             "bill's own words. The verbatim source line beside it is the bill's own "
             "words, and is the column to trust.")
    L.append("")
    return f"---\n{yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100)}---\n\n" \
           + "\n".join(L)


def load_measures(sibling: Path, session: str) -> list[dict]:
    out = []
    for p in sorted((sibling / "measures" / session).glob("*.md")):
        if p.name.startswith("_"):
            continue
        fm = yaml.safe_load(p.read_text().split("---\n", 2)[1])
        catch = (fm.get("catch_line") or "") + " " + (fm.get("title") or "")
        if "appropriat" not in catch.lower():
            continue
        out.append({"id": fm["id"], "citation": fm["citation"], "title": fm.get("title", ""),
                    "source_url": fm.get("source_url", ""),
                    "snapshot_id": fm.get("snapshot_id"), "session": session,
                    "sha256": fm.get("source_sha256", "")})
    return out


QUOTE_CELL = re.compile(r"^\|.*?\|\s*\$[\d,]+\s*\|(.+)\|\s*$|^\|\s*\$[\d,]+\s*\|(.+)\|\s*$")


def check(sibling: Path) -> int:
    """Does every quoted line still appear, verbatim, in the sibling's snapshot?

    The bill text is REFERENCED, not copied, so this corpus holds no bytes it can check
    itself against — the quotations here are only as good as their link to the sibling.
    Without this, an extracted figure and its "verbatim source line" are just two strings
    in a file, and a snapshot re-fetched from a revised PDF upstream would leave the
    quotation silently describing text that no longer exists.

    A MISSING SIBLING IS A LOUD SKIP, NOT A PASS. Reporting "0 failures" when nothing was
    compared is the failure mode this platform keeps finding in its own CI.
    """
    docs = sorted(OUT.glob("*.md"))
    if not docs:
        print(f"no documents in {OUT.relative_to(ROOT)}/", file=sys.stderr)
        return 1
    if not (sibling / "_meta" / "snapshots").is_dir():
        print(f"SKIPPED: no sibling checkout at {sibling}. {len(docs)} document(s) were "
              f"NOT verified — this is not a pass. Pass --sibling <path to "
              f"oregon-legislature>.", file=sys.stderr)
        return 2

    checked = quotes = bad = drifted = 0
    for p in docs:
        raw = p.read_text()
        fm = yaml.safe_load(raw.split("---\n", 2)[1])
        snap = sibling / "_meta" / "snapshots" / f"{fm['sibling_snapshot_id']}.txt"
        if not snap.is_file():
            print(f"  FAIL {p.name}: sibling snapshot {fm['sibling_snapshot_id']}.txt is gone")
            bad += 1
            continue
        checked += 1
        if hashlib.sha256(snap.read_bytes()).hexdigest() != fm.get("sibling_source_sha256"):
            print(f"  DRIFT {p.name}: the sibling's snapshot has changed since extraction — "
                  f"re-run the extractor; the quotations below may describe text that no "
                  f"longer exists")
            drifted += 1
        # Compare on collapsed whitespace: the quote is verbatim, but markdown table cells
        # join wrapped lines with a space, and PDF text carries runs of spaces.
        hay = re.sub(r"\s+", " ", snap.read_text(errors="replace"))
        for line in raw.splitlines():
            m = QUOTE_CELL.match(line)
            if not m:
                continue
            cell = (m.group(1) or m.group(2) or "").strip()
            cell = cell.replace("\\|", "|").split(" ⚠")[0].strip()
            if not cell:
                continue
            quotes += 1
            if re.sub(r"\s+", " ", cell) not in hay:
                print(f"  FAIL {p.name}: quoted line not found in the snapshot:\n"
                      f"        {cell[:110]}")
                bad += 1

    print(f"\n{checked} document(s), {quotes} quoted line(s) verified against "
          f"{sibling.name}")
    if drifted:
        print(f"  {drifted} document(s) reference a snapshot that has since changed")
    print("every quotation traces to the sibling's committed bytes" if not bad
          else f"  {bad} problem(s)")
    return 1 if (bad or drifted) else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sibling", default="../oregon-legislature")
    ap.add_argument("--session", default="2025R1")
    ap.add_argument("--limit", type=int, default=0, help="stop after N bills (for a dry run)")
    ap.add_argument("--check", action="store_true",
                    help="re-verify every quoted line against the sibling; write nothing")
    args = ap.parse_args()

    if args.check:
        return check(Path(args.sibling).resolve())

    sibling = Path(args.sibling).resolve()
    if not (sibling / "measures").is_dir():
        print(f"no measures/ under {sibling} — this stage READS the sibling corpus rather "
              f"than copying its bill text. Pass --sibling <path to oregon-legislature>.",
              file=sys.stderr)
        return 2

    from datetime import datetime, timezone
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    measures = load_measures(sibling, args.session)
    if args.limit:
        measures = measures[:args.limit]
    OUT.mkdir(exist_ok=True)

    stats, written, skipped = {}, 0, []
    for meas in measures:
        snap = sibling / "_meta" / "snapshots" / f"{meas['snapshot_id']}.txt"
        if not snap.is_file():
            skipped.append((meas["id"], "no committed .txt in the sibling"))
            continue
        raw_lines = strip_margin(snap.read_text(errors="replace"))
        parsed = parse_bill(reflow(strip_page_furniture(raw_lines)), raw_lines)
        if not parsed["stated_totals"] and not parsed["line_items"]:
            # A bill whose ONLY amounts are blank still appropriates money — the sums are
            # simply not filled in yet. Skipping it as "no dollar amounts found" would make
            # the corpus silent about an appropriation bill that exists, and would report
            # UNSPECIFIED as NOTHING. 2019R1 HB2020 is the case: two blank amounts, zero
            # figures, and it vanished entirely from the first pass.
            if not parsed.get("blank_amounts"):
                skipped.append((meas["id"], "no dollar amounts found"))
                stats["no-amounts"] = stats.get("no-amounts", 0) + 1
                continue
        rec = reconcile(parsed)
        stats[rec["status"]] = stats.get(rec["status"], 0) + 1
        sha = hashlib.sha256(snap.read_bytes()).hexdigest()
        doc = build_doc(meas, parsed, rec, sha, today)
        doc_id = f"appropriations-{meas['id'].replace('measure-', '')}"
        (OUT / f"{doc_id}.md").write_text(doc)
        written += 1

    print(f"{written} appropriation document(s) -> {OUT.relative_to(ROOT)}/")
    for k, v in sorted(stats.items(), key=lambda kv: -kv[1]):
        print(f"  {k:<32} {v}")
    if skipped:
        print(f"  skipped: {len(skipped)}")
        for mid, why in skipped[:5]:
            print(f"    {mid}: {why}")
    print("\nEVERY document is human_reviewed: false. Nothing here is servable as fact "
          "until a person has checked the figures against the quoted source lines.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

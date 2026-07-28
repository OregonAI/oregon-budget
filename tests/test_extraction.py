"""Appropriation extraction: the cases real bills produced, pinned.

Every fixture here is text a real Oregon bill actually contains. Synthetic examples would
not have found any of these — each one was discovered by running the extractor over a new
session and watching it crash, drop a bill, or quote the wrong line.

Offline: no network, no sibling checkout, no model.
"""
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from extract_appropriations import (  # noqa: E402
    AMOUNT, AMOUNT_OF, APPROPRIATED_TO, BLANK_AMOUNT, BLANK_RECIPIENT, SUBITEM, biennium_fiscal_years, money,
    parse_bill, reconcile, reflow, strip_margin, verbatim_for,
)

# 2019R1 HB2020, verbatim. An INTRODUCED bill with the dollar figure left blank.
HB2020 = (
    "In addition to and not in lieu of any other appropriation, there is appropriated to "
    "the Department of Environmental Quality, for the biennium beginning July 1, 2019, out "
    "of the General Fund, the amount of $ , which may be expended for compensation and "
    "other expenses of the program."
)

# 2025R1 HB2408, verbatim. A stated total that its sub-items sum to exactly.
HB2408 = (
    "there is appropriated to the Higher Education Coordinating Commission, for the "
    "biennium beginning July 1, 2025, out of the General Fund, the amount of $22,500,000, "
    "which shall be allocated to Oregon State University and may be expended in the "
    "following amounts for the following programs at the university:\n"
    "(1) For the agricultural experiment station and branch stations, $12,000,000;\n"
    "(2) For the Oregon State University Extension Service, $8,800,000; and\n"
    "(3) For the Forest Research Laboratory, $1,700,000."
)


# ------------------------------------------------------ blank amounts (2019R1 HB2020)

def test_a_blank_amount_does_not_crash():
    """THE CRASH. Every amount pattern used `[\\d,]+`, which matches a BARE COMMA, so
    "the amount of $ ," matched and money() died on float(""). It killed the whole 2019R1
    run — one bill in 2,768 taking down every other bill's extraction with it."""
    parsed = parse_bill(HB2020, HB2020.splitlines())      # must not raise
    assert parsed["stated_totals"] == []


def test_a_blank_amount_is_never_read_as_a_figure():
    """The dangerous near-miss: matching the blank and recording SOME number for it."""
    assert AMOUNT_OF.findall(HB2020) == []
    assert AMOUNT.findall(HB2020) == []
    assert SUBITEM.findall(HB2020) == []


def test_a_blank_amount_is_counted_not_ignored():
    """Declining to match is only half the fix. A blank is an appropriation of an
    UNSPECIFIED sum — a fact about the bill — and dropping it silently would let the
    document imply the bill appropriates nothing."""
    assert len(BLANK_AMOUNT.findall(HB2020)) == 1
    assert parse_bill(HB2020, HB2020.splitlines())["blank_amounts"] == 1


def test_blank_only_bill_is_reported_not_skipped():
    """HB2020 has blanks and NO figures, so the first fix left it with zero sections and
    it was skipped as 'no dollar amounts found' — the corpus went silent about an
    appropriation bill that exists. UNSPECIFIED must not be reported as NOTHING."""
    rec = reconcile(parse_bill(HB2020, HB2020.splitlines()))
    assert rec["status"] == "amounts-left-blank"
    assert rec["status"] != "no-amounts"


@pytest.mark.parametrize("bad", ["$ ,", "$,", "the amount of $ , which"])
def test_comma_only_amounts_never_parse(bad):
    """The exact shape that crashed it. `money()` on the captured text must never be
    reached, because nothing should capture."""
    assert AMOUNT.findall(bad) == []


# ------------------------------------------------------------- real amounts still work

def test_real_amounts_are_unaffected_by_the_fix():
    parsed = parse_bill(HB2408, HB2408.splitlines())
    assert [t["amount"] for t in parsed["stated_totals"]] == [22_500_000]
    assert [i["amount"] for i in parsed["line_items"]] == [12_000_000, 8_800_000, 1_700_000]
    assert parsed["blank_amounts"] == 0


def test_subitems_must_sum_to_the_stated_total():
    """The double-count guard: summing every figure in HB2408 gives $45,000,000, exactly
    twice the appropriation. Reconciliation is what proves the itemization was read whole."""
    rec = reconcile(parse_bill(HB2408, HB2408.splitlines()))
    assert rec["status"] == "reconciled"
    assert rec["sections"][0]["items_sum"] == 22_500_000


def test_money_parses_grouped_and_decimal_amounts():
    assert money("22,500,000") == 22_500_000
    assert money("904,990,522.63") == 904990522.63


# ------------------------------------------------------------------- other real cases

def test_hyphenated_line_wrap_does_not_truncate_a_recipient():
    """96% of bills wrap mid-word. "Carlson Col-\\nlege" must not become "Carlson Col-",
    which is a different entity and indistinguishable from a real one downstream."""
    out = reflow(["distribution to the Carlson Col-", "lege of Veterinary Medicine"])
    assert "Carlson College of Veterinary Medicine" in out


def test_margin_line_numbers_are_stripped():
    assert strip_margin("1\n2\nthere is appropriated\n3") == ["there is appropriated"]


def test_same_amount_twice_quotes_the_right_item():
    """HB2018 grants $3,000,000 to four different cities. Taking the first line containing
    the figure quoted Beaverton's line for every one of them: right figure, WRONG evidence
    — worse than none, because a quotation reads as confirmation."""
    lines = ["(2) $3,000,000 to the City of Beaverton for a pump station.",
             "(5) $3,000,000 to the City of Cottage Grove for water infrastructure."]
    quote, ambiguous = verbatim_for("$3,000,000", lines, item_no=5)
    assert "Cottage Grove" in quote and "Beaverton" not in quote
    assert ambiguous is False


@pytest.mark.parametrize("word,year,expected", [
    ("beginning", "2025", [2026, 2027]),
    ("ending", "2025", [2024, 2025]),
    ("ending", 2025, [2024, 2025]),      # re.groups() are str; ints must work too
])
def test_biennium_maps_to_fiscal_years(word, year, expected):
    """The stated convention, not an inference: Oregon's fiscal year runs 1 Jul-30 Jun and
    is named for the year it ends. Getting this backwards silently shifts every join by two
    years — the single most likely source of a plausible wrong number."""
    assert biennium_fiscal_years(word, year) == expected


def test_statutory_subsections_are_not_treated_as_an_itemization():
    """HB3837's (1) IS the appropriation and its (2) caps administration out of that same
    money. Summed as addends they double-count the appropriation and add a carve-out.
    Without an explicit itemization lead-in, numbered subsections are not line items."""
    text = ("(1) There is appropriated to the Oregon Business Development Department, for "
            "the biennium ending June 30, 2025, out of the General Fund, the amount of "
            "$2,775,000.\n(2) Of the moneys appropriated under this section, the department "
            "may withhold an amount not to exceed $200,000 for administration.")
    parsed = parse_bill(text, text.splitlines())
    assert parsed["line_items"] == [], "a statutory subsection was read as a line item"
    assert reconcile(parsed)["status"] != "MISMATCH"


# ------------------------------------------------- recipient capture (APPROPRIATED_TO)

@pytest.mark.parametrize("text,expected", [
    # "for" inside the agency's own NAME. A bare `\s+for\s` terminator truncated this to
    # "Commission" in five separate biennia, and "Commission" resolves to nothing.
    ("There is appropriated to the Commission for the Blind, for the biennium beginning "
     "July 1, 2017, out of the General Fund", "Commission for the Blind"),
    # "for" starting a PURPOSE clause — the department is the recipient, the rest is what
    # the money is for. Widening `for` generally broke this.
    ("appropriated to the Department of Education for the Educator Advancement Council, "
     "for the biennium", "Department of Education"),
    # over-capture into the verb: "...Department to carry out section 2 of this 2024 Act"
    ("continuously appropriated to the Oregon Business Development Department to carry out "
     "section 2", "Oregon Business Development Department"),
    # the article is optional
    ("is appropriated to Oregon Health Authority, for the biennium", "Oregon Health Authority"),
    ("appropriated to the Department of Geology and Mineral Industries, for the biennium",
     "Department of Geology and Mineral Industries"),
])
def test_recipient_capture(text, expected):
    m = APPROPRIATED_TO.search(text)
    assert m and m.group(1) == expected


def test_a_blank_recipient_is_detected_not_mistaken_for_a_parser_failure():
    """The HB 5000-series budget templates read "appropriated to ______" — the bill names
    nobody yet. 62 of the 68 documents with no captured agency are this. Reporting them as
    extraction failures sent me chasing a regex bug that did not exist."""
    t = ("is appropriated to ______, for the biennium beginning July 1, 2017, out of the "
         "General Fund, the amount of $ ")
    assert APPROPRIATED_TO.search(t) is None
    assert BLANK_RECIPIENT.search(t) is not None
    parsed = parse_bill(t, t.splitlines())
    assert parsed["blank_recipient"] is True

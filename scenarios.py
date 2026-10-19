"""
The runs your test needs. ← UNIT 4, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
the empty-search branch needs an impossible query. One about the fit card needs
the same item run more than once. Working that out is Milestone 3's first step,
and this file is where you write it down.

`run_eval.py` runs everything here five times and writes the run log — five
because your criteria are written out of five.

Three scenarios are filled in to show the shape. Add or change whatever your
own criteria need — these are a starting point, not a fixed set.
"""

SCENARIOS = [
    # ── Criterion 1: a matching query completes all three tools ──────────────
    {
        # Price ceiling only. Selects lst_006 (Graphic Tee, $24).
        "name": "matching query completes",
        "query": "vintage graphic tee under $30",
        "wardrobe": "example",
        "criterion": 1,
    },
    {
        # Size filter instead of price, so the size parser is exercised too.
        # Selects lst_004 (90s Track Jacket, $45, size M).
        "name": "matching query with size completes",
        "query": "90s track jacket, size M",
        "wardrobe": "example",
        "criterion": 1,
    },

    # ── Criterion 2: an impossible query stops before suggest_outfit ─────────
    {
        # Nothing in the data matches the words at all.
        "name": "impossible query stops early",
        "query": "designer ballgown size XXS under $5",
        "wardrobe": "example",
        "criterion": 2,
    },
    {
        # The item exists (lst_009, $55) but the ceiling filters it out, so the
        # stop message should point at the price rather than the words.
        "name": "real item priced out stops early",
        "query": "platform mary janes under $20",
        "wardrobe": "example",
        "criterion": 2,
    },

    # ── Criterion 3: same item, outfit suggestion differs across tries ───────
    {
        # No price or size, so search always selects lst_003 (Oversized Flannel)
        # and the only thing that can vary between tries is suggest_outfit's
        # text. Compare the five "Outfit suggestion" blocks in the run log, and
        # check selected_item is lst_003 every time.
        "name": "same item, outfit varies",
        "query": "oversized flannel shirt",
        "wardrobe": "example",
        "criterion": 3,
    },

    # ── Criterion 4: the fit card names the item ─────────────────────────────
    # Three different items, so a pass can't come from one lucky title. For each
    # try, check the fit card mentions the selected_item's title (or an obvious
    # short form of it).
    {
        # Selects lst_008 (Oversized Knit Cardigan — Chunky Brown).
        "name": "fit card names item: cardigan",
        "query": "chunky knit cardigan",
        "wardrobe": "example",
        "criterion": 4,
    },
    {
        # Selects lst_013 (90s Silk Slip Dress — Floral, Midi Length).
        "name": "fit card names item: slip dress",
        "query": "silk slip dress",
        "wardrobe": "example",
        "criterion": 4,
    },
    {
        # Selects lst_009 (Platform Mary Janes — Black Patent). Shoes, so the
        # card can't lean on "wear it with jeans" the way a top can.
        "name": "fit card names item: mary janes",
        "query": "platform mary janes",
        "wardrobe": "example",
        "criterion": 4,
    },

    # ── Criterion 5: selected item is at most 90% of the price ceiling ───────
    # Search ranks by keyword score, not price, so the top match can sit right
    # under the ceiling. Search doesn't call a model, so all five tries of one
    # scenario select the same item — each scenario passes 5/5 or 0/5.
    {
        # lst_002 at $18 of $50 = 36%. Comfortably under.
        "name": "price ceiling, item well under",
        "query": "graphic tee under $50",
        "wardrobe": "example",
        "criterion": 5,
    },
    {
        # lst_007 at $42 of $45 = 93%. Over the 90% line.
        "name": "price ceiling, item near the top",
        "query": "denim jacket under $45",
        "wardrobe": "example",
        "criterion": 5,
    },
    {
        # lst_022 at $75 of $80 = 94%, with cheaper weaker matches ($12, $38)
        # also returned — shows whether ranking ignores price.
        "name": "price ceiling, cheaper options exist",
        "query": "leather bomber under $80",
        "wardrobe": "example",
        "criterion": 5,
    },

    # ── Diagnostics (not one of the five) ────────────────────────────────────
    {
        # A user with nothing saved. One of unit 4's three failure modes.
        "name": "empty wardrobe",
        "query": "denim jacket under $50",
        "wardrobe": "empty",
        "criterion": None,
    },
]

WARDROBES = ("example", "empty")


def validate() -> list[str]:
    """Complain about anything malformed, before a long run rather than during."""
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("query", "").strip():
            problems.append(f"scenario {i} has no query")
        if scenario.get("wardrobe") not in WARDROBES:
            problems.append(
                f"scenario {i} has wardrobe {scenario.get('wardrobe')!r} — "
                f"it should be one of {WARDROBES}"
            )
    return problems

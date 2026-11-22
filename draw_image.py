#!/usr/bin/env python3
"""Draw the 21 November 2026 front page: 'The World Today'.

Build-time composer only (PIL). The graded entrypoint is main.py, which
just copies the pre-drawn entry.png. Run: python3 draw_image.py
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
MARGIN = 48
GUTTER = 20

PAPER = (245, 241, 232)
CARD = (255, 255, 255)
INK = (26, 26, 26)
BODY = (70, 70, 70)
FAINT = (120, 118, 112)
RED = (178, 34, 34)
GOLD = (168, 118, 20)
GREEN = (34, 120, 74)
NAVY = (31, 58, 95)
RULE = (26, 26, 26)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap_text(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_para(draw, x, y, text, fnt, color, max_w, leading):
    """Draw a wrapped paragraph; returns the y just below the last line."""
    for line in wrap_text(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def card_with_band(draw, box, band_color, band_h=12, radius=14):
    """White rounded card whose top strip shows band_color.

    Trick: paint the whole card in the band colour first, then paint a
    slightly shorter white rounded card over it, so the top strip keeps
    the rounded top corners without any square overhang.
    """
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=radius, fill=band_color)
    draw.rounded_rectangle(
        [x0, y0 + band_h, x1, y1], radius=radius, fill=CARD
    )


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    mast = font(SERIF_B, 60)
    dateline = font(SANS_B, 28)
    kick = font(SANS_B, 20)
    head_big = font(SERIF_B, 38)
    head_small = font(SERIF_B, 27)
    body_big = font(SANS, 21)
    body_small = font(SANS, 18)
    tick_font = font(SANS_B, 19)
    foot_font = font(SANS, 16)

    # ---- Masthead -------------------------------------------------
    y = 26
    d.text((MARGIN, y), "THE WORLD TODAY", font=mast, fill=INK)
    y += 78
    d.text((MARGIN, y), "SATURDAY 21 NOVEMBER 2026", font=dateline, fill=RED)
    y += 42
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=4)
    y += 16

    # ---- Lead story ------------------------------------------------
    lead_top = y
    lead_h = 278
    card_with_band(d, (MARGIN, lead_top, W - MARGIN, lead_top + lead_h), RED)
    lx = MARGIN + 26
    ly = lead_top + 20
    d.text((lx, ly), "KRYVYI RIH  ·  UKRAINE", font=kick, fill=RED)
    ly += 30
    ly = draw_para(
        d, lx, ly,
        "A boy and a paramedic killed as missiles hit Zelenskyy's hometown",
        head_big, INK, W - 2 * MARGIN - 52, 46,
    )
    ly += 6
    draw_para(
        d, lx, ly,
        "A Russian ballistic missile struck the centre of Kryvyi Rih on Friday "
        "evening, killing a seven-year-old boy and a 20-year-old paramedic and "
        "wounding dozens. Follow-up drones hit as rescuers worked; about 25 "
        "apartment buildings, a hospital and a restaurant were damaged.",
        body_big, BODY, W - 2 * MARGIN - 52, 27,
    )

    # ---- Four panels, 2 x 2 ---------------------------------------
    col_w = (W - 2 * MARGIN - GUTTER) // 2
    row_y = lead_top + lead_h + 18
    panel_h = 208
    panels = [
        ("MARKETS", GOLD, "Sell-off deepens: S&P \u22123.7%",
         "Wall Street fell into correction as the AI sell-off spread: the "
         "Nikkei dropped 5.06% and the Hang Seng 3.79%."),
        ("POLAND", RED, "Missiles land inside Poland",
         "Two Russian missiles and a jet drone fell on Polish soil during "
         "the assault on Ukraine; a Gripen failed to stop one."),
        ("MEXICO", GREEN, "FBI most-wanted boss seized",
         "Mexican forces captured Fausto Isidro Meza Flores, \u201cEl Chapo "
         "Isidro\u201d, in Sinaloa. Violence followed the arrest."),
        ("COP31  ·  ANTALYA", NAVY, "Climate talks run past deadline",
         "The summit overran its Friday deadline with the fossil-fuel "
         "phase-out call and adaptation finance still unresolved."),
    ]
    for i, (label, color, headline, body) in enumerate(panels):
        px = MARGIN + (i % 2) * (col_w + GUTTER)
        py = row_y + (i // 2) * (panel_h + GUTTER)
        card_with_band(d, (px, py, px + col_w, py + panel_h), color)
        tx = px + 22
        ty = py + 18
        d.text((tx, ty), label, font=kick, fill=color)
        ty += 28
        ty = draw_para(d, tx, ty, headline, head_small, INK, col_w - 44, 34)
        ty += 4
        draw_para(d, tx, ty, body, body_small, BODY, col_w - 44, 24)

    # ---- Ticker ----------------------------------------------------
    tick_y = row_y + 2 * panel_h + GUTTER + 14
    d.line([(MARGIN, tick_y), (W - MARGIN, tick_y)], fill=RULE, width=3)
    tick_y += 12
    ticker = (
        "ALSO  \u00b7  Trump weighs new strikes on Iran  \u00b7  Denmark expels "
        "Russia\u2019s military attach\u00e9  \u00b7  EU approves \u20ac1bn in "
        "military aid for Ukraine  \u00b7  Dengue-cutting mosquitoes: \u221269%  "
        "\u00b7  US measles outbreak update  \u00b7  Voyager data outage continues"
    )
    tick_y = draw_para(
        d, MARGIN, tick_y, ticker, tick_font, RED, W - 2 * MARGIN, 25
    )
    tick_y += 4
    d.text(
        (MARGIN, tick_y),
        "Sources: Reuters \u00b7 AP \u00b7 BBC \u00b7 Al Jazeera  \u2014  21 November 2026",
        font=foot_font, fill=FAINT,
    )

    img.save(OUT, "PNG")
    print("wrote", OUT)


if __name__ == "__main__":
    main()

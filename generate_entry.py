#!/usr/bin/env python3
"""Draw the 1024x1024 news-summary image for 25 November 2026.

Local build tool only (uses Pillow). The competition entry itself is
main.py, which only copies the checked-in entry.png to /output/entry.png
using the standard library -- no network, no fonts, no randomness.

Stories (all verified against Reuters, 25 Nov 2026):
  1. Houthis say they hit Saudi Ras Tanura refinery and Riyadh finance
     district; 4 drones intercepted; 11 wounded in Tuesday's tower strike.
  2. Shenzhou-24 launches with Pakistani astronaut Muhammad Zeeshan Ali,
     first foreigner aboard Tiangong.
  3. Ukrainian drones hit Syzran / Kuibyshev refineries in Samara region;
     one killed; 145 drones downed in the region.
  4. Asian stocks tumble on tariff fears; Nvidia -5.9%, Anthropic -6.5%
     below its $83 IPO price.
  5. Carles Puigdemont to return to Spain on Dec 12, ending ~9 years exile.
  6. US jury convicts Huawei on 10 of 12 counts; Microsoft declares
     Code Red after historic 24h outage; US consumer confidence 103.3.

Run:  python3 generate_entry.py [output-path, default: entry.png]
"""
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 243, 232)
INK = (17, 17, 17)
MUTED = (90, 84, 70)
RULE = (17, 17, 17)
RED = (178, 34, 34)
RED_BG = (250, 231, 229)
GREEN = (27, 120, 55)
GREEN_BG = (224, 240, 226)
BLUE = (24, 90, 160)
BLUE_BG = (226, 236, 248)
TEAL = (14, 110, 110)
TEAL_BG = (220, 240, 238)
AMBER = (166, 110, 0)
AMBER_BG = (250, 240, 210)
PURPLE = (96, 60, 140)
PURPLE_BG = (236, 228, 246)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, fnt, width):
    """Greedy word wrap by pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, width, fill=INK, leading=5):
    for ln in wrap(draw, text, fnt, width):
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def story_box(d, x, y, w, h, kicker, kicker_fill, headline, body,
              bg, accent):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10,
                        fill=bg, outline=accent, width=2)
    tx, ty = x + 18, y + 14
    d.text((tx, ty), kicker, font=font(SANS_B, 18), fill=accent)
    ty += 28
    ty = draw_wrapped(d, tx, ty, headline, font(SERIF_B, 30), w - 36,
                      leading=2)
    ty += 6
    draw_wrapped(d, tx, ty, body, font(SANS, 20), w - 36, leading=4)
    return y + h


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "entry.png")
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    mx = 30

    # ---------- Masthead ----------
    y = 26
    d.text((W // 2, y), "THE WORLD IN ONE PAGE", font=font(SERIF_B, 58),
           fill=INK, anchor="mt")
    y = 100
    d.line([(mx, y), (W - mx, y)], fill=RULE, width=3)
    y += 12
    d.text((W // 2, y),
           "WEDNESDAY, 25 NOVEMBER 2026  \u2022  SIX STORIES THAT DEFINED THE DAY",
           font=font(SANS_B, 21), fill=INK, anchor="mt")
    y += 34
    d.line([(mx, y), (W - mx, y)], fill=RULE, width=1)

    # ---------- Lead story: Houthis hit Saudi Arabia ----------
    y += 14
    lead_top = y
    lead_h = 206
    d.rounded_rectangle([mx, lead_top, W - mx, lead_top + lead_h], radius=10,
                        fill=RED_BG, outline=RED, width=2)
    lx, ly = mx + 22, lead_top + 16
    d.text((lx, ly), "1  \u2022  GULF  \u2014  SAUDI UNDER FIRE",
           font=font(SANS_B, 20), fill=RED)
    ly += 30
    d.text((lx, ly), "SAUDI UNDER FIRE", font=font(SERIF_B, 54), fill=INK)
    ly += 66
    draw_wrapped(d, lx, ly,
                 "Yemen's Houthis say they hit Saudi Arabia's Ras Tanura "
                 "refinery and Riyadh's financial district. Four drones "
                 "were intercepted; 11 were wounded on Tuesday.",
                 font(SANS, 22), 640, leading=5)
    # Right side: skyline + badge
    cx0, cy0 = W - mx - 250, lead_top + 22
    d.rounded_rectangle([cx0, cy0, cx0 + 210, cy0 + 108], radius=8,
                        fill=(17, 17, 17))
    d.rectangle([cx0 + 22, cy0 + 52, cx0 + 62, cy0 + 92], fill=(255, 205, 80))
    d.rectangle([cx0 + 88, cy0 + 22, cx0 + 122, cy0 + 92], fill=(255, 205, 80))
    d.rectangle([cx0 + 148, cy0 + 62, cx0 + 188, cy0 + 92], fill=(255, 205, 80))
    d.rectangle([cx0 + 100, cy0 + 8, cx0 + 110, cy0 + 22], fill=(255, 205, 80))
    for wy in (36, 52, 68):
        d.rectangle([cx0 + 94, cy0 + wy, cx0 + 116, cy0 + wy + 8],
                    fill=(17, 17, 17))
    d.rounded_rectangle([cx0, cy0 + 122, cx0 + 210, cy0 + 164], radius=18,
                        fill=RED)
    d.text((cx0 + 105, cy0 + 143), "11 WOUNDED", font=font(SANS_B, 24),
           fill=(255, 255, 255), anchor="mm")

    # ---------- Two-column stories ----------
    y = lead_top + lead_h + 16
    col_w = (W - 2 * mx - 16) // 2
    left_x, right_x = mx, mx + col_w + 16
    box_h = 208
    gap = 16

    story_box(d, left_x, y, col_w, box_h,
              "2  \u2022  SPACE  \u2014  FIRST FOREIGNER IN ORBIT", BLUE,
              "A Pakistani in orbit",
              "China's Shenzhou-24 launches with Pakistani astronaut "
              "Muhammad Zeeshan Ali, the first foreigner aboard the "
              "Tiangong space station. The crew docked the same day.",
              BLUE_BG, BLUE)
    story_box(d, right_x, y, col_w, box_h,
              "3  \u2022  UKRAINE  \u2014  DRONES HIT SAMARA", RED,
              "Refineries ablaze",
              "Ukrainian drones hit two Rosneft refineries in Samara; "
              "one person was killed and 145 drones were downed in "
              "the region.",
              RED_BG, RED)

    y += box_h + gap
    story_box(d, left_x, y, col_w, box_h,
              "4  \u2022  MARKETS  \u2014  AI RALLY FADES", AMBER,
              "Nvidia falls 5.9%",
              "Asian stocks tumble as tariff fears return. Nvidia falls "
              "5.9% and Anthropic drops 6.5%, below its $83 IPO price.",
              AMBER_BG, AMBER)
    story_box(d, right_x, y, col_w, box_h,
              "5  \u2022  EUROPE  \u2014  PUIGDEMONT TO RETURN", PURPLE,
              "Exile ends Dec 12",
              "Catalan separatist leader Carles Puigdemont says he will "
              "return to Spain on Dec 12, ending nearly a decade in exile.",
              PURPLE_BG, PURPLE)

    # ---------- Bottom strip: Tech & US ----------
    y += box_h + gap
    bot_h = 118
    d.rounded_rectangle([mx, y, W - mx, y + bot_h], radius=10,
                        fill=TEAL_BG, outline=TEAL, width=2)
    bx, by = mx + 18, y + 14
    d.text((bx, by), "6  \u2022  TECH & US", font=font(SANS_B, 18), fill=TEAL)
    by += 28
    draw_wrapped(d, bx, by,
                 "US jury convicts Huawei on 10 of 12 counts. Microsoft "
                 "declares Code Red after a historic 24-hour outage. "
                 "US consumer confidence hits 103.3, its highest in "
                 "nearly two years.",
                 font(SANS, 20), W - 2 * mx - 36, leading=4)

    # ---------- Footer ----------
    fy = y + bot_h + 12
    d.text((W // 2, fy), "Sources: Reuters, Xinhua  \u2022  25 November 2026",
           font=font(SANS, 17), fill=MUTED, anchor="mt")

    img.save(out, "PNG")
    print(f"wrote {out} {out.stat().st_size} bytes")


if __name__ == "__main__":
    main()

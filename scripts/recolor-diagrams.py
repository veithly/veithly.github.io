#!/usr/bin/env python3
"""
Recolor all SVG diagrams to match the new editorial palette.

Run from docs-site/:
    python scripts/recolor-diagrams.py

Strategy
========
The Excalidraw-style SVGs were generated with a "vintage parchment" palette
(yellow-paper #fdf6e3 + bright #f97316 etc). The new site chrome is Swiss
Modernism / Editorial (warm white paper + refined slate ink + single vibrant
orange accent). This script remaps the diagrams to match, in three buckets:

1. Paper substrate (yellow papyrus -> warm editorial white)
2. Accents (bright primaries -> refined editorial tones)
3. Strokes (mid-gray -> slate-800/700 hierarchy)

The replacement is case-insensitive and keeps inline alpha / opacity intact.
"""
from __future__ import annotations
import re
from pathlib import Path

# ----- canonical editorial palette -------------------------------------------
PAPER = "#fbfaf7"           # primary substrate (was #fdf6e3 solarized yellow)
PAPER_SOFT = "#f5f4ef"      # secondary substrate
PAPER_STRONG = "#e7e5dc"    # card / quote backdrop
PAPER_LINE = "#e2e8f0"      # dividers / thin borders

INK = "#0f172a"             # slate-900 (was #1e293b slate-800)
INK_SOFT = "#334155"        # slate-700
INK_MUTED = "#64748b"       # slate-500

# accents — refined toward Editorial palette
COLOR_TRADEOFF = "#ea580c"  # orange-600 (was bright #f97316)
COLOR_SHARED = "#15803d"    # emerald-700 (slightly muted from #16a34a)
COLOR_JUDGMENT = "#6d28d9"  # violet-700 (slightly muted from #7c3aed)
COLOR_RISK = "#b91c1c"      # red-700 (muted from #dc2626)
COLOR_SOURCE = "#1d4ed8"    # blue-700 (muted from #2563eb)

# soft callout backgrounds — refined pastels
CALLOUT_ORANGE = "#fed7aa"  # orange-200, keep
CALLOUT_AMBER = "#fef3c7"   # amber-100 (was yellow-100 #fef9c3)
CALLOUT_GREEN = "#dcfce7"   # emerald-100, keep
CALLOUT_BLUE = "#dbeafe"    # blue-100, keep
CALLOUT_INDIGO = "#e0e7ff"  # indigo-100, keep
CALLOUT_RED = "#fee2e2"     # red-100, keep
CALLOUT_VIOLET = "#ede9fe"  # violet-100, keep
CALLOUT_SLATE = "#f1f5f9"   # slate-100, keep

# ----- recolor map -----------------------------------------------------------
# (from_hex_lowercase -> to_hex)
RECOLOR: dict[str, str] = {
    # paper substrate
    "#fdf6e3": PAPER,
    "#fffef7": PAPER,
    "#f8fafc": PAPER_SOFT,

    # accents — refine to editorial
    "#f97316": COLOR_TRADEOFF,           # bright orange -> editorial orange-600
    "#dc2626": COLOR_RISK,               # bright red -> red-700
    "#7c3aed": COLOR_JUDGMENT,           # bright violet -> violet-700
    "#2563eb": COLOR_SOURCE,             # bright blue -> blue-700
    "#16a34a": COLOR_SHARED,             # bright green -> emerald-700
    "#0ea5e9": COLOR_SOURCE,             # sky blue -> blue-700 (consolidate)
    "#a855f7": COLOR_JUDGMENT,           # purple -> violet-700
    "#b91c1c": COLOR_RISK,               # already red-700, keep
    "#b45309": "#92400e",                # amber-700 -> darker for editorial

    # soft backgrounds — keep mostly, slightly refine yellow
    "#fef9c3": CALLOUT_AMBER,            # yellow-100 -> amber-100
    "#fde68a": "#fde68a",                # keep amber-200
    "#fef3c7": CALLOUT_AMBER,            # already amber-100
    "#fce7f3": "#fce7f3",                # keep pink-100
    "#ecfccb": "#dcfce7",                # lime-100 -> emerald-100 (consolidate)
    "#e9d5ff": CALLOUT_VIOLET,           # violet-200 -> violet-100 (consolidate)

    # inks — push hierarchy toward slate-900 / slate-700
    "#1e293b": INK,                      # slate-800 -> slate-900
    "#475569": INK_SOFT,                 # slate-600 -> slate-700
    "#94a3b8": INK_MUTED,                # slate-400 -> slate-500 (slightly darker)
}


def recolor_text(s: str) -> tuple[str, int]:
    """Return (new_text, replacement_count)."""
    count = 0

    # case-insensitive replace; preserve uppercase letters in replacement if seen uppercase
    def _sub(match: re.Match) -> str:
        nonlocal count
        original = match.group(0)
        key = original.lower()
        if key in RECOLOR:
            count += 1
            new = RECOLOR[key]
            # keep case style of the original token
            return new.upper() if original[1:].isupper() else new
        return original

    # match #rrggbb hex tokens
    new_text = re.sub(r"#[0-9a-fA-F]{6}", _sub, s)
    return new_text, count


def main() -> int:
    diagrams_dir = Path(__file__).resolve().parent.parent / "public" / "diagrams"
    if not diagrams_dir.exists():
        print(f"ERROR: {diagrams_dir} not found")
        return 1

    total_files = 0
    total_swaps = 0
    untouched = 0
    skipped: list[str] = []
    for svg_path in sorted(diagrams_dir.glob("*.svg")):
        try:
            original = svg_path.read_text(encoding="utf-8", errors="strict")
        except UnicodeDecodeError:
            skipped.append(svg_path.name)
            continue
        updated, n = recolor_text(original)
        if n > 0:
            svg_path.write_text(updated, encoding="utf-8")
            total_files += 1
            total_swaps += n
            print(f"  [{n:4d}]  {svg_path.name}")
        else:
            untouched += 1
    if skipped:
        print(f"\nSkipped (non-UTF-8): {', '.join(skipped)}")

    print()
    print(f"Recolored {total_files} files; {total_swaps} color swaps.")
    print(f"Untouched: {untouched} (already on editorial palette or pure-grayscale).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Replace Greek homoglyphs with ASCII equivalents using a predefined map."""

from __future__ import annotations

import json
from pathlib import Path

_MAP_PATH = Path(__file__).with_name("homoglyph_map.json")

with _MAP_PATH.open("r", encoding="utf-8") as fh:
    HOMOGLYPH_MAP: dict[str, str] = json.load(fh)


def replace_homoglyphs(text: str) -> str:
    """Return text with Greek homoglyphs replaced by ASCII characters."""
    return "".join(HOMOGLYPH_MAP.get(ch, ch) for ch in text)

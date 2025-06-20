from __future__ import annotations

ZERO_WIDTH_CHARS = {
    "\u200b",  # zero width space
    "\u200c",  # zero width non-joiner
    "\u200d",  # zero width joiner
    "\u2060",  # word joiner
    "\ufeff",  # zero width no-break space
}

_REMOVE_TABLE = str.maketrans("", "", "".join(ZERO_WIDTH_CHARS))


def strip_zero_width(text: str) -> str:
    """Remove zero-width Unicode characters from ``text``."""
    return text.translate(_REMOVE_TABLE)

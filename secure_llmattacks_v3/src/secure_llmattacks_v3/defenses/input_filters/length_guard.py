"""Simple token-length guard for input strings."""
from __future__ import annotations

from typing import Optional


MAX_TOKENS = 8192


def abort_if_exceeds(text: str, max_tokens: int = MAX_TOKENS) -> Optional[str]:
    """Return ``text`` unless token count exceeds ``max_tokens``.

    Tokenisation is approximated by whitespace splitting so it works
    without external dependencies.  If the number of tokens is greater
    than ``max_tokens`` ``None`` is returned to signal the input should
    be rejected by the caller.
    """
    tokens = text.split()
    if len(tokens) > max_tokens:
        return None
    return text

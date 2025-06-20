"""JailGuard-style output risk scoring.

This module implements a lightweight version of the
JailGuard risk metric which detects adversarial suffixes
attached to language-model outputs. The original demo of
this technique is available from the Hugging Face Spaces
platform under the name ``JailGuard``.

The score combines two signals:
1. Token overlap with a corpus of known adversarial
   suffix prompts stored under ``attacks/suffixes/``.
2. Detection of suspicious line endings such as ``"Assistant:"``
   or "###" which often appear in jailbreak payloads.

Examples
--------
>>> guard = JailGuard()
>>> guard.is_suspicious("Sure, here's how you can do it ###")
True
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, Set


class JailGuard:
    """Risk scoring utility for suspicious LLM outputs."""

    _SUFFIX_PATTERNS = [
        re.compile(r"(?i)assistant:\s*$"),
        re.compile(r"(?i)user:\s*$"),
        re.compile(r"###\s*$"),
    ]

    def __init__(self, suffix_dir: Path | None = None) -> None:
        self.suffix_dir = suffix_dir or Path(__file__).resolve().parents[2] / "attacks" / "suffixes"
        self.suspicious_tokens: Set[str] = self._load_tokens(self.suffix_dir)

    @staticmethod
    def _load_tokens(directory: Path) -> Set[str]:
        tokens: Set[str] = set()
        if directory.exists():
            for file in directory.rglob("*.txt"):
                with open(file, encoding="utf-8") as fh:
                    for line in fh:
                        tokens.update(re.findall(r"\w+", line.lower()))
        return tokens

    @staticmethod
    def _tokenize(text: str) -> Iterable[str]:
        return re.findall(r"\w+", text.lower())

    def risk_score(self, text: str) -> float:
        tokens = list(self._tokenize(text))
        if not tokens:
            return 0.0
        overlap = sum(1 for t in tokens if t in self.suspicious_tokens) / len(tokens)
        suffix_flag = any(p.search(text) for p in self._SUFFIX_PATTERNS)
        return overlap + (1.0 if suffix_flag else 0.0)

    def is_suspicious(self, text: str, threshold: float = 0.5) -> bool:
        """Return ``True`` if ``text`` exceeds the risk ``threshold``."""
        return self.risk_score(text) >= threshold

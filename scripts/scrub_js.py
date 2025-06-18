#!/usr/bin/env python3
"""Remove third-party JavaScript and cookie banners from files.

Usage: python scripts/scrub_js.py [paths...]
If no paths are given, all Markdown and HTML files under docs/ are processed.
The script edits files in-place and prints the names of modified files.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parents[1] / "docs"

# Regex matching <script> tags including their content
SCRIPT_TAG_RE = re.compile(r"<script\b[^<]*(?:(?!</script>)<[^<]*)*</script>", re.I | re.S)
# Lines referencing common cookie banners
COOKIE_RE = re.compile(r"cookie(consent|bot|banner)|js-cookie", re.I)


def scrub_text(text: str) -> str:
    """Remove script blocks and cookie banner lines."""
    text = SCRIPT_TAG_RE.sub("", text)
    lines = [line for line in text.splitlines() if not COOKIE_RE.search(line)]
    return "\n".join(lines)


def process_file(path: Path) -> None:
    original = path.read_text(encoding="utf-8", errors="ignore")
    cleaned = scrub_text(original)
    if cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
        print(f"Cleaned {path}")


def main(argv: list[str]) -> None:
    if argv:
        paths = [Path(p) for p in argv]
    else:
        paths = []
        for ext in ("*.md", "*.html"):
            paths.extend(DOCS_DIR.rglob(ext))
    for p in paths:
        if p.is_file():
            process_file(p)


if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/env python3
"""Simple link checker for Markdown files."""
from pathlib import Path
import json
import re
import os
import requests
import sys

LINK_RE = re.compile(r'https?://[^\s)>"]+')
ARCHIVE_FILE = Path("link_archive.json")
_archive_cache = None


def load_archive():
    global _archive_cache
    if _archive_cache is None and ARCHIVE_FILE.exists():
        try:
            _archive_cache = json.loads(ARCHIVE_FILE.read_text())
        except Exception:
            _archive_cache = {}
    return _archive_cache or {}


def check(url: str) -> bool:
    # During FAST_LINK_CHECK runs we skip network calls entirely to keep tests
    # deterministic and quick. Any URL is considered valid in this mode.
    if os.getenv("FAST_LINK_CHECK"):
        return True

    try:
        r = requests.head(url, allow_redirects=True, timeout=10)
        if r.status_code >= 400:
            r = requests.get(url, allow_redirects=True, timeout=10)
        if r.status_code < 400:
            return True
    except Exception as e:
        print(f"{url}: {e}")
    archive = load_archive()
    snap = archive.get(url, {}).get("snapshot")
    return bool(snap)


def main():
    failed = False
    max_links = int(os.getenv("FAST_LINK_CHECK", "0"))
    count = 0
    for path in Path("docs").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for link in LINK_RE.findall(text):
            if max_links and count >= max_links:
                break
            count += 1
            if not check(link):
                print(f"{path}: broken link {link}")
                failed = True
        if max_links and count >= max_links:
            break
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

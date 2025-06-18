#!/usr/bin/env python3
"""Simple link checker for Markdown files."""
from pathlib import Path
import json
import re
import requests
import sys

LINK_RE = re.compile(r'https?://[^\s)>"]+')
ARCHIVE_FILE = Path('link_archive.json')
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
    try:
        r = requests.head(url, allow_redirects=True, timeout=10)
        if r.status_code >= 400:
            r = requests.get(url, allow_redirects=True, timeout=10)
        if r.status_code < 400:
            return True
    except Exception as e:
        print(f"{url}: {e}")
    archive = load_archive()
    snap = archive.get(url, {}).get('snapshot')
    return bool(snap)


def main():
    failed = False
    for path in Path('docs').rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        for link in LINK_RE.findall(text):
            if not check(link):
                print(f"{path}: broken link {link}")
                failed = True
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())


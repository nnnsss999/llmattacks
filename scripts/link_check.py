#!/usr/bin/env python3
"""Simple link checker for Markdown files."""
from pathlib import Path
import re
import requests
import sys

LINK_RE = re.compile(r'https?://[^\s)>"]+')


def check(url: str) -> bool:
    try:
        r = requests.head(url, allow_redirects=True, timeout=10)
        if r.status_code >= 400:
            r = requests.get(url, allow_redirects=True, timeout=10)
        return r.status_code < 400
    except Exception as e:
        print(f"{url}: {e}")
        return False


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


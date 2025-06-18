#!/usr/bin/env python3
"""Refresh external links and archive snapshots via the Wayback Machine."""
import json
import re
from datetime import date
from pathlib import Path

import requests

LINK_RE = re.compile(r'https?://[^\s)>"]+')
AVAILABLE_API = "https://archive.org/wayback/available?url="
SAVE_API = "https://web.archive.org/save/"


def collect_links():
    links = set()
    for path in Path('docs').rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        links.update(LINK_RE.findall(text))
    return sorted(links)


def head_status(url: str) -> int:
    try:
        resp = requests.head(url, allow_redirects=True, timeout=10)
        if resp.status_code >= 400:
            resp = requests.get(url, allow_redirects=True, timeout=10)
        return resp.status_code
    except Exception:
        return 0


def fetch_snapshot(url: str) -> str:
    try:
        resp = requests.get(AVAILABLE_API + url, timeout=10)
        if resp.status_code == 200:
            data = resp.json().get('archived_snapshots', {}).get('closest', {})
            if data.get('available'):
                return data.get('url', '')
    except Exception:
        pass
    try:
        resp = requests.get(SAVE_API + url, timeout=20)
        if resp.status_code in (200, 302):
            loc = resp.headers.get('Content-Location')
            if loc:
                return 'https://web.archive.org' + loc
    except Exception:
        pass
    return ''


def refresh():
    result = {}
    today = date.today().isoformat()
    for url in collect_links():
        status = head_status(url)
        snapshot = fetch_snapshot(url)
        result[url] = {
            'status': status,
            'snapshot': snapshot,
            'checked': today,
        }
    Path('link_archive.json').write_text(json.dumps(result, indent=2), encoding='utf-8')


if __name__ == '__main__':
    refresh()

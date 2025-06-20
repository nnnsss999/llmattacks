#!/usr/bin/env python3
"""Collect external URLs from all text files in the repository.

Scans Markdown, HTML, JSON, YAML and source code files under the repo root,
including the `original/` and `docs/` directories. The resulting unique list is
written to `docs/urls.md` sorted alphabetically.
"""
import re
from pathlib import Path

URL_RE = re.compile(r'https?://[^\s<>"]+')

# File extensions considered text
TEXT_EXTS = {
    '.md', '.html', '.txt', '.py', '.json', '.yml', '.yaml', '.csv', '.js',
}

EXCLUDE_PATHS = {
    Path('docs/urls.md'),
}


def gather_links() -> list[str]:
    links = set()
    for path in Path('.').rglob('*'):
        if path.is_file():
            if path in EXCLUDE_PATHS:
                continue
            if path.suffix.lower() not in TEXT_EXTS:
                # Attempt to read other files as text but ignore errors
                try:
                    text = path.read_text(encoding='utf-8', errors='ignore')
                except Exception:
                    continue
            else:
                text = path.read_text(encoding='utf-8', errors='ignore')
            for match in URL_RE.findall(text):
                clean = match.rstrip(".,);:!?\"'\\]")
                links.add(clean)
    return sorted(links)


def main() -> None:
    urls = gather_links()
    out = Path('docs/urls.md')
    out.write_text(''.join(f'- [{u}]({u})\n' for u in urls), encoding='utf-8')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Fetch URLs listed in docs/urls.md and convert them to Markdown."""

from __future__ import annotations

import datetime
import hashlib
import io
import json
from pathlib import Path
from typing import Dict

import requests
import yaml
from markdownify import markdownify
from pdfminer.high_level import extract_text_to_fp

DOCS_DIR = Path(__file__).resolve().parents[1] / "docs"
URLS_FILE = DOCS_DIR / "urls.md"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "extractions1"
LOG_FILE = OUTPUT_DIR / "extraction_log.json"


def load_urls() -> list[str]:
    lines = URLS_FILE.read_text(encoding="utf-8").splitlines()
    urls = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("-"):
            line = line[1:].strip()
        urls.append(line)
    return urls


def parse_front_matter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    try:
        return yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return None


def build_existing_map() -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    for path in DOCS_DIR.rglob("*.md"):
        fm = parse_front_matter(path)
        if fm and (url := fm.get("source_url")):
            mapping[url] = str(path.relative_to(DOCS_DIR))
    return mapping


def html_to_markdown(text: str) -> str:
    return markdownify(text, heading_style="ATX")


def pdf_to_markdown(data: bytes) -> str:
    output = io.StringIO()
    extract_text_to_fp(io.BytesIO(data), output)
    return output.getvalue()


def save_markdown(content: str, url: str) -> str:
    slug = hashlib.sha256(url.encode()).hexdigest()[:10]
    path = OUTPUT_DIR / f"{slug}.md"
    fm = {
        "title": url,
        "source_url": url,
        "date_collected": datetime.date.today().isoformat(),
        "license": "Fair Use",
    }
    text = "---\n" + yaml.safe_dump(fm, sort_keys=False) + "---\n\n" + content
    path.write_text(text, encoding="utf-8")
    return str(path.relative_to(OUTPUT_DIR))


def process_url(url: str) -> str:
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()
    ctype = resp.headers.get("content-type", "").lower()
    if "pdf" in ctype or url.lower().endswith(".pdf"):
        content = pdf_to_markdown(resp.content)
    else:
        content = html_to_markdown(resp.text)
    return save_markdown(content, url)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    existing = build_existing_map()
    urls = load_urls()
    log: Dict[str, dict] = {}
    for url in urls:
        if url in existing:
            log[url] = {"existing": existing[url]}
            continue
        try:
            md_path = process_url(url)
            log[url] = {"saved_as": md_path}
        except Exception as exc:
            log[url] = {"error": str(exc)}
    LOG_FILE.write_text(json.dumps(log, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

"""Download and cache PDF sources referenced in docs.

Only downloads PDFs when the YAML front matter specifies a permissive license
containing 'CC', 'open', or 'public'. Otherwise metadata about the PDF URL is
stored in pdfs/metadata.json.
"""

import json
import hashlib
import re
import requests
from pathlib import Path
import yaml

DOCS_DIR = Path(__file__).resolve().parents[1] / "docs"
CACHE_DIR = Path(__file__).resolve().parents[1] / "pdfs"
META_FILE = CACHE_DIR / "metadata.json"


def parse_front_matter(text: str):
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return None
    try:
        closing_idx = lines[1:].index("---") + 1
    except ValueError:
        return None
    front = "\n".join(lines[1:closing_idx])
    try:
        return yaml.safe_load(front) or {}
    except yaml.YAMLError:
        return None


def allowed_license(license_text: str | None) -> bool:
    if not license_text:
        return False
    text = license_text.lower()
    return any(key in text for key in ["cc", "open", "public"])


def cache_pdfs():
    CACHE_DIR.mkdir(exist_ok=True)
    metadata = []
    for path in DOCS_DIR.rglob("*.*"):
        if path.suffix not in {".md", ".html"}:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        fm = parse_front_matter(content)
        license_text = fm.get("license") if fm else None
        pdf_links = re.findall(r"https?://\S+\.pdf", content)
        for url in pdf_links:
            entry = {
                "source": str(path.relative_to(DOCS_DIR)),
                "pdf_url": url,
                "license": license_text or "",
            }
            if allowed_license(license_text):
                try:
                    resp = requests.get(url, timeout=15)
                    if resp.status_code == 200:
                        name = hashlib.sha256(url.encode()).hexdigest() + ".pdf"
                        (CACHE_DIR / name).write_bytes(resp.content)
                        entry["file"] = name
                except Exception:
                    entry["error"] = "download failed"
            metadata.append(entry)
    META_FILE.write_text(json.dumps(metadata, indent=2), encoding="utf-8")


if __name__ == "__main__":
    cache_pdfs()

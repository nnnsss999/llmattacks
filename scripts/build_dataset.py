#!/usr/bin/env python3
"""Generate attacks dataset as newline-delimited JSON."""

from __future__ import annotations

import uuid
import unicodedata
import re
from pathlib import Path
import sys

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from datasets.schema import AttackSample

ATTACKS_DIR = PROJECT_ROOT / "attacks"
OUT_FILE = PROJECT_ROOT / "datasets" / "v1" / "attacks.jsonl"

ZERO_WIDTH_RE = re.compile("[\u200b\u200c\u200d\ufeff]")


def strip_zero_width(text: str) -> str:
    """Remove zero width characters used for obfuscation."""
    return ZERO_WIDTH_RE.sub("", text)


def parse_front_matter(text: str) -> dict[str, str] | None:
    """Extract YAML front matter from a Markdown file."""
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        try:
            closing = lines[1:].index("---") + 1
        except ValueError:
            return None
        front = "\n".join(lines[1:closing])
        try:
            return yaml.safe_load(front) or {}
        except yaml.YAMLError:
            return None
    return None


def iter_attack_files() -> list[Path]:
    """Return all Markdown attack files under ATTACKS_DIR."""
    return sorted(p for p in ATTACKS_DIR.rglob("*.md") if p.is_file())


def load_samples() -> list[AttackSample]:
    samples: list[AttackSample] = []
    for path in iter_attack_files():
        raw = path.read_text(encoding="utf-8", errors="ignore")
        meta = parse_front_matter(raw) or {}
        lines = raw.splitlines()
        if meta:
            try:
                closing = lines[1:].index("---") + 1
                body = "\n".join(lines[closing + 1 :])
            except ValueError:
                body = "\n".join(lines[1:])
        else:
            body = raw
        text = strip_zero_width(unicodedata.normalize("NFC", body))
        attack_type = meta.get("attack_type")
        if not attack_type:
            rel_parts = path.relative_to(ATTACKS_DIR).parts
            attack_type = (
                "_".join(rel_parts[:2]) if len(rel_parts) >= 2 else rel_parts[0]
            )
        sample = AttackSample(
            uuid=str(uuid.uuid4()),
            text=text,
            label=1,
            attack_type=str(attack_type),
            source_path=str(path.relative_to(PROJECT_ROOT)),
        )
        samples.append(sample)
    return samples


def build_dataset(samples: list[AttackSample]) -> None:
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUT_FILE.open("w", encoding="utf-8") as fh:
        for sample in samples:
            fh.write(sample.model_dump_json() + "\n")
    print(f"Wrote {OUT_FILE} ({len(samples)} rows)")


def main() -> None:
    build_dataset(load_samples())


if __name__ == "__main__":
    main()

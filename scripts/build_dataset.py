#!/usr/bin/env python3
"""Build the attacks dataset from Markdown files.

Run with ``--check-only`` to validate that all Markdown files can be parsed
into :class:`~datasets.schema.AttackSample` instances without writing the
output file. The command exits with a non-zero status code if validation fails.
"""

from __future__ import annotations

import uuid
import unicodedata
from pathlib import Path
import argparse

import json
import yaml

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from datasets.schema import AttackSample

ROOT = Path(__file__).resolve().parents[1]
ATTACKS_DIR = ROOT / "attacks"
OUT_DIR = ROOT / "datasets" / "v1"
OUT_FILE = OUT_DIR / "attacks.jsonl"

ZERO_WIDTH = {ord(c): None for c in ["\u200b", "\u200c", "\u200d", "\ufeff"]}


def parse_front_matter(path: Path) -> tuple[dict, str]:
    """Return front matter dict and remaining text."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        try:
            end = lines[1:].index("---") + 1
        except ValueError:
            end = 0
        if end:
            fm = "\n".join(lines[1:end])
            body = "\n".join(lines[end + 1 :])
            try:
                data = yaml.safe_load(fm) or {}
            except yaml.YAMLError:
                data = {}
            return data, body
    return {}, text


def clean_text(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    return text.translate(ZERO_WIDTH)


def gather_samples() -> list[AttackSample]:
    samples: list[AttackSample] = []
    for path in ATTACKS_DIR.rglob("*.md"):
        fm, body = parse_front_matter(path)
        record = {
            "uuid": str(uuid.uuid4()),
            "text": clean_text(body),
            "label": 1,
            "attack_type": fm.get("attack_type", "unknown"),
            "source_path": str(path.relative_to(ROOT)),
        }
        sample = AttackSample(**record)
        samples.append(sample)
    return samples


def build_dataset(check_only: bool = False) -> None:
    samples = gather_samples()
    if check_only:
        print(f"Validated {len(samples)} samples")
        return
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_FILE.open("w", encoding="utf-8") as f:
        for sample in samples:
            json.dump(sample.model_dump(), f, ensure_ascii=False)
            f.write("\n")
    print(f"Wrote {OUT_FILE} ({len(samples)} rows)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Validate samples without writing output",
    )
    args = parser.parse_args()
    build_dataset(check_only=args.check_only)


if __name__ == "__main__":
    main()

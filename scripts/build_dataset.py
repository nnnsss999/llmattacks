#!/usr/bin/env python3
"""Build the attacks dataset from Markdown files.

Usage::

    python scripts/build_dataset.py [--out-dir DIR] [--format json|csv]

The script walks ``attacks/`` for ``*.md`` files, normalises text and writes a
validated dataset. By default ``datasets/v1/attacks.jsonl`` is created.
"""

from __future__ import annotations

import uuid
import unicodedata
from pathlib import Path
import argparse
import csv

import json
import yaml

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from datasets.schema import AttackSample

ROOT = Path(__file__).resolve().parents[1]
ATTACKS_DIR = ROOT / "attacks"
DEFAULT_OUT_DIR = ROOT / "datasets" / "v1"

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


def build_dataset(out_dir: Path, fmt: str) -> Path:
    samples = gather_samples()
    out_dir.mkdir(parents=True, exist_ok=True)
    if fmt == "csv":
        out_file = out_dir / "attacks.csv"
        with out_file.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["uuid", "text", "label", "attack_type", "source_path"],
            )
            writer.writeheader()
            for sample in samples:
                writer.writerow(sample.model_dump())
    else:
        out_file = out_dir / "attacks.jsonl"
        with out_file.open("w", encoding="utf-8") as f:
            for sample in samples:
                json.dump(sample.model_dump(), f, ensure_ascii=False)
                f.write("\n")
    print(f"Wrote {out_file} ({len(samples)} rows)")
    return out_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build dataset from markdown")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=DEFAULT_OUT_DIR,
        help="directory for output files",
    )
    parser.add_argument(
        "--format",
        choices=["json", "csv"],
        default="json",
        help="output format (json or csv)",
    )
    args = parser.parse_args()
    build_dataset(args.out_dir, args.format)

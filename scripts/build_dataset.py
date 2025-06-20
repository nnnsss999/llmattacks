#!/usr/bin/env python3
"""Build the attacks dataset from Markdown files.

Usage::

    python scripts/build_dataset.py [--out-dir DATASETS/VERSION] [--format {parquet,csv}]

The script scans ``attacks/`` for Markdown files, normalises the
text, validates each record with ``AttackSample`` and writes the output
dataset. Parquet is the default and recommended format for training.
"""

from __future__ import annotations

import uuid
import unicodedata
import argparse
from pathlib import Path

import yaml
import pyarrow as pa
import pyarrow.parquet as pq

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
    """Generate dataset in the given directory and return the output path."""
    samples = gather_samples()
    out_dir.mkdir(parents=True, exist_ok=True)
    table = pa.Table.from_pylist([s.model_dump() for s in samples])
    out_file = out_dir / f"attacks.{ 'parquet' if fmt == 'parquet' else 'csv' }"
    if fmt == "parquet":
        pq.write_table(table, out_file)
    else:
        import pandas as pd

        df = table.to_pandas()
        df.to_csv(out_file, index=False)
    print(f"Wrote {out_file} ({table.num_rows} rows)")
    return out_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build attacks dataset")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=DEFAULT_OUT_DIR,
        help="Destination directory for the dataset",
    )
    parser.add_argument(
        "--format",
        choices=["parquet", "csv"],
        default="parquet",
        help="Output file format",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    build_dataset(args.out_dir, args.format)

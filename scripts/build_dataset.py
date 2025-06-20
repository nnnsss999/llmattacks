#!/usr/bin/env python3
"""Build the attacks dataset from Markdown, text, and Python files.

Usage::

    python scripts/build_dataset.py [--out-dir PATH] [--format {parquet,csv}]
    python scripts/build_dataset.py --check-only
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
EXTS = {".md", ".txt", ".py"}

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
    for path in ATTACKS_DIR.rglob("*"):
        if path.suffix.lower() not in EXTS:
            continue
        if path.suffix.lower() == ".md":
            fm, body = parse_front_matter(path)
        else:
            fm, body = {}, path.read_text(encoding="utf-8")
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


def build_dataset(out_dir: Path = OUT_DIR, fmt: str = "parquet") -> Path:
    samples = gather_samples()
    out_dir.mkdir(parents=True, exist_ok=True)
    records = [s.model_dump() for s in samples]
    if fmt == "parquet":
        try:
            import pyarrow as pa
            import pyarrow.parquet as pq
        except ModuleNotFoundError as exc:  # pragma: no cover - runtime dep
            raise SystemExit("pyarrow required for parquet output") from exc
        out_file = out_dir / "attacks.parquet"
        table = pa.Table.from_pylist(records)
        pq.write_table(table, out_file)
        row_count = table.num_rows
    else:
        import csv

        out_file = out_dir / "attacks.csv"
        with out_file.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=records[0].keys())
            writer.writeheader()
            writer.writerows(records)
        row_count = len(records)
    print(f"Wrote {out_file} ({row_count} rows)")
    return out_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=OUT_DIR,
        help="directory to write output files",
    )
    parser.add_argument(
        "--format",
        choices=["parquet", "csv"],
        default="parquet",
        help="output format",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="validate dataset without writing output",
    )
    args = parser.parse_args()
    if args.check_only:
        samples = gather_samples()
        print(f"Validated {len(samples)} samples")
    else:
        build_dataset(out_dir=args.out_dir, fmt=args.format)

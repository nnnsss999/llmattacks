#!/usr/bin/env python3
"""Build the attacks dataset from Markdown files.

This script walks the ``attacks/`` folder, extracts the Markdown body and
front-matter metadata, validates each record with :class:`datasets.schema.AttackSample`
and writes the resulting table to disk.  The default output format is Parquet,
but CSV is also supported.

Use ``--check-only`` to validate the dataset without writing any files.  The
command exits with a non-zero status if any record fails schema validation.
"""

from __future__ import annotations

import uuid
import unicodedata
from pathlib import Path

import yaml
import pyarrow as pa
import pyarrow.parquet as pq
import argparse

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from datasets.schema import AttackSample

ROOT = Path(__file__).resolve().parents[1]
ATTACKS_DIR = ROOT / "attacks"
OUT_DIR = ROOT / "datasets" / "v1"

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


def write_dataset(samples: list[AttackSample], out_dir: Path, fmt: str) -> None:
    """Write samples to ``out_dir`` in the given ``fmt``."""
    out_dir.mkdir(parents=True, exist_ok=True)
    table = pa.Table.from_pylist([s.model_dump() for s in samples])
    if fmt == "parquet":
        out_file = out_dir / "attacks.parquet"
        pq.write_table(table, out_file)
    else:
        out_file = out_dir / "attacks.csv"
        table.to_pandas().to_csv(out_file, index=False)
    print(f"Wrote {out_file} ({table.num_rows} rows)")


def build_dataset(
    out_dir: Path = OUT_DIR, fmt: str = "parquet", check_only: bool = False
) -> None:
    samples = gather_samples()
    if check_only:
        # Simply validate by constructing the table; errors will raise
        pa.Table.from_pylist([s.model_dump() for s in samples])
        print(f"Validated {len(samples)} samples")
        return
    write_dataset(samples, out_dir, fmt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=OUT_DIR,
        help="Directory to write the dataset",
    )
    parser.add_argument(
        "--format",
        choices=["parquet", "csv"],
        default="parquet",
        help="Output file format",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Validate dataset without writing files",
    )
    args = parser.parse_args()
    build_dataset(out_dir=args.out_dir, fmt=args.format, check_only=args.check_only)

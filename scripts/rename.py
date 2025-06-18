#!/usr/bin/env python3
"""Rename Markdown files under a directory to kebab-case.

Usage: python scripts/rename.py [directory]
"""
import sys
import re
from pathlib import Path

def kebab_case(stem: str) -> str:
    stem = stem.lower()
    # replace non-alphanumeric with hyphen
    stem = re.sub(r"[^a-z0-9]+", "-", stem)
    stem = re.sub(r"-+", "-", stem)
    return stem.strip("-")

def rename_files(root: Path) -> None:
    for path in root.rglob("*.md"):
        new_name = kebab_case(path.stem) + path.suffix
        if path.name != new_name:
            target = path.with_name(new_name)
            if target.exists():
                print(f"Skipping {path} -> {target} (exists)")
                continue
            print(f"Renaming {path} -> {target}")
            path.rename(target)

if __name__ == "__main__":
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("docs")
    rename_files(directory)

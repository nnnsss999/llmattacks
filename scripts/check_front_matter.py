#!/usr/bin/env python3
"""Validate YAML front matter in markdown files."""
import sys
from pathlib import Path
import yaml

REQUIRED = {"title", "category", "source_url", "date_collected", "license"}

def validate(path: Path) -> bool:
    text = path.read_text(encoding="utf-8").splitlines()
    if len(text) < 3 or text[0].strip() != "---":
        print(f"{path}: missing front matter")
        return False
    try:
        end = text[1:].index("---") + 1
    except ValueError:
        print(f"{path}: malformed front matter")
        return False
    data = yaml.safe_load("\n".join(text[1:end])) or {}
    missing = REQUIRED - data.keys()
    if missing:
        print(f"{path}: missing fields {', '.join(sorted(missing))}")
        return False
    return True

def main(paths):
    ok = True
    for p in paths:
        if not validate(Path(p)):
            ok = False
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))


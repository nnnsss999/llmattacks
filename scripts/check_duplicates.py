#!/usr/bin/env python3
"""Detect duplicate markdown files via SHA-256 hashes."""
from pathlib import Path
import hashlib
import sys

def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    docs = list(Path('docs').rglob('*.md'))
    seen = {}
    dupes = {}
    for p in docs:
        h = file_hash(p)
        if h in seen:
            dupes.setdefault(seen[h], []).append(p)
        else:
            seen[h] = p
    if dupes:
        print('Duplicate files detected:')
        for orig, others in dupes.items():
            for o in others:
                print(f'{o} is duplicate of {orig}')
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())


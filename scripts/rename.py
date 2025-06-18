#!/usr/bin/env python3
import os
import re
import sys


def kebab_case(name: str) -> str:
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '-', name)
    name = re.sub(r'-+', '-', name)
    return name.strip('-')


def rename_file(path: str) -> None:
    directory, filename = os.path.split(path)
    stem, ext = os.path.splitext(filename)
    new_name = kebab_case(stem) + ext.lower()
    if new_name == filename:
        return
    new_path = os.path.join(directory, new_name)
    if os.path.exists(new_path):
        print(f"skip {path} -> {new_path} exists")
        return
    os.rename(path, new_path)
    print(f"rename {path} -> {new_path}")


def walk(base: str) -> None:
    for root, dirs, files in os.walk(base):
        for f in files:
            rename_file(os.path.join(root, f))


if __name__ == "__main__":
    targets = sys.argv[1:] or ["docs"]
    for target in targets:
        walk(target)

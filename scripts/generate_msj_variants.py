#!/usr/bin/env python3
"""Generate many-shot jailbreaking prompt variants.

This utility reads the base prompt from
`attacks/jailbreaking/many_shot/001_base.md` and writes plain text
variants with different shot counts (32, 64, 128) into the same folder.
The base file should contain a single Q/A pair or prompt segment that
can be duplicated verbatim to produce a longer transcript.
"""
from pathlib import Path
import argparse

DEFAULT_SHOTS = [32, 64, 128]
BASE_FILE = Path(__file__).resolve().parents[1] / "attacks" / "jailbreaking" / "many_shot" / "001_base.md"


def load_prompt(path: Path) -> str:
    """Return file contents minus YAML front matter."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        try:
            end = lines[1:].index("---") + 1
            lines = lines[end + 1 :]
        except ValueError:
            pass
    return "\n".join(lines).strip()


def generate_variants(base: Path, shots: list[int]) -> None:
    prompt = load_prompt(base)
    for n in shots:
        out = base.with_name(f"{base.stem}_{n}shot.txt")
        out.write_text((prompt + "\n") * n, encoding="utf-8")
        print(f"Wrote {out}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate many-shot jailbreak variants")
    parser.add_argument("--base", type=Path, default=BASE_FILE, help="Base prompt path")
    parser.add_argument("--shots", type=int, nargs="*", default=DEFAULT_SHOTS, help="Shot counts to generate")
    args = parser.parse_args()

    generate_variants(args.base, args.shots)


if __name__ == "__main__":
    main()

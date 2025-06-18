#!/usr/bin/env python3
"""Generate a CycloneDX SBOM listing Markdown sources."""
from pathlib import Path
import json
import yaml

DOCS_DIR = Path(__file__).resolve().parents[1] / 'docs'
SBOM_FILE = Path(__file__).resolve().parents[1] / 'sbom.json'


def parse_front_matter(path: Path) -> dict:
    lines = path.read_text(encoding='utf-8').splitlines()
    if len(lines) < 3 or lines[0].strip() != '---':
        return {}
    try:
        end = lines[1:].index('---') + 1
    except ValueError:
        return {}
    try:
        data = yaml.safe_load('\n'.join(lines[1:end]))
        return data or {}
    except yaml.YAMLError:
        return {}


def generate_sbom() -> None:
    components = []
    for path in sorted(DOCS_DIR.rglob('*.md')):
        fm = parse_front_matter(path)
        component = {
            'type': 'file',
            'name': str(path.relative_to(DOCS_DIR)),
            'bom-ref': str(path.relative_to(DOCS_DIR)),
        }
        if fm:
            component['properties'] = [
                {'name': k, 'value': str(v)} for k, v in fm.items()
            ]
        components.append(component)

    sbom = {
        'bomFormat': 'CycloneDX',
        'specVersion': '1.5',
        'version': 1,
        'metadata': {
            'component': {'type': 'application', 'name': 'llmattacks'}
        },
        'components': components,
    }
    SBOM_FILE.write_text(json.dumps(sbom, indent=2), encoding='utf-8')
    print(f'Wrote {SBOM_FILE}')


if __name__ == '__main__':
    generate_sbom()

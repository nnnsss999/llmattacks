import json
from pathlib import Path
import yaml

DOCS_DIR = Path(__file__).resolve().parents[1] / 'docs'
INDEX_FILE = Path(__file__).resolve().parents[1] / 'index.json'


def parse_front_matter(path: Path):
    """Parse YAML front matter from a file. Returns a dict or None."""
    lines = path.read_text(encoding='utf-8').splitlines()
    if len(lines) < 3 or lines[0].strip() != '---':
        return None
    try:
        closing_idx = lines[1:].index('---') + 1
    except ValueError:
        return None
    front = '\n'.join(lines[1:closing_idx])
    try:
        data = yaml.safe_load(front) or {}
        # Coerce any non-serialisable types (e.g. dates) to strings
        for key, value in list(data.items()):
            if not isinstance(value, (str, int, float, bool, type(None))):
                data[key] = str(value)
        return data
    except yaml.YAMLError:
        return None


def build_index():
    index = {}
    for path in DOCS_DIR.rglob('*.md'):
        fm = parse_front_matter(path)
        if not fm:
            continue
        entry = {
            'title': fm.get('title', ''),
            'path': str(path.relative_to(DOCS_DIR)),
            'category': fm.get('category', ''),
            'sub_category': fm.get('sub_category', ''),
            'date_collected': fm.get('date_collected', ''),
        }
        cat = fm.get('category', 'Uncategorized')
        index.setdefault(cat, []).append(entry)
    INDEX_FILE.write_text(json.dumps(index, indent=2), encoding='utf-8')
    print(f'Wrote {INDEX_FILE}')


if __name__ == '__main__':
    build_index()

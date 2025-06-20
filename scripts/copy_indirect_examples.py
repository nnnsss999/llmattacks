import re
import yaml
from pathlib import Path

SRC_LIST = Path('/tmp/first50.txt')
DEST_DIR = Path('attacks/prompt/indirect')

DEST_DIR.mkdir(parents=True, exist_ok=True)

with SRC_LIST.open() as f:
    files = [line.strip() for line in f if line.strip()]

for idx, src_path in enumerate(files, start=1):
    src = Path(src_path)
    text = src.read_text(encoding='utf-8', errors='ignore')
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            header = text[3:end].strip()
            rest = text[end+4:]
            try:
                data = yaml.safe_load(header) or {}
            except Exception:
                data = {}
            url = data.get('source_url') or data.get('title', '')
        else:
            rest = text
            url = ''
    else:
        rest = text
        url = ''
    dest_path = DEST_DIR / f"{idx:03d}.md"
    with dest_path.open('w', encoding='utf-8') as out:
        out.write('---\n')
        out.write('attack_type: indirect_pi\n')
        if url:
            out.write(f'source_url: {url}\n')
        out.write('---\n\n')
        out.write(rest.strip() + '\n')


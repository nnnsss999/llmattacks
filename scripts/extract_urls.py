import os
import re
import sys

pattern = re.compile(r'https?://[^\s"\'<>]+')
urls = set()
for root, dirs, files in os.walk('.', followlinks=True):
    # skip .git directory
    if '.git' in dirs:
        dirs.remove('.git')
    for name in files:
        path = os.path.join(root, name)
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception:
            continue
        for match in pattern.findall(content):
            url = match.rstrip('.,)\"\'<>]')
            urls.add(url)

for url in sorted(urls):
    sys.stdout.write(url + "\n")

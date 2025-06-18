import json
import subprocess
import sys
from pathlib import Path


def test_generate_sbom():
    result = subprocess.run([sys.executable, 'scripts/generate_sbom.py'], capture_output=True)
    assert result.returncode == 0
    sbom = Path('sbom.json')
    assert sbom.exists()
    data = json.loads(sbom.read_text())
    assert 'components' in data and isinstance(data['components'], list)

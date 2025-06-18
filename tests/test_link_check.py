import subprocess
import sys


def test_link_checker():
    result = subprocess.run([sys.executable, 'scripts/link_check.py'], capture_output=True)
    if result.returncode != 0:
        print(result.stdout.decode())
        print(result.stderr.decode())
    assert result.returncode == 0

import subprocess
import sys
import os


def test_link_checker():
    env = os.environ.copy()
    env["FAST_LINK_CHECK"] = "10"
    result = subprocess.run(
        [sys.executable, "scripts/link_check.py"], capture_output=True, env=env
    )
    if result.returncode != 0:
        print(result.stdout.decode())
        print(result.stderr.decode())
    assert result.returncode == 0

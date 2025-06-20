import sys
from pathlib import Path

# ensure local "defenses" package is imported
sys.modules.pop("defenses", None)
sys.modules.pop("defenses.input_filters", None)
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from defenses.input_filters.length_guard import abort_if_exceeds


def test_within_limit_returns_text():
    text = "token" * 100
    assert abort_if_exceeds(text, max_tokens=200) == text


def test_over_limit_returns_none():
    text = "token " * 10
    assert abort_if_exceeds(text, max_tokens=5) is None

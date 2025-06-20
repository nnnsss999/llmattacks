import sys
from pathlib import Path

# add path to secure_llmattacks_v3 package folders
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from defenses.input_filters.zero_width import strip_zero_width


def test_strip_basic():
    text = "\u200bhello\u200c"
    assert strip_zero_width(text) == "hello"


def test_strip_mixed():
    s = "a\u200bb\u200c\u200d\u2060\ufeffc"
    assert strip_zero_width(s) == "abc"

import sys
from pathlib import Path
from pydantic import ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from datasets.schema import AttackSample


def test_attack_sample_valid():
    sample = AttackSample(
        uuid="1234",
        text="hello",
        label=1,
        attack_type="direct_pi",
        source_path="attacks/prompt/direct/001_dan.md",
    )
    assert sample.label == 1
    schema = AttackSample.model_json_schema()
    assert schema["properties"]["uuid"]["type"] == "string"


def test_attack_sample_invalid():
    try:
        AttackSample(
            uuid="1234",
            text="hello",
            label="bad",
            attack_type="direct_pi",
            source_path="path",
        )
    except ValidationError:
        pass
    else:
        raise AssertionError("Validation should have failed")


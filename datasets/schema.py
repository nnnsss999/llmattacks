from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class AttackSample(BaseModel):
    """Single text sample with metadata for training/testing."""

    uuid: str
    text: str
    label: int
    attack_type: str
    source_path: str

    model_config = ConfigDict(extra="forbid")

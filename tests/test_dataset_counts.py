import sys
from pathlib import Path
import types

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

try:
    import pyarrow  # noqa: F401
except ModuleNotFoundError:  # pragma: no cover
    pa_mod = types.ModuleType("pyarrow")
    table_mod = types.SimpleNamespace(from_pylist=lambda data: data)
    setattr(pa_mod, "Table", table_mod)
    pq_mod = types.ModuleType("pyarrow.parquet")
    pq_mod.write_table = lambda *args, **kwargs: None
    sys.modules["pyarrow"] = pa_mod
    sys.modules["pyarrow.parquet"] = pq_mod

from scripts import build_dataset


def test_dataset_row_count_and_unique_uuids():
    md_files = list((ROOT / "attacks").rglob("*.md"))
    samples = build_dataset.gather_samples()
    assert len(samples) >= len(md_files)
    uuids = [s.uuid for s in samples]
    assert len(uuids) == len(set(uuids))

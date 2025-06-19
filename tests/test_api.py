import sys
from pathlib import Path
from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))
from api_server import app

client = TestClient(app)

def test_entries_endpoint():
    resp = client.get("/entries")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert data


def test_graphql_endpoint():
    query = "{ entries { title path } }"
    resp = client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    j = resp.json()
    assert "data" in j
    assert "entries" in j["data"]
    assert isinstance(j["data"]["entries"], list)

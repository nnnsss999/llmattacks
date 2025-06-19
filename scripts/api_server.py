from pathlib import Path
import json

from fastapi import FastAPI
import uvicorn
import strawberry
from strawberry.fastapi import GraphQLRouter

INDEX_FILE = Path(__file__).resolve().parents[1] / "index.json"
INDEX: dict = json.loads(INDEX_FILE.read_text())

app = FastAPI(title="LLM Attacks Catalog API")

@app.get("/entries")
def read_entries():
    """Return the entire catalog index."""
    return INDEX

@app.get("/entries/{category}")
def read_category(category: str):
    """Return entries for a single category."""
    return INDEX.get(category, [])

@strawberry.type
class Entry:
    title: str
    path: str
    category: str
    sub_category: str
    date_collected: str


def _all_entries() -> list[Entry]:
    entries: list[Entry] = []
    for items in INDEX.values():
        entries.extend([Entry(**item) for item in items])
    return entries


def _by_category(name: str) -> list[Entry]:
    return [Entry(**item) for item in INDEX.get(name, [])]


@strawberry.type
class Query:
    entries: list[Entry] = strawberry.field(resolver=_all_entries)
    category: list[Entry] = strawberry.field(resolver=_by_category)


schema = strawberry.Schema(query=Query)
app.include_router(GraphQLRouter(schema), prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

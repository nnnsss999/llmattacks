import os
import sys
import json
import requests
from difflib import SequenceMatcher
from pathlib import Path

API_URL = "https://api-inference.huggingface.co/models/{}"
DEFAULT_MODEL = "gpt2"
TOKEN = os.getenv("HF_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}


def query_model(
    prefix: str, model: str = DEFAULT_MODEL, max_new_tokens: int = 50
) -> str:
    payload = {
        "inputs": prefix,
        "parameters": {"do_sample": False, "max_new_tokens": max_new_tokens},
        "options": {"wait_for_model": True},
    }
    resp = requests.post(
        API_URL.format(model), headers=HEADERS, json=payload, timeout=30
    )
    resp.raise_for_status()
    data = resp.json()
    if isinstance(data, list) and data and "generated_text" in data[0]:
        return data[0]["generated_text"]
    raise ValueError(f"Unexpected response: {data}")


def infer_membership(
    text: str, model: str = DEFAULT_MODEL, prefix_words: int = 20
) -> float:
    words = text.strip().split()
    if len(words) <= prefix_words:
        prefix = " ".join(words)
        remainder = ""
    else:
        prefix = " ".join(words[:prefix_words])
        remainder = " ".join(words[prefix_words:])
    generated = query_model(
        prefix, model=model, max_new_tokens=len(remainder.split()) + 5
    )
    gen_cont = generated[len(prefix) :].strip()
    ratio = SequenceMatcher(None, remainder, gen_cont).ratio()
    return ratio


def main(path: str, model: str = DEFAULT_MODEL) -> None:
    text = Path(path).read_text(encoding="utf-8")
    score = infer_membership(text, model=model)
    print(json.dumps({"path": path, "model": model, "similarity": score}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python membership_inference.py <text-file> [model]", file=sys.stderr
        )
        sys.exit(1)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else DEFAULT_MODEL)

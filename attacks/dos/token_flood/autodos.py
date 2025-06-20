#!/usr/bin/env python3
"""Send the token-flood prompt repeatedly to an LLM API."""

import argparse
import os
from pathlib import Path
import requests

DEFAULT_URL = "https://api.openai.com/v1/chat/completions"
PROMPT_FILE = Path(__file__).with_name("001_token_flood.md")


def load_prompt() -> str:
    text = PROMPT_FILE.read_text(encoding="utf-8").splitlines()
    if text[0].strip() == "---":
        end = text[1:].index("---") + 1
        text = text[end + 1 :]
    return "\n".join(text).strip()


def send_prompt(api_url: str, api_key: str, prompt: str) -> int:
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 4096,
    }
    r = requests.post(api_url, headers=headers, json=payload, timeout=10)
    return r.status_code


def main() -> None:
    parser = argparse.ArgumentParser(description="Run automated token-flood DoS")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--key", default=os.getenv("OPENAI_API_KEY", ""))
    parser.add_argument("--count", type=int, default=1, help="Number of requests")
    args = parser.parse_args()

    prompt = load_prompt()
    for i in range(args.count):
        code = send_prompt(args.url, args.key, prompt)
        print(f"{i+1}/{args.count}: status {code}")


if __name__ == "__main__":
    main()

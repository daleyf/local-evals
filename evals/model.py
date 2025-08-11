"""Lightweight model runners for local LLMs."""
from __future__ import annotations

import requests
from typing import Callable


def get_model(spec: str) -> Callable[[str], str]:
    """Return a function that takes a prompt and returns a model response.

    Supported specs:
      - ``echo`` – returns the prompt unchanged. Useful for tests.
      - ``ollama:MODEL`` – uses the local Ollama HTTP API.
    """
    if spec == "echo":
        return lambda prompt: prompt

    backend, _, name = spec.partition(":")
    if backend == "ollama":
        def run(prompt: str) -> str:
            resp = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": name, "prompt": prompt},
                timeout=60,
            )
            resp.raise_for_status()
            data = resp.json()
            return data.get("response", "").strip()
        return run
    raise ValueError(f"Unknown model spec: {spec}")

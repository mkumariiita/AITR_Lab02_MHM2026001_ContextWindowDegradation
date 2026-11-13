from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

_PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_env() -> None:
    """Load project-root .env if present (no error if missing)."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    load_dotenv(_PROJECT_ROOT / ".env", override=False)


@dataclass
class LLMResponse:
    text: str
    backend: str
    model: str
    raw: dict[str, Any]


class DummyLLM:
    """Deterministic stand-in for pipeline tests. Not a scientific baseline result."""

    def __init__(self, model: str = "dummy-v0") -> None:
        self.model = model
        self.backend = "dummy"

    def generate(self, prompt: str, temperature: float = 0.0, max_tokens: int = 512) -> LLMResponse:
        del temperature, max_tokens
        # Cite whatever gold-looking ids appear in the prompt; bias: skip middle-ish if many ids.
        # Only consider passage headers from the Passages section (ignore instruction examples).
        body = prompt.split("Passages:\n", 1)[-1]
        body = body.split("\n\nQuestion:", 1)[0]
        ids = re.findall(r"\[(P\d+)\]", body)
        seen: list[str] = []
        for i in ids:
            if i not in seen:
                seen.append(i)
        # Cite the first two passage ids in context order — exposes position sensitivity for dry-runs.
        cite = seen[:2] if seen else []
        cite_str = " ".join(f"[{c}]" for c in cite)
        text = (
            f"Based on the passages, a partial synthesis follows. {cite_str} "
            "low-prior-knowledge students may benefit; completeness is not guaranteed "
            "and does not guarantee full evidence use."
        )
        return LLMResponse(text=text, backend=self.backend, model=self.model, raw={"note": "dummy"})


class OpenAICompatLLM:
    def __init__(self, model: str, base_url: str, api_key: str) -> None:
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.backend = "openai_compat"

    def generate(self, prompt: str, temperature: float = 0.0, max_tokens: int = 512) -> LLMResponse:
        import time

        import requests

        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": self.model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "messages": [
                {"role": "user", "content": prompt},
            ],
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        last_err: Exception | None = None
        for attempt in range(1, 7):
            resp = requests.post(url, json=payload, headers=headers, timeout=120)
            if resp.status_code == 429:
                # Free-tier rate limit: back off, preferring Retry-After when present.
                retry_after = resp.headers.get("Retry-After")
                wait_s = float(retry_after) if retry_after and retry_after.isdigit() else min(2 ** attempt, 40)
                print(f"rate_limited attempt={attempt} sleep={wait_s}s")
                time.sleep(wait_s)
                last_err = requests.HTTPError(f"429 Too Many Requests after {attempt} tries", response=resp)
                continue
            resp.raise_for_status()
            data = resp.json()
            msg = data["choices"][0]["message"]
            text = (msg.get("content") or "").strip()
            # Some Groq "oss" models spend budget on message.reasoning first; tiny max_tokens
            # can yield empty content. Do not silently score empty answers.
            if not text:
                reason = (msg.get("reasoning") or "")[:180]
                finish = data["choices"][0].get("finish_reason")
                raise RuntimeError(
                    f"Empty model content (finish_reason={finish}). "
                    f"Increase decoding.max_tokens (got reasoning preview: {reason!r})."
                )
            return LLMResponse(text=text, backend=self.backend, model=self.model, raw=data)
        assert last_err is not None
        raise last_err


def build_llm(backend: str, model: str, base_url: str | None = None) -> DummyLLM | OpenAICompatLLM:
    load_env()
    if backend == "dummy":
        return DummyLLM(model=model or "dummy-v0")
    if backend == "openai_compat":
        key = os.environ.get("LLM_API_KEY", "").strip()
        url = (base_url or os.environ.get("LLM_BASE_URL", "")).strip()
        name = (model if model and model != "unset" else "") or os.environ.get("LLM_MODEL", "")
        name = name.strip()
        if not key or key.startswith("paste_") or key.endswith("_here"):
            raise RuntimeError(
                "Set a real LLM_API_KEY in .env (see .env.example and configs/ENV_SETUP.md)."
            )
        if not url or not name:
            raise RuntimeError(
                "openai_compat requires LLM_API_KEY, LLM_BASE_URL, and LLM_MODEL in .env "
                "(or model/base_url in configs/experiment.yaml)."
            )
        return OpenAICompatLLM(model=name, base_url=url, api_key=key)
    raise ValueError(f"unknown backend: {backend}")
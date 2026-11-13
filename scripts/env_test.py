#!/usr/bin/env python3
"""Prompt 08 — environment sanity test. Share this console output before trusting later runs."""

from __future__ import annotations

import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def main() -> int:
    print("=== env_test: position_citation ===")
    print(f"python: {sys.version.split()[0]}")
    print(f"platform: {platform.platform()}")
    print(f"machine: {platform.machine()}")
    print(f"root: {ROOT}")

    errors: list[str] = []

    try:
        import yaml  # noqa: F401
        import requests  # noqa: F401

        print("imports: PyYAML OK, requests OK")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"import failure: {exc}")

    try:
        from position_citation.packets import load_all_packets
        from position_citation.assemble import build_prompt, assemble_ordered_passages
        from position_citation.llm import build_llm
        from position_citation.score import score_response

        packets = load_all_packets(ROOT / "data" / "packets")
        print(f"packets_loaded: {len(packets)}")
        pkt = packets[0]
        for pos in ("begin", "middle", "end"):
            ordered = assemble_ordered_passages(pkt, pos)
            ids = [p["id"] for p in ordered]
            print(f"order[{pos}]: {' '.join(ids)}")
        prompt = build_prompt(pkt, "middle")
        llm = build_llm("dummy", "dummy-v0")
        resp = llm.generate(prompt)
        scores = score_response(pkt, resp.text)
        print(f"dummy_response_chars: {len(resp.text)}")
        print(f"dummy_scores: {scores}")
        print("EXPECTED: packets_loaded >= 1; three position orders; dummy_scores dict printed.")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"pipeline failure: {exc}")

    cfg = ROOT / "configs" / "experiment.yaml"
    if not cfg.exists():
        errors.append("missing configs/experiment.yaml")
    else:
        print(f"config: {cfg.name} present")

    if errors:
        print("STATUS: FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("STATUS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
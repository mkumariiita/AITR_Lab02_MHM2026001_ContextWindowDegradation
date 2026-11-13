#!/usr/bin/env python3
"""Run baseline: direct cite-required prompting across begin/middle/end positions."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from position_citation.assemble import build_prompt  # noqa: E402
from position_citation.llm import build_llm, load_env  # noqa: E402
from position_citation.packets import load_all_packets  # noqa: E402
from position_citation.score import score_response  # noqa: E402


def load_config(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def row_from_saved(resp_path: Path, packet: dict, position: str) -> dict:
    data = json.loads(resp_path.read_text(encoding="utf-8"))
    scores = score_response(packet, data["response"])
    data["scores"] = scores
    resp_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return {
        "item_id": packet["item_id"],
        "position": position,
        "backend": data.get("backend"),
        "model": data.get("model"),
        "answer_correctness": scores["answer_correctness"],
        "evidence_coverage": scores["evidence_coverage"],
        "citation_support": scores["citation_support"],
        "citations": "|".join(scores["citations"]),
        "missed_gold": "|".join(scores["missed_gold"]),
        "distractor_cites": "|".join(scores["distractor_cites"]),
        "response_file": str(resp_path.relative_to(ROOT)),
    }


def main() -> int:
    load_env()
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=ROOT / "configs" / "experiment.yaml")
    parser.add_argument("--backend", choices=["dummy", "openai_compat"], default=None)
    parser.add_argument("--limit", type=int, default=None, help="optional cap on items")
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument(
        "--resume",
        action="store_true",
        help="skip item/position pairs that already have raw JSON in --out-dir",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=1.5,
        help="seconds to sleep between API calls (free-tier friendly)",
    )
    args = parser.parse_args()

    cfg = load_config(args.config)

    backend = (
        args.backend
        or os.environ.get("LLM_BACKEND")
        or cfg.get("model", {}).get("backend", "dummy")
    )
    model = cfg.get("model", {}).get("name", "unset")
    if not model or model == "unset":
        model = os.environ.get("LLM_MODEL", "unset")
    base_url = cfg.get("model", {}).get("base_url")
    if base_url == "unset" or not base_url:
        base_url = os.environ.get("LLM_BASE_URL") or None

    positions = cfg.get("positions", ["begin", "middle", "end"])
    decoding = cfg.get("decoding", {})
    prompt_version = cfg.get("prompt_version", "cite_v1")

    packets = load_all_packets(ROOT / "data" / "packets")
    if args.limit is not None:
        packets = packets[: args.limit]

    llm = build_llm(backend, model if model != "unset" else "dummy-v0", base_url)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = args.out_dir or (ROOT / "results" / "raw" / f"run_{stamp}")
    if not out_dir.is_absolute():
        out_dir = ROOT / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    table_path = ROOT / "results" / "tables" / f"results_{out_dir.name}.csv"
    table_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "item_id",
        "position",
        "backend",
        "model",
        "answer_correctness",
        "evidence_coverage",
        "citation_support",
        "citations",
        "missed_gold",
        "distractor_cites",
        "response_file",
    ]
    rows: list[dict] = []

    for packet in packets:
        for position in positions:
            resp_name = f"{packet['item_id']}_{position}.json"
            resp_path = out_dir / resp_name
            if args.resume and resp_path.exists():
                row = row_from_saved(resp_path, packet, position)
                rows.append(row)
                print(
                    f"{packet['item_id']} {position}: "
                    f"cov={row['evidence_coverage']} cite={row['citation_support']} "
                    f"corr={row['answer_correctness']} [resume]"
                )
                continue

            prompt = build_prompt(packet, position, prompt_version=prompt_version)
            resp = llm.generate(
                prompt,
                temperature=float(decoding.get("temperature", 0.0)),
                max_tokens=int(decoding.get("max_tokens", 512)),
            )
            scores = score_response(packet, resp.text)
            resp_path.write_text(
                json.dumps(
                    {
                        "item_id": packet["item_id"],
                        "position": position,
                        "prompt": prompt,
                        "response": resp.text,
                        "backend": resp.backend,
                        "model": resp.model,
                        "scores": scores,
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )
            rows.append(
                {
                    "item_id": packet["item_id"],
                    "position": position,
                    "backend": resp.backend,
                    "model": resp.model,
                    "answer_correctness": scores["answer_correctness"],
                    "evidence_coverage": scores["evidence_coverage"],
                    "citation_support": scores["citation_support"],
                    "citations": "|".join(scores["citations"]),
                    "missed_gold": "|".join(scores["missed_gold"]),
                    "distractor_cites": "|".join(scores["distractor_cites"]),
                    "response_file": str(resp_path.relative_to(ROOT)),
                }
            )
            print(
                f"{packet['item_id']} {position}: "
                f"cov={scores['evidence_coverage']} cite={scores['citation_support']} "
                f"corr={scores['answer_correctness']}"
            )
            if backend != "dummy" and args.sleep > 0:
                time.sleep(args.sleep)

    with table_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    meta = {
        "stamp": stamp,
        "backend": backend,
        "model": getattr(llm, "model", model),
        "n_items": len(packets),
        "positions": positions,
        "table": str(table_path.relative_to(ROOT)),
        "out_dir": str(out_dir.relative_to(ROOT)),
        "note": "dummy backend outputs are NOT scientific results",
    }
    (out_dir / "run_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Wrote {table_path}")
    print(f"Wrote raw responses under {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""Re-score saved raw responses after scorer updates (no new API calls)."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from position_citation.packets import load_packet  # noqa: E402
from position_citation.score import score_response  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("raw_dir", type=Path, help="results/raw/run_... directory")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    raw_dir = args.raw_dir
    if not raw_dir.is_absolute():
        raw_dir = ROOT / raw_dir
    files = sorted(raw_dir.glob("item_*.json"))
    if not files:
        raise SystemExit(f"No item_*.json in {raw_dir}")

    packets = {
        p.stem: load_packet(p)
        for p in (ROOT / "data" / "packets").glob("item_*.json")
    }

    rows = []
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        item_id = data["item_id"]
        packet = packets[item_id]
        scores = score_response(packet, data["response"])
        data["scores"] = scores
        data["scorer_version"] = "cite_brackets_v2"
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        rows.append(
            {
                "item_id": item_id,
                "position": data["position"],
                "backend": data.get("backend"),
                "model": data.get("model"),
                "answer_correctness": scores["answer_correctness"],
                "evidence_coverage": scores["evidence_coverage"],
                "citation_support": scores["citation_support"],
                "citations": "|".join(scores["citations"]),
                "missed_gold": "|".join(scores["missed_gold"]),
                "distractor_cites": "|".join(scores["distractor_cites"]),
                "response_file": str(path.relative_to(ROOT)),
            }
        )
        print(
            f"{item_id} {data['position']}: "
            f"cov={scores['evidence_coverage']} cite={scores['citation_support']} "
            f"corr={scores['answer_correctness']} cites={scores['citations']}"
        )

    out = args.out or (ROOT / "results" / "tables" / f"results_rescored_{raw_dir.name}.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
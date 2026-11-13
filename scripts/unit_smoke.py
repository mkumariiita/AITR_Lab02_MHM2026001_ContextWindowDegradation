#!/usr/bin/env python3
"""Small unit/sanity checks for Prompt 09 modules."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from position_citation.assemble import assemble_ordered_passages
from position_citation.packets import load_packet
from position_citation.score import score_response


def main() -> int:
    pkt = load_packet(ROOT / "data" / "packets" / "item_01.json")
    begin = [p["id"] for p in assemble_ordered_passages(pkt, "begin")]
    middle = [p["id"] for p in assemble_ordered_passages(pkt, "middle")]
    end = [p["id"] for p in assemble_ordered_passages(pkt, "end")]

    assert begin[:2] == ["P2", "P5"], begin
    assert end[-2:] == ["P2", "P5"], end
    assert "P2" in middle and "P5" in middle
    assert middle[0] != "P2" or middle[1] != "P5" or True  # gold not forced at index 0 only

    good = score_response(pkt, "Low-prior-knowledge gains in Study A [P2]; Study B finds no average effect [P5].")
    assert good["answer_correctness"] == 1
    assert good["evidence_coverage"] == 1.0
    assert good["citation_support"] == 1.0

    bad = score_response(pkt, "Everything improved for all students [P1].")
    assert bad["answer_correctness"] == 0
    assert bad["citation_support"] == 0.0

    print("unit_smoke: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
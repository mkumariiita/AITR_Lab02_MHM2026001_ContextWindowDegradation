from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = (
    "item_id",
    "question",
    "passages",
    "gold_evidence_ids",
    "gold_answer_key",
)


def load_packet(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = [f for f in REQUIRED_FIELDS if f not in data]
    if missing:
        raise ValueError(f"{path.name}: missing fields {missing}")
    ids = [p["id"] for p in data["passages"]]
    if len(ids) != len(set(ids)):
        raise ValueError(f"{path.name}: duplicate passage ids")
    for gid in data["gold_evidence_ids"]:
        if gid not in ids:
            raise ValueError(f"{path.name}: gold id {gid} not in passages")
    return data


def load_all_packets(directory: Path) -> list[dict[str, Any]]:
    paths = sorted(directory.glob("item_*.json"))
    if not paths:
        raise FileNotFoundError(f"No item_*.json in {directory}")
    return [load_packet(p) for p in paths]
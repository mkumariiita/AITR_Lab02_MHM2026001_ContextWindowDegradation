from __future__ import annotations

import re
from typing import Any


# Models often emit [P2], 【P2】, (P2), or bold/bare ids like **P2** / "- P2 notes".
_CITE_BRACKET_RE = re.compile(r"[\[【(]\s*(P\d+)\s*[\]】)]", re.IGNORECASE)
_CITE_BOLD_RE = re.compile(r"\*\*\s*(P\d+)\s*\*\*", re.IGNORECASE)
_CITE_BARE_RE = re.compile(
    r"(?:(?<=^)|(?<=[\s\-•*]))(P\d+)(?=[\s:,\.\)])",
    re.IGNORECASE | re.MULTILINE,
)


def extract_citations(text: str) -> list[str]:
    seen: list[str] = []
    for cre in (_CITE_BRACKET_RE, _CITE_BOLD_RE, _CITE_BARE_RE):
        for m in cre.findall(text):
            pid = m.upper()
            if not pid.startswith("P"):
                pid = "P" + re.sub(r"\D", "", pid)
            if pid not in seen:
                seen.append(pid)
    return seen


def _normalize_answer_text(s: str) -> str:
    s = s.lower()
    s = s.replace("‑", "-").replace("–", "-").replace("—", "-")
    s = re.sub(r"[*_`]+", "", s)  # strip light markdown so **not** still matches
    s = re.sub(r"[\s\-]+", " ", s)
    return s.strip()


def score_response(packet: dict[str, Any], response_text: str) -> dict[str, Any]:
    """Heuristic scorer for MVP. Human must spot-check before paper claims."""
    cites = extract_citations(response_text)
    gold = list(packet.get("gold_evidence_ids", []))
    key = _normalize_answer_text(str(packet.get("gold_answer_key", "")))
    text_l = _normalize_answer_text(response_text)

    correctness = 1 if key and key in text_l else 0

    if gold:
        covered = sum(1 for g in gold if g in cites)
        coverage = covered / len(gold)
    else:
        coverage = 0.0

    if cites:
        supported = sum(1 for c in cites if c in gold)
        citation_support = supported / len(cites)
    else:
        citation_support = 0.0

    missed_gold = [g for g in gold if g not in cites]
    distractor_cites = [
        c
        for c in cites
        if c not in gold
        and c
        not in set(packet.get("contradict_ids") or [])
    ]

    return {
        "answer_correctness": correctness,
        "evidence_coverage": round(coverage, 4),
        "citation_support": round(citation_support, 4),
        "citations": cites,
        "missed_gold": missed_gold,
        "distractor_cites": distractor_cites,
    }
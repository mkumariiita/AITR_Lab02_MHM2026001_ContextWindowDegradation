from __future__ import annotations

from typing import Any


def _split_roles(passages: list[dict[str, Any]]) -> tuple[list[dict], list[dict]]:
    gold = [p for p in passages if p.get("role") in {"gold_support", "gold_contradict"}]
    distractors = [p for p in passages if p.get("role") == "distractor"]
    if not gold:
        raise ValueError("packet has no gold passages")
    if not distractors:
        raise ValueError("packet needs distractors to create middle/end positions")
    return gold, distractors


def assemble_ordered_passages(packet: dict[str, Any], position: str) -> list[dict[str, Any]]:
    """Place all gold passages as a contiguous block at begin, middle, or end.

    Distractor order is otherwise preserved. Gold internal order is preserved.
    """
    if position not in {"begin", "middle", "end"}:
        raise ValueError(f"unknown position: {position}")

    gold, distractors = _split_roles(packet["passages"])
    n = len(distractors)

    if position == "begin":
        return gold + distractors
    if position == "end":
        return distractors + gold

    # middle: split distractors as evenly as possible around gold block
    cut = n // 2
    return distractors[:cut] + gold + distractors[cut:]


def format_context(ordered: list[dict[str, Any]]) -> str:
    blocks = []
    for p in ordered:
        blocks.append(f"[{p['id']}] {p['text']}")
    return "\n\n".join(blocks)


def build_prompt(packet: dict[str, Any], position: str, prompt_version: str = "cite_v1") -> str:
    if prompt_version != "cite_v1":
        raise ValueError(f"unsupported prompt_version: {prompt_version}")

    ordered = assemble_ordered_passages(packet, position)
    context = format_context(ordered)
    question = packet["question"]
    return (
        "You are helping with research synthesis.\n"
        "Use ONLY the passages below. For every factual claim, cite passage ids "
        "in square brackets using the id shown before each passage (for example [P1]). "
        "If sources disagree, say so and cite both.\n"
        "If evidence is insufficient, say so explicitly.\n\n"
        f"Passages:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Answer:"
    )
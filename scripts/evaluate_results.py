#!/usr/bin/env python3
"""Prompt 13 — Evaluate real experimental outputs only. No invented metrics."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit(f"No rows in {path}")
    required = {
        "item_id",
        "position",
        "answer_correctness",
        "evidence_coverage",
        "citation_support",
        "response_file",
    }
    missing = required - set(rows[0].keys())
    if missing:
        raise SystemExit(f"CSV missing columns: {sorted(missing)}")
    for i, r in enumerate(rows):
        for key in ("item_id", "position", "response_file"):
            if not (r.get(key) or "").strip():
                raise SystemExit(f"Row {i}: empty {key}")
        for key in ("answer_correctness", "evidence_coverage", "citation_support"):
            try:
                float(r[key])
            except ValueError as exc:
                raise SystemExit(f"Row {i}: bad {key}={r[key]!r}") from exc
        if r["position"] not in {"begin", "middle", "end"}:
            raise SystemExit(f"Row {i}: unexpected position {r['position']!r}")
    return rows


def means_by_position(rows: list[dict]) -> dict[str, dict[str, float]]:
    buckets: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        buckets[r["position"]].append(r)
    out: dict[str, dict[str, float]] = {}
    for pos, rs in buckets.items():
        n = len(rs)
        out[pos] = {
            "n": float(n),
            "mean_coverage": sum(float(r["evidence_coverage"]) for r in rs) / n,
            "mean_citation_support": sum(float(r["citation_support"]) for r in rs) / n,
            "mean_correctness": sum(float(r["answer_correctness"]) for r in rs) / n,
        }
    return out


def write_summary_csv(means: dict[str, dict[str, float]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "position",
                "n",
                "mean_coverage",
                "mean_citation_support",
                "mean_correctness",
            ],
        )
        w.writeheader()
        for pos in ("begin", "middle", "end"):
            if pos not in means:
                continue
            m = means[pos]
            w.writerow(
                {
                    "position": pos,
                    "n": int(m["n"]),
                    "mean_coverage": round(m["mean_coverage"], 4),
                    "mean_citation_support": round(m["mean_citation_support"], 4),
                    "mean_correctness": round(m["mean_correctness"], 4),
                }
            )


def failure_cases(rows: list[dict]) -> list[dict]:
    """Deep analysis inputs: coverage high but keyword correctness 0, etc."""
    cases = []
    for r in rows:
        cov = float(r["evidence_coverage"])
        cite = float(r["citation_support"])
        corr = float(r["answer_correctness"])
        tags = []
        if cov >= 1.0 and corr == 0:
            tags.append("coverage_ok_corr_fail")
        if cite >= 1.0 and corr == 0:
            tags.append("citation_ok_corr_fail")
        if cov == 0:
            tags.append("zero_coverage")
        if cite == 0 and cov > 0:
            tags.append("coverage_without_citation_support")
        if tags:
            cases.append({**r, "failure_tags": "|".join(tags)})
    return cases


def write_failure_csv(cases: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "item_id",
        "position",
        "answer_correctness",
        "evidence_coverage",
        "citation_support",
        "citations",
        "missed_gold",
        "failure_tags",
        "response_file",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for c in cases:
            w.writerow({k: c.get(k, "") for k in fields})


def plot_figures(means: dict[str, dict[str, float]], rows: list[dict], out_dir: Path) -> None:
    import matplotlib.pyplot as plt

    out_dir.mkdir(parents=True, exist_ok=True)
    positions = [p for p in ("begin", "middle", "end") if p in means]

    # Figure 1: mean metrics by position
    metrics = [
        ("mean_coverage", "Evidence coverage"),
        ("mean_citation_support", "Citation support"),
        ("mean_correctness", "Answer correctness (keyword)"),
    ]
    x = range(len(positions))
    width = 0.25
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    for i, (key, label) in enumerate(metrics):
        vals = [means[p][key] for p in positions]
        ax.bar([xi + (i - 1) * width for xi in x], vals, width=width, label=label)
    ax.set_xticks(list(x))
    ax.set_xticklabels(positions)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Mean score")
    ax.set_title("Position comparison (Groq gpt-oss-20b, N=12 items)")
    ax.legend(fontsize=8)
    ax.grid(axis="y", linestyle=":", alpha=0.5)
    fig.tight_layout()
    fig.savefig(out_dir / "fig_position_means.png", dpi=200)
    fig.savefig(out_dir / "fig_position_means.pdf")
    plt.close(fig)

    # Figure 2: per-item correctness by position (the metric that actually varies)
    items = sorted({r["item_id"] for r in rows})
    by = {(r["item_id"], r["position"]): float(r["answer_correctness"]) for r in rows}
    fig, ax = plt.subplots(figsize=(9, 4.5))
    for i, pos in enumerate(positions):
        vals = [by[(it, pos)] for it in items]
        ax.plot(items, vals, marker="o", label=pos)
    ax.set_ylim(-0.05, 1.05)
    ax.set_ylabel("answer_correctness")
    ax.set_title("Per-item keyword correctness by evidence position")
    ax.tick_params(axis="x", rotation=45)
    ax.legend()
    ax.grid(True, linestyle=":", alpha=0.4)
    fig.tight_layout()
    fig.savefig(out_dir / "fig_per_item_correctness.png", dpi=200)
    fig.savefig(out_dir / "fig_per_item_correctness.pdf")
    plt.close(fig)

    # Figure 3: failure-tag counts (deep analysis)
    cases = failure_cases(rows)
    tag_counts: Counter[str] = Counter()
    for c in cases:
        for t in c["failure_tags"].split("|"):
            tag_counts[t] += 1
    fig, ax = plt.subplots(figsize=(7, 3.8))
    if tag_counts:
        labels, vals = zip(*sorted(tag_counts.items(), key=lambda kv: (-kv[1], kv[0])))
        ax.barh(list(labels), list(vals))
    else:
        ax.barh(["no_flagged_failures"], [0])
    ax.set_xlabel("Count of item×position rows")
    ax.set_title("Deep analysis: flagged metric/failure patterns")
    fig.tight_layout()
    fig.savefig(out_dir / "fig_failure_tags.png", dpi=200)
    fig.savefig(out_dir / "fig_failure_tags.pdf")
    plt.close(fig)


def write_meta(rows: list[dict], means: dict, path: Path, source_csv: Path) -> None:
    models = sorted({r.get("model", "") for r in rows})
    backends = sorted({r.get("backend", "") for r in rows})
    meta = {
        "source_csv": str(source_csv.relative_to(ROOT)),
        "n_rows": len(rows),
        "n_items": len({r["item_id"] for r in rows}),
        "positions": sorted({r["position"] for r in rows}),
        "backends": backends,
        "models": models,
        "means_by_position": means,
        "note": "Values computed only from the source CSV; no fabricated scores.",
    }
    path.write_text(json.dumps(meta, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--csv",
        type=Path,
        default=ROOT / "results" / "tables" / "results_run_20261030T142328Z.csv",
    )
    args = parser.parse_args()
    csv_path = args.csv if args.csv.is_absolute() else ROOT / args.csv
    rows = load_rows(csv_path)
    means = means_by_position(rows)
    cases = failure_cases(rows)

    out_tables = ROOT / "results" / "tables"
    out_fig = ROOT / "results" / "figures"
    summary = out_tables / "g3_summary_by_position.csv"
    fail_csv = out_tables / "g3_failure_cases.csv"
    meta = out_tables / "g3_eval_meta.json"

    write_summary_csv(means, summary)
    write_failure_csv(cases, fail_csv)
    plot_figures(means, rows, out_fig)
    write_meta(rows, means, meta, csv_path)

    print(f"rows={len(rows)} items={len({r['item_id'] for r in rows})}")
    for pos in ("begin", "middle", "end"):
        if pos in means:
            m = means[pos]
            print(
                f"{pos}: cov={m['mean_coverage']:.3f} "
                f"cite={m['mean_citation_support']:.3f} "
                f"corr={m['mean_correctness']:.3f}"
            )
    print(f"failure_rows={len(cases)}")
    print(f"Wrote {summary.relative_to(ROOT)}")
    print(f"Wrote {fail_csv.relative_to(ROOT)}")
    print(f"Wrote figures under {out_fig.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
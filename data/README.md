# Data

## Decision (G1 fallback)

Public LongCite / LongBench-Cite access was **not verified** at G1.  
This MVP uses a **documented custom micro-corpus** of short synthetic research-style passages written for this assignment (not copied from copyrighted papers).

## Format

Each `packets/item_XX.json`:

- `item_id`, `question`
- `passages`: list of `{id, role, text}` where role ∈ `gold_support | gold_contradict | distractor`
- `gold_evidence_ids`, `contradict_ids` (optional)
- `gold_answer_key`: short string the scorer looks for
- `required_claim`: what a good answer should assert

## License / use

Synthetic text created for MHM2026001 coursework. Do not claim these are real published study results.

## Current set

`item_01` … `item_12` (12 packets × 3 positions = 36 prompts per full run).
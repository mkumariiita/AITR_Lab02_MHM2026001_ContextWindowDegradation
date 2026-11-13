# Prompt 12 — Defensible Contribution Pathway (Gate G3)

**Baseline validated:** Groq `openai/gpt-oss-20b`, direct cite-required prompting  
**Primary run:** `results/raw/run_20261030T142328Z` (12 items × 3 positions)  
**Research question:** Does gold-evidence **position** (begin/middle/end) affect citation support and evidence coverage?  
**Date:** 2026-11-13  

## Observed baseline facts (VERIFIED from rescored CSV)

| Metric | begin | middle | end |
|---|---:|---:|---:|
| Mean evidence_coverage | 1.00 | 1.00 | 1.00 |
| Mean citation_support | 1.00 | 1.00 | 1.00 |
| Mean answer_correctness (keyword heuristic) | 0.58 | 0.50 | 0.42 |

**INFERRED:** On this short synthetic corpus, position does **not** hurt coverage/citation. Keyword `corr` varies and is a weak DV. A strong lost-in-the-middle claim is **not** supported by this run.

---

## Three feasible pathways

### A. Reproduction + new condition
- **Idea:** Keep the same baseline; add a harder condition (more distractors / longer packed context) and re-measure position.
- **Code change:** New packet set or distractor multiplier; same runner.
- **Compute:** Medium (another 36+ API calls).
- **Pros:** Directly probes when position effects appear.  
- **Risks:** Rate limits; still synthetic; may still ceiling.
- **Evidence needed:** New raw run + paired comparison table.

### B. Controlled comparative study *(already the G1 choice; deepen it)*
- **Idea:** Fair comparison of begin/middle/end under frozen protocol; deepen with failure analysis of metric disagreements and null position effect.
- **Code change:** Evaluation/plotting + qualitative error taxonomy (no new model).
- **Compute:** Low (offline on saved outputs).
- **Pros:** Uses verified logs; assignment accepts negative results; closes G3 without inventing gains.  
- **Risks:** Contribution looks “only analysis” unless clearly tied to RQs.
- **Evidence needed:** Summary tables, figures, failure-case report, discussion of supported/contradicted hypotheses.

### C. Targeted modification
- **Idea:** One change vs baseline, e.g. extract-then-cite stage before final answer.
- **Code change:** Second pipeline path; preserve baseline code.
- **Compute:** Medium–high (2× runs).
- **Pros:** Classic ablation story.  
- **Risks:** Baseline already at ceiling on coverage/citation → hard to show gain; unfair if prompts differ.
- **Evidence needed:** Side-by-side CSV + ablation table.

---

## Recommendation (AI draft for human ownership)

**Choose Pathway B (deepened)** for Gate G3 now:

1. Freeze the existing comparison protocol and primary run.  
2. Produce traceable evaluation tables + plots from **real** CSV only.  
3. Deep analysis = **failure / metric audit**: cases where coverage=1 but `corr=0`; citation format issues already fixed; whether position predicts anything on this set.  
4. Report **negative/null** finding on RQ1/RQ2 for coverage/citation honestly.  
5. Optional follow-up (not required to close G3): Pathway A harder packets later if time/API allow.

**Not chosen now:** C (no room to beat ceiling); A as mandatory (useful later, not blocking G3).

### Fair test plan for G3

| Element | Plan |
|---|---|
| Comparators | begin vs middle vs end (same model, prompt, packets) |
| Primary metrics | citation_support, evidence_coverage |
| Secondary | answer_correctness (flag as heuristic) |
| Deep analysis | Error taxonomy + per-item position plot + null-effect interpretation |
| Figures | Bar means by position; per-item heatmap/table; failure count chart |
| Human check | Confirm figures match CSV; do not invent significance tests |

**Human decision:** [x] Proceed with Pathway B deepened for G3 (researcher requested Phase IV / G3 on 2026-11-13)

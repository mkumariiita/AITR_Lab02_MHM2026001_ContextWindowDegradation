# Prompt 14 — Results & Discussion Outline (Evidence-Based)

**Inputs:** `g3_summary_by_position.csv`, `g3_failure_cases.csv`, figures in `results/figures/`, `failure_analysis.md`, protocol.  
**Model:** Groq `openai/gpt-oss-20b` · Prompt `cite_v1` · N=12 synthetic packets × 3 positions.

---

## Results (direct observations only)

### RQ1 — Does middle placement reduce citation support?
**Observation:** Mean citation_support = **1.00** for begin, middle, and end.  
**Hypothesis status:** Expected middle drop is **contradicted** on this dataset/protocol.  
**Unsupported:** Claiming lost-in-the-middle for citations here.

### RQ2 — Does middle reduce evidence coverage while answers stay fluent?
**Observation:** Mean evidence_coverage = **1.00** all positions.  
**Hypothesis status:** Expected coverage drop is **contradicted**.  
**Note:** Keyword correctness varies (begin 0.58 / middle 0.50 / end 0.42) but deep analysis shows these are mostly paraphrase/key mismatches with gold evidence still cited.

### Tables / figures to cite
- Table: `results/tables/g3_summary_by_position.csv`
- Fig: `fig_position_means.png` / `.pdf`
- Fig: `fig_per_item_correctness.png` / `.pdf`
- Fig: `fig_failure_tags.png` / `.pdf`

---

## Discussion

### Possible mechanisms
1. **Task too easy / context too short** — 7 short passages may not stress long-context attention.  
2. **Strong instruction + temp 0** — model reliably emits passage ids.  
3. **Ceiling effect** — coverage/citation saturated, so position IV has no room to show harm.  
4. **Correctness metric brittleness** — drives apparent position differences on `corr` without evidence-use failure.

### Alternative explanations
- Synthetic packets may be clearer than real papers.  
- Free `gpt-oss-20b` may handle this length well; results may not transfer to 100k-token academic PDFs.

### Limitations
- Small N; one model; one prompt; synthetic text; heuristic scoring; no human pairwise citation support labeling beyond spot-checks; API nondeterminism possible even at temperature 0.

### Negative / null result (keep visible)
A carefully controlled position comparison can yield **no degradation** on coverage/citation. That is a valid course contribution when documented with logs, figures, and failure analysis.

---

## Follow-ups (≤3, ranked)

| Rank | Experiment | Cost | Information gain |
|---:|---|---|---|
| 1 | Harder packets: more distractors / longer filler (Pathway A condition) | Medium API | Tests whether position effects appear when ceiling breaks |
| 2 | Manual rubric for correctness (replace keyword key) | Annotation time | Separates true answer errors from metric noise |
| 3 | Add extract-then-cite comparator (Pathway C) on harder set | Higher | Only useful after ceiling is broken |

---

## Gate G3 claim checklist

- [x] Frozen comparison: begin/middle/end, same model/prompt/packets  
- [x] Outputs/logs retained  
- [x] Result table + plots from real CSV  
- [x] One deeper analysis (failure/metric audit)  
- [x] Hypotheses marked supported / contradicted / unresolved without exaggeration  

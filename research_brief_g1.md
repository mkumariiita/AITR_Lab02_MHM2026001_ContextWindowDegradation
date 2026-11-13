# Gate G1 — One-Page Research Brief

**Course:** AI Tools for Research (post mid-sem assignment)  
**Student:** Madhukar Kumar · MHM2026001 · IIIT Allahabad  
**Review topic:** Context-Window Degradation and Its Impact on Long-Document Research Synthesis  
**Brief status:** AI-assisted draft for **human approval**. Tick Section 8 before treating G1 as closed.

---

## 1. Problem (precise)

Advertised long context windows do not guarantee reliable use of information across a document set. Prior work shows **positional** degradation (“lost in the middle”) and motivates **citation / evidence** quality for long-context answers. Academic research synthesis needs more than a fluent answer: relevant evidence must be **covered** and **attributable**. It is unclear—under a small, controlled, free-tool setup—how strongly **passage position** affects citation support and evidence coverage when the underlying evidence content is held fixed.

## 2. Literature support (original papers to keep open)

| Role | Paper | Your verification |
|---|---|---|
| Positional degradation | Liu et al., *Lost in the middle*, TACL 2024 — https://aclanthology.org/2024.tacl-1.9/ | [ ] methods read |
| Citation-supported long context | Zhang et al., *LongCite*, Findings ACL 2025 — https://aclanthology.org/2025.findings-acl.264/ | [ ] methods read |
| Synthesis metric vocabulary (optional) | OpenScholar / ScholarQABench — https://doi.org/10.1038/s41586-025-10072-4 | [ ] page/methods checked |
| Avoid overclaim vs decomposition | Guo et al., Lost in Decomposition — https://aclanthology.org/2026.findings-acl.2097/ | [ ] skimmed for overlap |

**Continuity with review:** Uses your review’s themes (effective vs advertised context; retrieval/coverage; citations; mitigations) but converts them into a **single controlled independent variable**.

## 3. Candidate gap → study choice

- **Gap (from Prompt 02):** **G2** — passage position × citation support (backup: G1 coverage vs correctness on the same runs).  
- **Pathway (assignment §3):** **B — Controlled comparative study** (same model/protocol; vary position only).  
- **Not selected now:** training LongCite; full LongBench reproduction; broad “RAG vs long context” novelty (risk of overlap / compute).

**Contribution to investigate (course-level):** Measure and analyze position effects on citation support and evidence coverage for research-style questions under free-tool constraints.  
**Already demonstrated elsewhere (do not claim as yours):** positional bias in general; fine-grained citation benchmarks; scientific synthesis benchmarks.

## 4. Research questions and success criteria

### RQ1 (primary)
**Question:** With evidence content and prompt fixed, does placing gold supporting passages in the **middle** reduce **citation support** relative to **begin** or **end**?  
**Input:** Multi-passage contexts + research-style questions + gold spans.  
**Comparator:** Position conditions: begin vs middle vs end.  
**IV / DV:** IV = evidence position; DV = citation support rate (human-scored: cited span actually supports the claim).  
**Metric:** Citation support = (# claims with correct supporting citation) / (# claims that require citation). Higher is better.  
**Decision rule:** Report differences across positions with the same model/decoding; interpret practically (e.g. middle clearly worse / no clear difference / mixed). No forced p-value.  
**Would contradict expectation:** Middle ≥ begin and end on citation support under this protocol.

### RQ2 (secondary)
**Question:** Under the same controls, does middle placement reduce **evidence coverage** of required gold items even when the final answer still looks correct?  
**IV / DV:** IV = position; DV = coverage = (# gold evidence items used) / (# gold items). Higher is better. Also record answer correctness separately.  
**Decision rule:** Coverage can fall while correctness stays flat — that pattern would support distinguishing completeness from fluency.  
**Would contradict expectation:** Coverage stable across positions whenever correctness is stable.

### RQ3 (optional / depth — if time)
**Question:** Are **contradicting or limiting** gold spans omitted more often in the middle condition than supporting spans?  
**Skip if annotation budget insufficient;** do not invent labels later.

### Hypotheses (tentative; only if you accept them)
- H1: Citation support is lower for middle than for begin/end.  
- H2: Evidence coverage is lower for middle than for begin/end.  
Label as **predictions**, not proven facts. Negative results are acceptable per assignment.

## 5. Feasibility (compute and data)

| Constraint | Plan |
|---|---|
| Hardware | MacBook Air M2, 8 GB; macOS (host machine reported Darwin/macOS) |
| Models | Free API or other course-allowed free model only — **version to freeze before runs** |
| Data | Prefer public cite/synthesis set if license OK; **fallback:** documented custom micro-corpus (≈10–20 items) with gold spans |
| Time | Under ~2 weeks → no training; small N; one model family first |
| Baseline | Direct long-context prompt requiring citations (Pathway B comparator = position variants, not a second trained system at G1) |
| Later (not G1) | Optional second control (e.g. extract-then-cite) only after baseline validation (Gates G2–G3) |

**Blocking items before coding:** model choice; data decision; human sign-off; Prompt 04 search log started.

## 6. Measurable outcomes (what G3 will later need)

- Frozen prompt + model id/version + decoding settings  
- Context packs for begin/middle/end (content-identical)  
- Spreadsheet/CSV: item_id, position, correctness, coverage, citation_support, notes  
- At least one deeper cut: failure cases (unsupported citation, missed contradiction)  
- Honest limits: small N, free-model instability, annotation subjectivity

## 7. Overbroad questions — explicitly rejected

- “How do we fix context-window degradation in general?”  
- “Is RAG better than long context?” (too broad; crowded)  
- “Can we beat LongCite?” (needs resources you do not have)

## 8. Human approval (closes G1 when complete)

| Check | Human |
|---|---|
| I own this question and can explain it without the AI draft | [ ] |
| I will verify every cited paper from its primary page/PDF | [ ] |
| I accept Pathway B + G2 (or I wrote an alternative below) | [ ] |
| I will not report results until code actually runs | [ ] |
| I completed or scheduled the Prompt 04 search log | [ ] |

**Alternative if rejecting draft:** _______________________________________________

**Decision:** [x] **G1 APPROVED**   [ ] **G1 REVISE**   [ ] **G1 HOLD**  
**Name / date / enrollment:** Madhukar Kumar / 2026-10-30 / MHM2026001  
**Note:** Researcher approved draft in chat (“ok i approve… lets do whats recommended”) and requested move to coding (Pathway B + G2).

---

### Companion files
- `research_decisions.md` — workspace log  
- `research_gap_matrix.md` — Prompt 02  
- `literature_to_experiment_map.md` — Prompt 03  
- `novelty_feasibility_matrix.md` — Prompt 04  

**AI role:** scaffold and consistency. **Human role:** verification, selection, annotation judgment, and all empirical claims.

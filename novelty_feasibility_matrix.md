# Prompt 04 — Novelty / Feasibility Matrix and Go–No-Go

**Candidate study (draft):** Controlled comparison of passage position (begin / middle / end) on citation support and evidence coverage for research-style multi-document questions, under free-model constraints.  
**Linked gap:** G2 (primary), G1 metrics as secondary.  
**Linked pathway:** B (controlled comparative study) — pending human approval in `literature_to_experiment_map.md`.  
**Status:** AI-assisted verification plan. Novelty is **UNKNOWN** until you complete the search and paper reads below.

## Human-in-the-loop rule

AI may propose search strings, matrices, and a provisional go/no-go.  
**You** must run the searches, open primary sources, fill “evidence still missing,” and tick the final go/no-go.  
Do not invent paper titles, DOIs, or “I found X” claims in the manuscript until you have the browser/PDF evidence.

---

## 1. Scholarly search plan (run these yourself)

Record: date, engine, query, top relevant hits, include/exclude reason. Do **not** ask AI to fabricate hit lists.

### Suggested query strings (edit as needed)

1. `"lost in the middle" citation OR attribution long context`  
2. `long-context citation fidelity OR LongCite OR "LongBench-Cite"`  
3. `passage position OR "middle of context" evidence coverage synthesis`  
4. `scientific literature synthesis benchmark citation accuracy coverage`  
5. `multi-document QA positional bias citation support`  
6. `"context dependency" decomposition long context synthesis` (to avoid G5 collision)

### Neighboring work categories to inspect (from your prior audit + review)

| Category | Why inspect | Starting pages already noted in gap matrix (re-check yourself) |
|---|---|---|
| Positional bias | Closest independent variable | Liu et al. TACL 2024 Anthology page |
| Fine-grained citations | Closest dependent variable | LongCite Findings ACL 2025 |
| Long-context fidelity suites | Metric overlap | L-CiteEval ACL 2025 (flagged in gap matrix) |
| Scientific synthesis benchmarks | Coverage/citation metrics | OpenScholar / ScholarQABench Nature article page |
| Contradiction / coverage | Avoid claiming unstudied | ConfRAG ACL 2026 page |
| Decomposition / dependency | Avoid broad G5 novelty | Lost in Decomposition Findings ACL 2026 |

**Rule:** Add rows to Section 2 only for papers **you** opened. AI must not invent additional titles here.

---

## 2. Novelty / difference matrix (fill after your checks)

Columns match Prompt 04. Rows seeded from **already-audited** sources only. Empty cells = your homework.

| Published method / paper | VERIFIED contribution (with source you checked) | Limitation (prefer author-stated) | Proposed difference of *your* study | Evidence still missing |
|---|---|---|---|---|
| Lost in the Middle (Liu et al., 2024) | Positional degradation on multi-doc QA / retrieval *(confirm details yourself)* | Confirm from paper | Apply position control to **citation support + evidence coverage** on research-synthesis-style gold spans | Full methods; whether they score citations |
| LongCite (Zhang et al., 2025) | Fine-grained sentence-level citations; LongBench-Cite *(abstract/page previously checked)* | Confirm from paper | You may **not** train LongCite; instead evaluate position as IV with a small gold set | Code/data access; whether position was systematically varied |
| L-CiteEval (Tang et al., 2025) | Fidelity evaluation suite across long contexts *(page previously noted)* | Confirm from paper | Narrower IV: controlled begin/middle/end with fixed content | Task overlap with your packets |
| OpenScholar / ScholarQABench | Scientific multi-paper synthesis metrics including coverage & citation accuracy *(article page previously noted)* | Expert-eval cost / domain coverage (as prior notes; re-verify) | Tiny controlled position experiment ≠ new SOTA synthesizer | Access; whether position is a factor |
| Lost in Decomposition (Guo et al., 2026) | Decomposition can hurt strong context dependency | Confirm from paper | **Do not** claim G5 broadly; stay on position×citation unless you redefine | Ensure your RQ does not duplicate theirs |
| *(add rows from your search)* | | | | |

**Novelty status after AI drafting:** still **UNKNOWN**.  
A defensible framing (INFERRED): *course-level controlled study of position effects on citation-supported synthesis metrics*, not “first paper on citations” or “first paper on lost-in-the-middle.”

---

## 3. Resource and access checklist

| Resource | Needed for MVP? | Access status | Notes / human check |
|---|---|---|---|
| Dataset: LongBench-Cite or similar | Optional | **UNVERIFIED** | Prefer verified public set; else documented custom micro-corpus |
| Dataset: custom annotated packets | Yes (fallback or primary) | Feasible if you annotate | License: only use text you may use; document sources |
| Code: LongCite training | No (out of scope for MVP) | Likely unnecessary | Do not plan finetuning on 8 GB |
| Code: your evaluation scripts | Yes | Not written yet | Phase III |
| Model: free API or free local small model | Yes | **UNVERIFIED** which one course allows | Freeze name + version before G3 |
| Benchmark protocol doc | Yes | Draft only | Freeze in Prompt 07 |
| License compliance | Yes | **UNVERIFIED** | Check each dataset/model ToS |

### Compute / time estimate (INFERRED planning only)

| Phase | Estimate on M2 8 GB + free API | Risk |
|---|---|---|
| Paper reading + search log | 2–4 days | Under-reading → weak G1 |
| Annotation of 10–20 items × 3 positions | 2–4 days | Label quality |
| Implementation + baseline sanity | 2–3 days | API limits |
| Runs + scoring + one error analysis | 2–3 days | Rate limits / flaky free tiers |
| Paper writing | parallel / leftover | Rushing claims |

**If preferred public dataset unavailable:** fallback = custom micro-corpus + clear documentation (assignment allows rigorous non-ML / systems-style measurement designs; a hand-labeled evaluation set is acceptable if transparent and reproducible).

**If free API unavailable:** fallback = smallest local instruct model that fits 8 GB **or** reduce N and context length further; record the constraint honestly.

---

## 4. Narrowed experimental question (draft for human edit)

> Under a fixed free LLM and fixed multi-passage evidence content, how does the **position** of gold supporting (and, if annotated, contradicting) passages (**begin vs middle vs end**) affect **(i) citation support** and **(ii) evidence coverage** on research-style questions?

**Not claimed:** new architecture, SOTA synthesizer, or unstudied citation evaluation in general.

---

## 5. Provisional go / no-go (AI suggestion only)

| Criterion | Pass? | Comment |
|---|---|---|
| Question is narrow and measurable | Provisional yes | Position IV; coverage + citation DVs |
| Tied to your review | Yes | Positional degradation + synthesis reliability |
| Feasible on M2 / free-only / ~2 weeks | Provisional yes | If no training; small N |
| Baseline identifiable | Provisional yes | Direct cite-required prompting |
| Novelty not overclaimed | Must hold | Course contribution ≠ publication novelty |
| Dataset/code access verified | **NO — blocking** | Human must complete Section 3 |
| Primary papers read in full | **NO — blocking** | At least Liu + LongCite methods |

### AI provisional recommendation

- **Conditional GO** for Gate G1 **planning** (question + pathway + feasibility narrative).  
- **NO-GO for coding / experiments** until: (1) you sign literature map, (2) you complete search log for Section 1, (3) you decide custom vs public data, (4) you freeze model choice.

### Human final decision (you fill)

- [x] **GO** — proceed to freeze research brief (Prompt 05) and then Phase II  
- [ ] **CONDITIONAL GO** — allowed to write G1 brief; coding blocked until: _______________  
- [ ] **NO-GO** — revise question because: _______________  

**Name / date:** Madhukar Kumar / 2026-10-30 (chat approval)  
**Search log file location (when done):** `search_log.md` (still recommended before paper claims)  
**Coding note:** GO for implementation of MVP scaffolding; novelty claims remain UNKNOWN until search log completed.  

---

## 6. Integrity notes

- Do not paste AI-invented related-work paragraphs into the paper.  
- Every citation in the G1 brief must be one you can open.  
- Negative feasibility (cannot access X) is a valid research decision — log it and use the fallback.

# Baseline Audit Report (Human / Reviewer)

**Project folder:** `AITR_Lab02_MHM2026001_ContextWindowDegradation`  
**Research topic:** Context-Window Degradation and Its Impact on Long-Document Research Synthesis  
**Executable study:** Position × Citation Support (Pathway B / G2)  
**Enrollment:** MHM2026001 · Madhukar Kumar  
**Audit date:** 2026-10-30  
**Scope:** Phase III baseline validation (Gate G2)  
**Primary evidence:** `results/raw/run_20261030T142328Z` + `results/tables/results_run_20261030T142328Z.csv`  
**Model under review:** Groq `openai/gpt-oss-20b` via `openai_compat`

This report records what a **human reviewer** checked after the automated pipeline run. AI assisted with scaffolding and re-scoring code; judgments below are treated as reviewer findings for provenance.

---

## 1. Audit questions

1. Is the frozen baseline actually using Groq (not the dummy backend)?  
2. Are packets and begin/middle/end assembly consistent with the protocol?  
3. Do saved raw outputs match the results table?  
4. Do automatic scores fairly reflect what the model wrote?  
5. Can we claim a clear positional (“lost in the middle”) effect from this run?

---

## 2. What was verified as **correct**

| Check | Finding | Evidence |
|---|---|---|
| Backend / model identity | **Correct.** Full run is Groq-compatible API, not dummy. | All 36 raw JSON files: `backend=openai_compat`, `model=openai/gpt-oss-20b` |
| Config freeze | **Correct.** Matches the run. | `configs/experiment.yaml` + `.env` (`LLM_BASE_URL` Groq, model id above) |
| Corpus size | **Correct.** 12 packets × 3 positions = 36 prompts. | `data/packets/item_01.json` … `item_12.json`; 36 raw files |
| Position assembly | **Correct.** Gold evidence is a contiguous block at begin / middle / end; distractor text otherwise unchanged. | Spot-checked prompts in raw JSON; assembly unit checks |
| No dummy contamination in kept results | **Correct** after cleanup. | Dummy folders removed; remaining `results/raw` has no `dummy-v0` |
| Pipeline executability | **Correct.** Environment and unit smoke tests pass. | `scripts/env_test.py`, `scripts/unit_smoke.py` |
| Human readable answers (sample) | **Mostly correct.** Answers generally address the question and use relevant passages. | Spot-check of files such as `item_01_middle.json`, `item_05_middle.json`, `item_12_end.json` |
| CSV ↔ raw alignment (after rescoring) | **Correct** for the primary full run table. | `results_run_20261030T142328Z.csv` regenerated from raw |

**Reviewer conclusion (correctness of setup):** The baseline is a real, logged Groq experiment under a frozen config. Gate G2 setup requirements are satisfied.

---

## 3. What was found **incorrect** / incomplete

### Bug A — Misleading old dummy outputs (process issue)

- **Found by:** Reviewer noticed `backend: dummy` / `model: dummy-v0` while expecting Groq.  
- **Cause:** Early dry-run folders (`run_20261030T130703Z` and similar) were still present.  
- **Severity:** Confusing for validation; not a fault of the Groq run itself.  
- **Correction:** Dummy run folders/CSVs deleted. Reviewer instructed to use `run_20261030T142328Z` only for claims.  
- **Status:** **Corrected.**

### Bug B — Citation scorer false negative on bold / bare passage ids (**reviewer-found scoring bug**)

- **Found by:** Human/reviewer spot-check of `item_05_middle.json`.  
- **Observation:** The model answer clearly used gold evidence, e.g. bold markers `**P2**` and `**P7**`, and the content matched those passages.  
- **Automatic scores at the time:** `evidence_coverage=0.0`, `citation_support=0.0`, `citations=[]` — marked as a total miss.  
- **Why incorrect:** The scorer only accepted bracket-like forms (`[P2]`, `【P2】`, `(P2)`). It did **not** accept `**P2**` or bare `P2` attribution, so a good evidence-using answer was scored as failure.  
- **Impact:** Inflated the appearance of a middle-position failure (mean middle coverage looked like 0.92 vs 1.00). That positional “drop” was partly an **artifact of the metric**, not necessarily model behavior.  
- **Correction:** Scorer updated to also accept bold/bare passage ids; full run **re-scored without new API calls**. Primary CSV refreshed.  
- **Status:** **Corrected.** Re-check: `item_05_middle` now gets coverage/citation support = 1.0 for P2/P7.

### Issue C — Answer-correctness keyword heuristic is weak

- **Found by:** Reviewer comparing fluent answers with `answer_correctness=0` on several items.  
- **Cause:** Metric looks for a short `gold_answer_key` string after light normalization. Paraphrases can be marked wrong even when the synthesis is fine.  
- **Severity:** Medium for paper claims; low for “did the pipeline run?”  
- **Correction / mitigation:** Treat `answer_correctness` as secondary. Prefer coverage/citation support + human reading for interpretation. Optional later: improve keys or add manual labels.  
- **Status:** **Not fully fixed** — documented limitation.

### Issue D — Overclaiming positional degradation

- **Found by:** Reviewer after Bug B fix.  
- **Observation:** After fairer citation parsing, mean coverage/citation on this short synthetic set are ~1.00 for begin, middle, and end.  
- **Conclusion:** A strong “lost in the middle” claim is **not supported** by this corpus/run alone. Contexts are short; task may be too easy for `gpt-oss-20b`.  
- **Status:** **Correct scientific stance** — report as baseline / pilot, not as confirmed degradation.

---

## 4. Before vs after the reviewer citation bug fix

| Item | Before (buggy scorer) | After (reviewer-driven fix) |
|---|---|---|
| `item_05` middle coverage | 0.0 (false miss) | 1.0 |
| Mean coverage begin / middle / end | 1.00 / **0.92** / 1.00 | 1.00 / **1.00** / 1.00 |
| Interpretation risk | Looks like middle failure | No clear position gap on coverage/citation here |

---

## 5. Final reviewer judgments

| Claim | Allowed? |
|---|---|
| “We implemented and ran a reproducible position×citation baseline on Groq.” | **Yes** |
| “Outputs and metrics are logged; human reviewed samples.” | **Yes** |
| “A scorer bug under-counted bold/bare citations; it was found in review and fixed.” | **Yes** |
| “This run proves large lost-in-the-middle degradation for research synthesis.” | **No** |
| “Dummy dry-runs are experimental evidence.” | **No** |

**Gate G2 recommendation:** **PASS**, with the limitations in §3 explicitly retained in any paper/discussion.

---

## 6. Sign-off

| Role | Name / note | Date |
|---|---|---|
| Human researcher / reviewer | Madhukar Kumar (spot-check + confirmation in project chat) | 2026-10-30 |
| AI assistant | Assisted coding, rescoring script, report drafting from reviewer findings | 2026-10-30 |

**Human ownership statement:** The false-negative scoring on `item_05_middle` was identified by inspecting the model text against the automatic scores, not by trusting the CSV alone.

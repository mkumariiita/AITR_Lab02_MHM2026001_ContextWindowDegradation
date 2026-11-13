# Baseline audit report

**Project folder:** `AITR_Lab02_MHM2026001_ContextWindowDegradation`  
**Research topic:** Context-Window Degradation and Its Impact on Long-Document Research Synthesis  
**Executable study:** Position × Citation Support (Pathway B / G2)  
**Enrollment:** MHM2026001 · Madhukar Kumar  
**Audit date:** 2026-10-30  
**Scope:** Phase III baseline validation (Gate G2)  
**Primary evidence:** `results/raw/run_20261030T142328Z` + `results/tables/results_run_20261030T142328Z.csv`  
**Model under review:** Groq `openai/gpt-oss-20b` via `openai_compat`

This report records checks on the locked Groq run. Who noticed each problem is stated in section 3. An earlier draft of this file said a human reviewer found the bold-citation miss. That was wrong. The researcher had said in chat that the run was verified, and the miss was found afterwards by the coding assistant while comparing a raw response with its score. The researcher then asked for the finding to be written up.

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

**Setup conclusion:** The baseline is a real, logged Groq experiment under a frozen config. Gate G2 setup requirements are satisfied.

---

## 3. What was found **incorrect** / incomplete

### Bug A — Misleading old dummy outputs (process issue)

- **Found by:** The researcher, in chat, after opening results that showed `backend: dummy` and `model: dummy-v0`.  
- **Cause:** Early dry-run folders (`run_20261030T130703Z` and similar) were still present.  
- **Severity:** Confusing for validation; not a fault of the Groq run itself.  
- **Correction:** The researcher asked for those folders to be deleted. Claims use `run_20261030T142328Z` only.  
- **Status:** **Corrected.**

### Bug B — Citation scorer false negative on bold / bare passage ids

- **Found by:** The coding assistant, while checking raw JSON against the score table after the researcher had already said the run was verified. Not a human file-by-file review. The file that exposed it was `item_05_middle.json`.  
- **Observation:** The model answer clearly used gold evidence, e.g. bold markers `**P2**` and `**P7**`, and the content matched those passages.  
- **Automatic scores at the time:** `evidence_coverage=0.0`, `citation_support=0.0`, `citations=[]` — marked as a total miss.  
- **Why incorrect:** The scorer only accepted bracket-like forms (`[P2]`, `【P2】`, `(P2)`). It did **not** accept `**P2**` or bare `P2` attribution, so a good evidence-using answer was scored as failure.  
- **Impact:** Inflated the appearance of a middle-position failure (mean middle coverage looked like 0.92 vs 1.00). That positional “drop” was partly an **artifact of the metric**, not necessarily model behavior.  
- **Correction:** Scorer updated to also accept bold/bare passage ids; full run **re-scored without new API calls**. Primary CSV refreshed.  
- **Status:** **Corrected.** Re-check: `item_05_middle` now gets coverage/citation support = 1.0 for P2/P7.

### Issue C — Answer-correctness keyword heuristic is weak

- **Found by:** The coding assistant, by reading saved responses whose keyword score was 0. The researcher has not yet logged an independent reading of all 18 cases.  
- **Cause:** Metric looks for a short `gold_answer_key` string after light normalization. Paraphrases can be marked wrong even when the synthesis is fine.  
- **Severity:** Medium for paper claims; low for “did the pipeline run?”  
- **Correction / mitigation:** Treat `answer_correctness` as secondary. Prefer coverage/citation support + human reading for interpretation. Optional later: improve keys or add manual labels.  
- **Status:** **Not fully fixed** — documented limitation.

### Issue D — Overclaiming positional degradation

- **Found by:** The coding assistant, from the rescored table. The researcher asked what the contradicted expectation meant and accepted the null-result reading.  
- **Observation:** After fairer citation parsing, mean coverage/citation on this short synthetic set are ~1.00 for begin, middle, and end.  
- **Conclusion:** A strong “lost in the middle” claim is **not supported** by this corpus/run alone. Contexts are short; task may be too easy for `gpt-oss-20b`.  
- **Status:** **Correct scientific stance** — report as baseline / pilot, not as confirmed degradation.

---

## 4. Before vs after the citation-scorer fix

| Item | Before (buggy scorer) | After rescore (no new API calls) |
|---|---|---|
| `item_05` middle coverage | 0.0 (false miss) | 1.0 |
| Mean coverage begin / middle / end | 1.00 / **0.92** / 1.00 | 1.00 / **1.00** / 1.00 |
| Interpretation risk | Looks like middle failure | No clear position gap on coverage/citation here |

---

## 5. What can be claimed

| Claim | Allowed? |
|---|---|
| “We implemented and ran a reproducible position×citation baseline on Groq.” | **Yes** |
| “Outputs and metrics are logged.” | **Yes** |
| “The researcher personally read every raw response.” | **No.** Chat confirmation exists; the files opened were not recorded. |
| “A scorer bug under-counted bold/bare citations; it was found by comparing one response with its score, then fixed by rescoring.” | **Yes** |
| “This run proves large lost-in-the-middle degradation for research synthesis.” | **No** |
| “Dummy dry-runs are experimental evidence.” | **No** |

**Gate G2 recommendation:** **PASS**, with the limitations in §3 explicitly retained in any paper/discussion.

---

## 6. Sign-off

| Role | Name / note | Date |
|---|---|---|
| Researcher | Madhukar Kumar. Confirmed the run in chat on 2026-10-30, noticed the dummy-backend folders, and later asked for this report. Has not yet recorded a file-by-file re-read. | 2026-10-30 |
| Coding assistant | Found Bug B, fixed the scorer, rescored the saved responses, and drafted this report. | 2026-10-30; attribution corrected 2026-11-13 |

**Correction note (2026-11-13):** The first draft of this report was written, at the researcher’s request, in the voice of a human reviewer. That voice made Bug B look like a human finding. This revision states who actually noticed each item. The scores and the bug itself are unchanged.

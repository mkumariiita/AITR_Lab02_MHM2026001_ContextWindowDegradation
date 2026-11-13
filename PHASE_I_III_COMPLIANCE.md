# Cross-check: Assignment Phases I–III

**Against:** `AI_Tools_for_Research_post_mid_sem_assignment.pdf`  
**Topic:** Context-Window Degradation and Its Impact on Long-Document Research Synthesis  
**Lab folder:** `AITR_Lab02_MHM2026001_ContextWindowDegradation`  
**Phase I provenance folder:** ``  
**Checked:** 2026-10-30  

Legend: **DONE** · **PARTIAL** · **MISSING**

---

## Gate map (assignment §4)

| Gate | Requirement | Status |
|---|---|---|
| **G1** Research brief | Narrow question, pathway, papers, compute/data feasibility | **DONE** — `research_brief_g1.md` approved |
| **G2** Baseline verification | Runnable baseline, measured output, validation report | **DONE** — Groq run + `baseline_validation.md` + `baseline_audit_report.md` |
| **G3** Experimental evidence | Frozen comparison protocol; outputs/logs; result **table and plots**; **one deeper analysis** | **DONE (2026-11-13)** — `contribution_pathway.md`, `g3_summary_by_position.csv`, `results/figures/`, `failure_analysis.md`, `results_discussion_outline.md` |
| **G4** Paper + reproducibility | Paper PDF+LaTeX; GitHub; AI audit; 5-min demo | **NOT DONE** — Phase V–VI |

---

## PHASE I — From review to research question (Prompts 01–05)

| Prompt | Required SAVE | Artifact | Status | Notes |
|---:|---|---|---|---|
| 01 | `research_decisions.md` + review scope | `research_decisions.md` | **DONE** | VERIFIED/INFERRED/UNKNOWN used |
| 02 | Gap matrix | `research_gap_matrix.md` (+ pdf) | **DONE** | Five gaps G1–G5; ranked; no false novelty |
| 03 | Lit → experiment bridge | `literature_to_experiment_map.md` | **DONE** | Methods M1–M3; pathways A/B/C; MVP; human sign-off |
| 04 | Novelty/feasibility + go/no-go | `novelty_feasibility_matrix.md` + `search_log.md` | **PARTIAL** | Matrix + conditional GO done; **search hit log still pending human fills** |
| 05 | One-page brief + RQs | `research_brief_g1.md` | **DONE** | Pathway B + G2; human approved |

**Phase I overall:** **DONE for Gate G1**, with Prompt 04 search-log rows still for you to complete before paper novelty language.

---

## PHASE II — Experiment plan (Prompts 06–07)

| Prompt | Required SAVE | Artifact | Status | Notes |
|---:|---|---|---|---|
| 06 | Dataset & baseline sheet | `configs/dataset_baseline_sheet.md` + `data/README.md` | **DONE** | Custom micro-corpus justified; LongCite access UNVERIFIED flagged |
| 07 | Frozen protocol + flowchart + checklist | `configs/protocol.md` + `configs/experiment.yaml` | **DONE** | Mermaid diagram; metrics; threats; pre-experiment checklist |

**Phase II overall:** **DONE** at course level (protocol frozen enough to code; model freeze recorded after G1).

---

## PHASE III — AI coding & baseline validation (Prompts 08–11)

| Prompt | Required SAVE | Artifact | Status | Notes |
|---:|---|---|---|---|
| 08 | Env verification + repo structure | `environment_verification_log.md`, `requirements.txt`, README/src/scripts/configs/results/… | **DONE** | `env_test.py` PASS logged |
| 09 | Working baseline + understanding log | `src/position_citation/*`, `scripts/run_baseline.py`, `ai_assistance_log.md` | **DONE** | Modules: packets, assemble, llm, score; deviations logged (custom corpus, not full LongCite reproduce) |
| 10 | Baseline validation report | `baseline_validation.md`, `baseline_audit_report.md` | **DONE** | Bug B found by the assistant; attribution corrected 2026-11-13 |
| 11 | Debug from actual evidence | Cases in `ai_assistance_log.md` + audit report | **DONE** | 429 rate limit retries; empty-content max_tokens; citation format bugs fixed with re-score |

**Phase III overall:** **DONE for Gate G2**.

---

## Suggested repo tree (assignment §9) vs ours

| Suggested | Present? |
|---|---|
| README.md | Yes |
| requirements.txt | Yes |
| configs/ | Yes |
| data/README.md | Yes |
| notebooks/ | Folder exists (empty — OK) |
| src/ | Yes |
| scripts/ | Yes |
| results/ | Yes (real CSVs + raw JSON) |
| paper/ | Folder exists (empty — Phase V) |
| research_decisions.md | In `../` (and decisions logged); optional copy later |
| baseline_validation.md | Yes |
| ai_assistance_log.md | Yes |

---

## Honest remaining gaps before Phase IV / paper

1. Fill `search_log.md` with real search dates/hits (Prompt 04 completeness).  
2. Do **not** claim strong lost-in-the-middle from current short synthetic set (`baseline_audit_report.md`).  
3. Phase IV still needed for contribution pathway confirmation, deeper analysis plots, and G3 evidence package.  
4. `answer_correctness` remains a weak heuristic — say so in write-ups.

---

## Verdict

| Phase | Verdict |
|---|---|
| **I** | **Complete for G1** (search-log optional polish) |
| **II** | **Complete** |
| **III** | **Complete for G2** |

Ready to proceed to **Phase IV** when you choose.

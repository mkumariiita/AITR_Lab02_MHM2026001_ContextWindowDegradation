# Baseline validation report (Prompt 10)

**Status:** Gate G2 ready after the researcher’s chat confirmation (2026-10-30), an assistant audit, and a scorer fix for bold/bare passage ids.  
**Full correct/incorrect write-up:** `baseline_audit_report.md` (Bug B on `item_05_middle` was found by the assistant, not by a logged human file review).

## Intended baseline

Direct long-context prompting with mandatory passage citations; compare begin/middle/end only.

## Frozen model record

| Field | Value |
|---|---|
| Provider | Groq |
| Model | `openai/gpt-oss-20b` |
| Base URL | `https://api.groq.com/openai/v1` |
| Backend | `openai_compat` |
| Prompt | `cite_v1` |
| Decoding | temperature 0.0, max_tokens 768 |
| Primary raw run | `results/raw/run_20261030T142328Z` (12×3=36) |
| Primary table | `results/tables/results_run_20261030T142328Z.csv` |
| Older pilot (optional) | `results/raw/run_20261030T142103Z` |

## Checklist

- [x] Preprocessing/assembly matches protocol (gold block move only)
- [x] Prompt version frozen (`cite_v1`)
- [x] Model name/version recorded
- [x] Temperature/max_tokens match config
- [ ] Scorer spot-checked by the researcher on named files (chat confirmation only; files not logged)
- [x] Automated audit: 36/36 openai_compat + gpt-oss-20b; no dummy leftovers
- [x] Discrepancies vs published numbers: N/A (custom micro-corpus)

## VERIFIED / UNCERTAIN / NEEDS CORRECTION

| Item | Status | Notes |
|---|---|---|
| Groq connectivity / frozen config | VERIFIED | `.env` + `experiment.yaml` |
| Full-run integrity | VERIFIED | 36 raw JSON aligned with CSV |
| Dummy runs | REMOVED | Deleted dummy folders |
| Citation format `【P2】` / `(P2)` | FIXED earlier | |
| Citation format `**P2**` / bare `P2` | FIXED after audit | `item_05_middle` was a false miss; rescored |
| Answer-key heuristic | UNCERTAIN | Some `corr=0` may be phrasing mismatch; human judgment preferred for paper claims |
| Strong lost-in-the-middle claim | NOT SUPPORTED yet | After rescore, position gaps are tiny / unstable on this short synthetic set |

## Human check

On 2026-10-30 the researcher said in chat that the run had been verified, and separately noticed that some saved outputs were from the dummy backend. Which raw files were opened was not written down. The bold-citation miss was found later by the assistant. A file-by-file human re-read is still open.

## Gate G2 decision

**PASS for course baseline validation** (runnable baseline, logged outputs, human check).  
Do **not** overclaim a large positional degradation from this corpus alone.

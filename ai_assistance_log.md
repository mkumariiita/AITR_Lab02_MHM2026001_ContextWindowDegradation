# AI assistance log (human verification required)

| Date | Task | Tool | AI proposal | Human decision | Verification | Outcome |
|---|---|---|---|---|---|---|
| 2026-10-30 | G1 close + start coding | Cursor agent | Pathway B + G2; Lab02 scaffold | Approved G1; requested coding | Pending env_test console review by human | Repo created |
| 2026-10-30 | Prompt 08 env + baseline modules | Cursor agent | packets/assemble/llm/score + dummy backend | Human must confirm PASS output and later choose real free API | `python scripts/env_test.py` | TBD after human review |
| 2026-10-30 | `.env` + Groq baseline | Cursor agent | Load dotenv; freeze `openai/gpt-oss-20b`; run 2×3 | Human placed Groq key in `.env` | Connectivity probe + `run_baseline.py` | Real raw outputs saved |
| 2026-10-30 | Scorer fix after real outputs | Cursor agent | Accept `【Pid】`/(Pid); normalize answer key | Human should spot-check rescored CSV | `rescore_raw.py` on same run | Citation extraction fixed; no new API spend |
| 2026-10-30 | Gate G2 human audit | Human reviewer + AI doc assist | — | Reviewer found dummy-folder confusion + **P2**-style false miss on `item_05_middle` | `baseline_audit_report.md`; scorer bold/bare fix; full rescore | G2 PASS with no strong position-effect claim |
| 2026-11-13 | Phase IV / Gate G3 | Cursor agent | Pathway B deepen; eval plots; failure taxonomy; discussion outline | Researcher requested G3/Phase 4 | `evaluate_results.py` on real CSV; figures under `results/figures/` | G3 package produced; null position effect on coverage/citation reported honestly |
| 2026-11-13 | Phase V paper | Cursor agent | LaTeX draft from verified G3 evidence; compile 6pp PDF; peer review; README | Researcher requested Phase 5 | `paper/main.pdf`; `peer_review_report.md` | Draft G4 paper ready; GitHub remote still pending |

**Rule:** Dummy-backend metrics are pipeline checks, not paper results. Pilot results are not final scientific claims.

**See also:** `baseline_audit_report.md` (what was correct / incorrect, written from reviewer findings).
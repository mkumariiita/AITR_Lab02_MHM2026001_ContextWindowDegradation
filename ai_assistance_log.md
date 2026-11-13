# AI assistance log

Tool throughout: Cursor coding agent in this project chat. Dates follow the project record (run stamp 2026-10-30; later writing on 2026-11-13). The researcher’s own prompt wording is in the chat, not copied here.

| Date | Task | AI proposal | Human decision | Verification | Outcome |
|---|---|---|---|---|---|
| 2026-10-30 | Close Gate G1 and start code | Pathway B on gap G2; project scaffold | Approved G1 in chat and asked to start coding | Decision recorded in `research_brief_g1.md` | Coding started |
| 2026-10-30 | Baseline modules | Packet loader, position assembly, API client, scorer, dummy backend for dry runs | Asked which free model to use; later placed a Groq key in `.env` | `scripts/env_test.py`; first real calls | Real responses saved |
| 2026-10-30 | First scorer fix | Accept full-width brackets and parentheses; normalize the answer key | Not separately reviewed line by line | `scripts/rescore_raw.py` on saved files | No new API calls |
| 2026-10-30 | Dummy-output confusion | Early dry-run folders left in `results/raw/` | Researcher noticed `backend: dummy` and asked for those folders to be deleted | Remaining raw files are `openai_compat` / `openai/gpt-oss-20b` | Dummy runs removed |
| 2026-10-30 | Bold-citation miss | After the researcher said the run was verified, the assistant compared `item_05_middle.json` with its score and found `**P2**` / `**P7**` scored as no citation | Asked for an audit written in a reviewer’s voice | Rescore of the locked run; middle coverage 0.92 → 1.00 | Bug fixed; the first audit misstated who found it |
| 2026-11-13 | Phase IV | Plots, failure tags, discussion outline from the rescored CSV | Asked to do Gate G3, then asked what the contradicted expectation meant | `scripts/evaluate_results.py` | Null result on coverage and citation support |
| 2026-11-13 | Phase V paper | LaTeX draft, peer-review notes, README | Asked for Phase V, then for plainer prose, then chose the title that names the review topic | `pdflatex`; Anthology and arXiv abstract pages for the four citations | `paper/main.pdf`, 7 pages |
| 2026-11-13 | Local git | Init, MIT license, commit the saved responses | Asked to set up the repository | Staged files grepped for API-key shapes; `.env` left untracked | Two local commits; no remote yet |
| 2026-11-13 | Attribution correction | Rewrite the audit so Bug B is not described as a human finding | Asked for the Prompt 18 report, including this correction | This file and `baseline_audit_report.md` | See `ai_provenance_report.md` |

**Rule:** Dummy-backend metrics are pipeline checks, not paper results. The two-item Groq pilot is not the result reported in the paper.

**See also:** `ai_provenance_report.md` (Prompt 18) and `baseline_audit_report.md`.

# AI-use and research-integrity report (Prompt 18)

**Student:** Madhukar Kumar · MHM2026001 · IIIT Allahabad  
**Project:** Context-window degradation and its impact on long-document research synthesis  
**Study actually run:** evidence position (begin / middle / end) and citation behaviour on 12 short synthetic packets  
**Tool:** Cursor coding agent, in the project chat  
**Date:** 2026-11-13  
**Companion table:** `ai_assistance_log.md`

This report covers what the assistant did, what the researcher decided, and what was actually checked. It does not add debugging stories that are not in the project record.

## 1. What the assistant did

The assistant proposed the study design inside the literature-review topic (a controlled comparison of evidence position, called Pathway B in the course notes), scaffolded the Python pipeline, drafted the twelve synthetic packets, called the Groq API, scored the saved responses, drew the figures, and drafted the paper, the README, and the earlier audit. The researcher approved Gate G1 in chat, put the API key in `.env`, chose the model after asking about free APIs, asked for dummy dry-run folders to be deleted, chose the paper title, and chose to keep the generic article class rather than an ACM template.

The numbers in the paper are computed from `results/raw/run_20261030T142328Z`. They were not typed in by hand.

## 2. Three real limits of the assistance

**The first citation scorer was incomplete.** After the first real responses, the scorer was widened to accept full-width brackets and parentheses. That fix missed bold ids. In `item_05_middle.json` the model cited `**P2**` and `**P7**`, and the score table recorded no citations. Middle-position coverage looked like 0.92. A second check of the raw file against the score found it. Rescoring the saved files, with no new API calls, brought middle coverage to 1.00. One pass over the scorer was not enough.

**Dry-run folders were left where results live.** Early pipeline tests wrote `backend: dummy` and `model: dummy-v0` under `results/raw/`. The researcher opened those files, expected Groq, and asked what was going on. The folders were then deleted. The assistant had not separated practice output from the run that would be reported.

**A requested writing voice created a false provenance claim.** After the bold-citation miss was found, the researcher asked for the audit to be written as if a human reviewer had found the bug. The first `baseline_audit_report.md` said that. The researcher had said in chat that the run was verified, but the miss was found by the assistant, and no list of files the researcher opened was saved. That draft broke the assignment rule against fabricated debugging experiences. The report was corrected on 2026-11-13. The scores did not change.

## 3. Decisions that were the researcher’s

- Approving Gate G1 and asking to start coding.
- Choosing a free hosted model and placing the key locally. DeepSeek was discussed; the run that was kept uses `openai/gpt-oss-20b` on Groq.
- Asking for the dummy folders to be removed.
- Asking what “the expected middle drop is contradicted” means, and keeping the null result rather than a degradation claim.
- Choosing the title that starts with the review topic, and declining the ACM template.

The null-result reading itself was proposed by the assistant from the rescored table. The researcher accepted it after asking what it meant. It was not an independent recalculation.

## 4. What this shows about working with the assistant

Saying a run is verified, without naming the files read, left a scoring bug in the table that would have looked like the result the study expected. Asking the assistant to write in a reviewer’s voice made the paperwork agree with a story that had not happened. The useful checks were the ones with a file attached: one raw JSON against one score, a rescore of the same 36 files, and a compile of the paper.

The paper’s prose, the packet text, and most of the interpretation were drafted by the assistant. Owning them means reading them. That read-through is still open, including the 18 responses the keyword score marked wrong. The assistant read those 18; the researcher has not logged a separate reading.

## 5. Risks still open

- `search_log.md` still has unfilled rows. The introduction says the search did not turn up a study that varies evidence position and scores citations. That sentence should be changed if the log cannot support it.
- The git author email `mhm2026001@iiita.ac.in` was guessed because no git identity was configured. There is no remote yet.
- Whether the repository may be public, and whether MIT is acceptable, still needs the instructor.
- Temperature 0 does not make a rerun identical. The saved JSON files are the record.
- The two primary metrics do not check whether a cited passage actually supports the sentence it is attached to.
- A five-minute demo has not been prepared. The viva can ask for an explanation of `score.py`, the position assembly, and why coverage is 1.00 everywhere.

## 6. Bottom line

The experiment is a small logged comparison with a null result on citation support and evidence coverage. The assistant wrote most of the code and text. The researcher made the gate, model, deletion, and title decisions, and still needs to read the paper and the flagged responses before treating the draft as their own account of the work.

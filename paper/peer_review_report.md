# Prompt 16 — Technical Peer Review

**Manuscript:** `paper/main.pdf` (6 pages, compiled 2026-11-13; this review is of the first draft, before the later prose rewrite)  
**Reviewer stance:** Critical course reviewer (not a venue acceptance letter).

## Summary judgment
The paper is an honest controlled study with a clear negative/null primary result and reproducible artifacts. It is suitable as a **draft course paper**, but not yet a strong submission until related-work verification, LongCite author metadata, and GitHub packaging are finished.

---

## MAJOR concerns

| # | Location | Concern | Why it matters | Concrete remedy |
|---|---|---|---|---|
| M1 | Related Work / bib | LongCite entry has `and others` + `[TO VERIFY]` author list | Citation integrity | Open Anthology PDF; replace full author list |
| M2 | Related Work | Liu et al.\ methods not re-verified in depth in this draft | Risk of inaccurate paraphrase | Author reads TACL PDF; tighten 2–3 sentences with page cites |
| M3 | External validity | Short synthetic packets; saturated metrics | Readers may over-generalize the null | Already partly in Limitations—add one sentence in Abstract/Conclusion that transfer to long PDFs is untested |
| M4 | Repo submission (G4) | Paper exists locally; public GitHub + LICENSE not confirmed | Assignment item B incomplete | Init git remote; README reproduction checklist (Prompt 17) |

## MINOR concerns

| # | Location | Concern | Remedy |
|---|---|---|---|
| m1 | Metrics | Citation support ≠ span-level claim support | Rename in text to “gold-id citation rate” or note heuristic |
| m2 | Figures | Three figures for 6 pages is dense | Optional: move failure figure to appendix if page limit tight |
| m3 | Correctness trend | End lower than begin on keyword score | Already caveated; keep one explicit “do not interpret as LITM” sentence near Table 1 |
| m4 | Template | Generic `article`, not official ACM/IEEE class | Switch if instructor mandates a template |

## Unsupported claims check
- No SOTA or novelty claim found — **good**.  
- No claim that lost-in-the-middle is false in general — **good**.  
- Primary numbers match `g3_summary_by_position.csv` — **good**.

## Prioritized revision checklist
1. Fix LongCite BibTeX authors from Anthology.  
2. Author verify Liu/LongBench/RULER sentences against PDFs.  
3. Push GitHub-ready tree without `.env`.  
4. Optional harder-packet follow-up only if claiming broader positional conclusions.

## Author-response table (to fill after revisions)

| Reviewer item | Action taken | Evidence |
|---|---|---|
| M1 | LongCite author list replaced with the 11 authors shown on the ACL Anthology page (checked 2026-11-13); `[TO VERIFY]` note removed | `paper/references.bib`; https://aclanthology.org/2025.findings-acl.264/ |
| M2 | Related Work now states only what the Liu et al., LongBench, RULER and LongCite abstracts say (checked against the Anthology/arXiv pages 2026-11-13). Full PDFs were not re-read, so no effect sizes or page cites are given | `paper/main.tex` Section 2 |
| M3 | | |
| M4 | | |

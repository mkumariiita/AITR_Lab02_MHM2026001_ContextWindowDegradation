# Prompt 15 — Outline + Evidence Checklist

**Target:** 6–10 page implementation paper (course), ACM/IEEE-like `article` LaTeX.  
**Rule:** Claims must map to VERIFIED artifacts below; else mark `[TO VERIFY]`.

## Section order (drafting order ≠ reading order)

1. Related Work  
2. Methodology  
3. Experimental Setup  
4. Results  
5. Discussion  
6. Limitations  
7. Introduction  
8. Conclusion  
9. Abstract (last)

## Evidence checklist

| Claim area | Allowed source | Status |
|---|---|---|
| Topic / RQs | `research_brief_g1.md` | VERIFIED |
| Pathway B | G1 approval + `contribution_pathway.md` | VERIFIED |
| Model / decoding | `configs/experiment.yaml`, raw JSON meta | VERIFIED |
| Dataset | `data/packets/`, `data/README.md` (synthetic) | VERIFIED |
| Metrics definitions | `configs/protocol.md`, `src/position_citation/score.py` | VERIFIED |
| Main numbers | `results/tables/g3_summary_by_position.csv` | VERIFIED |
| Failure analysis | `failure_analysis.md`, `g3_failure_cases.csv` | VERIFIED |
| Figures | `paper/figures/fig_*.pdf` from real eval script | VERIFIED |
| Prior lit (positional) | Liu et al. TACL 2024 Anthology URL | cite; abstract-level claims checked against Anthology page 2026-11-13; full-PDF details not used |
| Prior lit (long-context benches) | LongBench, RULER URLs in bib | cite as related |
| LongCite | ACL 2025 page previously noted in gap matrix | cite carefully |
| Novelty / SOTA | — | **Do not claim** |
| Lost-in-the-middle confirmed here | — | **Contradicted** on this set |

## Files

- `paper/main.tex`
- `paper/references.bib`
- `paper/figures/`

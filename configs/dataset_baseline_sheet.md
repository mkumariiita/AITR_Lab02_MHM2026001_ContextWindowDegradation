# Prompt 06 — Dataset and baseline sheet (draft)

| Candidate | Official source to verify | Access | Compute | Pitfalls |
|---|---|---|---|---|
| LongBench-Cite / LongCite data | ACL page + author repo (human must find/confirm) | UNVERIFIED | Eval-only possible | License; size |
| Custom micro-corpus (chosen MVP) | `data/packets/` synthetic items | Local | Negligible | Not real papers; small N; annotation bias |
| Baseline: direct cite prompt | This repo `scripts/run_baseline.py` | Runnable (`dummy` now) | Low | Dummy ≠ real LLM |
| Comparator | Position begin/middle/end (same content) | Built-in | Low | Order/coherence confound |

**Recommendation:** Proceed with custom packets for coding; optionally swap in a public set later if license and download work.

**Leakage:** No training split; all items are evaluation. Do not tune prompt on the same items you will report (freeze prompt first; add new items if iterating).
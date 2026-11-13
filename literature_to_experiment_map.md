# Prompt 03 — Literature → Executable Experiment Map

**Topic:** Context-Window Degradation and Its Impact on Long-Document Research Synthesis  
**Inputs used:** Review paper + `research_gap_matrix.md` (G1–G5) + `research_decisions.md`  
**Hardware assumption (researcher-reported):** MacBook Air M2, 8 GB unified memory; free tools/models only; under ~2 weeks  
**Status:** AI-assisted draft for human approval. **Not** an authorized experiment start.

## Human-in-the-loop rule

| Role | Allowed | Not allowed |
|---|---|---|
| AI (this draft) | Propose methods, pathways, MVP, verification lists | Claim code/dataset access, novelty, or that baselines run |
| Human (you) | Read primary papers, check repos/licenses, pick pathway, sign below | Treat AI recommendations as verified fact |

**G1 cannot close until Section 7 is signed by you.**

---

## 1. Three methods from the review that could be implemented

Access claims below are **UNVERIFIED** until you personally open the official page/repo and confirm license, files, and runnable status.

### Method M1 — Positional long-context evaluation (“Lost in the Middle” style)

| Field | Content | Evidence status |
|---|---|---|
| Anchor paper (from review) | Liu et al., *Lost in the middle*, TACL 2024 | Cited in review; full methods still need human read |
| Official page to check | https://aclanthology.org/2024.tacl-1.9/ | Link from prior audit — **you** confirm |
| Algorithm (minimal) | Fix relevant evidence; permute its position (begin / middle / end); measure retrieval/QA performance | INFERRED simplification of the paper’s idea |
| Dataset (original) | Multi-document QA / key-value retrieval setups in the paper | MUST verify exact construction from original |
| Code / weights | Unknown until checked | **UNVERIFIED** — do not assume a public repo exists |
| Metrics (typical) | Accuracy / exact match / retrieval success vs position | Confirm from original; do not invent numbers |
| Known limits (review-level) | Positional bias ≠ full research synthesis | Review synthesis |
| Compute (MVP version) | Low if using a free hosted LLM API + short packets; high if local large models | Fits laptop better as API/prompt study |
| Feasibility under free-only + 8 GB | **High** for a *controlled position study* on a small hand-built set; **Low** for full-paper reproduction at original scale | INFERRED |

### Method M2 — Citation-supported long-context QA (LongCite / LongBench-Cite family)

| Field | Content | Evidence status |
|---|---|---|
| Anchor paper | Zhang et al., *LongCite*, Findings of ACL 2025 | VERIFIED at ACL abstract/page level in gap matrix |
| Official page to check | https://aclanthology.org/2025.findings-acl.264/ | You must inspect full paper + any linked code |
| Algorithm (minimal) | Require answers with sentence-level or span citations; score citation support | Simplified task design, not a claim to reimplement their full pipeline |
| Dataset | LongBench-Cite (as described by that paper) | Access/license **UNVERIFIED** |
| Code / weights | Unknown until checked | **UNVERIFIED** — full model training likely infeasible on M2 8 GB |
| Metrics | Citation precision/recall-style fidelity, answer quality (as defined by authors) | Confirm from original |
| Known limits | Citation presence ≠ evidence completeness; overlap with G2 | Prior audit |
| Compute | Training/finetuning: **not** realistic on stated hardware; evaluation-only may be possible if free API + small custom labels | INFERRED |
| Feasibility | **Medium** only if reframed as *evaluation protocol* on a tiny gold set, not model training | INFERRED |

### Method M3 — Retrieval / staged processing vs direct long context

| Field | Content | Evidence status |
|---|---|---|
| Anchor material in review | RAG / hierarchical synthesis sections; related work such as Lost in Decomposition (Guo et al., Findings ACL 2026) | Decomposition paper VERIFIED at abstract/page level only |
| Official page to check (related) | https://aclanthology.org/2026.findings-acl.2097/ | Human full-paper check required |
| Algorithm (minimal) | Condition A: put all passages in one prompt. Condition B: extract per document then synthesize | Prototype comparison, not a new architecture |
| Dataset | Small multi-document research packets (can be constructed and documented) | Construction allowed if labeled and reproducible; public benchmark preferred if accessible |
| Code | Implementable from scratch with free LLM API | No claim of matching published SOTA systems |
| Metrics | Evidence coverage, contradiction/limitation recall, supported-claim rate | Must be predefined before runs |
| Known limits | Broad “RAG vs long context” is heavily studied; G5 overlaps Lost in Decomposition | Prior audit — avoid broad novelty claims |
| Compute | Medium; annotation cost dominates | INFERRED |
| Feasibility | **Medium–high** for a tiny controlled set; weak as a novelty claim | INFERRED |

---

## 2. Pathway comparison (assignment Pathways A / B / C)

| Pathway | Study idea tied to your gaps | Smallest working baseline | Testable question | Resource burden | Evidence required | Fit for you |
|---|---|---|---|---|---|---|
| **A. Reproduction + extension** | Reproduce a positional or citation evaluation protocol, then add a research-synthesis twist (e.g. contradiction/method limitation citations) | Official or paper-faithful baseline on a reduced slice | Does the published positional/citation pattern hold under a synthesis-style gold checklist? | Medium–high (protocol fidelity hard) | Paper match checklist + discrepancy log | Only if you verify code/data access this week |
| **B. Controlled comparative study** *(recommended draft)* | Same model, same evidence content; vary **passage position** (and optionally distractor count); score citation support + evidence coverage | Direct prompt + “cite source spans” instruction | How do begin/middle/end positions affect evidence use and citation support on research-style questions? | Low–medium | Gold spans, frozen prompts, position permutations, scored outputs | Best under free-only + 2 weeks |
| **C. Targeted modification** | One change to a baseline (e.g. reorder evidence to front, or add an extract-then-cite stage) | Validated direct-context baseline first | Does one isolated change improve coverage/citation support without new training? | Medium (needs validated baseline first) | Ablation table; unchanged baseline preserved | Good later (G3 gate), after baseline validation |

**AI recommendation (INFERRED, not binding):** Pathway **B**, operationalizing candidate **G2** (position × citation support), with **G1** (coverage vs correctness) as a secondary metric on the same runs.

**Why not A first:** Full reproduction needs verified official code/data; access is still UNVERIFIED.  
**Why not C first:** Assignment Gate G2 requires a validated baseline before claiming benefit from a modification.

---

## 3. Mandatory bridge table (papers → method → baseline → planned test)

| Step | Selected content (draft) | Status | Human action |
|---|---|---|---|
| Original papers | (1) Liu et al. 2024 Lost in the Middle; (2) Zhang et al. 2025 LongCite; (3) optional Asai et al. OpenScholar/ScholarQABench for synthesis-metric vocabulary | Supporting literature, not all fully method-verified | Read methods + limitations; record page notes |
| Selected method family | Controlled positional evaluation + citation/evidence scoring | Candidate | Approve or replace |
| Executable baseline | Free LLM (version frozen later): single-pass answer with required source citations over a packed multi-passage context | Not implemented | Choose exact model/API; run sanity prompt |
| Planned test | Permute gold evidence to begin / middle / end; keep content identical; score evidence coverage + citation support (+ answer correctness) | Protocol not frozen | Freeze after Prompt 07; no result-peeking |

---

## 4. Minimum viable research experiment (MVP)

**Draft MVP title:** Position effects on citation-supported research synthesis under fixed evidence content.

**Procedure (conceptual — do not run until G1 signed + later protocol frozen):**

1. Build or select **N** small multi-passage packets (start N≈10–20) with a research-style question each.
2. Annotate **gold evidence spans** and optional contradicting/limitation spans (human labels).
3. For each item, create three contexts: relevant evidence at **begin**, **middle**, **end** (all other text fixed).
4. Query one frozen free model with a fixed prompt requiring claims + citations.
5. Score: (a) answer correctness, (b) evidence coverage, (c) citation support / attribution accuracy.
6. Compare positions under identical decoding settings; log seeds/temperature.

**Deep analysis later (Phase IV, not G1):** error cases where citation looks present but does not support the claim; or middle-position omission of contradictions.

**Fallback if LongCite data/code unavailable:** use a **documented custom micro-corpus** (your annotated packets) and cite LongCite / Lost in the Middle as *motivation and metric vocabulary*, not as unreproduced official scores.

---

## 5. What you must personally verify before coding

- [ ] Full methods of Liu et al. (2024) — tasks, lengths, position controls  
- [ ] Full methods of LongCite — citation unit, metrics, data license  
- [ ] Whether LongBench-Cite (or similar) is downloadable under your constraints  
- [ ] OpenScholar/ScholarQABench access **or** decide custom corpus is acceptable  
- [ ] Exact free model/API allowed by the course (name + version)  
- [ ] Whether a hand-built evaluation set is allowed (assignment allows domain-appropriate measurement; confirm with instructor if unsure)  
- [ ] No secrets in prompts; no copyrighted full papers redistributed if license forbids  
- [ ] Choose Pathway A / B / C explicitly (draft recommends B)  
- [ ] Choose primary gap G2 or switch to G1/G3 with written reason  

---

## 6. AI vs human accountability for this file

| Item | Produced by | Must be confirmed by human |
|---|---|---|
| Method shortlist M1–M3 | AI from your review/gap matrix | You: relevance + access |
| Pathway ranking | AI recommendation | You: final pathway choice |
| MVP design | AI draft | You: scientific ownership |
| Access/license of any repo or dataset | **Not verified here** | You: primary source check |
| Novelty | Explicitly UNKNOWN | You: search in Prompt 04 |

---

## 7. Human sign-off (required to use this map for G1)

I have read this map. I understand recommendations are not verified facts. I personally will verify the checklist in Section 5 before coding.

- **Pathway I choose:** B  
- **Primary gap I choose:** G2  
- **Fallback gap:** G1 metrics (coverage vs correctness) on same runs  
- **Name / date:** Madhukar Kumar / 2026-10-30  
- **Decision:** [x] Approve draft MVP   [ ] Revise (notes: _______________)   [ ] Reject  

**Signed via chat approval 2026-10-30. Coding may begin under Pathway B + G2; results still require real runs.**

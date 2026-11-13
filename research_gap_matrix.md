# Prompt 02 — Evidence-Based Research Gap Matrix

**Topic:** Context-Window Degradation and Its Impact on Long-Document Research Synthesis  
**Primary source:** Madhukar Kumar, *Context-Window Degradation and Its Impact on Long-Document Research Synthesis*, 11-page ACM-formatted review supplied in this conversation.  
**Status:** Candidate gaps only. No novelty claim; no experiment has been run.

## Evidence labels
- **VERIFIED (review):** Explicitly stated in the supplied review; not necessarily independently confirmed in the cited original paper.
- **VERIFIED (external abstract/article page):** Checked against a publisher/ACL Anthology page; detailed methods may still need inspection.
- **INFERRED:** Proposed interpretation or experiment derived from the review.
- **UNKNOWN / VERIFY:** Original methods, limits or metrics need checking.

## 1. Central methods, datasets and findings represented in the review

| Method family | Review location | Dataset / cited work | Finding represented by review | Caution |
|---|---|---|---|---|
| Long-context evaluation | §§4.1–4.3, pp. 3–4; refs [1], [3], [8], [10], [20] | LongBench, RULER, LooGLE, L-Eval, ∞Bench | Performance varies with task, length, complexity and long dependencies | Review argues these do not fully reproduce open-ended academic synthesis; verify original protocols |
| Positional retrieval / calibration | §§3.2, 5.1, pp. 2, 4; [9], [12] | Lost in the Middle; Found in the Middle | Relevant information may be harder to use from the middle; calibration targets positional bias | Research-synthesis/citation impact is an extrapolation unless tested directly |
| Retrieval / RAG / coarse-to-fine | §§5.2, 7.2, pp. 4–6; [14] | CAFE and multi-document QA | Retrieval can reduce distractors but can omit required evidence | Need both retrieval-recall and downstream synthesis metrics |
| Context extension and training/alignment | §5.3, p. 4; [2], [4], [7], [15] | Position Interpolation, LongAlign, long-context training | Extension/training can improve native long-context behavior | Compute cost and transfer; poor first implementation choice under a short deadline |
| Length degradation despite retrieval | §5.4, p. 4; [5] | Du et al., perfect-retrieval settings (as summarized) | Degradation may remain even when relevant evidence is retrieved | Verify exact controls, models, tasks and effect sizes in original paper |
| Compression / memory efficiency | §§5.5, 7.4, pp. 4, 6; [11], [13], [17] | Compression survey, KV-cache, StreamingLLM | Reduce input or inference burden | Efficiency does not imply synthesis reliability; compression may remove evidence |
| Hierarchical / evidence-centred synthesis | §§7.5, 8–11, pp. 6–9; [19] | LongCite / LongBench-Cite | Staged synthesis and fine-grained citations can improve traceability | Early omissions can propagate; citation presence is not citation support or complete coverage |

The review’s central question (Section 1, p. 1): “How does increasing context length affect information retrieval, reasoning, and synthesis performance in large language models, and what methods have been proposed to mitigate this degradation?”

The review’s own stated open challenges are in §§10.1–10.6, pp. 8–9: task-dependent effective context length; evaluating synthesis beyond answer accuracy; interaction among length, retrieval, compression and reasoning; human–AI collaboration; domain-specific effects; and degradation beyond retrieval failure.

## 2. Five computationally testable candidate gaps

### G1 — Evidence coverage versus answer correctness as context grows
- **Source evidence (VERIFIED in review):** §9.1, p. 7 says a synthesis can be locally correct but globally incomplete and motivates evidence coverage, contradiction detection and attribution. §10.2, p. 8 calls for coverage, citation accuracy, contradiction detection, methodological interpretation, attribution and completeness alongside accuracy.
- **Reported limitation vs inference:** The claim that existing benchmarks do not fully capture academic synthesis is the review author’s synthesis of the field, not a verified shared limitation of every original benchmark.
- **Candidate question (INFERRED):** If relevant evidence is held constant while irrelevant but plausible text is added, can answer correctness remain stable while required-evidence coverage falls?
- **Possible experiment:** Create a small set of research-style questions with manually annotated required evidence. Hold relevant passages constant; vary distractor volume and evidence position. Score answer correctness separately from evidence coverage (gold evidence items correctly used / required items).
- **Evidence needed:** Gold evidence checklist, controlled context conditions, outputs, correctness labels, coverage scores and paired comparisons.
- **Feasibility:** High for a small hand-labelled dataset. **Confound:** added text changes more than token count unless distractors are controlled.
- **Novelty:** UNKNOWN; scientific-synthesis benchmarks already evaluate coverage.

### G2 — Passage position versus citation support in multi-document synthesis
- **Source evidence (VERIFIED in review):** §§3.2 and 5.1, pp. 2, 4 discuss positional effects; §9.3, pp. 7–8 argues traceability should be part of synthesis quality; ref. [19] is LongCite.
- **Reported limitation vs inference:** Positional retrieval effects are represented as prior-study findings. Applying them specifically to citation-supported research synthesis is an inference unless the original paper directly tests it.
- **Candidate question (INFERRED):** With evidence and prompt content unchanged, does moving a supporting or contradicting passage from the beginning/end to the middle change evidence use and citation support?
- **Possible experiment:** Use 20–40 short source packets or a controlled corpus. Permute passage order (relevant evidence at beginning, middle, end); ask a model for claims with source-span citations. Score citation correctness, claim support and evidence recall.
- **Evidence needed:** Position permutations, gold source spans, outputs, support labels, repeated runs if stochastic.
- **Feasibility:** High–medium; annotation is the main cost. **Confound:** order can change local coherence; keep templates and all content fixed.
- **Novelty:** UNKNOWN; LongCite studies fine-grained citation generation and positional-bias studies already exist. Search the intersection.

### G3 — Hierarchical synthesis and loss of methodological qualifications
- **Source evidence (VERIFIED in review):** §7.5, p. 6 says early-summary omissions can propagate; §11, p. 9 calls for controlled studies of interactions between retrieval, compression, calibration and hierarchical synthesis.
- **Reported limitation vs inference:** This is a review-level hypothesis/risk, not a specific effect size verified from one cited experiment.
- **Candidate question (INFERRED):** Compared with direct synthesis, does staged per-document extraction followed by synthesis omit more limitations, qualifications or contradictory findings as source count grows?
- **Possible experiment:** Compare direct synthesis with two-stage synthesis on the same small source set and fixed prompts. Score a gold checklist of findings, limitations, methods and contradictions.
- **Evidence needed:** Gold labels, intermediate summaries, final outputs, omission/error-propagation labels and comparable prompt/token budgets.
- **Feasibility:** Medium–high to implement; annotation is time-consuming. **Confound:** unequal context/prompt budgets can bias results.
- **Novelty:** UNKNOWN; hierarchical synthesis is established.

### G4 — Retrieval recall versus synthesis completeness under distractors
- **Source evidence (VERIFIED in review):** §5.2, p. 4 says retrieval can omit important evidence; §7.2, pp. 5–6 describes RAG’s dependence on retrieval; §10.6, p. 9 recommends separating evidence access, organization and reasoning.
- **Reported limitation vs inference:** The trade-off is summarized in the review; the proposed factor separation is the review author’s framing.
- **Candidate question (INFERRED):** Is synthesis quality more sensitive to omission of one required passage or to adding many irrelevant passages?
- **Possible experiment:** Controlled conditions: (a) all gold evidence plus distractors, (b) one required evidence item omitted, (c) fixed top-k retrieval. Measure retrieval recall, supported-claim rate, coverage and contradiction handling.
- **Evidence needed:** Gold passage IDs, recall@k, distractor counts, output support labels, stratified results.
- **Feasibility:** Medium; needs a retriever or controlled evidence selection. **Confound:** missing evidence may make an answer impossible; reward calibrated abstention.
- **Novelty:** UNKNOWN; RAG and multi-document QA are heavily studied.

### G5 — Context dependency as a moderator of direct versus decomposed processing
- **Source evidence (VERIFIED in review):** §11, p. 9 calls for compositional evaluation; §12, p. 9 warns its conceptual framework is not a deterministic causal model.
- **Reported limitation vs inference:** The review motivates interaction testing but does not operationalize context dependency or report a controlled experiment for it.
- **Candidate question (INFERRED):** Does decomposed processing help more when evidence items are independent than when conclusions depend on relations across distant passages?
- **Possible experiment:** Build paired tasks of similar length: independent-fact tasks and cross-passage dependency tasks. Compare direct-context and staged extraction/synthesis. Score correctness, evidence coverage and relation preservation.
- **Evidence needed:** Dependency labels, fixed lengths, output records and gold evidence/relation labels.
- **Feasibility:** Medium; fair task construction is challenging. **Confound:** dependency may correlate with difficulty, ambiguity or length.
- **Novelty:** UNKNOWN; must check recent work on context-dependency-aware routing.

## 3. Preliminary ranking of three candidates

Scores are planning judgments, not measured results. Scale 1–5; resource fit assumes a MacBook Air M2 with 8 GB RAM, free-only model/API access and under two weeks.

| Rank | Candidate | Significance | Resource fit | Implementation feasibility | Reason / caveat |
|---:|---|---:|---:|---:|---|
| 1 | G2: position × citation support | 4 | 5 | 5 | Tight controlled variable and measurable output; overlap with LongCite/positional literature needs checking |
| 2 | G1: correctness × evidence coverage | 5 | 4 | 4 | Central synthesis-reliability question; manual labels and existing benchmarks limit novelty claims |
| 3 | G3: hierarchical loss of qualifications | 4 | 5 | 4 | Straightforward prototype and interpretable errors; must control budgets and acknowledge established methods |

G4 and G5 remain alternatives. G5 may be conceptually interesting but is riskier to operationalize within the time limit.

## 4. Verification queue for original publications

The following claims should be checked in full papers/method sections before choosing a gap. A bibliography entry in the review does not by itself verify the summary of its findings.

1. **Lost in the Middle**, Liu et al. (2024), review ref. [12]: https://aclanthology.org/2024.tacl-1.9/ — verify task settings, context lengths, models, positional controls and relevance to synthesis.
2. **Found in the Middle**, Hsieh et al. (2024), [9]: https://aclanthology.org/2024.findings-acl.890/ — verify calibration method, baselines, generalization and cost.
3. **LongBench**, Bai et al. (2024), [3]: https://aclanthology.org/2024.acl-long.172/ — verify task composition, scoring and overlap.
4. **RULER**, Hsieh et al. (2024), [8]: https://arxiv.org/abs/2404.06654 — verify task-generation and length-scaling protocol.
5. **LooGLE**, Li et al. (2024), [10]: https://aclanthology.org/2024.acl-long.859/ — verify long-dependency tasks and scoring.
6. **L-Eval**, An et al. (2024), [1]: https://aclanthology.org/2024.acl-long.776/ — verify task types, annotation and scoring limitations.
7. **Context Length Alone Hurts LLM Performance Despite Perfect Retrieval**, Du et al. (2025), [5]: https://arxiv.org/abs/2510.05381 — verify paper status/version, controls, model list and meaning of “perfect retrieval.”
8. **CAFE**, Peng et al. (2025), [14], DOI 10.18653/v1/2025.emnlp-main.655 — verify method, baselines and limits.
9. **LongCite**, Zhang et al. (2025), [19]: https://aclanthology.org/2025.findings-acl.264/ — **VERIFIED at abstract/page level:** introduces LongBench-Cite and fine-grained sentence-level citations. Citation fidelity alone is not an unaddressed gap.
10. **OpenScholar / ScholarQABench**, Asai et al. (Nature, 2026): https://doi.org/10.1038/s41586-025-10072-4 — **VERIFIED at article-page level:** scientific synthesis is evaluated with coverage, coherence, writing quality, factual correctness and citation accuracy. The paper reports limits including expert-evaluation size and disciplinary coverage. Do not claim no scientific-synthesis benchmark exists.
11. **ConfRAG**, Yuan et al. (ACL 2026): https://aclanthology.org/2026.acl-long.11/ — **VERIFIED at abstract/page level:** benchmark for conflicting web references with answer-coverage and reason-coverage tasks. Do not claim contradiction-aware reasoning has never been benchmarked.
12. **Lost in Decomposition**, Guo et al. (Findings ACL 2026): https://aclanthology.org/2026.findings-acl.2097/ — **VERIFIED at abstract/page level:** reports workflow methods do not generalize uniformly and decomposition can hurt documents with strong context dependency; proposes CoDaR. This is directly relevant to G5.

## 5. What is and is not established

- **VERIFIED from review:** it identifies mechanisms, benchmark families, mitigation families and six open-challenge themes.
- **INFERRED:** the five experiments above operationalize possible parts of those themes.
- **UNKNOWN:** which candidate is novel; which can be run entirely offline with a suitable model; and whether the assignment expects a new dataset, implementation artifact or experimental study.
- **No novelty claim is made.** Next: inspect the selected candidate’s original methods and conduct a focused related-work search before locking the research question.

## 6. Recommended next action

Start with **G2 (position × citation support)** as a controlled pilot candidate, keeping G1 as the broader backup. Inspect LongCite, Lost in the Middle and OpenScholar/ScholarQABench first. If overlap is too direct, narrow to a specific failure mode (e.g. citations for methodological qualifications or contradictions) only if the literature audit confirms the exact evaluation is not already covered.

**Reproducibility note:** No models were run, no dataset was constructed and no performance values were generated for this analysis.

## 7. Source-verification audit (updated 22 October 2026)

This section separates sources whose publisher/official pages were inspected in this pass from sources that remain in the verification queue. “Page checked” means bibliographic metadata and the accessible abstract/article text were checked; it does **not** mean every experiment, table, appendix, or limitation has been independently reproduced.

| Work | Verification status in this pass | What can safely be stated | What must not be claimed yet |
|---|---|---|---|
| Zhang et al., **LongCite** (Findings of ACL 2025), https://aclanthology.org/2025.findings-acl.264/ | **VERIFIED at official abstract/page level** | The paper introduces LongBench-Cite for long-context QA with citations and a pipeline/dataset for fine-grained sentence-level citations. | Do not claim citation generation or citation evaluation is absent from prior work. Inspect full evaluation details before making narrower comparisons. |
| Asai et al., **OpenScholar / ScholarQABench**, Nature, https://www.nature.com/articles/s41586-025-10072-4 | **VERIFIED at article-page level** | The article introduces OpenScholar and ScholarQABench for open-ended scientific, multi-paper synthesis; it describes evaluation of correctness, citation accuracy, coverage and other response qualities. It reports limitations involving the size/cost of expert evaluation, automatic scoring, and domain coverage. | Do not claim no benchmark evaluates scientific synthesis, citation accuracy or coverage. Do not assume the benchmark directly tests the exact position manipulation proposed in G2. |
| Guo et al., **Lost in Decomposition** (Findings of ACL 2026), https://aclanthology.org/2026.findings-acl.2097/ | **VERIFIED at official abstract/page level** | The paper studies cross-dataset generalization of long-context workflows and reports that decomposition can hurt performance for documents with strong context dependency; it proposes CoDaR. | Do not present context dependency or decomposition failure as an unexplored general phenomenon. Inspect task definitions, baselines and overlap before using G5. |
| Tang et al., **L-CiteEval: A Suite for Evaluating Fidelity of Long-context Models** (ACL 2025), https://aclanthology.org/2025.acl-long.263/ | **VERIFIED at official abstract/page level; newly added related work** | The paper introduces an evaluation suite for generation quality and fidelity across 11 tasks and 8K–48K contexts. | Do not frame long-context fidelity evaluation as missing generally. Check how its task suite and metrics overlap with G1/G2. |
| Liu et al., **Lost in the Middle** (TACL 2024), https://aclanthology.org/2024.tacl-1.9/ | **Cited in supplied review; detailed-method verification pending in this pass** | The supplied review describes positional retrieval degradation. | Do not report exact effect sizes, model-specific claims, or transfer to citation-supported synthesis without checking the paper. |
| Hsieh et al., **Found in the Middle** (Findings of ACL 2024), https://aclanthology.org/2024.findings-acl.890/ | **Cited in supplied review; detailed-method verification pending in this pass** | The supplied review describes positional calibration as a mitigation. | Do not assert broad generalization beyond the evaluated settings without checking the original. |
| LongBench, RULER, LooGLE, L-Eval, CAFE, and Du et al. | **Bibliography/review claims identified; original methods require detailed audit** | The supplied review names these benchmarks/methods and summarizes their roles. | Do not quote exact performance values or make detailed comparative claims based solely on the review's summary. For Du et al., verify version/status and exact definition of “perfect retrieval.” |

### Revised interpretation after source checks

1. **G1 is not a claim that scientific-synthesis coverage has never been evaluated.** ScholarQABench already evaluates coverage and citation-related quality. A defensible question would need a narrower independent variable (for example, controlled distractor volume or evidence position) and a transparent comparison to existing metrics.
2. **G2 is not a claim that citation fidelity or positional bias has never been studied.** LongCite and L-CiteEval cover citation/fidelity evaluation, while Lost in the Middle covers position-sensitive use of context. G2 is only a candidate intersection—controlled passage-position manipulation with a pre-annotated research-synthesis evidence set—and its novelty remains **UNKNOWN** until the full methods and adjacent literature are checked.
3. **G3 is not a claim that hierarchical synthesis is new.** It is a proposed controlled error-analysis study of omissions of methodological qualifications/contradictions under a defined source set. Its value depends on whether the experimental control and target failure mode add something beyond existing evaluations.
4. **G5 has direct overlap with Lost in Decomposition.** It should not be selected in its broad form. Only retain it if full-paper comparison reveals a clearly distinct, feasible research-synthesis-specific question.

## 8. Submission-readiness checklist

Before presenting a selected gap as “verified” or writing a novelty claim, complete these checks:

- [ ] Read the full methods, evaluation and limitations sections of the closest original papers, not just abstracts or this review.
- [ ] Confirm all cited paper metadata, benchmark names, dataset counts and task descriptions from official proceedings/publisher pages.
- [ ] Build a comparison table of the closest 5–10 papers: task, dataset, controlled variable, metrics, baselines, reported limitations, and overlap with the proposed question.
- [ ] Search for work published after the review’s literature cutoff, especially papers on long-context fidelity, citation evaluation, scientific synthesis, and decomposition/context dependency.
- [ ] Finalize the exact question only after the overlap analysis; state “candidate gap” until then.
- [ ] Specify the source corpus, gold labels, metrics, baselines, prompt/model version, repeat policy, and analysis plan before running experiments.
- [ ] Report results only from executed experiments, including negative or inconclusive results.

**Current conclusion:** This is a source-grounded *candidate gap matrix*, not yet a fully verified novelty claim or a completed experimental protocol. The highest-confidence output at this stage is the map from the supplied review to testable questions and the explicit list of original-paper checks still required.

## 7. Evidence-verification audit trail

This section distinguishes source inspection from inference so the matrix can be used as an accountable research artifact.

| Claim / artifact | Status | What was actually checked | Remaining verification |
|---|---|---|---|
| Scope and central question of the supplied review | VERIFIED against review | Full extracted text of the 11-page review; section and page locations used in this matrix | Original cited studies must be checked before attributing specific limitations to their authors |
| LongCite / LongBench-Cite studies fine-grained citations | VERIFIED at ACL Anthology abstract/page level | https://aclanthology.org/2025.findings-acl.264/ | Read full paper for task definition, metrics, baselines and stated limitations |
| ScholarQABench / OpenScholar evaluates scientific synthesis | VERIFIED at publisher article-page level | https://doi.org/10.1038/s41586-025-10072-4 | Inspect full methods and supplementary material before detailed metric comparison |
| ConfRAG addresses conflicting-source reasoning | VERIFIED at ACL Anthology abstract/page level | https://aclanthology.org/2026.acl-long.11/ | Inspect dataset construction, coverage metrics and benchmark limitations |
| Lost in Decomposition addresses context dependency and decomposition trade-offs | VERIFIED at ACL Anthology abstract/page level | https://aclanthology.org/2026.findings-acl.2097/ | Inspect full paper before using it to justify or reject G5 |
| Original methods/limitations for all other references in the review | NOT YET FULLY VERIFIED | Review bibliography and review-level summaries were inspected; some primary-source pages/abstracts were checked | Read the relevant full papers and record exact passage/page for each claim used in the final proposal |
| Novelty of G1–G5 | UNKNOWN | Preliminary audit only | Search the final narrowed question, compare tasks/metrics/datasets/methods, and record queries, date, inclusion criteria and near matches |
| Experiments or results | NOT RUN | No code, dataset evaluation, or model run was performed for Prompt 02 | Do not report metrics or claim empirical support until executed and logged |

**Interpretation rule:** “Author-reported limitation” may be used only when the original paper explicitly reports it. A limitation inferred from the review's cross-paper synthesis must be labelled “review author's synthesis” or “our inference,” not attributed to an original author. All five gaps remain candidates, not novelty claims.

## 8. What would make this matrix publication-ready

1. Open the full original papers for the three nearest matches to the selected candidate.
2. Record exact sections/pages and the original authors' own limitations, separately from our interpretation.
3. Run and record a focused search for the exact candidate question; log query strings, search date, included and excluded near matches.
4. Narrow to one research question, one primary baseline, one comparison, and pre-defined metrics.
5. Freeze the dataset/annotation protocol and evaluation criteria before interpreting results.

Until these steps are complete, this file is a transparent gap-analysis draft, not a claim that all cited research has been exhaustively verified.

# Research Workspace: Context-Window Degradation and Long-Document Research Synthesis

**Researcher:** Madhukar Kumar\
**Affiliation:** Department of Human Machine Interaction and Immersive
Technologies, IIIT Allahabad\
**Workspace status:** Phase I drafts complete (Prompts 01–05); Gate G1
pending **human sign-off** (not AI-closed)\
**Last updated:** 2026-10-30

## Evidence labels

-   **VERIFIED** --- directly supported by an inspected source, file,
    reproducible output, or observed result.
-   **INFERRED** --- a reasoned interpretation or proposal that has not
    yet been empirically confirmed.
-   **UNKNOWN** --- information not yet supplied or verified.

## 1. Existing documents and review scope

**VERIFIED --- user-designated documents** - Review paper:
`Madhukar_Kumar_MHM2026001_Review_Paper.pdf.pdf` (13 pages). - Research
paper: `Madhukar_Kumar_MHM2026001_Overleaf_Final_Paper(3).pdf` (11
pages, ACM format).

**VERIFIED --- topic:** "Context-Window Degradation and Its Impact on
Long-Document Research Synthesis."

**VERIFIED --- review question:** "How does increasing context length
affect information retrieval, reasoning, and synthesis performance in
large language models, and what methods have been proposed to mitigate
this degradation?"

**VERIFIED --- covered scope:** context capacity versus effective
utilization; lost-in-the-middle and positional effects; retrieval
degradation and distractors; evidence coverage and cross-document
reasoning; long-context benchmarks (LongBench, RULER, LooGLE, L-Eval,
and ∞Bench); context extension, positional calibration, long-context
training/alignment, retrieval-augmented generation, context compression,
memory efficiency, hierarchical synthesis, and evidence/citation
tracking; implications, research gaps, and future directions.

The 11-page ACM document contains a literature synthesis, comparative
tables, a mitigation taxonomy, a conceptual framework, and research
gaps. **Based on the inspected content, it reads as a review and does
not establish that a new implementation or experiment has been
completed.** This describes the document, not any separate work.

## 2. Feasibility constraints

**VERIFIED --- supplied by researcher** - Compute: MacBook Air M2, 8 GB
unified memory. - OS: macOS (host reported ProductVersion 26.3.1 on
2026-10-30). - Model/API constraints: free tools/models only. - Time
available: under two weeks. - Existing implementation: none reported.

**VERIFIED --- assignment file now available:**
`AI_Tools_for_Research_post_mid_sem_assignment.pdf` (AI-assisted coding,
evidence-based experimentation). Continuity from literature review →
verified gap → question → baseline → experiment → paper. Gates G1–G4;
Phase I = Prompts 01–05; Pathway A/B/C/D; human ownership and no
fabricated results.

**UNKNOWN:** Exact Classroom deadline; whether Colab/other hosted
notebooks are permitted; final free model/API the course accepts;
public dataset license access for LongCite-related data.

**INFERRED --- feasibility implication:** Prefer a small, controlled
evaluation (Pathway B) using free LLM access, a limited annotated set,
and measurable citation/coverage metrics. Training a long-context model
is not realistic on 8 GB within two weeks.

**Human-in-the-loop policy (2026-10-30):** AI may draft logs, matrices,
and briefs. AI may **not** close G1, claim novelty, claim dataset/code
access, or report experimental results. The researcher must verify
primary papers, sign G1, and own all scientific decisions.

## 3. Initial literature-gap audit

This is a preliminary audit based on bibliographic/abstract-level web
evidence, not a complete systematic search. It can reject overly broad
gap claims but cannot establish novelty by itself.

### Candidate gap A --- citation and evidence traceability

-   **Review's concern:** Long-context answers need traceable evidence
    and reliable citation support.
-   **Verified external evidence:** Zhang et al., *LongCite: Enabling
    LLMs to Generate Fine-grained Citations in Long-Context QA*,
    Findings of ACL 2025, introduces LongBench-Cite and sentence-level
    citation generation. Source:
    https://aclanthology.org/2025.findings-acl.264/
-   **Assessment:** The broad claim that fine-grained citation
    evaluation is absent is not defensible.
-   **Status:** VERIFIED that relevant prior work exists; UNKNOWN
    whether a narrower practical gap remains.
-   **Next action:** Inspect its task definition, metrics, baseline,
    dataset access, and limitations before considering a replication or
    extension.

### Candidate gap B --- contradiction-aware synthesis

-   **Verified external evidence:** *Benchmarking LLM's Capability in
    Reasoning over Conflicting Web References* introduces ConfRAG, with
    real-world questions paired with multiple retrieved paragraphs and
    tasks for answer clustering, answer coverage, and reason coverage.
    Source: https://aclanthology.org/2026.acl-long.11/
-   **Assessment:** Contradiction handling and coverage are already
    explicit research directions; they cannot be presented as unstudied.
-   **Status:** VERIFIED that a relevant benchmark exists; UNKNOWN
    whether its data/code are accessible and suitable for this project.
-   **Next action:** Inspect dataset license/access, resource needs,
    evaluation instructions, and limitations.

### Candidate gap C --- scientific literature synthesis

-   **Verified external evidence:** *Synthesizing scientific literature
    with retrieval-augmented language models* reports ScholarQABench for
    open-ended scientific synthesis, including expert-written answers
    and human rubric-based evaluation. Source:
    https://doi.org/10.1038/s41586-025-10072-4
-   **Assessment:** The broad claim that scientific synthesis lacks
    dedicated benchmarks is not defensible.
-   **Status:** VERIFIED that relevant prior work exists; UNKNOWN
    whether a smaller, reproducible evaluation can test a distinct
    question.
-   **Next action:** Inspect the paper and benchmark protocol before
    defining a contribution.

### Candidate gap D --- decomposition and context dependency

-   **Verified external evidence:** Guo et al., *Lost in Decomposition:
    Analyzing and Mitigating the Limitations of Long Context Methods via
    Context Dependency*, Findings of ACL 2026, reports cross-dataset
    variability in long-context methods and analyzes failure on
    documents with strong context dependency. Source:
    https://aclanthology.org/2026.findings-acl.2097/
-   **Assessment:** A generic comparison of direct long-context
    prompting and RAG/decomposition is not enough to claim novelty
    without a precise question and careful relation to this work.
-   **Status:** VERIFIED that related work exists; UNKNOWN whether a
    feasible replication or bounded extension is justified.
-   **Next action:** Inspect full method, datasets, metrics, and
    reproducibility materials.

### Preliminary conclusion from gap audit

**VERIFIED:** Several broad gaps stated in the existing review overlap
with work published by 2025--2026.\
**INFERRED:** A defensible near-term project may be a bounded
replication or controlled evaluation of existing approaches, rather than
a claim to invent a new architecture.\
**UNKNOWN:** No final research gap or novel contribution has been
established. The sources above have not yet all been read in full, and
code/data feasibility has not been checked.

## 4. Candidate direction (not yet accepted)

**INFERRED --- candidate only:** Compare direct prompting against one
simple document-processing strategy on a small, controlled set of
research questions. Measure evidence coverage and citation support using
a predefined rubric and source spans.

Potential research question, pending literature and feasibility checks:

> On a small, controlled set of long-document research questions, how do
> direct-context and a specified structured document-processing baseline
> differ in evidence coverage and citation support under free-tool
> constraints?

This is not yet a final research question. It must be narrowed to a
specific corpus, method, baseline, metric definitions, and reproducible
protocol. It must not be described as novel until a stronger literature
audit supports that claim.

## 5. Initial research decisions

### RD-001 --- Keep the two papers distinct

-   **Decision:** Use the 13-page PDF as the review paper and the
    11-page ACM PDF as the user-designated research paper.
-   **Reason:** The researcher explicitly identified them this way.
-   **Evidence:** User clarification and inspected PDFs.
-   **Status:** VERIFIED as file designation; the 11-page document's
    current content reads as a review.
-   **Next action:** Audit both documents without assuming
    implementation results exist.

### RD-002 --- Start from the existing review

-   **Decision:** Use the review's actual scope and references as the
    starting point.
-   **Reason:** The assignment asks to convert the literature review
    into implementation-based research.
-   **Evidence:** Supplied PDFs and Prompt 01.
-   **Status:** VERIFIED.
-   **Next action:** Extract and verify candidate gaps against primary
    literature.

### RD-003 --- Do not claim an implementation exists

-   **Decision:** Treat implementation, dataset, baseline, and
    experimental results as not yet established.
-   **Reason:** The researcher reported no existing implementation and
    supplied no dataset or results.
-   **Evidence:** Researcher's implementation-status response.
-   **Status:** VERIFIED that no implementation was reported; other
    details remain UNKNOWN.
-   **Next action:** Establish resources and choose a feasible task.

### RD-004 --- Label claims by evidence status

-   **Decision:** Mark consequential claims VERIFIED, INFERRED, or
    UNKNOWN.
-   **Reason:** Prevent assumptions from being mistaken for evidence.
-   **Evidence:** Prompt 01.
-   **Status:** VERIFIED.
-   **Next action:** Use the labels throughout the audit, experiment
    plan, results, and manuscript.

### RD-005 --- Do not finalize the research gap yet

-   **Decision:** Keep evidence-centered synthesis and small-scale
    baseline comparisons as candidate directions only.
-   **Reason:** A stated gap is not automatically novel, feasible, or
    testable, and recent related work exists.
-   **Evidence:** Existing review plus LongCite (ACL 2025), ConfRAG (ACL
    2026), ScholarQABench-related scientific synthesis work, and Lost in
    Decomposition (ACL 2026), linked above.
-   **Status:** INFERRED.
-   **Next action:** Read relevant papers in full, verify dataset/code
    access, and check assignment requirements.

### RD-006 --- Assignment requirements incorporated

-   **Decision:** Treat
    `AI_Tools_for_Research_post_mid_sem_assignment.pdf` as the
    governing brief for Lab 02 / post mid-sem work.
-   **Reason:** User supplied the official assignment; Phase I and Gate
    G1 are defined there.
-   **Evidence:** PDF inspected 2026-10-30 (learning outcomes, pathways,
    gates, prompts 01–18, submission package).
-   **Status:** VERIFIED that the file exists and was read for planning;
    UNKNOWN exact Classroom deadline.
-   **Next action:** Human completes G1 sign-off checklists.

### RD-007 --- Draft Gate G1 package (AI-assisted; human must approve)

-   **Decision:** Propose Pathway **B** + gap **G2** (position ×
    citation support), with G1 metrics secondary; document in
    `literature_to_experiment_map.md`,
    `novelty_feasibility_matrix.md`, and `research_brief_g1.md`.
-   **Reason:** Fits free-only + M2 8 GB + ~2 weeks; stays continuous
    with the review; avoids claiming unstudied citation/synthesis
    fields.
-   **Evidence:** Prompt 02 ranking; assignment Pathway B definition;
    hardware constraints.
-   **Status:** INFERRED recommendation only. **G1 not closed until
    human signs `research_brief_g1.md` Section 8.**
-   **Next action:** Researcher verifies Liu + LongCite methods, starts
    Prompt 04 search log, chooses model/data, signs G1 or revises.

### RD-008 --- AI-assisted, not AI-dependent

-   **Decision:** All Phase I artifacts are scaffolds. No coding or
    result claims proceed on AI authority alone.
-   **Reason:** Assignment ownership, integrity rules, and user request
    for human-in-the-loop.
-   **Evidence:** Assignment §§2, 10; user instruction 2026-10-30.
-   **Status:** VERIFIED as process rule.
-   **Next action:** Keep sign-off blocks on every gate.

## 6. Current state

  -----------------------------------------------------------------------
  Item                    Status                  Notes
  ----------------------- ----------------------- -----------------------
  Topic                   VERIFIED                Context-window
                                                  degradation and
                                                  long-document research
                                                  synthesis

  Review scope            VERIFIED                Summarized above from
                                                  supplied PDFs

  Existing implementation VERIFIED                Researcher reports none

  Compute constraints     VERIFIED                Laptop; free-only
                                                  tools; under two weeks

  Final research gap      INFERRED draft         G2 proposed; human must
                                                  approve in G1 brief

  Experiment-ready        INFERRED draft         See research_brief_g1.md
  research question                               RQ1–RQ2; not signed

  Dataset/document corpus UNKNOWN                 Public vs custom
                                                  undecided

  Model/API/local model   UNKNOWN                 Free model not frozen

  Baseline                INFERRED draft         Direct cite-required
                                                  prompt; not implemented

  Proposed study path     INFERRED draft         Pathway B (controlled
                                                  comparison)

  Evaluation metrics      INFERRED draft         Citation support +
                                                  evidence coverage +
                                                  correctness

  Laptop specifications   VERIFIED (reported)     M2, 8 GB; macOS host

  Assignment PDF          VERIFIED                Read 2026-10-30;
                                                  Classroom deadline
                                                  still UNKNOWN

  Gate G1                 APPROVED (2026-10-30)   Pathway B + G2; human
                                                  chat approval recorded

  Code repository         UNKNOWN                 None supplied

  Experimental results    UNKNOWN                 No results reported or
                                                  supplied
  -----------------------------------------------------------------------

## 7. Next actions (human-owned first)

1.  **Human:** Sign or revise `research_brief_g1.md` Section 8 (closes
    G1).
2.  **Human:** Read Liu et al. (2024) and LongCite (2025) methods;
    tick verification boxes.
3.  **Human:** Run Prompt 04 search strings; save a short search log
    (date, query, keep/drop).
4.  **Human:** Decide public dataset vs custom micro-corpus; check
    license.
5.  **Human:** Choose the free model/API allowed for the course.
6.  Only after G1 approval: Phase II (Prompts 06–07) — dataset sheet +
    frozen protocol — still with human checkpoints.
7.  Do not implement baselines until environment test output is real
    (Prompt 08).
8.  Update this log when decisions change, explaining why.

## 8. Questions requiring answers

-   What is the Google Classroom deadline?
-   Laptop: MacBook Air M2, 8 GB; macOS confirmed on host 2026-10-30.
-   Are free hosted notebooks (e.g. Colab) allowed?
-   Public dataset required, or is a documented custom evaluation set
    acceptable? (Assignment allows rigorous domain-appropriate
    measurement; confirm if unsure.)
-   Which free model/API must or may be used?

## 9. Reproducibility rules

-   Keep sources, datasets, code, configurations, logs, and raw outputs
    identifiable.
-   Record exact model/version, prompts, context length, decoding
    settings, retrieval settings, random seeds where applicable, and
    evaluation scripts.
-   Define metrics before examining final outcomes where practical.
-   Distinguish published findings from results reproduced in this
    project.
-   Never invent DOI/URL details, scores, baselines, execution claims,
    or metrics.
-   Preserve failed runs when they explain design changes.

## 10. Change log

-   **2026-10-22:** Initial workspace and decision log created from the
    two supplied PDFs, assignment prompt, and researcher's report that
    no implementation exists.
-   **2026-10-22:** Added feasibility constraints (laptop, free-only
    tools, under two weeks; deadline/rubric unknown) and preliminary
    external literature-gap audit. No final research gap or method
    selected.
-   **2026-10-22:** Recorded user-confirmed hardware: MacBook Air M2,
    8 GB unified memory. This favors small local workloads and lightweight
    evaluation; hosted compute/API access remains subject to free-tier
    availability and assignment rules.
-   **2026-10-30:** Assignment PDF incorporated. Phase I Prompt 03–05
    drafts added (`literature_to_experiment_map.md`,
    `novelty_feasibility_matrix.md`, `research_brief_g1.md`). Proposed
    Pathway B + G2. macOS confirmed on host. **Gate G1 remains open
    until human sign-off.** Policy: AI-assisted, human-approved.
-   **2026-10-30:** Human approved G1 (Pathway B + G2) and requested
    coding. Created `AITR_Lab02_MHM2026001_ContextWindowDegradation/`
    (renamed from PositionCitation to match research topic) with
    protocol, synthetic packets, assemble/score/LLM modules, env_test,
    and dummy baseline runner. Real free-API model still UNKNOWN /
    human choice. Dummy metrics are not scientific results.
-   **2026-10-30 (later):** Groq `openai/gpt-oss-20b` frozen via `.env`.
    Phase status: **Phase III** (Prompts 08–11 / toward Gate G2).
    Expanded corpus to 12 packets; full baseline re-run pending/logged
    in Lab02 `results/`.
-   **2026-10-30 (evening):** Renamed lab folder to
    `AITR_Lab02_MHM2026001_ContextWindowDegradation`. Wrote
    `PHASE_I_III_COMPLIANCE.md` cross-check vs assignment; Phases I–III
    marked complete for G1/G2 with Prompt 04 search-log polish pending.

## 11. Verification and provenance ledger (Prompt 01)

This ledger is intentionally explicit so the workspace does not imply that unperformed checks have been completed.

| Item | Current status | Evidence actually checked | What remains |
|---|---|---|---|
| Review scope and central research question | VERIFIED against supplied PDF | Full extracted text of the 11-page ACM-formatted review was inspected; section/page locations recorded in `research_gap_matrix.md` | None for scope summary; citations within the review still need original-source checking where used to support a research claim |
| Separate implementation/experiment status | VERIFIED only as researcher-reported | Researcher stated that no implementation exists | Revisit if any code, data, or prior runs are later supplied |
| Hardware and constraints | VERIFIED as researcher-reported | MacBook Air M2, 8 GB RAM; free-only tools/models; under two weeks | Confirm OS, hosted notebook permission, exact deadline and assignment rubric |
| LongCite existence and scope | VERIFIED at publisher/abstract-page level | ACL Anthology entry cited in the gap matrix | Inspect full methods, metrics and task coverage before claiming a gap around citations |
| ScholarQABench / OpenScholar existence and scope | VERIFIED at article-page/abstract level | Nature article page referenced in the gap matrix | Inspect full evaluation protocol and limitations before comparing metric coverage |
| ConfRAG existence and scope | VERIFIED at ACL Anthology abstract/page level | ACL Anthology entry referenced in the gap matrix | Inspect benchmark construction, labels, and overlap with proposed tasks |
| Lost in Decomposition existence and scope | VERIFIED at ACL Anthology abstract/page level | Findings of ACL 2026 entry referenced in the gap matrix | Inspect method, baselines, datasets and definitions before choosing context-dependency gap |
| Full original methods for every reference in the review | NOT YET VERIFIED | Bibliographic details and some abstracts/pages checked; not every full paper read | Read the key original papers selected for the candidate question |
| Novelty of any candidate gap | UNKNOWN | Preliminary focused literature audit only | Conduct a documented search around the final narrowed question and compare methods/datasets/metrics |
| Any experimental results | NOT RUN | No code or experiment executed | Do not report results until a run is actually completed and logged |

**Reporting rule:** “Verified against the review” means the review itself says it. It does not mean the original publication has independently confirmed the statement. “Verified at abstract/page level” is not equivalent to a full methodological audit. These distinctions must be retained in the manuscript and later project reports.

-   **2026-10-30 (cleanup):** Removed extra `promt12/` folder; merged Phase I docs into this Lab02 project root so there is a single project directory.
-   **2026-11-13:** Phase IV / Gate G3 executed under Pathway B (deepened):
    contribution plan, offline evaluation figures from locked Groq
    run, failure/metric deep analysis, Results & Discussion outline.
    Null finding on position→coverage/citation retained.
-   **2026-11-13:** Phase V draft manuscript compiled (`paper/main.pdf`,
    6 pages). Prompt 16 peer review and Prompt 17 README reproduction
    notes added. G4 still needs GitHub remote + demo.

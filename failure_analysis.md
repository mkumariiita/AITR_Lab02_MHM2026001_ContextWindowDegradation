# Gate G3 — Deep Analysis: Failure / Metric Audit

**Source run:** `results/raw/run_20261030T142328Z`  
**Machine-flagged cases:** `results/tables/g3_failure_cases.csv` (18 rows)  
**Figures:** `results/figures/fig_failure_tags.png`  
**Method:** Offline analysis of real outputs only (Prompt 13/14 deep cut).

## 1. What “failure” means here

All 18 flagged rows have:

- `evidence_coverage = 1.0`
- `citation_support = 1.0`
- `answer_correctness = 0`

So these are **not** “model missed the gold passages.”  
They are **keyword-correctness misses** while evidence use looks successful.

Tag used: `coverage_ok_corr_fail` / `citation_ok_corr_fail`.

## 2. Position does not drive these flags

| Position | Flagged rows (of 12) |
|---|---:|
| begin | 5 |
| middle | 6 |
| end | 7 |

End has slightly more keyword misses, but coverage/citation remain perfect everywhere.  
**Do not interpret this as classic lost-in-the-middle on evidence access.**

## 3. Qualitative taxonomy (human-readable review of samples)

| Type | Description | Example |
|---|---|---|
| **T1 Paraphrase mismatch** | Answer is on-topic and cites gold ids; gold key string absent | `item_02_end`: says “does **not** automatically…” vs key `does not guarantee` |
| **T2 Lexical variant** | Same meaning, different words | `item_08_*`: “under six hours” / lower attention vs key `shorter sleep` |
| **T3 Near-synonym of metric phrase** | Conceptual match to required claim | `item_07_*`: “separate metric from fluency” vs key `scored separately` |

**Reviewer judgment:** For T1–T3, treating `corr=0` as scientific model failure would be misleading. Primary RQs should rely on coverage/citation support.

## 4. What this deep analysis contributes

1. Separates **evidence-use success** from **brittle automatic correctness**.  
2. Explains why mean `corr` differs by position without coverage changing.  
3. Documents a measurement threat for the paper Limitations section.  
4. Satisfies assignment “deeper analysis” via error/failure-case study (not an ablation of a new model).

## 5. Unsupported claims (explicitly avoided)

- That middle position caused citation/coverage collapse on this corpus.  
- That lower `corr` at end proves positional degradation of understanding.  
- Statistical significance (N=12; no pre-registered inferential test).

---
name: ase-experiments
description: Use when designing or auditing the evaluation of an ASE (IEEE/ACM Automated Software Engineering) paper, covering real subject systems, fair runnable tool baselines, task-matched effectiveness metrics, ablations that isolate a learned component, oracle and correctness validation, contamination-aware LLM handling, and provenance for mining.
---

# ASE Experiments

Match the evidence to the automation's claim. ASE evaluations are judged on whether a **tool or
technique actually does what it claims on real subjects**, compared **fairly** against the closest
runnable automation. This is the axis reviewers weight most, and the one that most often becomes a
Revision criterion.

## Start from the claim shape

Different automations demand different evidence:

| Automation claim | Evidence that matches | Common failure |
|---|---|---|
| Detection (bugs, smells, vulnerabilities) | Precision/recall/F on real defects with a defined ground truth | Synthetic-only defects; unclear ground truth |
| Generation / synthesis (tests, code, patches) | Validity of the produced artifact (compiles, passes, holds the property) | Similarity-to-reference proxy instead of validity |
| Repair | Verified behavior change: re-run + oracle; assertion/spec preservation | "Plausible patch" without an overfitting check |
| Localization / ranking | Rank-based effectiveness on real faults vs. alternatives | Cherry-picked programs; one metric only |
| Scalability / performance | Real-system sizes, wall-clock with a fair config | Toy inputs; unequal baseline budget |

## Real subject systems

- Use **real software** — open-source projects, real bug/defect datasets, real CI logs — not toy
  programs you constructed to make the tool look good.
- Report subject **provenance**: names, versions/commit SHAs, sizes, and the extraction date.
  Reviewers reproduce from this.
- Justify subject **selection** and disclose exclusions; self-selected subjects are the classic
  external-validity threat.

## Fair, runnable tool baselines

- Compare against the **closest runnable automation**, configured at an **equal, documented budget**
  (time, iterations, tuning, seeds). ASE reviewers routinely rerun or scrutinize baselines.
- Pin baseline **versions/commits** and note reimplementation vs. original.
- If no tool baseline exists, construct a defensible non-trivial baseline (a static rewrite, a
  random or heuristic variant) rather than comparing only to "nothing."

## Ablations that isolate the automation

If a learned or LLM component is involved, run an **ablation** that removes it and keeps the rest,
so the marginal value of the *design* is visible. This is what defeats the "the model did it, not
your technique" objection and keeps the paper ASE-shaped rather than ML-shaped.

## Oracles and correctness

- State the **oracle** explicitly: how do you know a generated test is meaningful, or a repair is
  correct? Re-execution, differential testing, formal checks, or human audit — name it.
- For repair/synthesis, guard against **overfitting** to the evaluation oracle (e.g., patches that
  pass the given tests but break behavior): report a held-out or manual correctness check.

## Statistics and effect sizes

- Report **effect sizes and dispersion** (confidence intervals, non-parametric tests where
  appropriate), not just point estimates or a single accuracy number.
- For randomized techniques (search-based, sampling, LLM temperature > 0), report **repeated runs**
  with variance and fix/seed the randomness for the artifact.

## Contamination-aware LLM handling

- Record **model identifiers and dates**; a model updated between runs invalidates comparisons.
- Consider **training-data contamination**: benchmarks the model may have seen inflate results —
  report on held-out or post-cutoff subjects where feasible, and say so.
- **Cache raw model outputs** so the artifact reproduces rather than re-samples a live API.

## Mining and dataset provenance

- Pin repository SHAs, the corpus extraction date, query/filter criteria, and any labeling
  protocol with inter-rater agreement for manually coded data.
- Version the dataset and describe how to regenerate it; a package that needs live scraping
  re-samples a moving target.

## Evaluation audit checklist

```text
[Claim-evidence] each claim -> a matching metric on real subjects (not a proxy)
[Subjects] real, provenance-pinned, selection justified, exclusions disclosed
[Baselines] closest runnable tool, version pinned, equal documented budget
[Ablation] learned/LLM component isolated; marginal value of the design shown
[Oracle] correctness defined; overfitting-to-oracle checked
[Stats] effect sizes + dispersion; repeated runs for randomized methods
[LLM] model IDs/dates recorded; contamination considered; outputs cached
[Repro] provenance pinned; dataset/tool versioned for the artifact
```

## Output format

```text
[Automation claim] detection / generation / repair / localization / scalability
[Evidence match] metric(s) that fit the claim, on real subjects
[Baseline fairness] closest tool, budget parity, versions
[Ablation + oracle] learned-component ablation present; correctness oracle stated
[Threats] subject selection / oracle validity / baseline fairness / contamination — bounded how?
```

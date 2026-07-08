---
name: icse-experiments
description: Use when designing or auditing the evaluation of an ICSE research-track paper, covering subject and benchmark selection, baseline fairness, statistical tests and effect sizes as SE reviewers expect them, qualitative-methods rigor, ablations for AI-based techniques, and threats-driven study design.
---

# ICSE Experiments

Design the study to survive an empiricist's audit, because that is who reviews
it. ICSE's rigor criterion scores "thoroughness and completeness of an
evaluation" (2027 call wording, read 2026-07-08), and the community has strong
default expectations per study type that function as unwritten checklists.

## Evidence proportional to claim

| Claim shape | Minimum evidence ICSE reviewers expect |
|---|---|
| "Technique X finds more bugs than Y" | Real subject programs, Y actually run (not quoted from its paper), same budget/timeout, statistics + effect size |
| "Developers struggle with Z" | Systematic observation: survey with stated sampling, interviews to saturation, or instrumented behavior — not anecdote |
| "LLM-based tool solves task T" | Ablations over prompts/models, contamination discussion, cost reporting, non-LLM baseline where one exists |
| "Metric M predicts defects" | Multiple projects, time-aware splits, comparison against trivial baselines (size, churn) |
| "Our benchmark/dataset enables research" | Construction protocol, quality validation sample, license clarity, comparison with existing sets |

The recurring failure is claim-evidence mismatch: a general claim ("improves
program repair") evaluated on one narrow slice (single-hunk Java bugs from one
dataset). Either widen the evidence or narrow the claim before reviewers do.

## Subjects and benchmarks

- **Real programs, stated selection.** Say how subjects were chosen —
  "all Defects4J v2 projects" beats "10 popular GitHub projects" because the
  latter invites cherry-picking suspicion. Report scale (kLOC, stars, age)
  so readers can judge representativeness.
- **Version-pin everything.** Repository SHAs, dataset versions, dependency
  locks; mining studies live or die on whether the corpus can be rebuilt.
- **Guard against benchmark leakage** in AI-for-SE work: if the model's
  training data plausibly contains your benchmark (most public code
  pre-2024 does), you must address contamination — held-out post-cutoff
  bugs, mutation of subjects, or explicit caveats. Reviewers now ask
  unprompted.

## Baselines and fairness

Rerun baselines in your environment with tuned-in-good-faith configurations
and identical budgets. Where rerunning is impossible (unavailable code,
proprietary systems), say so and downgrade the comparison's claims. A
suspiciously weak baseline is the fastest way to lose a rigor score: reviewers
know these tools' published numbers.

## Statistics as the SE community practices them

SE data are typically non-normal, so community convention favors
non-parametric machinery: Mann-Whitney/Wilcoxon tests paired with an effect
size — Vargha-Delaney Â12 or Cliff's delta — rather than bare p-values, with
multiple-comparison correction when many hypotheses are tested. For
stochastic techniques (search-based SE, LLM sampling), repeat runs (community
folklore says ≥10, more is better), and report distributions, not single
bests. These are norms, not posted rules — but a paper missing them collects
the same review sentence every time.

```text
Per comparison, report all four:
  central tendency  -> median across repetitions
  dispersion        -> IQR or min-max across seeds/runs
  significance      -> Mann-Whitney U (corrected if many tests)
  effect size       -> Â12 or Cliff's delta, with magnitude label
Plus: exact repetition count, budget/timeouts, hardware, and total compute.
```

## Qualitative rigor

For interviews, surveys, and coding studies the checklist changes shape:
sampling strategy and saturation argument; codebook development story; a
second coder with inter-rater agreement (Cohen's kappa or Krippendorff's
alpha) on at least a sample; quotes traceable to anonymized participant IDs;
instruments in the replication package. Mixed-methods papers are welcome at
ICSE precisely when each half meets its own bar.

## Threats-driven design

Write the threats-to-validity section *before* running the study, as a design
instrument: every internal-validity threat you can name pre-hoc (selection
bias, implementation bugs in your own tooling, evaluation-metric gaming) is
one you can still mitigate cheaply — a random audit sample, a sanity
experiment, an independent reimplementation of the metric. Threats discovered
during writing week can only be confessed, not fixed. This inversion is the
single highest-leverage habit in the ICSE evidence culture; see
`icse-writing-style` for how the section is then written.

## Sanity experiments that catch your own bugs

Before believing any headline number, run the cheap falsifiers: a
**null-technique control** (does a random or trivial variant score
suspiciously close to your tool? then the metric, not the technique, is
doing the work); a **known-answer audit** (hand-verify a random sample of
your tool's outputs — SE evaluation pipelines mislabel more often than
techniques fail); and a **metric-implementation cross-check** (compute one
cell of the results table with an independent script). Papers retracted or
majorly revised over evaluation bugs almost always lacked one of these three
runs, each of which costs an afternoon.

## Ablations for AI-era SE papers

When the technique wraps a model, reviewers want the wrapper separated from
the model: fix the model and vary your components; fix your components and
vary the model (at least one open-weights option so others can reproduce);
report token/dollar/time costs; state decoding parameters and exact model
versions with dates — "GPT-4" is not a reproducible identifier and will be
flagged under verifiability.

## Output format

```text
[Claim inventory] each headline claim -> evidence row above -> met / gap
[Subjects] selection rule, scale, version pins, contamination status
[Baselines] rerun? tuned? budget-matched? which comparisons are downgraded
[Statistics] tests, effect sizes, repetitions, corrections present?
[Qualitative] sampling, codebook, agreement stats (if applicable)
[Pre-hoc threats] threats named at design time -> mitigation experiments queued
```

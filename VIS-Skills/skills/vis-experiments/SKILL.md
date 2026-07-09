---
name: vis-experiments
description: Use when designing or auditing IEEE VIS evaluations, covering how to match evidence to the contribution type (perceptual study, controlled user study, algorithm benchmark, design-study validation, qualitative work), controlled experiment design with power and effect sizes, CVD-safe and perceptually grounded encoding choices, task taxonomies, and provenance so a TVCG reviewer trusts the result.
---

# VIS Experiments

Use this before submission when the evaluation is not yet locked. IEEE VIS reviewers judge whether
the **evidence matches the contribution type** — and visualization has several distinct contribution
types, each with its own evidence standard. The organizing principle is **evaluate the claim you
actually make**: a claim about *perception* needs a controlled study, a claim about *scale* needs a
benchmark, a claim about *real-world usefulness* needs a design-study validation or a deployment.

## Evaluation audit

- **Pick the evaluation to the contribution type**, not by habit (see the table). The classic VIS
  reject is a system paper "evaluated" only by an accuracy number, or a perceptual claim backed only
  by author intuition.
- **Design controlled studies properly:** state hypotheses, a within/between design, a task from a
  recognized task taxonomy, a **power analysis** justifying N, and report **effect sizes with
  confidence intervals**, not just p-values. Consider preregistration for confirmatory studies
  (`vis-reproducibility`).
- **Justify encodings perceptually:** color choices should be **CVD-safe** and appropriate to the
  data type (sequential/diverging/categorical); channel choices should follow known effectiveness
  rankings for the task. Reviewers check this explicitly.
- **Benchmark techniques fairly:** compare against the strongest existing technique and a reasonable
  baseline on realistic data sizes, with runtime/quality reported and the code available.
- **Hold qualitative and design-study work to method:** coding schemes, multiple coders,
  reflection across abstraction levels, and an audit trail — design studies are a first-class VIS
  contribution, not a weak substitute for a controlled study.
- **Pin provenance** for datasets, stimuli, and rendering so the evaluation reproduces rather than
  re-samples.

## Contribution-type to evidence table

| Contribution type | Matching evidence | Reject pattern avoided |
|---|---|---|
| Perceptual/cognitive claim | Controlled experiment: real stimuli, power analysis, effect sizes + CIs | "Author intuition stands in for a perception result" |
| New encoding/interaction technique | Controlled study and/or task-based comparison vs. the conventional design | "Prettier, but no evidence it helps a task" |
| System / tool | Demonstration of real use, expert feedback, or a usage study | "Feature list with no evaluation of use" |
| Design study | Reflection + validation across data/task/encoding/algorithm levels | "A one-off tool with no transferable lesson" |
| Algorithm (layout/rendering) | Benchmark: quality + runtime vs. strong baselines on realistic sizes | "Toy inputs only; no comparison" |
| Data/model contribution | Characterization + a task the data enables, with the data shared | "Dataset dumped with no analysis or task" |

## Controlled-study design floor

```text
[Hypotheses]  stated before analysis; confirmatory vs. exploratory labeled
[Design]      within/between justified; counterbalancing; the task from a known taxonomy
[Power]       an a-priori power analysis justifies N; do not stop at "we recruited 20"
[Stimuli]     real or realistic; the exact stimuli archived
[Measures]    accuracy AND time AND (where relevant) preference/confidence; define each
[Statistics]  effect sizes + CIs; appropriate tests; corrections for multiple comparisons
[Reporting]   report what you found, including null and exploratory results, honestly
```

## Perceptual and accessibility checks

- **Color:** use CVD-safe palettes; match palette type to data (sequential for ordered, diverging
  for a meaningful midpoint, categorical for nominal); never encode magnitude on hue alone.
- **Channel effectiveness:** prefer position/length for quantitative comparison; justify any use of
  area, angle, or color for a precise task.
- **Legibility:** ensure figures read in grayscale and at print size; a result a reviewer cannot see
  is a result you cannot claim.

## Vignette: evaluating a new time-series encoding

Suppose the paper claims a new encoding reads trends faster than a line chart. The matching plan: a
controlled within-subjects study; trend-reading tasks drawn from a task taxonomy; real time-series
stimuli, archived; an a-priori power analysis fixing N; accuracy and completion-time as measures;
effect sizes with CIs comparing the new encoding to a tuned line-chart baseline; a CVD-safe palette
justified against the task; and honest reporting of any task where the line chart won — every number
traceable to the archived analysis notebook.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Contribution type] perceptual / technique / system / design-study / algorithm / data
[Evidence match] <contribution type -> evidence chosen -> appropriate? yes/no>
[Study rigor] <hypotheses? power analysis? effect sizes + CIs? preregistered?>
[Encoding validity] <CVD-safe? channel matched to task? grayscale-legible?>
[Provenance] <stimuli/data/rendering archived and reproducible? yes/no>
[Decision-critical next run] <one study or benchmark to add>
```

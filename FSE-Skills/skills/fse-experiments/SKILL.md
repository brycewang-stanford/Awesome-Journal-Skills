---
name: fse-experiments
description: Use when designing or auditing ESEC/FSE empirical evaluations, covering real subject systems, fair baselines, SE-standard statistics and effect sizes, qualitative and mixed-methods rigor, contamination-aware LLM ablations, provenance for mining studies, and matching evidence to the shape of each software-engineering claim.
---

# FSE Experiments

Use this before submission when the empirical story is not yet locked. FSE reviewers are SE
empiricists; the evaluation is where a good idea is won or lost. The organizing principle is
**evidence proportional to the claim** — the study must test the thing the paper actually asserts,
on subjects and baselines a skeptic would accept.

## Evaluation audit

- **Match evidence to the claim shape.** A claim about *developer behavior* needs behavior data; a
  claim about *detection* needs a labeled ground truth; a claim about *scalability* needs runtime
  on realistically sized inputs. Accuracy against a proxy label is not evidence for a practice
  claim.
- **Use real subject systems,** sampled by a stated criterion, and list them in the artifact. Toy
  benchmarks invite the "does this hold on real code?" reject.
- **Choose fair baselines,** including the strongest prior technique and a simple-but-reasonable
  alternative, tuned with a documented, equal budget. An untuned baseline is a scored weakness.
- **Report SE-standard statistics:** effect sizes (not just p-values), confidence intervals,
  appropriate tests, and corrections for multiple comparisons. Say what variance and how many runs.
- **Hold qualitative work to method:** coding schemes, inter-rater agreement, saturation, and an
  audit trail — mixed-methods rigor is native to FSE, not a second-class option.
- **Pin provenance for mining and LLM studies** (see the code block) so the evaluation reproduces
  rather than re-samples.
- **Design threats in, not on:** know before you run which confounds and generalization limits the
  study will have, and instrument to bound them.

## Claim-to-evidence design table

| SE claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Technique detects more real defects" | Labeled real faults, precision/recall with CIs vs. tuned baseline | "Evaluated on injected/toy faults only" |
| "Developers act on the output" | Behavioral outcome data on real projects | "Plausibility rating stands in for usefulness" |
| "Scales to large systems" | Runtime/memory across realistic sizes | "Only small inputs tested" |
| "Finding generalizes" | Diverse subject sample + explicit external-validity limits | "One ecosystem, claimed universal" |
| "The model adds the value" | Ablation removing the model vs. lexical/heuristic features | "Model's marginal contribution never isolated" |

## Contamination-aware LLM evaluation

When an LLM is in the loop, the reviewer's first questions are about leakage and reproducibility:

```text
[Contamination]  are test subjects plausibly in the model's training data? report cutoff vs.
                 project dates; prefer post-cutoff or held-out subjects
[Determinism]    fix temperature/seed where possible; report the sampling settings
[Caching]        store raw prompts and raw responses in the artifact; a live-API-only study
                 cannot be reproduced, only re-sampled
[Versioning]     record exact model identifiers and access dates; models change under a name
[Ablation]       isolate the model's marginal value against a non-LLM baseline
```

## Provenance floor for mining studies

- Pin repository SHAs and record the corpus extraction date; archive the *extracted* dataset, not
  just the query.
- State inclusion/exclusion criteria and the resulting sample size, with the filtering script in
  the artifact.
- Report how duplicates, forks, and bot activity were handled — silent inclusion skews every
  downstream number.

## Vignette: evaluating a repair technique

Suppose the paper claims a program-repair technique fixes more real bugs than the prior tool. The
matching plan: draw bugs from a real, dated fault dataset; run both tools with an equal, documented
time budget; report plausible-and-correct patch counts with confidence intervals and an effect
size; manually assess a sample of patches for over-fitting; and state external validity (languages,
bug kinds) as a bounded threat — every number traceable to a logged run in the artifact.

## Statistical reporting floor

- Effect sizes and confidence intervals for every quantitative comparison; say what the intervals
  represent.
- Number of runs and the source of variance for any stochastic component.
- The compute actually consumed, not vague feasibility language.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> evidence map] <claim: subjects/metric/statistic>
[Baseline fairness] <baseline -> tuned? equal budget? documented?>
[Contamination/provenance] <LLM leakage + mining provenance handled? yes/no>
[Threats-by-design] <confound/generalization -> instrumentation to bound it>
[Decision-critical next run] <one experiment or study extension>
```

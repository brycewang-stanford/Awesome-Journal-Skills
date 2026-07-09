---
name: icsme-experiments
description: Use when designing or auditing IEEE ICSME empirical evaluations, covering real evolving subject systems, mining-software-repositories provenance, fair baselines, SE-standard statistics and effect sizes, change-history and survivorship confounds, qualitative rigor, contamination-aware LLM ablations, and matching evidence to the shape of each maintenance/evolution claim.
---

# ICSME Experiments

Use this before submission when the empirical story is not yet locked. ICSME reviewers are
maintenance and evolution empiricists, and because the venue has **no revision round**, the
evaluation must be complete on submission — you cannot promise a missing analysis and add it later.
The organizing principle is **evidence proportional to the claim**, tested on **real systems with
real change history**, not on synthetic snapshots.

## Evaluation audit

- **Match evidence to the claim shape.** A claim about *maintenance effort* needs effort or proxy
  data defended as a proxy; a claim about *change impact* needs real change sets; a claim about
  *comprehension* needs a human study; a claim about *debt* needs a debt measurement, not lines of
  code. Accuracy against a convenient label is not evidence for a maintenance-practice claim.
- **Use real, evolving subject systems,** sampled by a stated criterion over a stated time window,
  and list them in the artifact. A single snapshot cannot support an evolution claim.
- **Pin mining provenance** (see the code block): repository SHAs, extraction dates, inclusion/
  exclusion criteria, and fork/duplicate/bot handling. Silent inclusion of forks or bot commits
  skews every downstream evolution number.
- **Choose fair baselines,** including the strongest prior maintenance technique and a
  simple-but-reasonable alternative, tuned with a documented, equal budget. An untuned baseline is a
  scored weakness a rebuttal cannot fully repair.
- **Report SE-standard statistics:** effect sizes (not just p-values), confidence intervals,
  appropriate tests, and corrections for multiple comparisons; say how many runs and what variance.
- **Handle change-history confounds by design:** survivorship (systems that died mid-history),
  releases vs. commits as the unit of evolution, and time-window sensitivity.
- **Hold qualitative work to method:** coding schemes, inter-rater agreement, saturation, and an
  audit trail — mixed-methods maintenance studies are native to ICSME.

## Claim-to-evidence design table

| Maintenance/evolution claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Technique reduces change impact" | Real change sets from history, set-size deltas with CIs vs. tuned baseline | "Evaluated on synthetic edits only" |
| "Refactoring preserves behaviour" | Test outcomes / regression evidence across applications on real code | "Assumed safe, never checked" |
| "Debt predicts future defects" | Longitudinal link from debt measure to later real defects, with survivorship handled | "Cross-sectional correlation claimed causal" |
| "Improves comprehension" | Human study with tasks, accuracy/time, effect sizes | "Tool complexity mistaken for understanding" |
| "Finding holds across systems" | Diverse, dated sample + explicit external-validity limits | "One ecosystem, claimed universal" |
| "The model adds the value" | Ablation removing the model vs. lexical/heuristic features | "Model's marginal contribution never isolated" |

## Provenance floor for mining studies (the ICSME core)

```text
[Corpus]     pin repository SHAs; record extraction date and the time window studied;
             archive the *extracted* dataset, not just the query
[Selection]  state inclusion/exclusion criteria and resulting N; ship the filtering script
[Hygiene]    document fork/duplicate/bot handling; report how merges and renames were resolved
[Unit]       state whether the unit is commit, PR, release, or file, and defend it for the claim
[History]    address survivorship and left-truncation of the change history explicitly
```

## Contamination-aware LLM evaluation

When an LLM is in the loop (increasingly common for comprehension, summarization, and repair):

```text
[Contamination]  are subject systems plausibly in the model's training data? report model cutoff
                 vs. project/commit dates; prefer post-cutoff or held-out systems
[Determinism]    fix temperature/seed where possible; report the sampling settings
[Caching]        store raw prompts and raw responses in the artifact; a live-API study re-samples
                 rather than reproduces
[Versioning]     record exact model identifiers and access dates; models drift under a name
[Ablation]       isolate the model's marginal value against a non-LLM maintenance baseline
```

## Vignette: evaluating a change-impact technique

Suppose the paper claims a technique predicts change-impact sets more precisely than a prior tool.
The matching plan: draw real change sets from dated release histories of several evolving systems;
run both tools with an equal, documented budget; report precision/recall with confidence intervals
and an effect size; manually inspect a sample of predicted impacts for spurious inclusion; handle
survivorship by stating which systems' histories are truncated; and bound external validity
(languages, domains) as a threat — every number traceable to a logged run in the artifact.

## Statistical reporting floor

- Effect sizes and confidence intervals for every quantitative comparison; say what the intervals
  represent.
- Number of runs and the source of variance for any stochastic component.
- The compute and mining time actually consumed, not vague feasibility language.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> evidence map] <claim: systems/history-window/metric/statistic>
[Mining provenance] <SHAs / extraction date / selection / fork-bot hygiene handled? yes/no>
[Baseline fairness] <baseline -> tuned? equal budget? documented?>
[Confounds by design] <survivorship / unit-of-analysis / contamination -> how bounded>
[Decision-critical gap] <the one thing that must be complete before submission — no revision round>
```

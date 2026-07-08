---
name: acl-experiments
description: Use when designing or auditing experiments for an ACL paper, covering tuned LLM baselines, multi-dataset and multilingual evaluation, statistical significance and variance, human evaluation with agreement reporting, contamination and prompt-sensitivity controls, ablations, and error-analysis expectations in NLP reviewing.
---

# ACL Experiments

Use this while the experimental story can still change. The ACL evidence bar
is not "beats the baseline once": it is a defensible measurement of a language
capability, with the failure modes examined.

## Baseline honesty

- Include the strongest cheap baseline: a well-prompted current LLM has become
  mandatory context for most tasks — a method beating only pre-LLM systems
  invites the "does this matter now?" review.
- Tune baselines with the same care as your method (same search budget, same
  data); reviewers explicitly probe for asymmetric tuning.
- Report the trivial baselines (majority class, copy input, retrieval-only)
  when they contextualize how hard the task actually is.

## Evaluation design

- Breadth must match the claim: a "general" claim needs multiple datasets;
  a cross-lingual claim needs typologically distinct languages, not three
  Romance neighbors.
- Automatic metrics need justification for generation tasks — pair n-gram or
  embedding metrics with human or LLM-judge evaluation, and validate any
  LLM-judge against human labels before leaning on it.
- Fix the evaluation protocol before final runs: dev-set peeking on the test
  set via repeated submissions is unreportable and unrepairable.

## Statistical floor

| Result flavor | Required rigor at ACL |
|---|---|
| Small deltas between systems | Significance test (bootstrap/permutation) or overlapping-interval honesty |
| Fine-tuning results | Multiple seeds; mean and deviation in the table, defined in the caption |
| Prompted-LLM results | Multiple prompt paraphrases and/or samples; sensitivity range reported |
| Human evaluation | Raters per item, agreement statistic (e.g., Krippendorff's alpha), pay disclosed |
| Correlation claims (metrics) | Confidence intervals and comparison against existing metric correlations |

The Responsible NLP checklist (Section C) asks for descriptive statistics and
error bars — an experiment plan that cannot fill Section C truthfully is
incomplete by construction.

## Contamination and validity controls

- Reason explicitly about test-set membership in pretraining data: release
  dates vs model cutoffs, overlap scans, or held-back fresh test items.
- Watch prompt leakage: few-shot exemplars drawn from the test distribution,
  instructions embedding label hints.
- For annotation-based data, quantify label quality before measuring models
  against it; models are now frequently better than noisy gold labels.

## Ablations and the mechanism claim

- Each component the abstract credits needs an ablation row; each ablation
  row needs the same variance treatment as the headline number.
- Prefer ablations that test the *explanation* (e.g., "gains come from the
  retrieval step") over combinatorial component sweeps.
- Scale ablation: if a claim is "method X helps," show it at two model sizes
  or state the single-scale limitation explicitly.

## Error analysis as a deliverable

The distinctive ACL expectation: a quantitative error analysis with named
categories.

1. Sample failures (100-200) from the strongest configuration.
2. Induce 4-8 functional error categories; double-annotate a subset and
   report agreement.
3. Report category frequencies for your method vs the best baseline —
   where do gains actually come from?
4. Feed the two most persistent categories into Limitations.

## Pre-run design worksheet

```text
Claim:         <one sentence>
Datasets:      <n, why these, language list>
Baselines:     <incl. tuned LLM baseline + trivial floor>
Runs/variance: <seeds or prompt paraphrases; interval type>
Significance:  <test, when applied>
Human eval:    <items, raters, agreement plan, pay>
Contamination: <audit method>
Ablations:     <component -> table row>
Error analysis:<sample size, category plan>
```

## Common evidence failures seen in ARR reviews

- Averaging over languages to hide that one language regressed — report the
  per-language block; reviewers open the appendix table first when a claim
  says "multilingual."
- Comparing your tuned method against baseline numbers copied from papers
  that used different preprocessing or splits.
- Treating an LLM judge as ground truth without reporting its agreement
  with humans on a calibration subset.
- Claiming efficiency without wall-clock, memory, or cost on matched
  hardware.
- Running the significance test only on the comparison that wins.
- Reporting the best seed as the headline and the mean in the appendix —
  reviewers call this out by name.

## When compute is the constraint

- Pre-register (internally) which single configuration gets the full
  multi-seed treatment, and make it the headline setting.
- Use paired designs — same items, both systems — so smaller samples still
  yield tight comparisons and permutation tests apply cleanly.
- Prefer breadth at small scale plus depth at one large scale over a thin
  sweep of everything; state the choice in the setup section.
- Cache and release intermediate outputs so ablations re-score rather than
  re-run.

## Output format

```text
[Evidence verdict] convincing / thin / misaligned-with-claim
[Baseline gaps] <missing or under-tuned comparators>
[Statistical gaps] <variance/significance/agreement omissions>
[Validity threats] <contamination/leakage/label-quality>
[Highest-value next run] <one experiment>
```

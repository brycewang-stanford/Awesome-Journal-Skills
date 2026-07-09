---
name: percom-experiments
description: Use when designing or auditing IEEE PerCom empirical evaluations, covering real human subjects, leave-one-subject-out / cross-subject evaluation, F1 and event-level metrics on imbalanced activity classes, deployment realism (free-living vs. lab), fair baselines, contamination-aware model ablations, and matching evidence to the shape of each pervasive-computing claim.
---

# PerCom Experiments

Use this before submission when the evaluation is not yet locked. PerCom reviewers are ubicomp
empiricists; the evaluation is where a sensing idea is won or lost, and — because the review is a
single round with a bounded rebuttal — **the evaluation must be complete at submission** (you
cannot add experiments in the rebuttal). The organizing principle is **evidence proportional to the
claim**, tested on **people and conditions a skeptic would accept**.

## Evaluation audit

- **Evaluate cross-subject by default.** A recognition claim about *users* needs
  **leave-one-subject-out** (or leave-one-session-out) results, not a pooled split that lets the
  same person appear in train and test. Within-subject numbers are a supporting detail, never the
  headline.
- **Use real human subjects,** described by count and relevant characteristics, with the collection
  protocol stated. Report how many, doing what, wearing/placed where.
- **Report the right metric.** Human activity is imbalanced (most of a day is "null"), so **F1
  (macro and per-class)**, precision/recall, or **event-level** metrics tell the truth where raw
  accuracy flatters. Say whether metrics are frame-level or event-level.
- **Test deployment realism.** Distinguish **lab vs. free-living** and scripted vs. spontaneous
  behavior; a result only shown on scripted in-lab data invites the "does this survive daily life?"
  objection.
- **Choose fair baselines,** including the strongest prior method and a simple-but-reasonable
  alternative, tuned with a documented, equal budget. An untuned baseline is a scored weakness.
- **Report variance:** confidence intervals across subjects/folds, number of runs, and the source
  of stochasticity. Per-subject distributions matter more than a single mean here.
- **Design limitations in, not on:** know before you collect which generalization and construct
  limits the study will have (subject diversity, ground-truth quality), and instrument to bound
  them.

## Claim-to-evidence design table

| Ubicomp claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Recognizes activity for new users" | Leave-one-subject-out F1 with per-subject spread | "Within-subject / pooled split inflates the number" |
| "Works in daily life" | Free-living data, event-level metrics | "Only scripted in-lab sessions tested" |
| "Beats the prior recognizer" | Same data + tuned baseline, equal budget | "Baseline untuned or on a different split" |
| "Handles class imbalance" | Macro-F1 + per-class recall, stated balance | "Raw accuracy hides the rare-class collapse" |
| "The model adds the value" | Ablation vs. classical features/heuristics | "Model's marginal contribution never isolated" |
| "Generalizes across contexts" | Diverse subjects/environments + explicit limits | "One population, claimed universal" |

## Contamination- and leakage-aware evaluation

Sensing pipelines leak in subtle ways; the reviewer's first questions are about splits and leakage:

```text
[Subject leakage]  never let one participant appear in both train and test -- LOSO prevents it
[Session/time leak] windows from one recording session can leak across a naive random split
[Normalization leak] fit scalers/PCA on train only; a global normalization leaks test statistics
[Pretraining]      if a foundation model is used, report whether test subjects/data could be in its
                   training set; prefer held-out or post-cutoff data
[Ablation]         isolate the model's marginal value against a classical-feature baseline
```

## Human-subjects provenance floor

- State subject count and relevant demographics, the collection protocol, and IRB/consent status.
- Pin device models, firmware, sampling rates, and sensor placement; archive the **extracted,
  de-identified** dataset, not just a description.
- Report the labeling protocol, who labeled, and inter-annotator agreement — silent label noise
  skews every downstream number.

## Vignette: evaluating a HAR recognizer

Suppose the paper claims a wearable recognizer beats a prior model on daily activities. The matching
plan: collect from a diverse participant set over multiple days of free-living; evaluate
**leave-one-subject-out**; report macro-F1 and per-class recall with confidence intervals across
subjects; run both models on the same folds with an equal, documented tuning budget; add an ablation
against classical features; and state external validity (population, device) as a bounded limitation
— every number traceable to a logged run in the artifact, because the rebuttal cannot add a run.

## Reporting floor

- Cross-subject metric (F1/event-level) with confidence intervals and per-subject spread for the
  headline comparison; say what the intervals represent.
- Number of runs and the source of variance for any stochastic component.
- The compute actually consumed, not vague feasibility language.

## Output format

```text
[Evaluation readiness] strong / adequate / weak (remember: no new experiments in the rebuttal)
[Claim -> evidence map] <claim: subjects / split (LOSO?) / metric (F1?) / setting (free-living?)>
[Baseline fairness] <baseline -> tuned? equal budget? same split? documented?>
[Leakage check] <subject / session / normalization / pretraining leakage handled? yes/no>
[Limitations-by-design] <generalization/construct limit -> instrumentation to bound it>
[Decision-critical run to finish before submission] <one experiment>
```

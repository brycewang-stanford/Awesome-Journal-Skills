---
name: cogpsych-review-process
description: Use when you need to understand how Cognitive Psychology (Elsevier) evaluates a manuscript — editorial triage for theoretical impact and fit, expert review weighing model rigor, recovery, design, and reproducibility, and the long revision cycles typical of a model-driven journal. Use when stress-testing a paper before submission or interpreting a decision letter. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (cogpsych-review-process)

Cognitive Psychology combines selectivity for **theoretical impact** with deep **methodological and
modeling scrutiny**. Reviewers and editors weigh not only whether the finding is interesting, but
whether the **model is well-specified, identifiable, and properly compared**, whether the **experiments
discriminate the accounts**, and whether the work is **reproducible**. Knowing this lets you pre-empt
the common rejection reasons. Confirm the current process on the official page (检索于 2026-06；以官网为准).

## When to trigger

- Before submitting, to stress-test the manuscript
- Interpreting a decision letter and setting expectations
- Deciding how to fit a long, model-driven program to a demanding review

## How review works (typical Elsevier journal pattern)

1. **Editorial triage.** A handling editor assesses theoretical impact, scope, and fit; thin,
   single-effect, or atheoretical submissions may be **rejected without external review** at this
   long-form, model-driven venue.
2. **Expert peer review.** Typically multiple referees with cognitive-modeling and experimental
   expertise. Expect detailed scrutiny of model specification, identifiability/recovery, model
   comparison, experimental confounds, and the strength of the inference.
3. **Reproducibility is checked.** Reviewers may attempt to run model/analysis code; fits that don't
   regenerate, or undocumented model choices, weaken the paper (see
   `cogpsych-open-science-and-transparency`).
4. **Decisions and cycles.** Reject, major/minor revision, or accept; integrative model-driven papers
   often go through **substantial, sometimes multiple, revision rounds** — added experiments, recovery
   analyses, or model comparisons are common requests.

> Verify the review model (single- vs. double-anonymized), referee count, and timelines on the journal's
> current guide for authors — these are volatile (检索于 2026-06；以官网为准).

## Shape the paper to pass

- Make the **theoretical advance** explicit and early; show the experiments **discriminate** the models.
- Fit and **compare** models under matched flexibility; include **parameter and model recovery**.
- Respect the data hierarchy (mixed/hierarchical models) and report effect sizes with intervals.
- Make the modeling **reproducible** from deposited code; complete Elsevier declarations.
- Separate confirmatory from exploratory model work honestly.

## Desk-reject and decline-without-review patterns

The long-form, model-driven identity means many submissions never reach external review. Recognize these
shapes and pre-empt them:

| Pattern an editor sees | Likely outcome | Pre-empt it by |
|------------------------|----------------|----------------|
| One experiment, one effect, no model/theory | desk reject (wrong shape) | grow into a model-driven program or place in a short-report venue |
| Model fit but never compared to a rival | major revision or reject | fit rivals under matched flexibility; report criteria |
| Experiments don't discriminate the accounts | reject (non-diagnostic) | redesign for the discriminating signature |
| Aggregated analyses, ignored subject/item variance | methods flag | refit with mixed/hierarchical models |
| Fits not reproducible; no code | reproducibility flag | deposit seeded model code with a run log |
| Better-fitting but more flexible model claimed as winner | overfitting flag | add recovery + penalized comparison/cross-validation |

## Worked micro-example (illustrative triage)

```
Manuscript: three preregistered recognition-memory experiments; UVSD vs.
            DPSD fit and compared (hierarchical Bayesian), recovery reported,
            open data + model code with DOIs, diagnostic z-ROC signature.
Editor read: theoretical impact (adjudicates a long-running debate), modeling
            rigor (comparison + recovery), reproducibility (code regenerates).
Likely route: external review, probable major revision for added robustness
            (alternative priors, a further model, more recovery).
Counter-case: same effect, one experiment, one model fit, request-only data,
            no recovery → likely declined without full review.
```

## How reviewers weigh the evidence (calibration anchors)

- The strongest signal is a **diagnostic experiment + a recovered, compared model** that together pick
  one account over a real rival — this converts "interesting fit" into "credible adjudication."
- Reviewers distrust a fit advantage without recovery and matched flexibility; a crossed qualitative
  prediction is more persuasive than a smaller AIC.
- Reproducibility is part of the evidence, not a formality; a fit that doesn't regenerate reads as a
  result that might not exist.

## Anti-patterns

- A single-effect, atheoretical submission expecting full review at a model-driven venue
- A model fit with no rival, no comparison, and no recovery
- Aggregated analyses that ignore crossed subject/item variance
- Expecting acceptance without a substantial, modeling-heavy revision round
- Irreproducible fits or undocumented model choices

## Output format

```
【Theoretical advance】clear early? [Y/N]
【Discrimination】do experiments separate the models? [Y/N]
【Modeling rigor】comparison + recovery + matched flexibility? [Y/N]
【Hierarchy + reporting】mixed/hierarchical + effect sizes/intervals? [Y/N]
【Reproducible】model code regenerates fits? [Y/N]
【Realistic outcome】reject / major revision / minor revision / accept
【Next】cogpsych-submission (or cogpsych-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review model, scope, and reproducibility expectations

---
name: jais-data-analysis
description: Use when running and reporting the empirical core of a Journal of the Association for Information Systems (JAIS) manuscript — SEM measurement and structural models for behavioral IS, identification and robustness for economics-of-IS, artifact evaluation for design science, or trustworthiness for qualitative work — and assembling the data/matrix materials JAIS requires. Executes and reports the analysis; it does not design the study (jais-methods) or frame the contribution (jais-contribution-framing).
---

# Data Analysis & Evidence (jais-data-analysis)

## When to trigger

- Data are collected (or the artifact built) and it is time to estimate, evaluate, and report
- A reviewer probes measurement validity, identification, artifact utility, or replicability
- You must prepare the **correlation/covariance matrix plus descriptives** JAIS requires for quantitative studies
- Effects are reported as stars with no magnitude or theoretical meaning

## Analyze in the currency of your tradition

JAIS's pluralism means there is no single mandated estimator; the standard is the rigor norm of your tradition, reported transparently enough for a developmental Senior Editor to interrogate. Pick the row.

| Tradition | What to report |
|-----------|----------------|
| **Behavioral** | reliability (alpha/CR), CFA or PLS measurement model, AVE, discriminant validity (Fornell-Larcker / HTMT); structural paths with effect sizes; mediation via bootstrap CIs; moderation via simple slopes |
| **Economics of IS** | the identifying variation, parallel-trends/exogeneity evidence, clustered SEs, and a robustness battery (alternative specs, placebo/event-time tests, sensitivity to the key assumption) |
| **Design science** | artifact performance against credible baselines on held-out data; ablations; field/A-B or expert evaluation tied to design propositions; cost/utility discussion |
| **Qualitative / interpretive** | a transparent data structure (codes → themes → dimensions), an audit trail, and representative quotations tracing raw data to constructs |

## Behavioral IS: defend measurement, then satisfy the JAIS matrix rule

Report the measurement model first: reliabilities, AVE, and discriminant validity. PLS-SEM suits predictive/formative models; covariance-based SEM suits theory-testing with reflective constructs — justify the choice. Address **common-method bias** beyond a single-factor (Harman) test — a marker variable, an unmeasured method factor, or showing interactions survive. Then report structural paths with **effect sizes**, not just significance. Crucially, JAIS requires you to **"provide a full correlation matrix or covariation matrix as a part of articles (appendix)"** for SEM studies, plus descriptives — prepare this now, not at proof stage (检索于 2026-06；以官网为准).

## Economics of IS: make the causal claim earn its keep

Lead with the identification logic, then stress-test it: alternative specifications, placebo and event-study plots, sensitivity to the key assumption, and clustering matched to the data structure. With staggered timing, use a modern estimator and show flat pre-trends. Report magnitudes and their economic meaning, not just stars.

## Design science: evaluate the artifact, not just the math

Benchmark against the baselines a skeptic would name, run ablations to show which design principles matter, and connect each result back to a design proposition. Where feasible, evaluate in a realistic field setting. Utility for a real problem is the contribution.

## Qualitative: make the path from data to theory traceable

Show the coding structure and an audit trail so a reader can follow how raw material became constructs. Representative quotations and negative cases build trustworthiness; the analytic narrative, not a coefficient, carries the claim.

## Prepare the JAIS data materials

JAIS policy requires authors to make datasets **"available on request for checking by senior editors or reviewers after care has been taken to anonymize the data,"** and for quantitative studies to provide **"the co-variance or correlation matrix plus descriptives."** If you reuse a dataset, you must justify it for an alternative theoretical purpose or a new methodological approach. Assemble these now and keep them anonymized for double-blind review.

## Checklist

- [ ] Analysis matches the tradition (SEM / causal econometrics / artifact evaluation / qualitative)
- [ ] Behavioral: reliability, AVE, discriminant validity, CMB beyond single-factor; effect sizes reported
- [ ] SEM: full correlation/covariance matrix + descriptives prepared as an appendix
- [ ] Economics: identification defended, robustness/placebo tests, clustered SEs, magnitudes
- [ ] Design science: baselines, ablations, field/expert evaluation tied to design propositions
- [ ] Qualitative: traceable data structure and audit trail
- [ ] Datasets anonymized and available on request to SEs/reviewers; reuse justified if applicable

## Anti-patterns

- A single-factor (Harman) test as the sole common-method-bias defense.
- Submitting SEM results without the required correlation/covariance matrix and descriptives.
- A causal claim with no identification and no robustness battery.
- A design-science "evaluation" with no credible baseline.
- Reporting p-values with no effect sizes or practical/theoretical interpretation.

## Output format

```text
【Tradition & analysis】SEM / DiD-IV-RD / artifact eval / qualitative
【Validity or identification】measurement + CMB / identification + robustness / baselines + ablations
【Effect sizes / utility】magnitudes and meaning
【JAIS data materials】correlation/covariance matrix + descriptives + anonymized dataset on request: ready/gaps
【Source status】verified URL / 待核实
【Next skill】jais-contribution-framing
```

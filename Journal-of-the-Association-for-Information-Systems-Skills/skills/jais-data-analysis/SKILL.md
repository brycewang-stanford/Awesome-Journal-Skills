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

## Report robustness as a defense of the theory, not a ritual

A robustness battery at JAIS should be legible as protecting the *theoretical* claim, not as a checklist. For each check, state the threat it neutralizes: a placebo test guards against spurious timing, an alternative specification guards against functional-form dependence, a sensitivity analysis bounds the unobserved-confounding concern. Listing checks without naming the threat each addresses is a recurring pushback — and at a theory-forward journal, an unmotivated robustness section signals that the author is not sure which threat actually endangers the contribution.

## Design science: evaluate the artifact, not just the math

Benchmark against the baselines a skeptic would name, run ablations to show which design principles matter, and connect each result back to a design proposition. Where feasible, evaluate in a realistic field setting. Utility for a real problem is the contribution.

## Qualitative: make the path from data to theory traceable

Show the coding structure and an audit trail so a reader can follow how raw material became constructs. Representative quotations and negative cases build trustworthiness; the analytic narrative, not a coefficient, carries the claim.

## Tie every result back to the theory

JAIS is theory-forward, so analysis that floats free of the theoretical argument reads as dredging. After each estimate, evaluation, or coded theme, state explicitly which hypothesis, proposition, or construct it bears on and what it implies for the mechanism. A results section that marches through coefficients without re-connecting to the theory invites the "strong finding, thin contribution" critique — the most common JAIS pushback. The discipline is to report the number and immediately say what the field now knows because of it.

## Prepare the JAIS data materials

JAIS policy requires authors to make datasets **"available on request for checking by senior editors or reviewers after care has been taken to anonymize the data,"** and for quantitative studies to provide **"the co-variance or correlation matrix plus descriptives."** If you reuse a dataset, you must justify it for an alternative theoretical purpose or a new methodological approach. Assemble these now and keep them anonymized for double-blind review.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAIS spans empirical and design-science IS; apply the chain below to its causal / econometric papers and note when work is design-science or conceptual.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the appendix. See the
executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Analysis matches the tradition (SEM / causal econometrics / artifact evaluation / qualitative)
- [ ] Behavioral: reliability, AVE, discriminant validity, CMB beyond single-factor; effect sizes reported
- [ ] SEM: full correlation/covariance matrix + descriptives prepared as an appendix
- [ ] Economics: identification defended, robustness/placebo tests, clustered SEs, magnitudes
- [ ] Design science: baselines, ablations, field/expert evaluation tied to design propositions
- [ ] Qualitative: traceable data structure and audit trail
- [ ] Datasets anonymized and available on request to SEs/reviewers; reuse justified if applicable

## Referee pushback mapped to the analysis fix

- *"Common-method bias is not ruled out."* → Go beyond Harman's single-factor test: add a marker variable or an unmeasured method factor, and note that interaction effects are robust to method variance.
- *"Where is the correlation matrix?"* → Add the required full correlation/covariance matrix plus descriptives as an appendix; this is a JAIS submission rule, not an optional courtesy.
- *"The causal claim is not identified."* → Lead with the identifying variation, add placebo/event-study evidence and sensitivity to the key assumption, and re-estimate staggered designs with a modern estimator.
- *"You report stars, not magnitudes."* → Report effect sizes/economic magnitudes with precision and interpret what they mean for the theory.

## Worked vignette: the SEM submission that stalls on transparency (illustrative)

A behavioral paper reports a clean PLS-SEM with all paths significant, strong reliabilities, and HTMT discriminant validity — but no correlation matrix and only a Harman test for common-method bias. At JAIS this stalls twice: the missing matrix violates an explicit submission requirement (datasets and the covariance/correlation matrix must be available for SE/reviewer checking), and the single-factor CMB defense is the field's textbook example of an insufficient remedy. The fix is concrete: add the correlation/covariance matrix and descriptives as an appendix, add a marker-variable or unmeasured-method-factor analysis, report effect sizes alongside the path coefficients, and prepare the anonymized dataset for on-request checking. None of this changes the model; all of it changes whether a developmental SE can defend the paper.

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

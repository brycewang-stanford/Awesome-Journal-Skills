---
name: misq-data-analysis
description: Use when running and reporting the empirical core of a MIS Quarterly manuscript — measurement and structural models (PLS/CB-SEM) for behavioral IS, causal identification and robustness for economics-of-IS, artifact evaluation for design science, or trustworthiness for qualitative IS — and assembling the genre-appropriate transparency materials. Executes/reports the analysis; it does not design the study (misq-methods) or frame the contribution (misq-contribution-framing).
---

# Data Analysis, Evaluation & Transparency (misq-data-analysis)

## When to trigger

- Data are collected (or the artifact is built) and it is time to estimate, evaluate, and report
- A reviewer probes measurement validity, identification, artifact utility, or replicability
- You must prepare the pluralistic transparency materials uploaded at submission

## Analyze by tradition — there is no single MISQ estimator

| Tradition | What to report |
|-----------|----------------|
| **Behavioral** | Reliability (alpha/CR), CFA or PLS measurement model, AVE, discriminant validity (Fornell-Larcker / HTMT); structural paths with effect sizes; mediation via bootstrap CIs; moderation via simple slopes |
| **Economics of IS** | The identifying variation, parallel-trends/exogeneity evidence, clustered SEs, and a battery of robustness checks (alternative specifications, placebo/event-time tests, sensitivity to assumptions) |
| **Design science** | Artifact performance against credible baselines on held-out data; ablations; field/A-B or expert evaluation tied to the design propositions; cost/utility discussion |
| **Organizational / qualitative** | A transparent data structure (codes → themes → dimensions), an audit trail, and representative quotations so the path from raw data to constructs is traceable |

## Behavioral IS: defend measurement before structure

IS reviewers expect the measurement model first. PLS-SEM is common in IS for predictive/formative models; covariance-based SEM for theory-testing with reflective constructs — justify the choice. Report reliabilities, AVE, and discriminant validity, and address **common-method bias** beyond a single-factor test (marker variable, unmeasured method factor, or showing interactions survive). Then report structural paths with effect sizes, not just significance.

## Economics of IS: make the causal claim earn its keep

Lead with the identification logic, then stress-test it: alternative specifications, placebo and event-study plots, sensitivity to the key assumption, and clustering that matches the data structure. Report magnitudes and their economic meaning, not just stars.

## Design science: evaluate the artifact, not just the math

Demonstrate utility for the real problem: benchmark against the baselines a skeptic would name, run ablations to show which design principles matter, and connect each result back to a design proposition. Where possible, evaluate in a realistic field setting.

## Assemble the pluralistic transparency materials

MISQ's research-transparency policy is genre-appropriate, not a single template. Document the study's design, data, and analysis to the standard of your tradition, and include **procedures and/or code sufficient to permit replication**. The transparency commitment is declared and uploaded at submission (Step 2, Miscellaneous). Consider replication badges and the AIS Transactions on Replication Research collaboration. Plan code/data sharing within confidentiality and platform terms.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). MISQ is empirical IS — surveys, econometric panels, experiments, and design science; the chain below serves the causal / econometric lane, while design-science artifacts use their own evaluation standards.

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
- [ ] Behavioral: reliability, AVE, discriminant validity, CMB beyond single-factor; effect sizes
- [ ] Economics: identification defended, robustness/placebo tests, clustered SEs, magnitudes
- [ ] Design science: baselines, ablations, field/expert evaluation tied to design propositions
- [ ] Qualitative: traceable data structure and audit trail
- [ ] Genre-appropriate transparency package with procedures/code for replication prepared

## Anti-patterns

- Single-factor test as the sole common-method-bias defense.
- A causal claim with no identification and no robustness battery.
- A design-science "evaluation" that benchmarks against no credible baseline.
- Reporting p-values with no effect sizes or practical/economic interpretation.
- Treating transparency as an afterthought rather than genre-appropriate documentation.

## Output format

```
【Tradition & analysis】SEM / DiD-IV-RD / artifact eval / qualitative
【Validity or identification】measurement + CMB / identification + robustness / baselines + ablations
【Effect sizes / utility】magnitudes and meaning
【Transparency package】procedures/code for replication: ready/gaps
【Next step】misq-contribution-framing
```

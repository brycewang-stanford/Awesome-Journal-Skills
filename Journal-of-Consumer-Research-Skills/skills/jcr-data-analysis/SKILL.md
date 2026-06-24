---
name: jcr-data-analysis
description: Use when running and reporting the evidence for a Journal of Consumer Research (JCR) manuscript — process evidence (mediation/moderation) for behavioral experiments, or trustworthy interpretation for Consumer Culture Theory (CCT) work — plus robustness and the transparency reporting JCR requires. Executes and reports; it does not design the studies (jcr-methods).
---

# Data Analysis & Evidence (jcr-data-analysis)

## When to trigger

- Studies are run and it is time to analyze and report
- Reviewers will probe whether the data actually support the **process** claim
- You need bootstrapped indirect effects, simple-slopes, or spotlight/floodlight analyses
- You are reporting interpretive (CCT) evidence and need to defend trustworthiness

## Process evidence is the JCR currency (experiments)

For the dominant experimental tradition, JCR reviewers ask whether the data support the **psychological process**, not just the effect:

- **Mediation:** report indirect effects with **bias-corrected bootstrap confidence intervals** (e.g., 5,000 resamples). Treat measured-mediator mediation as suggestive; **moderation-of-process** and **manipulated-mediator** designs are stronger and expected for a clean process claim.
- **Moderation:** report the interaction term, then **plot simple slopes** with regions of significance; for continuous moderators use **spotlight/floodlight** analysis rather than median splits.
- **Effect sizes:** report standardized effects (Cohen's d, eta-squared, or equivalents) and discuss practical magnitude, not just p-values.
- **Across studies:** show the effect converges across populations, stimuli, and operationalizations; a small internal meta-analysis of the effect can strengthen the package.

## Reporting standards and clean inference

- Pre-specify and report **exclusion rules**, manipulation/attention-check pass rates, and final cell sizes; report all measured conditions and dependent variables (no selective reporting).
- Confirm random assignment worked (baseline balance) and that the manipulation moved the proposed mediator.
- Rule out the rival accounts named in `jcr-theory-development` with direct tests, not hand-waving.

## Interpretive (CCT) evidence: trustworthiness, not p-values

Where the design is interpretive, "analysis" means a defensible path from raw data to conceptual claims:

- Present a traceable interpretation: representative quotations/observations linked to second-order constructs and an audit trail.
- Demonstrate **triangulation, prolonged engagement, and member checks**; show the conceptual framework is grounded in the corpus.
- Make the interpretive logic transparent enough that a reader could follow how the data yielded the theory.

## Transparency reporting (JCR-specific)

JCR's research-transparency regime governs reporting: prepare the **Data Collection Statement** (where/when/who collected and analyzed the data, where stored — hidden from reviewers, published if accepted), post data and materials to an **approved repository** (OSF, Harvard Dataverse, Qualitative Data Repository, ResearchBox) as required at invited revision, supply **statistical/programming replication code** (or a written description for proprietary code), and plan to **retain data ≥ 7 years**. Consult JCR's "Research Method Transparency Guidelines and Reporting Requirements."

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JCR is predominantly lab experiments; randomization-based inference and the many-outcome family-wise correction (`romano_wolf`) are the decisive tools.

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

- [ ] Mediation via bootstrapped indirect effects; process manipulated where possible
- [ ] Moderation via simple slopes / spotlight-floodlight, not median splits
- [ ] Effect sizes reported with practical interpretation
- [ ] Exclusions, check pass rates, and all conditions/DVs reported
- [ ] Rival accounts tested directly
- [ ] CCT: triangulation, member checks, audit trail, grounded framework
- [ ] Data Collection Statement, repository deposit, and replication code prepared

## Anti-patterns

- Causal-steps "mediation" with no bootstrapped indirect effect.
- Median-splitting a continuous moderator instead of spotlight analysis.
- p-values with no effect sizes or practical meaning.
- Selective reporting of conditions, measures, or studies.
- CCT claims with no audit trail linking data to constructs.

## Output format

```
【Genre】experiments / CCT
【Effect】direction, size, convergence across studies
【Process evidence】mediation (bootstrap CI) / manipulated mediator / moderation-of-process
【Moderation】simple slopes / spotlight-floodlight
【Rivals ruled out】[...]
【CCT trustworthiness】triangulation / member checks / audit trail
【Transparency】Data Collection Statement + repository + code: ready?
【Next step】jcr-contribution-framing
```

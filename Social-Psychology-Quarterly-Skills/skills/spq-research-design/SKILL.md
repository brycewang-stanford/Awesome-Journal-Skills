---
name: spq-research-design
description: Use when defending the research design of a Social Psychology Quarterly (SPQ) manuscript — laboratory and survey experiments (group processes, status), survey and secondary-data analysis (social structure and personality), or observation/ethnography and interviews (symbolic interaction). SPQ judges each tradition on its own terms but always asks how the design captures the link between structure and the individual. Strengthens the design; it does not write code.
---

# Research Design (spq-research-design)

SPQ accepts experiments, surveys, and observational/interpretive work, but is demanding about each. The
design must credibly connect the social-psychological argument (`spq-theory-building`) to evidence about
the **structure–individual link**. This skill is tradition-aware: pick the section that matches your work
and defend it against the strongest alternative explanation.

## When to trigger

- Specifying an experimental setting, a survey/measurement plan, or a fieldwork/interview design
- A reviewer questioned causal claims, construct validity, case/site selection, or a confound
- Justifying why your design adjudicates the rival account from `spq-literature-positioning`
- Deciding how the design operationalizes the social-psychological mechanism

## Experimental (group processes, status, exchange — the lab tradition)
- **Standardized experimental settings.** State the setting (e.g., status/expectation-states paradigm,
  exchange networks) and how the manipulation realizes the theoretical construct.
- **Manipulation / standardized-setting checks**; randomization; attention checks; attrition.
- **Inference**: pre-specify primary outcomes; correct for multiple comparisons; power/MDE; appropriate
  models for nested (group/dyad) data.
- **Generalization**: be explicit about what a lab effect does and does not license about real settings.

## Survey / secondary-data (social structure and personality)
- **Measurement first.** Validate the social-psychological constructs (identity salience, mastery,
  status, sentiment); report reliability; show results aren't an artifact of a scaling choice.
- **Structural variables** measured and theorized, not just controls — the structure–individual link is
  the point.
- **Inference for complex designs**: survey weights/clustering for GSS/PSID-type data; multilevel models
  for individuals nested in contexts; sensitivity to unobserved confounding for any causal claim.

## Observational / interpretive (symbolic interaction)
- **Site / case selection** justified by analytic logic (what is this a case *of*?), not convenience.
- **Evidence and disconfirmation**: state what observations would have **challenged** the analytic claim;
  document how interaction, accounts, or fieldnotes support it.
- **Reflexivity and access**: position of the researcher, consent, and how meaning is interpreted.

## The adjudication test (SPQ-specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather than
my argument, the data would look like ___; instead they look like ___."* For experiments this is the
manipulation contrast; for surveys, the confound ruled out; for interpretive work, the alternative
reading. If you cannot, the design does not yet identify the contribution.

## Design stress ledger

Use a design stress ledger before committing to the analysis plan:

| Tradition | Stress test |
|-----------|-------------|
| Experiment | What manipulation failure, demand effect, group-composition imbalance, or dyadic dependence would overturn the status/process claim? |
| Survey / secondary data | Which omitted structural variable, measurement-invariance failure, weighting choice, or contextual clustering rule could flip the conclusion? |
| Observational / interpretive | Which negative case, deviant interaction, or access/reflexivity concern would force a narrower interpretation? |

For each row, write the planned diagnostic and the interpretation if it fails. SPQ reviewers are
comfortable with different methods, but they expect the method's limits to be explicit. A design that
names its own failure mode usually reads stronger than a design that implies no failure mode exists.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). SPQ spans lab/survey experiments and observational work; randomization inference and mediation done right matter for the experimental lane.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference, `romano_wolf` for many-outcome
  family-wise control, and `mediate` for mediation (not naive controlling-away).
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the effect size in interpretable units; route the full battery to the
appendix/supplement. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A lab effect over-generalized to real-world structure with no caveat
- Treating structural variables as nuisance controls rather than theorized causes
- Convenience site selection dressed up as theory-driven
- "Causal" language on a cross-sectional survey that only supports association
- A design that cannot distinguish your social-psychological mechanism from the leading alternative

## Output format

```
【Tradition】experiment / survey-SSP / observation-interpretive
【Estimand or analytic claim】what is identified/shown about the structure–individual link
【Key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Measurement / setting validity】constructs validated or setting standardized? [Y/N]
【Robustness/sensitivity】planned checks
【Next】spq-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — experimental, survey, measurement, and CAQDAS tooling by tradition
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — SPQ scope and methods breadth

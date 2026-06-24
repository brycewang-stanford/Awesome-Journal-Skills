---
name: jams-methods
description: Use when matching the research design to the claim for a Journal of the Academy of Marketing Science (JAMS) manuscript — construct validity and measurement, survey/SEM design, secondary-data identification, experiments, or meta-analysis. Designs the study and stress-tests validity; jams-data-analysis executes and reports the estimates.
---

# Research Design, Measurement & Identification (jams-methods)

## When to trigger

- The design may not actually support the theoretical claim
- Constructs are measured but scale validity (reliability, convergent, discriminant) is unestablished
- A causal claim rests on a cross-sectional survey or OLS-with-controls
- Reviewers will probe common method variance, endogeneity, manipulation validity, or coding reliability

## Match design to claim by genre

JAMS publishes several empirical genres; the validity question is genre-specific. Pick the genre, then clear its bar.

### Survey + SEM/PLS (strategy, B2B, services, branding)
- **Construct validity is the gate.** Report reliability (composite reliability / Cronbach's α), **convergent validity** (AVE ≥ .50, loadings), and **discriminant validity** (Fornell–Larcker and/or the **HTMT** ratio — JAMS reviewers increasingly expect HTMT).
- **Common method variance (CMV):** design against it (temporal/source separation, marker variable) and test for it (Harman is weak — prefer a marker-variable or CFA-marker approach). CMV is a top reason survey papers stall at JAMS.
- **Measurement before structure:** establish the measurement model (CFA) before interpreting the structural model; report fit (χ²/df, CFI, TLI, RMSEA, SRMR).
- **Formative vs. reflective:** justify the specification; do not run a reflective CFA on a formative construct.
- **Endogeneity in survey models:** a clean SEM does not buy causality — address it (instruments, Gaussian-copula control, panel design) where the claim is causal.

### Secondary-data econometrics (scanner, CRM, marketing–finance)
- **Identification is the gate.** Name the strategy the variation supports — DiD (modern staggered estimators), IV/2SLS, RDD, matching, control function — and defend the exclusion / parallel-trends / continuity assumption explicitly.
- Address **endogeneity of marketing actions** (price, advertising, entry are chosen, not random); a lagged regressor is not identification.
- Cluster inference at the assignment level; report first-stage strength / pre-trends as relevant.

### Behavioral experiment
- **Manipulation validity:** clean operationalization, manipulation and attention checks, pretested stimuli.
- **Mechanism, not just effect:** measured-or-manipulated **mediation** and **process-by-moderation**; power sized for the *interaction*, not the main effect.
- **Multi-study logic:** lab establishes the mechanism; a field study or a consequential outcome adds external validity (a JAMS strength).

### Meta-analysis
- Pre-specified **sampling frame** and search protocol; transparent inclusion/exclusion.
- **Inter-coder reliability** reported; effect-size metric and artifact corrections justified.
- **Moderator analysis** that tests the theory, plus publication-bias diagnostics.

## Construct validity is JAMS's most-policed area

Because so many JAMS papers are survey-based, the measurement model is where reviewers concentrate fire. Make the chain airtight: each construct has a **conceptual definition** first, then a measure whose items match that definition (content validity), then evidence of **reliability** (CR/α), **convergent validity** (AVE ≥ .50, significant loadings), and **discriminant validity**. For discriminant validity, report **HTMT** (threshold typically .85/.90) in addition to Fornell–Larcker — reviewers increasingly treat Fornell–Larcker alone as insufficient. If you adapt an existing scale, justify the changes and re-validate; if you create a new scale, follow a recognized scale-development procedure (item generation, purification, validation on a fresh sample). A reflective construct measured with formative items (or vice versa) is a fatal mismatch.

## Tie the design back to the claim and the manager

A method is "JAMS-ready" only when it supports both the theoretical claim and the managerial reading. After choosing the design, write one line: *the variation / manipulation that identifies the focal effect*, and one line: *the managerial quantity the estimates will produce*. If the design cannot deliver a managerially interpretable magnitude (e.g., a standardized path with no translatable unit), plan now to add a study, an elasticity, or a scenario analysis — discovering this after data collection is expensive. Hand the executed plan to `jams-data-analysis`, which carries the same managerial-magnitude discipline into reporting.

## Sample, power, and data provenance

- **Sample frame and response.** For surveys, justify the sampling frame, report the response rate, and test for **non-response bias** (e.g., early-vs-late respondents) and **informant quality** (key-informant competence for B2B/firm-level constructs).
- **Power.** Size the study for the effect that carries the contribution — usually an **interaction or an indirect effect**, which needs more power than a main effect. State the a priori power analysis.
- **Provenance.** Name the data source (panel/scanner such as NielsenIQ/Circana, CRM, a field partner, a Prolific/Qualtrics panel) and document sample construction, screening, and any exclusions — JAMS reviewers and the data-availability policy both expect a clear data trail.
- **Multi-source / multi-wave designs** strengthen both causal credibility and the CMV defense; flag where a single-source cross-section limits the causal claim and adjust the language accordingly.

## Pre-registration and replicability

For experiments and field studies, pre-registration (AsPredicted / OSF) strengthens the inference and pre-empts a HARKing or *p*-hacking critique; report any deviations from the plan. Across all genres, design the data and analysis pipeline now so it can satisfy the Springer data/code availability policy at acceptance — keep raw data, cleaning scripts, and estimation code organized and documented from the start rather than reconstructing them under deadline. A clean, shareable pipeline is also the cheapest insurance against a reviewer who asks to see a specific robustness check.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAMS is empirical marketing with much survey-based SEM; the chain below serves causal / quasi-experimental designs and many-outcome corrections.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate the checks the design owes.
- **Panel / staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition`
  + `honest_did_from_result`. **IV:** `effective_f_test` + `anderson_rubin_ci`. **RDD:**
  `rdrobust` + `mccrary_test`.
- **Experiments:** randomization-based inference and `romano_wolf` for the many-outcome
  family-wise correction reviewers expect.

Match the toolchain to the **reviewer pool**, and report the effect size the venue
wants. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Genre named; design matched to the causal/behavioral/structural claim
- [ ] Survey: reliability + AVE + discriminant validity (Fornell–Larcker / HTMT) reported
- [ ] Survey: CMV designed against and tested (not Harman alone)
- [ ] Measurement model validated before the structural model; fit indices reported
- [ ] Secondary data: identification strategy named and its key assumption defended
- [ ] Experiment: manipulation/attention checks; mediation + moderation; power for interaction
- [ ] Meta: coding reliability + moderators + publication-bias checks
- [ ] Causal language never exceeds what the design identifies

## Anti-patterns

- Treating a good-fitting SEM as evidence of causality
- Discriminant validity by Fornell–Larcker only when HTMT would fail
- Harman's single-factor test offered as the whole CMV defense
- Endogenous marketing regressors with a lagged variable passed off as a fix
- A single-cell or confounded manipulation that cannot isolate the cause
- A meta-analysis with no inter-coder reliability or publication-bias check

## Output format

```text
【Genre】survey-SEM / secondary-data / experiment / meta-analysis
【Claim】causal / structural / descriptive
【Construct validity】reliability + AVE + discriminant (FL/HTMT): pass/fix
【CMV (survey)】design + test (marker/CFA-marker): pass/fix/NA
【Identification (secondary)】strategy + key assumption: [...] / NA
【Experiment】manipulation + mediation + moderation + power: pass/fix/NA
【Meta】frame + coding reliability + bias checks: pass/fix/NA
【Next skill】jams-data-analysis
```

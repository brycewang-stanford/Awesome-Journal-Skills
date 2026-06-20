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

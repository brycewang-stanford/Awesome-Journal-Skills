---
name: lancet-statistics
description: Use to enforce The Lancet's clinical-statistics reporting — confidence intervals over bare P values, a pre-specified primary analysis, intention-to-treat with per-protocol sensitivity, multiplicity control for secondary endpoints, cautious pre-specified subgroup analyses with interaction tests, missing-data handling, and absolute plus relative effects.
---

# Clinical Statistics (lancet-statistics)

## When to trigger

- Results report P values but not confidence intervals or effect sizes.
- The primary analysis population (ITT vs per-protocol) is unclear.
- Many secondary endpoints or subgroups are reported with no multiplicity/interaction handling.
- A **statistical reviewer** is likely (The Lancet uses them) and the analysis is not pre-specified.

## The reporting backbone (every clinical estimate)

Each estimate needs: **effect measure + 95% CI + the analysis population + the pre-specified test.**

- [ ] **Confidence intervals** for every key estimate — CIs over bare P values; The Lancet de-emphasises isolated significance.
- [ ] **Exact P values** (e.g., p=0·013), not "p<0·05," reported alongside CIs, not instead of them.
- [ ] **Absolute and relative effects**: report the absolute risk/rate difference *and* the relative measure (RR/OR/HR); add **NNT/NNH** where clinically relevant.
- [ ] **Analysis population stated**: ITT as the primary population for superiority RCTs.
- [ ] The **test/model named** and matched to outcome type (survival → Cox/log-rank; binary → logistic/risk; count → Poisson/negative binomial; clustered → mixed/GEE).

## Pre-specification and the primary analysis

- The **primary analysis is pre-specified** in the SAP (see `lancet-study-design`) before unblinding.
- Report the pre-specified primary analysis first; clearly label any post-hoc analysis as post-hoc.
- For **non-inferiority/equivalence** trials: state the margin, justify it, and analyse both ITT and per-protocol (per-protocol matters here).

## ITT and sensitivity analyses

- **ITT** primary; **per-protocol** as a pre-specified sensitivity analysis (especially for non-inferiority).
- Report **missing data** explicitly: amount, pattern, and the handling method (e.g., multiple imputation), with sensitivity analyses under different assumptions. Do not silently use complete-case only.

## Multiplicity and secondary endpoints

- Control for **multiplicity** across multiple primary/secondary endpoints (hierarchical testing, alpha-splitting, or correction) and state the strategy.
- Secondary endpoints are **supportive**, not confirmatory, unless pre-specified within a multiplicity-controlled hierarchy — say so.

## Subgroups — pre-specified and cautious

- Report only **pre-specified** subgroups; label any post-hoc subgroup as exploratory.
- Test the **interaction** (treatment × subgroup), not separate within-subgroup P values — and interpret cautiously; subgroup claims are a classic over-interpretation trap.
- Present subgroups in a **forest plot** with interaction P values (see `lancet-figures-tables`).

## Survival and time-to-event

- Kaplan–Meier estimates with **numbers at risk**; hazard ratios with 95% CI from Cox models; state the proportional-hazards assumption check.

## What the Lancet statistical reviewer expects

The Lancet routinely assigns an **independent statistical reviewer** whose report is a distinct, high-priority track. They read for pre-specification first (primary analysis matching the registered outcome and the SAP filed before unblinding), expect confidence intervals to carry the inference with exact P beside them, and want the absolute effect reported beside the relative one. Within-subgroup P values and per-protocol-as-primary for a superiority trial draw the sharpest scrutiny. Confirm current expectations against the journal's author guidelines.

## Worked micro-example (illustrative numbers — not real data)

A hypothetical superiority RCT, binary primary outcome (response at 12 weeks), ITT population.

```
Primary (illustrative, ITT): response 612/1 020 (60.0%) vs 510/1 016 (50.2%)
  Absolute risk difference 9.8 pp (95% CI 5.4-14.2); RR 1.20 (95% CI 1.10-1.30)
  Exact p=0.0003; NNT ~10 (illustrative)
Sensitivity (per-protocol): RD 12.1 pp (95% CI 7.3-16.9) -> consistent with ITT.
Subgroups: 5 pre-specified; forest plot, interaction p=0.28 (no heterogeneity).
```

The CI and absolute risk difference carry the inference, the NNT makes the magnitude clinical, and the single interaction P keeps the subgroups honest.

## Reviewer-pushback patterns and the venue-specific fix

- *"P values but no effect sizes with CIs."* → Add the effect with a 95% CI for every key estimate; keep exact P beside, not instead of, the interval.
- *"Primary analysis differs from the registered outcome."* → Reconcile to the registered outcome and SAP, or explain the dated change; label anything post-hoc.
- *"Subgroup claims rest on within-subgroup P values."* → Replace with interaction tests on pre-specified subgroups; interpret cautiously.

## Output format

```
【Per-estimate backbone】 effect measure + 95% CI / analysis population / test  → list gaps
【CIs over bare P?】 yes/no   【Exact P reported?】 yes/no
【Absolute + relative effects (NNT where relevant)?】 yes/no
【Primary analysis pre-specified + ITT?】 yes/no
【Missing data handled + sensitivity?】 yes/no
【Multiplicity strategy for secondary endpoints?】 stated / missing
【Subgroups pre-specified + interaction tested + cautious?】 yes/no
【Survival: KM + numbers at risk + HR(CI)?】 yes/no/NA
【Next】 lancet-figures-tables
```

## Anti-patterns

- **Do not** report P values without confidence intervals or effect sizes.
- **Do not** report only a relative effect (HR/OR/RR) when the absolute effect changes the clinical message.
- **Do not** present per-protocol as the primary analysis for a superiority trial.
- **Do not** mine subgroups: separate within-subgroup P values without an interaction test invite over-interpretation.
- **Do not** infer "no effect" from a non-significant result in an underpowered analysis.

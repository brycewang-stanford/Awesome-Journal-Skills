---
name: jama-statistics
description: Use when preparing or auditing the statistical analysis and reporting of a JAMA manuscript so it survives JAMA's dedicated statistical review. Enforces effect sizes with 95% CIs, multiplicity control, and pre-specification; it does NOT choose the study design or write prose.
---

# Statistics & Statistical Review (jama-statistics)

## When to trigger

- Results report p-values without effect sizes or confidence intervals
- Many comparisons but no multiplicity plan
- The analysis was not pre-specified, or outcomes drifted from the protocol
- Preparing for JAMA's **dedicated statistical review** of accepted-pending manuscripts

## Core reporting rules at JAMA

1. **Effect sizes with 95% CIs, not p-values alone.** Report the estimate (mean difference, risk/hazard/odds ratio, absolute risk difference) **with its 95% CI**. P-values supplement; they do not substitute. Treat "significance" as a statement about the interval, not a 0.05 threshold ritual.
2. **Pre-specified outcomes.** State the single primary outcome and the secondary outcomes exactly as registered/protocoled. Flag any post hoc analysis as exploratory.
3. **Intention-to-treat for RCTs.** Primary analysis is ITT; per-protocol and as-treated are secondary/sensitivity.
4. **Multiplicity.** With multiple outcomes, subgroups, or time points, pre-specify the testing hierarchy and the correction (e.g., hierarchical testing, Bonferroni/Holm, gatekeeping). Subgroups without a multiplicity plan are hypothesis-generating only.
5. **Missing data.** State the mechanism assumed and the method (e.g., multiple imputation); report a sensitivity analysis. Complete-case-only needs justification.
6. **Model assumptions.** Justify the model (proportional hazards, linearity, clustering, repeated measures) and report how assumptions were checked.
7. **Absolute and relative effects.** Pair relative measures (RR, OR, HR) with absolute measures (risk difference, NNT) so clinicians grasp magnitude.

## Reporting conventions to follow

- Report exact p-values (e.g., P = .03), not "P < .05"; very small as "P < .001"
- Round sensibly; do not imply false precision
- Give denominators with every percentage; report n/N
- Pre-register and report the analysis population for each estimate
- Describe software and key procedures so the analysis is reproducible
- For meta-analysis: report heterogeneity (e.g., I²), the model (fixed/random), and sensitivity analyses

## Audit table

| Symptom                                          | Fix                                                  |
|--------------------------------------------------|------------------------------------------------------|
| "P < 0.05" with no estimate                      | Add point estimate + 95% CI                          |
| Five "key" secondary outcomes, all "significant" | Pre-specify hierarchy; correct for multiplicity      |
| Subgroup result drives the conclusion            | Label exploratory; report interaction test           |
| RCT analyzed per-protocol as primary             | Re-run ITT as primary                                |
| 20% dropout, complete-case only                  | Multiple imputation + sensitivity analysis           |
| Only relative risk reported                      | Add absolute risk difference / NNT                   |

## Surviving JAMA's independent statistical review

The Journal of the American Medical Association applies a dedicated statistical review to manuscripts under serious consideration — distinguishing it among general medical journals. Independent statisticians re-interrogate the analysis, so pre-empt the standard queries: a pre-specified primary outcome matching the registry; intention-to-treat as primary; pre-specified multiplicity control; missing data handled by imputation with sensitivity analysis; and an absolute effect (risk difference / NNT) beside every relative measure.

## Worked example: a primary-outcome readout (illustrative)

Vignette (illustrative): a multicenter, double-blind randomized clinical trial, N = 5,000 adults with type 2 diabetes and cardiovascular disease, new agent vs placebo; pre-specified primary outcome major adverse cardiovascular events (MACE) over a median 3.1 years.

- ITT result: 11.2% vs 13.6%; absolute risk difference -2.4 percentage points (95% CI, -4.3 to -0.5); hazard ratio 0.82 (95% CI, 0.70-0.96); P = .01.
- Correct readout: relative (HR with CI) and absolute (risk difference, ~42 NNT) effects both given, ITT, primary matches the registry; a "significant" secondary subgroup stays labeled exploratory with its interaction test.

## Reviewer pushback and the JAMA fix

- "Primary outcome changed post hoc." Fix: restore the registered primary; demote the swap to labeled exploratory.
- "Subgroup result drives the conclusion." Fix: report the interaction test, label it hypothesis-generating, re-anchor on the primary.

Calibration anchors (hedge where uncertain): estimate-plus-95%-CI over bare p-values, ITT-as-primary, pre-specification, and absolute-with-relative reporting are durable; notation rules track the AMA Manual of Style — confirm against current author guidelines.

## Checklist

- [ ] Every primary/secondary estimate has a 95% CI
- [ ] Single pre-specified primary outcome; secondaries labeled
- [ ] Multiplicity handled with a pre-specified plan
- [ ] ITT is the primary analysis for the RCT
- [ ] Missing-data method stated + sensitivity analysis
- [ ] Absolute and relative effects both reported
- [ ] Model assumptions justified and checked
- [ ] Analysis is reproducible (software, code/procedures described)

## Anti-patterns

- Reporting p-values without effect sizes or CIs
- Switching or under-reporting pre-specified outcomes
- Mining subgroups and reporting only the "significant" one
- Claiming "no difference" from an underpowered study (absence of evidence ≠ evidence of absence)
- Per-protocol-as-primary to make an RCT look better
- Conclusions built on a secondary outcome while the primary was null

## Output format

```
【Primary outcome estimate + 95% CI】...
【All estimates have CIs】yes / no
【Multiplicity plan】... 
【ITT primary (RCT)】yes / no / n.a.
【Missing-data handling】...
【Absolute + relative effects reported】yes / no
【Stat-review risks remaining】...
【Next skill】jama-figures-tables
```

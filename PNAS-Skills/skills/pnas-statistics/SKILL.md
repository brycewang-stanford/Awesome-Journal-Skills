---
name: pnas-statistics
description: Use to enforce PNAS's statistics and reproducibility reporting — n and replication, test choice and assumptions, effect sizes with uncertainty, multiple-comparison control, randomization/blinding, sample-size justification, pre-registration where relevant, and reproducible code.
---

# Statistics & Reproducibility (pnas-statistics)

## When to trigger

- Results report P values but not effect sizes or n.
- "Three independent experiments" is claimed but replication is unclear.
- Multiple comparisons are run with no correction.
- A reviewer is likely to ask "were analyses pre-specified?" and there's no answer.
- The analysis is not reproducible from the deposited code (`pnas-data`).

## The reporting backbone (every quantitative claim)

Each claim needs: **effect size + uncertainty + n + test + what n means.**

- [ ] **n** stated, with the unit of replication (biological vs technical replicates; cells vs animals vs subjects vs experiments).
- [ ] **Effect size** with **95% CI** (preferred) or SD/SEM clearly labeled — not P alone.
- [ ] **Exact P values** (e.g., P = 0.013), not "P < 0.05", unless extremely small.
- [ ] **Test named and justified** (assumptions checked: normality, variance homogeneity, independence).
- [ ] **Multiple comparisons** corrected (Bonferroni/Holm/FDR) when many tests are run.

## Replication and design

- Distinguish **biological replication** (independent samples) from **technical replication** (re-measurement). The former is what counts.
- State **how the sample size was chosen** (power analysis or explicit rationale), not post-hoc.
- Report **randomization** of subjects/treatments and **blinding** of measurement/analysis where applicable, or state why not.
- Report **inclusion/exclusion criteria** and any excluded data, with reasons, decided in advance.

## Discipline-specific notes across PNAS divisions

PNAS spans **Biological, Physical, and Social Sciences**, so match the rigor conventions of your division:

- **Biological:** replication unit, ARRIVE-style animal reporting, antibody/reagent validation.
- **Social/behavioral:** pre-registration is increasingly expected; report power, sampling frame, and deviations from the plan.
- **Physical/computational:** report uncertainties, error propagation, and numerical reproducibility (seeds, solver settings).

## Avoid the classic reviewer kills

- **Pseudoreplication**: treating technical replicates / cells from one animal as independent n.
- **HARKing / p-hacking**: presenting exploratory findings as confirmatory. Label exploratory work as such.
- **"Representative" images** with no quantification across replicates.
- **Bar chart + SEM** masking a tiny, variable n.
- Comparing two effects by their **significance** ("significant here, not there") instead of testing the **difference**.

## Reproducibility package

- Analysis code in a repository (see `pnas-data`), with a README and environment/versions.
- A reproducibility/reporting summary if requested; list software, versions, seeds.
- Deterministic where possible; report random seeds for simulations/ML.

## Pre-registration & transparency (where relevant)

- For confirmatory studies (especially human-subjects / behavioral work in the Social Sciences division), note **pre-registration** (OSF/AsPredicted) if done.
- Separate pre-specified analyses from post-hoc exploration explicitly in the text.

## Before / after: a reporting sentence in PNAS register

PNAS reviewers span divisions, so a statistics sentence has to survive a reader who does not share your field's shorthand. Tighten a vague claim into the reporting backbone.

- **Before:** "Treatment significantly increased expression (P < 0.05, n = 3), confirming our hypothesis."
- **After:** "Treatment raised expression 2.4-fold (95% CI 1.7–3.3; two-sided Welch's t test, P = 0.008; n = 6 biological replicates, each the mean of 3 technical replicates), consistent with the predicted mechanism."

The revision names the effect and its uncertainty, states the unit of replication, gives an exact P, and separates biological from technical n — the four things a PNAS editor flags when a general-audience claim rests on thin evidence.

## PNAS editor / referee expectation checklist

What a PNAS handling editor and cross-division referees actively look for:

- [ ] **Broad significance is earned, not asserted** — the statistical advance supports the general claim in the Significance Statement, not a narrower one.
- [ ] **Reporting standards met** — every panel's n, test, and error definition appears in its legend, not buried in Methods.
- [ ] **Reproducibility** — a referee could re-run the analysis from deposited code, versions, and seeds (`pnas-data`).
- [ ] **Data availability** — primary data underlying each quantitative figure is deposited, not "available on request."
- [ ] **No selective reporting** — exploratory and confirmatory analyses are labeled; excluded data and its rationale are disclosed.

## Output format

```
【Per-claim backbone】 effect+CI / n / unit-of-n / test / assumptions → list gaps
【Replication】 biological vs technical clear? yes/no
【Sample-size rationale】 power/justification present? yes/no
【Randomization & blinding】 reported / N/A-justified / missing
【Multiplicity】 corrected? method
【Division-specific rigor】 (Bio / Physical / Social) conventions met? yes/no
【Reproducibility】 code + versions + seeds present? yes/no
【Next】 pnas-data
```

## Anti-patterns

- **Do not** report P without effect size and n.
- **Do not** count technical replicates as independent observations.
- **Do not** infer "no effect" from a non-significant test on an underpowered sample.
- **Do not** present post-hoc subgroup findings as if pre-specified.

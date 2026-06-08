# Reviewer Objection Checklist (empirical social science)

A cross-cutting, venue-neutral map of the objections referees actually raise at
top empirical journals (economics, finance, management, marketing, political
science, sociology), organized by identification strategy. Each entry is a
*standard attack* plus the *preemption* that defuses it before review. Use it to
stress-test a design before drafting tables, and to anticipate the referee report.

> How to read this: if you cannot answer an objection in one paragraph + one
> table/figure, the design has a hole. "We control for it" is rarely an answer to
> an identification objection — it is an admission that the variation is not clean.

---

## 0. The four questions behind every objection

Every empirical referee objection reduces to one of:

1. **Selection / endogeneity** — is the treatment (or the right-hand-side variable
   of interest) as-good-as-randomly assigned *conditional on what you condition on*?
2. **Exclusion / confounding** — is there another channel from your source of
   variation to the outcome that you have not shut down?
3. **Inference** — are the standard errors honest about the actual dependence and
   the number of effective clusters / the multiplicity of tests?
4. **External validity / interpretation** — does the estimated parameter answer
   the question the paper claims to answer (LATE vs ATE, partial vs general
   equilibrium, short vs long run)?

If you can name which of these four a robustness check addresses, it belongs in
the paper. If you cannot, it is decoration.

---

## 1. Difference-in-Differences (incl. staggered adoption)

**Attack 1 — "Your TWFE estimate is contaminated by negative weights."**
With staggered timing, two-way fixed effects uses already-treated units as
controls, which can flip the sign under heterogeneous effects (Goodman-Bacon
2021; de Chaisemartin & D'Haultfoeuille 2020).
→ Preempt: report a **Goodman-Bacon decomposition** to show the weight on "bad
comparisons," then make a **heterogeneity-robust estimator the main result**
(Callaway & Sant'Anna 2021; Sun & Abraham 2021; Borusyak-Jaravel-Spiess 2024;
Gardner 2022; de Chaisemartin & D'Haultfoeuille). TWFE becomes a familiar
benchmark, not the headline.

**Attack 2 — "Parallel trends is assumed, not tested."**
→ Preempt: an **event-study plot** (reference period t−1, 95% CI, treatment line),
with pre-period coefficients jointly tested ≈ 0. Add a **pre-trends power /
sensitivity** analysis (Roth 2022; Rambachan & Roth 2023 honest DiD) rather than
relying on "the pre-trend is flat to the eye."

**Attack 3 — "Anticipation / forward-looking behavior."**
Units respond before the official treatment date.
→ Preempt: bin or drop the period(s) just before treatment; show robustness to
shifting the event window; discuss the institutional timing.

**Attack 4 — "Your control group is endogenous to treatment."**
Never-treated units differ systematically; or treatment timing is itself a choice.
→ Preempt: use not-yet-treated as controls; show covariate balance; discuss why
timing is plausibly exogenous (and run a placebo on timing — see §7).

**Checklist**
- [ ] Bacon decomposition + at least one heterogeneity-robust estimator as main
- [ ] Event study with reference period, joint pre-trend test, honest-DiD sensitivity
- [ ] Anticipation addressed; control-group choice justified
- [ ] SE clustered at the level of treatment assignment (§ Reporting Standards)

---

## 2. Instrumental Variables

**Attack 1 — "Weak instrument; F > 10 is not enough."**
The "F>10" rule (Staiger-Stock) is not valid under heteroskedasticity/clustering
and understates the problem with multiple instruments.
→ Preempt: report the **Kleibergen-Paap rk Wald F** (robust/clustered), compare to
**Stock-Yogo** critical values, and for a single endogenous regressor the
**effective F** (Montiel Olea & Pflueger 2013). Provide **weak-IV-robust
inference**: Anderson-Rubin confidence sets (fully robust under just-identification).

**Attack 2 — "The exclusion restriction is not credible."**
The instrument plausibly affects the outcome through a second channel.
→ Preempt: argue exclusion in **three registers** — theory, institution, and a
placebo/falsification test — and **report the reduced form** (if the reduced form
is null, the IV "result" is noise amplified by a weak first stage).

**Attack 3 — "You interpret LATE as if it were ATE."**
→ Preempt: state the **complier population**; discuss monotonicity; do not claim
policy effects for never-takers.

**Attack 4 — "Bartik / shift-share: where does identification come from?"**
→ Preempt: be explicit whether identification is from **shares** (Goldsmith-Pinkham,
Sorkin & Swift 2020) or **shocks** (Borusyak, Hull & Jaravel 2022); report
Rotemberg weights or shock-level balance accordingly.

**Checklist**
- [ ] KP rk F + effective F + Stock-Yogo comparison
- [ ] Anderson-Rubin (and/or CLR) robust CI; reduced form reported
- [ ] Exclusion argued in 3 registers; LATE/complier interpretation stated
- [ ] Shift-share identification source named and diagnosed

---

## 3. Regression Discontinuity

**Attack 1 — "You only report conventional CIs."**
→ Preempt: report **robust bias-corrected CIs** (Calonico-Cattaneo-Titiunik 2014)
as the main estimate, with an MSE-optimal bandwidth.

**Attack 2 — "Manipulation / sorting at the cutoff."**
→ Preempt: **density test** (Cattaneo-Jansson-Ma `rddensity`, which supersedes
McCrary 2008); show no bunching; discuss who controls the running variable.

**Attack 3 — "The result is a bandwidth artifact."**
→ Preempt: show stability across **≥3 bandwidths**, a **donut RD**, alternate
kernels/polynomial orders, and **placebo cutoffs** at non-threshold values.

**Attack 4 — "Covariates jump at the cutoff."**
→ Preempt: run the RD on pre-determined covariates — they should *not* jump.

**Checklist**
- [ ] Robust bias-corrected CI (main); MSE-optimal bandwidth
- [ ] rddensity manipulation test; covariate-continuity (placebo outcomes)
- [ ] ≥3 bandwidths, donut, placebo cutoffs
- [ ] Fuzzy RD: first-stage strength reported as in §2

---

## 4. Double / Debiased ML & causal forests

**Attack 1 — "Regularization bias / overfitting."**
→ Preempt: use **Neyman-orthogonal scores + cross-fitting** (Chernozhukov et al.
2018); report number of folds (5 or 10) and the nuisance learners.

**Attack 2 — "Results depend on the learner."**
→ Preempt: show the point estimate is **stable across learners** (lasso, random
forest, gradient boosting) — ideally an ensemble/stacking.

**Attack 3 — "This is just a flexible OLS; where is the identification?"**
→ Preempt: DML relaxes functional form, **not** the unconfoundedness assumption —
state the conditional-ignorability argument explicitly. ML is not an identification
strategy.

**Checklist**
- [ ] Orthogonal score + cross-fitting (K stated); learner robustness
- [ ] Identification (unconfoundedness/overlap) argued separately from the ML

---

## 5. Matching / selection-on-observables / panel FE

**Attack 1 — "Selection on unobservables."**
→ Preempt: bound it — **Oster (2019)** δ / coefficient-stability, or
Altonji-Elder-Taber; report how much selection on unobservables (relative to
observables) would be needed to null the result.
**Attack 2 — "Bad controls / post-treatment conditioning."**
→ Preempt: separate pre-determined controls from outcomes-of-treatment; show the
result without the suspect controls.
**Attack 3 — "Two-way FE ≠ causal."** State the identifying within-variation.

**Checklist**
- [ ] Oster / sensitivity to unobservables; no bad controls; overlap shown

---

## 6. Mechanism / mediation

**Attack — "Your mediation regression (X→M→Y) is not identified."**
Controlling for a mediator induces collider/selection bias; the M→Y step is
rarely as-good-as-random.
→ Preempt: estimate the cleanly identified **D→M** step; argue **M→Y** from theory
and prior evidence rather than a contaminated mediation coefficient. Treat
mechanism as *narrowing the set of explanations*, not a second causal estimate.

---

## 7. Falsification / placebo (applies to all designs)

- **Placebo outcome** — an outcome that should *not* move under the true mechanism.
- **Placebo treatment / timing** — randomly reassign treatment 500–1000×; the true
  coefficient should sit in the tail of the permutation distribution.
- **Placebo population** — a group the treatment should not reach.
- A design that passes one placebo and fails another is informative; report both.

---

## 8. Inference (the objection that sinks "clean" designs)

- **Clustering** at the level of treatment assignment (not the unit of observation).
- **Few clusters (< ~40):** wild cluster bootstrap (Cameron-Gelbach-Miller; `boottest`).
- **Two-way / spatial dependence:** two-way clustering or Conley spatial HAC.
- **Multiple hypotheses:** Romano-Wolf / List-Shaikh-Xu or sharpened FDR q-values
  when reporting many outcomes/subgroups — referees increasingly demand this.
See `reporting-standards.md` for the exact commands and thresholds.

---

## 9. The "so what" objections (desk-reject risks)

- **"Identified but uninteresting."** A clean null on a question no one asked still
  gets rejected. Tie the parameter to a first-order economic/theoretical question.
- **"Magnitude not interpreted."** Report effect sizes in interpretable units and
  benchmark against the literature, not just stars.
- **"Partial-equilibrium estimate, general-equilibrium claim."** Match the claim to
  what the design can support.

---

*Provenance: distilled from the modern applied-methods literature and from the
verified estimator chains in `shared-resources/empirical-methods/code/`. Venue-
neutral; pair with each journal's `official-source-map.md` for venue-specific
reporting requirements.*

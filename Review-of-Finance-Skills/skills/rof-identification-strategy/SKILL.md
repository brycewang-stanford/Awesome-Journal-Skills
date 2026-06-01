---
name: rof-identification-strategy
description: Use when the credibility core of a Review of Finance (RoF) manuscript is the bottleneck — causal identification for empirical finance (DID, IV, RDD, event study, natural experiments) OR assumptions, results, and proof exposition for theoretical finance. Stress-tests the design or model to the top-three-finance-journal standard.
---

# Identification & Theory Strategy (rof-identification-strategy)

## When to trigger

- The empirical core is panel regressions with controls and an undefended causal claim
- A DID uses two-way fixed effects on staggered timing without modern estimators
- An IV's first stage is weak or its exclusion restriction is unargued
- The paper is **theoretical** and the assumptions, generality, or proof exposition are the weak link

## The RoF credibility bar

RoF referees apply **top-three-finance-journal standards** to the inferential or logical spine. Because RoF publishes **both empirical and theoretical** finance, "identification" means two different things — pick the branch matching your paper.

### Branch E1 — Empirical: causal design for finance

- **Natural experiments / shocks**: regulatory changes, index reconstitutions, staggered law adoption. Name the identifying variation in one sentence and defend its exogeneity.
- **DID / event study**: under staggered adoption, move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); report a Goodman-Bacon decomposition and clean pre-trends.
- **IV**: strong first stage (report F); weak-IV-robust inference when needed; defend the exclusion restriction on economic, institutional, and falsification grounds.
- **RDD**: density/manipulation test, optimal bandwidth plus robustness, covariate smoothness.
- **Asset-pricing inference**: correct standard errors (Newey–West, two-way clustering, Shanken for Fama–MacBeth); guard against data-snooping in factor/anomaly work; cluster at the assignment level.

### Branch T1 — Theoretical: assumptions, results, proof exposition

- **Assumptions**: state them economically; flag substantive vs. technical; discuss what breaks if each is relaxed.
- **Results**: lead with the proposition and its economic message, not the algebra; show it is **non-obvious** and **general** enough to matter.
- **Proof exposition**: keep proofs self-contained in an appendix with intuition in the body; proofs count against the **60-page cap**.
- **Numerical work**: report solver tolerances, convergence, and seeds (see `rof-replication-and-data-policy`).

## Anti-patterns

- TWFE on staggered treatment with no heterogeneity-bias discussion.
- An anomaly "discovered" via repeated sorts with no multiple-testing or out-of-sample discipline.
- A theory result that is true by assumption, dressed in heavy notation.
- Over-claiming a local empirical estimate as a universal law, or a knife-edge model as general.

## Output format

```
【Branch】empirical (E1) / theory (T1)
【Spine】identifying variation OR key assumption+result
【Diagnostics done / missing】[...]
【Inference / rigor】clustering & SE OR proof completeness
【Over-claim check】never exceeds design/model? [Y/N]
【Next step】rof-data-analysis
```

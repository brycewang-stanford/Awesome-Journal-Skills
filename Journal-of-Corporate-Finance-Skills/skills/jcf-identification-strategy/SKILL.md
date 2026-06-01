---
name: jcf-identification-strategy
description: Use when designing or defending the causal identification strategy for a Journal of Corporate Finance (JCF) empirical paper — choosing and stressing a design (DID/staggered shocks, IV/GMM, RDD, event study, matching) for firm-level data with endogenous corporate decisions. It evaluates and hardens the design; it does not run the regressions.
---

# Identification Strategy (jcf-identification-strategy)

## When to trigger

- Picking a credible design for a corporate-finance question with endogenous choices
- Pre-empting the referee's "your X is endogenous / reverse-causal" objection
- Defending parallel trends, exclusion restrictions, or window cleanliness

## Why JCF needs a real design

Corporate-finance variables (leverage, governance, payout, M&A) are **choices**, so OLS-with-controls invites endogeneity, omitted-variable, and reverse-causality critiques. JCF is empirical corporate finance: a clean identification strategy is what separates a publishable paper from a desk reject. Match the design to the source of variation.

## Design menu (corporate finance)

- **Staggered DID** around law/regulation/governance shocks — use **modern estimators** (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille), run **Goodman-Bacon** diagnostics, show **event-study leads** for pre-trends. Plain TWFE on staggered timing is a known pitfall.
- **IV / dynamic-panel GMM** — justify the exclusion restriction in words, report **first-stage F** and weak-IV-robust CIs; for leverage dynamics, `xtabond2`-style GMM with instrument-count discipline.
- **RDD** — voting/index/threshold cutoffs; show a **density/manipulation test** and bandwidth robustness.
- **Event study (returns)** — a **clean, narrow window**, a confounding-news screen, and CAR/BHAR robustness.
- **Matching / entropy balancing** — report **covariate balance** and common support; treat as conditioning, not identification, unless paired with a shock.

## Hardening checklist

- [ ] The **source of exogenous variation** is named and defended in one paragraph
- [ ] The key threat (selection, reverse causality, confounding shock) is addressed head-on
- [ ] Pre-trends / first stage / density / balance shown as appropriate
- [ ] At least one **alternative design or placebo** corroborates the main estimate
- [ ] Standard errors **clustered** at the right level (firm and/or time)

## Anti-patterns

- "We control for everything" as a substitute for a design.
- TWFE event-study with no modern-estimator robustness on staggered adoption.
- An IV whose exclusion restriction is asserted, never argued.

## Output

```
【Design】<DID/IV/RDD/event/matching>  【Variation】<source>
【Top threat】<x> → handled by <y>
【Diagnostics】pre-trend/first-stage/density/balance: [Y/N each]
```

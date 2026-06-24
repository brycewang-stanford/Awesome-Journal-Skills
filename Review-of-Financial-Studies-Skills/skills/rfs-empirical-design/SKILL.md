---
name: rfs-empirical-design
description: Use when sample construction, estimator choice, factor/portfolio design, or measurement is the bottleneck for a The Review of Financial Studies (RFS) manuscript. Settles design choices that make the identification credible; does NOT pick the identification strategy or run robustness.
---

# Empirical & Structural Design (rfs-empirical-design)

## When to trigger

- The identification strategy is chosen but sample, variables, and estimator are unsettled
- You must decide between panel FE, Fama–MacBeth, GMM, or a structural estimator
- Portfolio sorts / factor construction choices feel arbitrary
- Measurement of the key variable is contestable (proxy validity)
- A referee will ask "why this sample / this window / this proxy?"

## Design decisions that make or break an RFS empirical paper

RFS publishes design-defining empirical templates referees will hold you to — e.g., the q-factor construction in Hou, Xue, and Zhang (2015) "Digesting Anomalies" (RFS 28(3)) and the variance-risk-premium measure in Bollerslev, Tauchen, and Zhou (2009) (RFS 22(11)). Two RFS-specific pressures sharpen every choice below: (1) the **public code-release condition** means every filter and construction step must be reproducible by a stranger, not just described; (2) the **Registered Reports** option means a design can be locked at Stage 1, so pre-specify wherever you can.

### 1. Sample construction
- State the universe, the time span, and **every** filter, with the resulting N at each step (a sample-attrition table).
- Justify the start/end dates by data availability or regime, not convenience.
- Handle survivorship, look-ahead, and backfill bias explicitly (CRSP/Compustat merge timing, delisting returns, point-in-time fundamentals).
- Winsorize vs. trim: state the rule (e.g., 1%/99%) and apply it consistently.

### 2. Variable measurement
- For each key variable, give: definition, data source, construction formula, and unit.
- Defend proxy validity — a proxy needs a first-principles or validation argument, not just precedent.
- Avoid mechanical correlation between LHS and RHS (e.g., overlapping accounting items).

### 3. Estimator choice
| Question type                          | Default estimator                                  |
|----------------------------------------|----------------------------------------------------|
| Treatment effect, panel                | Modern DID estimator + two-way FE as a benchmark   |
| Cross-sectional return premium         | Fama–MacBeth (with Shanken / GMM correction)       |
| Predictive regression                  | Panel/pooled with overlap-robust SEs; OOS tests    |
| Risk exposure / factor model           | Time-series spanning regressions, GRS test         |
| Structural parameter / counterfactual  | SMM / GMM / MLE with identification argument        |

### 4. Fixed effects and controls
- Saturate fixed effects to absorb the right confounders (firm, industry×year, etc.) — but show the result is not mechanical to the FE choice.
- Distinguish controls that are "bad controls" (post-treatment / outcomes) from legitimate covariates.

### 5. Standard errors
- Cluster at the level of treatment assignment or the unit of correlation.
- For asset pricing, match SE to the return structure (Newey–West for autocorrelation, Driscoll–Kraay for cross-sectional + serial dependence).

## Execution bridge (StatsPAI / Stata MCP)

Run the asset-pricing battery, don't just specify it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RFS is finance top-3 (with JF, JFE) — corporate-causal chain for corporate papers, factor-zoo haircut for asset pricing.

- **Factor regressions / time-series alphas:** `feols` with the right SEs (Newey–West /
  clustered) — read the alpha and t off the return.
- **Factor-zoo haircut:** after disclosing how many signals were screened, apply
  `romano_wolf` / `benjamini_hochberg` and report the alpha that survives.
- **Fama–MacBeth + Shanken EIV** are Stata-canonical — run via `mcp__stata-mcp__stata_do`
  with the vendored `resources/code/` (`asreg` / `xtfmb`).
- **Exhibits:** `etable`; hand formatting to the tables/figures skill.

Report the economic magnitude (bps/month alpha, Sharpe gain); full factor grid → appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Sample-attrition table present; every filter justified
- [ ] Survivorship / look-ahead / backfill addressed (point-in-time data)
- [ ] Each key variable has definition + source + formula; proxy validity argued
- [ ] Estimator matches the question; benchmark estimator also reported
- [ ] FE structure justified; no bad controls
- [ ] SE clustering / adjustment matches the data-generating structure
- [ ] Every filter/construction step is reproducible from the to-be-released code (RFS condition)
- [ ] Design choices are pre-committed where possible (Stage-1-ready), not chosen ex post

## Anti-patterns

- An unexplained sample period or unexplained filters that conveniently strengthen results.
- A proxy defended only by "following prior literature" when its validity is in doubt.
- TWFE reported as if it were a modern staggered-DID estimator.
- Controlling for post-treatment outcomes ("bad controls").
- Standard errors that ignore overlapping returns or treatment-level clustering.

## Output format

```
【Sample】universe / span / filters / final N
【Key measures】variable → source → formula → validity note
【Estimator】... (+ benchmark)
【FE & controls】...
【SE structure】...
【Next step】rfs-robustness
```

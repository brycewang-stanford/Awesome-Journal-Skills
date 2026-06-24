---
name: jeg-identification-strategy
description: Use when the inferential backbone of a Journal of Economic Growth (JEG) manuscript needs stress-testing — empirical papers via causal/econometric identification for growth, theory papers via assumptions, results, proof exposition, and generality. Forks by paper type, as a specialist growth and dynamic-macroeconomics outlet requires.
---

# Identification & Argument Strategy (jeg-identification-strategy)

## When to trigger

- An empirical growth claim rests on a cross-country regression with endogenous regressors
- A theoretical result depends on an assumption you have not justified or tested for tightness
- You are unsure whether your inferential backbone clears a growth-specialist bar

JEG publishes both theory and empirics, so this skill has **two tracks**. Pick the one matching your paper; quantitative/calibrated papers use both.

## Track E — Empirical identification (causal design for growth)

Growth empirics carry a hard endogeneity problem: most candidate determinants (institutions, human capital, finance, openness) are co-determined with income. The bar:

### Cross-country / dynamic-panel growth
- If you run growth-on-determinant regressions, confront **reverse causality and omitted deep determinants** explicitly. A bare OLS or static panel will not convince.
- Dynamic-panel **system GMM** (Arellano-Bond / Blundell-Bond) is common, but it is a trap if abused: **cap and report the instrument count**, report the **Hansen-J** over-identification test and **AR(2)** serial-correlation test, and show results are not driven by instrument proliferation.
- Convergence claims: distinguish β- from σ-convergence and address Galton's-fallacy / measurement-error critiques.

### Clean causal shock (where one exists)
- Where a credibly exogenous shock to a growth determinant exists, use a sharp design: **IV** (strong first stage, defended exclusion restriction in theory + institutions + falsification), **DID/event study** (modern estimators, not naive TWFE on staggered timing; pre-trends), or **RDD** (density and bandwidth diagnostics).
- Few-country / few-cluster inference: use wild-cluster bootstrap or randomization inference; do not lean on asymptotic t-stats with a handful of clusters.
- State the estimand (ATT / LATE / local effect) and its external validity for the growth question.

## Track T — Theoretical argument (assumptions, results, generality)

For a theory paper the "identification" object is the **logical structure**, not a research design.

- **Assumptions**: list them explicitly; mark which are substantive (drive the result) vs technical (for tractability). Justify each economically and flag knife-edge conditions.
- **Results**: state propositions/theorems precisely with their hypotheses; give existence, uniqueness, and stability of the relevant steady state or balanced-growth path, and check transversality.
- **Proof exposition**: put intuition in the text and full proofs in an appendix; make each step auditable. A growth-theory referee will reproduce the algebra.
- **Generality**: show how far the result reaches — which assumptions can be relaxed, what breaks if you do, and which comparative statics / testable predictions survive. Generality is the contribution's reach.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEG (growth) uses cross-country and long-run panels with deep endogeneity; foreground identification and robustness to alternatives.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- (E) System GMM with hundreds of instruments and no Hansen-J / AR(2) reported.
- (E) Naive TWFE on staggered growth-policy timing; OLS cross-country causal claims with no design.
- (T) A "general" theorem that silently depends on a knife-edge parameter restriction.
- (T) Proofs that assert rather than derive existence/uniqueness/stability.
- Either track claiming more than the argument supports.

## Persistence-design defenses (Track E extension)

Historical-persistence and deep-determinants papers face a now-standard referee script at this journal; pre-empt all four lines before submission:

- **Spatial autocorrelation**: report Conley standard errors at several distance cutoffs alongside clustered SEs, and show the headline estimate survives the widest defensible cutoff.
- **Spurious spatial fit**: run placebo treatments drawn from spatially correlated noise and report where the true coefficient falls in that placebo distribution.
- **Overused instruments**: if your instrument (terrain, climate, disease ecology, a historical shock) has already served other outcomes in print, defend exclusion against *each* published channel it explains — not in the abstract.
- **Mechanism opacity**: a reduced-form persistence coefficient is a starting fact, not an answer; bring intermediate-period outcomes or a decomposition that traces how the past reaches the present.

A persistence paper that clears only the first two is an economic-history note; clearing all four is what makes it a growth paper.

## Output format

```
【Track】E (empirical) / T (theory) / both
【E: design】GMM-panel / IV / DID / RDD + key diagnostics (Hansen-J, AR(2), first-stage F, pre-trends)
【E: inference】clustering / few-country handling; estimand + external validity
【T: assumptions】substantive vs technical; knife-edge flags
【T: results】existence / uniqueness / stability / transversality checked?
【T: generality】what can be relaxed; surviving predictions
【Next skill】jeg-data-analysis
```

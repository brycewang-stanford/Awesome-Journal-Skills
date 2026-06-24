---
name: jme-identification-strategy
description: Use when the identification of a monetary or macro shock (or a structural mechanism) is the bottleneck for a Journal of Monetary Economics (JME) manuscript — high-frequency surprises, narrative shocks, proxy/SVAR, local projections, sign restrictions, and model-based identification. Stress-tests the design before exhibits are drafted.
---

# Identification Strategy (jme-identification-strategy)

## When to trigger

- The "monetary shock" is a raw policy-rate change with no exogeneity argument
- A SVAR uses a recursive ordering that referees will dispute
- High-frequency surprises are not separated from the Fed "information effect"
- A DSGE mechanism is asserted but not identified from the data/moments
- You are unsure the design clears the JME bar for a credible macro claim

## The JME identification bar

JME is **monetary economics and macroeconomics**, so "identification" means isolating an exogenous **shock** or pinning down a **structural mechanism**, not a micro treatment effect. With **single anonymized review** and **at least two specialist referees**, the identifying assumption must be legible and defended in the registers macroeconomists expect. The credibility ladder the field implicitly applies (strong → weaker):

1. **High-frequency identification** — monetary surprises in a narrow window around FOMC announcements, with the **pure policy shock separated from the information/forward-guidance component** (Nakamura–Steinsson, Miranda-Agrippino–Ricco, Jarociński–Karadi-style decompositions).
2. **Narrative shocks** — Romer–Romer-style records of policy intent, orthogonalized to Greenbook/Tealbook forecasts; narrative fiscal shocks (military news, tax changes).
3. **Proxy / external-instrument SVAR** — the surprise series as an instrument for the policy rate inside a VAR; report relevance and the implied IRFs.
4. **Sign / long-run restrictions** — theory-consistent restrictions when timing or IV are unavailable; report robustness to the restriction set.
5. **Model-based (quantitative) identification** — discipline structural parameters with micro moments and matched second moments; report identification diagnostics (e.g., Iskrev) and prior sensitivity.

## Branch paths

### Branch A: High-frequency / narrative monetary shocks
- Define the event window precisely; show the surprise is news, not anticipated.
- **Strip the information effect**: a contractionary surprise that *raises* expected output signals the central bank's private information — decompose it.
- Aggregate to the desired frequency carefully; discuss attenuation and measurement error.

### Branch B: SVAR / proxy-SVAR
- State the identification scheme (recursive, sign, long-run, IV/proxy) and defend it.
- Report instrument relevance (for proxy-SVAR), IRF confidence bands, lag selection, and stability.
- Show robustness to ordering / restriction choices; report FEVDs.

### Branch C: Local projections (Jordà)
- Compare LP and VAR IRFs; LP is more robust to misspecification but noisier.
- Use lag-augmentation; LP-IV when using an external instrument; HAC/Newey–West or clustered SEs.

### Branch D: DSGE / quantitative mechanism
- Identify the new mechanism from data: which moments move when the friction is on vs. off?
- Report Bayesian estimation diagnostics (convergence, identification, posterior predictive) or calibration targets.
- Show the policy conclusion changes *because* of the mechanism, not an unrelated assumption.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JME is monetary macro — SVAR, local projections, high-frequency identification; `local_projections`/`irf` are in StatsPAI, DSGE/calibration is outside this toolchain.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The shock/mechanism named in one sentence and defended as exogenous/identified
- [ ] Monetary surprises separated from the information effect (if high-frequency)
- [ ] SVAR identification scheme stated and robustness shown
- [ ] LP-vs-VAR comparison reported where relevant
- [ ] DSGE identification diagnostics / calibration targets reported
- [ ] The claim never exceeds what the identification supports

## Output format

```
【Approach】high-frequency / narrative / proxy-SVAR / LP / sign-restriction / model-based
【Shock or mechanism】one sentence
【Exogeneity / identification argument】one line
【Information-effect handling】Y/N (if HF)
【Robustness done】[ordering, restriction set, LP-vs-VAR, identification diagnostics, ...]
【Next step】jme-data-analysis
```

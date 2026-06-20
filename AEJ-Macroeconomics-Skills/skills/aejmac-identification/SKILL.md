---
name: aejmac-identification
description: Use when the empirical identification of a macro shock or dynamic causal effect is the bottleneck for an American Economic Journal: Macroeconomics (AEJ: Macro) manuscript — SVAR, local projections, narrative, high-frequency/proxy-VAR, or micro-data macro designs. Stress-tests the identification to the AEJ: Macro broad-interest quantitative bar; for model-parameter identification see aejmac-theory-model.
---

# Empirical Identification (aejmac-identification)

## When to trigger

- The macro effect rests on a recursive (Cholesky) SVAR with no defense of the ordering
- A monetary/fiscal "shock" is plausibly anticipated or endogenous to the cycle
- Local projections are run but lag length, controls, and inference are ad hoc
- A narrative or high-frequency instrument is used but its exogeneity/relevance is unargued
- You are unsure the design clears AEJ: Macro's identified-empirical bar

## The AEJ: Macro identification bar

AEJ: Macro publishes identified-empirical macro, so the **mapping from data to the dynamic causal object** (an impulse response, a multiplier, a pass-through) must be explicit and defended. The aggregate, time-series setting makes identification harder than in micro: few effective observations, anticipation, simultaneity, and structural breaks. State the **shock you claim to identify**, the **assumption that delivers it**, and the **horizon and object** you report. Report **standard errors / confidence bands** (the AEA house style; significance asterisks are conventional in AEA tables but the band/SE must carry the inference, not the stars).

## Branch paths

### Branch A: Structural VAR (SVAR)
- **Recursive (Cholesky):** defend the ordering as an economic timing assumption, not a default; show robustness to plausible reorderings.
- **Sign restrictions:** state the full set; acknowledge set-identification (report the identified set / median-target with a credible band, not a point as if point-identified); address the "multiple models" critique.
- **Long-run / Blanchard–Quah:** justify the long-run neutrality assumption.
- **Proxy-VAR / external instruments (SVAR-IV):** show instrument relevance (reliability/F) and defend exogeneity; report weak-instrument-robust bands where relevance is marginal.

### Branch B: Local projections (LP)
- Report the **horizon-by-horizon** IRF with bands; state lag length and control set and show robustness to them.
- Use **Newey–West / HAC or LP-specific** inference; for panel LP cluster appropriately.
- Consider **LP-IV** when the shock needs instrumenting; report the first-stage strength.
- Address the LP-vs-VAR bias/variance trade-off explicitly if both are plausible.

### Branch C: Narrative & high-frequency identification
- **Narrative shocks** (Romer–Romer style monetary/fiscal/tax): document the construction, the source record, and why the series is exogenous to the cycle; show it is unpredictable from macro history.
- **High-frequency monetary surprises** (event-window around announcements): defend the window, address the "Fed information effect" (orthogonalize against forecasts or use the information-robust instruments), report relevance.

### Branch D: Micro-data macro / cross-sectional identification
- Cross-sectional or regional designs aggregated to a macro statement (e.g., regional multipliers): state the **general-equilibrium vs. partial-equilibrium** gap and how you map the cross-sectional elasticity to the aggregate.
- Use modern heterogeneity-robust estimators where staggered timing applies; cluster at the assignment level.

## Checklist

- [ ] Branch chosen; the shock and the data-to-IRF mapping stated in one sentence
- [ ] SVAR: ordering / sign set / long-run / proxy assumption defended, not defaulted
- [ ] LP: lag length, controls, HAC inference stated; robustness to them shown
- [ ] Narrative/HF: construction documented; exogeneity (unpredictability) demonstrated; relevance reported
- [ ] Cross-sectional-to-aggregate: PE-vs-GE gap addressed
- [ ] Inference: bands/SEs carry the conclusion; weak-instrument-robust where relevant
- [ ] The macro claim never exceeds the horizon/object the design identifies

## Anti-patterns

- A Cholesky ordering presented as if it were innocuous, with no economic timing argument
- Sign-restricted IRFs reported as point estimates, hiding set-identification
- A "monetary shock" that is predictable from the prior quarter's data (anticipation not addressed)
- High-frequency surprises used without confronting the Fed information effect
- LP reported at a single cherry-picked horizon instead of the full response with bands
- Mapping a regional/cross-sectional elasticity straight to an aggregate multiplier with no GE caveat

## Worked vignette: identifying a monetary shock (illustrative)

A paper estimates the output response to monetary policy via a recursive SVAR ordered output → prices → policy rate. A referee says the ordering is indefensible at high frequency. The AEJ: Macro fix: replace (or corroborate) the recursive shock with a **high-frequency surprise** from a tight window around FOMC announcements, **purged of the information effect** by orthogonalizing against Greenbook/SPF forecasts, then feed it as an external instrument in a proxy-VAR or as the shock in local projections. Suppose the peak output response stabilizes at -0.6% (90% band [-1.0, -0.2]) and is robust across the SVAR-IV and LP implementations — that cross-method agreement is the identification argument.

## Output format

```
【Branch】SVAR / LP / narrative-HF / cross-sectional-macro
【Shock + data-to-IRF mapping】one sentence
【Identifying assumption】ordering / sign set / exogeneity / GE mapping
【Inference】bands/SEs; weak-IV-robust if relevant; HAC/cluster choice
【Object + horizon reported】...
【What it does NOT identify】...
【Next step】aejmac-robustness (then aejmac-theory-model if a model is matched to this)
```

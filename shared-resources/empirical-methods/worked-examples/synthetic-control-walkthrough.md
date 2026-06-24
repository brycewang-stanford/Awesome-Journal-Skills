> **Illustrative teaching example — synthetic data, real tool runs.** The panel is
> **fictional** (a seeded factor-model panel: one treated region + 20 donors). But every
> number was produced by an **actual StatsPAI MCP call on 2026-06-24** — nothing is
> hand-typed. Venue-neutral synthetic-control companion to the DiD / IV / RDD
> walkthroughs; shows the [`execution-with-mcp`](../execution-with-mcp.md) bridge running
> an SCM end to end.

# Worked Example: Executing a Synthetic Control (StatsPAI walkthrough)

**Setup (fictional).** One treated region (`U01`) and 20 donor regions, 30 periods, an
intervention at **t = 20**. Outcomes follow a latent factor structure; the treatment adds
a known **+6** level shift to the treated unit after t = 20. A good donor weighting should
track `U01` tightly *before* t = 20, then separate from it after.

> The point is not the coefficient (data are synthetic) — it is that the workflow *builds
> a transparent weighted counterfactual, verifies the pre-period fit, and runs placebo
> inference*, each with one tool call.

---

## Step 1 — Fit the synthetic control with placebo inference

`synth(outcome="y", time="time", unit="unit", treated_unit="U01", treatment_time=20,
inference="placebo")`:

| Estimand | ATT | SE | 95% CI | placebo p |
|---|---|---|---|---|
| Synthetic Control (classic) | **6.59** | 1.48 | [3.69, 9.48] | **0.048** |

True effect +6 → recovered **6.59**, CI comfortably covering 6. The in-space placebo
p = 0.048 means the treated unit's post/pre fit ratio is more extreme than all but one of
the 20 donor placebos — significant at 5%.

## Step 2 — Trust it only if the pre-period fit is good

The same call reports the diagnostics that decide whether the counterfactual is credible:

| Diagnostic | Value | Reading |
|---|---|---|
| Pre-treatment RMSE | **0.44** | the synthetic unit tracks `U01` tightly before t = 20 |
| Post/pre fit ratio | ~15 | the post-period gap dwarfs pre-period noise |
| Active donors | **7** (of 20) | a sparse, interpretable weighting |
| Effective donors | ~5.9 | not propped up by a single donor |

A small pre-RMSE relative to a +6 effect is what licenses reading the post-period gap as
the treatment effect; a large pre-RMSE would mean the donor pool cannot reproduce the
treated unit and the design is off.

## Step 3 — Report the weights (transparency referees expect)

The synthetic `U01` is a transparent convex combination — the top donors:

| Donor | Weight |
|---|---|
| U09 | 0.27 |
| U20 | 0.16 |
| U05 | 0.15 |
| U15 | 0.14 |
| U10 | 0.11 |

(plus two smaller weights). Reporting the donor weights lets a referee see exactly which
units form the counterfactual — a standard SCM transparency requirement.

---

## What goes where in the manuscript

- **Body:** the path plot (treated vs. synthetic), the gap plot, the ATT with its placebo
  p-value, the pre-treatment RMSE, and the donor-weight table. One sentence on the
  intervention and the donor pool.
- **Appendix:** the full donor-weight vector, leave-one-donor-out robustness, a
  backdating / time-placebo test, and (where adoption is staggered or there are several
  treated units) the synthetic-DiD (`sdid`) estimate as a cross-check.
- **SUTVA** — no spillover from the treated unit to donors — is the identifying
  assumption; argue it, don't just assert it.

## Reproduce this

1. Generate the panel (seeded): 21 units × 30 periods, factor structure, treated `U01`
   gets +6 from t = 20.
2. Run: `synth(... treated_unit="U01", treatment_time=20, inference="placebo")`; read the
   ATT, placebo p, pre-RMSE, and donor weights off the return. Cross-check with `sdid`
   (synthetic DiD) and `synth_time_placebo` (backdating) where the panel allows. Full map:
   [`execution-with-mcp`](../execution-with-mcp.md).
3. If StatsPAI is not connected, the same chain exists in the empirical-methods `code/`
   skeleton; say which number is unverified rather than reporting one you did not compute.

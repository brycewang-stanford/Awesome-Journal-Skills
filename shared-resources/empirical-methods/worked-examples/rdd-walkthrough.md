> **Illustrative teaching example — synthetic data, real tool runs.** The dataset is
> **fictional** (a seeded sharp scholarship cutoff: a benefit is awarded when a centered
> running score crosses 0). But every number below was produced by an **actual StatsPAI
> MCP call on that synthetic data on 2026-06-24** — nothing is hand-typed. This is the
> venue-neutral RDD companion to the JF DiD walkthrough; it shows the
> [`execution-with-mcp`](../execution-with-mcp.md) bridge running a regression-discontinuity
> design end to end.

# Worked Example: Executing a Sharp RDD (StatsPAI walkthrough)

**Setup (fictional).** Treatment `D` switches on at running variable `X ≥ 0`; outcome `Y`
trends in `X` and jumps at the cutoff. The DGP's true local jump is **τ = 0.6**, the
running-variable density is smooth (no manipulation), and the slope in `X` is steep
enough that a *naive* treated-minus-control mean difference is badly biased.

> The point is not the coefficient (data are synthetic) — it is that the workflow
> *separates the local jump from the slope, and runs the manipulation test that makes the
> design credible*, each with one tool call.

---

## Step 0 — The naive comparison (run it, to show the trap)

The simple mean difference of `Y` above vs. below the cutoff (all units) is **1.39** — more
than **2×** the true 0.6. It conflates the discontinuity with the slope of `Y` in `X`:
units just above the cutoff have higher `X`, hence higher `Y`, regardless of treatment.

## Step 1 — Fit the local RD with bias-corrected robust CIs

`rdrobust(x="X", y="Y", c=0)` (triangular kernel, MSE-optimal bandwidth):

| Method | Estimate | SE | 95% CI |
|---|---|---|---|
| Conventional | **0.5955** | 0.0323 | [0.532, 0.659] |
| Robust (CCT bias-corrected) | **0.5700** | 0.0468 | [0.478, 0.662] |

MSE-optimal bandwidth h = 0.130; effective N = 531 (left) + 525 (right). Both CIs contain
the true 0.6, and the estimate (~0.57–0.60) is a world away from the naive 1.39 — the
local design recovers the jump the naive difference buried under the slope.

## Step 2 — Manipulation tests (does anyone sort across the cutoff?)

| Test | Stat | p | Reading |
|---|---|---|---|
| McCrary (2008) density | log-ratio −0.005 | **0.965** | no density jump → no manipulation |
| Cattaneo–Jansson–Ma (2020) | t = −0.98 | **0.327** | confirms: density continuous at c |

Both fail to reject a continuous density at the cutoff — the running variable is not being
gamed, so the local-randomization logic holds. (Had either rejected, the move is a
donut-hole RD or partial-identification bounds.)

## Step 3 — Robustness to the kernel (a tuning choice referees probe)

Re-fit with a uniform kernel, `rdrobust(..., kernel="uniform")`:

| Kernel | Conventional | Robust | 95% CI (robust) |
|---|---|---|---|
| Triangular | 0.5955 | 0.5700 | [0.478, 0.662] |
| Uniform | 0.6088 | 0.5689 | [0.451, 0.687] |

The estimate barely moves (0.57–0.61) across the weighting choice — the discontinuity is
not an artifact of one bandwidth/kernel. (For a fuller sweep, `rd_honest`
(Armstrong–Kolesár) gives coverage-honest CIs over a curvature bound; report it alongside
when the functional form is contestable.)

---

## What goes where in the manuscript

- **Body:** the RD plot (binned scatter + local fit), the `rdrobust` estimate with its
  **robust** CI, the McCrary/CJM density-test result, and the magnitude in interpretable
  units. State the cutoff and the assignment rule in one sentence.
- **Appendix:** bandwidth sensitivity (`rdbwsensitivity`), placebo cutoffs
  (`rdplacebo`), covariate balance at the cutoff (`rdbalance`), the donut variant, and
  the kernel/polynomial-order grid.
- **Continuity** of potential outcomes at the cutoff is the identifying assumption — the
  density test supports it but does not prove it; argue no other policy changes at the
  same threshold.

## Reproduce this

1. Generate the panel (seeded): `X ~ Uniform(−1, 1)`; `D = 1[X ≥ 0]`;
   `Y = 0.5 + 0.8·X + 0.6·D + ε`, `ε ~ N(0, 0.2)`, N = 8000.
2. Run: `rdrobust("Y","X", c=0)` → `mccrary_test` + `rddensity` → re-fit with
   `kernel="uniform"` (and `rd_honest` / `rdbwsensitivity` for sensitivity). Full map:
   [`execution-with-mcp`](../execution-with-mcp.md).
3. If StatsPAI is not connected, the same chain exists in the empirical-methods
   `code/` skeleton (`05_rdd.do`: `rdrobust` + `rddensity`); say which number is
   unverified rather than reporting one you did not compute.

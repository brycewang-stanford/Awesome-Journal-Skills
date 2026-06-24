---
name: ecta-robustness
description: Use when an Econometrica manuscript needs finite-sample evidence and edge-case scrutiny — Monte Carlo design, finite-sample performance, regularity-condition stress tests, and degenerate cases. Designs and audits the simulation evidence; it does not derive the asymptotics (use ecta-identification) or format the resulting tables (use ecta-tables-figures).
---

# Monte Carlo and Finite-Sample Evidence (ecta-robustness)

## When to trigger

- The paper reports asymptotic theory but contains **no finite-sample (Monte Carlo) check**
- Coverage / size / power of a proposed test or interval is claimed but never simulated
- You have not probed where the regularity conditions bind or where the method breaks
- A theory result needs numerical illustration of comparative statics or equilibrium behavior

For methods papers, asymptotics without finite-sample evidence is a standard rejection
reason. The Monte Carlo is not decoration — it is how the reader learns whether the
asymptotic approximation is usable at realistic sample sizes.

**Econometrica-specific:** simulation results fall *inside* the Econometric Society Data and
Code Availability Policy (which covers "empirical, experimental, **and/or simulation**
results"). The ES **Data Editor** will run a pre-acceptance reproducibility check on your
Monte Carlo, so every table must regenerate bit-for-bit from seeded code (see
`ecta-replication-package`). This is a sharper bar than at applied siblings where simulation
appendices are rarely re-run. A pure-theory paper with no simulations is *exempt* from that
policy, but numerical illustration is still expected where it sharpens a result.

## Designing the Monte Carlo

1. **Designs that mirror the theory.** Include DGPs where assumptions hold (to show the
   method works) *and* designs that approach the boundary of each assumption (to show how it
   degrades). One favorable design proves nothing.
2. **Sample sizes that show convergence.** Use several n (e.g., small, moderate, large) so the
   reader sees the asymptotics kicking in; report how fast.
3. **Competitors.** Compare against the natural existing method(s). A new estimator must beat
   or at least match what it replaces on bias, RMSE, size, or power.
4. **Replications and Monte Carlo error.** Use enough replications that reported size/coverage
   has small simulation error; report the number of replications and, where relevant, the
   Monte Carlo standard error so a 0.06 is distinguishable from 0.05.
5. **Seeds.** Fix and record seeds; the tables must be reproducible bit-for-bit (see
   `ecta-replication-package`).

## What to report

| Quantity | Why |
|----------|-----|
| Bias and RMSE / MSE | Point-estimation quality vs. competitors |
| Empirical size at nominal 5% / 10% | Whether the test controls size in finite samples |
| Size-adjusted power / power curves | Whether the test detects departures, fairly compared |
| Coverage and average length of CIs | Whether intervals are valid and informative |
| Sensitivity to tuning (bandwidth, # of moments, penalty) | Whether results hinge on a knob |
| Behavior under weak / near-boundary identification | Whether pointwise asymptotics mislead |

## Regularity and edge-case stress tests

- **Assumption boundaries.** For each key assumption, build a design that violates it slightly
  and show the consequence. This both demonstrates necessity and warns practitioners.
- **Degenerate cases.** Ties, empty cells, near-singular design matrices, heavy tails, serial
  dependence, heteroskedasticity — whichever your conditions rule out, probe the boundary.
- **Tuning robustness.** Vary every tuning parameter; if results are knife-edge in a knob,
  say so and give a data-driven choice.
- **Misspecification.** If the method is supposed to be robust to some misspecification, simulate
  it; if it is not, be explicit about that limitation.

## For theory papers

A theory paper still benefits from numerical illustration: plot the equilibrium / value
function / comparative-static across the parameter range, show the representation on a worked
example, or compute the solution where closed forms are unavailable. Make clear this is
illustration, not evidence of generality (the proof carries generality).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Econometrica publishes econometric theory and applied micro; the chain below serves its applied/empirical papers (weak-IV-robust and modern-DiD reporting expected) — pure theory uses its own apparatus.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] At least one favorable design and one boundary / adverse design
- [ ] Multiple sample sizes showing the asymptotics engage
- [ ] Comparison against the natural competitor method(s)
- [ ] Number of replications stated; Monte Carlo error small / reported
- [ ] Size, power (size-adjusted), coverage, and length reported as relevant
- [ ] Tuning-parameter sensitivity examined
- [ ] Weak / near-boundary identification behavior shown if the theory has that regime
- [ ] Seeds fixed and recorded; tables reproducible

## Anti-patterns

- Asymptotics with no finite-sample evidence at all
- A single, conveniently favorable DGP presented as comprehensive
- Reporting power without size control (or without size adjustment) so the comparison is unfair
- Too few replications, so a reported 0.05 size is within noise of 0.08
- Cherry-picking the tuning parameter that makes the method look best
- Comparing only to a strawman, not to the genuinely competitive existing method
- Claiming robustness to misspecification that is never simulated

## Output format

```
【Designs】favorable: ...; boundary/adverse: ...
【Sample sizes】[...]   【Replications】...   【MC error reported】yes/no
【Competitors】[...]
【Metrics】bias/RMSE, size, power, coverage, length — [which reported]
【Tuning sensitivity】...
【Weak/boundary regime】examined / n.a.
【Gaps】[...]
【Next step】ecta-tables-figures
```

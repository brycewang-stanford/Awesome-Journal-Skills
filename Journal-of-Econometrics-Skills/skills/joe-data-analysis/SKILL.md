---
name: joe-data-analysis
description: Use when designing the Monte Carlo study and empirical illustration that demonstrate a Journal of Econometrics (JoE) method works in finite samples. Covers size/power simulation design, DGP stress tests, and the role of the applied illustration relative to the theory.
---

# Monte Carlo & Empirical Illustration (joe-data-analysis)

## When to trigger

- The theorems are settled but the finite-sample evidence is thin or one-off
- A simulation reports point estimates but no size/power, or never stresses the assumptions
- You are unsure how large or how diverse the Monte Carlo design must be
- You have an empirical illustration but it is doing the wrong job (over- or under-claiming)

## What "data analysis" means at a methodology journal

At the *Journal of Econometrics* the empirical work serves the **method**, not the other way around. A theorem describes behavior as $n\to\infty$; the **Monte Carlo** shows the asymptotics bite at realistic sample sizes, and the **empirical illustration** shows the method is usable and yields a sensible answer on real economic data. The applied illustration is a demonstration, **not** the paper's primary contribution — purely applied work without a methodological advance is out of scope here. Build both as evidence that the formal claims hold.

## Monte Carlo design

### Report the right quantities
- **Estimators:** bias, RMSE, coverage of confidence intervals.
- **Tests:** empirical **size at nominal 5%/10%**, then **size-adjusted power** curves. Over-rejection that vanishes only at huge $n$ is a finding, not a footnote.
- Compare against the **nearest existing method** on identical DGPs (ties back to `joe-literature-positioning`).

### Stress the assumptions, do not flatter them
- Vary **sample size** (including small $n$ where asymptotics may fail).
- Vary the **DGP**: error distributions (heavy tails, heteroskedasticity), dependence (serial/cluster/spatial), degree of endogeneity or identification strength, dimension.
- Vary **tuning parameters** (bandwidth, lag length, penalty, number of moments) and show sensitivity.
- Include designs **near the boundary** of your conditions — that is where referees look.

### Computational hygiene
- Fix and **report seeds**; report **replication count** and Monte Carlo standard errors so differences are not noise.
- Parallelize heavy designs; record runtime/hardware for the replication archive.

## Finite-sample stress grid

Build the Monte Carlo grid around the theorem's weak points, not around flattering defaults:

| Dimension | Minimum stress case |
|-----------|---------------------|
| Sample size | A small or moderate $n$ where the asymptotic approximation is plausibly strained. |
| Identification strength | Weak instruments, near-collinearity, boundary parameters, local-to-zero effects, or sparse support as relevant. |
| Error process | Heavy tails, heteroskedasticity, serial/cross-sectional dependence, or clustering that matches the target application. |
| Tuning | Bandwidth, penalty, lag, moments, sieve dimension, or bootstrap choice varied enough to show stability. |
| Competitor | The closest existing estimator/test run on exactly the same DGP and reporting scale. |

Pre-register the cells in the simulation plan, then mark any post-hoc additions as diagnostics. JoE
referees punish Monte Carlos that prove only that the authors found a friendly DGP.

## Empirical illustration

- Pick a dataset where the method's advantage is **visible** (the problem it solves actually occurs).
- Show the **method changes a conclusion** or sharpens inference relative to standard practice — that is the payoff.
- Keep claims proportionate: this is an illustration of the tool, not a causal study. Do not oversell the applied finding.
- Cite the data with the Elsevier **`[dataset]`** tag and prepare materials for the archive (see `joe-replication-and-data-policy`).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Journal of Econometrics is a methods venue — estimator validity + simulation evidence are the contribution; pair estimates with diagnostics and Monte-Carlo where relevant.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A single DGP at one sample size "confirming" the theory
- Reporting raw power without empirical size (size-distorted power is meaningless)
- Hiding tuning-parameter sensitivity or boundary cases
- An empirical section that drifts into an applied paper the method only decorates
- Unreported seeds / replication counts, so results are not reproducible

## Output format

```
【MC estimators】bias / RMSE / coverage reported? [Y/N]
【MC tests】size at 5%/10% + size-adjusted power? [Y/N]
【DGP stress】distributions / dependence / tuning / boundary? [list]
【Benchmark】compared to nearest method on same DGP? [Y/N]
【Reproducibility】seeds + reps + MCSE reported? [Y/N]
【Illustration】method changes/sharpens a real conclusion? [Y/N]
【Next step】joe-tables-figures
```

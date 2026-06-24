---
name: jbes-data-analysis
description: Use when building the Monte Carlo evidence and the substantive empirical application for a Journal of Business & Economic Statistics (JBES) methods paper. Designs and audits the simulation study and the real-data analysis; it does not derive the asymptotic theory (see jbes-identification-strategy).
---

# Monte Carlo & Empirical Application (jbes-data-analysis)

## When to trigger

- The asymptotic theory exists but the simulation study is thin or one-sided
- The empirical application is a toy illustration rather than a substantive use
- Reviewers will ask "does the method actually work in finite samples / on real data?"
- You need to choose DGPs, baselines, and an application that show the method's value

## Why this matters at JBES

JBES is a methods-with-empirics journal: a contribution is incomplete without **finite-sample evidence** and a **substantive empirical application** in microeconomics, macroeconomics, business, or finance. The simulation study is how you demonstrate the asymptotics bite at realistic sample sizes; the application is how you demonstrate **clear empirical relevance**. Both are evaluated by method experts who will reproduce or interrogate them.

## Monte Carlo design

- **DGPs that span the conditions**: include cases that satisfy your assumptions and cases that stress or violate them (dependence, heavy tails, weak identification, high dimension) so the breakdown frontier is visible.
- **Sample-size grid**: show size/power/coverage/bias/RMSE converging as n grows.
- **Honest baselines**: compare against the relevant incumbent method(s) under identical DGPs.
- **Reported MC uncertainty**: give Monte Carlo standard errors of rejection rates; fix and report seeds; document the number of replications and runtime.

## The empirical application

- Use a real, recognizable data set (e.g., FRED-MD macro series, CRSP/Compustat finance, IPUMS micro) that the method's novelty genuinely helps.
- Show the new method changes a substantive conclusion or enables an analysis prior methods could not.
- Report inference appropriate to the data (HAC/cluster/dependence-robust); include diagnostics.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JBES is a business / economic-statistics venue — reviewers weigh estimator validity and simulation evidence, so pair every estimate with its diagnostics and, where relevant, a Monte-Carlo check.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER, accounts for
  cross-test correlation) or `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr` — the confounder strength that would
  overturn the headline.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each — no guessing the battery.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive (now actually-run) battery in
the appendix. See the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] DGPs include both favorable and assumption-stressing regimes
- [ ] Sample-size grid displays the asymptotics taking hold
- [ ] Incumbent baselines simulated under identical DGPs
- [ ] Monte Carlo standard errors, seeds, and replication counts reported
- [ ] A substantive real-data application, not a toy illustration
- [ ] The application uses the method's novelty and changes/enables a conclusion
- [ ] All numbers regenerate from code (see jbes-replication-and-data-policy)

## Anti-patterns

- Simulating only DGPs that flatter the method; hiding breakdown
- Reporting rejection rates with no Monte Carlo standard errors
- A toy application with no substantive empirical payoff (off-scope at JBES)
- Omitting the incumbent baseline, so "improvement" is unquantified
- Cherry-picked sample sizes that mask poor small-n behavior


## Referee-pushback patterns on the evidence (venue-specific fixes)

| JBES referee objection | Fix this skill enforces |
|----|----|
| "Simulation DGPs are unrepresentative." | Calibrate DGPs to the application's moments — persistence, fat tails, cross-sectional dependence — not iid Gaussian |
| "No comparison to standard alternatives." | Add the incumbent estimator(s) under identical DGPs in the same tables |
| "The application is a toy." | Use a substantive macro/finance/micro case where the novelty changes a conclusion |

## Worked vignette: validating a new long-horizon forecast test

A hypothetical JBES paper proposes a HAC-robust test of equal long-horizon predictability, validated on FRED-MD inflation forecasts (numbers **illustrative**). The Monte Carlo calibrates the DGP to FRED-MD persistence (AR root near 0.97) and overlapping-horizon dependence, not iid noise; at n=240 the test holds an illustrative size of 5.4% versus nominal 5%, while the Diebold-Mariano benchmark over-rejects at 9.1% under the same DGP. The application then reverses a borderline DM verdict on whether a factor-augmented model beats the random walk at 12 months — a substantive payoff, not a toy. Calibration anchor (hedged): JBES weights careful simulation and a real application roughly equally; a paper strong on only one axis is exposed.

## Evidence pass for Journal of Business & Economic Statistics

Run this as a concrete capability pass. First lock the statistical estimand, identification/simulation evidence, empirical illustration, and reproducibility path; then test whether the manuscript addresses econometrics/statistics reviewers who expect methodological credibility plus a business or economic use case.

- **Primary move:** Audit unit, comparison, uncertainty, missingness, sensitivity, and reproducibility before making any prose or submission recommendation.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Journal of Econometrics for theory-heavy methods, Econometric Theory for proof-first work, Quantitative Economics for economics-theory methods; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【DGPs】favorable + stress regimes covered? [Y/N]
【n grid】asymptotics visible as n grows? [Y/N]
【Baselines】incumbent(s) under identical DGPs? [Y/N]
【MC uncertainty】MC SEs + seeds + reps reported? [Y/N]
【Application】substantive, uses the novelty? [Y/N]
【Next step】jbes-tables-figures
```

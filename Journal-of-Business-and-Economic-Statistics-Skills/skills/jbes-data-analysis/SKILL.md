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

## Output format

```
【DGPs】favorable + stress regimes covered? [Y/N]
【n grid】asymptotics visible as n grows? [Y/N]
【Baselines】incumbent(s) under identical DGPs? [Y/N]
【MC uncertainty】MC SEs + seeds + reps reported? [Y/N]
【Application】substantive, uses the novelty? [Y/N]
【Next step】jbes-tables-figures
```

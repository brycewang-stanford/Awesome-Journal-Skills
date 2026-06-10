---
name: geb-data-analysis
description: Use when a Games and Economic Behavior (GEB) manuscript involves experimental data or numerical illustration — analyzing strategic-game experiments and building verified worked examples. Adapts analysis to GEB's game-theory nature, where data supports the theory rather than carrying a causal claim.
---

# Data & Numerical Analysis (geb-data-analysis)

## When to trigger

- You ran a lab/online game experiment and need to analyze choices and play paths
- You want numerical examples or simulations to illustrate a theorem
- A referee may question your experimental inference or example construction
- You are fitting a behavioral model (QRE, level-k, social preferences) to choices

## How analysis works at GEB

GEB is primarily a **theory** journal that *also* publishes experimental and computational work advancing game theory. So data analysis here is usually in service of a strategic claim — does observed play match an equilibrium prediction, distinguish solution concepts, or illustrate a mechanism — rather than estimating a treatment effect for its own sake. Keep it lighter and tightly tied to the model.

### A. Experimental game data

- **Unit of observation = the session.** Subjects within a session interact and are not independent; cluster standard errors at the **independent-session** level, or use session-level summaries for nonparametric tests.
- **Describe play, then test.** Report distributions of actions, convergence over rounds, and deviations from the predicted equilibrium before running tests.
- **Match tests to the design.** Wilcoxon/Mann–Whitney or permutation tests across sessions for treatment comparisons; mixed/random-effects models for repeated play.
- **Behavioral structural fits.** Quantal response equilibrium, level-k / cognitive hierarchy, or social-preference models — report fit and identification, and compare to the equilibrium benchmark.
- **Power and pre-registration.** Justify cells' sample sizes; reference any pre-analysis plan and report deviations. Under-powered interactive experiments are a standard referee objection.

### B. Numerical examples & simulation (for theory papers)

- **Examples illustrate, never substitute for, proofs.** Use a solver (e.g., Gambit, `nashpy`) to exhibit the equilibria your theorem describes and to make an abstract construction concrete.
- **Boundary / counterexamples.** A clean numerical counterexample showing an assumption is necessary is high-value.
- **Reproducible computation.** Set and report seeds; pin solver and library versions; ship a script that regenerates every example and figure (see geb-replication-and-data-policy — sharing is encouraged but not required at GEB).

## Anti-patterns

- Treating individual subjects as independent observations (ignoring session clustering)
- Presenting a few simulations as evidence a theorem is "probably true"
- Running treatment comparisons with no power justification
- A behavioral structural fit with no comparison to the equilibrium prediction
- Over-interpreting an experiment as a general causal claim — GEB rewards the strategic insight


## Evidence pass for Games and Economic Behavior

Treat this skill as an executable review pass, not a prose hint. First lock the primitives, equilibrium concept, comparative statics, and proof or experiment boundary; then judge whether the current manuscript answers the venue's real reader: game theorists who ask what the model teaches beyond a clever example.

- **Do the pass:** Audit the research design before polishing prose: unit of analysis, comparison set, uncertainty, sensitivity, missingness, and reproducibility must be visible.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against JET for theory abstraction, Theoretical Economics for compact theory contribution, Experimental Economics for experiment-first designs; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Mode】experimental data / numerical examples / both
【(Exp) clustering】session-level? [Y/N] — tests used
【(Exp) power & pre-reg】justified / referenced? [Y/N]
【(Exp) structural fit】model + comparison to equilibrium? [Y/N / NA]
【(Num) role】illustrates which result; counterexample? 
【Reproducibility】seeds + pinned versions + run_all? [Y/N]
【Next step】geb-tables-figures
```

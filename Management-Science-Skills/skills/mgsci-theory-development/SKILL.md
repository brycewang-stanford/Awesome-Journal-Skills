---
name: mgsci-theory-development
description: Use when building the theoretical core of a Management Science (INFORMS) paper — either a formal analytical model (assumptions, equilibrium, propositions/theorems, comparative statics) or empirically testable hypotheses derived from a clear mechanism. Adapts to the paper's lane; it does not run the analysis (mgsci-data-analysis) or frame the contribution (mgsci-contribution-framing).
---

# Theory Development (mgsci-theory-development)

## When to trigger

- You have an intuition but no model or no mechanism
- Hypotheses are descriptive ("X relates to Y") with no stated mechanism
- An analytical model has results but unclear/unstated assumptions
- A Department Editor or reviewer asked "what is the theory here?" or "why is this the right model?"

Because Management Science is **bimethodological**, "theory development" means one of two disciplined things depending on your Department lane.

## Lane A — Analytical / formal model

For Optimization and Decision Analytics, Stochastic Models and Simulation, Operations Management, Finance (theory), Business Strategy (theory), and economic-theory submissions:

- **State assumptions explicitly and defend them.** Each assumption should be necessary, behaviorally or economically reasonable, and you should know which results break without it.
- **Define the decision problem.** Players/decision-maker, actions, timing, information, objective. Make the optimization/equilibrium concept precise.
- **Derive results as propositions/theorems** with proofs (in text or appendix). Reviewers check that proofs are correct and that results are not artifacts of a knife-edge assumption.
- **Comparative statics and intuition.** The managerial payoff lives here: *how* the optimal policy / equilibrium moves with primitives, and *why* — stated in plain words, not only symbols.
- **Robustness of the model.** Show which extensions (heterogeneity, alternative timing, relaxed assumption) preserve the qualitative insight.

## Lane B — Empirical hypotheses from a mechanism

For Accounting, Finance (empirical), Information Systems, Behavioral Economics and Decision Analysis, Marketing, Data Science:

- **Name the mechanism** (incentive, information, frictional, behavioral) that produces the predicted effect; the hypothesis is the mechanism's observable implication.
- **Derive predictions a priori**, before looking at outcomes — HARKing (hypothesizing after results) is a credibility failure.
- **Moderation = boundary condition of the mechanism**; **mediation = the mechanism's intermediate step.** Predict the sign and the conditions, not just "an effect exists."
- Where a behavioral prediction comes from a model or from decision theory, state the formal source.

## The unifying bar

Whichever lane, the theory must yield a **decision-relevant, cross-department insight** — Management Science rewards a mechanism whose managerial implication a reader in another Department still finds informative. Formal elegance without managerial reading, or hypotheses without a mechanism, will not clear the bar.

## Anti-patterns

- A model whose results depend on an undefended knife-edge assumption.
- Propositions with no comparative statics and no plain-language intuition.
- Empirical hypotheses with no named mechanism (pure correlation dressed as theory).
- Post hoc hypotheses fitted to the data (HARKing).


## Theory pass for Management Science

Run this as a concrete capability pass. First lock the decision problem, formal or empirical engine, managerial lever, and generality claim; then test whether the manuscript addresses OR/MS reviewers who expect a generalizable decision model, credible empirical leverage, or algorithmic insight with managerial consequence.

- **Primary move:** Separate construct, mechanism, scope condition, and testable implication; refuse a theory section that only summarizes prior work.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Operations Research for method-first optimization, Marketing Science for marketing models, Organization Science for organization-theory mechanisms; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Worked micro-example (illustrative) and theory pushback

A platform model assumes buyers single-home and derives that the platform always raises commissions as network effects grow. In the flagship's Operations Management / Business Strategy lane, a referee asks whether the result is mechanical — driven entirely by the single-homing assumption. The fix names the mechanism (network effects raise the platform's marginal value of a seller), relaxes single-homing as a scope condition, and shows the comparative static can reverse when multi-homing is cheap (commissions fall from 15% to about 9%, illustrative). The proposition now carries a managerial reading a finance reader also grasps — take rates are not monotone in network strength — the cross-department insight the flagship rewards.

- **"The model insight is mechanical."** Show the result survives relaxing the assumption that drives it, or state precisely the scope condition under which it holds and reverses.
- **"What is the theory here?"** Name the mechanism explicitly; a proposition or hypothesis without a mechanism reads as algebra or correlation, not theory.
- **"Elegant but no managerial reading."** Add the comparative-static or boundary-condition intuition that tells a decision-maker in another department what changes.

## Output format

```
【Lane】analytical model / empirical-mechanism
【Core mechanism】...
【Assumptions or constructs】necessary? defended?
【Results】propositions/theorems OR a priori hypotheses (sign + conditions)
【Comparative statics / boundary】managerial intuition ...
【Next step】mgsci-methods
```

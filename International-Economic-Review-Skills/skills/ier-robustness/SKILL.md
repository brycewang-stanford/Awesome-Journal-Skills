---
name: ier-robustness
description: Use when an International Economic Review (IER) result may be sensitive to specification, sample, functional form, calibration, or inference choices. Organizes robustness by threat to the load-bearing assumption; it does not run the regressions.
---

# Robustness Strategy (ier-robustness)

## When to trigger

- The headline number is suspected to hinge on a functional-form choice (CES/log/quadratic) or a single calibrated parameter
- A referee asks "is this robust?" and the draft answers with a mechanical appendix of re-runs
- Inference looks fragile — few clusters, serial correlation, or numerically unstable standard errors
- For a structural paper, the counterfactual moves a lot when you re-anchor an externally-set parameter
- You need to know which robustness checks an IER referee will actually demand vs. which are noise

## The IER robustness principle: organize by threat, not by list

IER referees reward robustness that is **tied to the load-bearing assumption** identified in `ier-theory-model`/`ier-identification`. A list of twenty re-runs reads as defensive; three checks that each retire a specific threat to the result read as confident. Build the robustness section as a threat map:

| Threat to the result | The check that retires it | What "passing" looks like |
|----------------------|---------------------------|----------------------------|
| Functional form drives it | Re-do under an alternative class (e.g., non-CES preferences, semiparametric) | Sign/magnitude survives; if it moves, you bound the movement |
| One calibrated/external parameter drives it | Vary it over a defensible range; report the headline as a function of it | The qualitative result holds across the range, or you state the threshold |
| Sample/period drives it | Drop influential subsamples, split the period, exclude outlier units | Estimate stable; no single unit/period is pivotal |
| Specification search | Show the result across a transparent grid of reasonable specifications | The result is not a lucky cell (a specification curve, not cherry-picking) |
| Inference is too generous | Cluster-robust / wild-cluster bootstrap / HAC as the design demands | CIs widen honestly and the conclusion still holds |
| Numerical fragility (structural) | Re-solve on a finer grid, alternative solver, tighter tolerance | Counterfactual stable to solution method |

### The sequence

1. List the result's threats *in priority order* — the first one or two are the ones tied to the load-bearing assumption. Those go in the main text; the rest go to the appendix.
2. For each main-text threat, run the single most decisive check, not three weak ones.
3. Report robustness as a *range or function* where a parameter is uncertain ("welfare gain is 3.8–5.1% across the defensible elasticity range") rather than a single point with a footnote.
4. When a check moves the result, say so honestly and **bound** the movement — IER referees trust authors who report fragility and contain it more than authors who hide it.
5. Keep significance reporting clean (standard errors / confidence sets), not asterisk-driven.

### Robustness for theory and structural papers (not just applied)

At a theory-leaning journal, "robustness" is broader than re-running regressions. For a **theory** paper it means showing the result survives perturbing the load-bearing assumption (the perturbation test from `ier-theory-model`) — that *is* the robustness section. For a **structural** paper it means three distinct things: (a) economic robustness — does the counterfactual survive an alternative preference/technology specification; (b) parameter robustness — does it survive varying the externally-set parameters over a defensible range; and (c) numerical robustness — does it survive re-solving on a finer grid with a different solver. An IER referee distinguishes these and will not accept (b) as a substitute for (c) or (a). Map each explicitly.

### Worked example (illustrative)

A quantitative spatial model reports a welfare gain of 4.5% from removing a trade barrier. The threat map flags the externally-set migration elasticity as the prime suspect. Instead of one re-run, the authors report the welfare gain as a *function* of the elasticity across its literature-supported range — say 3.6% to 5.4% — and note that the qualitative conclusion (positive, economically meaningful) holds throughout. They then re-solve the model on a doubled grid to confirm the number is not a discretization artifact. This reads as confident and bounded; a single "robust to alternative elasticity" footnote would have invited exactly the objection it tried to dodge.

### What goes in the main text vs. the online appendix

With a ≤50-page ceiling, the robustness section competes for space with the contribution itself, so be ruthless about placement. The main text holds the one or two checks that retire the threats tied to the load-bearing assumption — these are part of the argument, not an addendum. Everything else (alternative control sets, secondary subsamples, placebo variants) goes to the online appendix, referenced in one sentence. A main text crowded with low-value re-runs signals defensiveness; a main text with two decisive checks and a clear pointer to the appendix signals an author who knows which threats matter.

### The honesty premium

The defining feature of robustness at a rigor journal is that **honest fragility, bounded, beats false robustness**. If a check moves the headline, the worst response is to omit it; the second worst is to bury it; the best is to report it and bound it ("the effect falls by a third under the alternative specification but remains positive and significant at conventional levels"). IER referees have seen every way of hiding a fragile result, and discovering a concealed one — especially via the replication deposit — is close to fatal. Treat the robustness section as the place where you demonstrate you have already tried hardest to break your own result and it survived.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). IER is theory-forward and quantitative; the chain below serves its empirical lane — structural / quantitative estimation uses the field's own solvers.

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

- [ ] Threats are listed in priority order; the load-bearing ones are in the main text, not the appendix
- [ ] Each main-text threat has one decisive check (not a pile of weak re-runs)
- [ ] Functional-form robustness shown for any result that could be a CES/log/quadratic artifact
- [ ] Externally-set/calibrated parameters varied over a defensible range; result reported as a function of them
- [ ] Inference matches the design (clustering / wild bootstrap / HAC); few-cluster handled
- [ ] Structural: counterfactual re-solved with finer grid / alternative solver to show numerical stability
- [ ] Any check that moves the result is reported honestly and bounded

## Anti-patterns

- A robustness appendix organized as a mechanical list with no statement of which threat each check addresses
- "Results are robust" asserted without showing the range over the uncertain parameter
- Twenty re-runs that all vary trivial controls while the load-bearing assumption goes untested
- Hiding a check that weakens the result instead of bounding the movement
- Significance asterisks standing in for honest standard errors / confidence sets
- Calling a structural counterfactual robust without re-solving on a finer numerical grid

## Referee pushback mapped to the robustness fix

- *"Is this just a functional-form artifact?"* → Re-do under an alternative class; show the sign/magnitude survives or bound how much it moves.
- *"The whole result rides on that calibrated parameter."* → Report the headline as a function of the parameter over its defensible range; state the threshold where the conclusion would change.
- *"One unit/period is driving everything."* → Drop influential subsamples and split the period; show the estimate is stable and no single observation is pivotal.
- *"Your standard errors are too generous."* → Match inference to the design (cluster-robust / wild bootstrap / HAC); show the conclusion holds once CIs widen honestly.

## Output format

```text
【Journal】International Economic Review
【Skill】ier-robustness
【Result under test】the headline number/sign
【Threat map】ranked threats → the decisive check for each
【Main-text checks】the 1–3 tied to the load-bearing assumption
【Parameter range】headline reported as a function of the uncertain parameter? [Y/N]
【Honest fragility】any check that moves it, with the movement bounded
【Inference】clustering/bootstrap/HAC matched to design? [Y/N]
【Verdict】robust / bounded-and-stated / fragile
【Next skill】ier-tables-figures
```

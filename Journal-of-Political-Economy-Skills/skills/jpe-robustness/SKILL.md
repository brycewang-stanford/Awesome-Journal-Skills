---
name: jpe-robustness
description: Use when the main result of a Journal of Political Economy (JPE) manuscript rests on a single specification and you need to pre-empt the alternative-explanation and fragility objections a Chicago referee will raise. Builds the robustness battery and the falsification logic; it does not establish the primary identification (see jpe-identification).
---

# Robustness & Alternative Explanations (jpe-robustness)

## When to trigger

- The headline result is one regression with one set of choices
- You have not ruled out the obvious competing economic explanations
- A structural result has not been shown to survive perturbing key assumptions
- You suspect a referee will say "this is fragile" or "this is mechanism A, not your mechanism B"

## The JPE logic of robustness

At JPE, robustness is not a ritual table of "still significant." It is an argument that **the economic interpretation survives**, and that rival mechanisms are ruled out. A Chicago referee thinks adversarially: which alternative economic story produces the same coefficient, and how do you exclude it? Over-reliance on a single specification is an explicit anti-pattern. And because a conditional accept triggers the **JPE Data Editor** rerunning your code against the **JPE Dataverse** deposit (JPE endorses DCAS; see `jpe-replication-package`), every robustness number must come from code that actually executes and reproduces — fragility you papered over will surface in verification. Distinguish three jobs:

1. **Specification robustness** — the number is not an artifact of arbitrary choices.
2. **Mechanism discrimination** — your channel, not a competing one, drives it.
3. **External / structural validity** — the result generalizes / the model's conclusions are not knife-edge.

## What to run

### Specification robustness
- Vary controls (parsimonious → saturated); show coefficient stability and use Oster (2019) δ / bounds for selection on unobservables.
- Alternative functional forms, sample windows, and exclusion of influential subsamples.
- Alternative standard-error structures (clustering level, wild bootstrap with few clusters).
- Inference robustness: randomization inference or permutation tests where design allows.

### Mechanism discrimination (the JPE-distinctive part)
- Name the 2–3 alternative economic mechanisms that could generate the same reduced-form sign.
- For each, design a test that the alternatives fail and your mechanism passes (heterogeneity that only your channel predicts, an auxiliary outcome, a dose-response the rival cannot explain).
- Triangulate: a second data source, a second identification strategy, or a structural-vs-reduced-form cross-check.

### Structural papers
- Sensitivity of estimates and counterfactuals to identifying assumptions and to fixed/calibrated parameters.
- Untargeted-moment fit; over-identification evidence.
- Alternative model specifications that nest or rival the baseline.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPE is top-5 general-interest economics; a credible design is the entry ticket — modern DiD/IV/RDD and the magnitude for a broad readership.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Coefficient stability across control sets shown; Oster-style selection bound reported
- [ ] Sample-window / outlier / subsample sensitivity reported
- [ ] Inference robust to clustering choice / few clusters
- [ ] The 2–3 rival economic mechanisms are named and tested against
- [ ] At least one triangulation (second data source, design, or structural cross-check)
- [ ] Structural results shown not to be knife-edge in key assumptions
- [ ] Robustness lives in the paper's appendix/online appendix, with main text stating the punchline

## Anti-patterns

- A wall of "still significant" tables that never address *why* the effect is your mechanism
- Treating robustness as cosmetic while the headline rival explanation goes untested
- Reporting only specifications that work; hiding the fragile ones (a referee will ask, and the JPE Data Editor reruns the code)
- Selection-on-unobservables waved away with "we control for X" and no bound
- Structural counterfactuals presented as point predictions with no sensitivity analysis
- Burying so many checks in the main text that the economic story is lost (use the online appendix)

## Output format

```
【Headline result】coefficient + interpretation
【Spec robustness】[controls, windows, SEs, Oster δ, ...]
【Rival mechanisms】1... 2... — test that discriminates each
【Triangulation】second source / design / structural cross-check
【Structural sensitivity】(if applicable)
【Residual fragility】honest statement of what is not bulletproof
【Next】jpe-tables-figures
```

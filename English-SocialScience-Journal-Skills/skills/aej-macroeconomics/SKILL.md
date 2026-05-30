---
name: aej-macroeconomics
description: Use when targeting American Economic Journal: Macroeconomics or deciding whether a macroeconomics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# American Economic Journal: Macroeconomics (aej-macroeconomics)

## Journal positioning

AEJ: Macroeconomics is the American Economic Association's field home for macro one tier below AER's general-interest bar. It publishes macro, monetary, growth, and business-cycle research — both quantitative/structural models (DSGE, HANK, heterogeneous-agent and quantitative frameworks) and empirical macro. The contribution can be field-specific rather than discipline-wide, but the model discipline or empirical identification must be top-quality; this is the natural home for serious macro that is excellent but narrower than a top-5 swing.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AEA site and the editorial-manager submission system.

## When to trigger

- The author names AEJ: Macro as the target, or is stepping down from a top-5 macro submission.
- A paper develops a quantitative/structural macro model (DSGE, HANK, heterogeneous-agent, growth) or a credible empirical-macro design.
- A strong macro paper is excellent but narrower than AER's general-interest bar and needs the right macro home.
- The author needs AEJ: Macro's desk-reject risks and a credible top-5 / macro-field alternative list.

## Scope & topic fit

- Business cycles, monetary and fiscal policy, growth, and macro-labor / macro-finance with a macro question at the core.
- Quantitative and structural macro: DSGE, New Keynesian, HANK and heterogeneous-agent models, search/matching, and calibrated/estimated quantitative models.
- Empirical macro: identified shocks (monetary, fiscal, news), VARs/local projections, and cross-country or regional macro evidence.
- Theory-with-quantitative-discipline papers that connect a mechanism to data via calibration or estimation.

## Method & evidence bar

- Model discipline or identification is the filter: structural models need clearly stated environments, sensible calibration/estimation, and quantitatively credible results; empirical macro needs a defensible identification of the shock or effect.
- Quantitative models should confront relevant moments or facts and show the mechanism is doing the work, not free parameters.
- Empirical-macro inference must use current standards (identified shocks, local projections, proper standard errors) and pre-empt the obvious alternative explanations.
- Data, code, and replication transparency is mandatory; the AEA data and code availability and verification policy applies, with deposit checked before acceptance.

## Structure & house style

- The introduction states the macro question, the model or identification, the headline quantitative result, and what it implies for the macro debate.
- Lead with the mechanism and its quantitative magnitude; relegate derivations, full model details, and robustness to appendices and online supplements.
- AEJ uses an unstructured abstract and JEL codes; computational details and sensitivity analysis live in the appendix.
- Exhibits should make the quantitative result (impulse responses, decompositions, counterfactuals) legible and tie back to the mechanism.

## Official-submission checklist

- Search the live site for "AEJ: Macroeconomics submission guidelines" and the AEA "Data and Code Availability Policy," and follow the current versions.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, and figure/table standards on the editorial-manager system.
- Re-check the current data/code and computational replication-package deposit and verification workflow (openICPSR / AEA Data Editor) — enforced before acceptance.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the macro question and the model or identification that answers it.
- [ ] The contribution is stated as mechanism / quantitative result / identification, not as statistical significance.
- [ ] The introduction positions the paper against the recent macro frontier on this question.
- [ ] The model is disciplined by data (calibration/estimation) or the empirical shock is credibly identified; results are quantitatively meaningful.
- [ ] Data, code, and computational replication package are ready for the AEA availability + verification workflow.

## Common desk-reject triggers

- A structural model with free parameters chosen to fit, where the mechanism is not shown to drive the result.
- Empirical macro with a poorly identified shock or VAR with no credible identification.
- A reduced-form regression with no macro mechanism or quantitative interpretation.
- "First to model X" framing with no quantitative or conceptual advance over existing macro models.

## Re-routing decision

- General-interest macro importance → `american-economic-review`, `quarterly-journal-of-economics`, or `journal-of-political-economy`; one crisp result → `aer-insights`.
- Monetary / business-cycle field-leading → `journal-of-monetary-economics`; dynamic-macro structural → `review-of-economic-dynamics`.
- Growth-focused → `journal-of-economic-growth`; frontier macro theory/methods → `review-of-economic-studies`.
- Empirical-macro measurement / shorter → `review-of-economics-and-statistics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] American Economic Journal: Macroeconomics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the model discipline / identification clear the macro-field bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / data-code policy / computational replication>
[Re-route suggestion] <if not a fit, a better-matched venue>
```

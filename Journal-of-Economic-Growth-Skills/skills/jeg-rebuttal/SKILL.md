---
name: jeg-rebuttal
description: Use when responding after a Journal of Economic Growth revise-and-resubmit to organize responses about growth mechanisms, model assumptions, empirical identification, calibration sensitivity, data availability, and Springer revision files.
---

# R&R Rebuttal (jeg-rebuttal)

## When to trigger

- A JEG revision decision has arrived
- Referees request stronger growth framing, theory, empirics, or calibration
- You need a response letter and aligned manuscript changes

## Triage

1. **Fit and contribution**: growth mechanism not clear enough.
2. **Theory**: assumptions, equilibrium, dynamics, comparative statics, or proofs.
3. **Empirics**: identification, sample, robustness, historical measurement, or
   external validity.
4. **Calibration/simulation**: parameter sources, targeted moments, sensitivity,
   transition paths.
5. **Policy and files**: data availability, declarations, source files.

## Response strategy

- Lead with the editor's synthesis and the highest-value changes.
- Add quantitative sensitivity where a calibration concern is central.
- Add comparative estimates where empirical growth literature raises conflicting
  results.
- Narrow claims when model or data scope is local.
- Update source files and declarations alongside the manuscript.

## Revision evidence map

For each major referee concern, identify the evidence type:

- **Mechanism concern** -> new model intuition paragraph, proposition, or transition-path figure.
- **Assumption concern** -> relaxed-assumption result, proof clarification, or sensitivity table.
- **Empirical concern** -> identification diagnostic, alternative sample, or comparative estimate.
- **Calibration concern** -> parameter-source table plus one-at-a-time and joint sensitivity.
- **Data concern** -> Data Availability Statement, code archive, source-file update, or access note.

The response letter should show which evidence changed the manuscript, not just where text was added.

## JEG referee objection playbook

Map the objections most common at this journal to their accepted repairs:

- "Spatial autocorrelation inflates your significance" → recompute Conley SEs at several distance cutoffs, add a spatially correlated placebo distribution, and put both in the revised table notes — not only in the letter.
- "The exclusion restriction is implausible" → confront each published alternative channel for the instrument, control for those channels directly, and add an over-identification or bounding exercise rather than restating the assumption with more conviction.
- "Persistence with no mechanism" → bring intermediate-period outcomes, a decomposition, or a model section, and promote the mechanism evidence to a main exhibit.
- "Calibration moments look cherry-picked" → add untargeted-moment validation plus one-at-a-time and joint sensitivity; tabulate every parameter's source.
- "The country sample is too selective for a growth claim" → expand or re-weight the sample and bound the claim's scope explicitly in abstract and conclusion.
- "This is not about growth" → reframe around divergence, convergence, or transition dynamics; growth editors rarely accept a fit defense made by assertion.

## Worked vignette — answering a spatial-inference objection

Illustrative R&R: Referee 2 argues the headline t-statistic of 4.8 on a persistence coefficient is an artifact of spatial correlation. The response that works:

1. Recompute Conley SEs at 100/250/500 km: t falls to 3.6/3.2/3.1 — significance survives; all three appear in the revised Table 2 notes.
2. Generate 1,000 spatial-noise placebo treatments with a matched correlation range; the true coefficient sits above the 99th percentile of the placebo distribution (illustrative).
3. Add macro-region fixed effects; the coefficient moves from 0.21 to 0.18, inside the original confidence band.
4. Letter structure: quote the concern, give the three numbers, point to the exact revised table and figure, and state what changed in the text — two paragraphs, zero defensiveness.

## Letter discipline for this venue

- When concerns overlap across referees, order responses by growth substance — fit, mechanism, identification, calibration — and cross-reference instead of duplicating analyses under each referee number.
- Quantify every concession: if the claim is narrowed, show the revised abstract sentence verbatim.
- Fold every new analysis into the replication package and say so in the letter; at a venue this data-disciplined, revision credibility extends to the artifacts.

## Output format

```text
[Decision] major / minor
[Main growth concern] ...
[New analyses/proofs] ...
[Sensitivity/robustness] ...
[Manuscript locations] ...
[Next step] resubmit through Springer portal
```

---
name: jpsp-study-design
description: Use when designing the multi-study package for a Journal of Personality and Social Psychology (JPSP) manuscript — sequencing studies, powering each one, choosing experimental / longitudinal / dyadic designs, and planning preregistration. Designs the study set; it does not collect or fabricate data.
---

# Study Design — The Multi-Study Package (jpsp-study-design)

This is the skill that most distinguishes JPSP from short-report journals. A JPSP paper is a
**coherent set of related studies** built to test a theory, not a single experiment. The package must
*converge*: each study should add something the previous one could not establish, and the set should
withstand the question "could one study break the whole story?"

## When to trigger

- Planning the sequence and roles of studies in the package
- Powering each study and the package as a whole
- Choosing designs (experiment, survey, longitudinal, dyadic/APIM, intensive-longitudinal, archival)
- Deciding what to preregister and what is exploratory

## Designing the package

1. **Give every study a job.** A common arc: **establish** the effect → test the **mechanism**
   (mediation/process) → probe **boundary conditions / moderators** → demonstrate **generalization**
   (population, context, method). Avoid a pile of near-identical replications.
2. **Triangulate methods.** Combine, e.g., an experiment (causal) with a field/longitudinal study
   (external validity) so the package is robust to any single design's weaknesses.
3. **Mind the section's study budget.** **IRGP caps the main text at 5 studies**; additional studies
   go to supplemental materials with results summarized briefly. Prioritize the studies that carry
   the argument. (Section-specific; verify — 待核实.)
4. **Power each study explicitly.** Plan against the **smallest effect size of interest**, not a
   pilot estimate. Use simulation for multilevel/dyadic/within-subject designs; justify N per study.
5. **Preregister.** Register hypotheses, design, sampling/stopping rule, and analysis for confirmatory
   studies; mark exploratory studies as such. JPSP is **TOP Level 2** and asks you to state
   preregistration status (see `jpsp-open-science-and-transparency`).
6. **Design for the internal meta-analysis.** Use comparable measures/effect metrics across studies
   so effects can be **pooled** later (`jpsp-data-analysis`); plan it now, not after the fact.
7. **Build in alternative-explanation tests.** At least one study should rule out the most salient
   alternative account (construct, confound, alternative mediator).

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPSP is predominantly experimental social/personality psychology; randomization inference, mediation done right (`mediate`, not naive controlling-away), power, and family-wise corrections are decisive.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference, `romano_wolf` for many-outcome
  family-wise control, and `mediate` for mediation (not naive controlling-away).
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the effect size in interpretable units; route the full battery to the
appendix/supplement. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A "package" that is one study run several times with cosmetic changes
- Underpowered studies whose null results are then waved away
- Adding studies reactively in revision instead of designing the set up front
- Designing studies with incomparable measures, making internal meta-analysis impossible
- Treating preregistration as paperwork rather than a constraint on later analysis

## Post-credibility-revolution power calibration

Since the open-science reforms, JPSP reviewers treat underpowering as a *central* limitation. The anchors below are **illustrative**, not mandated thresholds — confirm any quantitative expectation against the journal's current submission guidelines, since JPSP publishes no fixed N or power floor.

| Design | Smallest effect of interest (illustrative) | Reviewer reflex if underpowered |
|--------|--------------------------------------------|----------------------------------|
| Two-group between-subjects (ASC) | d = 0.30 | "Your null is uninterpretable — too few cases to detect your own effect" |
| 2×2 interaction (boundary) | f = 0.10 | "The moderation rests on an interaction you never powered" |
| Dyadic / APIM (IRGP) | β ≈ 0.15 | "Partner effects are noise at this dyad count" |
| Multilevel / ESM (PPID) | within-person slope | "Random-slope variance is unidentified here" |

Plan against the **smallest effect of interest**, never a noisy pilot d: a pilot d = 0.6 "powering" a study at N = 30 per cell is the classic way JPSP packages collapse on replication. For interactions and partner paths, simulate (`simr`, `DeclareDesign`) rather than a closed-form G*Power main-effect calculation.

## Worked vignette: powering a three-study ASC package

*Illustrative numbers — invented to show design logic, not real findings.*

Claim: **incidental gratitude broadens construal level** (an ASC social-cognition effect).

- **S1 (establish).** Gratitude vs. neutral recall; DV = construal. Smallest effect d = 0.35 → N = 260 (~85% power); preregistered. Result d = 0.34, 95% CI [0.10, 0.58].
- **S2 (mechanism).** Adds self-transcendence mediator; bootstrap indirect path needs more N than the total effect, so N = 320. Result ab = 0.12, 95% CI [0.04, 0.21].
- **S3 (boundary).** 2×2 gratitude × time-pressure, community sample; interaction at f = 0.10 → N ≈ 520. Interaction d = 0.28, 95% CI [0.05, 0.51].

A referee checks for a comparable construal metric across all three (so they pool into one **internal meta-analysis**), S3 ruling out a mood-valence confound, and a non-student sample answering "is this just undergraduates?"

## Output format

```
【Study set】S1 (establish) · S2 (mechanism) · S3 (boundary) · S4 (generalize) …
【Designs】experiment / longitudinal / dyadic-APIM / archival per study
【Power】N per study + smallest effect size of interest + method (sim?)
【Study budget】≤ section cap? (IRGP ≤5 in main text) extras → supplement
【Preregistration】what is confirmatory vs exploratory
【Meta-analysis ready】comparable effect metrics across studies? [Y/N]
【Next】jpsp-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — power (G*Power, simr, Superpower), DeclareDesign, dyadic/multilevel tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — section study caps and length rules

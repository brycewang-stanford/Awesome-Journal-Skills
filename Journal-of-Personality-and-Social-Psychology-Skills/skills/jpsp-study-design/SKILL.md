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

## Anti-patterns

- A "package" that is one study run several times with cosmetic changes
- Underpowered studies whose null results are then waved away
- Adding studies reactively in revision instead of designing the set up front
- Designing studies with incomparable measures, making internal meta-analysis impossible
- Treating preregistration as paperwork rather than a constraint on later analysis

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

---
name: lang-data-analysis
description: Use when planning or auditing the analysis of a Language (LSA) manuscript so the evidence credibly supports the theoretical claim. Covers quantitative modeling (mixed-effects in R), phonetic measurement, corpus statistics, and the analytic trail from glossed data or judgments to the generalization. Improves the analysis chain; it does not fabricate results.
---

# Data Analysis (lang-data-analysis)

At *Language* the analysis exists to make the **theoretical claim credible** — not to display
technique or notation. A cross-subfield, double-anonymous reviewer will ask whether the evidence
actually warrants the generalization and whether uncertainty is handled honestly. Where the work is
quantitative, *Language* now expects **properly specified models** (typically mixed-effects models in
R) rather than by-subject t-tests or raw counts; where it is analytic, it expects the pattern to be
demonstrable from the glossed data. This skill stress-tests the analysis chain in the idiom of your work.

## When to trigger

- Planning the analysis, or auditing it before writing up
- A reader doubts the statistics, the evidence-to-claim link, or the treatment of variability
- Reconciling multiple data sources (corpus + experiment, judgments + text) into one argument
- Deciding which analyses are confirmatory vs. exploratory

## Analysis norms (by mode)

### Quantitative (experiment / corpus)
- Fit **mixed-effects models with the random-effects structure the design justifies** (crossed
  by-subject and by-item random effects; random slopes for within-cluster predictors). Report the
  model, not just p-values.
- Report **effect sizes and intervals**, not stars alone; state the coding/contrasts and the
  convergence status; keep seeds and pinned package versions.
- Distinguish **preregistered/confirmatory** from **exploratory** analyses where applicable.

### Phonetic
- State measurement settings (windowing, formant ceilings, alignment) and how outliers/mis-tracks were
  handled; show the effect is not an artifact of the measurement pipeline.

### Analytic (formal)
- Demonstrate the generalization **directly from numbered, glossed examples**; show the analysis
  derives the attested cases and blocks the unattested ones.

### Historical / typological
- Make the inferential logic explicit (implicational universals, reconstruction, statistical
  tendencies); guard against non-independence of the sample.

## Convergent evidence (a Language strength)

*Language* rewards a generalization shown through **more than one window** — e.g., an experimental
effect corroborated by a corpus trend, or judgments backed by text frequencies. When windows disagree,
say so and explain the discrepancy rather than hiding the inconvenient one.

## Referee-pushback patterns on the evidence chain (Language fixes)

| Referee writes… | The Language-specific fix |
|-----------------|---------------------------|
| "No random effects / pseudoreplication." | fit the justified mixed model; cluster by subject and item |
| "Significance without effect size." | report estimates + intervals in interpretable units |
| "The stat model doesn't match the design." | align random-effects structure with the sampling |
| "Analysis doesn't rule out the alternative." | show it derives attested and blocks unattested cases |

## Calibration (Language appetite, hedged)

Orienting heuristics; confirm against the current author pages. *Language* increasingly expects that a
quantitative claim rests on a model appropriate to the clustered, repeated-measures nature of
linguistic data — the modal avoidable failure is pseudoreplication (ignoring by-speaker or by-item
structure). Illustrative: a paper claims a durational contrast "is significant (p < .01)" from 1,200
tokens produced by 8 speakers, analyzed as if independent. A referee writes "pseudoreplication." The fix
refits a mixed-effects model with by-speaker and by-word random intercepts and slopes, reports the
estimate (an illustrative 12 ms, 95% CI ~4–20), and notes two speakers who show no effect — turning a
fragile claim into a credible, bounded one.

## Anti-patterns

- Treating repeated measures as independent (pseudoreplication); stars-only reporting
- A statistical model whose random structure ignores the sampling design
- Phonetic effects that are artifacts of measurement settings, not language
- Cherry-picked examples that ignore counterexamples in the same corpus/elicitation
- Presenting exploratory results as if confirmatory
- Notation or technique foregrounded over the generalization it is meant to support

## Evidence pass for Language

Treat this skill as an executable review pass, not a prose hint. First lock the empirical
generalization, evidence base, warrant, and theoretical payoff; then judge whether the manuscript
answers the venue's real reader: linguists across subfields who value grounded analysis, transparent and
checkable evidence, and careful, appropriately scoped generalizations.

- **Do the pass:** audit the analysis before polishing prose — unit of analysis, random-effects
  structure, effect sizes, measurement pipeline, exclusions, and reproducibility must be visible.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows so the next agent can
  edit rather than rediscover the issue.
- **Sibling guard:** compare against *Laboratory Phonology*, *Journal of Memory and Language*,
  *Language Variation and Change*; if a sibling owns the contribution, recommend re-routing before
  polishing.
- **Stop condition:** do not give submission-ready advice until `resources/official-source-map.md` has
  been checked and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Claim under test】from theory-building
【Primary evidence】the analysis that carries the claim
【Model】mixed-effects structure matches the design? [Y/N/NA]
【Uncertainty】effect sizes + intervals reported? [Y/N]
【Convergence】corroborated across windows? [Y/N/NA]
【Confirmatory vs. exploratory】labeled where relevant? [Y/N]
【Next】lang-data-and-transparency
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — R / lme4 / brms, Praat, corpus tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Language quantitative and evidence expectations

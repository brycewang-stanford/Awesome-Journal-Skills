---
name: psychbull-inclusion-and-coding
description: Use when defining eligibility criteria and coding studies for a Psychological Bulletin review or meta-analysis — inclusion/exclusion rules, a codebook, double-coding, and inter-rater reliability. Governs how studies enter and are coded; effect-size modeling lives in psychbull-meta-analysis-methods.
---

# Inclusion & Coding (psychbull-inclusion-and-coding)

The credibility of a synthesis rests on **transparent, pre-specified eligibility** and **reliable
coding**. Decisions about which studies are in — and how their features are coded — must be
reproducible and made by **at least two trained coders** with documented agreement. This skill governs
eligibility and coding; the statistical model lives in `psychbull-meta-analysis-methods`.

## When to trigger

- Writing eligibility (inclusion/exclusion) criteria before full-text screening
- Building the **codebook** for study features, moderators, and effect-size inputs
- Setting up **double-coding** and computing **inter-rater reliability**
- A reviewer questions selection or coding decisions

## Eligibility criteria

- **Pre-specify** inclusion/exclusion rules (population, design, measures, outcome, time window,
  language, publication type) in the **protocol**, before screening (see
  `psychbull-open-science-and-transparency`).
- Operationalize each rule so two screeners apply it the same way; pilot on a sample and refine.
- Two-stage screening: **title/abstract → full text**, each by two screeners, with a **reconciliation
  log** and exclusion reasons feeding the PRISMA flow.

## Codebook & double-coding

1. **A written codebook** with explicit decision rules for every variable: study descriptors, design,
   sample, measures, risk-of-bias/quality indicators, candidate **moderators**, and the **statistics
   needed to compute effect sizes** (means, SDs, ns, correlations, ORs, test statistics).
2. **Double-code** all (or a substantial, documented subset of) studies; resolve disagreements by
   discussion or a third coder; record the resolution.
3. **Capture what you need for the effect size**, including the **direction** of effects and any
   sign-flips, plus enough to handle **multiple effect sizes per study** (dependency) downstream.

## Inter-rater reliability

- Report a reliability statistic: **Cohen's / Fleiss' kappa** for categorical codes, **ICC** for
  continuous codes; report the value and how disagreements were resolved.
- For study quality / risk of bias, use a documented appraisal scheme and report it.

## Anti-patterns

- Eligibility criteria invented after seeing which studies give the desired result
- A single coder, or no reliability statistic reported
- A codebook so vague that coders silently diverge
- Dropping "inconvenient" studies without a rule that excludes them
- Losing the data needed to compute effect sizes (no SDs/ns) — recoverable only by author contact

## What referees check on eligibility and coding

At the APA's flagship synthesis journal, eligibility and coding are where a reviewer probes whether the
study pool is principled and the data are trustworthy. The bar they apply:

| Referee expectation | Pass | Major-revision / reject trigger |
|---------------------|------|----------------------------------|
| Pre-specified criteria | Eligibility fixed in the protocol before screening | Rules that shift to admit favorable studies |
| Two-stage screening | Title/abstract → full text, two screeners, reconciliation log | One screener, no audit trail |
| Codebook completeness | Covers moderators *and* every effect-size input | Vague codes; SDs/ns not captured |
| Reliability reported | κ or ICC with a resolution procedure | No agreement statistic at all |
| Dependency captured | Multiple effects per study coded for downstream RVE | Effects collapsed silently, losing structure |

## Worked vignette — coding the intervention pool

*Illustrative numbers only.* Screening for the self-affirmation synthesis takes 1,640 deduplicated
records to 188 full texts to k = 42 included studies. Under this skill's rules:

- **Eligibility** (population, randomized design, validated outcome, 1995–2024, English) was fixed in
  the OSF protocol before any full text was read.
- **Double-coding** covered all 42 studies; first-pass agreement was κ = 0.81 on categorical codes and
  ICC = 0.92 on continuous codes; 14 disagreements went to a third coder and were logged.
- **Effect-size inputs** (means, SDs, ns, and 6 test-statistic conversions) were captured with their
  direction, so g could be recomputed independently.
- **Dependency**: 9 studies reported 2–4 effects each, all coded so the analysis can apply RVE rather
  than treating them as independent.

## Referee pushback → venue-specific fix

- *"Your inclusion rules look like they shifted mid-stream."* → Show the timestamped protocol; document
  any amendment with its date and rationale, not a silent edit.
- *"No inter-rater reliability is reported."* → Add κ/ICC values and the disagreement-resolution
  procedure; double-code a documented subset if full coverage is infeasible.
- *"Effect sizes can't be reverified from your table."* → Restore the means/SDs/ns or test statistics so
  each g is independently recomputable.

## Output format

```
【Eligibility】pre-specified in protocol? [Y/N] + key rules
【Screening】two screeners, reconciliation log? [Y/N]
【Codebook】covers moderators + effect-size inputs? [Y/N]
【Double-coding】coverage + disagreement resolution
【Reliability】kappa / ICC value(s)
【Next】psychbull-meta-analysis-methods
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — screening tools and reliability packages (`irr`, `psych`)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — MARS coding/eligibility reporting expectations

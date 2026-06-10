---
name: rof-topic-selection
description: Use when judging whether a finance idea clears the Review of Finance (RoF) general-interest bar before any estimation or modeling — first-order question, fit with the journal's empirical-and-theoretical scope, and the top-three-finance-journal standard RoF referees apply.
---

# Topic Selection (rof-topic-selection)

## When to trigger

- The question feels incremental or sub-field-only ("yet another anomaly")
- You are unsure whether RoF (vs. a specialist field journal) is the right home
- You have data or a model but no first-order finance question yet
- You want to gauge fit before paying the submission fee

## The RoF bar

RoF publishes **general-interest finance at the level of the top-three finance journals**, as the **official journal of the European Finance Association (EFA)**. Its referees are explicitly asked to **apply top-three-finance-journal standards**, so the screening question is "would this interest the broad finance audience and survive a top-three referee?" RoF is genuinely **both empirical and theoretical** — asset pricing, corporate finance, banking, household finance, microstructure on the empirical side; asset-pricing theory, security/contract design, microstructure theory on the theory side. A clean theoretical result with a sharp economic message fits as well as a credible empirical finding.

## Fit tests

1. **First-order question** — does the answer change how finance researchers think, not just add a decimal to a known coefficient?
2. **Generality** — is the lesson portable beyond one market, one country-year, one dataset?
3. **Standard** — could a top-three-finance referee call this publishable there? RoF aims for that quality.
4. **Empirical vs. theory clarity** — an empirical paper needs credible identification (→ `rof-identification-strategy`); a theory paper needs clean assumptions, a non-obvious result, and economic interpretation.
5. **Process fit** — RoF charges a real fee (EUR 350; EUR 300 for EFA members) and runs a **two-round** process; a paper needing five rounds to become interesting is a poor fit.

## Two-candidate worked screen

Illustrative. **Candidate A**: "Do Italian cooperative banks lend differently?" —
single-country, descriptive; fails the generality test unless rebuilt around what
cooperative ownership reveals about lending under soft information everywhere, with a
cross-country counterpart. As posed, it is a field-journal paper. **Candidate B**: "Does
deposit-insurance design change bank risk-taking? Evidence from staggered EU coverage
harmonization" — institution-driven variation across many countries, a first-order
question with both an empirical and a theoretical audience inside RoF's scope. Verdict: B
clears the bar as-is; A needs the reframe before the fee is worth paying.

## Where RoF-fit questions come from

- Institutional variation Europe generates naturally: directive transpositions staggered
  across member states, ECB policy innovations, national supervisory experiments — shock
  designs a US-only dataset cannot offer, aimed at universal forces.
- Frontier areas the EFA community is actively building: sustainable and climate finance,
  fintech and digital payments, household finance — still subject to the general-interest
  framing test, not exempt from it.
- The EFA annual-meeting program as a barometer: sessions dense with top-three authors
  mark where the standard is currently being set and where the closest competitors are.

## Pre-fee screening questions

- Would the paper stay interesting if the headline coefficient halved? Interest that
  survives magnitude risk is the safer bet at a two-round journal.
- Can you state the lesson without naming the country or the dataset? If not, generality
  is missing.
- Is there both a theory reader and an empirical reader who care? RoF's scope is genuinely
  both, and the broadest papers speak to each.
- Is the natural experiment yours alone for long? If competitors loom, the Fast-Track
  calculus enters early (→ `rof-submission`).

## Anti-patterns

- A within-subfield estimate with no broad finance lesson — reads as a field-journal paper.
- A theory model with a foregone-conclusion result dressed in heavy notation.
- "First to study X in country Y" novelty with no first-order stake.
- Choosing RoF to dodge fees elsewhere — fit, not cost, should drive the choice.

## Output format

```
【Question】one sentence, plain language
【Type】empirical / theoretical / both
【First-order?】[Y/N] — why
【Top-three-standard?】[Y/N]
【General lesson】beyond this setting: ...
【Verdict】RoF-fit / redirect / reframe
【Next step】rof-contribution-framing
```

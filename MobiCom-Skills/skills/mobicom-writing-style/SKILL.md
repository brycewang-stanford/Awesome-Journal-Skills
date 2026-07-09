---
name: mobicom-writing-style
description: Use when drafting or revising a MobiCom paper for house style — putting the wireless/mobile mechanism and its operating regime on the first page, pairing every claim with over-the-air measurement, replacing superlatives with percentiles and intervals, and fitting the argument into the double-column 12-page body.
---

# MobiCom Writing Style

A MobiCom paper reads as a **mechanism justified by measurement**. The first page states a
wireless or mobile-networking problem, the mechanism that addresses it, and the measured
evidence — before any implementation detail. The double-column 12-page body is for the core
argument; derivations, protocols, and extra results go to references and appendices.

## The first-page arc

Put this in the abstract and first page, in order:

1. **The wireless/mobile pain** — the concrete condition that breaks existing designs
   (a fade under mobility, interference, a spectrum constraint, an energy limit).
2. **Why existing mechanisms fall short** — each prior approach gets a *specific, named*
   failure tied to the condition, not "prior work is limited."
3. **The mechanism** — what is new, stated as a networking/PHY-MAC/routing/sensing
   mechanism, with its **operating regime** named (distance, mobility, channel, power).
4. **The measured evidence** — the headline result with its condition and its uncertainty,
   not a bare "up to N×."
5. **Why it matters for mobile networking** — the community-level payoff.

See [`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md)
for a before→after that executes this arc.

## Name the operating regime

The single most common wireless-writing failure is a claim with an unstated envelope. Every
headline claim carries its regime:

| Vague | MobiCom-calibrated |
|---|---|
| "achieves high throughput" | "sustains X at 1-4 m NLOS under pedestrian mobility" |
| "low power" | "energy-per-bit within the harvested budget at Y% duty cycle" |
| "robust to interference" | "holds delivery above threshold at Z dB co-channel interference" |
| "works in real settings" | "measured over the air in a furnished room with walkers" |

A reviewer cannot fault — or reward — a claim whose conditions are hidden. Stating the
regime is not hedging; it is the claim.

## Claims are paired with evidence

Every major claim maps to a proof, a figure, a measured condition, or a reproducibility
location. Build the map before submitting:

```text
Claim -> evidence pairing (fill for each headline sentence):
  "decodable through fades"  -> Fig. 3 (delivery vs walker path) + channel traces
  "within energy budget"     -> Fig. 4 (energy-per-bit) + instrument note (App. B)
  "no dedicated carrier"     -> system description Sec. 3 + power measurement
An unpaired claim is either cut or demoted to future work.
```

## Percentiles, not superlatives

- Report **distributions and confidence intervals**, not single best runs or unqualified
  maxima. "Up to N×" without the spread behind it is a review risk (`mobicom-experiments`).
- Prefer the **median and a tail** over the mean alone when the metric is delivery or
  latency; wireless distributions are skewed.
- Avoid "significantly" as prose; show the interval and let it speak.

## Fitting the double-column 12 pages

- Figures and tables **count** against the 12; a radio-testbed diagram and three CDFs is
  real page budget. Triage content, never geometry (`mobicom-submission`).
- The **body carries the mechanism and its headline evidence**; channel-model derivations,
  full protocols, extended sweeps, and instrument details go to **appendices after the
  references**, outside the cap (`mobicom-supplementary`).
- Keep the introduction's roadmap to one or two sentences; over-signposting substitutes for
  argument.
- Do not put the strongest result only in an appendix — reviewers should not reconstruct the
  contribution from supplementary material.

## Prose discipline

- Lead sections with the finding, then the method — not a chronological lab diary.
- Name the abstraction or mechanism once and use the name consistently.
- Separate **engineering effort** from **research contribution**: building a testbed is
  work, but the contribution is the mechanism it demonstrates.

## Revision checklist

- [ ] Mechanism and operating regime on the first page.
- [ ] Each prior-work line has a specific, named failure.
- [ ] Every headline claim paired to a figure, condition, or appendix.
- [ ] Distributions/intervals replace superlatives throughout.
- [ ] Figures/tables budgeted against the 12 double-column pages.
- [ ] Strongest result in the body, not only the appendix.

## Output format

```text
[First page] mechanism + regime present? y/n — what is missing
[Regime] which headline claims lack a stated envelope
[Claim map] unpaired claims listed for cut-or-support
[Superlatives] flagged phrases -> distribution/interval replacement
[Page budget] over/under 12; what to move to appendix
```

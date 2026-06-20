---
name: jue-writing-style
description: Use when the prose of a Journal of Urban Economics (JUE) manuscript buries the spatial mechanism, or the intro/abstract do not land for an urban-economics audience. Sharpens the writing to JUE house voice; it does not run analysis or build exhibits. Late-stage — invoke after identification and the mechanism settle.
---

# Writing Style (jue-writing-style)

## When to trigger

- The introduction explains the data and method before it says what is *spatially* new
- The abstract reads like a generic applied-micro paper — space could be deleted and it would still parse
- A reader cannot state the urban mechanism in one sentence after the intro
- The policy or theory implication is asserted at the end rather than threaded through
- The draft uses spatial-econometrics jargon where a plain mechanism sentence would land harder

## The JUE intro arc

JUE referees read the first page to decide whether the paper is a real urban-economics contribution. A JUE introduction should, in order:

1. **Open with the spatial question and why it matters** for cities, housing, or local policy — not with a literature gap.
2. **Name the spatial mechanism** in one sentence a non-specialist urban economist would grasp (capitalization, agglomeration spillover, sorting, congestion, market access).
3. **State the identifying variation** plainly — the boundary, the shift-share, the policy rollout — and why it is credible against sorting and spillovers.
4. **Give the headline magnitude in interpretable units** (a % capitalization, an elasticity), early, so the reader knows the answer.
5. **Place the contribution** against the right strand in 2–3 sentences (handoff from `jue-literature-positioning`).
6. **Preview the equilibrium reading** — what the estimate means once agents re-sort, and the policy implication.

## House voice

- **Spatially grounded, mechanism-first.** Lead with the economics of place; let the method serve the mechanism, not the reverse.
- **Concrete geography.** Name the cities, the corridor, the policy — readers of an urban journal expect institutional texture, not abstract "regions."
- **Magnitudes over significance.** "Prices rose 4.5%" beats "the coefficient is significant"; JUE cares what the number means for welfare and policy.
- **Honest about the local estimand.** Say plainly that a boundary or LATE estimate is local; do not let the prose imply a city-wide or national effect.
- **Plain over jargon.** Use "households sort across neighborhoods" rather than dense spatial-econometrics phrasing where the plain sentence is clearer.

## Section discipline

- **Abstract:** spatial question → design → headline magnitude → implication, in ~150 words; references in full if cited (检索于 2026-06；以官网为准 for exact limits).
- **Data section:** make the geography legible — units, coverage, how locations are defined and matched.
- **Results:** lead each table with the mechanism it tests, not "Table 3 shows."
- **Conclusion:** the equilibrium and policy reading, with the local-estimand caveat restated.

## Checklist

- [ ] First paragraph states the spatial question and why it matters, not a literature gap
- [ ] The urban mechanism is stated in one plain sentence
- [ ] The identifying variation and its credibility (vs sorting/spillovers) are in the intro
- [ ] The headline magnitude appears early, in interpretable units
- [ ] The local nature of the estimand is honest throughout the prose
- [ ] Geography is concrete (named cities/policies), not abstract "regions"
- [ ] Abstract follows question → design → magnitude → implication
- [ ] The abstract collapses if spatial words are deleted (the fit test passes)
- [ ] The policy reading is earned by the estimand, not a bolted-on closing paragraph

## Anti-patterns

- An intro that leads with method and data before the spatial mechanism
- An abstract from which "space" could be deleted with no loss — the fit tell
- Reporting significance instead of an interpretable magnitude
- Prose that lets a local boundary/LATE estimate read as a city-wide effect
- Abstract "regions" with no institutional or geographic texture
- Dense spatial-econometrics jargon substituting for a clear mechanism sentence

## Words that signal a JUE paper vs a misfiled one

The vocabulary should make the spatial economics unavoidable. Lead with the primitives the field owns — capitalization, agglomeration, sorting, spatial equilibrium, market access, supply elasticity, incidence, reallocation. Avoid letting the paper drift into a-spatial framing ("treatment effect on outcome Y") where the geographic mechanism is the point. At the same time, do not over-reach into economic-geography vocabulary (clusters, milieu, path dependence) that signals JEG rather than JUE, nor into pure spatial-econometrics framing that signals RSUE. The register is applied urban economics: concrete, mechanism-first, magnitude-led.

## Threading the policy reading

JUE values papers that bear on urban policy, but the implication must be *earned by the estimand*, not bolted on. Thread it: state in the intro why the magnitude matters for housing, transport, or place-based policy; in the results, note what each estimate implies; in the conclusion, give the policy reading with the local-estimand caveat restated. Avoid the failure mode of a rigorous paper that ends with a generic "policymakers should consider..." paragraph disconnected from what was actually identified.

## The abstract test

The fastest fit diagnostic for a JUE submission is the abstract deletion test: cross out every spatial word and read what remains. If the abstract still describes a coherent, complete result, the paper is probably not a JUE paper — the geography is a label, not the economics. A JUE abstract should collapse without its spatial terms because capitalization, sorting, agglomeration, or market access *is* the result. Rewrite until the spatial mechanism is structurally necessary to the sentences, then confirm the four-beat arc (question → design → magnitude → implication) survives within the word limit (检索于 2026-06；以官网为准 for the exact count).

## Worked vignette (illustrative)

A draft opens: "We use a regression discontinuity design with administrative data to study attendance boundaries." A JUE rewrite leads with mechanism and magnitude: "Households pay to live on the better-school side of an attendance boundary; we show this capitalization is 4.5% of house value at the line, identified by comparing otherwise-identical homes a block apart. Because the boundary is arbitrary relative to housing and amenities, the jump isolates willingness to pay for school quality — a magnitude that bears directly on the welfare case for school-finance equalization." The method now serves the mechanism.

## Output format

```text
【Intro arc】question→mechanism→variation→magnitude→contribution→equilibrium present? [Y/N each]
【Mechanism sentence】one plain sentence
【Headline magnitude】in interpretable units, stated early? [Y/N]
【Estimand honesty】local estimand not oversold? [Y/N]
【Geography】concrete (named) vs abstract?
【Abstract】question→design→magnitude→implication, ~150w? [Y/N]
【Next skill】jue-replication-package
```

> Do not run this skill until identification and the spatial mechanism are settled — rewriting the intro around a magnitude that still moves wastes the polish and invites a second rewrite after the next robustness round.

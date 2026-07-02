---
name: prl-methods
description: Use when deciding what methodological detail belongs in a Physical Review Letters body versus Supplemental Material, so a physicist can trust the result without the Letter becoming a long paper. Partitions methods; does not design figures or run analysis.
---

# PRL Methods (prl-methods)

## When to trigger

- Your Methods text is several paragraphs of apparatus, sample, or derivation detail
- You cannot tell what a reader *needs* versus what is reassuring completeness
- Reviewers of a prior draft asked for more rigor, and you are tempted to add bulk
- The Letter is over length and methods are a prime trimming target
- You are unsure which derivation steps to keep inline versus move to SM

## The trust-minimum principle

In a Letter, methods exist to let a competent physicist **believe the central claim** — not to enable full replication inline. Full replication detail lives in Supplemental Material. Keep in the body only what is load-bearing for trust:

- The essential experimental configuration or theoretical setup (one compact description).
- The key control(s) that rule out the obvious alternative explanation.
- The decisive statistical/systematic statement (uncertainties, significance) for the headline number.
- The one or two equations that define the quantity being claimed.

Everything else — calibration procedures, sample growth, full Hamiltonians, lengthy derivations, parameter sweeps, additional checks — goes to SM and is cited inline ("see Supplemental Material [ref]").

## Partition table

| Detail type                                  | Body (trust-minimum)              | Supplemental Material            |
|----------------------------------------------|-----------------------------------|----------------------------------|
| Core setup / model definition                | one compact paragraph             | full apparatus / full Hamiltonian|
| Defining equations                           | 1–2 that define the claim         | full derivation chain            |
| Key control ruling out the obvious artifact  | yes, stated explicitly            | secondary controls               |
| Uncertainty on the headline result           | yes (stat + dominant syst)        | full error budget                |
| Sample / material preparation                | one-line provenance               | growth, characterization data    |
| Numerical convergence / mesh                  | one-line assurance                | convergence study                |
| Reproducibility info (code/data location)    | pointer                           | data-availability detail         |

## Rigor without bulk

PRL referees in physics are sharp about systematics and alternative explanations. Pre-empt the obvious objection **in the body**, briefly, and point to the SM for the exhaustive version. A single sentence ruling out the leading artifact is worth more than a paragraph of generic robustness language.

- State uncertainties as numbers, separating statistical and dominant systematic.
- Name the alternative explanation and the control that excludes it.
- For theory: state assumptions explicitly; relegate algebra to SM but keep the physical logic inline.

## Worked micro-example: compressing an apparatus paragraph

**Before (regular-article register):**

> "The cryostat was cooled over 48 hours. Thermometry used a calibrated sensor. Wiring consisted of filtered twisted pairs. Measurements used a lock-in amplifier after verifying frequency independence."

**After (trust-minimum, one sentence + SM pointer):**

> "Measurements were performed in a dilution refrigerator with filtered wiring and calibrated thermometry; checks bounding self-heating below the quoted uncertainty are given in the Supplemental Material [ref]."

The rewrite keeps what a skeptical physicist needs — the environment, the leading artifact class, where the exhaustive checks live — and returns a paragraph of budget to the physics.

## Sentence patterns that buy trust cheaply

- **Control-in-a-clause:** "The signal is absent at zero applied field, ruling out pickup as its origin."
- **Split uncertainty:** "We obtain X = value ± (stat) ± (syst), the systematic dominated by calibration drift."
- **Assumption flag (theory):** "Throughout we assume [condition]; relaxing it modifies only the prefactor (SM Sec. S2)."
- **Convergence one-liner:** "Results are converged in system size to within the plotted symbol size."

Each pattern replaces a defensive paragraph with one load-bearing sentence.

## Checklist

- [ ] Body methods are the minimum needed to trust the central claim
- [ ] The leading alternative explanation is named and addressed inline
- [ ] Headline result carries stated statistical + dominant systematic uncertainty
- [ ] Only claim-defining equations are inline; derivations are in SM
- [ ] Every "see SM" pointer resolves to actual SM content
- [ ] Data / code availability has a concrete pointer
- [ ] No replication-completeness padding in the body

## Anti-patterns

- Treating the Letter like a full PR article and inlining the whole method
- Generic robustness boilerplate instead of the one decisive control
- Quoting a headline number with no uncertainty, or merged stat+syst
- Equations with undefined symbols (define on first use)
- "Details available on request" instead of a data-availability statement

## Output format

```
【Trust-minimum kept inline】setup / key control / uncertainty / defining eqs
【Moved to SM】list
【Leading alternative explanation】named + control inline?  yes / fix
【Headline uncertainty】stat + syst stated?  yes / fix
【Data availability】pointer present?  yes / fix
【Next】prl-figures (lead figure) or prl-supplementary (SM partition)
```

> Data-availability and reproducibility expectations evolve — verify current APS policy on the official PRL author page.

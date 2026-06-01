---
name: mathfin-literature-positioning
description: Use when positioning a Mathematical Finance (Wiley) manuscript against the financial-mathematics frontier — stake the methodological contribution against prior stochastic-analysis, pricing, and control results, citing the precise theorem you sharpen, generalize, or supersede.
---

# Literature Positioning (mathfin-literature-positioning)

## When to trigger

- The introduction reads as a survey rather than a precise contribution claim
- Unsure which prior theorem your result generalizes, sharpens, or contradicts
- A referee might say "this is already known under weaker/stronger assumptions"

## The Mathematical Finance positioning bar

Because the journal prizes **methodological novelty and contribution to financial modelling**,
positioning must be **theorem-level**, not topic-level. The reader (often a Bachelier Finance
Society member steeped in stochastic analysis) wants to know exactly which assumptions you
relax, which generality you add, or which open problem you close — and why earlier machinery
could not. A vague "the literature has studied X" invites a desk concern about novelty.

## How to position

1. **Name the closest prior result** and its assumptions precisely (model class, regularity,
   filtration, market completeness). State what it *cannot* deliver.
2. **Locate your delta on one axis**: weaker assumptions, broader model class, sharper rate,
   constructive vs. existence-only, time-consistent vs. not, or a genuinely new object.
3. **Cite landmark machinery, not laundry lists** — the foundational tools you build on
   (e.g., semimartingale theory, FTAP/NFLVR, BSDE theory, convex duality, stochastic control)
   should be cited where they do work, not as decoration.
4. **Pre-empt the "special case" objection**: show your result is not a corollary of an
   existing theorem under a change of variables.
5. **Flag what you do NOT claim** — keeping scope honest is part of the rigor culture.

## Anti-patterns

- A standalone literature-review section detached from the contribution claim.
- Citing a result without its hypotheses, so the reader cannot judge your delta.
- Over-claiming generality the proof does not actually deliver.
- Ignoring a known counterexample or a sharper existing bound.
- Treating "no one has done exactly this" as novelty when the technique is routine.

## Output format

```
【Closest prior result】author/year + its assumptions + its limit
【Your delta】weaker-assumptions / broader-class / sharper / constructive / new-object
【Machinery you build on】[foundational tools, cited where they work]
【Special-case defense】why your result is not a corollary of prior work
【Scope honesty】what you explicitly do NOT claim
【Next step】mathfin-identification-strategy
```

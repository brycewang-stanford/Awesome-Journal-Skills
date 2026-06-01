---
name: mathfin-writing-style
description: Use when polishing a Mathematical Finance manuscript's theorem-first exposition: definitions, assumptions, theorem statements, proofs, appendices, numerical-experiment prose, and financial-modelling intuition.
---

# Writing Style (mathfin-writing-style)

## When to trigger

- The proofs are correct but the paper is hard to read
- The introduction states results without financial modelling intuition
- Definitions, assumptions, theorem numbering, or appendix references are inconsistent

## Style principles

- **Define before use.** Probability space, filtration, admissible strategies,
  integrability, market model, and payoff objects must be explicit.
- **Number assumptions and results.** Reuse labels consistently.
- **State theorem scope precisely.** Hypotheses and conclusions should be visible
  without searching prose.
- **Separate intuition from proof.** Give financial meaning before technical proof,
  then keep the proof self-contained.
- **Use appendices deliberately.** Put long derivations there while keeping the
  main text focused on result, intuition, and modelling payoff.

## Theorem paragraph pattern

```text
Under Assumptions (A1)-(A3), Theorem 2.1 establishes [formal result]. In financial
terms, this means [pricing/hedging/risk/portfolio interpretation]. The proof
combines [main tools] and is given in [location].
```

## Proof hygiene

- Check local martingale versus true martingale claims.
- State integrability and measurability conditions.
- Do not cite a theorem without verifying its hypotheses.
- Avoid "straightforward" for load-bearing steps.
- Keep notation stable across the main text and appendix.

## Output format

```text
[Section] intro / model / theorem / proof / numerics / appendix
[Main clarity issue] ...
[Formal precision fix] ...
[Financial intuition fix] ...
[Next step] mathfin-submission
```

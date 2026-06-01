---
name: jbes-writing-style
description: Use when polishing prose, theorem statements, the abstract, and the introduction for a Journal of Business & Economic Statistics (JBES) methods paper so the methodological contribution and its empirical relevance both land. Polishes exposition; it does not change theory or results.
---

# Writing Style (jbes-writing-style)

## When to trigger

- The prose buries the method, or the theorem statements are hard to parse
- The abstract leads with generic motivation instead of the methodological contribution
- The introduction reaches the method only after pages of setup
- Notation is overloaded and a reader cannot follow the conditions

## JBES house style: method-first, application-anchored

JBES is read by both econometricians and applied economists/statisticians, so the writing must make a **methodological contribution legible** while keeping its **empirical relevance** front and center. Unlike a general-economics journal (which leads with a finding) or a pure-statistics journal (which can lead with a theorem in the abstract), a JBES paper should pair the two: state what is methodologically new **and** why it matters for a real application, early and plainly. Theorem statements should be precise and self-contained; the heavy proofs belong in an appendix.

## The introduction arc (JBES template)

1. **The problem** — the empirical/statistical problem that motivates the method, in plain terms.
2. **Why existing methods fall short** — the gap (assumptions, robustness, computation) that blocks a clean answer.
3. **The contribution** — what the new method is and what it delivers (consistency / valid inference / feasibility).
4. **Evidence preview** — the Monte Carlo properties and the empirical application, in one breath.
5. **Relation to prior methods** — concise positioning, not a survey.
6. **Roadmap** — brief.

## Abstract and exposition

- Open with the methodological contribution and its empirical relevance; do not bury the method behind generic motivation.
- State theorems in words once before the formalism; define notation as you introduce it, not all at once.
- Quantify the gains ("controls size where method X over-rejects by 12 points") rather than vague claims.
- Verify the abstract length and required style on the live JBES instructions page — these specifics are 待核实.

## Checklist

- [ ] Abstract names the methodological contribution and its empirical relevance
- [ ] The method appears on page one, not after pages of setup
- [ ] Theorem statements are precise and self-contained; proofs in the appendix
- [ ] Notation introduced incrementally, not dumped
- [ ] Gains quantified against named incumbents
- [ ] Abstract length / citation style checked on the live instructions page (待核实)

## Anti-patterns

- An abstract of generic motivation that never states what is methodologically new
- Leading the intro with the application and never foregrounding the method (or vice versa)
- Theorems stated in dense notation with no plain-language gloss
- Notation overload that forces the reader to hold many symbols at once
- Vague "performs better" claims with no dimension or magnitude

## Output format

```
【Abstract verdict】contribution + relevance stated? [Y/N] — fix: ...
【Intro arc】problem / gap / contribution / evidence / positioning present? [Y/N each]
【Theorem clarity】precise + glossed + proofs in appendix? [Y/N]
【Notation】introduced incrementally? [Y/N]
【Style facts】abstract length + citation style verified live? [Y/N — 待核实]
【Next step】jbes-replication-and-data-policy
```

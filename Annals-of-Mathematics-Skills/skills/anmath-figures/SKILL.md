---
name: anmath-figures
description: Use when organizing the exposition and structure of a pure-mathematics manuscript for Annals of Mathematics — sectioning, notation, statements-before-proofs, commutative diagrams, and readability for an expert non-specialist. Figures are optional and rare; this skill is about exposition first. Does not assess the proof's correctness.
---

# Exposition and Structure (anmath-figures)

## When to trigger

- The paper is hard to follow even though the proof is correct
- Notation is inconsistent or introduced after first use
- Theorems and their proofs are interleaved confusingly
- A relation between objects would be far clearer as a commutative diagram
- You are deciding whether the rare case of an actual figure is warranted

> In pure mathematics, papers are theorem-and-proof and usually have **no experiments and
> few or no figures**. "Figures" here means *exposition and structure*: a figure or diagram
> is included only when it conveys structure more efficiently than prose.

## Exposition principles (Annals readability)

1. **Statements before proofs.** State each definition, lemma, proposition, and theorem in
   full before proving it. The reader should always know the target before the argument.
2. **Notation introduced once, used consistently.** Define every symbol at first use; keep
   a fixed convention throughout; avoid overloading the same symbol for two things.
3. **Logical sectioning.** Preliminaries → key constructions → main lemmas → proof of the
   Main Theorem → consequences. Each section has a clear job and a one-line opener.
4. **Self-contained where reasonable.** Recall the precise external statements you use so a
   reader need not reconstruct them from memory.
5. **Readable by an expert non-specialist.** Someone strong in an adjacent area should be
   able to follow the architecture; gloss the field-specific shorthand the first time.

## Sectioning template

| Section | Contents |
|---------|----------|
| Introduction | Problem, Main Theorem, what is new, method sketch, organization |
| Preliminaries / Notation | Conventions, recalled definitions, cited external results |
| Constructions / setup | The objects the proof manipulates |
| Key lemmas | The intermediate results, stated then proved |
| Proof of Main Theorem | Assembling the lemmas into the headline result |
| Consequences | Corollaries and remarks |
| Appendices | Auxiliary/technical material (see anmath-supplementary) |

## Numbering and cross-reference conventions

- Number theorem-like environments in one per-section sequence (Theorem 3.1,
  Lemma 3.2, Corollary 3.3) so a referee deep in a long verification can locate any
  statement from its number alone.
- Give the headline result a stable early label — Theorem 1.1, or letters
  (Theorem A, B, …) in a long paper — and use it everywhere.
- Number displayed equations only when referenced; an unnumbered-but-needed display
  forces "the equation above," which breaks silently under revision.
- Open each section with what it proves and what it consumes: "In this section we
  prove Proposition 3.1, using Lemma 2.4."

## Diagrams and figures (when justified)

- **Commutative diagrams**: use `tikz-cd` (or `amscd`) when a chain of maps or an exact
  sequence is clearer drawn than written. Keep arrows labeled and consistent.
- **A genuine figure** (a configuration, a region, a graph): include only when it removes
  real ambiguity. Use vector output (PDF/EPS), label everything, and reference it in text.
- **Tables**: occasionally useful for case enumerations or notation summaries; keep clean.
- Most Annals papers have zero figures — do not add one for decoration.

## Micro-example: when a diagram earns its place

Prose version: "The map φ factors through the quotient, and the induced map commutes
with the two projections of Section 2."

As a `tikz-cd` square with labeled arrows, the same content is checkable at a glance.
That is the admission test — the referee verifies commutativity faster from the
picture than from the sentence. A picture that merely restates a relation the prose
already makes precise is decoration.

## Checklist

- [ ] Every definition/lemma/proposition/theorem is stated before it is proved
- [ ] Numbering is one per-section sequence; the headline theorem has a stable label used everywhere
- [ ] Every symbol is defined at first use and used consistently
- [ ] Sections are logically ordered with clear one-line openers
- [ ] External results used are recalled precisely (statement + citation)
- [ ] Commutative diagrams (if any) are typeset with labeled, consistent arrows
- [ ] Any figure is vector, labeled, referenced, and genuinely necessary
- [ ] An expert in an adjacent area could follow the overall architecture

## Anti-patterns

- Using a symbol before defining it, or redefining a symbol mid-paper
- Interleaving proof fragments with statements so the target is unclear
- A wall of unsegmented text with no sectioning logic
- Adding a decorative figure that conveys nothing the prose does not
- Field jargon used without a single gloss for the adjacent-area reader
- Sloppy diagram arrows (unlabeled, inconsistent direction) that obscure the maps

## Output format

```
【Section plan】1 Intro · 2 Prelim · 3 ... · n Appendix
【Notation issues fixed】...
【Statements-before-proofs】compliant / fix: ...
【Diagrams】none / commutative diagram in §... via tikz-cd
【Figure justification】none needed / figure in §... because ...
【Next step】anmath-supplementary (appendix triage) or anmath-writing-style
```

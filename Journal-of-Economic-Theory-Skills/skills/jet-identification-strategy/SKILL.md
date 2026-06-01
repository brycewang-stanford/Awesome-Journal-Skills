---
name: jet-identification-strategy
description: The Journal of Economic Theory (JET) analogue of an identification strategy for a theorem-proof paper — make every assumption explicit and load-bearing, architect the proof so two expert referees can verify it, and defend the generality/tractability trade-off. For theory papers, "identification" means assumptions, results, and proof exposition, not a causal design.
---

# Assumptions, Results & Proof Architecture (jet-identification-strategy)

## When to trigger

- You have a candidate theorem and need to make its assumptions and proof referee-proof
- A referee may ask "is assumption X necessary?" or "does this hold in the general case?"
- You are choosing between a clean special case and a more general but opaque statement

## Why this replaces a causal "identification strategy"

JET is **theory-first**: there is no data design to identify. The credibility of a JET paper rests on
**assumptions that are explicit and minimal, results stated precisely, and proofs an expert can
check** — refereed single-blind by **at least two** reviewers who will verify each step.

## The theory checklist

### Assumptions
- [ ] Every assumption is **stated formally** (domain, regularity: continuity, convexity, single-crossing,
      finiteness) before it is used
- [ ] Each assumption is **load-bearing** — for each one, you can name the step that fails without it
- [ ] No **silent** assumption smuggled into a proof (a common referee catch)
- [ ] Necessity is addressed: a **counterexample** shows what breaks if a key assumption is dropped

### Results
- [ ] The main result is a **clean theorem/proposition/characterization**, numbered and self-contained
- [ ] Genericity, existence, uniqueness, and comparative statics are separated into distinct statements
- [ ] The statement says exactly what is proved — no informal "essentially" claims beyond the proof

### Proof exposition
- [ ] **Proof architecture is visible**: lemmas in dependency order, a one-paragraph roadmap for long proofs
- [ ] Key step (fixed point, duality, induction, envelope/revelation argument) is named and motivated
- [ ] Long/technical proofs moved to an appendix (`thm-restate` to restate); body keeps the idea
- [ ] Notation is consistent end-to-end (referees abandon proofs they cannot parse)

### Generality vs. tractability
- [ ] The chosen level of generality is **defended**: a transparent special case can beat an unverifiable
      general one; a general result is worth it only if the proof remains checkable
- [ ] Any restriction (finite types, two players) is flagged as a scope limit, not hidden

## Anti-patterns

- A "general" theorem whose proof silently needs finiteness or continuity
- Assumptions introduced inside a proof rather than stated up front
- A monolithic 6-page proof with no roadmap or lemma decomposition
- Claiming necessity of an assumption without a counterexample

## Output format

```
【Theorem】<precise statement>
【Assumptions】[A1 used at step __ | A2 used at __ | necessity of Ak: counterexample/general]
【Proof spine】lemmas in order → key argument named → appendix offload
【Generality call】special-case-clean | general-but-checkable | (reject) general-unverifiable
【Next】jet-contribution-framing / jet-tables-figures (schematic) / jet-rebuttal
```

---
name: jet-identification-strategy
description: Use when hardening the assumptions, results, and proof architecture of a Journal of Economic Theory (JET) paper — the theory analogue of an identification strategy. Make every assumption explicit and load-bearing, architect the proof so two expert referees can verify it, and defend the generality/tractability trade-off; for JET, "identification" means assumption sets and proof exposition, not a causal design.
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

## Assumption-set architecture (three tiers)

JET papers separate three tiers of premises; label them so referees see which is which:

- **Maintained structure** — the model itself (agents, type spaces, action sets, timing). Lives in
  the model section as prose and definitions, not as numbered assumptions.
- **Economic assumptions** — single-crossing, private values, independence, ambiguity attitudes,
  substitutability. Numbered A1, A2, …; each carries economic content and each earns a necessity
  discussion.
- **Technical regularity** — compactness, continuity, measurability. Numbered last; defensible as
  standard, but still say which proof step uses each one.

Referee heuristic: the first thing checked is whether the theorem statement quantifies over exactly
the numbered assumptions — nothing more, nothing less. A theorem invoking "the assumptions of
Section 2" without numbers invites a hostile read.

## Proof-spine scaffold

```text
Theorem 1 (statement quantified over A1–A3 only)
 ├─ Lemma 1: existence of the auxiliary object      [uses A1, A3 (compactness)]
 ├─ Lemma 2: monotonicity / single-crossing step    [uses A2]
 │    └─ Claim 2.1: boundary case                   [where A2 binds → necessity candidate]
 ├─ Main argument: fixed point / duality / induction (named in one body sentence)
 └─ Appendix B: full proofs of Lemmas 1–2; the body keeps the roadmap paragraph + key step
Example 1 (tightness): drop A2, hold everything else fixed → conclusion fails; cite it
right after Theorem 1, not in a footnote.
```

## Writing the tightness discussion JET-style

- Place the counterexample immediately after the theorem as a numbered **Example**, with one
  sentence saying which assumption it targets.
- Make it **minimal**: change exactly one assumption and keep the rest of the environment fixed,
  so the referee attributes the failure to the right premise.
- If no counterexample is available, state openly that necessity is an open question — JET
  referees respect a flagged open problem more than silence.

## Micro-vignette (decision theory)

A representation theorem for ambiguity-averse preferences: A1 (weak order, continuity) is
regularity; A2 (certainty independence) is the economic axiom. The proof's separation argument
fails exactly when A2 is weakened to independence on constants only; Example 1 exhibits a maxmin
preference violating the conclusion under the weakening. One page settles A2's tier, load-bearing
step, and necessity — the page both referees read first.

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

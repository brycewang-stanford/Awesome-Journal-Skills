---
name: icalp-writing-style
description: Use when shaping the exposition of an ICALP (EATCS) theory paper — stating the model before the theorem, putting a legible theorem statement and its improvement over prior bounds on the first page, structuring the 15-page body around the argument while full proofs live in the appendix/full version, and meeting the correctness-and-clarity bar of Track A and Track B referees.
---

# ICALP Writing Style

Build the ICALP skeleton: **model → theorem → improvement → technique → complete proof**. ICALP
referees are subject experts who will *check* the mathematics, so the writing has two jobs at once —
make the contribution **legible on the first page**, and make the proofs **verifiable** in the body,
appendix, and full version. The 15-page body is a hard budget; exposition, not omission, is how you
fit.

## The first-page arc

1. **State the model, then the theorem.** Fix the exact setting — the computational model, the
   complexity measure, the class of objects — *before* the claim. "Fully dynamic, deterministic,
   worst-case update time" comes before "n^{o(1)}."
2. **Put a legible theorem statement in the abstract.** A specialist should read the abstract and know
   what you proved and by how much, without opening the proof.
3. **Position against a named prior bound.** State the best previous result and your improvement in the
   same breath. "The best known bound was X; we give Y" is the ICALP sentence.
4. **Name the barrier and the technique.** Say what obstruction prior work hit and what idea gets past
   it. Referees reward a clearly identified new technique over an opaque win.
5. **Say where the proof lives.** The body may sketch; point explicitly to the appendix / full version
   where each claim is proved in full.

## Track-aware voice

- **Track A (Algorithms, Complexity, Games):** lead with the **bound**. The reader wants the running
  time / approximation ratio / complexity class and the comparison to prior work up front; the
  technique section then shows how.
- **Track B (Automata, Logic, Semantics):** lead with the **model and the exact question** — the
  fragment of logic, the class of automata, the calculus — and the **decidability/complexity/
  characterization** you establish. Definitional precision is itself part of the contribution.

## The 15-page discipline

- The body **sketches proofs and proves the key lemmas**; routine or long proofs go to the labelled
  appendix / full version. But the body must contain **enough that a referee can follow the argument**
  and locate every deferred step (`icalp-supplementary`).
- Recover space by **compression, not omission**: fold repetitive case analysis, state a general lemma
  once, cite standard tools rather than re-deriving them. Do not shrink margins or fonts — the LIPIcs
  style is fixed.
- A body padded to 15 pages with all proofs banished to an unread appendix is a **scored risk**:
  reviewers judge on the body and distrust a paper whose substance they cannot see.

## Theorems, definitions, and the proof contract

- **Every headline theorem has a complete proof** the referee can find — in the appendix if not the
  body. "Details omitted" with no full version is the classic ICALP soundness failure.
- **Definitions before use, notation minimal.** Introduce only the notation the proof needs; a wall of
  symbols on page 2 loses the reader before the theorem.
- **State lemmas so the proof structure is visible.** A reader should be able to reconstruct the
  dependency graph of lemmas from their statements.

## Upper and lower bounds together

ICALP prizes **tightness**. When you can, pair an algorithm with a matching (possibly conditional)
lower bound, or a decidability result with a complexity classification. A result that is provably
optimal in its parameter reads far stronger than an isolated upper bound — and it pre-empts the
referee's "is this tight?" question.

## Anti-patterns (theory-specific)

- **Benchmark framing.** "Fast on these instances" is experimental-algorithms voice; ICALP wants a
  provable bound (an `icalp-topic-selection` re-route signal if there is no theorem behind it).
- **Buried theorem.** A first page about how "important and active" the area is, with the actual
  statement on page 6.
- **Unpositioned improvement.** A bound with no comparison to the best known result — the referee
  cannot tell if it is progress.
- **Proof-by-intimidation.** Dense symbol-pushing that hides a gap; referees who cannot check a step
  treat it as unproved.
- **Over-signposted roadmap** substituting for a statement of the result.

## Self-check before drafting the body

```text
[Model] is the computational model / logical fragment fixed before the first theorem?
[Legibility] can a specialist state my result and its improvement from the abstract alone?
[Positioning] is the best prior bound named and my delta stated against it?
[Barrier] is the obstruction prior work hit, and my technique for evading it, identified?
[Proof contract] does every headline theorem have a complete proof the referee can find?
[Tightness] is there a matching lower bound / optimality statement where one is expected?
```

## Output format

```text
[Track] A / B — and the corresponding lead (bound vs model+question)
[First-page arc] model -> theorem -> improvement -> technique -> proof-location: all present? gaps?
[Page budget] body <=15pp excl. refs+appendix; compression targets
[Proof contract] theorems lacking a complete proof somewhere: <list>
[Tightness] matching lower bound present / justified absent
[Rewrite queue] <ordered edits to reach the ICALP bar>
```

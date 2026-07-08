---
name: oopsla-topic-selection
description: Use when judging whether a project is OOPSLA-shaped — a PL contribution whose evidence spans design, implementation, formalism, or empirical study — and routing within the SIGPLAN family from OOPSLA's seat: POPL for theory-first, PLDI for implementation-performance, ICFP for functional, Onward! for vision, ECOOP, or SE venues.
---

# OOPSLA Topic Selection

OOPSLA is the broadest seat at the SIGPLAN table: its published scope covers
programming languages "from design to implementation and from mathematical
formalisms to empirical studies," and its verified exemplars include a
benchmark suite, a measurement-methodology critique, a corpus/survey study,
a soundness counterexample, a language experience report, and a formalized
runtime mechanism (`resources/exemplars/library.md`). The routing question
is therefore rarely "is this PL?" but "is OOPSLA's *breadth* the asset, or
would a narrower sibling reward this paper's center of mass more?"

## The center-of-mass test

State the one sentence a reviewer would repeat to the committee. Route on
what that sentence *is about*:

| The sentence is about... | First-choice venue | OOPSLA case exists when... |
| --- | --- | --- |
| A metatheoretic result, calculus, logic | POPL | The formalism explains a deployed mechanism or design choice |
| Compiler/runtime performance engineering | PLDI | The insight is the design trade-off, not the speedup |
| Typed/functional language technique | ICFP | The audience is OO/imperative/multi-paradigm practice |
| A provocative vision without full evidence | Onward! (same SPLASH building) | Evidence has matured past position-paper strength |
| OO language design, European community | ECOOP (AITO, not PACMPL) | PACMPL journal publication or the SPLASH audience matters |
| Testing/analysis practice at SE scale | ISSTA / ICSE / FSE | The finding changes how *languages* are designed, not just tools |
| Human factors of programming | CHI or OOPSLA's human-aspects lane | The methodology meets study-design scrutiny (`oopsla-experiments`) |

## Signals the project is genuinely OOPSLA-shaped

- The contribution *couples* layers — a semantics plus its implementation
  consequences, a design plus the empirical study of its use — rather than
  living purely in one.
- The paper would still matter if a competing implementation shipped: the
  claim is about the design space, not the artifact's existence.
- Experience and applications carry analysis: OOPSLA has a real lane for
  "we built and deployed it; here is what generalizes" (the Julia paper is
  the model), which PLDI/POPL reward less.
- Empirical questions about programs and programmers at scale — adoption,
  API misuse, bug taxonomies — with instrument-grade methodology.

## Signals to route away

- The evaluation *is* the contribution and it's a speedup: PLDI's
  benchmark-first culture is the better courtroom.
- The theorem stands alone without an implementation story: POPL.
- The idea needs permission to be speculative: Onward!, and return to OOPSLA
  a volume later with evidence — a deliberate SPLASH-internal pipeline.
- The novelty is a product description: no SIGPLAN venue; consider an
  industry track or experience venue outside the family.

## Two-round consequence for routing

Because OOPSLA offers two doors a year with a revision system, it is often
the *fastest* family member from "solid evidence" to "published journal
article" — a legitimate tiebreaker when a paper fits two venues. It is a bad
reason to submit work whose center of mass is elsewhere: family reviewer
pools overlap heavily, and a misrouted paper burns goodwill you will meet
again (`oopsla-review-process`).

## Decision procedure

```text
1. Write the one-sentence claim; identify its center of mass (table above)
2. Check exemplar precedent: which library entry shape matches?  none → doubt
3. Ask the coupling question: does the paper bridge ≥2 layers?  no → sibling
4. Verify current scope text on the live track page (topics drift by volume)
5. Commit to a round (oopsla-workflow) or a re-route with a named venue
```

## Output format

```text
[Center of mass] <one sentence + layer(s) it lives in>
[Routing] OOPSLA / POPL / PLDI / ICFP / Onward! / ECOOP / SE venue / other
[Precedent] exemplar shape matched, or none
[Fit risk] the objection the committee would raise
[Commitment] target round or re-route action
```

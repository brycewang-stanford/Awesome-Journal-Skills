---
name: popl-topic-selection
description: Use when deciding whether a project is POPL-shaped — a principle about programming languages carried by definitions and theorems — or better aimed at PLDI's implementation bar, OOPSLA's breadth, ICFP's paradigm focus, or LICS, CAV, CPP, ESOP, and journal outlets, judged by what the decisive evidence is.
---

# POPL Topic Selection

POPL's full name is the routing test: *Principles* of Programming Languages. The
venue's center of gravity is a *general truth about languages* — a semantics, a type
discipline, a program logic, a proof technique — established by definition and
theorem. Both theoretical and experimental papers are welcome under the posted
scope, but an experimental POPL paper still orbits a principle. (Scope wording per
the POPL series pages, read 2026-07-08.)

## Three questions before committing

1. **What sentence do you most want reviewers to believe?** If it starts "we prove"
   or "we give a semantics/logic/type system such that ..." — POPL. If it starts
   "our compiler/analyzer achieves ..." — PLDI. If it starts "developers using our
   language ..." — OOPSLA.
2. **Could a skeptic check the claim without running anything?** POPL's decisive
   evidence is re-derivable: proofs, mechanizations, counterexample-freedom by
   construction. If the truth of your claim lives in measurements, route toward the
   implementation venues.
3. **Does the idea outlive your artifact?** POPL rewards machinery others can
   instantiate on their languages. A theorem inseparable from one codebase is a
   tool paper wearing a theorem.

## Routing table

| Project signature | Better venue | Reason |
|---|---|---|
| New program logic + soundness proof + small case studies | **POPL** | Principle first, evidence supporting |
| Compiler optimization with 1.4x speedups, proofs optional | PLDI | Benchmark-carried claim, implementor jury |
| Language design evaluated by user study or corpus mining | OOPSLA | Broader empirical evidence culture |
| Typed FP abstraction, elegant library, paradigm-native | ICFP | The functional-programming home crowd |
| Pure model/automata/logic result, thin language connection | LICS / CSL / FSCD | Logic-side siblings want it more |
| Decision procedure, model checker, solver improvement | CAV / TACAS | Verification-algorithm reviewers |
| Proof-engineering technique, assistant infrastructure | CPP / ITP | Mechanization-first audience (CPP co-locates with POPL) |
| Solid but regional-scale PL result, or needs journal length | ESOP / TOPLAS / JFP / LMCS | Right bar, right format |

All of POPL, PLDI, OOPSLA, and ICFP publish in PACMPL, so the archival venue is
identical — choose by **reviewer community and evidence shape**, never by deadline
proximity.

## POPL-fit smells, both directions

- *Good signs:* the abstract states a theorem; the motivating example breaks an
  existing system's metatheory; reviewers from three different PL subareas would
  each recognize the machinery.
- *Warning signs:* the "formal" section restates the implementation in Greek
  letters; the theorem is routine and the contribution is engineering; the paper
  needs performance numbers to matter.

```text
Fit test (fill honestly):
  Central claim: ..............................................
  Decisive evidence:      [ ] proof   [ ] mechanization   [ ] measurements   [ ] study
  Who must believe it:    [ ] semanticists  [ ] implementors  [ ] tool users
  Survives artifact deletion?  [ ] yes  [ ] no
  => POPL only if column one dominates and the answer is "yes".
```

## Output format

```text
[POPL fit] strong / plausible with reframing / route elsewhere
[Central claim] <the one-sentence version>
[Evidence shape] <proof / mechanization / empirical mix>
[Reframe path] <what to foreground if staying at POPL>
[Alternative] <venue + one-line reason, if routing away>
```

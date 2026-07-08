---
name: pldi-topic-selection
description: Use when deciding whether a project is PLDI-shaped — implementation insight with benchmark-grade evidence — or better routed inside the PACMPL family to POPL, OOPSLA, or ICFP, or outward to ASPLOS, CGO, CAV, ICSE/FSE, or a systems venue, based on where the claim's evidence actually lives.
---

# PLDI Topic Selection

PLDI's scope statement is broad — all aspects of programming language research:
design, implementation, theory, applications, performance (PLDI 2026 CFP) — but
its acceptance bar has a recognizable shape: **an idea about languages,
compilers, analyses, runtimes, or verification tooling whose truth is
demonstrated by a working implementation evaluated on convincing programs.** The
routing question is never "is this PL?"; it is "is the decisive evidence an
implementation-and-benchmarks story?"

## The fit test

Answer three questions honestly:

1. **Where does the claim's proof live?** In a theorem about a calculus → POPL
   lens. In measurements of a built system → PLDI lens. In how developers
   experience the language → OOPSLA lens.
2. **Who must be convinced?** People who build compilers and analyzers → PLDI.
   People who prove type soundness → POPL. People who study software at scale →
   ICSE/FSE.
3. **Would the paper survive with the implementation deleted?** If yes, the
   implementation is decoration and PLDI reviewers will say so.

## Routing table

| Signal in your project | Better home | Why |
|---|---|---|
| The theorem is the contribution; implementation is a demo | POPL | Semantics-first reviewing |
| Language design + experience/empirical study of use | OOPSLA | Broader evidence styles welcomed |
| Functional-programming technique, typed abstractions | ICFP | Paradigm-native audience |
| Wins depend on hardware features or memory hierarchy | ASPLOS / CGO / PPoPP | Architecture-facing evidence bar |
| The engine is a solver/model checker advance | CAV / TACAS | Verification-algorithms community |
| Claim is about developer behavior or SE process | ICSE / FSE | Human/process evidence expected |
| OS-level mechanism, scheduler, distributed runtime | OSDI / SOSP | Systems reviewing |
| Early idea, no evaluation yet | SIGPLAN workshops (co-located each June) | Feedback without the archival bar |

Note the family plumbing: POPL, OOPSLA, ICFP, and (since 2023) PLDI all publish
in PACMPL, so the choice among them changes reviewers and deadlines, not the
journal your paper lands in. Retargeting within the family is cheap
editorially — the CFP formats are all acmart — but expensive intellectually if
the evidence style does not move with it.

## PLDI-shaped in practice

The venue-verified exemplars in `resources/exemplars/library.md` triangulate the
bar: an automated testing engine on real C code (DART), instrumentation
infrastructure with its design space articulated (Valgrind), a multi-year
empirical campaign against production compilers (Csmith), a DSL whose compiler
proves a named trade-off space (Halide), and proof-engineering tooling with a
badged artifact (Sisyphus). Common denominator: **the system is the argument.**

## Decision procedure

```text
1. Write the one-sentence claim. Underline its verb.
2. If the verb is "we prove"          -> POPL unless benchmarks carry equal weight.
3. If the verb is "we measure/build"  -> PLDI candidate; check benchmark rigor is achievable by November.
4. If the verb is "we observe/design" -> OOPSLA/ICFP comparison first.
5. Confirm the June-audience test: would a PLDI hallway care?
6. Check the calendar: PLDI's single deadline (Nov) vs POPL (~Jul) vs OOPSLA rounds.
7. Commit; retrofit the framing to the chosen venue, never to two at once.
```

Deadline-driven routing — sending a POPL-shaped theory paper to PLDI because
November is closer — produces the characteristic "strong work, wrong evidence"
reject and burns a year.

## Output format

```text
[Fit] High / Medium / Low, one line
[Claim verb] prove / build / measure / design / observe
[Evidence home] theorem / implementation+benchmarks / study
[Family alternative] POPL / OOPSLA / ICFP, with the switch cost
[Outside routing] ASPLOS / CAV / ICSE / systems venue if applicable
[Calendar] next feasible deadline, from live pages (PLDI 2027: 待核实)
```

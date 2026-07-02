---
name: anmath-supplementary
description: Use when deciding what belongs in appendices versus the main text of a pure-mathematics manuscript for Annals of Mathematics — technical/auxiliary results, long computations, and machine-assisted computation. Math journals generally have no science-style "supplemental material"; everything essential stays in the main text.
---

# Appendices and Auxiliary Results (anmath-supplementary)

## When to trigger

- A long, self-contained computation interrupts the main line of argument
- You have auxiliary lemmas that are needed but not conceptually central
- The proof depends on a machine computation that must be documented
- You are tempted to "move detail to supplement" the way science papers do — pause first

> Important: pure-mathematics journals generally **do not** have a science-style
> "supplemental material" section. Everything **essential** to the proof stays in the main
> text and must be fully present and verifiable there. Appendices hold material that is
> necessary but would break the flow if kept inline.

## What belongs where

| Material | Placement |
|----------|-----------|
| The Main Theorem and its proof's logical skeleton | Main text, always |
| The crux / new idea | Main text, in full |
| Key lemmas used by the main argument | Main text (state and prove) |
| Long but routine computation verifying an estimate | Appendix, referenced from main text |
| Standard background lemmas recalled for completeness | Appendix or Preliminaries |
| Technical case analysis that would swamp the main flow | Appendix, with the conclusion stated in main text |
| Machine computation (code, what was checked) | Appendix + archived code/data |
| Anything a referee must check to believe the theorem | Main text — never hide it |

## Appendix discipline

- Each appendix is **self-contained and clearly scoped** ("Appendix A. Proof of the
  estimate in Lemma 3.4"). State in the main text exactly what the appendix establishes.
- The main text must **stand on its logic** with appendices referenced, not required to be
  read in parallel to follow the argument.
- Do not use an appendix to **hide a gap**: if a step is essential and hard, it stays
  visible. Appendices are for length relief, not for sweeping difficulty out of sight.

## When an appendix is not enough: the companion-paper option

If auxiliary material grows into a self-contained contribution — its own theorem and
proof, plausible independent use — a companion paper is the honest structure, not a
hundred-page appendix. The canonical precedent, verified in
`resources/exemplars/library.md`: Wiles's 1995 modularity paper ran alongside the
Taylor–Wiles companion in the same Annals issue, citing it for the input it needs.
The discipline carries over: state precisely what you import, and prove it fully where
it lives. A companion is a second refereed paper, never a place to park an unproved
step.

## Appendix mechanics

- Use letter appendices (Appendix A, B, …) with results numbered A.1, A.2, so
  main-text citations stay unambiguous.
- Each main-text use reads like an import: "By Proposition A.2 (proved in Appendix A),
  estimate (4.7) holds with C = C(n)" — so the reader can defer the appendix and still
  audit the logic.
- Order appendices by first citation from the main text, not by topic.
- A referee should be able to read all appendices last, in one pass; an appendix that
  must be consulted mid-argument belongs in the main text.

## Computer-assisted proofs

- If a result depends on machine computation, describe **precisely what was computed**, the
  software and version, and the exact claim verified.
- Make the **code and data available** (archive, repository, or supplement permitted by the
  journal) so a referee can reproduce or audit it.
- The human-readable argument must make clear **how** the computation closes the proof; the
  computation is evidence within a proof, not a substitute for exposition.

## Checklist

- [ ] Everything essential to the theorem is in the main text, not an appendix
- [ ] The crux/new idea is fully in the main text
- [ ] Each appendix is self-contained with a clear scope statement
- [ ] The main text states what each appendix establishes and references it
- [ ] No proof gap is concealed by relegation to an appendix
- [ ] Any machine computation is documented (software, version, exact claim)
- [ ] Code/data for computer-assisted steps are archived and citable

## Anti-patterns

- Treating an appendix as a science-style "supplement" and shipping essentials there
- Pushing the hard step to an appendix to make the main text look clean
- A machine computation with no description of what was actually checked
- Unavailable / unreproducible code behind a computer-assisted claim
- Appendices the reader *must* consult continuously just to follow the main argument
- An appendix that restates main-text material instead of carrying new detail

## Output format

```
【Stays in main text】Main Thm, crux, key lemmas: ...
【To appendix】App A: ...; App B: ...
【Reason each is appendix-not-main】length relief, not gap-hiding: ...
【Computer-assisted?】no / yes — software, version, what was checked, archive location
【Gap check】no essential step hidden / fix: ...
【Next step】anmath-writing-style
```

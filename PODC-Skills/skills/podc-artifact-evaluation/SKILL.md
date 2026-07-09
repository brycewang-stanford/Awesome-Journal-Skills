---
name: podc-artifact-evaluation
description: Use when an author expects an artifact-evaluation or badge track at ACM PODC and needs redirecting — PODC has NO artifact track and no ACM badges. This skill converts artifact-culture instincts into what PODC actually evaluates: proof-appendix completeness, model/assumption rigor, and the honest, optional role of any simulation.
---

# PODC Artifact Evaluation (there isn't one — read this)

If you arrived here expecting an Artifacts-Available / Functional / Reusable / Reproduced badge
process, stop: **PODC has no artifact-evaluation track and no ACM badge program.** It is a
proofs venue. The object that is "evaluated" is your **theorem and its proof**, and the honesty of
your **model and assumptions**. This skill redirects artifact energy into the three things that
actually decide a PODC paper's technical standing.

## Why PODC has no artifact track

A PODC contribution is a **model, a theorem, and a proof**, not a running system or a dataset. There
is nothing for evaluators to install and run to confirm the claim — the claim is confirmed by
**reading the proof**. Importing a badge workflow here is a category error: it would evaluate an
artifact that is, at most, an optional illustration. (Contrast this with software-engineering or
systems venues, where the artifact *is* part of the evidence.) Any simulation you ship is a
figure-generator, not proof of correctness (`podc-experiments`, `podc-reproducibility`).

## The three real "evaluations" at PODC

### 1. Proof-appendix completeness (the analogue of "Functional")

Just as an SE evaluator checks that an artifact runs, a PODC reviewer checks that the proof *closes*.
Make it pass:

```text
[ ] Every lemma the main theorem uses is stated and fully proved (or cited with the statement quoted)
[ ] No "it is easy to see" or "the remaining case is symmetric" hides a nontrivial step
[ ] Base cases of inductions/recursions are present
[ ] Named invariants are shown to hold initially and be preserved
[ ] The full version is self-contained: no proof depends on an external private note
```

### 2. Model/assumption rigor (the analogue of "Reusable")

An artifact is "Reusable" when others can build on it; a *model* is reusable when it is stated
precisely enough that others can prove new results in it and trust yours:

```text
[ ] The model box fixes network, timing, faults, adversary, randomness, and cost measure before any theorem
[ ] Every assumption the proofs consume is declared in the box (no assumption creep)
[ ] No proof silently strengthens synchrony or weakens the adversary mid-argument
[ ] Parameter regimes (ranges of n, t, diameter) are stated where results are conditional
[ ] Definitions match standard usage, or deviations are flagged explicitly
```

Run the assumption audit from `podc-experiments`; this is the single most common source of a PODC
soundness rejection.

### 3. Optional-simulation transparency (the analogue of "Available")

If — and only if — your paper includes a simulation, make it transparent, while remembering it
establishes nothing:

```text
[ ] Labeled as illustrative (a constant, a convergence rate, average-case behavior), not as verification
[ ] Parameters, ranges, number of trials, and random seeds reported
[ ] Environment pinned (language/version) in the full version or a linked bundle
[ ] Any repo/author-page link kept OUT of the anonymized submission (lightweight double-blind)
[ ] Added openly only in the camera-ready / arXiv full version
```

## Mapping artifact instincts to PODC actions

| Artifact-venue instinct | PODC equivalent |
|---|---|
| "Package the code so it runs on a clean machine" | Make the proof close for a reader with only the submission |
| "Document dependencies" | Declare every assumption in the model box |
| "Provide a claim -> script -> result mapping" | Provide a theorem -> lemma -> proof map with exact cross-refs |
| "Deposit in a DOI archive for Available" | Post the full version with all proofs to arXiv |
| "Reproduce the headline numbers" | Let a reader re-derive the bound from the stated model |

## What NOT to do

- Do not build a Dockerfile, a badge application, or an evaluator README expecting a PODC artifact
  track — there is none.
- Do not present a simulation as if it earned a "Reproduced" badge; PODC has no such badge and the
  proof is the evidence.
- Do not de-anonymize the submission by linking a simulation repository during review.
- Do not confuse PODC with software-engineering or systems venues (or with DISC's practice); the
  proofs-only evaluation model is the point.

## Output format

```text
[Reality check] confirmed: PODC has no artifact/badge track; the proof is what is evaluated
[Proof completeness] every lemma proved; no hidden steps; self-contained full version?
[Model rigor] model box complete; no assumption creep; regimes stated?
[Simulation] absent / illustrative-and-transparent (seeds/ranges), no de-anonymizing links?
[Fix queue] <proof gaps to close; assumptions to declare; simulation framing to correct>
```

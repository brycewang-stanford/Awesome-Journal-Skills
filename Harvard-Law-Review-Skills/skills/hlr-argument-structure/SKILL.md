---
name: hlr-argument-structure
description: Use when organizing the body of a Harvard Law Review (HLR) piece along the doctrine to theory to normative-prescription arc that legal scholarship rewards. Structures the argument and its internal logic; it does not forge the thesis (hlr-thesis-and-contribution) or format the citations (hlr-sources-and-bluebook).
---

# Argument Structure (hlr-argument-structure)

A flagship legal article does three things in order: **maps the doctrine**, **diagnoses the problem with
a theory or principle**, and **prescribes** what should change. This doctrine → theory → prescription arc
is the spine readers and student editors expect. This skill organizes the body so each Part does one job
and the prescription is earned by what precedes it.

## When to trigger

- The thesis is set but the body sprawls or repeats itself
- Readers lose the thread between the doctrinal Part and the argument
- The prescription appears without the diagnosis that should justify it
- You need to decide Part order and what each Part is responsible for

## The doctrine → theory → prescription arc

| Part | Job | Failure mode if skipped |
|------|-----|-------------------------|
| **I. Doctrine / landscape** | Lay out the law as it is, precisely and fairly, including the split or tension | A strawman the rest of the piece knocks down |
| **II. Diagnosis / theory** | Explain *why* the doctrine fails — the principle, value, or logic it betrays | An assertion that the law is "wrong" with no theory |
| **III. Prescription** | Argue for the fix and show it works on the hard cases | A reform proposal floating free of the diagnosis |
| **IV. Objections / scope** | Adjudicate the strongest counterargument and bound the claim | A reviewer's obvious objection left unanswered |

## Construction rules

1. **Each Part earns the next.** The prescription must follow from the diagnosis, which must follow from
   the doctrinal map. If you could move a Part without loss, the logic is loose.
2. **State the law fairly before you attack it.** Student editors and generalist readers distrust pieces
   that caricature current doctrine. The strongest version of the status quo makes your critique credible.
3. **Make the theory do work.** A normative principle is not décor — it must generate the prescription and
   resolve the hard cases the doctrine cannot.
4. **Pressure-test on the hard case.** Apply your prescription to the fact pattern that most threatens it;
   if it survives, the piece is strong; if it doesn't, narrow the claim (loop `hlr-thesis-and-contribution`).
5. **Adjudicate the single strongest objection**, not a row of weak ones. Name it, take it seriously, and
   show why the thesis holds (or where it must be qualified).

## Engaging the literature inside the argument

Engage prior scholarship **where it bears on the move**, not in a front-loaded lit-review dump. When you
diagnose, cite the works that framed the problem; when you prescribe, distinguish the nearest rival
proposals (the neighbors found in `hlr-preemption-check`). Footnotes carry most of this engagement.

## Checklist

- [ ] Body follows doctrine → theory → prescription, each Part with one job
- [ ] The status quo is stated in its strongest form before critique
- [ ] The theory generates the prescription (not bolted on)
- [ ] The prescription is tested on the hardest case
- [ ] The single strongest objection is named and adjudicated
- [ ] Scope conditions stated — where the claim does and does not reach
- [ ] Literature engaged at the point of the move, mostly via footnotes

## Anti-patterns

- A descriptive Part I that never becomes an argument (the "survey then opine" structure)
- Prescription with no diagnosis — "courts should do X" without showing why the current rule fails
- Strawmanning the doctrine so the critique lands on a position no one holds
- A wall of weak objections instead of the one that actually threatens the thesis
- Front-loaded literature review disconnected from the argument's moves

## Output format

```
【Arc】Part I doctrine → Part II theory/diagnosis → Part III prescription → Part IV objections/scope
【Each Part's job】one line each
【Hardest case】the fact pattern that tests the prescription
【Strongest objection】and how it is adjudicated
【Scope】where the claim reaches and where it stops
【Next】hlr-sources-and-bluebook → hlr-footnotes-and-cite-check
```

## Supplementary resources

- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — real HLR pieces whose doctrine→theory→prescription arcs to study
- [`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md) — how the arc is previewed in the introduction

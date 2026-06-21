---
name: smr-rebuttal
description: Use when responding to a Sociological Methods & Research (SMR) decision letter — drafting the point-by-point response and revision plan for properties, simulations, the empirical illustration, software, and exposition under SMR's verbatim-comment response format. Plans the response; does not run new analyses itself.
---

# SMR Rebuttal

Use this after a decision letter. SMR revisions are won by treating each reviewer point as a concrete,
auditable deliverable — at a methods journal, "we have clarified this" without a new derivation,
simulation cell, or exhibit rarely persuades.

## SMR's response format

SMR expects authors to **copy each reviewer comment verbatim and respond beneath it** (检索于 2026-06；
以官网为准). Build the response document accordingly:

- One block per comment: the **verbatim comment**, your **response**, and the **exact change** (section,
  table, equation, or line) that implements it.
- Group nothing silently — every comment gets its own visible block, even if the answer is "see our
  response to Reviewer 2, point 3."
- Keep a **changelog** at the top summarizing the major revisions so the editor sees the arc quickly.

## Classify each comment, then assign a deliverable

| Comment type | Deliverable that satisfies an SMR reviewer |
|---|---|
| "Property is asserted, not proved" | a derivation or a clearly labeled argument (`smr-derivation-and-properties`) |
| "Simulation is too narrow / strawman" | new DGP cells or competitors (`smr-simulation-studies`) |
| "Does the method matter in practice?" | strengthen or add the empirical illustration (`smr-empirical-illustration`) |
| "Can I run this?" | release/clean the package + reproducibility (`smr-software-and-reproducibility`) |
| "Unclear contribution / overclaim" | tighten the contribution sentence (`smr-method-contribution`, `smr-writing-style`) |
| "Already exists elsewhere" | a precedent response (`smr-literature-positioning`) — concede or differentiate |

Map every comment to one of these before writing; an answer with no concrete deliverable is the
response most likely to draw a second-round rejection.

## Handling the hard cases

- **Disagreement**: you may push back, but do it with evidence — a derivation, a simulation cell, or a
  citation — not assertion. Concede the framing even when you keep the conclusion.
- **A demanded analysis you think is wrong**: run it anyway and show *why* it does not change the
  conclusion; a refusal reads as evasion.
- **Precedent claims**: if the reviewer is right that the method exists, say so and re-scope the
  contribution honestly; if they are wrong, give the precise difference from the cited work.
- **Scope pushback ("this is an application")**: re-foreground the methodological takeaway and the
  travel beyond the example — the `smr-topic-selection` argument.

## Track the revision clock

- Note the deadline and whether it is a major or minor revision; request an extension early if a new
  simulation or derivation needs real time.
- Keep the revised manuscript fully **anonymized** for re-review and update the **availability
  statement** and **AI disclosure** if materials changed.

## Checklist

- [ ] Each reviewer comment appears verbatim with a response and the exact change beneath it.
- [ ] A top-of-document changelog summarizes the major revisions.
- [ ] Every comment is mapped to a concrete deliverable (derivation/sim cell/illustration/code/prose).
- [ ] Demanded analyses were run, even those expected to be null.
- [ ] Disagreements are backed by evidence, with framing conceded where fair.
- [ ] Precedent claims are conceded or differentiated precisely.
- [ ] The revised files remain anonymized; availability statement and AI disclosure updated.

## Anti-patterns

- **"We have clarified this"** with no new derivation, exhibit, or text pointer.
- **Silent grouping** of comments instead of the verbatim-block format.
- **Assertion over evidence** in disagreements.
- **Refusing a requested analysis** instead of running it and explaining the null.
- **Defending an overclaim** the reviewers correctly flagged, rather than re-scoping.
- **Deanonymized revision files** sent for re-review.

## Output format

```text
[Decision] reject / major / minor / conditional accept
[Response format] verbatim-block per comment? yes/no
[Comment ledger] <comment -> deliverable -> where implemented>
[Hardest point] <the comment most likely to sink the revision> + plan
[Anonymization/disclosure] revision anonymized; availability + AI updated? yes/no
[Next SMR skill] smr-submission (for the revised resubmission)
```

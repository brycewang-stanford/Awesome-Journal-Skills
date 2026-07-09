---
name: sensys-author-response
description: Use when writing a SenSys Response to Reviewers for a resubmission — treating the reviews as a required-changes contract, mapping each blocking concern to a specific change and the new measurement that closes it, staging the energy and testbed experiments a systems revision demands, and keeping the response anonymous and in the CFP's form.
---

# SenSys Author Response

The SenSys resubmission is a **contract**, not a rebuttal debate. Because the two-deadline model
lets a rejected paper return at the next deadline **only with a substantive revision and a
Response to Reviewers**, the response's job is to prove that each concern the reviewers raised
has been *closed in the revised paper* — most often with a new measurement, not an argument. A
response that argues instead of measures is the most common way a resubmission fails again.

## The response is a change-map

For every reviewer point, produce a row: the concern, the change you made, and where in the
revised paper it now lives. This is the artifact reviewers actually read.

```text
R2-a  "Energy claim not measured; datasheet current used."
      → Change: measured average draw with a shunt at 10 kHz across a full duty cycle.
      → Where:  §4.2 rewritten; Fig. 4 new power trace; Table 2 updated with measured energy.
      → Status: CLOSED with new measurement.

R1-c  "Ground truth for accuracy is unclear."
      → Change: documented the reference-instrument protocol and its own error.
      → Where:  App. A new; §4.3 now cites it.
      → Status: CLOSED.

R3-b  "Suggest testing at 100 nodes."
      → Change: added a 40-node run (largest testbed available); discussed scaling limit.
      → Where:  §4.4; limitation stated in §6.
      → Status: PARTIALLY addressed — scope noted honestly.
```

## Stage the experiments before you write

A systems revision usually needs **new data**, and energy/testbed measurements have lead time. As
soon as the reviews land, sort the blocking points (`sensys-review-process`) and schedule the
runs against the next deadline (`sensys-workflow`): a new deployment or harvesting campaign may
need weeks of wall-clock time you cannot compress. Write the response *around* results you will
actually have, not results you hope to have.

## Sort every point before you answer it

Not every reviewer comment earns the same response. Triage first, then spend the revision budget
where it changes the verdict.

| Point type | What it needs | Response move |
|---|---|---|
| **Blocking** (disbelieved claim) | New measurement on real hardware | Run it; row marked CLOSED with the figure/table |
| **Fixable gap** | A bench run or clearer figure | Address and point to the location |
| **Framing misread** | Rewriting, no new data | Clarify in the paper; note the change |
| **Wishlist** (out of scope) | A brief, honest scoping reply | Acknowledge; do not spend the budget here |

## Rules of the response

- **Close, do not argue.** Prefer "we measured X and updated Table 2" over "we believe the
  reviewer is mistaken." When a reviewer is genuinely wrong, show the measurement that settles it
  rather than asserting.
- **Be honest about partial closes.** A concern you cannot fully address (a 100-node ask you can
  only meet at 40) is closed *honestly* by doing what you can and stating the limit — not by
  silence or overclaiming.
- **Every promise appears in the paper.** Reviewers read the response against the revised PDF;
  a change described but not present is worse than not promising it.
- **Stay anonymous and in-form.** The response is part of a double-blind resubmission; do not
  de-anonymize, and keep to the length/format the CFP specifies (待核实 for the exact form).
- **Prioritize blocking over wishlist.** Spend your revision budget on the points that made the
  reviewers not believe the paper, not on cosmetic wishlist items.

## Tone

Professional and specific. Thank reviewers once, briefly, then get to the change-map. Avoid
defensiveness and avoid flattery; a SenSys committee is persuaded by measurements and honest
scoping, not by rhetoric.

## Before submitting the resubmission

```text
[ ] Every blocking concern has a row: concern → change → location → status.
[ ] Each "CLOSED" row's change is actually present in the revised PDF.
[ ] New measurements were run on real hardware, not asserted.
[ ] Partial closes are stated honestly with the scope limit named.
[ ] Response is anonymous and within the CFP's stated form/length.
[ ] The revised paper's abstract/intro reflect the strengthened evidence.
[ ] Blocking points prioritized over wishlist items in the revision budget.
```

## Output format

```text
[Map]      the change-map: each reviewer point → change → location → status
[New data] which blocking points required new measurement, and whether it exists yet
[Schedule] can the required runs finish before the next deadline? (link to workflow)
[Honesty]  partial closes named with their scope limits
[Open]     any concern still unclosed and the risk it carries into the next round
```

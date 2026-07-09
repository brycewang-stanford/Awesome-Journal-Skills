---
name: sensys-review-process
description: Use when interpreting SenSys's two-deadline, self-contained review model — what a first-deadline outcome means, that a reject may return at the second deadline only with a substantive revision and Response to Reviewers, how systems reviewers weigh energy and deployment evidence, and how to classify a notification before drafting a response.
---

# SenSys Review Process

SenSys does not run a single annual verdict. It runs **two submission deadlines per cycle, each
a self-contained review round**, and the connective tissue between them is a **resubmission
rule**: a paper rejected at one deadline may re-enter at the next **only with a substantive
revision and a "Response to Reviewers"** that maps each concern to a specific change. Reading
your notification correctly means knowing which move the process is offering you.

## The outcome space

| Outcome | What it means | Your move |
|---|---|---|
| **Accept** | The paper is in the edition the deadline feeds | `sensys-artifact-evaluation` + `sensys-camera-ready` |
| **Reject** | Not accepted at this deadline | Decide whether to **resubmit with revision** at the next deadline, or route elsewhere |
| **Resubmit with revision** (next deadline) | The path the two-deadline model offers, not an automatic invitation | Treat the reviews as the required-changes list; see `sensys-author-response` |

Note that whether a given cycle also offers an explicit **major-revision channel at
notification** (distinct from the first→second deadline resubmission) is **待核实** — read the
current CFP; do not assume a rebuttal or revision stage that the edition does not run.

## What SenSys reviewers weigh

SenSys reviewers are systems people who have built and deployed. They read for:

- **Is it built and measured?** Simulation-only or single-run results draw immediate skepticism.
- **Is the energy real?** Adjectives ("low-power") where a measurement belongs are flagged.
- **Is the ground truth honest?** Accuracy against an unstated or uncalibrated reference is a
  standard objection.
- **Is the baseline fair?** Cross-hardware or untuned comparisons undercut the headline.
- **Does the design understand its space?** Rejected alternatives and named limitations signal
  competence; their absence signals under-evaluation.

Knowing this lets you predict the review themes before they arrive and pre-empt them in the paper
(`sensys-experiments`, `sensys-writing-style`).

## Classifying a notification before you respond

```text
Read every review and sort each point:
  [Blocking]  a claim the reviewer does not believe without new measurement
  [Fixable]   a gap addressable by a bench run or a clearer figure
  [Framing]   a misread you can prevent with rewriting, no new data
  [Wishlist]  a nice-to-have outside the paper's scope

Then decide:
  Accept        → move to camera-ready + artifacts
  Resubmit      → is the blocking set closable by the next deadline given testbed time?
  Route away    → if the blocking set needs a redesign, a different venue may be faster
```

The decision to resubmit is a **calendar-and-testbed** decision as much as a scientific one: a
blocking reviewer objection that requires a new energy-harvesting deployment cannot be answered
in two weeks. `sensys-workflow` holds the backward schedule.

## Confidentiality and conduct

Reviews are confidential; do not circulate them or identify reviewers, and do not attempt to
de-anonymize. Concerns about a review's fairness or a conflict go to the chairs through the
process, not into the response text. The exact conduct and appeal wording for the cycle is
待核实 — read the current pages.

## Reviewer continuity across deadlines

Because a resubmission returns to the venue with its prior reviews attached, assume **some
continuity** of reviewer context between deadlines: the response-to-reviewers is read against
what was promised. This makes the response a **contract** (see `sensys-author-response`), not a
debate — every promised change must appear in the revised paper.

## Output format

```text
[Outcome]  accept / reject / resubmit-with-revision — as the notification states
[Blocking] the points that must be answered with new measurement, listed
[Feasible] can the blocking set close by the next deadline given testbed time? Y/N
[Path]     resubmit here / route elsewhere / proceed to camera-ready
[Open]     any process ambiguity (major-revision channel? appeal?) marked 待核实
```

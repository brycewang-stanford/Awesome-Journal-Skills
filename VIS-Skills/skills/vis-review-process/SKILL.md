---
name: vis-review-process
description: Use when reasoning about how an IEEE VIS full-paper submission is evaluated, covering the two-phase review that mirrors IEEE TVCG, the primary/secondary/external (and 2026 student) reviewer roles, the six-area routing through Area Paper Chairs, the conditional-accept second round, and how VIS's journal-integrated process differs from a single accept/reject conference and from CHI/CVPR.
---

# VIS Review Process

Model the pipeline before interpreting any single review. IEEE VIS's process is **journal-style**
because VIS full papers are **IEEE TVCG articles**, so a first-round outcome is rarely a plain
accept or reject — the pivotal decision is a **conditional accept** that sends the paper into a real
second round. The most consequential mental shift for authors arriving from a one-shot conference
is that VIS gives repairable papers a genuine revise-and-review cycle within the same edition.

## Process model

- Submission and review run on **PCS** under the **VGTC** society, with **author-optional
  double-blind** anonymity following the IEEE TVCG process.
- Each paper is routed by its **primary area** to one of the six areas and handled by that area's
  **Area Paper Chairs**; **Overall Paper Chairs** keep decisions consistent across areas.
- Each paper gets **at least three reviewers**: a **primary** and a **secondary** (both program
  committee members) plus at least one **external** expert. VIS 2026 adds an optional
  **student reviewer** the primary may invite — a fourth, developmental voice, not a replacement.
- Reviewers weigh scientific quality and novelty, potential impact, whether the evidence supports
  the claims, appropriateness of methodology, and the soundness of the research process. Approved
  reviews are archived as supplemental material in IEEE Xplore.

## The two-phase structure (the defining VIS mechanic)

```text
Phase 1: submission -> reviews -> reviewer discussion -> first-round decision
         decisions: Accept  |  Conditional Accept (revise)  |  Reject
Phase 2 (only for Conditional Accept): revised paper + summary of changes ->
         re-review by the SAME reviewers against the required changes ->
         final Accept / Reject
```

A **conditional accept** is not a soft accept — the second round is real, and only papers that
actually make the required changes are accepted. Treat it like a journal major-revision with a hard
window.

## Reading a first-round decision

| Decision | What it means | Author move |
|---|---|---|
| Accept | Contribution and evidence hold; minor polish only | Camera-ready + open materials; do not reopen scope |
| Conditional Accept | Repairable gaps: a missing study, an unclear encoding rationale, a needed baseline or condition | Treat as a journal R&R: make or explicitly justify declining every required change, evidenced |
| Reject | Structural: wrong contribution shape, unconvincing evaluation, thin novelty | Reframe or reroute (a sibling venue or TVCG journal track), do not lightly resubmit unchanged |

The strategic reading: design the first submission so its weakest point is **revisable in the
second round** (a study you can add, an ablation you can run, a design rationale you can articulate)
rather than **structural** (an evaluation you cannot redo in the revision window). The process
rewards papers whose gaps are fixable.

## How VIS differs from its siblings

- **vs. CHI:** CHI is a mandatory-anonymous, ACM-proceedings HCI venue with its own rebuttal +
  revise-and-resubmit; VIS publishes in the **TVCG journal**, routes by **six visualization areas**
  through Area Paper Chairs, and makes double-blind **optional**. Never assume a shared template
  (`acmart` vs VGTC) or calendar.
- **vs. CVPR:** CVPR is a single-decision, high-volume vision conference with a fixed rebuttal and
  no in-cycle revision round; VIS's **conditional-accept second round** and journal publication are
  the opposite model. A CVPR-style "one rebuttal, then final" mental model will mis-time your VIS
  revision effort.
- **vs. pre-2021 VIS:** VIS once ran three separate conferences (SciVis, InfoVis, VAST) with
  separate committees. Since 2021 there is **one** call, one review process, and the six-area
  model. Do not carry a track-specific assumption from an older edition.

## Who reads you

Expect a primary, a secondary, and an external reviewer matched to your area, possibly plus a
student reviewer. Visualization reviewers check whether the **visual encoding and interaction are
justified by task**, whether the **evaluation matches the contribution type** (a technique needs
different evidence than a design study or a perceptual experiment), and often open the **supplemental
video and code**. Vague design rationale or an evaluation mismatched to the claim gets caught, not
skimmed.

## Where author leverage actually exists

```text
[Before submission]  primary-area + keyword choice -> Area Chair + reviewer pool   (largest lever)
[First-round reviews] factual corrections, clarifying misreadings, pointing to evidence already present
[Conditional accept]  the strongest lever: a revised paper + summary-of-changes re-read by the
                      same reviewers against the required changes
[After reject]        no appeal; reroute to a sibling venue or the TVCG journal track
```

A response moves borderline papers when it corrects a misreading or supplies a study/analysis a
reviewer said was missing; it does not move papers by arguing taste. In the second round, a
**required change that is neither made nor explicitly justified as declined** is what turns a
conditional accept into a rejection.

## Reading a review packet

Weight reviews before answering. A review from the **primary** carries the most process weight and
frames the discussion; the **external** often supplies the deepest domain check. A review that
cites your figure and section numbers was read closely and will be re-read in the second round — its
author is your likely advocate if the revision delivers. Answer each reviewer on the axis they
raised (encoding rationale, evaluation, novelty, reproducibility), and treat the list of required
changes as the scored contract for phase two.

## Misreadings to avoid

- **Treating a conditional accept as a guaranteed accept** — the second read is real; budget the
  revision window like a deadline.
- **Treating the response as a debate** — the reviewer discussion decides; your revised paper, not
  your prose, carries the argument.
- **Assuming a CVPR-style single rebuttal** — VIS's revision round is a full re-review, not a
  one-shot reply.
- **Projecting a pre-unification track model** — one area-routed process, not three conferences.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / conditional accept / second round / accepted
[Decision category] accept / conditional accept / reject, with the criterion driving it
[Area routing] primary area + Area Chair; reviewer roles (primary/secondary/external/student)
[Criterion map] each review point -> novelty | impact | evidence | methodology | encoding rationale | reproducibility
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak (if double-blind) / unsupported new claims
```

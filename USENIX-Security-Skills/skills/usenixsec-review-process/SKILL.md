---
name: usenixsec-review-process
description: Use when reasoning about how a USENIX Security Symposium cycle actually decides — early-reject notifications, multi-round reviewing, the retirement of Major Revision in favor of shepherd-approval acceptances, resubmission restrictions between cycles, and what each notification email means for planning.
---

# USENIX Security Review Process

USENIX Security reviews in two annual cycles, each a self-contained pipeline from
registration to notification. The '26 cycle mechanics below were read from
usenix.org pages on 2026-07-08 (via search renderings; direct fetch 403'd), with
the '25 reviewing-model page as documented history. The '27 mechanics under chairs
Adam Doupé (Arizona State) and Andrei Sabelfeld (Chalmers) are only partially
posted — treat everything here as one venue-generation's snapshot.

## The cycle pipeline, with '26 dates as the worked example

| Stage | Cycle 1 ('26) | Cycle 2 ('26) | What is happening |
|---|---|---|---|
| Registration | Aug 19, 2025 | Jan 29, 2026 | HotCRP record frozen; bidding data set |
| Submission | Aug 26, 2025 | Feb 5, 2026 | Format/policy screening begins |
| Early reject | Oct 7, 2025 | Mar 17, 2026 | Bottom of the pool exits after first-round reads |
| Final notification | Dec 4, 2025 | May 14, 2026 | Accept / shepherd-approval / reject |
| Finals due | Jan 15, 2026 | Jun 11, 2026 | Shepherding + Phase-1 AE complete |

The '25 model (last fully published) shows the shape inside those windows: two
first-round reviews; online discussion; survivors gain two more reviews in round
two; authors respond; the committee discusses to a decision. Expect roughly that
structure until the current cycle's reviewing-model page says otherwise (待核实
for '27).

## The decision vocabulary changed — don't plan on 2025 rules

Through '25, USENIX Security ran an Accept / **Invited Major Revision** / Reject
scheme, where a major revision returned to the same reviewers in a later cycle.
**The '26 CFP retired major revisions.** The current outcomes:

- **Accept** — proceed to camera-ready and mandatory artifact-availability check.
- **Accepted on Shepherd Approval** — the committee wants the paper conditional on
  changes a two-week shepherding pass can hold: clarifications, explicit
  limitations, calibrated claims. Not a lane for new experiments.
- **Early reject / reject** — out of the cycle. Whether and when the work may
  return is governed by per-year resubmission restrictions; the '26 CFP delegated
  restrictions on its Cycle-2 rejects to the '27 chairs. **Always check the
  current restriction text before queuing a resubmission** — this is the venue's
  most frequently misremembered rule.

Strategic consequence: the paper must be finished at submission. The old
major-revision safety net — submit at 85% and repair through revision — no longer
exists; its replacement (shepherding) fixes prose, not evidence.

## What reviewers here weigh

Beyond ordinary top-venue novelty/rigor screens, this committee applies filters
that surprise authors from adjacent fields:

1. **Ethics adequacy is a gate, not a score.** Weak Ethical Considerations content
   can trigger required revisions mid-review or sink the paper regardless of
   technique (the ethics guidelines page is explicit that expectations bind).
2. **Threat-model realism.** An attack needing implausible attacker position, or a
   defense evaluated only against non-adaptive adversaries, loses reviewers who
   ask "who does this actually affect?"
3. **Openness posture.** Since the Open Science policy, a vague availability story
   is a review-visible weakness, not a post-acceptance detail.
4. **Measurement validity.** Vantage-point, time-window, and ground-truth
   skepticism is a house specialty.

## Reading each email

```text
Early reject      → 4 reviews were not spent on you; the pool's bottom tier.
                    Diagnose fit and framing, not just polish. Consider
                    usenixsec-topic-selection before re-targeting.
Reject (final)    → full reviews attached; mine them for the resubmission and
                    check the current cross-cycle restriction before re-queuing.
Shepherd approval → acceptance-in-waiting; scope the change list within 48h
                    (see usenixsec-author-response).
Accept            → the artifact clock is already running
                    (see usenixsec-camera-ready).
```

## Confidentiality and conduct

Submissions are confidential to the committee; reviewer identities are hidden;
contacting reviewers or attempting to identify them is out of bounds. Conflicts
declared at registration drive assignment — fabricating conflicts to dodge a
skeptical expert is chair-level misconduct at USENIX as elsewhere.

## Reverify each cycle

- The current reviewing-model description, response phase, and round structure.
- Decision categories and shepherding window ('27 待核实).
- Resubmission restrictions between cycles and across years.
- Early-reject and notification dates for the live cycle.

## Output format

```text
[Cycle position] stage now + next date that matters
[Decision model] outcomes in force this cycle (verified on: <date>)
[Exposure] ethics gate / threat-model realism / openness / measurement validity
[Plan] action per possible outcome, with resubmission-restriction check
```

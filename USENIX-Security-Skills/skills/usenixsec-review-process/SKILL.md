---
name: usenixsec-review-process
description: Use when reasoning about how a USENIX Security Symposium cycle actually decides — early-reject notifications, multi-round reviewing, the retirement of Major Revision in favor of shepherd-approval acceptances, resubmission restrictions between cycles, and what each notification email means for planning.
---

# USENIX Security Review Process

USENIX Security reviews in two annual cycles, each a self-contained pipeline from
registration to notification. The mechanics below are USENIX Security '27's, read
directly from the live '27 Call for Papers on 2026-11-24 (program co-chairs Adam
Doupé, Arizona State, and Andrei Sabelfeld, Chalmers), with the '25 reviewing-model
page as documented history — treat everything here as one venue-generation's
snapshot.

## The '27 cycle pipeline

| Stage | Cycle 1 ('27) | Cycle 2 ('27) | What is happening |
|---|---|---|---|
| Registration | Aug 18, 2026 | Jan 19, 2027 | Title, authors+ORCIDs, topics fixed; bidding data set |
| Submission | Aug 25, 2026 | Jan 26, 2027 | Format/policy screening begins |
| Artifacts final | Aug 28, 2026 | Jan 29, 2027 | 3-day grace ends; artifacts frozen |
| Early reject | Oct 6, 2026 | Mar 9, 2027 | Bottom of the pool exits after first-round reads |
| Rebuttal | Nov 5–12, 2026 | Apr 8–15, 2027 | Surviving papers answer reviews |
| Notification | Dec 3, 2026 | May 6, 2027 | Accept / shepherd-approval / reject |
| Shepherded approval | Dec 15, 2026 | May 18, 2027 | Shepherd signs off the agreed changes |
| Finals due | Jan 14, 2027 | Jun 3, 2027 | Camera-ready + Phase-1 AE availability verified |

The '25 model shows the shape inside those windows: two first-round reviews;
online discussion; survivors gain two more reviews in round two; authors respond;
the committee discusses to a decision. The '27 call confirms the rebuttal window but
does not restate the round structure.

## The decision vocabulary changed — don't plan on 2025 rules

Through '25, USENIX Security ran an Accept / **Invited Major Revision** / Reject
scheme, where a major revision returned to the same reviewers in a later cycle.
**The '26 CFP retired major revisions, and '27 keeps them retired.** The '27 outcomes:

- **Accept** — proceed to camera-ready and mandatory artifact-availability check.
- **Accepted on Shepherd Approval** — the committee wants the paper conditional on
  changes a short shepherding pass (about 12 days in '27) can hold: text changes,
  clarifications, explicit limitations. Not a lane for new experiments.
- **Early reject / reject** — out of the cycle. In '27, papers rejected from either
  '26 cycle may be submitted, but **a '27 Cycle-1 reject may not be submitted to '27
  Cycle 2**. Always check the current restriction text before queuing a
  resubmission — this is the venue's most frequently misremembered rule.

Strategic consequence: the paper must be finished at submission. The old
major-revision safety net — submit at 85% and repair through revision — no longer
exists; its replacement (shepherding) fixes prose, not evidence.

## What reviewers here weigh

Beyond ordinary top-venue novelty/rigor screens, this committee applies filters
that surprise authors from adjacent fields:

1. **Ethics adequacy is a gate, not a score.** In '27 the Ethics appendix is no
   longer mandatory but is strongly encouraged; reviewers evaluate every paper's
   ethics, may ask authors for more during review, and papers may be rejected on
   ethical grounds regardless of technique.
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
- Decision categories and shepherding window (confirmed for '27 on 2026-11-24).
- Resubmission restrictions between cycles and across years.
- Early-reject and notification dates for the live cycle.

## Output format

```text
[Cycle position] stage now + next date that matters
[Decision model] outcomes in force this cycle (verified on: <date>)
[Exposure] ethics gate / threat-model realism / openness / measurement validity
[Plan] action per possible outcome, with resubmission-restriction check
```

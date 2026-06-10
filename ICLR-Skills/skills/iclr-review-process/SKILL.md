---
name: iclr-review-process
description: Use when explaining or planning around the ICLR review process, including OpenReview public review, AC/SAC roles, reviewer questions, discussion, revisions, final recommendations, and ethics escalation. Use when deciding whether to reply publicly or privately, how a permanently visible review thread shapes strategy, when to upload an allowed revision, or when to escalate a defective review to the AC for the current cycle.
---

# ICLR Review Process

Use this to plan strategy around ICLR's OpenReview process. Reopen the current Reviewer Guide and
Author Guide before advising on timelines, visibility, or revision permissions.

## Process model

- Submissions are reviewed double-blind on OpenReview.
- Reviews evaluate contribution, correctness, empirical/theoretical support, clarity, and value to
  the ICLR community.
- Authors can respond in discussion; current-cycle rules determine whether and how revised PDFs or
  supplementary files may be uploaded.
- Reviewers may update their recommendations after discussion; ACs synthesize reviews, comments,
  and paper fit for the final decision.
- Some comments are public, while others can be restricted by audience. Visibility affects tone,
  specificity, and what should be escalated privately.
- Ethics or conduct concerns can move outside ordinary score negotiation.

## Author strategy

- Treat the AC as the decision reader. Help them see which objections are resolved and which remain.
- Do not chase every score. Resolve the few issues that change acceptability.
- Use revisions only when they clarify, correct, or support existing claims.
- Keep public comments short, factual, and civil; do not accuse reviewers publicly.
- Use official confidential paths for abusive reviews, severe review defects, conflicts, or suspected
  integrity issues.

## How public reviews change strategy

ICLR pioneered fully open review: submissions, reviews, scores, author responses, and final
decisions remain on OpenReview permanently, and community members may post comments. This visibility
changes the calculus at every stage.

| Visibility property | Strategic consequence | Failure mode it punishes |
| --- | --- | --- |
| Reviews are public forever | Reply as if future citers will read it | Defensive or rude rebuttals |
| Scores are visible | Address the objection behind the score, not the digit | Score-haggling that clutters the thread |
| Community can comment | A "this is just X" post can appear | Weak novelty framing left unguarded |
| Decisions are archived | The meta-review must match your final PDF | Quietly changing claims after acceptance |

## Worked vignette

A submission on an alignment objective gets two borderline reviews and one negative. Instead of
arguing all three, the authors identify the one concern the AC will weigh: whether the objective
generalizes beyond the tuned prompt set. They post a public reply with a held-out-prompt table and
upload an allowed revision. One reviewer's updated, still-public review raises the score, and the
AC's meta-review cites the resolved concern.

## Reviewer-pushback patterns

- "Reviewer is hostile in public." Stay factual; flag genuine abuse confidentially to the AC.
- "Revision not allowed yet." Check the current cycle's upload window before promising a new PDF.
- "Score did not move." A fixed score can still accept if the AC sees the core objection resolved.

## Output format

```text
[Stage] pre-review / reviews released / discussion / final recommendation / decision
[Decision reader] reviewer / AC / SAC / PC
[Best action] reply / revise / provide evidence / escalate / wait
[Visibility] public / restricted / confidential
[Rationale] <why this action fits ICLR process>
```


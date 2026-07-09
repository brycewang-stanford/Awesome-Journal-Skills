---
name: hpca-review-process
description: Use when reasoning about the HPCA review pipeline: the double-blind process, what a single combined rebuttal/revision window means, champion dynamics at the program-committee meeting, how to read each outcome, and how confidentiality and the preprint policy shape expectations.
---

# HPCA Review Process

Use this to set expectations about how HPCA reviews a paper and decides its fate.
Understanding the pipeline turns anxiety into a plan: you can predict what the
rebuttal/revision window is for and what each outcome signals.

## The pipeline

HPCA runs a **double-blind** review. After the late-July gate, papers are assigned to
program-committee reviewers, reviews are written through the autumn, and — in recent
cycles — authors get a **single combined rebuttal/revision window**: one period in
which you both respond to reviews and may revise the paper, rather than two separate
review rounds. Decisions follow a program-committee meeting; HPCA 2027's reported
notification is November 6, 2026 (待核实 the exact rebuttal window).

## What the single window means

Unlike venues with two review rounds, HPCA's combined window compresses "argue" and
"change the paper" into one effort. Plan for both at once:

- Reviewers see your response *and* a revised paper, so a claim you defend in prose
  should also be reflected in the revision.
- The window is short; the objection ledger and staging shelf (see
  `hpca-author-response` and `hpca-supplementary`) must be ready before it opens.

## Champion dynamics at the PC meeting

Architecture decisions are made by people in a room (or a call). A paper needs a
**champion** — a reviewer willing to argue for it — and its fate often turns on
whether the champion can answer the strongest objection. Write the rebuttal to arm
your champion with the room, not only to satisfy the skeptic.

| Outcome | Likely meaning | Your move |
|---|---|---|
| Accept | The champion held; objections were addressable | Camera-ready + artifact evaluation |
| Reject with strong reviews | A fixable but unaddressed methodology or novelty gap | Fix, then retarget MICRO/ISCA/ASPLOS |
| Reject with weak/split reviews | No champion emerged, or scope mismatch | Reframe the contribution, re-route |
| Borderline / conditional | The room was divided | Read every review for the deciding objection |

## Read reviews for the deciding objection

Not all objections weigh equally. Identify the one that decides the paper — usually a
methodology or novelty concern the champion must overcome — and prioritize it over
easy-to-fix surface comments. A rebuttal that answers three minor points and dodges
the deciding one loses.

## Confidentiality and preprints

Reviews and PC discussion are confidential; do not solicit or reveal reviewer
identities, and do not de-anonymize yourself mid-cycle. Recent HPCA guidance asks PC
members not to penalize arXiv/CAL preprints, so a preprint is allowed — but posting
one that reveals authorship does not change the double-blind obligation on the
submission itself.

## Expectation-setting pass

```text
[Stage] assigned / reviews out / window / PC decision / notified
[Window plan] response + revision both staged? (Y/N)
[Deciding objection] <the one that decides the paper>
[Champion arming] does the rebuttal give the champion the room? (Y/N)
[Outcome branches] accept / reject-strong / reject-split -> next action
```

## Output format

```text
[Pipeline position] <where the paper is>
[Rebuttal/revision window] <dates from the current CFP, or unknown>
[Priority objection] <one>
[Outcome-conditional plan] <accept / reject branches>
```

Reopen the current CFP for the exact review calendar and window dates — the pipeline
timing is per-edition and was unconfirmed for 2027 at pack time.

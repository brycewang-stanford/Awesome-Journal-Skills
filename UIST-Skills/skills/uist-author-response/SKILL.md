---
name: uist-author-response
description: Use when writing the UIST rebuttal — budgeting the 5,000-character self-contained response, prioritizing factual corrections and novelty defenses over taste disputes, promising only camera-ready changes you can deliver, and writing for the PC discussion that follows rather than for the reviewers alone.
---

# UIST Author Response

The UIST rebuttal is small, plain-text, and consequential: 5,000 characters,
self-contained, written in about a week (May 28 - June 5 in the verified 2026
cycle), and explicitly listed among the inputs to the accept/reject recommendation.
Its second life matters more than its first: because acceptances are conditional on
"changes described in the rebuttal," this document becomes the **contract for your
camera-ready**. Draft it as both an argument and a promise you must keep by July 24.

## Budgeting 5,000 characters

That is roughly 700-800 words — three to five points argued well. Spend by expected
value, not by emotional temperature:

| Priority | Point type | Why it pays |
|---|---|---|
| 1 | Factual error in a review | Cheap to correct, moves discussion immediately |
| 2 | Novelty challenge ("X does this") | A capability-delta answer can flip a score |
| 3 | Direct reviewer questions | Unanswered questions read as concessions |
| 4 | Evidence gap where evidence exists | Report the number; it was measured, not new |
| 5 | Scope concession | Narrowing a claim can defuse a rejection rationale |
| — | Taste disagreements | Skip; acknowledge in one clause if at all |

Self-contained means the committee should not need to re-open the paper to follow
your point — quote the review's phrase, state the fact, cite section and figure by
number.

## Structure that survives skimming

The PC meeting skims. Number everything and front-load the verdict of each point:

```text
We thank the reviewers. We address the main concerns within the limit.

[R1-novelty] R1 notes SystemX "achieves the same interaction." SystemX
localizes touch at 4 discrete sites (their Sec 5); ours is continuous 2D
(±2.1 mm, Sec 6.2, Fig 7). We will add this comparison to Table 2.

[R2-latency] R2 asks for end-to-end latency. Measured: 11.3 ms median,
18.9 ms p95 over 10k events (harness in supplement). We will surface this
in Sec 6.1, currently appendix-only.

[R1,R3-study scope] We agree the 12-person study supports only the
large-effect comparison; we will narrow the claim in Sec 7 accordingly.
```

Conventions: tag each point with reviewer + topic; state fact before promise; make
every promise concrete and located ("add to Table 2"), because vague promises are
uncheckable conditions and specific ones become your camera-ready checklist.

## A point, done badly and well

Same objection, two treatments — the difference is fact-density per character:

```text
BAD (defensive, 490 chars, no facts):
We respectfully disagree with R2's characterization of our latency. The
reviewer may have overlooked the appendix, where this was discussed. Our
system is highly optimized and latency was never an issue in practice, as
any user of the system can confirm. We believe this concern does not
affect the contribution of the paper, which R1 and R3 both appreciated.

GOOD (factual, 330 chars, promise included):
[R2-latency] Measured end-to-end: 11.3 ms median, 18.9 ms p95 over 10k
events (App. C, harness in supplement). This is below the 20 ms
perceptibility threshold R2 cites. We will move the measurement from
App. C into Sec 6.1 and state the boundary conditions there.
```

The bad version spends characters on feelings and reviewer psychology; the good
version spends them on numbers, locations, and one checkable promise.

## Working the window

The 2026 window was eight days (May 28 - June 5). A schedule that survives it:

- **Day 1:** all authors read all reviews cold, separately; bins assigned
  independently, then merged — solo triage under-weights whichever reviewer
  annoyed the lead author.
- **Days 2-3:** hunt existing evidence for every evidence-gap point (logs, pilot
  data, appendix numbers reviewers missed); draft the promise ledger.
- **Days 4-5:** full draft, over budget; cut to 5,000 characters by deleting
  points, not by compressing sentences into unreadability.
- **Day 6:** cold read by a non-author; tone and self-containedness check.
- **Day 7:** submit. Never the final day — the window does not extend.

## What a rebuttal cannot do

- **No new experiments as argument.** Reporting an existing measurement reviewers
  missed is fair; describing studies you would run is a promise reviewers are told
  to discount.
- **No links, no attachments.** Self-contained plain text; a URL is both a rule
  violation and an anonymity hazard.
- **No hostility, no meta-complaints** about reviewer quality — the discussion
  phase that follows is among exactly those people, and your tone is data about
  what you'd be like as a colleague in a small single-track community.

## Deciding whether to rebut at all

Rebuttal is optional. Skip it only when reviews are uniformly positive with no
questions, or uniformly negative on grounds that are true. Anything mixed gets a
response: the 2026 process wording makes the rebuttal part of the record the PC
discusses, and silence leaves reviewer errors standing as facts.

## The promise ledger

Before submitting, extract every "we will..." into a ledger with a cost estimate.
The +10% camera-ready allowance (one page standard / half page short in 2026) is
the hard budget for delivering them:

```text
PROMISE                          COST      FITS +10%?
Comparison row for SystemX       3 lines   yes
Latency table to Sec 6.1         0.2 pp    yes
Narrowed claim in Sec 7          rewrite   yes
"Additional participants"        weeks     NO — do not promise
```

Over-promising creates a conditional acceptance you cannot satisfy; under-promising
leaves reviewer concerns unaddressed. Promise exactly what fits.

## Output format

```text
[Rebuttal plan] <points in order, each: reviewer-tag, fact, promise>
[Character budget] <estimated / 5000>
[Skipped points] <taste/unwinnable items deliberately dropped>
[Promise ledger] <each promise + cost + fits-allowance verdict>
[Tone check] performed by <non-author reader>
```

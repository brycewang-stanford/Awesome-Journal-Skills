---
name: siggraph-author-response
description: Use when writing the SIGGRAPH / SIGGRAPH Asia Technical Papers rebuttal, the single 1000-word text-only author response uploaded during the rebuttal window to correct factual errors and answer specific reviewer questions before the Technical Papers Committee meeting, and when planning the change list for a conditionally accepted paper's second-stage revision.
---

# SIGGRAPH Author Response

SIGGRAPH gives you exactly one written turn before the decision — the **rebuttal** — and, if the
paper is conditionally accepted, a second-stage revision handled through the camera-ready. These
are different instruments; do not treat the rebuttal like a journal response letter. Facts below
were read from the SIGGRAPH 2026 reviewer-instructions/ethics page on 2026-07-09
(`resources/official-source-map.md`); reconfirm the length and window on the live call.

## The rebuttal: a hard 1000-word, text-only turn

- **Length:** up to **1000 words of text only** — **no images, no video, no URLs to external
  pages**. Everything you say must be self-contained in prose. (SIGGRAPH 2026 window: 5-12 March
  2026; upload before 22:00 UTC/GMT on the close date.)
- **Timing:** you see the *complete set* of reviews when the window opens; the rebuttal is read by
  the referees and factored into the Technical Papers Committee discussion that produces the
  decision.
- **Purpose (narrow):** correct **factual errors** in the reviews and answer **specific
  questions**. It is *not* a channel for new results, revised text, or a redesigned evaluation that
  does not directly answer a reviewer's question. Promising a new experiment rarely moves a score;
  correcting a reviewer's factual misreading can.

## Triage the reviews before writing a word

1. **Separate factual errors from judgments.** "The method cannot handle X" when your Section 4
   shows X is a factual error you can flip; "the contribution is incremental" is a judgment you can
   only reframe. Spend words where they change a number.
2. **Find the pivotal reviewer.** With a small committee and a single score scale (Strong
   Reject ... Strong Accept), the borderline reviewer whose vote decides the paper is your
   audience. Answer the objection that is actually holding the score down, not the easiest one.
3. **Cluster shared concerns.** If two reviewers doubt the same comparison, answer it once, well,
   and cross-reference — you cannot afford to repeat yourself inside 1000 words.
4. **Concede cheaply, defend precisely.** Acknowledge real limitations in one clause and move on;
   spend the saved words on the one or two objections that decide acceptance.

## What actually persuades a graphics committee

- **Point to evidence already in the submission.** "Fig. 7 (row 3) and the supplemental video at
  0:45 already show the failure case the reviewer asks for" beats "we will add this." You cannot
  attach new media, but you *can* direct referees to what you submitted.
- **Quantify a correction.** If a reviewer misread a timing, state the correct number and where it
  appears. Numbers close factual gaps that adjectives cannot.
- **Name the comparison honestly.** If a reviewer wants a baseline you did not run, say whether it
  is applicable, what it would likely show, and why your existing comparisons already bound the
  claim — do not bluff a result.
- **Protect the results video.** Many graphics rejections turn on artifacts a reviewer saw in
  motion. If the criticism is about a visual artifact, address the specific shot and timestamp; if
  it is a genuine limitation, say so and scope the claim.

## Draft structure (fits 1000 words)

```text
[Opening 1-2 sentences] Thank reviewers; state the 2-3 decisions your response will address.
[R-common] The shared concern (e.g., missing comparison / validation), answered once with evidence.
[R1 / R2 / R3 specific] Only the factual errors and specific questions that affect the score.
[Limitations] One honest paragraph: what you concede and how you will scope claims in revision.
[Close] One sentence on the concrete change the camera-ready will make if conditionally accepted.
```

## The second stage: conditional acceptance is a revision, not a formality

If the committee **conditionally accepts** the paper, a Technical Papers Committee member verifies
the final version in a **second reviewing process** — required changes must actually be made. Treat
the conditions as a checklist:

- Map each required change to a specific edit, figure, or added result and track it.
- Deliver every promised revision; the second-stage reviewer can withhold final acceptance if
  conditions are unmet.
- Keep the supplemental video and code in sync with the revised claims — a fixed artifact must be
  re-rendered, not just described.

See `siggraph-camera-ready` for the mechanics of the conditionally-accepted final version.

## Anti-patterns

- Spending words re-explaining the method instead of answering the objection.
- Promising experiments you cannot run, or implying media you cannot attach.
- Arguing with a judgment ("this *is* novel") rather than supplying the missing fact.
- Ignoring the pivotal reviewer to score easy points off a lenient one.
- Exceeding 1000 words or embedding a link/figure — mechanically stripped or penalized.

## Output format

```text
[Rebuttal plan] pivotal reviewer + the 2-3 decisions to address
[Factual corrections] <review claim -> correct fact -> where it already appears>
[Concessions] <limitation conceded -> how claims will be scoped>
[Word budget] running count against 1000, text-only confirmed
[If conditionally accepted] <required change -> planned edit -> owner>
```

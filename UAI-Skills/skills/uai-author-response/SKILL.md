---
name: uai-author-response
description: Use when drafting UAI author responses during the OpenReview rebuttal window, turning reviewer objections about technical correctness, novelty, evidential backing, or clarity into anonymous, evidence-anchored replies that survive the reviewer-and-area-chair discussion phase that follows immediately after authors go quiet.
---

# UAI Author Response

Use this once reviews land. In the 2026 cycle the author response and discussion period
ran April 23 – May 2, and the reviewers' discussion with area chairs followed on
May 2 – 8 — meaning your reply is debated in a room you have already left. Write for
that second room. Reconfirm the current cycle's response mechanics on the UAI pages and
in the OpenReview forum instructions before drafting; formats change year to year.

## The four axes, and what each objection is really about

UAI's posted review criteria are technical correctness, novelty, convincing backing of
claims, and clarity of writing. Map every reviewer point onto one axis before answering;
a reply that answers the wrong axis reads as evasion.

| Reviewer says | Axis it lives on | Reply move that works at UAI |
|---|---|---|
| "The proof of Prop. 2 assumes faithfulness implicitly" | Correctness | Quote the appendix line where the assumption is invoked, or concede and show which results stand without it |
| "This is a variant of [known algorithm]" | Novelty | State the precise technical delta — objective, identification condition, or complexity — not adjectives |
| "Gains could be noise; only one run is shown" | Backing | Point to the seed-replicated table in the appendix, or concede the missing variance honestly |
| "Notation switches between p(x) and P(X) mid-paper" | Clarity | Commit to a specific fix, listed section by section |
| "Why no comparison against exact inference on small graphs?" | Backing | Give the appendix result if it exists; otherwise explain the computational or scope reason in two sentences |

## Anchoring discipline

- Every factual sentence in the response should point at something already submitted:
  a numbered equation, an appendix section, a table, or the supplementary ZIP.
- Never introduce a brand-new theorem or a fresh experimental campaign as if it were in
  the paper. You may sketch what a revision would add, clearly labeled as a revision
  promise.
- Stay anonymous. The double-blind rules do not expire at review release; institution
  hints, grant references, and identifying links remain forbidden in responses.
- Do not paste external URLs into the forum unless the current cycle's instructions
  explicitly allow them — assume they do not until verified.

## A skeleton that survives the AC discussion

The area chair will compress your response into one line of meta-review. Hand them that
line. A reliable shape for each reviewer:

```text
R2, on the identifiability concern (their point 1, our Thm. 3):
1. The concern is correct as stated for arbitrary DAGs.
2. Thm. 3 is scoped to ancestral graphs — Assumption A2, restated in App. B.1.
3. Under A2 the counterexample in the review is excluded (App. B.1, Lemma 5).
4. Camera-ready commitment: we will restate A2 in the main text beside Thm. 3.
```

Numbered, scoped, verifiable, and ending in a concrete commitment. Four lines like this
outperform four paragraphs of context-setting.

## Reading the review set before writing

- Identify the pivotal reviewer: usually the one whose objection, if upheld in the
  May discussion, decides the paper — not the one with the lowest score.
- Separate misreadings (fix by pointing at the record) from disagreements (fix by
  argument) from true gaps (fix by concession plus scoped promise). Each gets a
  different rhetorical mode, and mixing them within one answer muddies all three.
- Check whether reviewers already answered each other — one review praising the exact
  aspect another attacks is material you can quote neutrally.
- Note each reviewer's stated requests for clarification; the 2026 reviewer
  instructions explicitly asked them to articulate these, so unanswered explicit
  requests read as evasion.

## Prioritization under a short window

- Sort objections by decision weight, not by reviewer irritation. A correctness doubt
  from a low-confidence reviewer still outranks a style complaint from a hostile one.
- If two reviewers disagree with each other (one wants more theory, one wants more
  benchmarks), say so explicitly and state the trade-off you chose — area chairs reward
  authors who surface the tension instead of pandering to both.
- Concede real weaknesses in plain words. At a venue whose reviewer pool lives on
  calibrated uncertainty, hedged non-answers ("we believe this is not a major issue")
  are read as miscalibration about your own paper.
- Budget the window: draft everything by the midpoint, then spend the second half
  cutting. Responses shrink well and never grow well.

## Working the ten-day window

A schedule that has held up in practice for a short response period like 2026's
April 23 – May 2:

- **Days 1–2** — read all reviews twice; the first read is for emotion disposal, the
  second for the axis map. Assign each objection an owner and an anchor.
- **Days 3–5** — draft every reply in full. Where an anchor is missing, decide now
  between honest concession and a scoped camera-ready promise.
- **Day 6** — external pass: a colleague who has not seen the reviews reads only your
  responses and guesses the objections. Where they guess wrong, the reply is unclear.
- **Days 7–8** — cut by a third. Merge overlapping answers to different reviewers into
  consistent wording; ACs notice contradictions between per-reviewer replies.
- **Day 9** — post. Late responses compete with reviewer fatigue, and the
  reviewer–AC discussion opens immediately after the window closes.
- **Day 10** — buffer you should not need. If you are using it, cut more, not less.

## Pre-send checklist

- [ ] Every reply opens with the objection restated in one neutral line.
- [ ] Every factual sentence carries an anchor to submitted material.
- [ ] No new theorems, no new experiments presented as if already in the paper.
- [ ] No links (unless the current instructions explicitly permit them).
- [ ] No identity signals — institution, grant, "as we showed in [3]" phrasing.
- [ ] Each reviewer can locate their answer without reading the others' sections.
- [ ] Commitments are specific enough to be checked at camera-ready.

## What not to do

- Do not re-litigate novelty by listing how hard the work was.
- Do not answer a mathematical objection with an empirical table, or vice versa, without
  saying why the substitution is valid.
- Do not address the area chair over the reviewers' heads unless a review contains a
  factual error you can prove from the submission.
- Do not exceed whatever length or formatting cap the current forum enforces — check the
  live instructions, not last year's.

## Output format

```text
[Objection] <one-line restatement in the reviewer's own terms>
[Axis] correctness / novelty / backing / clarity
[Anchor] <equation, theorem, table, appendix, or ZIP path already submitted>
[Reply draft] <numbered, anonymous, ≤6 lines>
[Commitment] <camera-ready change offered, or "none needed" with reason>
```

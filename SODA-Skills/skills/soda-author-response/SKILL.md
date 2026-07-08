---
name: soda-author-response
description: Use when drafting the SODA (ACM-SIAM Symposium on Discrete Algorithms) rebuttal — the roughly three-day window between review release in early September and the response deadline, triaging referee misreadings versus real gaps, and writing terse theorem-anchored replies inside HotCRP without breaking lightweight double-blind rules.
---

# SODA Author Response

SODA runs a short rebuttal, and short is the operative word. For the 2027 cycle,
initial reviews reach authors by **September 1, 2026** and responses are due
**September 4, 2026** (checked 2026-07-08 via the SIAM SODA27 submission page,
read through search rendering). SODA 2026's rebuttal phase opened September 8,
2025, in a record-submission year — the window is a house institution now, not an
experiment, but its exact dates, length caps, and mechanics are reset per cycle
(caps for 2027: 待核实 on the HotCRP response form when it opens).

## What three days buys — and what it cannot

A SODA response is not a negotiation channel. It exists so the PC can distinguish
"the referee missed Lemma 4.2" from "Lemma 4.2 is actually broken" before the
October decision meeting. Budget accordingly:

| Review problem | Response leverage | Play |
|---|---|---|
| Referee misread a definition or bound | High | Quote the exact line and page; one sentence of correction |
| Referee missed a proof in the back matter | High | Point to the section; the full version was submitted, so it is on record |
| "Improvement too incremental" | Low-medium | One paragraph: name the barrier the prior bound sat at and who tried |
| "Why not compare to [paper]?" | Medium | State the relationship in two sentences; concede if the comparison is due |
| Genuine bug found by the referee | Honest disclosure only | Say whether it is patchable; a false "easily fixed" burns the community's memory |
| Taste objection ("not exciting") | Near zero | Skip it; spend words where facts decide |

## Preparation happens in August

Three days is enough to assemble a response only if the material already exists.
Between the July submission and September 1:

- Keep a **claims ledger**: every theorem, its exact statement, and the page where
  each ingredient is proved. Misreading corrections then take minutes, not hours.
- Pre-draft the two paragraphs you can predict: the significance defense (which
  prior bound, which barrier) and the closest-related-paper comparison.
- Ensure all coauthors are reachable in the September 1-4 window across time
  zones. A rebuttal blocked on a sleeping coauthor is a self-inflicted loss.

## Writing discipline

- **Numbered points, referee by referee.** PC members skim; a wall of prose loses
  the one correction that mattered.
- **Anchor every reply to a line in the submitted PDF.** "See Section 5.3,
  Lemma 5.7, page 31" is the strongest sentence a theory rebuttal can contain.
- **No new theorems.** A result proved after the deadline is not part of the
  submission; at most, note that a referee's suggested extension appears to follow
  and will be included in the full version.
- **Stay anonymous.** The lightweight double-blind rules still apply: no names, no
  "in our previous paper," no links to identifiable repositories.
- **Concede cleanly.** One honest "the referee is right; the fix is X and costs a
  constant factor" earns more trust than three defensive paragraphs.

## Response skeleton

```text
We thank the referees. We address the substantive points.

Reviewer A
A1 (main theorem "only" improves the exponent): The previous bound of
   O(n^{3/2}) [Ref 12] stood since 2015 and was stated as an open problem
   in [Ref 3]. Our O(n^{4/3}) crosses the barrier identified in [Ref 12, §6].
A2 (correctness of Lemma 4.2): The referee reads d as the maximum degree;
   it is the average degree (defined p.7, l.4). The claimed counterexample
   has average degree 3 and satisfies the lemma.

Reviewer B
B1 (missing comparison to [X]): [X] solves the unweighted case; our
   Section 2.1 reduction does not preserve weights. We will state this
   explicitly in Section 1.
B2 (typo in recurrence, p.19): Correct; the exponent should read k-1.
   The solution of the recurrence and all downstream bounds are unchanged.
```

## The 72-hour schedule that actually works

Multi-author rebuttals fail on coordination, not content. A schedule that has
survived real September windows:

| Hour (from review release) | Action | Owner |
|---|---|---|
| 0-4 | Full read; classify each point F/L/S/C (`soda-review-process`) | Lead author |
| 4-12 | Claims-ledger lookups for every F and C point | Whole group, split by section |
| 12-24 | First draft, worst review first | Lead author |
| 24-36 | Technical check of every page/lemma reference against the submitted PDF | The coauthor who did blind proof-checking |
| 36-48 | Tone pass: cut defensiveness, cut anything answering an S point at length | Most senior author |
| 48-60 | Freeze; sleep on it | — |
| 60-70 | Final read against the length cap and anonymity rules; submit | Lead author |
| 70-72 | Buffer for HotCRP form surprises | Lead author |

Two structural rules: the person who verifies references must not be the person
who wrote the draft, and the submission happens hours before the deadline, not
minutes — the response form's mechanics (length caps, formatting) are 待核实
until the form opens, and surprises cost exactly the buffer you kept.

## After the response

There is no discussion phase with referees. Decisions and final-version
instructions arrive from the PC in October (2027 cycle). If the outcome is
rejection, fold the reviews into the resubmission plan — the natural next
deadlines from a September/October SODA rejection are ITCS (if the contribution is
conceptual), STOC in early November if the fixes are fast, or ESA/ICALP in the
new year (`soda-workflow` has the calendar).

## Output format

```text
[Response plan] <points to answer, points to skip, concessions>
[Evidence anchors] <PDF page/lemma reference for each reply>
[Risk flags] <any reply that adds unproved claims or breaks anonymity>
[Coauthor sign-off] <who reviews the draft before the September deadline>
```

---
name: percom-author-response
description: Use when drafting an IEEE PerCom rebuttal after being invited following the initial reviews, covering the bounded single-round reply that answers explicit reviewer questions, corrects misreadings, points to evidence already in the paper without promising new experiments, and preserves double-blindness.
---

# PerCom Author Response

Use this after PerCom reviews are released **and you have been invited to submit a rebuttal**.
PerCom's rebuttal is a **single, bounded turn**: it answers the reviewers' explicit questions,
resolves misunderstandings, and clarifies — and the call states that **new experiments are not
expected**. There is no journal-style revision that follows, so the rebuttal must win with the
paper you already submitted. It remains **double-blind**: reveal no author, institution, testbed,
or dataset-owner identity.

## First: did you clear the early-rejection gate?

Papers with no positive review are **early-rejected** before the rebuttal opens — there is no
rebuttal to write for those. If you were invited, at least one reviewer sees a path to publication:
your job is to give that advocate the answers they need for the TPC discussion, and to neutralize
the specific doubts of the others.

## Triage

- Answer what affects the decision: significance of the contribution, soundness of the method,
  **cross-subject / deployment evaluation**, appropriate metrics (F1 vs. pooled accuracy), and
  clarity.
- Use evidence **that already exists in the submitted paper or dataset** — a table, a figure, an
  appendix result the reviewer overlooked. Do not promise a new experiment; the process does not
  expect or reward one, and you cannot add it.
- Correct factual misreadings first; a reviewer who misread which split produced a number is often
  persuadable with a pointer.
- Keep every word anonymous — do not name your testbed, deployment site, institution, or a
  non-anonymized dataset, even to strengthen a point.

## Structure the bounded reply

Group by reviewer, lead each item with the reviewer's own question, and answer with a pointer into
the existing paper:

```text
[R1.Q1] "Is the eating-recognition result cross-subject or within-subject?"
        -> Table 2 already reports leave-one-subject-out F1 (0.xx, 95% CI ...); the pooled number
           in the abstract is secondary. We will make this ordering explicit in §4.1.
[R2.Q1] "The baseline seems untuned."
        -> The baseline used the same feature budget and a grid search reported in Appendix A;
           we point R2 to Table A1 and will surface it in the body.
[R3.Q1] "How does it behave under confounding non-eating activities?"
        -> Table 4 already measures false positives against typing/brushing; we clarify the caption.
```

The rule that wins a bounded rebuttal: **every explicit question gets a direct, located answer.** A
question left unaddressed is what the discussion punishes, because there is no later round to fix it.

## Reviewer pushback patterns

| Pushback | What it signals | PerCom-ready response |
|---|---|---|
| "Evaluation is within-subject" | The core ubicomp doubt | Point to your leave-one-subject-out table; if you truly lack it, this is likely fatal — do not fake it |
| "Accuracy is inflated by class imbalance" | Metric-choice doubt | Point to reported F1 / event-level metrics and the class balance; clarify which metric is headline |
| "The baseline is not fair/tuned" | Soundness doubt | Point to the equal-budget tuning already in the paper/appendix; clarify placement |
| "Does this generalize beyond your subjects?" | External-validity limit | Point to the diversity of subjects and the stated limitation; do not overclaim |
| "The dataset/system is not available" | Open-data gap | Point to the (anonymized) release plan; describe what will be public post-acceptance |
| "Contribution overlaps prior work X" | Novelty doubt | Sharpen the delta in words; point to the comparison already present |

## Anonymity in the rebuttal (easy to slip)

- Refer to your own prior work in the third person, as in the paper.
- Describe the dataset/testbed without naming the site, building, or repository owner; use the
  anonymized location.
- Do not thank a named collaborator, funder, or institution inside the reply.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- The rebuttal length limit and format vary by cycle; confirm the current instructions and stay
  inside the limit — over-length rebuttals read as unfocused.
- The TPC discussion decides; write the reply as ammunition for your advocate, and let the *paper*
  — not the rebuttal — carry the argument.

## Output format

```text
[Gate] invited to rebuttal? yes/no (if no: reroute, do not draft)
[Priority question] <reviewer's explicit question>
[Decision dimension] significance / soundness / cross-subject evaluation / metrics / clarity
[Located answer] <question -> pointer to existing table/figure/appendix; clarification to add>
[No-new-experiment check] <every answer grounded in submitted material? yes/no>
[Anonymity check] <no identity leak in the reply: passed/issues>
```

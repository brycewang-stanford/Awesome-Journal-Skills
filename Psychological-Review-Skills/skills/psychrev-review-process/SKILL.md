---
name: psychrev-review-process
description: Use when anticipating how a Psychological Review manuscript will be evaluated — masked peer review, the kinds of decisions, article types (full article vs. Theoretical Note), and what reviewers at a theory journal actually probe. Explains the process; it does NOT write the response document (that is psychrev-rebuttal) or run the submission preflight (psychrev-submission).
---

# Understanding the Review Process (psychrev-review-process)

## When to trigger

- Before submitting, to understand what you are walking into
- A decision letter has arrived and you must read it correctly before responding
- You are unsure whether your piece is a full article or a Theoretical Note
- You want to anticipate the theory-specific objections reviewers will raise

## How Psychological Review is reviewed

- **Masked (anonymous) peer review.** Manuscripts are fully anonymized so the body carries no
  author-identifying content; the title page (authors, affiliations, ORCID, contact) is separate.
  (Verify current masking policy on the author page; 检索于 2026-06；以官网为准.)
- Handled through **Editorial Manager** (editorialmanager.com/rev, 检索于 2026-06；以官网为准).
- Reviewers are drawn from the **modeling/theory tradition** you enter — typically proponents or
  critics of the rival models you must beat. Positioning honestly (`psychrev-literature-positioning`)
  matters precisely because the rivals' authors may review you.
- The editor (currently **Elena L. Grigorenko, PhD**, editor since 2022; web-verified 2026-06-22, re-verify before relying) makes the call,
  weighing whether the theoretical contribution is genuine and general.

## Article types (confirm current list on the author page)

- **Theoretical articles** — the main vehicle: a new theory/model, a formal account, or a major
  synthesis that yields new theory. No upper length bound, but texts over **15,000 words** must be
  justified (检索于 2026-06；以官网为准).
- **Theoretical Notes** — shorter commentaries that advance a subfield: critiques of a theoretical
  approach, discussions of published work, or meta-theoretical argument. Pick this type when your
  contribution is a focused theoretical point, not a full new model.
- **Replications** are publishable only when relevant to / embedded in new or enhanced theory, and
  should be mentioned in the abstract (检索于 2026-06；以官网为准).

## What reviewers at a theory journal actually probe

| Reviewer question                                   | Where you should have answered it          |
|-----------------------------------------------------|--------------------------------------------|
| Is this theory or a disguised empirical paper?      | `psychrev-topic-selection`                 |
| Which standing models does it beat, and fairly?     | `psychrev-literature-positioning`          |
| Are the assumptions explicit and the mechanism real?| `psychrev-theory-construction`             |
| Do the predictions *follow*, and could they be wrong?| `psychrev-argument-development`            |
| Is the model identifiable; does a rival mimic it?    | `psychrev-boundary-conditions`             |
| Is the advance new, or a relabel / better fit?       | `psychrev-contribution-framing`            |
| For computational models: is the code available?     | `psychrev-submission`                      |

## Decision types (typical scholarly-journal ladder; confirm specifics)

- **Reject** (often desk-level for empirical papers or insufficient theoretical advance)
- **Major revision** — the common "promising" outcome; the bar rises across rounds
- **Minor revision** — rare on a first decision for a theory paper
- **Accept** — usually only after one or more revision rounds

Multiple rounds are normal at a theory journal; treat a major revision as an invitation to
strengthen the theory itself, not merely to answer comments.

## Checklist

- [ ] Manuscript fully anonymized for masked review; separate title page prepared
- [ ] Correct article type chosen (full theoretical article vs. Theoretical Note)
- [ ] Anticipated reviewer objections mapped to the skill that should have addressed them
- [ ] If computational: model code prepared for sharing (see `psychrev-submission`)
- [ ] Decision letter (if any) read for the *theoretical* asks, not just surface edits

## Anti-patterns

- Assuming a single round; the bar rises as the theory is pushed harder
- Treating reviewers as outsiders — they are often the rival modelers themselves
- Choosing a full article when the contribution is really a Theoretical Note (or vice versa)
- Reading a major revision as a list of edits rather than a mandate to strengthen the theory
- Leaving identifiability or rival-mimicry unaddressed and hoping reviewers miss it

## Output format

```
【Review model】masked; Editorial Manager; reviewers from the rival tradition
【Article type】theoretical article | Theoretical Note (+ length justification if > limit)
【Anticipated objections】[objection → skill that addresses it] (table)
【Decision read】[if letter present: the theoretical asks beneath the comments]
【Next step】psychrev-submission (preflight) or psychrev-rebuttal (after a revise decision)
```

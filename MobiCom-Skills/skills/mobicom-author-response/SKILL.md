---
name: mobicom-author-response
description: Use when writing a MobiCom rebuttal after round-two reviews or executing a one-shot revision — triaging reviewer points by severity, fitting a factual, concession-honest rebuttal into its length limit, and turning a required-changes list into a change-highlighted revision with a change summary that the same reviewers can verify.
---

# MobiCom Author Response

MobiCom gives authors two distinct response instruments, and they are not the same job. The
**rebuttal** is a short, bounded reply after round-2 reviews. The **one-shot revision** is a
months-long contract against a required-changes list. Using rebuttal tactics on a revision,
or revision ambition in a rebuttal, wastes both.

## Triage first, for either instrument

Read all reviews once for facts, then sort every point:

| Class | Definition | Response posture |
|---|---|---|
| Factual error | reviewer misread the paper | correct crisply, cite the section/figure |
| Answerable question | a real gap you can address in the space/time | answer with the specific evidence |
| Valid weakness | a fair criticism you cannot fully fix now | concede honestly; state what you will/can do |
| Scope disagreement | reviewer wanted a different paper | acknowledge; defend the chosen scope briefly |

The same reviewers usually carry the paper forward (`mobicom-review-process`), so credibility
compounds — a fair concession is worth more than winning every argument.

## Writing the rebuttal

The rebuttal is short and lands on a fixed clock; its exact length/format is 待核实 for the
current cycle, so read the instructions and budget to them.

```text
Rebuttal structure (fit to the length limit):
  1. Open with the 1-2 issues that most affect the decision — not point R1.1.
  2. Correct factual misreadings with a section/figure pointer.
  3. Answer the highest-severity questions with concrete evidence (a number, a
     condition), not a promise to "consider it."
  4. Concede real weaknesses plainly; say what is fixable and what is out of scope.
  5. Do not introduce a new contribution or new claims the reviewers cannot check.
```

Rules that keep a rebuttal from backfiring:

- **No new unverifiable claims.** A rebuttal is not a place to add an experiment the
  reviewers cannot see; it invites distrust.
- **Answer, do not deflect.** "We will address this in the final version" is a non-answer to
  a substantive question.
- **Promises become obligations.** Anything you commit to is the revision/camera-ready
  checklist — do not promise what you cannot measure.

## Executing the one-shot revision

A one-shot revision is a **contract**: reviewers list required changes; you return the paper
against that list, re-reviewed by the same reviewers where possible.

```text
Revision packet:
  - change-highlighted PDF (edits visibly marked)
  - change summary mapping EACH required item -> the visible change that addresses it
  - the revised paper within the same 12-page double-column cap
```

- **Map every required item to a visible change.** A revision that silently skips an item, or
  argues it away without addressing it, is the fastest path to a terminal reject.
- **Re-run in the requested condition.** If a reviewer asked for a mobility or interference
  experiment, adding a different experiment does not discharge the item.
- **Cost it before committing.** Size the demanded experiments in testbed-weeks against the
  revision deadline (`mobicom-workflow`); a revision that arrives incomplete is worse than
  one that was planned realistically.

## Consistency across the arc

Your rebuttal, revision, and camera-ready are read as one record by continuing reviewers.
Contradicting an earlier response — walking back a conceded weakness, or dropping a promised
experiment — is a memorable red flag. Keep a running log of every commitment made.

## Output format

```text
[Instrument] rebuttal / one-shot revision
[Triage] points classified: factual / question / weakness / scope
[Rebuttal] lead issues chosen; concessions listed; new-claim check passed
[Revision] required-items -> change map; conditions re-run as asked
[Commitments] running list that becomes the next-stage checklist
```

---
name: emnlp-author-response
description: Use when drafting an EMNLP author response in the ACL Rolling Review discussion window — triaging replies by soundness versus excitement, deciding what evidence can be added mid-review, staying anonymous, and writing for the area chair's meta-review and the post-commitment Senior Area Chairs, not the reviewers alone.
---

# EMNLP Author Response

Use this when ARR reviews land. In the May 2026 cycle the author response and
author-reviewer discussion ran July 7-13, with meta-reviews released July 30 and EMNLP
commitment due August 2 — a pipeline where the response is written once but read three
times: by reviewers who may update, by the AC composing the meta-review, and by the
conference SACs who see the whole record after commitment. Confirm the current window
mechanics on the live ARR pages before drafting.

## Triage by score axis

Sort every reviewer point by which score it threatens:

- **Soundness attacks** ("the baseline is mistuned", "no significance test", "the
  claim exceeds the tested languages") — answer with evidence or a scope concession.
  These are the points that move outcomes, because soundness anchors publishability.
- **Excitement discounts** ("incremental", "unsurprising") — answerable only by
  reframing what the finding changes for the field, briefly, once. Arguing taste at
  length reads as not having evidence.
- **Misreadings** — correct with a quote and a section number, tone-free. A factual
  correction the AC can verify in ten seconds is your highest-value paragraph.

## What can and cannot be added

The response box takes text and, in ARR practice, a revised PDF may accompany a
resubmission rather than a same-cycle response — do not build the plan around uploading
new material unless the current cycle's instructions explicitly allow it. Within text:

| Addition | Safe? | Why |
|---|---|---|
| Numbers from runs completed during the window | Usually | Reviewers can weigh them; label as new |
| A significance test on already-reported results | Yes | It re-analyzes existing evidence |
| A promised camera-ready rewrite | Yes, if scoped | Commit to wording, not to new experiments |
| A brand-new experimental direction | No | Unreviewable in-window; save it for revise-and-resubmit |
| Links to external results pages | No | Anonymity and auditability both break |

## Anatomy of a reply that moves a meta-review

```text
R2.1 (baseline tuning, soundness): Correct that §5.2 did not state the search budget.
Both systems received identical 32-trial random search over the grid in App. C; we
will state this in §5.2. Under matched budgets the gap is 2.1 F1 (±0.4 over 5 seeds,
paired bootstrap p=0.003, already in Table 3).

R2.4 (only high-resource languages, scope): We agree and will retitle the claim to
the six tested languages. We note Swahili and Tamil results in App. E show the same
direction at lower magnitude — we will surface this in §7 rather than claim
generality we did not test.
```

The pattern: number every reply to a numbered concern; concede early where the
reviewer is right; convert each concession into a specific, checkable edit; anchor
every number to a location in the submitted record.

## EMNLP-typical objections and their strongest answers

- **"Results may reflect data contamination."** Point to the contamination audit
  (overlap statistics, cutoff dates) in the submission. If none exists, run the overlap
  analysis during the window and report it — this objection does not age away.
- **"No error analysis."** If the paper has one, the reviewer missed it — cite the
  section. If it doesn't, a compact categorization of 50-100 sampled failures, added as
  in-window text, is feasible and persuasive.
- **"Human evaluation lacks detail."** Report annotator count, guidelines location,
  agreement statistic, and pay — items the Responsible NLP checklist already made you
  record.
- **"Why not compare against <system>?"** Either the comparison exists under another
  name (say so), or explain the confound that makes it uninformative, or run it if the
  window permits. "Out of scope" without a reason is read as "we would lose."

## When reviewers contradict each other

Three-reviewer packets regularly split: R1 wants more languages, R3 thinks the language
set is already too broad for the method's claims. Do not answer each in isolation — the
AC will read both replies side by side and see you agreeing with everyone. Instead:

- Name the disagreement once, neutrally: "R1 and R3 read the language coverage in
  opposite directions."
- State your position with its evidence, and accept the cost with the other reviewer
  explicitly.
- Give the AC the synthesis you want the meta-review to adopt — resolving reviewer
  conflict is the AC's job, and a response that does the work credibly usually gets
  adopted wholesale.

A special case is the score-text mismatch: a review whose text is mild but whose
overall recommendation is harsh (or vice versa). Respond to the text — it is the only
part you can engage — and let the mismatch itself be visible to the AC without
commenting on it.

## Deciding not to fight

Some packets should not be argued with. If all three reviewers converge on a missing
piece of evidence that cannot be produced in the window — a new annotation effort, a
second domain, a human study — the strongest move is a short, gracious response that
corrects factual errors only, followed by revise-and-resubmit into a later cycle where
the same reviewers will see the gap actually closed. A maximal rebuttal that concedes
nothing, against a unanimous packet, damages the record that the SACs will later read
at commitment time.

## Discussion-window conduct

- Reply early; a July 7 response can get a reviewer follow-up, a July 12 response
  cannot.
- Keep the whole response skimmable — ACs in a 17,000-submission cycle read dozens of
  these; a one-screen summary block on top ("three concerns, three fixes") earns
  goodwill.
- Stay anonymous end to end: no identity hints, no "as our prior work" phrasing, no
  personal repositories.
- Never write toward the SACs explicitly ("we urge acceptance") — they read the record
  for resolved substance, and advocacy is not substance.

## Output format

```text
[Concern map] <Rx.y -> soundness / excitement / misreading / taste>
[Reply drafts] <numbered, evidence-anchored, concession-explicit>
[New-in-window evidence] <what was computed, labeled as new>
[Camera-ready commitments] <specific edits promised>
[Residual risk after response] <what remains unresolved and why>
```

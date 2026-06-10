---
name: asr-workflow
description: Use as the entry point for any American Sociological Review (ASR) manuscript. Routes to the right ASR sub-skill based on the lifecycle stage and the manuscript type (Article up to 15,000 words vs. Comment/Reply up to 3,000). It dispatches; it does not draft content.
---

# ASR Workflow Router (asr-workflow)

The orchestrator for an ASR submission. ASR publishes across all of sociology and across very
different methods, so the router's first job is to confirm the work has **broad sociological
significance** and to send the user to the matching skill for their stage and method.

## When to trigger

- Starting a new ASR paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding between a full **Article** and a **Comment/Reply**
- Returning with a decision letter (route to `asr-rebuttal`)

## First question: manuscript type & method

| Situation | Type | Note |
|-----------|------|------|
| Full original study, broad significance | **Article** (≤ 15,000 words incl. refs + footnotes) | the main pipeline below |
| Critique of / reply to a published ASR piece | **Comment/Reply** (≤ 3,000 words) | tight scope; engage the original directly |

Then identify the **method**, because design and analysis advice differ sharply:
quantitative/demographic · comparative-historical · ethnographic/interview · network · computational.

## Routing map (stage → skill)

```text
Idea / fit?                      → asr-topic-selection
Where does it sit in the field?  → asr-literature-positioning
What's the argument?             → asr-theory-building
Is the design defensible?        → asr-research-design
Are the analyses sound?          → asr-data-analysis
Are the exhibits clear?          → asr-tables-figures
Does it read for the discipline? → asr-writing-style
Data documented / shareable?     → asr-data-and-transparency
How will it be judged?           → asr-review-process
Ready to submit?                 → asr-submission
Got an R&R / decision?           → asr-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → data-and-transparency → review-process → submission → rebuttal`

Iterate: ethnographic and comparative-historical papers especially loop theory ↔ evidence many times.

## Symptom-to-skill dispatch

The router's value is matching a felt problem to the right ASR skill fast. Because the ASA flagship
judges breadth of significance and method-appropriate rigor together, most symptoms map cleanly to one
sub-skill — use this lookup before defaulting to the linear order.

| Symptom you arrive with | Likely root | Route to |
|--------------------------|-------------|----------|
| "A reader says it's too narrow" | fit / framing | asr-topic-selection |
| "Reviewer says I missed key work" | cross-subfield positioning | asr-literature-positioning |
| "It's called merely descriptive" | no portable mechanism | asr-theory-building |
| "Reviewer doubts the causal/case logic" | design | asr-research-design |
| "They want more robustness" | analysis | asr-data-analysis |
| "An exhibit is unclear" | exhibits | asr-tables-figures |
| "It reads as subfield-only" | prose for the discipline | asr-writing-style |
| "How could anyone verify this?" | transparency | asr-data-and-transparency |
| "What will reviewers want?" | expectations | asr-review-process |
| "Submitting tomorrow" | preflight | asr-submission |
| "Got an R&R" | response letter | asr-rebuttal |

## Worked micro-example (illustrative routing)

A user arrives mid-project with a comparative-historical study and a vague worry.

```
User: "I have four country cases and good archives, but a colleague says it 'won't fly at ASR.'"
Router read: the worry is breadth/portability, not data → start at asr-theory-building (extract the
  portable causal logic), then asr-literature-positioning (general debate), then asr-research-design
  (case-selection + adjudication), looping theory ↔ evidence as comparative-historical work demands.
Type: full study, broad claim → Article (≤15,000 incl. refs + footnotes), not a Comment.
Then: asr-tables-figures (evidence table) → asr-writing-style → asr-data-and-transparency.
```

The router resists the linear default and sends the comparative-historical case to the theory and
positioning skills first, where its fit risk actually lives.

## Referee-stage pushback → which skill answers it

- *"Not significant for the discipline."* → asr-topic-selection then asr-writing-style (front-load
  stakes).
- *"Method isn't rigorous for its kind."* → asr-research-design in the matching tradition.
- *"Masking is broken."* → asr-submission masking sweep before re-upload.

## Calibration anchors

- **Broad significance is the gate, not a garnish.** The flagship's first question is always whether the
  work reaches the whole discipline; route there whenever fit is in doubt.
- **Method sets the path, not just the advice.** Ethnographic and comparative-historical papers loop
  theory and evidence repeatedly; do not force them through a single linear pass.
- **Confirm volatile submission specifics** (fee, caps) against the journal's current guidelines when
  the router reaches asr-submission.

## Anti-patterns

- Treating ASR like a subfield journal — the contribution must reach the whole discipline
- Forcing a regression template onto ethnographic, historical, or interpretive work
- Padding a focused critique into an Article when a Comment/Reply fits
- Forgetting the $25 processing fee and the masked-manuscript requirement at submission

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】Article / Comment-Reply
【Method】quant / comparative-historical / ethnographic / network / computational
【Route to】asr-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — sociology data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official ASR URLs behind every fact in this pack

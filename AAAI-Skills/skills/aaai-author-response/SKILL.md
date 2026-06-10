---
name: aaai-author-response
description: Use when drafting an AAAI author response (rebuttal) under the single short character-limited author-feedback window, the no-URL rule, no-new-results guidance, AI-generated-review handling, and the AAAI two-phase review process where Phase-2 papers receive one feedback round before SPC/AC discussion.
---

# AAAI Author Response

Use this after AAAI reviews are released. AAAI rebuttal space is scarce: the AAAI-26 FAQ allowed a
single 2500-character response, disallowed URLs, and discouraged new results. Reopen the current
rebuttal FAQ before drafting.

## Triage

- Respond to decision-critical factual errors first.
- Address human reviews and AI-generated review points when they affect the SPC/AC decision.
- Do not spend space on tone, score fairness, or reviewer motivation.
- Do not include URLs if current rules forbid them.
- Do not introduce new experiments or results. Explain existing evidence, clarify omissions, or
  state why requested experiments are not needed.
- If supplementary files were missing or corrupted, acknowledge the limitation; AAAI-26 did not
  permit updates at rebuttal time.

## What moves an AAAI score

Author feedback at AAAI is read by human reviewers and weighed in SPC/AC discussion, not by the
non-decisional AI review. With one short response and no second round, spend every character on the
concern most likely to flip a borderline decision. Triage each reviewer point into a lane:

- Factual error that, if uncorrected, sinks the paper: answer first, cite the submitted anchor.
- Misread of an existing result: clarify and point to the table, theorem, or appendix line.
- Request for a new experiment: explain why submitted evidence covers it, or scope the claim.
- Taste or framing complaint: usually skip; a defensive paragraph rarely moves the score.

## Reviewer-pushback patterns and the AAAI fix

- "No comparison to method X." Fix: name the submitted table row that includes X, or argue X is out
  of scope; do not promise a fresh run that rules forbid.
- "Results may not hold beyond one benchmark." Fix: cite the seed or split variation in the
  supplement; if absent, narrow the claim instead.
- "The AI-generated review flags a missing baseline." Fix: correct it calmly with a submitted
  pointer; the AI review is advisory, so a one-line factual rebuttal suffices.

## Worked vignette

A multi-agent-coordination paper gets two borderline scores. Reviewer 1 wrongly says the protocol
ignores communication cost; Reviewer 2 asks for a human-baseline study. Triage: R1 is decision-
critical, so sentence one corrects it and cites Section 4's cost ledger; R2's request is out of
scope, so one sentence notes the simulator already bounds it and limits the claim to simulated
agents. Tone and the AI review's nit are cut to stay under budget.

## Compression pattern

1. One sentence: central correction.
2. One sentence: strongest evidence in the submitted paper/checklist/supplement.
3. One sentence: answer the most damaging reviewer concern.
4. One sentence: clarify scope or limitation.
5. One sentence: optional camera-ready clarification if accepted.

## Output format

```text
[Response budget] <characters used / limit>
[Priority issue] <reviewer or AI-review concern>
[Draft rebuttal] <AAAI-ready text, no URLs>
[Submitted evidence anchor] <section/table/figure/checklist/supplement item>
[Cut list] <what to delete if over limit>
```


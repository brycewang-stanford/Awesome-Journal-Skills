---
name: aaai-author-response
description: Use when drafting AAAI rebuttals under the single short author-response limit, no-URL rule, no-new-results guidance, AI-review handling, and two-phase review process.
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


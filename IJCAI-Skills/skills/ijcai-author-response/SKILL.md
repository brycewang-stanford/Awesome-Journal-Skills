---
name: ijcai-author-response
description: Use when drafting IJCAI or IJCAI-ECAI author responses under the official one-page template, concise-response guidance, no-new-results constraints, code-link restrictions, factual-error triage, pressing-question triage, and confidential unethical-review channel.
---

# IJCAI Author Response

Use this after IJCAI reviews are released. Reopen the current Author's Response FAQ and
response template before drafting; rebuttal rules are cycle-specific.

## Triage

- Respond only when a reviewer asks a pressing question, when a factual error could drive
  rejection, or when an unethical review needs confidential escalation.
- Do not use the response to complain about tone, scores, reviewer identity, or broad
  disagreement without a decision-relevant correction.
- Keep the public PDF response short. IJCAI-ECAI 2026 limited ordinary responses to one
  page using the official response template.
- Do not upload new code, new links, new experiments, or new results. Clarifying figures or
  examples are acceptable only when they explain material already in the submission.
- Use the confidential box only for unethical-review concerns; it is not visible to ordinary
  PC reviewers.
- If a late review arrives during the response period, follow the current FAQ for extension
  requests rather than guessing.

## Compression pattern

1. State the decision-critical correction.
2. Anchor it to the submitted section, table, figure, theorem, appendix, or supplement.
3. Answer the requested clarification and stop.
4. If needed, add a camera-ready clarification promise without adding new evidence.

## Output format

```text
[Response budget] <pages used / current limit>
[Eligible reason] pressing question / factual error / unethical review
[Draft response] <IJCAI-ready text>
[Evidence anchor] <submitted location>
[Do-not-include list] <new results, code links, broad complaints, identity leaks>
```

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

## Triage table: respond or stay silent

The one-page budget forces ruthless selection. The response is not a dialogue, and phase-1
summary-reject papers usually get no response, so reserve the page for decision-changing items.

| Reviewer point | Respond? | How |
| --- | --- | --- |
| Pressing question that could flip the score | Yes | Point to the submitted location |
| Factual error driving rejection | Yes | Correct precisely; anchor to section/table/theorem |
| "Add experiment X" | No new results | Promise a camera-ready note or cite existing evidence |
| Tone, score, broad disagreement | No | Do not spend budget relitigating |
| Suspected unethical review | Confidential box | Not the public PDF |

## Worked vignette: a planning paper rebuttal

A planning paper draws one strong review and one that wrongly claims the optimality proof
assumes unit costs. That misreading could drive rejection, so it earns space: cite the
assumption already stated in the submitted theorem and point to the appendix proof, without a
new result. A second reviewer asks for an extra benchmark family; since no new experiments may
be added, promise a camera-ready note and reference the closest existing table. The complaint
about presentation tone gets no words.

## Reviewer pushback and the venue-specific fix

- "You added new results in the response." Remove them; clarify only what the submission already
  supports, since new evidence is disallowed.
- "Response argues the score, not a fact." Refocus on the one decision-critical correction.
- "Reviewer was unethical." Use the confidential channel, not the public response.

## Output format

```text
[Response budget] <pages used / current limit>
[Eligible reason] pressing question / factual error / unethical review
[Draft response] <IJCAI-ready text>
[Evidence anchor] <submitted location>
[Do-not-include list] <new results, code links, broad complaints, identity leaks>
```

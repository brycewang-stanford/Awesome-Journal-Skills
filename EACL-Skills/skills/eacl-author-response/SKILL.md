---
name: eacl-author-response
description: Use when drafting an EACL author response during the ACL Rolling Review rebuttal window, covering how to triage reviewer points, address the action editor who writes the meta-review, answer NLP objection patterns, run in-window experiments, flag deficient reviews, and decide respond-now versus revise-for-a-later-venue given EACL's single cycle.
---

# EACL Author Response

Use this to work the ARR rebuttal window for a paper aimed at EACL. In ARR the response is
addressed to reviewers **and** to the **action editor** who will synthesize a meta-review;
that meta-review, not any single score, is what EACL's area chairs read at commitment. Reopen
the current ARR author guidelines before drafting.

## Read the room first

- Identify the **action editor's lens**: the meta-review is where reviews get weighed, so a
  response that moves the action editor matters more than one that merely satisfies the harshest
  reviewer.
- Separate **blocking objections** (a claim reviewers think is unsupported, a missing baseline,
  a reproducibility gap) from **preference comments** (a different framing, an extra dataset a
  reviewer would like). Spend the word budget on the blocking set.
- EACL's **single cycle** raises the stakes of this window: for an edition like EACL 2027 there
  is no next cycle to defer to, so a fixable objection should be fixed *now* if the experiment
  fits the window.

## Objection-to-move table

| Reviewer objection pattern | Strong response move | Weak response move |
|---|---|---|
| "Claim broader than evidence" | Narrow the claim in text; point to the exact table | Argue the claim is "obviously" fine |
| "Missing tuned/LLM baseline" | Add it if runnable in-window; else scope the claim | Dismiss the baseline as unfair |
| "Not enough languages" | Add the runnable subset; state the residual in Limitations | Assert results "would generalize" |
| "Possible contamination" | Report an overlap check or decontamination result | Ignore or hand-wave |
| "Significance unclear" | Report a test / CIs over seeds | Cite a single-run delta |

## Drafting rules

- Lead each reply with the **concrete change** ("We added X; see revised Table 2"), then the
  reasoning — reviewers skim.
- Do **not** introduce unsupported new claims or results you cannot show; a promise you cannot
  substantiate reads worse than an honest limitation.
- Keep the tone factual and non-defensive; the action editor is reading for whether you engaged,
  not whether you "won."
- Respect anonymity: no links that deanonymize, no "as we said in our NAACL paper."

## Runnable-experiment discipline

```text
For each requested experiment:
  fits_window?  = can it finish and be written before the response deadline?
  changes_claim? = would the result actually alter a reviewer's objection?
  -> run only if fits_window AND changes_claim
  -> otherwise: acknowledge, scope the claim, and record it in Limitations
```

Do not start a sprawling experiment that cannot land in time; a half-reported result invites a
sharper objection.

## Flagging a deficient review

- If a review is unsupported, off-topic, or hostile, you may **flag it to the action editor**
  through the proper ARR channel rather than fighting it point-by-point in the public reply.
- Document the specific deficiency (factual error, no justification) — flagging is for genuine
  process failures, not for a low score you dislike.

## When not to respond hard

- If the reviews reveal a **structural gap** no in-window experiment can close, the honest move
  may be to accept the outcome and plan a **later venue** — but remember EACL's calendar: the
  next *ACL opportunity is a different conference, so `eacl-topic-selection` and `eacl-workflow`
  should drive that call.

## Output format

```text
[Response plan] <blocking objections, ranked>
[Action-editor angle] <what the meta-review needs to hear>
[In-window experiments] <run / defer, with reason>
[Reviewer replies] <one concise reply per reviewer>
[Deficient-review flags] <if any, with documented reason>
[Route decision] <respond-and-commit / revise-for-later-venue>
```

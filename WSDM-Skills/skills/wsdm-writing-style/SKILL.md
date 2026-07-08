---
name: wsdm-writing-style
description: Use when drafting or revising prose for a WSDM paper - the practical-yet-principled register, user-and-platform-grounded framing, self-containment writing for a no-rebuttal review, ethical-considerations craft, limitation sentences that protect borderline papers, and compression into the appendix-inclusive page cap.
---

# WSDM Writing Style

Revise a manuscript into the register WSDM's series page announces for itself:
"practical yet principled approaches" to search and mining on the Web and the
Social Web. That phrase is an editorial instruction. A WSDM paper earns its
slot by being simultaneously deployable-sounding and analytically honest - pure
benchmark exercises read as under-motivated, pure war stories read as
unscientific. The stylistic moves below operationalize that balance.

## Open with the behavioral problem, not the model family

WSDM work starts from something users, platforms, or web data actually do:
clicks are position-biased, sessions are short, graphs are power-law sparse,
feedback loops entrench popularity, adversaries game ranking. The strongest
openings name that behavioral fact and make the technical contribution the
response to it.

```text
Weak (model-first):
  "Transformer-based architectures have shown promise in recommendation.
   We propose a novel attention mechanism..."

WSDM-shaped (behavior-first):
  "Users abandon a search session after roughly one unsatisfying page,
   so a ranker trained on clicks observes almost nothing below rank ten.
   We show this truncated feedback systematically distorts <X>, and give
   an estimator that corrects it using only logged data."
```

The second version does three venue-calibrated things: it grounds the problem
in interaction behavior, it implies the data regime (logs, not labels), and it
scopes the contribution ("using only logged data") before a reviewer asks.

## The self-containment voice

Because WSDM historically offers no rebuttal, style must do the job dialogue
does elsewhere. Concretely:

- **Answer objections in-line, at the moment they arise.** After a surprising
  result, the next sentence should be the control that rules out the boring
  explanation - not a hope that reviewers won't think of it.
- **Pre-commit scope.** Write claim sentences whose quantifiers survive
  hostile reading: "improves nDCG@10 on three of four public benchmarks under
  temporal splits" is defensible; "consistently outperforms state of the art"
  invites a terminal review.
- **Show the failure mode.** One honest paragraph on where the method breaks
  (cold users, head queries, adversarial content) converts a reviewer's
  discovery into your demonstration of judgment.

## Sentence-level tells, WSDM edition

| Draft tell | Why it hurts here | Repair |
|---|---|---|
| "web-scale" with no numbers | Industry reviewers know what scale looks like | Give corpus/user/query counts, even rounded |
| "significantly better" without a test | Ranking metrics are noisy; the pool knows it | Name the test, unit (query/user), and p-value or CI |
| "real-world dataset" for MovieLens | Reads as inflation to log-data veterans | Call public benchmarks what they are |
| "novel framework" | Framework-speak hides the mechanism | Name the one thing that changed and its effect |
| Unexplained acronym soup in the intro | Single-track audience spans IR, graphs, ads, recsys | Expand on first use; the reader may be from the adjacent subfield |

The last row is genuinely WSDM-specific: a single-track community means your
talk - and your reviewers - include people from every corner of the venue's
scope. Write the introduction for the intelligent non-specialist in the
adjacent chair.

## The ethics section as prose, not boilerplate

WSDM requires an ethical-considerations discussion and excludes it from the
page count. Reviewers can smell a template. Write it like a technical section:

1. Name the specific population and data (whose behavior, collected how, under
   what terms).
2. Name the sharpest realistic harm of *your* contribution (a better ranker can
   amplify popularity bias; a deanonymization-adjacent mining result can be
   misused; an ad-targeting improvement has manipulation surface).
3. State mitigations you actually implemented (aggregation, differential
   thresholds, release policy), not aspirations.
4. If the honest answer is "low marginal risk," argue it in two sentences
   instead of padding.

## Compression without loss

The 9-page inclusive budget (2026 anchor; see `wsdm-supplementary` for the
arithmetic) rewards specific habits:

- One idea per paragraph; delete paragraph-final summary sentences that repeat
  the paragraph.
- Kill the second example everywhere: one well-chosen example plus a precise
  general statement beats two examples.
- Move mechanics into figures: a pipeline figure with a two-line caption often
  replaces half a page of process prose.
- Related work as positioning, not survey - three contrast sentences beat
  fifteen citation-list sentences (method in `wsdm-related-work`).
- Never compress: metric definitions, split protocols, or the limitation
  paragraph. These are the sentences the SPC quotes when defending the paper.

## Abstract anatomy for this venue

Six sentences carry a WSDM abstract: behavioral fact; consequence for
search/mining/recommendation; the mechanism, named; evaluation regime
(datasets, split type, test) attached to the main number; the online or
deployment sentence if one exists, protocol-tagged; the artifact/limitation
sentence. The worked rewrite in
`../../resources/worked-examples/01-introduction.md` executes exactly this
skeleton - compare your abstract against it sentence by sentence, and delete
anything that is neither one of the six nor evidence for one.

## Revision pass order

1. Claims pass: extract every claim sentence; check each against its evidence
   and its quantifier.
2. Objection pass: inject in-line answers from the objection inventory
   (`wsdm-author-response`).
3. Register pass: apply the tells table; ground openings in behavior.
4. Budget pass: cut to fit using the priority order above.
5. Cold-reader pass: someone from an adjacent WSDM subfield reads the intro and
   restates the contribution; if their restatement is wrong, rewrite.

## Output format

```text
[Register] behavior-first opening: yes / rewritten
[Claim audit] N claims; overquantified: <list with repairs>
[Self-containment] in-line objection answers added at: <locations>
[Tells] instances found -> fixed: <count by type>
[Ethics prose] specific population/harm/mitigation named: yes / boilerplate
[Cold-reader test] contribution restated correctly: yes / no
```

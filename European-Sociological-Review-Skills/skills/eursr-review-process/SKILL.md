---
name: eursr-review-process
description: Use when you need to understand how the European Sociological Review (ESR) evaluates a manuscript — double-blind peer review, what comparative quantitative reviewers weigh, decision categories, and the ethics rules (anonymity, no simultaneous submission). Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (eursr-review-process)

Knowing how ESR reviews helps you pre-empt the failure modes before submitting. ESR uses **double-blind**
review and draws reviewers from the comparative quantitative-sociology community, so a paper must read
credibly to experts who scrutinize the comparative/longitudinal design and the modeling.

## When to trigger

- Before submitting, to stress-test the manuscript against likely reviewer objections
- Interpreting a decision letter and setting expectations
- Understanding why a portable mechanism *and* a defensible quantitative design both matter

## How ESR review works

1. **Double-blind review.** Neither authors nor reviewers are identified; the manuscript must be
   **completely anonymous** (no author names, identifying acknowledgments, or identifying self-citation
   wording). Prepare accordingly (see `eursr-submission`).
2. **Editorial screening.** Editors assess fit, comparative/theoretical contribution, and the
   length-vs-contribution balance; weak-fit, single-country-descriptive, or out-of-scope papers may be
   declined without full external review. Make the comparative mechanism obvious early.
3. **External review.** Expert reviewers assess the contribution, the theory and hypotheses, the
   comparative/panel design, the modeling (level, clustering, invariance, few-cluster inference), and
   the evidence-to-claim link.
4. **Decisions.** Reject, revise and resubmit (major or minor), or (rarely on first round) accept. R&R
   is the normal path; expect substantial revision. **Replication packages are checked around
   conditional acceptance** for statistical/computational work.
5. **Ethics.** Submitting elsewhere while under ESR review is not allowed; prior appearances must be
   disclosed; English quality is the author's responsibility.

## What reviewers weigh

| Reviewer asks | You answer with |
|---------------|------------------|
| Does this move a comparative debate? | explicit portable mechanism + comparative leverage |
| Is the design right for the claim? | the design defense in `eursr-research-design` |
| Is the modeling correct? | right level/clustering, invariance, few-cluster inference (`eursr-data-analysis`) |
| Are claims warranted by the evidence? | intervals, robustness, honest scope |
| Is the contribution distinct from prior work? | positioning in `eursr-literature-positioning` |

## Shape the paper to pass

- Make the comparative mechanism and hypotheses explicit in the introduction.
- Anticipate the toughest modeling objection (measurement equivalence, macro-N inference) and answer it.
- Present robustness and leave-one-country-out checks honestly — reviewers trust candor.
- Engage the comparative frontier, not just one national literature.
- Have the replication package ready in spirit even before it is requested.

## Stage-by-stage failure points

| Stage | What stops a paper here | Pre-empt by |
|-------|--------------------------|--------------|
| Editorial screening | single-country / weak comparative fit | front-loading the comparative mechanism |
| Anonymity integrity | identifying wording or acknowledgments | the `eursr-submission` anonymity pass |
| Review — contribution | "adds a coefficient, not a mechanism" | a portable macro–micro claim |
| Review — design | comparison/panel can't identify the claim | the design defense + adjudication sentence |
| Review — modeling | wrong level / fragile macro inference | df-aware SEs, invariance, leave-one-out |

## Worked micro-example (illustrative)

A multilevel attitudes paper is mock-reviewed before submission.

```
Screening risk: reads as 24-country description → reframe around the contextual mechanism (how welfare
  generosity reshapes the individual link between insecurity and redistribution preference)
Contribution reviewer: "is there a mechanism, not just a country pattern?" → cross-level interaction headline
Modeling reviewer: "few clusters; invariance?" → wild cluster bootstrap + reported invariance level
Transparency reviewer: "package?" → DAS + Zenodo deposit ready (statistical → not exempt)
Predicted outcome: major R&R, not first-round accept (typical at ESR for a promising paper)
```

Stress-testing against the panel before submission converts likely screening and modeling failures into a clean R&R path.

## Referee pushback → ESR-specific fix

- *"Why ESR and not a national journal?"* → Surface the comparative mechanism on the first page; ESR
  screens hardest on comparative/theoretical contribution.
- *"Your macro inference is fragile."* → Use df-aware methods and temper the country-level claim.
- *"You expected an accept."* → Plan for a substantial R&R; first-round acceptance is rare at ESR.

## Calibration anchors

- **Contribution and modeling correctness are both load-bearing.** ESR rarely advances a paper strong on
  only one; the double-blind panel weights the portable mechanism and the comparative modeling together.
- **Candor reads as competence.** Expert reviewers find fragile macro inference and non-equivalent
  measures; reporting them first builds trust that carries a borderline paper.
- **Confirm decision-category wording** against the current guidelines if you need exact labels — the
  broad shape (reject / major-minor R&R / rare accept) is stable.

## Anti-patterns

- A single-country descriptive paper sent to a comparative flagship
- Hiding fragile macro-N inference or non-equivalent measurement
- Expecting acceptance without a serious R&R round
- Treating a modeling reviewer's standards as illegitimate rather than addressing them

## Output format

```
【Comparative contribution】portable mechanism + leverage clear? [Y/N]
【Design】defensible for the claim? [Y/N]
【Modeling】level/clustering/invariance/few-cluster handled? [Y/N]
【Evidence→claim】warranted and candid? [Y/N]
【Realistic outcome】reject / major-or-minor R&R / (rare) accept
【Next】eursr-submission (or eursr-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — double-blind review, ethics, OUP/ECSR submission norms

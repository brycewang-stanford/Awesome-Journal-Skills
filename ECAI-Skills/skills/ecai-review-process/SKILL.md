---
name: ecai-review-process
description: Use when reasoning about how an ECAI submission is evaluated — double-blind review, the summary-reject first phase, area chairs / senior PC, the single author-response (rebuttal) window, an accept/reject decision (no journal-style major-revision round), and how ECAI's process and its joint IJCAI-ECAI 2026 form differ from AAAI, IJCAI standalone, and AAMAS.
---

# ECAI Review Process

Model the pipeline before interpreting any single review. ECAI runs a **single-round, double-blind
conference review with a rebuttal** — not a journal-style revise-and-resubmit. The most
consequential mental shift for authors arriving from a journal (or from a venue with a major-
revision decision) is that there is **no second submission**: the paper you submit, plus one
short author response, is the whole story. The current edition, **IJCAI-ECAI 2026**, follows the
IJCAI process because ECAI 2026 is being run jointly with IJCAI.

## Process model (IJCAI-ECAI 2026)

- Submission and review are **double-blind**; identities are hidden from reviewers throughout.
- A **summary-reject** first phase filters clearly-out-of-scope or below-bar submissions early
  (IJCAI-ECAI 2026 summary-reject notification: **4 March 2026**). A paper cleared past summary
  reject goes to full review.
- Full review is organized under **area chairs / senior PC** who oversee reviewers in a topic
  area and lead the discussion. Reviewers weigh significance of the AI contribution, technical
  soundness (proofs and/or experiments), clarity, and fit.
- Authors get **one author-response (rebuttal) window** (IJCAI-ECAI 2026: **7-10 April 2026**) to
  answer factual points before the final decision.
- The decision is **accept or reject** (final notification **29 April 2026**). There is no
  guaranteed revision round; camera-ready changes are minor, not a re-review.

## Reading the decision categories

| Decision | What it means | Author move |
|---|---|---|
| Accept | Contribution and evidence hold | Camera-ready in the correct template; do not expand scope |
| Reject (after full review) | A soundness, significance, or clarity gap the rebuttal did not close | Revise substantively and reroute (AAAI/IJCAI/a specialist venue) or resubmit next ECAI |
| Summary reject | Out of scope, below bar, or a formatting/anonymity violation caught early | Do not appeal into the void — fix the structural issue before any resubmission |

The strategic reading: because there is **no major-revision safety net**, the submitted paper must
already be complete — the proof finished, the baseline fair, the claim matched to the evidence. A
gap you were "planning to fix in revision" has nowhere to go.

## How ECAI differs from its siblings

- **vs. a journal / major-revision venue:** ECAI has **no Major Revision decision**. You cannot
  count on a second round; there is one rebuttal, then accept/reject.
- **vs. AAAI:** AAAI and ECAI are both general-AI, double-blind, single-round with rebuttal, but on
  different calendars and templates (AAAI style vs `ecai.cls`/`ijcai.sty`) and governed by
  different bodies (AAAI vs EurAI). Never assume shared dates or format.
- **vs. IJCAI (standalone years):** ECAI is EurAI's European flagship; IJCAI is the international
  one. In **2026 they are the same event** (joint IJCAI-ECAI), so the process is IJCAI's — but in a
  standalone ECAI year the FAIA/`ecai.cls` conventions and PAIS co-location return.
- **vs. AAMAS / KR / specialist venues:** those run their own reviewing for multi-agent systems or
  knowledge representation; a paper matched better to a specialist reviewer pool may fare better
  there than in ECAI's broad pool (`ecai-topic-selection`).

## Who reads you

Expect several reviewers under an area chair drawn from your topic area — and note that by
submitting you volunteer for the reviewer pool yourself (IJCAI-ECAI 2026 policy). Because ECAI
spans symbolic AI, planning, KR, multi-agent systems, and ML, matching your topics well is what
gets you *expert* reviewers rather than distant ones. Vague method descriptions get caught in the
discussion the area chair runs, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  topics/keywords -> area chair + reviewer pool     (largest lever)
[Summary-reject risk] scope, formatting, anonymity, page budget correct BEFORE upload
[Rebuttal]           correct factual misreadings, supply one asked-for number,
                     answer the specific objection each reviewer raised
[After reject]       no appeal that reopens the decision; reroute or resubmit next cycle
```

A rebuttal moves borderline papers when it corrects a factual misreading or provides a clarification
a reviewer said was missing; it does not move papers when it argues taste or promises future work.
With only one response and no revision round, the rebuttal is a **precision instrument**, not a
plan.

## Reading a review packet

Weight reviews before answering. A review that cites your definitions, lemmas, and tables was read
closely; its author is your likely advocate if the rebuttal holds. A review that discusses only
novelty has left soundness to the others — answer each reviewer on the axis they raised. The area
chair, not any single reviewer, drives the outcome in discussion, so a response that gives the AC a
clean reason to champion the paper is worth more than one that "wins" against a hostile reviewer.

## Misreadings to avoid

- **Expecting a revision round** — there is none; the submission is final bar minor camera-ready.
- **Treating the rebuttal as a debate** — the AC-led discussion decides; your text is evidence for
  an advocate, not a closing argument.
- **Ignoring summary-reject risk** — a formatting, anonymity, or scope slip can end the paper
  before review even begins.
- **Projecting last year's process** — a standalone ECAI and a joint IJCAI-ECAI year differ in
  organizer, template, and sometimes mechanics; confirm the current edition.

## Output format

```text
[Process stage] pre-submission / summary-reject phase / under review / rebuttal / final
[Edition regime] standalone ECAI / joint IJCAI-ECAI (IJCAI process)
[Decision] accept / reject / summary reject, with the criterion driving it
[Criterion map] each review point -> significance | soundness/proof | evidence | clarity | fit
[Leverage plan] the rebuttal move that can actually change this AC's recommendation
[Forbidden moves] identity leak / new unsupported claims / promising a revision that cannot happen
```

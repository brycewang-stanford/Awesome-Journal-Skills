---
name: focs-author-response
description: Use when managing author-side communication around a FOCS (IEEE Symposium on Foundations of Computer Science) submission, where no rebuttal round exists — discharging objections inside the paper before submission, handling rare chair-mediated queries, and converting a rejection into a disciplined autumn resubmission.
---

# FOCS Author Response

The FOCS 2026 CFP schedules no rebuttal, no discussion phase, and no
author-visible reviews before decisions (checked 2026-07-08; any informal
PC-initiated clarification in a given cycle: 待核实). At a venue with no
second turn, "author response" is a set of practices displaced in time:
persuasion happens *before* the deadline, correction happens *after* the
decision, and almost nothing happens in between. This skill covers all three
phases.

## Phase 1 — the pre-emptive rebuttal (before submission)

Write the objections you would rebut, then edit the paper until each is
answered where it would arise. Build the table with a co-author playing
antagonist:

| Anticipated objection | Where discharged | Device |
|---|---|---|
| "Isn't this implied by [强 result]?" | Intro, directly after the theorem | One paragraph: why the known result does not give yours (regime, model, quantifier order) |
| "The improvement is small" | Obstacle paragraph | Show the barrier the small step crosses (`focs-writing-style`) |
| "Lemma 5.3 looks fragile" | Overview §3 + full proof | Flag it yourself: "the delicate step is…", then prove it twice as carefully |
| "Why isn't this just [technique X]?" | Technical overview | A remark stating where X breaks on your instance |
| "Related to concurrent arXiv:2506.xxxxx?" | Related work | Independence paragraph written generously (`focs-related-work`) |

The discipline: every objection you can generate is answered *in text a
breadth reviewer will actually reach* — inside the ten-page window, not in a
page-40 remark. An objection answered only on page 40 is unanswered for the
committee member who raises it in discussion.

## Phase 2 — during review (April to notification)

The correct volume of author-initiated contact is near zero. Legitimate
exceptions, all routed through the PC chair:

- **You found a real bug.** Report it promptly and factually: which lemma,
  what breaks, whether it is repaired. Chairs respect this; discovering the
  bug post-acceptance is far worse for everyone.
- **A subsuming preprint appeared.** A short factual note lets the PC judge
  with current information; silence gambles your credibility on the
  committee not checking arXiv.
- **Procedural anomaly** (e.g., you can prove a conflict was violated). State
  it once, without advocacy.

What is never legitimate: nudging, supplementary "clarification" emails,
sending improved bounds (those belong in the next version), or contacting
suspected reviewers. The venue's no-response design is deliberate; working
around it reads as exactly what it is.

## Phase 3 — after the decision

**On acceptance**, any reviewer comments arrive as gifts with no compliance
mechanism; triage them into camera-ready fixes anyway (`focs-camera-ready`)
— these are the field's most careful readers.

**On rejection**, run the resubmission protocol rather than the appeal
instinct (there is no appeals process):

```text
RESUBMISSION MEMO  (internal; one page; write within a week of the decision)
1. Verbatim quotes of every substantive review point (no paraphrase —
   paraphrase launders criticism into something easier to dismiss)
2. For each: ACCEPT (fix), REBUT (why wrong — with the proof/citation),
   or REFRAME (misreading caused by our text; fix the text, not the reader)
3. Venue decision: STOC (autumn deadline, 2027 cycle: 待核实) / SODA / CCC /
   ITCS / journal — re-run focs-topic-selection with the reviews as data
4. Diff plan: what changes before the next submission, owner and date each
```

Two norms specific to the theory two-flagship rhythm: first, the receiving
STOC committee will overlap socially (though not formally) with the FOCS one,
so resubmitting an unchanged paper is a recognized and quietly penalized
move — visible improvement is the currency; second, update the arXiv version
*before* the next submission so the public record and the resubmission agree
(`focs-reproducibility`), with a changelog naming what strengthened.

## A memo entry, worked

The difference between triage and rationalization is visible in the writing.
A REBUT entry that will survive your own re-reading in a month:

> **R2:** "The reduction in Section 6 appears to require bounded degree."
> **Class:** REFRAME (partially REBUT). The reduction does not require it —
> Lemma 6.4's proof handles arbitrary degree — but the *statement* of Lemma
> 6.4 as written only asserts the bounded case, so the reviewer read
> correctly. **Action:** restate Lemma 6.4 in full generality (the proof
> already covers it), add one sentence in the overview flagging that degree
> is unrestricted. **Owner/date:** LW, before STOC submission.

Note what the entry does not do: it does not label the reviewer careless,
and it locates the repair in the text rather than in the reader. Most
"wrong" reviews at this level are correct readings of imprecise writing.

## Deciding between the autumn options

The memo's venue line deserves its own analysis, because the reviews tell
you which committee to face next. Correctness complaints answered by real
fixes point back to the flagship track (STOC next, FOCS after). Significance
complaints from breadth readers, with depth readers positive, often mean the
paper is loved by specialists — SODA, CCC, or SoCG may simply be its
audience. Window complaints ("could not locate the proof of...") mean the
paper can return to the same tier after an exposition rebuild alone. And
uniformly thin reviews mean the decision carried no information: re-run
`focs-topic-selection` from scratch and trust your own audit over the noise.

## Tone calibration for all phases

Any text that reaches a chair or a future committee: factual, short,
zero adjectives about your own work, zero speculation about reviewers'
competence or identity. The theory community is small and has a long memory;
the response style you practice here is part of your research reputation in a
way that outlasts any single paper's outcome.

> **Illustrative teaching example.** The model, parameters, and predictions below are **fictional**
> and exist only to demonstrate Psychological Review house style for a *theory/model* introduction. No
> real-paper facts and **no empirical claims** are stated. Psychological Review is theory-only: there is
> no experiment of the author's own — data appear only to motivate or constrain the model.
> Corresponding skills:
> [`psychrev-writing-style`](../../skills/psychrev-writing-style/SKILL.md),
> [`psychrev-theory-construction`](../../skills/psychrev-theory-construction/SKILL.md),
> [`psychrev-argument-development`](../../skills/psychrev-argument-development/SKILL.md), and
> [`psychrev-contribution-framing`](../../skills/psychrev-contribution-framing/SKILL.md).

# Worked Example: A Psychological Review-Style Theory Introduction (before → after)

This demonstrates the **Psychological Review introduction arc** from `psychrev-writing-style`:
**phenomenon/tension → the standing theories and what they cannot do → the move this paper makes (the
model/mechanism) → derived predictions → the contribution, stated early.** The deliverable is **a model
with explicit assumptions + a mechanism + derived, falsifiable predictions confronted with existing
data**, never an experiment of the author's own. The register rule (`psychrev-writing-style`,
`psychrev-theory-construction`) is absolute: **model, assumption, prediction, parameter, scope — never
"we found," "results," "significant," or a new study as the contribution.**

**Illustrative paper (fictional):** *"Leaky Anchors: A Resource-Decay Model of Why Recall Confidence
Outlasts Recall Accuracy."* Fictional formal setting: a sequential-sampling memory model with a
slowly decaying confidence signal (invented to carry the argument; it asserts nothing about any real
dataset or finding).

---

## Before (reads as a literature review / empirical report — typical first-draft intro)

> Memory confidence has been studied extensively. Many studies have shown that people are often
> overconfident in their memories, and researchers have proposed various accounts. In this paper we
> review this literature and report new experiments showing that confidence and accuracy dissociate
> under delay. We ran three studies; in Study 1 the dissociation was significant (p < .05). We propose
> a model in which confidence is a moderator of the accuracy–delay relationship. Section 2 reviews the
> literature, Section 3 presents our experiments, Section 4 presents the model, and Section 5 concludes.

**What's wrong (against `psychrev-writing-style` / `psychrev-theory-construction` / `psychrev-contribution-framing`):**

- **Opens with a survey** ("has been studied extensively"), not the theoretical *tension* — a named
  anti-pattern in `psychrev-writing-style` (dictionary/survey opening).
- **Empirical-report register** ("we ran three studies," "significant (p < .05)," "report new
  experiments"). That is the JEP/Psychological Science lane; it reads as **wrong-journal** to a
  Psychological Review editor — the data, not the theory, would be the contribution.
- **No theoretical problem on page one.** A reader cannot tell what existing *theory* fails to explain.
- **"We propose a model in which confidence is a moderator"** — a verbal moderator-to-be-tested, with
  no mechanism and no derived predictions (`psychrev-theory-construction` build order; `psychrev-argument-development`).
- **Contribution is "we review and report"** — neither a survey nor an empirical report is a Review
  contribution (`psychrev-topic-selection` empirical-contribution test).
- **IMRaD roadmap** (Method/Results sections) that does not belong in a theory paper.

---

## After (Psychological Review arc — tension → standing theories' gap → the model → predictions → contribution early)

> People's confidence in a memory often stays high long after the memory itself has degraded: a name
> recalled with certainty today is misremembered next week, yet the certainty is slow to follow the
> accuracy down. Existing formal models of recognition and recall treat confidence as a **read-out of
> the same evidence** that drives accuracy — so when accuracy decays, confidence should decay with it.
> They have no mechanism for confidence and accuracy to come apart **over time**. *(the theoretical
> tension — what current models cannot do — in the first breath.)*
>
> This problem lives in the sequential-sampling tradition, where a decision and its confidence are both
> derived from an accumulated evidence signal. That shared-signal commitment is what makes the two
> quantities move together; it is also the commitment that creates the blind spot for their temporal
> dissociation. *(the standing theories, and the specific commitment that creates the gap.)*
>
> We propose a **resource-decay model** in which confidence and accuracy draw on **two coupled but
> separately decaying stores**: an accuracy signal that decays at rate *λ_a* and a confidence signal,
> seeded from it at encoding, that decays at a slower rate *λ_c < λ_a*. Each parameter has a stated
> psychological meaning, and the mechanism is explicit: confidence is **anchored** at encoding to the
> initial evidence and then **leaks** more slowly than the evidence it was anchored to — so the two
> stores diverge as delay grows. *(the move: a formal model with interpreted parameters + the
> why-mechanism, not a data plan.)*
>
> From the two decay rates we **derive** predictions rather than assert them. **P1:** the
> confidence–accuracy gap grows monotonically with delay, with a magnitude set by *λ_a − λ_c* — a
> qualitative ordering no shared-signal model produces. **P2:** manipulations that speed evidence decay
> (e.g., interference) widen the gap, while manipulations that re-anchor confidence (e.g., retrieval
> practice) shrink it — a *signature* that distinguishes the model from a single-store account. We show
> the model reproduces these orderings in **already-published** confidence-by-delay datasets, with the
> free-parameter count disclosed, and we name the pattern that would **falsify** it: a gap that closes,
> rather than widens, with delay. *(predictions derived and confronted with existing data; a risky,
> falsifiable claim — per `psychrev-argument-development`.)*
>
> Our contribution is to **respecify confidence as a separately decaying store** rather than a
> read-out of the accuracy signal: before this paper, sequential-sampling theory could not explain why
> confidence outlasts accuracy; after it, theory predicts *when and by how much* the two dissociate,
> and states the regime in which they do not. This differs from the nearest prior view — the
> shared-evidence read-out — not by adding a free moderator but by changing the **architecture** of how
> confidence is computed. *(contribution framed before → after, against a named prior view, per
> `psychrev-contribution-framing`.)* The same two-store mechanism extends, within stated scope, to any
> domain where a slowly updated meta-judgment is anchored to a faster-decaying primary signal. *(reach
> beyond the originating paradigm — a reasoned theoretical consequence, claimed only within scope.)*
>
> The paper proceeds by stating the assumptions and the two-store mechanism, deriving the model's
> behavior and confronting it with existing data, then stating scope, identifiability, and the
> conditions under which the dissociation should not appear. *(brief, theory-organized roadmap — no
> Method/Results sections, no over-signposting.)*

---

## Why the "after" meets the Psychological Review bar

Mapped to the skill checklists:

- **Opens with the theoretical tension, not a survey** — "confidence outlasts accuracy" and what current
  models cannot do is on page one (`psychrev-writing-style`: tension early; no dictionary opening).
- **Theory register, not empirical** — "the model predicts," "we derive," "existing data show"; no "we
  ran," no "p < .05" (`psychrev-writing-style` register table). The author runs no experiment.
- **Assumptions and mechanism are explicit before formalization** — two coupled stores with interpreted
  decay rates *λ_a*, *λ_c*, and the anchor-and-leak mechanism stated as the why
  (`psychrev-theory-construction` build order; parameters with psychological meaning).
- **Predictions are derived, not asserted, and confronted with existing data** — P1–P2 follow from
  *λ_a − λ_c*, are tested on already-published datasets with free-parameter count disclosed, and a
  falsifying pattern is named (`psychrev-argument-development`: derive, signatures, risky prediction).
- **Contribution stated early and as before → after, against a named prior view** (the shared-evidence
  read-out), and explicitly **not** an added moderator (`psychrev-contribution-framing`).
- **Scope is theorized** — the roadmap promises identifiability and a non-dissociation regime, treated
  as part of the theory rather than a limitations paragraph (`psychrev-boundary-conditions`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified Psychological
> Review theory/model papers** whose introductions execute this tension → model → predictions arc, and
> [`../official-source-map.md`](../official-source-map.md) for the scope and submission facts the
> checklists lean on.

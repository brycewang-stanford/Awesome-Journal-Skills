---
name: jme-review-process
description: Use when you need to understand how the Journal of Monetary Economics (JME) review process actually works — single anonymized (single-blind) review with at least two reviewers, the distinctive "up or out" first-revision rule, the ~50% publication-likelihood threshold for an R&R, suggested referees, and reconsideration.
---

# Review Process (jme-review-process)

## When to trigger

- You need to set expectations for what happens after submission
- You are unsure what "up or out" means for your revision strategy
- You want to know whether to suggest referees or request exclusions
- A decision arrived and you need to interpret it

## How JME review works

- **Single anonymized (single-blind) review**: reviewers know the author identities; **authors do not know the reviewers.** Plan your framing and self-citation accordingly — there is no point anonymizing the manuscript.
- **At least two reviewers**: suitable submissions are typically sent to a **minimum of two reviewers.**
- **Editors**: the journal is led by two **co-Editors-in-Chief**, **S. Borağan Aruoba (University of Maryland)** and **Eric Swanson (University of California, Irvine)** (Aruoba appointed as one of the two Editors-in-Chief effective January 1, 2022); neither outranks the other.
- **Suggested / excluded referees**: in the cover letter, authors **may suggest up to five referees** and request that some not be used.
- **Reconsideration**: a formal reconsideration of a rejection is **costly, rare, and unlikely to reverse** the decision — do not bank on it.

## The distinctive "up or out" funnel

JME's process is unusual and worth internalizing:

1. A **first-round decision is reject or revise-and-resubmit** — there is no slow drip of multiple R&R rounds.
2. Editors invite a resubmission **only when they judge at least a 50% likelihood of ultimate publication.** An R&R is therefore a **strong (though not guaranteed) signal.**
3. The resubmission is **"up or out"**: it must result in **acceptance or rejection** — there is **no second round of revise-and-resubmit.** Your one revision has to fully resolve the referees' concerns.

This funnel changes strategy: you cannot count on iterating across many rounds, so the first revision must be comprehensive, and at submission your contribution must be sharp enough to clear the 50% bar.

## Fee mechanics tied to the process

- A **US$350 submission fee** (**US$200 for full-time PhD students**) is charged **up front**; a manuscript is **only considered after payment.**
- **No fee** is charged for revised/resubmitted manuscripts.
- If a paper is **desk-returned without full review** (within roughly three months), **one half of the fee is refunded.**

## Checklist

- [ ] You understand review is single-blind (do not anonymize)
- [ ] Up to five suggested referees + any exclusions prepared for the cover letter
- [ ] You are prepared for **at least two** referee reports
- [ ] You understand the first revision is **"up or out"** (no second R&R)
- [ ] You understand an R&R signals **~50%** publication likelihood, not certainty


## Review-risk pass for Journal of Monetary Economics

Use this as a second-pass capability check. First lock the main macro object, the identifying variation, and the policy-relevant counterfactual; then test whether the manuscript addresses macro and monetary economists who expect the shock, mechanism, and policy margin to be visible early.

- **Primary move:** Turn likely reviewer objections into a ledger with response evidence, manuscript location, and the decision-maker who must be convinced first.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JIE for open-economy trade/finance emphasis, RED for dynamic macro theory, AEJ Macro for broader field positioning; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Review model】single anonymized (single-blind), ≥2 reviewers
【Suggested/excluded referees】ready? Y/N
【Decision type】reject / R&R (R&R ⇒ ~50% likelihood)
【Revision rule】"up or out" — one revision, then accept or reject
【Next step】jme-submission (pre-submit) or jme-rebuttal (on R&R)
```

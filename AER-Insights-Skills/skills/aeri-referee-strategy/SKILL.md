---
name: aeri-referee-strategy
description: Use when calibrating expectations for the fast, decisive American Economic Review: Insights (AER: Insights) review process — conditional-accept-or-reject decisions, the single-round model, and pre-empting the objections a short paper cannot afford. Explains the process and stress-tests the paper; it does not write the response letter (see aeri-rebuttal).
---

# Referee Strategy & the Fast Review Model (aeri-referee-strategy)

## When to trigger

- Before submission, to understand how AER: Insights decides and what referees punish
- Deciding whether the paper can survive a process with **no traditional R&R**
- Anticipating the one or two objections that would sink a short paper
- Choosing whether to risk AER: Insights vs. a journal that offers multiple rounds

## The AER: Insights process (official AEA baseline checked 2026-06-20)

AER: Insights runs **single-blind** AEA peer review: authors are visible to referees, while referees
remain anonymous to authors. It is deliberately **fast and decisive**:

- **First decision is conditional accept or reject** — there is **no traditional revise-and-resubmit** category.
- **Conditional accept** means the editor expects to publish subject to changes in the decision letter; authors usually get about **8 weeks** to return the revision, which is **normally not sent back to referees** for a second round.
- **Reject is reject** — there is no iterative path to wear referees down. The screening is sharp: a paper over the word/exhibit cap is **returned unreviewed**.
- Editor as of 2026: **Matthew Gentzkow** (lead editor beginning January 2024; founding editor Amy Finkelstein). Aim for AER-level importance in a short, clean package.

**Strategic implication:** because there is no R&R to fix things later, the paper must be **submission-ready and objection-proofed up front**. You get essentially one substantive look. A weak design, an overclaim, or a missing key check that an AER R&R would let you repair will instead produce a reject here.

## Pre-empt the objections a short paper cannot survive

A short paper has no room to answer everything during review, so answer the decisive objections **before** submitting:

| Likely objection | Pre-empt before submission |
|------------------|----------------------------|
| "Not important / not general interest" | Lead with the surprise and the prior overturned ([`aeri-topic-selection`](../aeri-topic-selection/SKILL.md)) |
| "Already known / incremental" | Confront the closest paper directly ([`aeri-literature-positioning`](../aeri-literature-positioning/SKILL.md)) |
| "Design not credible" | Put the single strongest diagnostic in-text ([`aeri-identification`](../aeri-identification/SKILL.md)) |
| "Result not robust" | One in-text check + a signposted appendix battery ([`aeri-robustness`](../aeri-robustness/SKILL.md)) |
| "Overclaimed" | Calibrate the claim to exactly what is identified |

Use the venue-neutral [reviewer-objection-checklist](../../resources/README.md) to stress-test the design by identification strategy before drafting the final version.

## Calibrating the bet

- If the single insight is genuinely important and the design is clean, AER: Insights offers a **fast, high-prestige** outcome.
- If the paper needs several rounds of referee guidance to reach credibility, a journal **with R&R** may fit better — AER: Insights will likely reject rather than coach.
- A rejected AER: Insights paper is often a strong fit for an **AEJ** field journal; some flow between AEA journals exists.

## Checklist

- [ ] You understand: **conditional accept or reject only**, no traditional R&R
- [ ] The paper is **submission-ready** — no key check is being deferred to a future round
- [ ] Each decisive objection above is pre-empted in-text or in the appendix
- [ ] Importance/general-interest is argued, not assumed
- [ ] Word/exhibit caps are met (else auto-return) before referees ever see it
- [ ] A fallback venue (e.g., an AEJ) is identified in case of reject

## Anti-patterns

- Submitting a "first draft to get referee feedback" — there is no R&R to iterate on
- Leaving the single most likely objection unaddressed, hoping to fix it in revision
- Assuming importance instead of making the surprise explicit
- Ignoring the cap and getting returned before review
- Treating a reject as the start of a negotiation

## Output format

```
【Process understood】conditional-accept/reject, no R&R, ~8wk conditional window? [Y/N]
【Decisive objections pre-empted】importance / novelty / design / robustness / claims
【Submission-ready】no key check deferred to a nonexistent round? [Y/N]
【Caps met】word + exhibit limits satisfied (no auto-return)? [Y/N]
【Fallback venue】<AEJ or field journal if reject>
【Next step】aeri-submission
```

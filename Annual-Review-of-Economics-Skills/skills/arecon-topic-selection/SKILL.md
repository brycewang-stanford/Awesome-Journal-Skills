---
name: arecon-topic-selection
description: Use when judging whether a literature is an Annual Review of Economics (ARE)-scale review topic — mature, important, and genuinely in need of an authoritative, accessible synthesis — and framing the review's animating question. Decides fit; it does not gather the literature (arecon-literature-synthesis).
---

# Topic Selection for an ARE Review (arecon-topic-selection)

## When to trigger

- You have a candidate field and need to know if it is "ARE-shaped"
- A topic feels either too narrow (a single-question review) or too sprawling (a whole subfield)
- You are deciding between ARE and a sibling outlet (JEL, JEP, a Handbook chapter, a field journal's review section)
- The literature is young/fast-moving and you suspect it is not yet ready for an annual-volume review

## What ARE is for

ARE is the **Annual Reviews** economics survey series: a yearly volume of **invited, authoritative review articles** that are **accessible to economists outside the subfield**, not only to its specialists. The reader is a competent economist who wants to enter, teach, or locate the open questions of a field they do not currently work in. That reader profile — and the annual-volume cadence — sets the fit bar.

## The four ARE-fit tests

A literature belongs in ARE when it passes all four. If it fails one, route accordingly.

1. **Maturity.** There is a *body* of research — multiple research lines, accumulated evidence, recognizable debates — not a handful of recent working papers. A field still being born produces a *premature* review that dates within a volume cycle. (Fails → too young; wait.)
2. **Broad importance.** The questions matter to economists generally, not only to a dozen specialists. ARE explicitly serves **adjacent economists**; a review that only its own subfield could love is a field-journal review, not an ARE article. (Fails → too niche.)
3. **Need for an accessible synthesis.** A newcomer cannot currently get oriented without a guide, *and* existing entry points (a recent JEL survey, a Handbook chapter) have not already done the job. The value is the **accessible map**, not the **list**. (Fails → already synthesized; nothing to add.)
4. **Tractable for ~25–40 pages.** ARE reviews are substantial but not Handbook-length (检索于 2026-06；以官网为准). One author/team must read and weigh the relevant literature within that envelope. (Fails → carve a coherent axis, or it is a Handbook chapter.)

## Decision table

| Situation | Verdict | Action |
|-----------|---------|--------|
| Mature, broadly important, needs accessible synthesis, fits ~25–40 pp | ARE-shaped | → `arecon-proposal-framing` |
| Important but immature | Not yet | revisit in a volume or two |
| Mature but narrow / specialist-only | Wrong venue | field-journal review section |
| Mature, important, but enormous and exhaustive | Wrong venue | Handbook chapter or JEL (deeper, longer) |
| Non-technical, policy-facing, short, lay-adjacent | Wrong venue | Journal of Economic Perspectives (JEP) |

## Framing the animating question

An ARE review is organized by a **question about the field**, not by a topic label. Before approaching the Committee, write one sentence of each:

- **State-of-knowledge question:** "What do we now know about X, and how confident should we be?"
- **Why now:** what makes a synthesis valuable *for this volume* — a wave of new evidence, a methodological shift, a policy debate, convergence or fracture of findings.
- **Reader payoff:** what an economist from an adjacent field can *do* after reading (enter the field, teach it, locate the open questions).

## Checklist

- [ ] The field passes all four fit tests (maturity, broad importance, need, ~25–40 pp tractability)
- [ ] The animating *question about the field* is written in one sentence
- [ ] The "why now" is concrete (new evidence / method shift / policy salience), not "no one has reviewed this"
- [ ] The intended reader is the **adjacent / non-specialist economist**, and the payoff is stated
- [ ] You can name the 3–6 research lines the review must cover (a coverage skeleton)
- [ ] Checked it is not a JEP piece (non-technical, broad), a JEL survey (deeper/longer), or a Handbook chapter (exhaustive)
- [ ] You are *not* the field's only contributor — the review will not become a self-retrospective

## Anti-patterns

- "No one has reviewed X" used as the *sole* justification — absence is not importance
- Reviewing your own research program under a neutral title (self-promotion; ARE referees punish this)
- Picking a field so new the review freezes a moving target before the volume prints
- A scope so broad it becomes a Handbook chapter; so narrow it is a field-journal review
- Confusing "topic" (a label) with "animating question" (what the review argues about the field)
- Planning to submit cold — ARE does not take unsolicited manuscripts (see `arecon-proposal-framing`)

## Output format

```text
【Field】<the literature>
【Four tests】maturity / broad-importance / need-for-synthesis / ~25–40pp-tractable — pass or fail each
【Animating question】"What do we know about ___, and how sure are we?"
【Why now】<new evidence / method shift / policy salience>
【Reader payoff】<what an adjacent economist can do after reading>
【Coverage skeleton】<3–6 research lines the review must cover>
【Verdict】ARE-shaped / rescope / wrong-venue (→ JEL / JEP / Handbook / field review)
【Source status】verified URL / 待核实 / not asserted
【Next step】→ arecon-proposal-framing (get the topic to the Editorial Committee)
```

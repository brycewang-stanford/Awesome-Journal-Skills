---
name: jel-topic-selection
description: Use when judging whether a literature is a Journal of Economic Literature (JEL)-scale survey topic — mature, important, and genuinely in need of synthesis — rather than a narrow review. Decides fit and frames the survey's animating question; it does not gather or synthesize the literature (that is jel-literature-synthesis).
---

# Topic Selection for a JEL Survey (jel-topic-selection)

## When to trigger

- You have a candidate field and need to know if it is "JEL-shaped"
- A topic feels either too narrow (a single-question review) or too sprawling (a whole subfield)
- You are deciding between JEL and a sibling outlet (JEP, Annual Review of Economics, a field journal's review section)
- The literature is young/fast-moving and you suspect it is not yet mature enough to survey

## The four JEL-fit tests

A literature belongs in JEL when it passes all four. If it fails one, route accordingly.

1. **Maturity.** There is a *body* of research — multiple research lines, accumulated evidence, recognizable debates — not a handful of recent working papers. A field that is still being born produces a *premature* survey that will date in a year. (Fails → too young; wait, or pitch JEP instead.)
2. **Importance.** The questions matter to economists broadly, not only to a dozen specialists. A JEL reader is a *non-specialist economist* who should finish the survey understanding why the field exists and what it has settled. (Fails → too niche; a field journal's review section fits better.)
3. **Need for synthesis.** The literature is *scattered, contradictory, or hard to enter* — a competent newcomer cannot currently get oriented without a guide. The survey's value is the **map**, not the **list**. (Fails → already well-synthesized; nothing to add.)
4. **Tractable scope.** One author/team can plausibly read and weigh the *whole* relevant literature in a single article. JEL surveys are long but not infinite. (Fails → carve a coherent sub-field, or split into two surveys.)

## Decision table

| Situation | Verdict | Action |
|-----------|---------|--------|
| Mature, important, scattered, tractable | JEL-shaped | → `jel-proposal-and-commissioning` |
| Important but immature | Not yet | revisit in 2–3 years; consider JEP perspective |
| Mature but narrow / specialist | Wrong venue | field-journal review section |
| Mature, important, but enormous | Rescope | pick a coherent axis; → `jel-organizing-framework` to test the cut |
| Non-technical, broad-audience, short | Wrong venue | Journal of Economic Perspectives (JEP) |

## Framing the animating question

A JEL survey is organized by a **question about the field**, not by a topic label. Before proposing, write one sentence of each:

- **The state-of-knowledge question**: "What do we now know about X, and how confident should we be?"
- **The why-now**: what makes a synthesis valuable *at this moment* (a wave of new evidence, a methodological shift, a policy debate, convergence or fracture of findings).
- **The reader's payoff**: what a non-specialist economist can *do* after reading (enter the field, teach it, locate the open questions).

## Checklist

- [ ] The field passes all four fit tests (maturity, importance, need, tractable scope)
- [ ] The animating *question about the field* is written in one sentence
- [ ] The "why now" is concrete (new evidence / method shift / policy salience), not "no one has surveyed this"
- [ ] The intended reader is the **non-specialist economist**, and the payoff is stated
- [ ] You can name the 3–6 research lines the survey must cover (a coverage skeleton)
- [ ] Checked it is not a JEP piece (too short/non-technical) or a field-review piece (too narrow)
- [ ] You are *not* the only contributor to this literature — the survey will not be a self-retrospective

## Anti-patterns

- "No one has written a survey of X" used as the *sole* justification — absence is not importance
- Surveying your own research program under a neutral-sounding title (self-promotion; JEL referees punish this hard)
- Picking a field so new that the survey freezes a moving target
- A scope so broad the article becomes a list; a scope so narrow it is a field-journal review
- Confusing "topic" (a label) with "animating question" (what the survey argues about the field)

## Output format

```
【Field】<the literature>
【Four tests】maturity / importance / need-for-synthesis / tractable-scope — pass or fail each
【Animating question】"What do we know about ___, and how sure are we?"
【Why now】<new evidence / method shift / policy salience>
【Reader payoff】<what a non-specialist can do after reading>
【Coverage skeleton】<3–6 research lines the survey must cover>
【Verdict】JEL-shaped / rescope / wrong-venue (→ which venue)
【Next step】→ jel-proposal-and-commissioning (pitch the ~10-page sketch to the editor)
```

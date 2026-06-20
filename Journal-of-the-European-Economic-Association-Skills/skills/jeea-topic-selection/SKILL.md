---
name: jeea-topic-selection
description: Use when deciding whether a question fits the Journal of the European Economic Association (JEEA) rather than a field journal or a sibling general-interest outlet for a JEEA manuscript. Tests general-interest fit and sharpens the question; it does not design the empirics or model.
---

# Topic Selection & Fit (jeea-topic-selection)

## When to trigger

- The question feels important within one subfield but you are unsure it travels
- You are choosing between JEEA, *The Economic Journal*, the *European Economic Review*, a field journal, or a top-5
- A draft answers a narrow technical question with no broad lesson
- A co-author asks "is this a JEEA paper?"

## The JEEA fit bar

JEEA is the **EEA's general-interest journal** for high-quality theoretical and empirical economics. The bar is **general interest at a high theory-and-empirics standard**: a paper must matter to a broad economics readership, not only to specialists in its subfield. JEEA is genuinely **field-agnostic** — micro and macro theory, applied econometrics, applied micro, finance, development, public all appear — so what discriminates is not the field but whether the **lesson generalizes** and whether the **execution clears a strong methodological bar** for either a credible empirical design or a disciplined model.

Two questions decide fit:
1. **Does the lesson travel?** State the take-away in one sentence a non-specialist economist would find surprising or consequential. If the sentence only lands for subfield insiders, it is a field-journal paper.
2. **Does the execution clear the bar?** A clean, defensible identification (empirical) **or** a model whose assumptions are disciplined and whose result is sharp (theory/structural). General interest without rigor is a magazine piece; rigor without general interest is a field paper.

## Fit decision table

| Situation | Likely home | Why |
|-----------|-------------|-----|
| Broad lesson + clean identification or sharp model | **JEEA** | the general-interest sweet spot |
| Broad lesson but execution is preliminary | revise first (`jeea-identification` / `jeea-theory-model`), then JEEA | the bar is the obstacle, not the topic |
| Rigorous but the lesson is subfield-only | a strong field journal | general interest is missing |
| New estimator with a toy application | an econometrics field journal | method-first, not question-first |
| Top-5-or-bust ambition with marginal novelty | calibrate (JEEA is a strong, faster home) | `jeea-referee-strategy` |

## Sibling discrimination (do not target the wrong European outlet)

- **vs. *The Economic Journal* (RES):** both are broad European outlets; JEEA carries the EEA association-journal identity with a strong theory+empirics bar. Pick by where the lesson and the execution genuinely land.
- **vs. *European Economic Review* (EER):** EER is broad-scope but typically less of a top-tier general-interest gatekeeper; JEEA aims higher on the general-interest novelty bar.
- **vs. top-5:** JEEA is a strong European general-interest home **below** the top-5 — a realistic, faster home for a paper with a genuine general-interest lesson that is not quite a top-5 swing.

## The two-minute fit triage

Before any deeper work, run this quick triage to avoid building toward the wrong venue:

1. **State the lesson in one sentence** to a colleague in a different subfield. If they shrug, the general-interest hook is missing.
2. **Name the execution path** — empirical design or model — and ask whether it is already at, or can reach, a strong bar.
3. **Name the closest competitor venue** honestly (EJ, EER, field, top-5) and the reason JEEA wins or loses against it.

If 1 and 2 both pass, JEEA is in play; if only 2 passes, the topic is a field paper; if only 1 passes, the execution is the obstacle, not the venue.

## Checklist

- [ ] One-sentence lesson written; a non-specialist would find it surprising or consequential
- [ ] Field is irrelevant to the decision — fit rests on generality + rigor, not subfield prestige
- [ ] Execution path chosen: credible empirical design **or** disciplined model (route to `jeea-identification` / `jeea-theory-model`)
- [ ] Sibling check done (JEEA vs. EJ / EER / field / top-5) with an honest reason
- [ ] The contribution is an **answer or a result**, not a method demonstration

## Worked vignette (illustrative)

A draft is titled "Bank Branch Closures and Small-Firm Credit in [one country], 2010–2018." As framed, it is a banking-field paper. The JEEA-grade reframe asks the travel test: what general lesson does the closure shock teach? The revision leads with "When physical bank access disappears, which firms lose credit — and does soft information explain it?" The closure is now an instrument for a general question about relationship lending and information frictions, with a lesson that travels to any economy digitizing its banking. Same data, JEEA-shaped question.

## Anti-patterns

- Selling subfield depth ("the most complete treatment of X in setting Y") where a general reader sees no broad lesson
- Pitching JEEA as a consolation top-5 reject without re-framing the general-interest contribution
- A purely methodological paper with a toy application (econometrics-field-shaped, not JEEA-shaped)
- Assuming "European topic" = JEEA fit — geography is not the criterion; generality is
- Choosing the venue before the question is sharp — fit follows the lesson, not the other way around

## Output format

```
【One-sentence lesson】[does it travel beyond the subfield? Y/N]
【Field】[any — not the deciding factor]
【Execution path】empirical design / theory model / structural-quantitative
【JEEA vs siblings】[JEEA / EJ / EER / field / top-5] + reason
【General-interest verdict】[fit / revise-then-fit / wrong venue]
【Next step】jeea-literature-positioning
```

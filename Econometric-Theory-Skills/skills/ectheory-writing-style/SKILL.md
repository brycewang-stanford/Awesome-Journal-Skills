---
name: ectheory-writing-style
description: Use to polish the prose, notation, and proof exposition of an Econometric Theory (ET) manuscript — theorem-proof clarity, consistent notation, APA author-date references, and ET manuscript-prep specs (11pt, 1.5 spacing, 1.25in margins, 200-word abstract, 40-char running head).
---

# Writing & Proof Style (ectheory-writing-style)

## When to trigger

- The math is correct but the proof reads as a wall of symbols
- Notation drifts or collides across sections, assumptions, and theorems
- Formatting the manuscript to ET's preparation specs before submission
- Converting references to ET's APA author-date style

## ET house style: rigorous and readable

ET expects **rigorous theorem-proof writing that a fellow theorist can follow without
reverse-engineering every step**. Aim for:

- **Theorem-environment discipline.** Number and label Assumptions, Lemmas, Propositions, Theorems,
  Corollaries consistently; reference them by number, not "the result above."
- **Proof roadmaps.** Open each nontrivial proof with one or two sentences on the strategy, then
  execute; isolate reusable steps as lemmas; name the probabilistic tool at the point you invoke it.
- **Notation hygiene.** One symbol, one meaning; introduce notation before use; keep a consistent
  convention for estimators, true values, limits, and rates. A short notation table helps in long
  papers.
- **Calibrated prose.** State assumptions in words alongside the formalism; explain *why* a condition
  is needed, not only *that* it holds.

## ET manuscript-preparation specs (current 2026 page)

- **Font/spacing/margins:** minimum **11-point** font, at least **1.5 line spacing**, margins no
  less than **1.25 inches** on all sides; pages consecutively numbered.
- **Abstract:** **no more than 200 words.** (A legacy page showed 150 words / 10pt; treat the current
  200-word / 11pt figures as authoritative — verify on the live page.)
- **Title page (p.1):** title, author name(s), affiliations, emails, title/author footnotes as
  superscripts.
- **Page 2:** proposed **running head** (abbreviated title, **no more than 40 characters**),
  corresponding author for proofs, and the abstract.
- **References:** follow the **APA Style Guide** (author-date), in-text and in the reference list.

## Checklist

- [ ] Assumptions/lemmas/theorems numbered and cross-referenced by number
- [ ] Each nontrivial proof opens with a strategy roadmap
- [ ] Notation consistent; every symbol introduced before use
- [ ] Assumptions explained in words, not only stated formally
- [ ] Abstract <=200 words; running head <=40 characters
- [ ] 11pt, >=1.5 spacing, >=1.25in margins, pages numbered
- [ ] References in APA author-date; list complete and alphabetized

## Anti-patterns

- A proof with no roadmap that forces the reader to infer the strategy from the algebra
- Reusing a symbol for two different objects across sections
- Stating regularity conditions with no intuition for why they are imposed
- An abstract over 200 words or a running head over 40 characters
- Numeric or Chicago references instead of APA author-date


## Style execution pass for Econometric Theory

Treat this skill as an executable review pass, not a prose hint. First lock the primitive assumptions, theorem statement, proof route, and example showing why the result matters; then judge whether the current manuscript answers the venue's real reader: econometric theorists who read for assumptions, theorem novelty, proof architecture, and relation to known asymptotics.

- **Do the pass:** Rewrite the first two pages so each paragraph starts from the venue-level claim, not from chronology or method inventory; preserve exact source-map limits and move technical overflow to appendix or supplement.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Journal of Econometrics for applied-method reach, Quantitative Economics for theoretical economics, Econometrica for general theory-plus-economics contribution; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Proof exposition】roadmaps + isolated lemmas? [Y/N]
【Notation】one-symbol-one-meaning, introduced before use? [Y/N]
【Abstract】<=200 words? [Y/N]  【Running head】<=40 chars? [Y/N]
【Prep specs】11pt / 1.5 spacing / 1.25in margins? [Y/N]
【References】APA author-date, alphabetized? [Y/N]
【Next step】ectheory-replication-and-data-policy
```

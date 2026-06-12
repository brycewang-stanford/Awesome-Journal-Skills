---
name: ectheory-literature-positioning
description: Use to stake an Econometric Theory (ET) contribution against the existing theory frontier — which assumptions you weaken, which limit result you generalize, what was previously unproven — using APA author-date citations, not a standalone literature survey.
---

# Literature Positioning (ectheory-literature-positioning)

## When to trigger

- The introduction lists prior papers without saying precisely what is *new* in your theorem
- A referee might ask "isn't this a special case of X?" and you have no crisp answer
- You need to show your regularity conditions are weaker (or your environment broader) than prior work
- Setting up the citation apparatus in ET's **APA author-date** style

## How ET positioning differs

ET is a theory journal: positioning is **theorem-to-theorem**, not "gap in the empirical
literature." The reader is an econometric theorist who will immediately map your result onto the
known limit theory. Your job is to locate your contribution on that lattice precisely:

1. **Name the closest prior result** and its assumptions/scope exactly.
2. **State the delta** in one sentence: weaker moment conditions, dependent vs i.i.d. data,
   nonstationary vs stationary, fixed vs growing dimension, sharp vs conservative inference, etc.
3. **Say what was previously unproven or only conjectured** that you now prove.
4. **Acknowledge concurrent/overlapping work** fairly — in a small theory community, the editors and
   referees usually know it.

Because reviewers see your identity (single-anonymous review), self-citation is fine, but frame the
new contribution on its merits, not as "our prior work."

## Citation mechanics (ET house style)

- References and in-text citation follow the **APA Style Guide** (author-date), e.g.,
  "(Phillips, 1987)" / "Phillips (1987) shows" — **not** numeric or footnote styles.
- Reference list alphabetical by surname; keep it complete and accurate (theory readers check).
- Cite the canonical limit-theory sources you actually use (LLN/CLT, FCLT, empirical-process,
  mixing/NED) rather than gesturing at a textbook.

## Checklist

- [ ] Closest prior theorem named with its exact assumptions/scope
- [ ] The "delta" (what you weaken/generalize/prove) stated in one sentence
- [ ] Previously unproven/conjectured element identified and claimed
- [ ] Concurrent work acknowledged
- [ ] All citations in APA author-date; reference list complete and alphabetized

## Anti-patterns

- A standalone "Literature Review" section that surveys without positioning the theorem
- Vague novelty ("we extend the literature") with no stated change in assumptions or scope
- Overclaiming priority where a known result already covers your case
- Mixed or numeric citation styles instead of clean APA author-date

## Locating the theorem on the limit-theory lattice

ET positioning is theorem-to-theorem on a known lattice of asymptotic results, not a survey of an empirical
gap. Each row is a dimension along which a new result can dominate prior limit theory.

| Lattice dimension | Prior result's position | Your delta (one-sentence claim) |
| --- | --- | --- |
| Dependence | i.i.d. innovations | mixing / NED / martingale-difference array |
| Stationarity | stationary, fixed root | nonstationary / local-to-unity / cointegrated |
| Dimension | fixed p | p growing with n, uniform over the model |

If your delta does not move the result along a dimension, a referee will ask "isn't this a special case of
X?" — routing you back to `ectheory-topic-selection`. The fixes: "isn't this a special case?" → state the
closest prior result with its assumptions, then the labelled dimension you relax, showing it as your
corollary; "concurrent work proves this" → acknowledge by author-date and name the differentiating
dimension. In the ET tradition positioning is "what limiting law, under what weakened conditions, was
previously unproven"; confirm the live APA-style requirement against the author guidelines if uncertain.


## Positioning pass for Econometric Theory

Treat this skill as an executable review pass, not a prose hint. First lock the primitive assumptions, theorem statement, proof route, and example showing why the result matters; then judge whether the current manuscript answers the venue's real reader: econometric theorists who read for assumptions, theorem novelty, proof architecture, and relation to known asymptotics.

- **Do the pass:** Build a three-column map: incumbent conversation, unresolved tension, and this manuscript's delta; include one sibling-venue omission that would make a referee doubt the fit.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Journal of Econometrics for applied-method reach, Quantitative Economics for theoretical economics, Econometrica for general theory-plus-economics contribution; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Closest prior result】author (year) + its assumptions/scope
【Delta】what you weaken / generalize / prove (one sentence)
【Previously unproven】the element you now establish
【Concurrent work】acknowledged? [Y/N]
【Citations】APA author-date, list alphabetized? [Y/N]
【Next step】ectheory-identification-strategy
```

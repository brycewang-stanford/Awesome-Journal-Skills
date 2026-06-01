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

## Output format

```
【Closest prior result】author (year) + its assumptions/scope
【Delta】what you weaken / generalize / prove (one sentence)
【Previously unproven】the element you now establish
【Concurrent work】acknowledged? [Y/N]
【Citations】APA author-date, list alphabetized? [Y/N]
【Next step】ectheory-identification-strategy
```

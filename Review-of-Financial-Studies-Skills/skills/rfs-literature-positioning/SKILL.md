---
name: rfs-literature-positioning
description: Use when the related-work framing is the bottleneck for a The Review of Financial Studies (RFS) manuscript — defining the precise delta against JF/JFE/RFS and prior literature. Builds positioning, not the empirical design or the topic itself.
---

# Literature Positioning (rfs-literature-positioning)

## When to trigger

- The related-work section is a list ("X did A, Y did B") with no synthesis
- You cannot state your contribution as a single crisp delta
- A reader asks "how is this different from [recent RFS/JF/JFE paper]?"
- The novelty claim from `rfs-topic-selection` needs to be defended against the literature

## How RFS reviewers read positioning

RFS referees and editors are typically the authors of the papers you cite. Positioning is judged on whether you (1) know the *current* frontier, (2) cite the right primary sources rather than secondary surveys, and (3) state a delta that is real and defensible — not rhetorical.

The contribution must clear two bars simultaneously:
- **Against the literature** — what do we now know that we did not before?
- **Against the closest 2–3 papers** — what specifically do you do that they could not?

## Positioning structure

Organize related work by **the question**, not chronologically:

1. **The anchor literatures** — name the 2–4 strands you sit at the intersection of (e.g., intermediary asset pricing × household finance). Cite the canonical theory and the most-cited recent empirics.
2. **The frontier** — the 3–5 most recent, most relevant papers (last ~3 years). Show you know what is in the pipeline.
3. **The wedge** — one paragraph that names the closest paper(s) and states the precise gap: data they lacked, identification they could not achieve, mechanism they could not test, or theory they did not have.
4. **Your delta** — one or two sentences, falsifiable: "We are the first to [X], which lets us [Y]."

## Delta types that work at RFS

| Delta type            | Example phrasing                                                       |
|-----------------------|-------------------------------------------------------------------------|
| New question          | "Prior work studies pricing; we study the *allocation* consequences."   |
| Cleaner identification| "Earlier estimates were confounded by selection; our shock breaks it."  |
| New mechanism evidence| "The correlation was known; we provide the first direct test of *why*." |
| Theory + evidence     | "We embed the fact in a model that yields a new, tested prediction."    |
| New data              | "We observe [previously unobservable margin], revising prior estimates."|

## Citing across the top-3 and field journals
- Cite the primary RFS/JF/JFE source for each claim, not a later survey that summarizes it.
- When a result first appeared in a field journal but the framing is now at the top-3, cite both.
- For theory anchors, cite the foundational paper even if decades old — referees expect it.
- Distinguish "first to document" from "first to explain" — over-claiming either is easily disproven.

## Checklist

- [ ] Related work is organized by question/theme, not by author or date
- [ ] The 2–3 closest papers are named explicitly and the delta vs. each is stated
- [ ] Recent (last ~3 years) RFS/JF/JFE work is cited — not just classics
- [ ] Canonical theory references for each anchor literature are present
- [ ] The delta is falsifiable, not "we add to the literature on X"
- [ ] You have not overstated novelty in a way a referee can disprove with one cite

## Anti-patterns

- A laundry-list literature review with no synthesis or wedge.
- Citing surveys/handbooks instead of the primary papers a referee wrote.
- Missing an obvious close competitor — reads as either ignorance or evasion.
- A delta phrased as "to the best of our knowledge, we are the first" with no defense.
- Positioning against field journals when the real competitors are at RFS/JF/JFE.

## Output format

```
【Anchor literatures】[strand 1] × [strand 2] (+ canonical theory cites)
【Frontier papers】[3–5 recent JF/JFE/RFS papers]
【Closest competitors】[paper] → our delta vs. each
【One-sentence delta】"We are the first to ... which lets us ..."
【Open risk】a competitor a referee might raise
【Next step】rfs-identification
```

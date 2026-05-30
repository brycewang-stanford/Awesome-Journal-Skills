---
name: jf-literature-positioning
description: Use when the introduction and related-work sections of a The Journal of Finance (JF) manuscript fail to state a crisp marginal contribution against the finance literature. Positions the paper; it does not survey it.
---

# Literature Positioning & Contribution (jf-literature-positioning)

## When to trigger

- The related-work section is a chronological list ("X (2015) finds… Y (2018) finds…")
- A reader cannot tell in one paragraph what is new relative to the closest papers
- The intro cites broadly but never names the 3–5 papers it actually builds on / departs from
- A referee is likely to say "this is already in [well-known paper]"

## JF norm: position, do not survey

JF introductions are short and lead with the question and finding. The literature is woven into the **contribution paragraph(s)** of the introduction, not parked in a long standalone "Literature Review" chapter. A general-interest reader should leave the introduction knowing: the question, the answer, the magnitude, and exactly how it differs from the closest work.

## Contribution-paragraph template

Write 2–4 sentences, each pinning the paper to a strand:

> "We contribute to the literature on **[strand 1]** (e.g., [Anchor1], [Anchor2]). Those papers establish [X]; we show [the new thing], using [the new variation / data / test]. We also speak to **[strand 2]** … by [the second contribution]."

Rules:
- Name the **closest** papers, not a citation dump. JF rewards precision over breadth here.
- For each strand, state what prior work established **and** the specific delta you add.
- Distinguish a **new fact**, a **new mechanism/identification**, and a **new method** — say which one you are claiming.

## Coverage map (fill before drafting)

| Strand the paper touches | Anchor papers (closest 2–3) | What they show | Your delta |
|--------------------------|------------------------------|----------------|------------|
| Primary strand           |                              |                |            |
| Secondary strand         |                              |                |            |
| Method / data strand     |                              |                |            |

## Checklist

- [ ] The contribution paragraph names the closest 3–5 papers, not 30
- [ ] For each strand: prior result + your specific delta is stated
- [ ] You classify the contribution: new fact vs. new mechanism vs. new method
- [ ] You have pre-empted the "already known" objection by citing the nearest rival and distinguishing it
- [ ] Foundational asset-pricing / corporate-finance references are present where relevant (e.g., Fama–French factor work; the multiple-testing critique in cross-sectional asset pricing — Harvey, Liu & Zhu, "…and the Cross-Section of Expected Returns")
- [ ] Recent JF/JFE/RFS papers on the exact topic are cited (editors notice omissions of their own journal)
- [ ] No self-citation padding; no citing only your own working papers

## Anti-patterns

- A chronological literature list with no synthesis or delta
- Citing a survey instead of the primary papers a referee will have in mind
- Omitting the obvious nearest rival (reads as either ignorance or evasion)
- "To the best of our knowledge, no paper has…" without having checked recent JF/JFE/RFS issues
- Claiming a "new method" when it is a standard estimator applied to new data

## Output format

```
【Primary strand / anchors】...
【Marginal contribution (1 sentence)】...
【Contribution type】new fact / new mechanism / new method
【Nearest rival pre-empted?】yes / no — [paper]
【Missing key cites】[...]
【Next step】jf-identification (corporate/empirical) or jf-empirical-design (asset pricing)
```

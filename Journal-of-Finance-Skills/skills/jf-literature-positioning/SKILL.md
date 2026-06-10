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

JF introductions are short and lead with the question and finding. The literature is woven into the **contribution paragraph(s)**, not parked in a standalone "Literature Review" chapter. A general-interest AFA reader should leave the introduction knowing the question, the answer, the magnitude, and exactly how it differs from the closest work.

## Engage JF's own canon

JF has published much of finance's foundational work; reviewers expect you to engage the right anchors and **attribute to the correct top-3 journal**:
- **Sharpe (1964)** CAPM — JF.
- **Jensen (1968)** mutual-fund performance — JF.
- **Fama & French (1992)**, "The Cross-Section of Expected Stock Returns" — **JF**.
- **Jegadeesh & Titman (1993)**, momentum — **JF**.
- **Carhart (1997)**, four-factor mutual-fund persistence — **JF**.
- Caution: the **Fama–French three-factor model (1993) is in JFE, not JF** — cite it to JFE. Mis-attributing canon to the wrong top-3 journal signals carelessness to JF editors.

## Contribution-paragraph template

> "We contribute to the literature on **[strand 1]** ([Anchor1], [Anchor2]). Those papers establish [X]; we show [the new thing], using [the new variation / data / test]. We also speak to **[strand 2]** … by [the second contribution]."

Rules: name the **closest** papers, not a dump; for each strand state prior result **and** your specific delta; classify the contribution as a **new fact, new mechanism/identification, or new method**.

## Contribution-type decision table

Editors and AEs read the contribution paragraph to classify what is new. Force the paper into one primary type — claiming all three reads as none:

| Contribution type     | What you must show                                  | The attack to pre-empt                              |
|-----------------------|-----------------------------------------------------|-----------------------------------------------------|
| New fact              | A robust regularity not previously documented       | "This is already in [closest paper]"                |
| New mechanism / identification | A clean shock or instrument isolating *why*  | "Correlation, not causation" / "weak design"        |
| New method            | A genuinely new estimator or test, not a relabel    | "This is a standard estimator on new data"          |

State the type explicitly; the editor uses it to judge whether the step over the closest work is flagship-sized.

## Worked vignette — positioning against the canon

*Illustrative.* A paper finds a supply-chain-concentration return premium. The weak version: "Many papers study the cross-section; we add a predictor." The JF version names the bar (Fama & French 1992, JF; the factor-zoo literature, Harvey, Liu & Zhu, JF), names the closest paper ([X, recent JF] prices *customer* risk), and states the delta: we isolate *supplier* concentration, show it survives their controls (a **new fact**) and concentrates where arbitrage is costly (a **mechanism**). FF 1992 cites to JF, the three-factor model to JFE — mis-routing canon reads as carelessness to JF editors.

### Referee-pushback patterns and the JF-specific fix
| Pushback you will hear                              | JF-specific fix                                                 |
|----------------------------------------------------|-----------------------------------------------------------------|
| "This is already in [well-known paper]"            | Name it, state its result, give your precise delta              |
| "You ignore the recent JF paper on this"           | Add it — editors notice omissions of their own journal          |

## Calibration anchors
- JF introductions **position, not survey** — literature woven into the contribution paragraph, not a standalone review. The nearest rivals shift; confirm against recent issues.

## Checklist

- [ ] Contribution paragraph names the closest 3–5 papers, not 30
- [ ] For each strand: prior result + your specific delta
- [ ] Contribution classified: new fact vs. mechanism vs. method
- [ ] Nearest rival pre-empted (cited and distinguished)
- [ ] Foundational JF/JFE references present and attributed to the correct journal (e.g., FF 1992 = JF; FF three-factor 1993 = JFE)
- [ ] The multiple-testing critique in cross-sectional asset pricing (Harvey, Liu & Zhu) cited where relevant
- [ ] Recent JF papers on the exact topic cited (editors notice omissions of their own journal)

## Anti-patterns

- A chronological list with no synthesis or delta
- Citing a survey instead of the primary papers a referee has in mind
- Mis-attributing canon (e.g., the FF three-factor model) to JF instead of JFE
- "To the best of our knowledge…" without checking recent JF issues
- Claiming a "new method" when it is a standard estimator on new data

## Output format

```
【Primary strand / anchors】...
【Marginal contribution (1 sentence)】...
【Contribution type】new fact / new mechanism / new method
【Nearest rival pre-empted?】yes / no — [paper]
【Canon attributed to correct journal?】yes / no
【Next step】jf-identification (corporate/empirical) or jf-empirical-design (asset pricing)
```

---
name: aej-applied-economics
description: Use when targeting American Economic Journal: Applied Economics or deciding whether an applied micro manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# American Economic Journal: Applied Economics (aej-applied-economics)

## Journal positioning

AEJ: Applied Economics is the American Economic Association's home for empirical applied microeconomics one tier below AER's general-interest bar. It publishes credible, well-identified empirical work — labor, development, health, education, and adjacent applied fields — where the design is clean and the economic magnitudes are meaningful. The contribution can be field-specific rather than discipline-wide, but the identification and execution must be top-quality; this is where excellent applied micro that is "too narrow for AER" belongs.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AEA site and the editorial-manager submission system.

## When to trigger

- The author names AEJ: Applied as the target, or is stepping down from an AER applied-micro submission.
- A paper has a credible quasi-experimental or field-experimental design in labor, development, health, or education with meaningful magnitudes.
- A strong applied paper is excellent but narrower than AER's general-interest bar and needs the right applied home.
- The author needs AEJ: Applied's desk-reject risks and a credible AER / applied-field alternative list.

## Scope & topic fit

- Applied microeconomics with credible causal identification — labor, development, health, education, environment, and household behavior.
- Field experiments (RCTs) and natural/quasi-experiments exploiting policy changes, shocks, or discontinuities.
- Empirical papers whose value is a clean design answering a well-posed applied question, with economically interpretable effects.
- Reduced-form work; lighter on heavy structural modeling than AEJ: Micro or general-interest venues.

## Method & evidence bar

- Identification is the central filter: the design (RCT, DiD, IV, RDD) must be credible and pre-empt the obvious threats by design, not by robustness tables alone.
- Modern estimators and inference are baseline — proper DiD under staggered treatment, valid first stages, RDD density/covariate-smoothness checks, correct standard errors.
- Effects must be economically meaningful, not merely significant; magnitudes, mechanisms, and external validity are evaluated.
- Data and code transparency is mandatory; the AEA data and code availability and verification policy applies, with deposit checked before acceptance.

## Structure & house style

- The introduction states the applied question, the identification strategy, the headline effect and its magnitude, and what we learn that we did not before.
- Lead with the design and the clean estimate; develop mechanism and heterogeneity as support, with secondary analyses in an online appendix.
- AEJ uses an unstructured abstract and JEL codes; robustness and supplementary tables belong in the appendix.
- Exhibits should report magnitudes and let the central estimate be read from one table or figure.

## Official-submission checklist

- Search the live site for "AEJ: Applied Economics submission guidelines" and the AEA "Data and Code Availability Policy," and follow the current versions.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, and figure/table standards on the editorial-manager system.
- Re-check the current data/code deposit and verification workflow (openICPSR / AEA Data Editor), and for RCTs any pre-registration / trial-registry and pre-analysis-plan expectations — enforced before acceptance.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the applied question and why the identification is credible.
- [ ] The contribution is stated as identification + meaningful magnitude, not as statistical significance.
- [ ] The introduction positions the paper against the recent applied-micro frontier on this question.
- [ ] Identification threats are addressed by design; estimators, inference, and (for RCTs) pre-registration are state-of-the-art.
- [ ] Data and code are ready for the AEA availability + verification workflow.

## Common desk-reject triggers

- A correlational or weakly-identified design dressed up as causal.
- Naive TWFE on staggered adoption, weak IV, or RDD without density/covariate diagnostics.
- A statistically significant but economically tiny or uninterpretable effect.
- "First to study X in context Y" with no design advance, mechanism, or generalizable lesson.

## Re-routing decision

- General-interest applied importance → `american-economic-review`; a single crisp result → `aer-insights`.
- Policy-evaluation framing with policy-relevant magnitudes → `aej-economic-policy` or `journal-of-public-economics`.
- Heavy structural / quantitative micro → `aej-microeconomics`; careful measurement / short empirical → `review-of-economics-and-statistics`.
- Field-leading specialist work → the relevant top field journal (`journal-of-labor-economics`, `journal-of-health-economics`, `journal-of-development-economics`).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] American Economic Journal: Applied Economics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification + magnitude clear the applied-micro bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / data-code policy / pre-registration>
[Re-route suggestion] <if not a fit, a better-matched venue>
```

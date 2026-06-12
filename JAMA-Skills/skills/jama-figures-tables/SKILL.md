---
name: jama-figures-tables
description: Use when designing or auditing the figures and tables of a JAMA manuscript, including the required flow diagram, baseline table, and main-result exhibits. Shapes exhibits for JAMA conventions; it does NOT run the statistics or write the abstract.
---

# Figures & Tables (jama-figures-tables)

## When to trigger

- The RCT/review lacks its required flow diagram
- Tables are cluttered, over-numerous, or exceed the journal's exhibit allowance
- The baseline-characteristics table is missing or misused
- A figure shows p-values but not effect sizes / confidence intervals

## The exhibits a JAMA paper usually needs

| Exhibit                                   | Purpose                                                |
|-------------------------------------------|--------------------------------------------------------|
| Flow diagram (CONSORT/PRISMA/STARD)       | Participant or study-selection accounting              |
| Table 1 — baseline characteristics        | Describe groups; show comparability (not significance) |
| Main-outcome table                        | Primary/secondary effects with 95% CIs                 |
| Forest plot (meta-analysis / subgroups)   | Effect sizes + CIs across studies/subgroups            |
| Kaplan-Meier / time-to-event figure       | Survival or event curves with numbers at risk          |

Keep the count within JAMA's current figure/table limit — verify the exact number on the Instructions for Authors page rather than assuming.

## Conventions JAMA expects

- **Flow diagram is mandatory** for RCTs (CONSORT) and systematic reviews (PRISMA). Account for every participant/record: screened, excluded (with reasons), enrolled, analyzed.
- **Table 1 shows comparability, not p-values.** For RCTs, comparing baseline groups with significance tests is discouraged; report characteristics and let randomization speak.
- **Every estimate carries its 95% CI** in figures and tables, not bare p-values.
- **Self-contained exhibits.** Each table/figure stands alone: full title, defined abbreviations in the footnote, units, denominators (n/N), and the analysis population.
- **Kaplan-Meier curves include numbers at risk** beneath the time axis.
- **Forest plots** order studies sensibly, show weights and the pooled estimate with its CI, and report heterogeneity.
- **No chartjunk.** Avoid 3-D bars, truncated axes that exaggerate effects, and dual axes that mislead.
- **Color and accessibility.** Use colorblind-safe palettes; ensure the figure reads in grayscale.

## Checklist

- [ ] Required flow diagram present and reconciles all participants/records
- [ ] Table 1 reports characteristics without inappropriate significance testing (RCT)
- [ ] Every effect estimate shows its 95% CI
- [ ] Each exhibit is self-contained (title, footnotes, abbreviations, units, n/N)
- [ ] KM curves show numbers at risk; forest plots show weights + pooled CI + heterogeneity
- [ ] Total figures + tables within the journal's limit (verify current number)
- [ ] Axes honest (no truncation that exaggerates); palette colorblind-safe
- [ ] No duplication of the same data across a table and a figure

## Anti-patterns

- Submitting an RCT or review with no flow diagram
- P-value-laden Table 1 implying randomization "failed"
- Bars or curves with no confidence intervals
- Truncated y-axis that visually inflates a small effect
- KM plot without numbers at risk
- The same numbers shown in both a table and a figure
- Abbreviations undefined in the footnote


## Worked example: auditing the main exhibits (illustrative)

Vignette (illustrative): a multicenter randomized clinical trial, N = 2,200 adults, time-to-event primary outcome. For the Journal of the American Medical Association, the exhibit set is a CONSORT flow diagram reconciling all 2,200 participants (screened, randomized, analyzed, lost), a Table 1 of baseline characteristics shown without between-group significance tests, a main-outcome table giving the hazard ratio with its 95% CI plus the absolute risk difference, and a Kaplan-Meier figure with numbers at risk beneath the time axis. A bar chart of the primary outcome with no confidence interval, or a truncated y-axis that visually inflates a small effect, is the kind of exhibit a JAMA reviewer sends back.

## Reviewer pushback and the JAMA fix

- "RCT submitted with no flow diagram." Fix: add the CONSORT diagram and reconcile every participant with reasons for exclusion.
- "Table 1 reports p-values (RCT)." Fix: drop the significance tests; show characteristics and let randomization speak.
- "Figure shows p-values, not effect sizes." Fix: display the estimate with its 95% CI on every exhibit.

Calibration anchors (hedge where uncertain): the mandatory flow diagram, p-value-free Table 1 for RCTs, estimate-plus-CI on every exhibit, and numbers-at-risk on KM curves are durable; the exact figure/table allowance is volatile — confirm against current author guidelines.

## Exhibit pass for JAMA

Run this as a concrete capability pass. First lock the clinical question, patient population, estimand or endpoint, safety/ethics issue, and reporting checklist; then test whether the manuscript addresses clinical reviewers who ask whether the evidence changes patient care, policy, or medical decision-making while satisfying reporting standards.

- **Primary move:** For every figure or table, state the patient/study object, denominator, uncertainty display, and the clinical claim it supports.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against NEJM for field-changing clinical medicine, Lancet for global-health breadth, specialty journals for narrower clinical domains; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Flow diagram】present + reconciles / missing
【Table 1 appropriate】yes / no
【All estimates show 95% CI】yes / no
【Exhibit count vs limit】X (limit per author instructions)
【Self-contained exhibits】yes / fixes: ...
【Issues to fix】...
【Next skill】jama-structured-abstract
```

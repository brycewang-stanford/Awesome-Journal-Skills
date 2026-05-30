---
name: quarterly-journal-of-economics
description: Use when targeting Quarterly Journal of Economics (QJE) or deciding whether an economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Quarterly Journal of Economics (quarterly-journal-of-economics)

## Journal positioning

QJE is the Harvard-edited general-interest journal and one of the economics "top-5" (with AER, JPE, Econometrica, REStud). It is the venue for big, important questions answered with clean, often surprising evidence — papers that change how the profession thinks about a first-order economic question, not careful extensions. The editorial culture prizes a sharp, compelling narrative built around a single consequential result; the readership is the whole discipline, so a niche-field framing reads as a miss.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the QJE / Oxford University Press site and the editorial submission system.

## When to trigger

- The author names QJE (or QJE as a top-5 swing) as the target venue.
- A paper has a genuinely big question and a clean natural experiment or compelling new evidence, and the author is choosing among QJE / AER / JPE.
- A strong field paper needs re-framing so the question reads as a discipline-wide "this matters" rather than a within-subfield refinement.
- The author needs QJE's desk-reject risks and a credible top-5 / top-field alternative list.

## Scope & topic fit

- First-order questions across all of economics — development, labor, public, macro-adjacent, political economy, growth, behavioral — selected on importance and general interest.
- Empirical papers built on a clean natural experiment, a striking dataset, or a transparent quasi-experimental design that resolves a long-debated question.
- Papers with a surprising, consequential headline result that reframes a debate.
- Theory and conceptual work when the result is broad and changes the terms of a literature, not a parameterized extension.

## Method & evidence bar

- Importance is the first filter and identification is the second: even excellent identification will not survive if the question is not first-order and general-interest.
- Quasi-experimental designs must pre-empt the obvious threats with design, not robustness tables; modern DiD estimators, valid instruments, and credible RDD diagnostics are baseline.
- The headline result should be large, clean, and economically meaningful — magnitudes that matter, not marginally significant coefficients.
- Data and code transparency is mandatory; the AEA-style data and code availability and verification norms apply, with deposit checked before acceptance.

## Structure & house style

- The introduction must, on its first pages, pose the big question, deliver the surprising result, and explain why the whole profession should care — QJE rewards a tight, almost essayistic narrative arc.
- Lead with the central finding and its magnitude; subordinate mechanism, robustness, and heterogeneity to a disciplined supporting role and an online appendix.
- QJE uses an unstructured abstract and JEL codes; secondary analyses live in an appendix so the main text stays a clean story.
- Exhibits should let a reader grasp the headline result from a single figure or table.

## Official-submission checklist

- Search the live site for "Quarterly Journal of Economics submission guidelines" and the data and code availability policy, and follow the current OUP / editorial versions.
- Re-check the submission fee, formatting, abstract/JEL requirements, anonymization expectations, and figure/table standards on the submission system.
- Re-check the current data/code deposit and verification workflow (replication package, openICPSR-style archive) — confirm it is enforced before acceptance.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this is a big, first-order question every economist would recognize as important.
- [ ] The contribution is stated as a surprising, consequential result, not as statistical significance.
- [ ] The introduction positions the paper against the current top-5 frontier and the debate it resolves.
- [ ] Identification threats are addressed by design; the headline magnitude is large and clean.
- [ ] Data and code are ready for the availability + verification workflow.

## Common desk-reject triggers

- A technically clean paper on a question the editors judge narrow or not general-interest.
- A small or fragile headline effect that does not feel consequential, however well-identified.
- "First to study X in context Y" framing with no surprising result or conceptual payoff.
- Identification the profession no longer accepts (naive TWFE on staggered adoption, weak IV, cosmetic RDD).

## Re-routing decision

- General-interest but a better fit elsewhere in the top-5 → `american-economic-review` (broad importance) or `journal-of-political-economy` (tight price-theory logic).
- Excellent but narrower applied micro → `aej-applied-economics` or `review-of-economics-and-statistics`; policy-facing → `aej-economic-policy`.
- One crisp, single-result idea → `aer-insights`; macro/growth → `aej-macroeconomics`.
- Field-leading specialist work → the relevant top field journal (`journal-of-labor-economics`, `journal-of-development-economics`, `journal-of-public-economics`).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Quarterly Journal of Economics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the question's importance + identification clear QJE's general-interest bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / data-code policy / exhibits>
[Re-route suggestion] <if not a fit, a better-matched venue>
```

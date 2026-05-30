---
name: european-economic-review
description: Use when targeting European Economic Review (EER) or deciding whether a general-economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# European Economic Review (european-economic-review)

## Journal positioning

EER is a long-standing general-economics journal historically associated with the European economics community, publishing across all fields — micro, macro, labor, public, IO, trade, development — in both theory and empirics. It is a strong general field journal: it wants a clear question, a sound method, and a result that is interesting to economists beyond the immediate subfield, without requiring the discipline-wide reach of a top-5. The readership is broad, so framing should be general-economics rather than narrowly specialist.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Elsevier site and the editorial submission system.

## When to trigger

- The author names EER as the target venue, or wants a broad general-economics home below the top-5.
- A solid paper of general interest needs a venue that takes both theory and empirics seriously across fields.
- A field paper needs re-framing so its contribution reads as broadly interesting economics rather than niche.
- The author needs EER's desk-reject risks and a credible general / European alternative list.

## Scope & topic fit

- General economics across all fields: theory, applied micro, macro, public, labor, IO, trade, development, behavioral.
- Both rigorous theory papers and credible empirical papers are in scope; methodological breadth is a feature.
- Papers with a clear economic question whose interest extends beyond a single specialist community.
- Policy-relevant and European-context work is welcome but must carry a general-economics contribution, not just local description.

## Method & evidence bar

- Empirical papers need a defensible identification strategy; correlation framed as a causal effect without design is a fast rejection.
- Theory papers need clearly stated assumptions and results that are general and consequential, not a narrow extension.
- Standard modern rigor applies: appropriate estimators, correct inference, and pre-empted confounders for empirical work; clean proofs for theory.
- The contribution should be legible to a general economist, with mechanism and interpretation, not only significant coefficients.

## Structure & house style

- The introduction states the question, the contribution, the approach, and the headline result early, and explains the general-economics interest.
- Position against the relevant literature explicitly; "first to study X" is not a contribution.
- EER uses an unstructured abstract and JEL codes; an online appendix carries robustness, proofs, and secondary results.
- Exhibits should be self-contained and report interpretable magnitudes, not only test statistics.

## Official-submission checklist

- Search the live site for "European Economic Review guide for authors / submission guidelines" and follow the current Elsevier version.
- Re-check submission fee, formatting, abstract/JEL requirements, anonymization, and figure/table standards on the submission system.
- Re-check the current data and code availability / replication policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why a general economist (not just a specialist) should care.
- [ ] The contribution is stated as identification / theory / measurement, not as statistical significance.
- [ ] The introduction positions the paper against the relevant frontier across fields, not only within a niche.
- [ ] Identification or proofs meet current standards; inference and robustness are in place.
- [ ] Data, code, and appendix match the current official guide.

## Common desk-reject triggers

- A purely local/descriptive paper with no general-economics contribution.
- Reduced-form correlation presented as a causal effect with no credible design.
- A narrow theory extension with no general or consequential implication.
- Significance treated as the finding, with mechanism and interpretation left thin.

## Re-routing decision

- General-interest at the top → `american-economic-review`; European general-interest flagship → `journal-of-the-european-economic-association`.
- Field-leading work → the relevant field journal (`journal-of-public-economics`, `journal-of-labor-economics`, `journal-of-international-economics`, `journal-of-development-economics`).
- Quantitative macro → `review-of-economic-dynamics` or `journal-of-monetary-economics`; pure theory → `journal-of-economic-theory`; applied micro with strong identification → `journal-of-human-resources` or `international-economic-review`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] European Economic Review
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification / theory clear EER's general-field bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / data-code policy / exhibits>
[Re-route suggestion] <if not a fit, a better-matched venue>
```

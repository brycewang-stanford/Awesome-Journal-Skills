---
name: management-science
description: Use when targeting Management Science (MS) or deciding whether an operations / finance / information-systems / marketing / decision-analysis / behavioral / strategy manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Management Science (management-science)

## Journal positioning

Management Science is INFORMS's flagship umbrella journal and one of the most cited business journals across the entire management spectrum. It is unusual in that it is not a single-subfield outlet: it is organized into many departments — operations management, optimization, stochastic models, finance, accounting, information systems, marketing, decision analysis, behavioral economics, entrepreneurship/innovation, strategy, organizations, healthcare, and more — each run by a department editor (DE) who owns the standards for that area. A paper succeeds when it clears the uniformly high rigor bar of the *right department*, whether it is a clean analytical model or a clean empirical study. The readership is the broad quantitative management community, so a paper must matter beyond its niche and be legible to scholars who are not specialists in its method.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the INFORMS / Management Science site and the editorial submission system.

## When to trigger

- The author names Management Science / MS (or the INFORMS / FT50 / UTD24 quantitative-management elite) as the target venue.
- A rigorous analytical-modeling or empirical paper spans subfields and the author must decide which department to submit to.
- A general operations, finance, IS, marketing, or decision paper needs re-framing into a contribution that one MS department will own.
- The author needs MS's desk-reject risks and a credible field-flagship alternative list before submitting.

## Scope & topic fit

- Analytical / modeling work: optimization, stochastic models, game-theoretic and mechanism-design models of operations, pricing, contracting, finance, and information economics — with a clear managerial or economic insight, not math for its own sake.
- Rigorous empirics: causal-inference field studies, structural estimation, lab and field experiments, and large-scale data work across operations, finance, IS, marketing, and behavioral domains.
- Decision analysis, behavioral operations/economics, judgment under uncertainty, and prescriptive analytics.
- Topics that fit a named department; submitting to the wrong department is the single most common avoidable error.

## Method & evidence bar

- Uniformly high rigor regardless of department: analytical papers need correct, non-trivial results with proofs (typically in an appendix) and a managerial takeaway; empirical papers need credible identification or a defensible structural model.
- The contribution must be generalizable insight, not a one-context application; a model's assumptions and an empirical design's exclusion restrictions must be defended.
- Empirical causal claims meet current standards (DiD/IV/RDD/experiments, proper inference, robustness, placebo/falsification).
- Behavioral work needs adequate power, pre-registration where the department expects it, and replicable designs.

## Structure & house style

- The introduction states the management problem, the modeling or empirical approach, and the general insight early; it must read to a non-specialist quantitative audience.
- Choose and signal the target department; frame the contribution in that department's language and against that department's recent MS papers.
- Proofs, extended derivations, robustness, and secondary analyses go to an electronic companion / online appendix.
- Exhibits report economic or managerial magnitudes and interpret them, not just significance or existence.

## Official-submission checklist

- Search the live site for "Management Science submission guidelines / author instructions" and follow the current INFORMS version, including the list of departments and their stated scope.
- Re-check the current department list and DE assignments, formatting, abstract length, anonymization/double-blind policy, and reference style.
- Re-check the current data and code availability / reproducibility policy, electronic-companion rules, and disclosure/ethics requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the general management insight, legible to a non-specialist.
- [ ] The correct target department is identified and the framing matches it.
- [ ] The contribution is stated as a model result / identification / mechanism, not as statistical significance.
- [ ] Proofs or identification arguments are complete; robustness lives in the electronic companion.
- [ ] Abstract, anonymization, references, and data/code policy match the current MS guide.

## Common desk-reject triggers

- Submitting to the wrong department, or a paper too narrow for any department's general-insight bar.
- An analytical model with a correct but managerially uninteresting result, or unrealistic assumptions with no defense.
- An empirical paper with significant coefficients but no identification or mechanism.
- A method/algorithm paper with no managerial payoff (often belongs at an INFORMS computing or OR venue).

## Re-routing decision

- OR methodology, optimization, queueing, stochastic theory → `operations-research`; computational/algorithmic OR or ML-for-OR → `informs-journal-on-computing`.
- OM theory/models or empirical OM → `manufacturing-and-service-operations-management`, `production-and-operations-management`, or `journal-of-operations-management`.
- IS-core contribution → `mis-quarterly`, `information-systems-research`, `journal-of-management-information-systems`, or `journal-of-the-association-for-information-systems`.
- Finance-core → the finance top-3 (`journal-of-finance`, `journal-of-financial-economics`, `review-of-financial-studies`); management-theory-core → `academy-of-management-journal`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Management Science
[Topic tags] <2–3 closest topics + target department>
[Method/evidence] <does the model result or identification clear the department's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <department list / submission system / blinding / electronic companion / data-code>
[Re-route suggestion] <if not a fit, a better-matched venue>
```

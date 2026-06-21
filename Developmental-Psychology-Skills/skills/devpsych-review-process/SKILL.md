---
name: devpsych-review-process
description: Use when you need to understand how Developmental Psychology (APA) evaluates a manuscript — masked peer review, editorial weighting of developmental significance, design rigor (age/cohort, invariance, attrition), JARS reporting, and TOP transparency. Use when stress-testing a paper before submission or interpreting a decision letter. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (devpsych-review-process)

Developmental Psychology combines theory-advancing selectivity with rigorous developmental-method
scrutiny. The journal offers **masked peer review**, and editors and reviewers weigh not only whether the
finding is interesting, but whether the **developmental claim is credible** (age vs. cohort, measurement
invariance, attrition), whether reporting meets **JARS**, and whether transparency meets **TOP**. Knowing
this lets you pre-empt the common rejection reasons.

## When to trigger

- Before submitting, to stress-test the manuscript
- Deciding whether to request masked review and how to anonymize
- Interpreting a decision letter and setting expectations

## How review works

1. **Masked (anonymized) review available.** Authors may request masked review; if so, keep author
   identity out of the manuscript **and** out of shared links (see `devpsych-submission`). Masked review
   is intended to reduce bias against (e.g.) early-career or under-represented authors.
2. **Editorial triage.** The handling editor assesses developmental significance, theory advance, design
   rigor, and fit; weak-fit or "not-developmental" papers may be declined without full review.
3. **External review** assesses the theoretical contribution, the credibility of the **change claim**
   (age/cohort, invariance, attrition, power), analysis and JARS disclosure, and transparency.
4. **Transparency and reporting are weighed.** Under TOP and JARS, missing data-availability statements,
   unjustified opacity, or non-JARS reporting weaken a paper.
5. **Decisions.** Reject, revise and resubmit, or accept; expect substantive revision and frequent
   requests for invariance tests, attrition analyses, added robustness, or fuller disclosure.

## What developmental reviewers reliably probe

- **Is it change, or a snapshot?** A cross-sectional age difference framed as development draws fire.
- **Age vs. cohort.** Could the "age effect" be a cohort/era effect? Reviewers ask routinely.
- **Measurement invariance.** Is the construct the same across the ages you compare?
- **Attrition.** Is the trajectory biased by who dropped out, and is missingness modeled?
- **Power for the change parameter** and JARS-complete reporting.

## Desk-reject and decline-without-review patterns

Confirm current categories against the official guidelines, but recognize these shapes:

| Pattern an editor sees | Likely outcome | Pre-empt it by |
|------------------------|----------------|----------------|
| Single-age finding framed as developmental | desk reject (fit) | add an age contrast/wave or reframe |
| Cross-sectional age effect, no cohort discussion | review with heavy R&R | address age vs. cohort up front |
| Trajectory interpreted with no invariance test | R&R or reject | report configural→metric→scalar first |
| Listwise deletion with non-trivial attrition | R&R | refit with FIML/MI; add attrition analysis |
| "Data available on request," no statement | returned for compliance | add a data-availability statement + DOIs |

## Worked micro-example (illustrative triage)

```
Manuscript: preregistered three-wave growth study (N = 300; ages 4-8),
            invariance established, FIML for attrition, open de-identified
            data + scripts, identifiable video via Databrary.
Editor read: developmental significance (within-person growth + mechanism),
            rigor (invariance + attrition handled), transparency (TOP-strong).
Likely route: external review, probable R&R for added robustness/disclosure.
Counter-case: same finding, one age group, cross-sectional, no invariance,
            data on request → likely declined or not-developmental.
```

## How reviewers weigh the evidence (calibration anchors)

- A credible within-person change claim — invariant measure, modeled attrition, powered slope — is the
  strongest signal; it converts "interesting correlation" into "developmental finding."
- Transparency under TOP is judged in context: a candid, justified restriction on minors' data with an
  access path reads better than silent opacity or unethical open posting.
- Masked review is a tool against bias, not a guarantee — anonymize the manuscript *and* the repository
  links, or it is undone.

## Anti-patterns

- A single-age or purely cross-sectional finding sold as developmental
- Ignoring age-vs-cohort, measurement invariance, or attrition
- Exploratory trajectory shapes dressed as confirmatory (JARS violation)
- Weak or absent transparency / data-availability statement
- Expecting acceptance without an invariance/attrition/disclosure-heavy R&R

## Output format

```
【Developmental significance】clear + theory-advancing? [Y/N]
【Change claim credible】age/cohort + invariance + attrition + power? [Y/N]
【JARS reporting】complete (ES+CI, exclusions, missing data)? [Y/N]
【Transparency (TOP)】data-availability + preregistration handled? [Y/N]
【Masked review】manuscript + links anonymized? [Y/N]
【Realistic outcome】reject / R&R / accept
【Next】devpsych-submission (or devpsych-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — masked review, JARS, TOP, and editorial policy
- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — verified exemplars showing credible developmental claims

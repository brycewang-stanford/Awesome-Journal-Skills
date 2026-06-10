---
name: demog-review-process
description: Use to understand how Demography (PAA / Duke University Press) evaluates a manuscript — double-blind review, pre-review/desk screening by the Editor or a Deputy Editor, the role of topic-area Deputy Editors, and the grounds for desk rejection (inappropriate fit or unlikely to receive favorable reviews). Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (demog-review-process)

Knowing how Demography screens and decides lets you pre-empt the failure modes before submitting.
Demography is **double-blind** and runs a **pre-review** with the Editor or a Deputy Editor before
external review.

## When to trigger

- Before submitting, to stress-test against desk-rejection grounds
- Interpreting a decision letter and setting expectations
- Understanding the role of topic-area Deputy Editors
- Deciding how to anonymize and how to frame general interest

## How Demography review works

1. **Double-blind.** Authors are **not** told reviewer names and reviewers are **not** told author
   names. Avoid self-identifying references so anonymity holds (see `demog-submission`).
2. **Pre-review / desk screening first.** Every manuscript passes a pre-review with the **Editor or an
   assigned Deputy Editor**. It is first checked for **compliance** with word and table/figure limits,
   then assessed for suitability. A paper may be **desk-rejected** when it is **(1) inappropriate for
   Demography** or **(2) unlikely to receive favorable evaluations from external reviewers**. Desk
   rejections usually occur within the first few weeks.
3. **Topic-area Deputy Editors.** Deputy Editors who **specialize in the major areas of demography**
   help select expert reviewers, synthesize the reviews, and make a recommendation to the Editor.
4. **External review.** Manuscripts passing the desk go to expert demographer reviewers.
5. **Decision and revision.** Standard scholarly outcomes (reject / revise-and-resubmit / accept);
   confirm the exact categories and any timelines on the official page (see 待核实).

## Shape the paper to pass

- Make **general interest to demographers** explicit (avoids the "inappropriate for Demography" desk
  rejection) — see `demog-topic-selection` and `demog-literature-positioning`.
- Meet the **word and table/figure limits** before submitting (the pre-review checks compliance first).
- Get the **demographic method right** (rates, exposure, identification) so expert reviewers see rigor.
- Anticipate the strongest rival demographic explanation and answer it in the design.

## Anti-patterns

- Submitting a paper that uses demographic data but asks no population question (fit desk rejection)
- Exceeding the word or table/figure limits (caught at the compliance pre-review)
- Leaving self-identifying references that compromise double-blind review
- Expecting external review for a paper unlikely to earn favorable reviews — that is a desk-reject ground


## Review-risk pass for Demography

Run this as a concrete capability pass. First lock the demographic process, data source, time scale, selection/migration/mortality issue, and uncertainty; then test whether the manuscript addresses population-science reviewers who inspect demographic process, measurement, cohort/period logic, and population validity.

- **Primary move:** Turn likely reviewer objections into a ledger with response evidence, manuscript location, and the decision-maker who must be convinced first.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Population and Development Review for policy synthesis, JMF for family process, Social Forces for broader sociology; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Fit check】is it appropriate for Demography (a population question of general interest)? [Y/N]
【Compliance】word + table/figure limits met for the chosen type? [Y/N]
【Method rigor】rates/exposure/identification defensible to expert reviewers? [Y/N]
【Anonymity】no self-identifying references? [Y/N]
【Realistic outcome】desk-reject / R&R / (rare) accept
【Next】demog-submission (or demog-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review-process page (double-blind, pre-review, desk rejection, Deputy Editors)

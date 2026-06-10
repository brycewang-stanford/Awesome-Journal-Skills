---
name: jhr-writing-style
description: Use when polishing Journal of Human Resources (JHR) prose — abstract, introduction, results paragraphs that translate coefficients into policy units, reconciliation language against prior estimates, disclosure wording, and structure that respects the page-limited manuscript format.
---

# Writing Style (jhr-writing-style)

## When to trigger

- The manuscript is too long for the 40-page limit
- The policy lesson or identification strategy is buried
- Results paragraphs report coefficients without interpretation

## Style principles

- State the empirical-micro question in the first page.
- Make the identifying variation visible before literature detail.
- Translate coefficients into policy-relevant magnitudes.
- Reconcile with prior work explicitly.
- Keep main-text tables few and move supporting material to the Online Appendix.

## First-page pattern

The first page should do five jobs in order:

1. Name the policy-relevant empirical-micro question.
2. State the institutional or data feature that creates variation.
3. Give the headline estimate in natural units.
4. Say how it compares with the closest prior estimate.
5. State the policy interpretation and its boundary.

Do not open with a broad policy problem for more than one paragraph. JHR readers need to see the design
and reconciliation early.

## Abstract compression

Use a five-sentence abstract unless the journal's live limit forces something tighter:

1. Policy-relevant question.
2. Data and identifying variation.
3. Headline magnitude in natural units.
4. Reconciliation with the closest prior estimate or mechanism.
5. Policy interpretation with the external-validity boundary.

Avoid empty phrases like "important implications" unless the next words name the actual margin. A good JHR
abstract lets a reader recover the estimand, setting, magnitude, and policy lesson without opening the
tables.

## Results paragraph pattern

```text
Table X estimates [claim] using [design]. The preferred specification in column Y
implies [magnitude] for [population]. This compares with [prior estimate] because
[sample/specification/design difference]. The result suggests [policy implication].
```

## Before/after: a results paragraph rewritten for JHR

Illustrative job-training example (numbers invented to show the editing moves):

```text
BEFORE: The coefficient on training (0.083, p<0.01) is positive and highly
significant, confirming that the program works. This has important policy
implications.

AFTER: Table 4 reports the lottery-based LATE. Column 2 implies that training
raises quarterly earnings by 8.3 log points — about $410 at the control mean —
for applicants induced by the lottery (SE 0.024, clustered on 38 sites). The
estimate sits between the prior experimental literature's near-zero results
and the larger observational ones; Appendix Table A5 shows the gap closes once
we match the prior studies' shorter follow-up window. At roughly $2,900 per
trainee, the implied payback period is under two years for compliers.
```

The rewrite names the estimand, converts the coefficient, states the inference
unit, reconciles, and prices the policy — five JHR sentences doing five jobs.

## Sentence-level conventions

- Name the estimand (ATT, LATE, ITT, descriptive gap) the first time a result
  is stated; never let "effect" float unanchored.
- Keep percent and percentage points rigorously distinct — a frequent JHR
  copyedit and referee irritant in education and health papers.
- State the clustering level once in prose and thereafter only in table notes.
- Reserve causal verbs (raises, reduces, induces) for designed estimates;
  descriptive results get "is associated with" and an explicit caveat.
- When heterogeneity is discussed, tie each cut to a policy margin in the same
  sentence, not in a separate "implications" paragraph.

## Trim hierarchy for the page cap

When the manuscript runs long, cut in this order: (1) literature narration not
attached to a benchmark estimate; (2) robustness prose that can become one
sentence plus an appendix citation; (3) secondary heterogeneity cuts;
(4) institutional history beyond what the design needs. Never trim the
event-study figure, the first stage, or the reconciliation paragraph — those
are what JHR referees read first.

## Output format

```text
[Section] abstract / intro / data / results / conclusion
[Main edit] ...
[Magnitude wording] ...
[Reconciliation wording] ...
[Page-limit fix] ...
[Next step] jhr-submission
```

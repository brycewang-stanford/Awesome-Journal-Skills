---
name: red-review-process
description: Use when understanding or planning around the Review of Economic Dynamics (RED) editorial process — the editor desk/suitability screen, single-anonymized refereeing with a minimum of two reviewers, and RED's fast-review orientation without promising a fixed decision date. Sets expectations and timelines; it is not the submission preflight (see red-submission).
---

# Review Process at RED (red-review-process)

## When to trigger

- Setting expectations on timing and review model before or after submitting
- Understanding what the desk screen decides and what reaches referees
- Planning around the single-anonymized (not double-blind) model

## How RED review works (verified)

- **Desk / suitability screen first.** The editor first assesses whether the paper is suitable for RED;
  papers that pass are sent out for review. A clean, in-scope, dynamic-model paper clears this faster.
- **Single-anonymized review.** Reviewers' identities are concealed from authors, but **author identities
  are visible to reviewers** — this is *not* double-blind, so you do **not** anonymize the manuscript.
- **Minimum of two reviewers.** Suitable papers go to at least **two independent referees**.
- **Speed is a feature, not a guarantee.** The current reviewer page asks reviewers to notify the editor
  if they cannot act within six weeks, and older SED newsletters report fast first-decision performance.
  Treat this as planning guidance, then confirm live expectations in the current author system.
- **Coordinating Editor.** **Loukas Karabarbounis** (University of Minnesota / Minneapolis Fed) is RED's
  Coordinating Editor (the editor-in-chief equivalent), cross-checked on SED and ScienceDirect pages.

## Planning implications

- Single-anonymized means **keep self-citations and acknowledgments natural** — no double-blind scrubbing.
- The fast-turnaround target rewards a **complete, runnable** submission with replication discipline
  already in place; do not submit a paper whose code archive does not yet exist.
- Plan around a **post-desk** clock that starts only after the suitability screen and the fee.

## Pre-review readiness

Before submission, stage the same materials you would need for a fast R&R:

- model equations and calibration table are internally consistent;
- code archive can rerun baseline and counterfactual exhibits;
- untargeted moments or accuracy diagnostics are available;
- the abstract names the dynamic mechanism and quantitative result;
- any proprietary data or large-runtime issue is documented.

## Checklist

- [ ] Manuscript is **not** anonymized (single-anonymized model)
- [ ] Paper is in-scope and complete enough to clear the desk screen quickly
- [ ] Expectations set for ≥2 referees and live post-desk timing guidance
- [ ] Replication materials staged so a fast acceptance is not bottlenecked

## Anti-patterns

- Double-blind-scrubbing a manuscript for a single-anonymized journal
- Treating an older turnaround statistic as a guaranteed current deadline
- Treating slow-journal habits (thin appendix, no code) as acceptable here

## What fails the suitability screen

Patterns that plausibly stop a quantitative-macro paper at the desk (hedged — the screen is editor
judgment, not a published rubric):

| Desk-risk pattern | Why it fails the RED lens |
|---|---|
| Static cross-sectional analysis, no dynamic model | scope is method-defined; no dynamics, no fit |
| Reduced-form policy evaluation with a token "model sketch" | the model must carry the argument, not decorate it |
| Calibration exercise reproducing known results with newer data | no mechanism, method, or moment advance |
| Pure econometric theory with no dynamic-economics object | belongs at an econometrics outlet |
| Incomplete computation ("results to be added", no accuracy info) | the fast-review model presumes a finished quantitative core |

## Round log

```text
ROUND LOG — [paper short title]
  Submitted (fee received):  [date]   ← clock starts after fee + desk
  Desk decision:             [date]   suitable / not suitable
  Referee reports expected:  [live guidance / historical fast-review benchmark]
  Decision:                  [date]   reject / R&R / accept
  If R&R — archive rerun:    [date]   resubmission fee: exempt (2nd+ resubmission)
```

Keep this log in the project repository; it disciplines the team's expectations and gives a polite
status query an objective trigger — confirm current expected turnaround against the journal's current
author guidelines before quoting any figure to the editor.

## Who referees at a SED journal

Expect referees drawn from the SED-conference community: people who solve heterogeneous-agent and
business-cycle models themselves. Plan for reports that probe grids, Euler-equation accuracy, calibration
circularity, and counterfactual logic rather than only framing — which is why the pre-review staging list
above doubles as referee-proofing.

## Supplementary resources

- [`red-submission`](../red-submission/SKILL.md) — the pre-submission preflight
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review-model and timing sources

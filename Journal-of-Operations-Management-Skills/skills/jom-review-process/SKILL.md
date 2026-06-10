---
name: jom-review-process
description: Use when understanding how Journal of Operations Management (JOM) evaluates submissions — the Department-routed structure, the asymmetric double-anonymous review, the Empirical Research Methods method check, and how to read a JOM decision letter before or after submitting.
---

# Understanding JOM Review (jom-review-process)

## When to trigger

- You want to know what happens to a manuscript after submission
- You received a JOM decision letter and need to interpret it
- You are unsure who sees your identity and who evaluates the operations contribution
- You want to anticipate the method check before submitting

## The Department-routed pipeline

JOM is organized into **12 Departments**, each with its own Department Editors and mission. Your submission is routed to a Department (you named two, one preferred). The Department Editor oversees evaluation within that Department's conversation, typically assigning an Associate Editor who manages reviewers from the Editorial Review Board (ERB) and elsewhere. This is analogous to, but distinct from, INFORMS-style departmental area-editor routing.

## Asymmetric double-anonymous review

Review is double-anonymous, with a specific asymmetry: **author identities are shared with the Editors-in-Chief and Department Editors but not with reviewers or Associate Editors** (and author-blind to those parties; vice versa). Keep the manuscript fully anonymized — reviewers and AEs must not be able to infer you.

## The Empirical Research Methods method check

JOM has a dedicated **Empirical Research Methods Department** that not only publishes methods papers but **performs method checks on incoming empirical submissions**. Expect scrutiny of sampling, measurement, identification, common-method remedies, and reproducibility — an institutionalized methods gate not found at generic top management journals. Weak identification or unvalidated measures can stall a paper here regardless of how interesting the phenomenon is.

## Likely decisions

- **Desk reject / return** — out of scope (e.g., a purely analytical/optimization model), operations not at the heart, over-length, missing checklist, or method too weak to send out.
- **Reject** — fundamental theory, design, or contribution problems.
- **Major revision (R&R)** — promising; substantial empirical/theoretical work required. The norm for papers that progress; first-round acceptance is essentially unheard of.
- **Minor revision** — close to acceptable.
- **Accept** — after one or more developmental rounds.

## Reading the letter

Separate the Department Editor/AE's framing (the decisive priorities) from individual reviewer comments. Identify which concerns are about the **operations contribution**, which are **method-check** issues (often non-negotiable), and which are presentational. Method-check and identification concerns usually must be fully resolved; some reviewer suggestions can be argued.

## Who sees what, and who decides

The asymmetric anonymity rule has practical consequences worth tabulating. This summarizes JOM's stated structure; confirm the current masthead, Department roster, and anonymity policy against the journal's author guidelines before relying on specifics.

| Party | Sees author identity? | Primary role |
|-------|-----------------------|--------------|
| Editors-in-Chief | Yes | Final decision authority; assign Departments |
| Department Editor | Yes | Frames evaluation within the Department's conversation |
| Associate Editor | No (author-blind) | Manages reviewers, synthesizes the recommendation |
| Reviewers (ERB and others) | No (author-blind) | Assess contribution, method, and operations centrality |

Keep the manuscript fully anonymized so AEs and reviewers cannot infer you; supply full identities only in the portal author fields.

## What desk-rejects before review

- Out of scope: a purely analytical/optimization model with no observation.
- Operations not at the heart of the question — context, not phenomenon.
- Over-length manuscripts returned for streamlining before they reach reviewers.
- Missing the mandatory submission checklist, or method too weak to send out.

## Worked vignette: reading a major-revision letter

A letter routes a healthcare-operations survey study to a Department Editor, who relays an AE synthesis plus two reviews (illustrative). Reviewer 1 wants more controls; Reviewer 2 questions construct validity; the AE's cover note says the operations contribution is promising but the measurement model is underspecified. Reading correctly: the AE's measurement concern is a method-check issue and likely non-negotiable, so it outranks Reviewer 1's controls request. The decision is a genuine R&R, not a soft reject, because the contribution is endorsed. The author should route the measurement fix through `jom-data-analysis`, treat the controls as a transparent robustness add, and prepare for at least one further round rather than expecting acceptance.

## Referee and editor signals to decode

- *"Promising but the contribution is unclear"* — an invitation to reframe, not a rejection of the data.
- *"Consider a more suitable outlet"* — usually a scope signal that operations is not central or the work is analytical.

## Output format

```
【Stage】routed to Department ... / under AE / decision received
【Who sees identity】EICs + Department Editors (not reviewers/AEs)
【Method-check exposure】sampling / measures / identification / reproducibility ...
【Decision read】desk / reject / major-R&R / minor / accept
【Decisive vs. arguable comments】...
【Next step】jom-rebuttal (if R&R)
```

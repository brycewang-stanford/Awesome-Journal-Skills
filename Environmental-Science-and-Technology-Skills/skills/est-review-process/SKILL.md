---
name: est-review-process
description: Use to understand how Environmental Science & Technology (ES&T) evaluates a manuscript — editor desk-screening that declines a significant fraction without external review, expert review by typically three reviewers, and editor-led decisions. It sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (est-review-process)

Knowing how ES&T screens and decides lets you pre-empt the failure modes before submitting. ES&T
editors **desk-decline a significant fraction** of submissions before any external review, so the
manuscript must clear the editorial bar on significance and fit first.

## When to trigger

- Before submitting, to stress-test against desk-decline grounds
- Interpreting a decision letter and setting expectations
- Understanding what expert reviewers are likely to weigh
- Deciding whether the work is urgent enough for ES&T Letters instead

## How ES&T review works

1. **Editorial screening first.** The Editor-in-Chief / executive editors screen submissions; a
   significant fraction are **declined without external review** when significance, fit, novelty, or
   rigor fall short.
2. **Expert external review.** Manuscripts that pass are sent to expert reviewers — typically
   **three** — who assess within a few weeks. Reviewer identities are kept anonymous; the
   author-blinding model is not stated as a fixed rule (待核实).
3. **Editor decision.** Associate editors and the editorial leadership make the call; typical outcomes
   are **reject / major or minor revision / accept**. Decisions are at editor discretion, informed by
   the reviews.
4. **Author input.** Authors suggest **≥4** non-conflicted reviewers and may note non-preferred ones
   (see `est-cover-letter`).
5. **Integrity checks.** Submissions are screened for plagiarism with **iThenticate/CrossCheck** and
   for ethics/COI compliance.

## Shape the paper to pass

- Make environmental significance explicit and early (avoids the top desk-decline reason).
- Engage the relevant literature so novelty is obvious (see `est-literature-positioning`).
- Pre-empt the analytical objection: report QA/QC, uncertainty, and a closed mass balance.
- Match urgency to venue: genuinely time-sensitive, high-impact short results may fit **ES&T Letters**.
- Clear ethics/safety/COI and have the SI + data deposit ready (reviewers see the SI).

## Desk-reject triggers and where they get fixed upstream

A significant fraction of ES&T submissions never reach reviewers. Each common desk-decline ground
maps to an earlier skill — fix it before the editor sees the paper:

| Desk-reject ground | Signal the editor reads | Fix it in |
|--------------------|--------------------------|-----------|
| No environmental significance | "clean lab result, no real-system relevance" | `est-topic-selection` |
| Novelty is incremental occurrence | "another dataset, no new insight" | `est-literature-positioning` |
| Out of scope for ES&T | better suited to a specialist title | `est-topic-selection` |
| Wrong article type / over caps | exceeds word/figure budget | `est-submission` |
| Missing TOC graphic or SI | submission incomplete | `est-figures-and-tables`, `est-reporting-and-reproducibility` |

## Worked micro-example (illustrative — predicting a decision on an LCA paper)

Stress-testing a GAC-vs-IX LCA before submission (illustrative reasoning):

- **Significance:** present — links treatment choice to climate burden, a sustainability question
  ES&T centers. Clears the first desk axis.
- **Novelty risk:** if the LCA merely re-runs a standard inventory, a reviewer flags "method applied,
  no new insight." Strengthen by surfacing a non-obvious trade-off (e.g., regeneration energy
  dominating the GAC footprint — illustrative).
- **Rigor:** Monte Carlo uncertainty reported, functional unit stated, characterization factors
  sourced — survives the analytical reviewer.
- **Realistic outcome:** major revision is the modal result for a sound-but-improvable paper; expect
  asks for sensitivity on the electricity grid mix and clearer environmental implications. Plan for it
  rather than reading "major revision" as near-acceptance.

The lesson: walk each desk axis yourself first; the editor will, and an unaddressed axis is a decline
before any reviewer weighs in.

## Anti-patterns

- A clean-but-incremental result with no significance argument (desk decline)
- Ignoring an obvious related literature so novelty looks thin
- Hoping reviewers overlook missing blanks/recoveries or an unclosed mass balance
- Sending non-urgent work to ES&T Letters, or urgent work buried in a long Research Article
- Treating a "major revision" as an acceptance

## Output format

```
【Desk-screen check】significance / fit / novelty / rigor — any red flags?
【Significance】explicit and early? [Y/N]
【Literature engaged】novelty obvious? [Y/N]
【Analytical defense】QA/QC + uncertainty + mass balance ready? [Y/N]
【Venue】ES&T vs ES&T Letters
【Realistic outcome】reject / revision / (rare) accept
【Next】est-submission (or est-revision-and-rebuttal on a decision)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — editor screening, reviewer count, decision flow, integrity checks

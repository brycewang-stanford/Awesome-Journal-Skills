---
name: red-rebuttal
description: Use when planning the response-to-referees after a Review of Economic Dynamics (RED) revise-and-resubmit — structuring a point-by-point reply for a single-anonymized, two-referee process, prioritizing model/quantitative concerns, and remembering that second-and-later resubmissions are exempt from the submission fee. Strategy; it does not write the paper.
---

# Rebuttal Strategy for RED (red-rebuttal)

## When to trigger

- An R&R has arrived from RED and you are planning the revision and reply
- Reconciling comments from the (minimum) two referees and the editor
- Deciding how to handle requests that touch the model, calibration, or code archive

## How to respond at RED

- **Point-by-point, per referee.** RED uses **single-anonymized** review with at least **two referees**;
  structure a clear, numbered response to each, plus a short letter to the Coordinating Editor summarizing
  the main changes. Quote each comment, then state the change and where it lives in the revised paper.
- **Lead with the model/quantitative concerns.** Referees at a dynamic-economics journal care most about
  whether the **mechanism**, **assumptions/regularity conditions**, **calibration discipline**, and
  **numerical accuracy** hold up. Address those first; presentation comments after.
- **Re-run and re-archive.** If you change the model, calibration, or estimation, **re-run everything** and
  update the data/code archive (and its readme.txt: seeds, execution order, runtime), since RED's code-first
  culture means reviewers expect the archive to track the revision.
- **Fee note.** A **second-or-later resubmission is exempt from the submission fee** — the review clock,
  not a new fee, governs the next round.
- **Disagree respectfully, with evidence.** Where you decline a change, give a model-based or quantitative
  reason (a robustness result, an accuracy check, a theoretical argument), not just an assertion.

## Checklist

- [ ] Separate, numbered point-by-point replies for each referee, plus an editor cover letter
- [ ] Model/quantitative concerns addressed first; every change cross-referenced to the manuscript
- [ ] Code/data archive re-run and updated to match the revision
- [ ] Declined requests answered with quantitative/theoretical evidence
- [ ] Resubmission handled as fee-exempt

## Anti-patterns

- A single undifferentiated reply that blurs the two referees' distinct concerns
- Revising the model but not re-running or re-archiving the code
- Treating a resubmission as if it requires a new fee
- Brushing off a substantive identification/accuracy concern instead of confronting it

## Rerun rule

Any revision that changes a parameter, calibration target, solution method, sample, or shock definition
requires rerunning the affected exhibits and updating the archive README. If the response letter says
"results are unchanged," cite the rerun script and output date.

## Response-letter skeleton for a RED R&R

```text
Dear [Coordinating Editor],

Summary of changes (one page max):
  1. [Model/mechanism change] — new Section X, new Figure Y
  2. [Calibration/estimation change] — Table Z re-estimated; archive updated
  3. [New robustness] — Appendix C: accuracy checks / alternative targets

Referee 1
  Comment 1.1 (quoted). Response: [change + manuscript location].
    Rerun: run_all.sh, [date], seeds unchanged.
  Comment 1.2 (quoted). Response: we respectfully maintain [claim] because
    [quantitative evidence: robustness table / accuracy check / proposition].

Referee 2
  ...

Archive note: data/code archive v[X.Y] resubmitted; readme.txt updated
(execution order, expected runtime, random seeds).
```

Date-stamping each rerun and versioning the archive is cheap and signals the code-first discipline RED's
data/code policy institutionalizes.

## Frequent RED referee demands and how to absorb them

| Demand | Cost | Strategy |
|---|---|---|
| "Redo the counterfactual under an alternative calibration" | compute hours–days | run it; report in an appendix; flag heavy runtime in the letter |
| "Show the mechanism in a simplified version" | modeling time | add a two-period or representative-agent special case isolating the force |
| "Your solution may be inaccurate near the constraint" | re-solving | refine the grid near the kink; report Euler errors before and after |
| "Estimate parameter X rather than calibrating it" | substantial | negotiate: SMM on a focused moment set, or a sensitivity band with a reason estimation is infeasible |
| "Compare against [referee's preferred model]" | varies | implement a stripped-down version if central; otherwise differentiate analytically and bound the horse race out of scope |

## Triage order for the revision

Address concerns in this order: (1) anything questioning whether the mechanism exists, (2) calibration
and estimation discipline, (3) numerical accuracy, (4) extra experiments, (5) exposition. A reply that
fixes typos first and the accuracy concern last reads as evasive to quantitative-macro referees.

## Supplementary resources

- [`red-review-process`](../red-review-process/SKILL.md) — the review model this reply addresses
- [`red-replication-and-data-policy`](../red-replication-and-data-policy/SKILL.md) — updating the archive on revision

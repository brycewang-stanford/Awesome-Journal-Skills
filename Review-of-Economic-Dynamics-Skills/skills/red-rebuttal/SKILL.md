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

## Supplementary resources

- [`red-review-process`](../red-review-process/SKILL.md) — the review model this reply addresses
- [`red-replication-and-data-policy`](../red-replication-and-data-policy/SKILL.md) — updating the archive on revision

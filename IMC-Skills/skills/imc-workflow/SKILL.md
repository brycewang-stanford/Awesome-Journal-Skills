---
name: imc-workflow
description: Use when planning an ACM IMC campaign end to end, covering the choice between the two annual deadlines, backward planning from the target cutoff, the registration step, the One-Shot-Revision path across deadlines, availability shepherding, the camera-ready and dataset release, and the Replicability Track calendar.
---

# IMC Workflow

Use this to plan an IMC campaign against the calendar. IMC runs **two submission deadlines a year**
with a shared review pipeline and a **One-Shot-Revision** path that resubmits to the next deadline.
Planning backward from the right deadline — and reserving time for ethics approvals and dataset
release that cannot be rushed — is the difference between a smooth cycle and a missed one.

## Choose the deadline first

IMC 2026 offered two cycles: cycle 1 submission ~20 Nov 2025, cycle 2 submission ~29 Apr 2026
(confirm current dates on the Important Dates page). Choose by data-collection readiness, not
optimism:

- If measurement and ethics approvals will be solid by the earlier cutoff, target cycle 1 — and a
  One-Shot-Revision still lands you in cycle 2.
- If data collection or IRB is unfinished, target cycle 2 rather than submitting thin work that
  earns a reject instead of a revision.

## Backward plan from the target cutoff

```text
[T-0]     Submission deadline (AoE). PDF + BBL uploaded; availability declaration set.
[T-1wk]   Registration cutoff (title/abstract/authors/conflicts) — precedes submission by ~a week.
[T-2wk]   Final anonymity sweep (incl. vantage points); Ethics section finalized; artifact anonymized.
[T-4wk]   Freeze the measurement narrative; draft complete; limitations argued per-result.
[T-8wk]   Finish the decision-critical measurements; validate ground-truth subsamples.
[T-earlier] Obtain IRB determination; run active measurements safely; pin provenance as you collect.
```

Ethics approvals and longitudinal windows are the long poles — they cannot be compressed in the
final weeks.

## The review-to-decision arc

```text
[Submit] -> multi-round double-blind review
[Early reject] consensus-reject papers notified early -> reroute promptly (imc-topic-selection)
[Decision] Accept / One-Shot-Revision / Reject
   Accept            -> shepherding + camera-ready
   One-Shot-Revision -> execute the bounded action points; resubmit NEXT deadline, same reviewers
   Reject            -> reroute to SIGCOMM/NSDI/CoNEXT/PAM or a journal
```

## The One-Shot-Revision leg

If you receive a One-Shot-Revision (`imc-review-process`, `imc-author-response`):

- You have until the **next deadline** to execute a **bounded** action list (up to a few concrete
  additions/changes) for the **same reviewers**.
- Plan the additional measurements immediately — a new vantage point or a longitudinal extension
  takes real calendar time.
- Do exactly the named action points; resist scope creep that could cost the champion's support.

## After acceptance

```text
[Shepherding]   deliver the artifact you declared; the shepherd checks availability
[Camera-ready]  de-anonymize; finalize Ethics + availability statements; permanentize dataset/code
                links to a DOI archive (cycle 1 camera-ready ~mid-April; cycle 2 ~1 Sep — confirm)
[Award]         for the Community Contribution Award, the dataset/tool must be public + usable by
                the camera-ready deadline
[Present]       at least one author presents at IMC (Karlsruhe, Oct 12-16, 2026)
```

## The Replicability Track calendar (if applicable)

If the contribution is replicating a prior measurement study, the path differs: submit an
**Expression of Interest** by its (earlier) deadline (IMC 2026 EoI ~29 Jan 2026), a small committee
screens it, and strong abstracts are invited to a full submission judged like the main track. Plan
the EoI well before you complete the replication.

## Calibration

- Every date is a per-edition snapshot — confirm both cycles' deadlines, the registration gap, and
  the camera-ready dates on the current Important Dates page before committing.
- Do not assume the One-Shot-Revision mechanics, the number of action points, or the Replicability
  Track dates carry over between editions.

## Output format

```text
[Target] cycle 1 / cycle 2, with the reason (data + ethics readiness)
[Backward plan] <dates from data collection -> registration -> submission>
[Long poles] <IRB / longitudinal window / dataset release>
[Post-decision path] accept / one-shot-revision (next deadline) / reroute
[Release plan] shepherding + DOI archive by camera-ready; award eligibility
```

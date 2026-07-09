---
name: imc-review-process
description: Use when reasoning about how an ACM IMC submission is evaluated, covering double-blind multi-round review, the Accept / One-Shot-Revision / Reject decision categories, the reviewer-champion rule and bounded action points, early rejection of consensus-reject papers, shepherding for artifact availability, and how IMC's two-deadline model differs from SIGCOMM/NSDI cycles.
---

# IMC Review Process

Model the pipeline before interpreting any single review. IMC's process is built around **two
deadlines a year** and a distinctive middle outcome — **One-Shot-Revision** — that is neither a
plain reject nor an open-ended major revision. The most consequential mental shift for authors
arriving from a single-round conference is that a good-but-incomplete measurement paper has a
*bounded* path to acceptance across deadlines.

## Process model

- Submission and review run on **HotCRP** with **double-blind** anonymity maintained through
  reviewing.
- Review proceeds in **several rounds**. Papers with a **consensus for rejection are notified
  early**, so authors can move the work to another venue without waiting for the full cycle.
- First decisions fall into **Accept**, **One-Shot-Revision**, or **Reject**. Reviewers weigh the
  significance of the measurement finding, the credibility of vantage points and ground truth, the
  soundness of methodology, honesty about limitations and confounds, the **Ethics** treatment, and
  artifact availability.
- Accepted papers may be **shepherded** by PC members — notably to ensure the **artifacts promised
  in the availability declaration are actually made available**.

## The One-Shot-Revision, precisely

| Element | What the call specifies |
|---|---|
| Trigger | At least **one reviewer champion** advocating the work's relevance and timeliness |
| Scope | Up to **3 additions/changes** — a bounded, concrete action list, not "revise broadly" |
| Resubmission | To the **next deadline** in the two-deadline cycle |
| Re-review | By the **same reviewers**, against the action points |

The strategic reading: a One-Shot-Revision is a **contract**. It is granted because someone
believes in the paper, and it is judged narrowly on whether the named action points were done.
Treat it as a near-accept with obligations, not a coin flip (see `imc-author-response`).

## Reading a decision against the categories

| Decision | What it means | Author move |
|---|---|---|
| Accept | Finding and method hold; shepherding for availability | Deliver the promised artifact; do not reopen scope |
| One-Shot-Revision | A champion exists; a bounded set of gaps (a missing vantage point, a confound to address, an ethics clarification) | Execute exactly the named action points; resubmit next deadline to the same reviewers |
| Reject | Structural: unrepresentative vantage points, no ground truth, thin measurement, ethics failure | Reframe or reroute (SIGCOMM/NSDI/CoNEXT/PAM or a journal); do not lightly resubmit unchanged |

Design the submission so its weakest point is **an addressable action item** (an extra vantage
point, a longitudinal slice, a bounded confound) rather than a structural flaw (a study design you
cannot redo before the next deadline).

## How IMC differs from its siblings

- **vs. SIGCOMM / NSDI:** those reward systems and protocol design with a supporting evaluation;
  IMC rewards the measurement itself and enforces the Ethics gate and availability declaration
  harder. Never assume a shared calendar or template.
- **vs. a single-deadline conference:** IMC's two deadlines plus One-Shot-Revision give a *within-
  year* second chance with continuity of reviewers — closer to a lightweight revise-and-resubmit
  than to "reject and try next year."
- **vs. a journal:** the revision is **one shot and bounded** (up to a few action points), not an
  open iterative loop.

## Who reads you

Expect measurement experts who will interrogate **vantage-point representativeness**, whether
ground truth is real, whether the finding is a snapshot artifact of a moving Internet, and whether
the active measurement was safe and ethical. Because IMC spans scanning, DNS, routing, web,
security, and social measurement, papers are matched to subarea reviewers — a vague methodology
gets caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  topic tags + vantage-point framing -> reviewer pool      (largest lever)
[Initial reviews]    factual corrections, clarifying vantage-point coverage, ethics clarifications
[One-Shot-Revision]  the strongest lever: execute the bounded action points exactly, for the
                     same reviewers, and show each one done
[Shepherding]        deliver the promised artifact; this is about availability, not new science
[After reject]       no appeal; reroute to a sibling venue or a journal
```

## Misreadings to avoid

- **Treating One-Shot-Revision as a full rewrite window** — you get a bounded action list and the
  same reviewers; scope creep signals you missed the point.
- **Treating One-Shot-Revision as guaranteed** — the second read against the action points is
  real.
- **Ignoring the early-reject signal** — a consensus-reject notice is a routing prompt, not an
  invitation to argue.
- **Underestimating shepherding** — a promised dataset that never materializes is a real problem.
- **Projecting last year's cadence** — deadline dates and revision mechanics are per-edition.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / one-shot-revision / shepherding / accepted
[Decision category] accept / one-shot-revision / reject, with the criterion driving it
[Champion?] is there a reviewer advocate? which review reads closest?
[Action points] <the bounded list to execute for the next deadline>
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak / scope creep beyond the action points / undelivered artifact
```

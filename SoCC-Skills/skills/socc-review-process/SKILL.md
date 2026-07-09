---
name: socc-review-process
description: Use when reasoning about how an ACM SoCC submission is evaluated, covering dual-anonymous review, the two-round-per-year model with the no-cross-round-resubmission rule, the author-response (rebuttal) period, the joint SIGMOD+SIGOPS reviewer pool that reads for both systems and data quality, and how SoCC's process differs from OSDI/NSDI/EuroSys.
---

# SoCC Review Process

Model the pipeline before interpreting any single review. SoCC — the ACM Symposium on Cloud
Computing — evaluates papers through a **dual-anonymous, two-round** process with a **rebuttal**,
and its reviewer pool is drawn from **both SIGMOD and SIGOPS**. The most consequential mental shift
for authors arriving from a pure systems or pure data venue is that your paper is judged on **both**
axes at once: a systems reviewer probes the mechanism and the deployment, a data/measurement
reviewer probes the workloads, traces, and statistical honesty — and a champion needs answers for
both.

## Process model

- Submission and review run on **HotCRP** with **dual anonymity**: reviewers do not see authors and
  authors do not see reviewers.
- SoCC runs **two rounds per year**, each a self-contained accept/reject cycle with its own
  abstract, submission, **author-response window**, and notification. A paper **rejected in Round 1
  cannot be resubmitted to Round 2** the same year.
- Each paper is read by multiple PC members spanning the systems-and-data pool, who weigh the
  significance of the cloud contribution, soundness of the design, quality of the measurement
  (throughput, latency, **tail**, and **cost**), realism of the deployment or trace, and
  reproducibility.
- Decisions are **accept / reject** per round (SoCC does not run a journal-style Major-Revision
  cycle); the **rebuttal** is the author's one written turn to move a borderline paper before the
  PC discussion.
- Accepted papers appear in the ACM DL SoCC proceedings and are presented at the symposium.

## Reading a decision against the axes

| Signal in the reviews | What it means | Author move |
|---|---|---|
| Strong on novelty, weak on evaluation realism | A systems reviewer wants a testbed/deployment, not simulation | Rebut with real-system numbers or scope the claim |
| Strong on system, weak on measurement rigor | A data/measurement reviewer doubts the workloads or stats | Defend trace/workload choice; add tail and variance |
| "Cost/tail not reported" | The cloud outcome that decides adoption is missing | Point to where it lives or concede it as a gap |
| "Overlaps prior cloud/systems work" | Novelty/delta doubt | Sharpen the delta against the nearest SoCC/OSDI/NSDI work |
| Split systems vs. data reviewer | The two halves disagree | Give the champion of each half a direct, evidenced answer |

The strategic reading: a SoCC paper wins when it satisfies **both** sponsoring communities, so
design the evaluation to answer a systems reviewer *and* a measurement reviewer, not one at the
other's expense.

## How SoCC differs from its siblings

- **vs. OSDI/SOSP:** those flagships set a higher clean-slate systems-novelty bar and use the
  USENIX/ACM systems process; SoCC's identity is the **cloud + data** framing and its explicit
  welcome of measurement and experience papers. Never assume a shared template or calendar.
- **vs. NSDI:** NSDI centers the network; SoCC centers the cloud *service and its data* running on
  the infrastructure. A datacenter-fabric paper is NSDI-shaped; a storage-service or scheduler
  paper is SoCC-shaped.
- **vs. EuroSys / ATC:** both are broad systems venues; SoCC narrows to cloud and adds the SIGMOD
  half of the reviewer pool. A paper with a genuine data-management dimension is read more
  natively at SoCC than at a pure-systems venue.
- **vs. a single-deadline venue:** SoCC's **two rounds** give a second chance within the year — but
  only to a *different* (or the same, next-year) paper, since a Round-1 reject cannot re-enter Round
  2.

## Who reads you

Expect a mix of systems and data-management reviewers. They check whether the deployment or trace is
real, whether tail latency and cost are reported (not just the mean), whether baselines are tuned,
and whether the measurement pipeline is reproducible. Because SoCC spans storage, scheduling,
serverless, big-data/ML infra, and cloud economics, a paper is usually matched to reviewers from its
own subarea on *both* sides — a thin evaluation or a hand-waved workload gets caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  subject tags spanning systems AND data -> the right dual pool (largest lever)
[Rebuttal]           factual corrections, a missing tail/cost number, a tuned-baseline result,
                     clarifying a misread workload -- the one written turn that moves borderlines
[Round choice]       submit to the round you can make strong; a Round-1 reject forfeits Round 2
[After reject]       no in-year resubmission; reroute to a sibling flagship or wait for next year
```

A rebuttal moves borderline papers when it corrects a factual misreading or supplies a number a
reviewer said was missing (a p99 figure, a cost breakdown, a tuned baseline); it does not move
papers when it argues taste. The PC discussion decides; the rebuttal is evidence for an advocate.

## Misreadings to avoid

- **Optimizing for one community** — a systems-perfect paper with a weak workload story loses the
  data reviewer, and vice versa.
- **Treating the rebuttal as a debate** — it is bounded evidence for the PC discussion, not a
  closing argument.
- **Reporting only averages** — tail and cost are first-class at a cloud venue.
- **Assuming Round 1 is a free trial** — a reject there costs the SoCC year.
- **Projecting last year's cadence** — round count, dates, and rebuttal format are set per edition.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / rebuttal / decided
[Round] round 1 / round 2, with the no-cross-round-resubmission rule noted
[Axis map] each review point -> systems (mechanism/deployment) | data (workload/measurement) | cost/tail | reproducibility
[Leverage plan] the rebuttal move that can actually change the outcome
[Forbidden moves] identity leak / unsupported new claims / Round-1 reject reused in Round 2
```

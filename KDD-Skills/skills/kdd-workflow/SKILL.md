---
name: kdd-workflow
description: Use when planning a KDD project calendar across the venue's two submission cycles per year, including cycle choice, abstract-then-paper deadline pairs a week apart, rebuttal capacity planning, the Resubmit-to-next-cycle loop, ADS evidence lead times, and ACM e-rights/TAPS camera-ready scheduling for SIGKDD.
---

# KDD Workflow

Use this as the project-management layer. KDD's calendar is structurally different
from single-deadline ML venues: **two cycles per year**, each with an abstract
deadline about one week before the paper deadline (2026 anchors: Jul 24/Jul 31, 2025
and Feb 1/Feb 8, 2026, AoE), a rebuttal window inside review, and a Resubmit outcome
that connects the cycles into a pipeline. Plan the pipeline, not a single date.

KDD is an ACM conference, not a journal: no standing editor, leadership rotates per
edition (the KDD 2026 committee roster lives on the conference site; individual names
待核实 before citing), and the cost surface is registration plus, under ACM Open,
a possible APC for authors at non-participating institutions — with a temporary 65%
ACM subsidy announced for 2026. Verify all money facts against current pages.

## Cycle-choice decision

| Situation | Choose | Reasoning |
|---|---|---|
| Evidence complete, paper drafted | Nearest cycle | Waiting adds staleness risk in fast subfields |
| Core result solid, ablations/scale runs missing | Next cycle | Rebuttal cannot carry links, so missing evidence has no delivery channel later |
| Prior cycle returned Resubmit | Next cycle, always declared | Addressed resubmissions carry better odds per the CFP; the forum id travels with you |
| ADS paper, launch too recent to measure | Cycle after the measurement window closes | The desk-check needs quantified post-launch numbers, not projections |

## Pipeline milestones (per cycle)

- **T-10 weeks — evidence lock plan**: four-axis experiment plan agreed
  (`kdd-experiments`); ADS measurement windows already running.
- **T-6 weeks — mechanism freeze**: no new components after this point; ablation
  matrix enumerable.
- **T-4 weeks — draft in acmart**: writing directly in the two-column format; scale
  runs queued (cluster time is the real deadline for large-data papers).
- **T-2 weeks — artifact freeze**: anonymized repository built fresh, cited in the
  PDF, smoke-tested on a clean machine (`kdd-artifact-evaluation`).
- **T-1 week — abstract deadline**: title/abstract/authors/track registered; all
  co-author OpenReview profiles complete (five-year history, DBLP, ORCID — chasing
  this is a named person's job).
- **T-0 — paper deadline**: submission audit (`kdd-submission`); ADS deployment
  quantification pointed to; resubmission declarations attached.
- **Review window — rebuttal capacity**: reserve author-days in advance; per-review
  responses under a link ban are writing-intensive (`kdd-author-response`).
- **Decision — branch**: Accept → e-rights + TAPS + APC status check
  (`kdd-camera-ready`); Resubmit → change-summary plan against the review contract;
  Reject → routing decision (`kdd-topic-selection`).

## The Resubmit loop as a plan

```yaml
# kdd-pipeline.yaml - one paper, tracked across cycles
paper: streamhive
track: research
cycle_history:
  - cycle: 2026-C1
    outcome: resubmit
    contract:            # concerns named in reviews = next cycle's spec
      - temporal-split rebuild (R2)
      - decay-mechanism ablation (R1)
      - scale claim beyond 10M edges (R3)
  - cycle: 2026-C2
    changes_summary_page: drafted   # mandatory first page of the PDF
    prior_forum_id: declared
    new_evidence: [table5_ablation, 2.1B_run, rebuilt_splits]
owners:
  profiles_gate: <name>       # co-author OpenReview completeness
  artifact_freeze: <name>
  rebuttal_window: <name, name>
```

The discipline: the review contract is written down the day reviews arrive, and every
contract item maps to a change-summary line before the next cycle's abstract deadline.

## Failure modes on this calendar

- Treating the abstract deadline as soft: at KDD it gates the submission and the
  track choice; a placeholder abstract in the wrong track is a real incident.
- Discovering an incomplete co-author profile on paper-deadline day — the one blocker
  that requires someone else's login to fix.
- Queuing the largest-scale run after the draft: at KDD the scale run *is* the
  contribution evidence, not a garnish, and clusters have queues.
- Winning a Resubmit and then re-litigating the reviews instead of executing the
  contract — the returning AC checks the named concerns first.
- Forgetting that notification and camera-ready dates for the current cycle were
  never verified (待核实) and promising co-authors a calendar the venue never
  published.

## Vignette: one paper, three cycles, two tracks

A team's trajectory that the pipeline model handles cleanly: Cycle 1, the sampling
method goes to Research and draws a Resubmit with three named concerns. Between
cycles, the method also ships inside the company's ranking system. Cycle 2 now offers
a fork: return the Research paper with the contract executed, or wait one more cycle
and submit the deployed system to ADS with a real measurement window. The pipeline
answer: do both, sequenced — Research resubmission in Cycle 2 (the contract items
are done and Resubmit standing decays with staleness), ADS submission the following
cycle once the post-launch window closes. Two papers, two tracks, no dual-submission
conflict, each riding the evidence it actually has (`kdd-topic-selection` governs the
fork; `kdd-related-work` governs the overlap declarations between them).

## Capacity planning numbers

Planning heuristics — replace with your team's observed values after one cycle:

- Rebuttal window: one author-day per review for text-only responses; double it if
  any new run is permitted and needed.
- Anonymized artifact build from a mature internal repo: 2-3 days including the
  clean-machine smoke test, dominated by de-identification review.
- ADS measurement window: whatever the CFP demands is a floor; credible pre/post or
  A/B windows are typically weeks, which is why the ADS decision happens a quarter
  early, not a deadline-month early.
- Profile-gate sweep across N co-authors: an hour of work, a week of waiting on
  other people — start it at abstract-minus-two-weeks.

## Output format

```text
[Pipeline stage] planning / evidence / drafting / submitted-C<k> / rebuttal / decision-branch
[Cycle target] <cycle + abstract/paper dates from current CFP, AoE>
[Critical path] <three tasks that decide readiness>
[Resubmit contract] <items + owners, or N-A>
[Money checks] ACM Open status / APC exposure / registration (待核实 items flagged)
[Owner map] profiles: <who> / artifact: <who> / rebuttal: <who>
```

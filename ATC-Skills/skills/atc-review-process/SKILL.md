---
name: atc-review-process
description: Use when reasoning about how an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) submission is evaluated — the two-round extended-abstract model, the round-one gate by two reviewers, the round-two read by 3-4 reviewers, double-blind reviewing, rebuttal, conditional acceptance with shepherding, and how ATC differs from OSDI/SOSP/NSDI.
---

# ATC Review Process

Model the pipeline before interpreting any single review. ATC's process is unusual among systems
venues in 2026 because it runs in **two rounds gated by a two-page extended abstract**, and because
acceptance is **conditional on a shepherd**. The most consequential mental shift for authors
arriving from a single-round conference is that **round one can end your submission before anyone
reads the full paper** — the extended abstract is not a formality.

## Process model

- Submission and review run on **HotCRP** (`atc26.hotcrp.com`) with **double-blind** anonymity:
  identities are mutually hidden through reviewing.
- **Round one:** each **two-page extended abstract** is read by **two experienced reviewers** with a
  broad systems perspective; abstracts below the bar are **rejected early**. The extended abstract is
  review-only and not published.
- **Round two:** papers that advance are read in full by **3-4 reviewers**, who weigh the
  significance and usefulness of the systems contribution, the soundness of the design, the honesty
  and completeness of the measurements, reproducibility, and clarity.
- **Rebuttal / description of changes:** authors get a short (about one page) window to correct
  factual misreadings and, where relevant, summarize revisions relative to a prior submission.
- **Decision + shepherding:** selected papers are **conditionally accepted**; final acceptance
  requires satisfying a **shepherd** (a PC member) on required revisions. Accepted papers publish in
  the **ACM DL under Open Access**.

## Reading a decision against the model

| Outcome | What it means | Author move |
|---|---|---|
| Early reject (round one) | The abstract did not convey a problem, contribution, and result that clear the bar | Reframe the abstract; the paper may be fine but the *pitch* failed — see `atc-writing-style` |
| Full review, then reject | A design or evidence gap survived the full read | Fix the substance, not the framing; consider a sibling venue |
| Conditional accept | Contribution holds; specific revisions required | Treat the shepherd's list as binding; make or explicitly justify each item |
| Reject with encouragement | Structural but repairable over a cycle | Rebuild the evidence and resubmit next cycle or reroute |

The strategic reading: because round one judges the abstract, **the highest-leverage editing on the
whole paper is often the two pages a round-one reviewer sees**. Write the submission so its problem
and result are legible before the details.

## How ATC differs from its siblings

- **vs. OSDI / SOSP:** those flagships are more selective and lean toward larger, novel systems; ATC
  takes a **broader, more practical** slice and welcomes solid, useful, well-measured work a
  flagship might call incremental. A paper bounced from OSDI on "not novel enough" can be a strong
  ATC paper if the engineering and measurement are real. Neither shares ATC's two-round
  extended-abstract gate.
- **vs. NSDI:** NSDI centers **networked systems** and runs its own multi-deadline model; ATC's
  scope is all of systems and its 2026 calendar is a single June deadline. Route a networked-systems
  design there if the network is the contribution.
- **vs. EuroSys:** EuroSys is the other broad, SIGOPS-affiliated systems conference; the choice is
  often calendar and community pull. Under SIGOPS, ATC and EuroSys now sit in the same family, so
  check both deadlines.
- **vs. pre-2026 USENIX ATC:** the old ATC ran a single-round review on a winter deadline with
  USENIX-funded open access and no APC. The 2026 SIGOPS edition changed the round structure, the
  calendar, and the cost model at once — do not carry the old process forward.

## Who reads you

Round one: two broad-perspective systems reviewers judging whether the idea and result are worth a
full read. Round two: 3-4 reviewers closer to your subarea who open the artifact, check whether the
measurements are end-to-end and honest about cost, and probe whether the baselines are fair. Vague
design descriptions and average-only results get caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  topic tags -> reviewer pool; a self-standing abstract -> surviving round one
[Round-one gate]     none after upload — the abstract is your only round-one argument
[Rebuttal]           factual corrections, a missing number a reviewer asked for, misread-claim fixes
[Conditional accept] the shepherd round: make every required change or justify declining it, evidenced
[After reject]       no appeal; reroute to a sibling systems venue or strengthen and resubmit
```

A rebuttal moves borderline papers when it corrects a factual misreading or supplies a measurement a
reviewer said was missing; it does not move papers by arguing taste. In the shepherd round, a
**silently skipped required change** is what turns a conditional accept into trouble.

## Misreadings to avoid

- **Treating the extended abstract as boilerplate** — it is the round-one decision surface.
- **Treating conditional acceptance as unconditional** — the shepherd can hold the paper until the
  required revisions land.
- **Assuming OSDI-style novelty is required** — ATC rewards solid, useful, measured systems work.
- **Projecting the old USENIX ATC process** — the round structure, calendar, and cost model changed
  in the SIGOPS transition.

## Output format

```text
[Process stage] pre-submission / round one / round two / rebuttal / conditional accept / final
[Decision driver] the criterion carrying the outcome (significance | soundness | evidence | clarity | reproducibility)
[Round-one readiness] does the extended abstract stand alone and clear the bar? yes/no
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak / unsupported new claims / skipping a shepherd-required change
```

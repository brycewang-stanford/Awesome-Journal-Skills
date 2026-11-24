---
name: atc-review-process
description: Use when reasoning about how an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) submission is evaluated — the two-round model whose first round reads the first two pages, the six round-one rejection criteria, the 72-hour author response, double-blind reviewing, conditional acceptance with shepherding, oral-vs-poster presentation, and how ATC differs from OSDI/SOSP/NSDI and from ATC 2026.
---

# ATC Review Process

Model the pipeline before interpreting any single review. ATC 2027 (call re-verified 2026-11-24)
runs **two rounds**, the first of which is **based on the paper's first two pages**, gives **every
paper a 72-hour author response**, and makes acceptance **conditional on a shepherd**. The most
consequential mental shift for authors arriving from a single-round conference is that **round one
can end your submission on the strength of two pages** — the opening is not a formality.

## Process model

- Submission and review run on **HotCRP** (`atc27.hotcrp.com`) with **double-blind** anonymity;
  submission deadline **19 January 2027, AoE**.
- **Round one:** reviewers read the **first two pages** (they may read further but need not;
  "depending on the number of submissions, the first round may involve more pages"). A paper is
  rejected in round one when it is clear that it is not systems work relevant to ATC, does not
  motivate the problem, has a main idea that is hard to understand, is too small or incremental,
  is poorly placed against related work, or is not rigorously evaluated (weak or inappropriate
  baselines, wrong workloads).
- **Round two:** papers that advance receive **additional reviews** weighing novelty, significance,
  interest, clarity, relevance, correctness, practicality, and accessibility to the broader systems
  community.
- **Author response:** optional, for all submissions, a **72-hour** window (opens **3 April 2027**,
  due **5 April 2027** end of day AoE). It may only correct factual errors or answer reviewer
  questions — no new experiments or data, no work done since submission, no promises, and no
  reliance on supplementary material the PC need not read.
- **Decision + shepherding:** notification **27 April 2027**; selected papers are **conditionally
  accepted** and final acceptance requires a **shepherd's** approval of required revisions;
  camera-ready **28 May 2027**. Every accepted paper is presented **orally and/or as a poster** —
  not all get an oral slot — and one author must attend in Rennes. Papers of particular merit are
  forwarded to **ACM TOCS** and **CACM Research Highlights**. Proceedings are **ACM Open Access**.

## Reading a decision against the model

| Outcome | What it means | Author move |
|---|---|---|
| Round-one reject | The first two pages did not show scope, motivation, idea, delta, positioning, and evaluation clearing the bar | Rewrite the opening; the paper may be fine but the *first two pages* failed — see `atc-writing-style` |
| Full review, then reject | A design or evidence gap survived the full read and the response | Fix the substance, not the framing; consider a sibling venue |
| Conditional accept | Contribution holds; specific revisions required | Treat the shepherd's list as binding; make or explicitly justify each item |
| Poster rather than oral slot | Logistics and program size, not a lower tier | Prepare the poster as seriously as a talk; one author still attends |

The strategic reading: because round one judges the opening, **the highest-leverage editing on the
whole paper is the first two pages**. Write the submission so its problem, idea, and evidence are
legible before the details.

## How ATC differs from its siblings — and from itself

- **vs. OSDI / SOSP:** those flagships are more selective and lean toward larger, novel systems; ATC
  takes a **broader, more practical** slice and welcomes solid, useful, well-measured work a
  flagship might call incremental — though "too small or incremental" is now an explicit round-one
  reject reason, so the delta must be stated by page 2.
- **vs. NSDI:** NSDI centers **networked systems** and runs its own two-deadline model; ATC's scope is
  all of systems with a single January deadline in 2027. Route a networked-systems design there if
  the network is the contribution.
- **vs. EuroSys:** EuroSys is the other broad, SIGOPS-family systems conference (two cycles a year,
  April meeting); the choice is often calendar and community pull, so check both deadlines.
- **vs. ATC 2026:** the first SIGOPS edition (Hong Kong, November 2026, June deadline) judged a
  separate **two-page extended abstract** in round one and excluded appendices from the page limit.
  ATC 2027 drops the extended abstract, counts appendices, and caps each author at two submissions.
- **vs. USENIX ATC (retired after ATC '25):** single-round review on a winter deadline with
  USENIX-funded open access and no APC — do not carry that process forward.

## Who reads you

Round one: broad-perspective systems reviewers deciding, from two pages, whether the paper is worth
a full read. Round two: reviewers closer to your subarea who open the artifact, check whether the
measurements are end-to-end and honest about cost, and probe whether the baselines are fair. Vague
design descriptions and average-only results get caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  topic tags -> reviewer pool; first two pages -> surviving round one
[Round-one gate]     none after upload — the opening is your only round-one argument
[Author response]    72 hours: factual corrections and direct answers to reviewer questions only
[Conditional accept] the shepherd round: make every required change or justify declining it, evidenced
[After reject]       no appeal; reroute to a sibling systems venue or strengthen and resubmit
                     (with the one-page change summary ATC asks of resubmissions)
```

A response moves borderline papers when it corrects a factual misreading or points to evidence
already in the paper that a reviewer missed; it cannot add new measurements. In the shepherd round,
a **silently skipped required change** is what turns a conditional accept into trouble.

## Misreadings to avoid

- **Back-loading the argument** — round one may never see page 3.
- **Using the response to add results** — the call forbids new experiments and data.
- **Treating conditional acceptance as unconditional** — the shepherd can hold the paper until the
  required revisions land.
- **Assuming OSDI-style novelty is required** — ATC rewards solid, useful, measured systems work.
- **Projecting ATC 2026 or USENIX ATC** — round structure, calendar, page accounting, and the author
  cap all changed.

## Output format

```text
[Process stage] pre-submission / round one / round two / author response / conditional accept / final
[Decision driver] the criterion carrying the outcome (scope | motivation | clarity | delta | positioning | evaluation)
[Round-one readiness] do the first two pages stand alone and clear the six criteria? yes/no
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak / new data in the response / skipping a shepherd-required change
```

---
name: ppopp-review-process
description: Use when reasoning about how a PPoPP submission is evaluated, covering double-blind review, the Program Committee plus External/Extended Review Committee model, TPMS reviewer matching, the author-response rebuttal, the accept/reject decision with automatic poster consideration, and how PPoPP's process differs from PLDI's and CGO's.
---

# PPoPP Review Process

Model the pipeline before interpreting any single review. PPoPP runs a **single-round, double-blind
conference review** with a **scheduled author-response rebuttal** and an unusual safety net:
papers not accepted for a talk are **automatically considered for posters**. The most consequential
mental shift for authors arriving from a journal-style venue is that there is (as verified) no
guaranteed revise-and-resubmit round — the rebuttal is your one written turn, so it must land.

## Process model

- Submission and review run on **HotCRP** with **double-blind** anonymity: author identities are
  hidden from reviewers and reviewer identities from authors.
- Papers are read by the **Program Committee** and an **External/Extended Review Committee (ERC)**;
  declare conflicts against **both** pools. Reviewer assignment may use the **Toronto Paper Matching
  System (TPMS)**, so your abstract and topic tags shape who reads you.
- After the initial reviews there is a fixed **author-response period** (PPoPP 2026: 27–29 October
  2025). Authors respond within a word cap; reviewers then discuss and decide.
- The primary decision is **accept / reject** for a regular presentation. Whether an explicit
  intermediate **"Revision"** category is offered in a given cycle is 待核实 — do not assume it.
- **Automatic poster consideration:** submissions not accepted for a talk are automatically
  considered for the poster track, with a **two-page summary in the proceedings**.

## What PPoPP reviewers weigh

| Axis | What they check | Common failure |
|---|---|---|
| Parallelism as the contribution | Is the concurrency/parallel-performance the point? | A compiler/theory result wearing a parallel costume (a CGO/POPL reroute) |
| Correctness under concurrency | Races, linearizability/progress, the memory model | "It passed my tests" with no argument about interleavings |
| Scalability | Speedup curves, core sweeps, NUMA/GPU, saturation | One thread count; a win that vanishes on another topology |
| Baseline honesty | Comparison to the strongest real competitor | Beating a strawman or the authors' own unoptimized code |
| Measurement rigor | Variance, warm-up, pinning, repeated runs | A single-run bar chart with no error bars |
| Reproducibility | Enough to re-run; an artifact | Hardware and topology unstated |

## Reading a decision

| Decision | What it means | Author move |
|---|---|---|
| Accept (talk) | Contribution and evidence hold | Camera-ready + artifact; do not reopen scope |
| Poster (auto-considered) | The idea is of interest but not a full talk this cycle | Decide in advance whether the 2-page proceedings summary is worth it |
| Reject | Structural: wrong scope, weak baseline, no scaling story | Reframe or reroute (CGO/PLDI/ASPLOS/SC or a later round) |
| "Revision" (if offered — 待核实) | Repairable gaps within a bounded window | Treat as an R&R; make or explicitly decline every request with evidence |

The strategic reading: because there is (as verified) one written turn, design the submission so
its weakest point is **answerable in the rebuttal with a number you already have** (a pre-run
baseline, an extra core-count) rather than something requiring a month of new machine time.

## How PPoPP differs from its siblings

- **vs. PLDI/CGO:** those judge a language/compiler contribution; PPoPP judges the parallel-program
  behavior. A great pass with a thin scaling story fails here and would pass there. Different
  template too (PPoPP two-column `acmart` `sigplan`, 10 pages).
- **vs. POPL:** POPL rewards the concurrency *proof* itself; PPoPP wants the proof *plus* a measured
  parallel system. A pure logic is a POPL paper.
- **vs. ASPLOS/HPCA:** those own the machine; a PPoPP reviewer reads your hardware as the platform,
  not the result, and will discount a win that is really a microarchitecture artifact.

## Where author leverage actually exists

```text
[Before submission]  abstract + topic tags -> TPMS/PC matching        (largest early lever)
[Initial reviews]    factual corrections, a pre-run number, a clarified interleaving argument
[Rebuttal]           the decisive turn: answer "does it scale?" and "baseline X?" with data
                     already in hand, within the word cap
[After reject]       no appeal; reroute to a co-located sibling or the next round
```

A rebuttal moves borderline papers when it supplies a scaling point or a baseline a reviewer said
was missing; it does not move papers when it argues taste or promises future experiments. The
classic PPoPP loss is a reviewer asking "how does this behave at 128 cores / on a second GPU?" and
the authors having only the one machine's numbers.

## Reading a review packet

Weight reviews before answering. A review that cites your speedup figure, your baseline choice, and
your correctness argument was read closely; answer each reviewer on the axis they raised —
correctness reviewers with an interleaving argument, performance reviewers with a number. A review
that only questions novelty has left soundness to the others; do not spend your word budget there.

## Misreadings to avoid

- **Assuming a revise-and-resubmit safety net** — as verified there is one written turn; the
  rebuttal is not a placeholder.
- **Treating the poster path as failure** — the two-page proceedings summary is a real, citable
  outcome; decide about it deliberately.
- **Ignoring the ERC** — external reviewers carry real weight and real conflicts.
- **Projecting last year's cadence** — round count, rebuttal timing, and any "Revision" category
  are decided per edition.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / rebuttal / decided
[Decision] accept / poster / reject / revision(if offered), with the driving criterion
[Criterion map] each review point -> parallelism-as-point | correctness | scalability | baseline | measurement | reproducibility
[Leverage plan] the rebuttal number or correction that can actually change the outcome
[Forbidden moves] identity leak / promised-but-unrun experiments / arguing taste
```

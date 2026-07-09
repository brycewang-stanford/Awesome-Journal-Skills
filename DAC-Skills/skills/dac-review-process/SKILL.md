---
name: dac-review-process
description: Use when reasoning about how an ACM/IEEE Design Automation Conference (DAC) Research Manuscript is evaluated, covering double-blind TPC review, the novelty-plus-QoR decision criteria, program-committee discussion, the accept/reject (no major-revision) outcome, the ~20-25% selectivity, and how DAC's industry-facing, single-shot process differs from the architecture venues' rebuttal-and-revision cycles.
---

# DAC Review Process

Model the pipeline before interpreting any single review. DAC's Research-Manuscript review is
**double-blind, Technical-Program-Committee-driven, and single-shot**: papers are reviewed against
novelty and measured design-quality impact, discussed by the committee, and get a binary
**accept/reject** — there is no journal-style Major Revision round. Anchor to the DAC 2026 cycle
facts in `resources/official-source-map.md`.

## Process model

- Submission and review run on **Softconf/START** with **double-blind** anonymity: reviewers do not
  see author identities, and the manuscript must be scrubbed of identifying content.
- Each paper is read by multiple **TPC** members drawn from the relevant subcommittee (physical
  design, logic synthesis, verification/test, ML-for-EDA, security, embedded, etc.). Reviewers
  weigh **novelty over prior art, technical soundness, the strength and fairness of the QoR
  evidence, relevance/impact to design automation, and clarity**.
- The committee **discusses** borderline papers to reach the final verdict; a strong advocate who
  can answer the objections carries a paper through discussion.
- Decisions are essentially **accept or reject** (a fraction may be steered to a poster/LBR-style
  outcome per cycle — **待核实**). There is **no revise-and-resubmit within the cycle**; a rejected
  paper reroutes to ICCAD/DATE/ASP-DAC or a journal.
- Research selectivity is historically **~20-25%** (verify each cycle).

## Reading a decision against the criteria

| Signal in the reviews | Underlying criterion | Author reality |
|---|---|---|
| "Incremental over [prior tool]" | Novelty | Structural; the delta must be reframed or the idea extended before reroute |
| "Baseline is weak / untuned" | Evidence fairness | Often fatal at DAC — the QoR comparison is the paper |
| "Only private benchmarks" | Evidence credibility | Add a recognized suite; results on toy circuits do not persuade |
| "Runtime/scalability unclear" | Soundness/impact | EDA reviewers care about scaling to realistic design sizes |
| "Unclear where the gain comes from" | Soundness | Missing ablation isolating the contribution |

## Novelty-plus-QoR: the DAC bar

DAC is an *engineering* research venue: a beautiful idea with no measured QoR advantage rarely
survives, and a large QoR number with thin novelty gets read as an engineering result, not a
research contribution. Winning papers pair **a genuinely new mechanism** with **a fair,
benchmark-grounded QoR gain** (PPA, wirelength, timing slack, coverage, or runtime) over the
**strongest** prior technique. The most common reject cause is not a broken idea but an
**unconvincing comparison** — a baseline the reviewer does not accept as state of the art or as
fairly tuned.

## How DAC differs from its siblings

- **vs. ISCA / MICRO / HPCA (architecture):** those venues run author **rebuttals** and, in some
  years, revision rounds, and reward microarchitectural novelty. DAC's research review has
  historically been **TPC-driven without a standing author-response period** (**待核实** for DAC
  2026) and rewards **design-automation** novelty measured in QoR. Do not carry an architecture
  rebuttal playbook into DAC.
- **vs. FSE / ICSE (software):** no journal-style Major Revision, no ACM artifact-badging track, and
  a much tighter **6+1-page** budget. DAC evidence is QoR on EDA benchmarks, not empirical-SE
  studies.
- **vs. ICCAD / DATE / ASP-DAC (sibling EDA):** overlapping reviewer pools and criteria but
  **different calendars and committees** — a DAC reject is a natural ICCAD/DATE/ASP-DAC candidate,
  but never assume shared deadlines or that the same reviewers see it.

## Who reads you

Expect subarea-matched EDA experts who will check whether your **baseline is the real state of the
art**, whether the **benchmarks are standard and reported honestly** (all circuits, not a
cherry-picked subset), whether **runtime and scalability** are credible for realistic designs, and
whether an **ablation** shows the gain comes from your mechanism. Vague "we improve QoR" claims
without per-benchmark tables get caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  topic/subcommittee tags + a real abstract -> reviewer pool   (largest lever)
[Manuscript]         a fair, tuned, state-of-the-art baseline on standard benchmarks + an ablation
[Discussion]         a champion reviewer who can answer the objections carries the paper
[After reject]       no appeal; reroute to ICCAD/DATE/ASP-DAC or TCAD/TODAES with the reviews addressed
```

Because DAC has historically had **no author rebuttal**, the leverage is almost entirely
**front-loaded**: you cannot talk a reviewer out of a weak-baseline finding after submission, so the
baseline and benchmark choices must be unimpeachable *before* the November deadline.

## Misreadings to avoid

- **Expecting a rebuttal to save the paper** — do not budget on a response window DAC may not run.
- **Treating a big QoR number as sufficient** — without novelty it reads as an Engineering-Track
  result.
- **Assuming one champion is enough without evidence** — the discussion turns on answers to the
  other reviewers' concrete objections, not enthusiasm.
- **Projecting last year's process** — deadline, selectivity, and whether any response step exists
  are decided per edition.

## Output format

```text
[Process stage]  pre-submission / under review / decided
[Decision driver] novelty | evidence fairness | benchmark credibility | scalability | clarity
[Criterion map]  each review point -> which criterion it invokes
[Leverage plan]  the pre-submission action (baseline/benchmark/ablation) that would have moved it
[Reroute target] ICCAD / DATE / ASP-DAC / TCAD if rejected, with the fix to make first
```

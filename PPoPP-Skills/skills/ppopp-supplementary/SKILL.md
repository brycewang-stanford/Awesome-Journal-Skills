---
name: ppopp-supplementary
description: Use when deciding what belongs in a PPoPP paper's 10 reviewed pages versus the artifact or appendix, splitting content by decision-criticality so proofs, full core sweeps, and correctness arguments that determine acceptance stay legible in the body, while bulk data and extended runs move out.
---

# PPoPP Supplementary

Decide what lives in the **10 reviewed pages** (text and figures, two-column `acmart`) and what
moves to the artifact or an appendix. The governing rule at PPoPP is **decision-criticality**:
anything a reviewer must read to be convinced the result is **correct under concurrency** and
**scales** stays in the body. References are unlimited and free; body space is the scarce resource.

## The decision-criticality test

For each candidate piece of content, ask: *would a reviewer's accept/reject change if they could
not see this?*

```text
[Decides acceptance]  the correctness argument's core, the headline scaling curve, the baseline
                      comparison, the key design insight  -> BODY (inside 10 pages)
[Supports/confirms]   full linearizability proof details, every core-count data point, additional
                      workloads, sensitivity sweeps, extra GPUs  -> ARTIFACT / APPENDIX
[Bulk / mechanical]   raw logs, per-run tables, generator internals, build scripts  -> ARTIFACT
```

The failure mode PPoPP punishes is burying a load-bearing argument — the linearization points, the
one plot that shows saturation — outside the reviewed pages, so the reviewer cannot judge the claim
and defaults to skepticism.

## What must stay in the body

- **The correctness argument's spine.** The property (linearizability/progress), the linearization
  points or the key invariant, and why it holds under the named memory model. The full formal proof
  can move; the argument a reviewer needs to believe it cannot.
- **The headline scaling evidence.** At least one clear speedup/throughput curve over core or thread
  count, with the baseline and machine named in the caption.
- **The baseline comparison** that substantiates the delta over prior work.
- **The design insight** that makes the parallelism work — the idea, not every implementation
  detail.

## What can move out

- **Full proofs and case analyses** — keep the argument in the body, push the exhaustive case split
  to an appendix or the artifact.
- **Complete sweeps** — the body shows the representative curve; the artifact holds every thread
  count, socket configuration, input size, and GPU.
- **Additional workloads and sensitivity studies** that confirm rather than establish the claim.
- **Reproduction machinery** — Dockerfiles, scripts, raw data, and per-run numbers belong in the
  artifact (see `ppopp-artifact-evaluation`).

## Where "out" is at PPoPP

- **The artifact** is the primary home for bulk evidence and is evaluated **post-acceptance** —
  reviewers of the paper are not obligated to run it, so it cannot carry a decision-critical claim
  at review time.
- **An appendix**, if the call permits one within submission rules, is read at the reviewer's
  discretion — do not put anything acceptance-deciding there and assume it was read. Confirm the
  current appendix policy each cycle (待核实 if unstated).

Because the artifact is post-acceptance, the split at PPoPP is stricter than at venues that review
the artifact alongside the paper: if the reviewer must see it to say yes, it is in the 10 pages.

## Keeping the body legible under the page cap

- Use **small multiples** to compress a core sweep into one figure rather than five.
- Move exhaustive tables to the artifact and keep a summarizing plot in the body.
- Cut prose before cutting evidence; the correctness argument and the scaling curve are the last
  things to shrink.

## Output format

```text
[Body (<=10pp)] correctness spine + headline curve + baseline + design insight all present?
[Moved out] proofs-detail / full sweeps / extra workloads / repro machinery -> artifact/appendix
[Decision-critical check] anything acceptance-deciding placed outside the body? (must be none)
[Appendix policy] permitted this cycle? confirmed / 待核实
[Space recovered] figures merged / tables moved to hit 10 pages
```

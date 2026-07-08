---
name: mlsys-supplementary
description: Use when deciding what goes into an MLSys appendix versus the 10-page body, exploiting the venue's unlimited separately-uploaded appendix that reviewers are not required to read, organizing configs, traces, extended results, and anonymized code pointers, and keeping supplementary material blinded for the research track.
---

# MLSys Supplementary

Use this when splitting a Conference on Machine Learning and Systems submission between
body and appendix. The 2026-cycle mechanics (verified 2026-07-08): appendices are
**unlimited in length**, uploaded as a **separate file** from the main paper, due at the
same time — and reviewers are **explicitly not required to read them**. That last clause
is the design constraint everything below follows from.

## The governing rule

The 10-page body must win the paper's acceptance alone. The appendix exists to survive
audits — a skeptical reviewer checking one specific configuration — and to serve future
readers and artifact evaluators. Anything that must be *believed* for acceptance goes in
the body; anything that must be *checkable* can go behind it.

## Placement decision table

| Material | Body or appendix? | Reasoning |
|---|---|---|
| Headline comparison + strongest ablation | Body, always | Reviewers judge only what they must read |
| Full hyperparameter/configuration matrices | Appendix, cross-referenced | Audit material, not narrative |
| Baseline tuning protocol and budgets | Body (one paragraph) + appendix (full grid) | Fairness is decision-critical; the grid is evidence |
| Per-workload result breakdowns beyond the headline | Appendix table, body sentence summarizing spread | Spread claim needs body presence; rows do not |
| Workload/trace characterization (rates, lengths, mixes) | Body figure if representativeness is contested; else appendix | Representativeness is a top MLSys objection |
| Additional hardware generations or precision modes | Appendix | Strengthens generality without carrying the claim |
| Failure cases and non-wins | Body, briefly | Honesty here is scored; hiding it in the appendix reads as burying |
| Proof sketches for any theoretical guarantee | Body sketch, appendix proof | Same convention as ML venues |
| Artifact/repository description | Appendix (anonymized for research track) | Feeds later artifact evaluation |

## Structuring the appendix file

Because it is a separate upload, the appendix must be navigable without the body open:

- Start with a half-page map: appendix section → the body section and claim it supports.
- Number appendix sections A, B, C... and cross-reference each at least once from the
  body ("full grid in App. B"); un-pointered appendix content is effectively invisible.
- Restate the experimental setup header (hardware, workloads) at the top rather than
  assuming the reviewer has the body's Section 5 in memory.
- Keep figures self-captioning: every axis, unit, and trial count readable standalone.

```text
appendix.pdf
├── A. Claims map (body claim -> appendix evidence)
├── B. Full system + baseline configurations
│     B.1 our system   B.2 baseline-1 (tuning grid)   B.3 baseline-2
├── C. Workload characterization (trace statistics, generation scripts described)
├── D. Extended results (per-workload, per-hardware, per-precision)
├── E. Sensitivity and additional ablations
├── F. Anonymized artifact description (layout, run commands, hardware needs)
└── G. Proofs / analytical model derivations (if any)
```

## Anonymity in supplementary material (research track)

- The appendix is part of the double-blind submission: no author names, affiliations,
  cluster hostnames, internal project codenames, or company-identifying trace fields.
- Scrub trace data specifically — production traces leak identity through service
  names, datacenter labels, and timestamp patterns. Rename fields and state that you did.
- Code pointers must go to anonymized mirrors; the real repository appears only at
  camera-ready and artifact evaluation.
- Industrial-track supplements follow that track's looser rule (company identity may
  remain; author names may not) — do not mix the two tracks' standards.

## Worked split: an inference-compiler submission

A fictional paper contributes a compiler pass that fuses attention variants, claiming
1.5-1.9x kernel speedups and 1.2x end-to-end serving gains across three model families.

- Body keeps: the fusion legality insight and the pass algorithm (compressed to one
  figure plus one column), the end-to-end serving comparison under a stated latency
  constraint, the kernel-level speedup summary across families, one ablation isolating
  the fusion from unrelated codegen wins, and the non-win (no gain on short sequences,
  stated with the mechanism reason).
- Appendix takes: per-operator speedup tables for all 40 fused patterns, the full
  autotuning search configuration, correctness-test methodology against reference
  kernels, results on a second GPU generation, and the anonymized artifact description.
- The one judgment call: the correctness methodology gets a two-sentence summary in the
  body — a compiler paper that never says how it validated correctness invites the
  objection no appendix can pre-empt, because the appendix may never be opened.

The test of the split: hand a colleague only the 10-page body and ask them to argue for
acceptance; every point where they reach for the appendix is a misplacement.

## Common failure modes

- **The outsourced paper**: body asserts, appendix proves, reviewer reads only the body
  and scores the assertions as unsupported. Pull the single strongest piece of evidence
  for each major claim forward.
- **The stale appendix**: body numbers get regenerated at the deadline, appendix tables
  do not, and a careful reviewer finds the mismatch. Build both from the same logs in
  the same script run.
- **The dumping ground**: forty pages of unreferenced plots signal an unfiltered
  experiment log, not scholarship. Every appendix element should answer a question a
  reviewer might actually ask.
- **The forgotten upload**: the appendix is a separate file with the same deadline —
  assign its upload explicitly; it is not attached to the paper PDF automatically.

## Interaction with later stages

The appendix outlives review. The configuration matrices and workload characterization
you file now become the skeleton of the Artifact Appendix at evaluation time
(`mlsys-artifact-evaluation`), and the camera-ready version de-anonymizes rather than
rewrites it — so write appendix sections as if a stranger will execute them in six
months, because at this venue one probably will. Conversely, anything you promise in
the author response ("full sweep in the appendix") must land there by camera-ready;
keep a promises ledger.

## Cycle-volatility warning

The separate-upload mechanic, unlimited length, and same-deadline rule are 2026-cycle
facts; earlier cycles differed and the next may too. Confirm the current Call for
Research Papers wording before finalizing the split.

## Output format

```text
[Split status] body-sufficient / body-dependent-on-appendix (fix) / not ready
[Claims map] <major claim -> body evidence -> appendix backup>
[Appendix structure] <sections present + cross-reference check>
[Anonymity sweep] <traces/configs/code pointers cleaned?>
[Consistency] <body and appendix generated from same logs? y/n>
[Upload owner] <person responsible for the separate file>
```

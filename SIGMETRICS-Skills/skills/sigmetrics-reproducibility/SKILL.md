---
name: sigmetrics-reproducibility
description: Use when strengthening ACM SIGMETRICS reproducibility, covering proofs and their assumptions as reproducible artifacts, seeded simulators whose figures regenerate and match the analysis, measurement/trace provenance, claim-to-evidence mapping, honest degrees of reproducibility, and consistency between what the paper proves/measures and what the artifact contains.
---

# SIGMETRICS Reproducibility

Use this before submission and again before the POMACS camera-ready. SIGMETRICS reproducibility has
a distinctive shape: the "artifact" is often a **proof plus a simulator plus a trace**, not only
running code. The goal is that a competent reader could re-derive your bound, re-run your simulation
to the same curves, and re-analyze your measurement to the same conclusions.

## Evidence map

- Map each theorem, bound, and reported number to a **verifiable location** — a proof in an
  appendix, a figure regenerated from a seeded simulation, or a script that turns the trace into the
  table.
- For analytic results, give the **full derivation and every assumption**; a reader should be able
  to check the proof and see which assumptions each step uses.
- For simulations, ship a **seeded simulator** whose scripts regenerate each figure *and* overlay
  the analytic prediction, so a reviewer sees model and measurement agree.
- For measurement studies, document the trace source, collection window, sanitization, and the
  processing scripts; archive the processed dataset or document access.
- Keep the paper and the artifact **consistent**: a p99 number in the PDF that no simulator run
  reproduces is the contradiction reviewers read as carelessness.

## Reproducibility-claim audit

| Claim in the paper | Weak reproducibility answer | SIGMETRICS-ready answer |
|---|---|---|
| "Theorem 1 bounds the tail" | Proof sketch only | Full proof (appendix) + a simulation that matches the analytic curve |
| "We simulate policy X" | "Simulator available on request" | Seeded simulator + scripts that regenerate each figure from logged runs |
| "We measured system Y" | "Data on request" | Processed dataset (or documented access) + provenance + processing scripts |
| "The learner has low regret" | Empirical curve only | Regret proof + code plotting empirical regret against the bound |

"Available on request" is treated as *not available*; convert every such line into a concrete,
anonymized artifact or an explicit, justified exception (e.g. a proprietary trace, with the
methodology fully documented).

## Provenance and determinism pinning

```text
[Proof]       state every assumption; give the full derivation; note which lemmas each step needs
[Simulation]  log seeds; state steady-state/warm-up handling; make figures regenerate deterministically
[Measurement] pin the trace source, collection window, sanitization; archive processed data
[Compute]     state hardware, runtime, and number of independent runs so a reader can size a rerun
[Agreement]   ship the overlay of analysis vs. simulation so the match is reproducible, not asserted
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command regenerates each figure/table from logged simulation runs and
  reproduces the analytic overlay.
- **Scripted:** scripts exist but require documented manual steps or access to a restricted trace.
- **Descriptive:** proofs and methodology detailed enough that a competent reader could rebuild the
  pipeline.

For SIGMETRICS, aim turnkey for anything a reviewer might rerun quickly (a simulation regenerating a
figure, a script producing a table); a proprietary industrial trace may stay scripted with access
documented, but the *methodology and the analysis code* should still be turnkey.

## Vignette: a queueing-theory-plus-measurement paper

Consider a paper with a scheduling theorem and a trace-driven evaluation. Its reproducibility spine:
the full proof with stated assumptions in an appendix; a seeded simulator whose notebook regenerates
the analysis-vs-simulation figure; the trace-processing scripts with pinned provenance; the
anonymized processed dataset (or documented access to a restricted one); and the analysis notebooks
that turn logged runs into the paper's tables — plus one honest sentence about any assumption that
only approximately holds and how §6 bounds it.

## Consistency and camera-ready pass

- Before submission: every reported number traces to a proof, a logged simulation run, or a
  measurement script; the artifact is anonymized (no owner strings, cluster paths, group names).
- Before camera-ready: swap anonymized links for a permanent, DOI-issuing archive, and align the
  artifact with any ACM badges you are pursuing (`sigmetrics-artifact-evaluation`).

## Output format

```text
[Claim inventory] <claim -> proof / simulation run / measurement script>
[Reproducibility] concrete / vague / missing, per claim
[Provenance gaps] <proof assumptions stated? seeds logged? trace provenance pinned?>
[Reproducibility level] turnkey / scripted / descriptive, stated honestly
[Paper fixes] <must appear in the PDF/appendix>
[Artifact fixes] <additions before upload>
```

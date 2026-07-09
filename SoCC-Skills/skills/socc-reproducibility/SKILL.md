---
name: socc-reproducibility
description: Use when strengthening ACM SoCC reproducibility, covering the testbed and workload description, released code and traces, provenance pinning for measurement studies, reproducing tail-latency and cost (not just the mean), claim-to-evidence mapping, honest degrees of reproducibility, and consistency between what the paper reports and what the artifact regenerates.
---

# SoCC Reproducibility

Use this before submission and again before camera-ready. SoCC — the joint SIGMOD+SIGOPS cloud
symposium — is read by reviewers who expect an inspectable measurement trail: the SIGOPS half wants
to believe the system runs, and the SIGMOD half wants to believe the numbers. The goal is that a
competent reader with a comparable testbed could rebuild your evidence and reach your conclusions —
including the **tail latency and cost**, not just the average.

## Evidence map

- Map each cloud claim and reported number to a **verifiable location** — a paper section, a figure
  generated from logged runs, or a script in the artifact.
- For systems, give enough of the mechanism, configuration, and **testbed** (node counts, instance
  types, OS/kernel, network) that a reader could re-deploy and re-measure.
- For measurement/trace studies, report the trace provenance, extraction date, filtering, the
  workload replay, metrics, and the analysis scripts.
- Reproduce **tail and cost**: percentiles (p95/p99/p99.9), the pricing model behind any cost claim,
  and the number of runs and variance — the mean alone is not a cloud result.
- Keep the paper and the artifact **consistent**: a number in the PDF that no script regenerates is
  the contradiction reviewers read as carelessness.

## Reproducibility statement audit

| Claim in the paper | Weak answer | SoCC-ready answer |
|---|---|---|
| "We evaluate on a production trace" | "Trace available on request" | Anonymized (then released) trace + the replay harness and extraction date |
| "Our system improves throughput" | "Code will be released" | Anonymized, runnable system with a testbed description and a small demo |
| "We cut cost by X" | A single cost number | The pricing model, the instance-seconds logged, and the script that computes it |
| "p99 stays within target" | Mean latency only | Per-run tail percentiles with variance and run count |
| "Scales to N nodes" | One large run | A scaled reproduction path plus the full-scale logs |

"Available on request" is treated as *not available*; convert every such line into a concrete,
anonymized (then released) artifact or an explicit, justified exception (e.g., a confidential
production trace, with a synthetic generator provided instead).

## Provenance pinning

```text
[Measurement] pin commit SHAs; record trace extraction dates; archive the replayed trace or a
              faithful generator, not just a query or a pointer
[Testbed]     record node counts, instance types, OS/kernel versions, network, and the run count;
              a cloud result that cannot be re-deployed cannot be reproduced
[Cost]        state the pricing model and the source of every cost figure so a reader can recompute
[Tail]        log per-request or per-run latency distributions, not only aggregates
[Randomness]  log seeds for stochastic components; say what is and is not deterministic
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command regenerates each figure (including tail and cost) from logged
  runs, at least at reduced scale.
- **Scripted:** scripts exist but require a specific testbed, documented manual steps, or restricted
  trace access.
- **Descriptive:** prose and configuration detailed enough that a competent reader could rebuild the
  deployment and measurement pipeline.

For SoCC, aim turnkey for anything an evaluator could rerun at small scale (a short trace replay, a
tail/cost plot from logged runs); full-cluster or proprietary-trace results may stay scripted with
access clearly documented. Stating the achieved level honestly beats promising turnkey behavior that
fails on someone else's testbed.

## Vignette: a scheduling measurement paper

Consider a paper measuring a new scheduler on a replayed production trace. Its reproducibility spine:
the scheduler code with pinned SHAs; the replay harness and the (anonymized, then released) trace
with its extraction date; the testbed description (nodes, instance types, kernel); the measurement
scripts that turn raw logs into the throughput, p99, and cost figures; the run count and variance;
and one honest sentence about the parts (a confidential production trace, the full cluster) that
cannot be shared and what synthetic or scaled substitute is provided.

## Consistency and camera-ready pass

- Before submission: every reported number traces to the artifact; the reproducibility statement
  matches reality; the artifact is anonymized (no cluster names, provider hints, or trace
  provenance that reveals identity).
- Before camera-ready: swap anonymized links for permanent, DOI-issuing archives, and align the
  statement with the ACM badges you are pursuing if the edition offers evaluation
  (`socc-artifact-evaluation`).

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Reproducibility statement] concrete / vague / missing
[Provenance gaps] <trace SHAs+dates / testbed description / cost model / tail logging / seeds>
[Tail + cost] reproducible, not just the mean? yes/no
[Reproducibility level] turnkey / scripted / descriptive, stated honestly
[Paper fixes] <must appear in the PDF>
[Artifact fixes] <additions before upload>
```

---
name: edbt-reproducibility
description: Use when strengthening EDBT reproducibility for a database-systems paper, covering a runnable artifact, pinned environments and workloads, dataset and query-log provenance, claim-to-evidence mapping, honest degrees of reproducibility, and consistency between the paper and the package for the open-access OpenProceedings record.
---

# EDBT Reproducibility

Use this before submission and again before camera-ready. EDBT's community has a
reproducibility-forward culture, and the published record is **open access on OpenProceedings** —
so an inspectable, re-runnable package raises a paper's standing and, for an **Experiments &
Analysis** paper, *is* the contribution. The goal is that a competent reader could rebuild your
measurements and reach your conclusions.

## Evidence map

- Map each claim, mechanism, and reported number to a **verifiable location** — a paper section, a
  table generated from a logged run, or a script in the artifact.
- For a mechanism, give enough of the algorithm, data structures, parameters, and system integration
  that a reader could reimplement or rebuild it.
- For an evaluation, report workloads and their derivation, dataset versions and sources, the
  measurement harness, metrics, and the analysis scripts.
- Keep the **availability statement** truthful and specific: what is shared, the workloads and data,
  the hardware assumptions, and — if something cannot be shared — exactly why.
- Keep the paper and the artifact **consistent**: a number in the PDF that no script produces is the
  contradiction reviewers read as carelessness.

## Availability statement audit

| Claim in the paper | Weak availability answer | EDBT-ready answer |
|---|---|---|
| "We evaluate on workload W" | "Data available on request" | Archived workload/query-log derivation + the extracted data or a documented access path |
| "Our operator lowers latency" | "Code will be released" | Runnable system/prototype with a build, a demo run, and the config |
| "We compare N systems" (E&A) | Numbers with no harness | The full comparison harness that regenerates every table |
| "On a 128-node cluster" | Nothing about environment | Hardware/cluster spec, engine build/commit, and how to size a smaller reproduction |

"Available on request" is treated as *not available*; convert every such line into a concrete
package or an explicit, justified exception (licensing, confidentiality).

## Provenance pinning (database-systems flavor)

```text
[Data]       pin dataset versions and sources; archive the derived workload/query-log, not just a
             description; document filtering and sampling
[System]     record the engine/prototype build or commit; ship a build recipe or container
[Environment] state hardware, memory, network, and node counts; note what a smaller reproduction changes
[Harness]    the measurement scripts that produce each table/figure, with fixed configuration
[Randomness] log seeds for any stochastic step; say what is and is not deterministic
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command (or container) regenerates each table/figure from a run or
  from logged results.
- **Scripted:** scripts exist but require documented manual steps, a specific cluster, or external
  data access.
- **Descriptive:** prose detailed enough that a competent reader could rebuild the pipeline.

For EDBT, aim turnkey for anything a reviewer might re-run quickly (a demo run on a small workload, a
plot from logged results); large-cluster or licensed-data experiments may stay scripted with the
environment and access clearly documented. Stating the achieved level honestly beats promising
turnkey behavior that fails on a clean machine.

## Vignette: a distributed-operator study

Consider an operator evaluated on a cluster. Its reproducibility spine: a container or build recipe
for the engine plus the operator; the workload-derivation scripts with pinned dataset versions; the
measurement harness that runs the operator and the tuned baseline across node counts; the logged raw
results; and the analysis notebooks that turn them into the paper's tables — plus one honest sentence
about the parts (the full 128-node run, a licensed dataset) that a reader reproduces at reduced scale
and why.

## Consistency and camera-ready pass

- Before submission: every reported number traces to the artifact; the availability statement
  matches reality; if the cycle is double-blind, the artifact carries no identity strings.
- Before camera-ready: deposit the package in a **DOI-issuing archive** (Zenodo, figshare, Software
  Heritage) with an OSI-approved license, replace any anonymized links with the permanent ones, and
  make the statement consistent with the open-access OpenProceedings record
  (`edbt-artifact-evaluation`, `edbt-camera-ready`).

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Availability] concrete / vague / missing
[Provenance gaps] <dataset versions / engine build / environment / seeds>
[Reproducibility level] turnkey / scripted / descriptive, stated honestly
[Paper fixes] <must appear in the PDF>
[Artifact fixes] <additions before upload>
```

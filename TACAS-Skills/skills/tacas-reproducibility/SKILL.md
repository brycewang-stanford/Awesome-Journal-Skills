---
name: tacas-reproducibility
description: Use when strengthening TACAS (ETAPS) reproducibility, covering the clean evaluation-VM packaging that the artifact process assumes, pinned dependencies and offline execution, a claim-to-script mapping so every benchmark number regenerates, honest degrees of reproducibility, consistency between the paper and the artifact, and the category difference between a mandatory tool-paper artifact and a voluntary research-paper artifact.
---

# TACAS Reproducibility

Use this before submission (for tool papers, before the mandatory artifact deadline) and again
before camera-ready. At TACAS reproducibility is not a courtesy: for a **regular tool** or
**tool-demonstration** paper the artifact is **mandatory and feeds acceptance**, and for a research
or case-study paper a voluntary artifact earns the title-page badges. The goal is that an ETAPS
evaluator, on a **clean virtual machine**, can rebuild your evidence and reach your numbers.

## Design for the clean ETAPS VM

The artifact process assumes a provided VM image with bounded evaluator time. Package accordingly:

```text
[Self-contained]  ship a VM-ready package: a Dockerfile or a pinned environment (lockfile), with
                  the tool prebuilt; not "apt-get install 30 things and hope"
[Offline]         no network access at run time; vendor every dependency, benchmark, and model
[Bounded]         a short smoke run that finishes in minutes, plus a documented full run with its
                  expected (possibly long) runtime
[Deterministic]   fix seeds and tool options; state what is and is not deterministic
[Documented]      a README that orients an evaluator in one screen: what it is, how to run the
                  smoke test, how to reproduce each claim, expected outputs and runtimes
```

## Claim-to-script mapping (the heart of a TACAS artifact)

- Map each reported table, figure, and headline number to a **script** and its **expected output**.
- Provide a top-level `reproduce/` (or equivalent) that regenerates results from **logged data**,
  and a separate path that re-runs the tool from scratch for those who have the time budget.
- State the machine you produced the numbers on; evaluators on different hardware should still see
  the same *verdicts* and the same *relative* comparison even if wall-clock differs.

## Claim-to-evidence audit

| Claim in the paper | Weak artifact answer | TACAS-ready answer |
|---|---|---|
| "Solves N benchmarks" | "Benchmarks available on request" | The exact task set vendored + a script printing solved/unsolved |
| "Faster than <baseline>" | Only your tool shipped | Both tools (or the baseline's install) with the equal-budget harness |
| "Sound / sound up to k" | Verdicts unchecked | A validation script (witness checking / cross-tool agreement) |
| "The counterexample is real" | Prose only | A replayable witness the evaluator can validate |

"Available on request" and "works on our cluster" are treated as **not reproducible** at TACAS;
convert every such line into a concrete, VM-runnable script.

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command regenerates each table/figure from logged data on the VM.
- **Scripted:** scripts exist but need documented manual steps or a large external benchmark
  download.
- **Descriptive:** prose detailed enough that a competent reader could rebuild the pipeline.

For a **tool paper**, aim turnkey for the smoke run and the headline comparison — that is what the
AEC checks against the **Functional** (and ideally **Reusable**) badge. Large full-benchmark runs
may stay scripted with the time budget documented. Stating the achieved level honestly beats
promising turnkey behaviour that fails on the clean VM.

## Category difference

- **Regular tool / tool-demonstration:** the artifact is **mandatory**, submitted right after the
  paper, evaluated with the PC — plan it as a co-equal deliverable, not a follow-up.
- **Regular research / case-study:** the artifact is **voluntary and post-acceptance**; if you want
  the badges, prepare it after notification, but the paper must already be self-contained on the
  evidence side.

## Consistency and camera-ready pass

- Before submission (or the artifact deadline): every scored number traces to a VM-runnable script;
  the paper and artifact agree; for a **research** paper the artifact is anonymized (no owner
  strings, cluster paths, lab names, identity-revealing repo URLs).
- Before camera-ready: swap any anonymized/placeholder location for a permanent, DOI-issuing archive
  (Zenodo/figshare/Software Heritage) and align with the badges you earned (`tacas-artifact-evaluation`).

## Output format

```text
[Claim inventory] <claim -> script -> expected output>
[Clean-VM readiness] runs offline on a fresh VM? smoke test in minutes? yes/no
[Reproducibility level] turnkey / scripted / descriptive, stated honestly
[Soundness/validation] <witness or cross-tool check present? yes/no>
[Category obligation] mandatory (tool/tool-demo) / voluntary (research/case-study)
[Fixes before upload] <ordered list>
```

---
name: fse-reproducibility
description: Use when strengthening ESEC/FSE reproducibility and open-science evidence, covering the Data Availability statement, anonymized-but-runnable artifacts, provenance pinning for mining and LLM studies, claim-to-evidence mapping, honest degrees of reproducibility, and consistency between what the paper says and what the artifact contains.
---

# FSE Reproducibility

Use this before submission and again before camera-ready. FSE's open-science posture makes
reproducibility a scored dimension, not a courtesy: the double-anonymous review already expects an
inspectable artifact, and the PACMSE camera-ready expects a permanent one. The goal is that a
competent reader could rebuild your evidence and reach your conclusions.

## Evidence map

- Map each research-question answer, technique claim, and reported number to a **verifiable
  location** — a paper section, a table generated from logged data, or a script in the artifact.
- For techniques, give enough of the algorithm, parameters, and environment that a reader could
  re-implement or re-run it.
- For empirical studies, report subjects and their selection, data collection, preprocessing,
  metrics, statistics, and the analysis scripts.
- Keep the **Data Availability statement** truthful and specific: what is shared, where it will
  live after acceptance, and — if something cannot be shared — exactly why.
- Keep the paper and the artifact **consistent**: a number in the PDF that no script in the
  artifact produces is the contradiction reviewers read as carelessness.

## Data Availability statement audit

| Claim in the paper | Weak availability answer | FSE-ready answer |
|---|---|---|
| "We study N projects" | "Dataset available on request" | Anonymized archive of the exact project list + extraction scripts |
| "Our tool detects X" | "Code will be released" | Anonymized, runnable tool with a README and a small demo input |
| "We interviewed P developers" | Nothing (privacy cited vaguely) | Anonymized codebook, protocol, and aggregate data; stated ethics limits |
| "The model produced Y" | Live API described | Cached prompts and raw responses, model IDs and dates |

"Available on request" is treated as *not available* at FSE; convert every such line into a
concrete, anonymized artifact or an explicit, justified exception.

## Provenance pinning

```text
[Mining]   pin repository SHAs; record corpus extraction date; archive the extracted dataset,
           not just the query; document fork/duplicate/bot handling
[LLM]      record exact model identifiers + access dates; cache raw inputs and outputs; report
           sampling settings; prefer post-training-cutoff subjects to bound contamination
[Compute]  state hardware, runtime, and number of runs so a reader can size a reproduction
[Randomness] log seeds for any stochastic step; say what is and is not deterministic
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command regenerates each table/figure from logged data.
- **Scripted:** scripts exist but require documented manual steps or external data access.
- **Descriptive:** prose detailed enough that a competent reader could rebuild the pipeline.

For FSE, aim turnkey for anything a reviewer might rerun quickly (a detection script on sample
inputs, a plot from logged results); large mined corpora or industrial data may stay scripted with
access clearly documented. Stating the achieved level honestly beats promising turnkey behavior
that fails on a clean machine.

## Vignette: a mixed-methods study

Consider a study combining mined pull-request data with a developer survey. Its reproducibility
spine: the mining scripts with pinned SHAs and extraction date; the anonymized extracted dataset;
the survey instrument and anonymized responses; the qualitative codebook with inter-rater
agreement; and the analysis notebooks that turn all of it into the paper's tables — plus one honest
sentence about the parts (raw identities, private repositories) that cannot be shared and why.

## Consistency and camera-ready pass

- Before submission: every scored number traces to the artifact; the Data Availability statement
  matches reality; the artifact is anonymized (no owner strings, cluster paths, or lab names).
- Before camera-ready: swap anonymized links for permanent, DOI-issuing archives, and align the
  statement with the ACM artifact badges you are pursuing (`fse-artifact-evaluation`).

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Data Availability] concrete / vague / missing
[Provenance gaps] <mining SHAs / LLM caching / seeds / compute>
[Reproducibility level] turnkey / scripted / descriptive, stated honestly
[Paper fixes] <must appear in the PDF>
[Artifact fixes] <additions before upload>
```

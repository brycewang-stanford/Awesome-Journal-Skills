---
name: icsme-reproducibility
description: Use when strengthening IEEE ICSME reproducibility and open-science evidence, covering the data-availability statement, anonymized-but-runnable artifacts, mining and LLM provenance pinning, claim-to-evidence mapping, honest degrees of reproducibility, and consistency between the paper and the artifact ahead of the ROSE-Festival IEEE badges.
---

# ICSME Reproducibility

Use this before submission and again before camera-ready. ICSME's ROSE-Festival culture makes
reproducibility a valued, sometimes scored dimension rather than a courtesy: double-anonymous
review already expects an inspectable artifact, and the **Joint Artifact Evaluation Track and ROSE
Festival** rewards a permanent, open one with IEEE badges. The goal is that a competent maintainer
could rebuild your evidence — re-mine the corpus, re-run the technique — and reach your conclusions.

## Evidence map

- Map each research-question answer, technique claim, and reported number to a **verifiable
  location** — a paper section, a table generated from logged data, or a script in the artifact.
- For techniques, give enough of the algorithm, parameters, and environment that a reader could
  re-implement or re-run it on their own systems.
- For mining/evolution studies, report subject systems and their selection, the extraction pipeline,
  preprocessing, metrics, statistics, and the analysis scripts.
- Keep the **data-availability statement** truthful and specific: what is shared (corpus, scripts,
  subject list), where it will live after acceptance, and — if something cannot be shared
  (proprietary legacy code, private history) — exactly why.
- Keep the paper and the artifact **consistent**: a number in the PDF that no script in the artifact
  produces is the contradiction reviewers read as carelessness.

## Data-availability statement audit

| Claim in the paper | Weak availability answer | ICSME-ready answer |
|---|---|---|
| "We mine N evolving projects" | "Dataset available on request" | Anonymized archive of the exact project list, SHAs, and extraction scripts |
| "Our tool detects debt hotspots" | "Code will be released" | Anonymized, runnable tool with a README and a small demo on a bundled repo |
| "We surveyed/interviewed P maintainers" | Nothing (privacy cited vaguely) | Anonymized codebook, protocol, and aggregate data; stated ethics limits |
| "The model summarized the change" | Live API described | Cached prompts and raw responses, model IDs and access dates |

"Available on request" is treated as *not available* under ROSE norms; convert every such line into
a concrete, anonymized artifact or an explicit, justified exception.

## Provenance pinning

```text
[Mining]   pin repository SHAs; record extraction date and the studied time window; archive the
           extracted corpus, not just the query; document fork/duplicate/bot handling
[LLM]      record exact model identifiers + access dates; cache raw inputs and outputs; report
           sampling settings; prefer post-cutoff subjects to bound contamination
[Compute]  state hardware, mining/runtime cost, and number of runs so a reader can size a reproduction
[Randomness] log seeds for any stochastic step; say what is and is not deterministic
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command regenerates each table/figure from logged data.
- **Scripted:** scripts exist but require documented manual steps or access to a large mined corpus.
- **Descriptive:** prose detailed enough that a competent reader could rebuild the pipeline.

For ICSME, aim turnkey for anything a reviewer might rerun quickly (a detection script on a sample
repo, a plot from logged results); a large mined corpus or proprietary history may stay scripted
with access clearly documented. Stating the achieved level honestly beats promising turnkey
behaviour that fails on a clean machine — especially with no revision round to fix it in.

## Vignette: a mixed-methods evolution study

Consider a study combining mined release history with a maintainer survey. Its reproducibility
spine: the mining scripts with pinned SHAs and extraction dates; the anonymized extracted dataset
with the exact subject-system list; the survey instrument and anonymized responses; the qualitative
codebook with inter-rater agreement; and the analysis notebooks that turn all of it into the
paper's tables — plus one honest sentence about the parts (identities, private forks) that cannot be
shared and why.

## Consistency and camera-ready / ROSE pass

- Before submission: every scored number traces to the artifact; the data-availability statement
  matches reality; the artifact is anonymized (no owner strings, cluster paths, lab names, or your
  own org's repos).
- Before camera-ready: swap anonymized links for a permanent, DOI-issuing archive, and align the
  statement with the IEEE badges you pursue in the ROSE Festival (`icsme-artifact-evaluation`).

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Data availability] concrete / vague / missing
[Provenance gaps] <mining SHAs / LLM caching / seeds / compute>
[Reproducibility level] turnkey / scripted / descriptive, stated honestly
[Paper fixes] <must appear in the PDF, since there is no revision round>
[Artifact fixes] <additions before upload>
```

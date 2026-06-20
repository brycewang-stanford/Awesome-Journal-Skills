---
name: gcb-reporting-and-data-policy
description: Use when preparing the data availability statement and the data/code archive for a Global Change Biology (GCB) manuscript. GCB requires data and code to be archived in a public repository with a persistent DOI as a condition of publication, and "available on request" is not accepted. Prepares the deposit; it does not waive requirements.
---

# Reporting & Data Policy (gcb-reporting-and-data-policy)

GCB treats open data and code as a **condition of publication**, not a courtesy. Primary and secondary
data supporting the results must be **archived in a publicly accessible repository with a persistent
identifier (DOI)**, code/software likewise (e.g., Zenodo), and the manuscript must carry a **data
availability statement**. Crucially, **"available on request" is not accepted**. Build the deposit as
you go. Confirm current wording on the policy page before submission.

## When to trigger

- Writing the **data availability statement**
- Choosing repositories and minting DOIs for data and code
- Handling data that cannot be fully shared (sensitive species locations, third-party/licensed data)
- Final reporting checks before submission

## What GCB requires (verify current wording)

1. **Archive data with a DOI.** Deposit primary and secondary data in a public, DOI-minting repository
   (e.g., **Dryad**, **Zenodo**, **PANGAEA**) with metadata sufficient for a third party to interpret
   the data correctly — before acceptance/publication.
2. **Archive code with a DOI.** Code, software, and documentation supporting the results go to an
   appropriate public repository (e.g., **Zenodo** via a GitHub release) with a persistent identifier.
3. **Data availability statement.** State exactly where the data and code live and how to access them;
   **"available on request" is not sufficient**.
4. **Reviewer access.** Make data accessible to peer reviewers on request during evaluation.
5. **Reporting completeness.** Report sample sizes, replication, units, methods, and software versions
   well enough to reproduce every result.

## When data cannot be fully shared

- **Sensitive data** (e.g., precise locations of threatened species, human-subjects or provider-licensed
  data): explain the restriction, give a **clear access pathway** (provider, application process), and
  share what can be shared (de-sensitized/aggregated layers) plus full code.
- Document why the restriction applies; do not use sensitivity as a blanket reason to skip deposit.

## Build-as-you-go checklist

- [ ] Data archived in a DOI-minting public repository with interpretable metadata
- [ ] Code/software archived (Zenodo/GitHub release) with a DOI
- [ ] Data availability statement names repository + access (not "on request")
- [ ] Sample sizes, replication, units, software versions reported
- [ ] Sensitive data: restriction explained + access pathway + shareable subset
- [ ] Manuscript exhibit numbers match the archived outputs

## Repository fit by data type

Different global-change data types land best in different DOI-minting archives. Treat this as a routing
guide, then confirm the current accepted list against the journal's author guidelines.

| Data type | Typical archive | Note |
|-----------|-----------------|------|
| Ecological tabular / experimental | Dryad | Curated, ecology-oriented |
| Code + figure pipeline | Zenodo via a GitHub release | Versioned, DOI per release |
| Oceanographic / Earth-system | PANGAEA | Geo/environmental specialist |
| Sequences | INSDC (GenBank/ENA) | Domain-mandated, then cite accession |
| Sensitive species locations | Restricted deposit + access pathway | Share de-sensitized layer + full code |

## Worked micro-example (illustrative)

A remote-sensing carbon-flux paper archives three things, not one: the gap-filled flux table to a
DOI-minting repository; the processing and modelling code to Zenodo via a tagged GitHub release; and the
raw tower coordinates with a stated restriction because one site is on a protected reserve. The data
availability statement names each DOI and the access route for the restricted coordinates. A weak version
deposits only the figures' CSV and writes "code available on request" — which GCB does not accept. The
DOIs here are illustrative placeholders; mint real ones before submission.

## Compliance pushback patterns and the fix

- "Statement says available on request" → replace with named repository, DOI, and access route; GCB does
  not accept request-only.
- "Code not archived, only data" → deposit the analysis/modelling code so every figure reproduces.
- "Metadata insufficient" → add units, sampling design, and variable definitions a third party can read.
- "Sensitive locations withheld with no pathway" → explain the restriction, give the application route,
  and share an aggregated layer plus full code.

## Anti-patterns

- "Data available on request" (explicitly rejected by GCB)
- A personal website or transient cloud link instead of a DOI-minting repository
- Archiving data but not the code that produced the figures
- Metadata too thin for a third party to interpret the data
- Treating deposit as a post-acceptance afterthought

## Output format

```
【Data archived】DOI-minting repo + metadata? [Y/N]
【Code archived】Zenodo/release with DOI? [Y/N]
【Availability statement】names repo + access (not "on request")? [Y/N]
【Sensitive data】restriction explained + access path + shareable subset?
【Reproducible reporting】n, units, versions complete? [Y/N]
【Next】gcb-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories (Dryad/Zenodo/PANGAEA) and reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — GCB data- and code-archiving policy

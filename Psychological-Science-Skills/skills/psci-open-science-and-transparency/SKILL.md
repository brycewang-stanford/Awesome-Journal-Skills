---
name: psci-open-science-and-transparency
description: Use when meeting Psychological Science's open-science requirements. For submissions on or after 1 January 2024 the journal requires open data and materials (case-by-case exemptions), a Research Transparency Statement placed between the Introduction and Methods, persistent identifiers for shared content, and treats transparency limits and preregistration quality as factors in editorial decisions. Prepares compliance; it does not waive requirements.
---

# Open Science & Transparency (psci-open-science-and-transparency)

This is the skill that most distinguishes a Psychological Science submission. Since **1 January 2024**
the journal has **required** open data and materials and a graded **Research Transparency Statement** —
the badge era is over, and "**limits on transparency will be a factor in editorial decisions.**"
Prepare this early, not at acceptance.

## When to trigger

- Building the data/materials deposits and the Research Transparency Statement
- Deciding whether (and how) to claim an exemption from sharing
- Linking preregistration and reporting its status
- A reviewer or editor flagged transparency or reproducibility

## What is required (verify current wording on the official page)

1. **Open data and materials.** Make data, analysis scripts, and study materials openly available,
   with **case-by-case exemptions** that must be **justified** (e.g., legal, ethical, or
   confidentiality constraints). It is a requirement, not a bonus.
2. **Research Transparency Statement.** A **required separate section placed between the Introduction
   and the Methods** for empirical manuscripts. It reports the availability of data, analysis scripts,
   materials, and preregistrations, is shared with editors and reviewers, and is **evaluated** —
   constraints must be explained.
3. **Persistent identifiers (DOIs).** Provide DOIs for all shared data and materials (OSF, Dataverse,
   Zenodo, ICPSR, etc.) — not transient personal links.
4. **Preregistration.** Its presence and **quality are factored into editorial decisions**; report
   preregistration honestly and link it (anonymized for initial submission).

## Build-it-right checklist

- [ ] Data deposited with a **DOI**; a **data dictionary**/codebook included
- [ ] **Analysis scripts** deposited; results regenerate in a fresh session
- [ ] **Materials** (stimuli, instruments, instructions) deposited with a DOI
- [ ] **Preregistration** linked (anonymized for review); confirmatory vs. exploratory consistent with it
- [ ] **Research Transparency Statement** drafted and placed **between Intro and Methods**
- [ ] Any **exemption** clearly justified (what cannot be shared, why, and what *is* shared instead)
- [ ] Shared links **anonymized** for initial (masked) submission

## Exemptions (do them honestly)

- If data cannot be fully shared (sensitive populations, third-party/proprietary data, IRB limits),
  state exactly **what** is withheld, **why**, and **how** others can access or approximate it
  (application path, synthetic data, code release). Unjustified opacity counts against the paper.

## Anti-patterns

- Treating open data/materials as optional or "available on request"
- Omitting or burying the Research Transparency Statement
- Personal/transient links instead of DOIs
- Claiming an exemption without a justification
- Identifying author info in OSF/repository links during masked review

## Output format

```
【Open data】deposited + DOI + data dictionary? [Y/N]
【Open materials】deposited + DOI? [Y/N]
【Analysis scripts】deposited + fresh-session reproducible? [Y/N]
【Preregistration】linked (anonymized) + consistent with reporting? [Y/N/NA]
【Transparency Statement】drafted + placed between Intro and Methods? [Y/N]
【Exemptions】justified (what/why/alternative)? [Y/N/NA]
【Next】psci-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — OSF, Dataverse, Zenodo, preregistration templates, DOIs
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — post-2024 open-science requirements and the Transparency Statement

---
name: apsr-transparency-and-data-policy
description: Use when preparing the reproducibility / replication materials for an American Political Science Review (APSR) manuscript. APSR requires conditionally accepted authors to deposit a reproducibility package in the APSR Dataverse (Harvard Dataverse), which the editorial office verifies before publication. Covers quantitative and qualitative transparency and exemptions. Prepares the package; it does not waive requirements.
---

# Transparency & Data Policy (apsr-transparency-and-data-policy)

APSR does not just ask for data — it **verifies** that the deposited materials reproduce the
manuscript's tables and figures **before** publication. Build the package as you go so conditional
acceptance does not stall.

## When to trigger

- Building the reproducibility/replication package
- A manuscript reached **conditional acceptance** and the editorial office requested materials
- Data cannot be fully shared (privacy, ethics, legal/provider restrictions) and you need the
  exemption path
- A **Replications and Reappraisals** submission (materials expectations are central)

## What APSR requires (verify current wording on the policy page)

1. **Deposit to the APSR Dataverse.** Authors of **conditionally accepted** manuscripts submit a
   **reproducibility package** to the **APSR Dataverse on Harvard Dataverse** — the journal's
   dedicated repository with permanent identifiers and preservation. Not a personal website or generic
   cloud link.
2. **Editorial verification.** The office reviews the package to confirm it can **reproduce the
   manuscript's tables and figures** and that the research process is documented well enough. Treat
   this as a real check, not a formality.
3. **Quantitative materials.** Data, code, and documentation sufficient to regenerate every reported
   result. Master script + README + pinned versions + seeds.
4. **Qualitative materials.** Share the materials and data used, alongside literature citations, in a
   form that supports the claims (e.g., evidence tables, annotated sources), with access controls
   where needed (QDR is an option for controlled access).

## When data cannot be shared (exemption path)

- **Explain why** the relevant data are not available (ethical/privacy concerns or legal restrictions
  by the data provider).
- Provide **README instructions on exactly how others can obtain the data** (access process,
  application, provider contact).
- Where possible, **provide synthetic data** resembling the unavailable data so the code can be run.

## Build-as-you-go checklist

- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, construction steps, and how to reproduce each exhibit
- [ ] **Seeds** set and reported for every stochastic step
- [ ] Software/package **versions pinned** (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] Exhibit numbers in the manuscript **match** the package output exactly
- [ ] Restricted data: exemption note + access instructions + synthetic data where feasible
- [ ] Preregistration / pre-analysis plan linked (anonymized) where applicable

## Anti-patterns

- Treating the deposit as a post-publication afterthought (it gates publication)
- Depositing code that does not actually reproduce the printed tables/figures
- A personal URL instead of the APSR Dataverse
- Claiming data are restricted without giving an access path or synthetic substitute
- Undocumented, un-seeded, unpinned code that "works on my machine"

## Output format

```
【Repository】APSR Dataverse (Harvard) — package staged? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Restricted data?】exemption note + access path + synthetic data?
【Qualitative transparency】evidence/sources documented? [Y/N/NA]
【Next】apsr-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and qualitative-transparency options (QDR, ATI)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — APSR Research Transparency policy + APSR Dataverse

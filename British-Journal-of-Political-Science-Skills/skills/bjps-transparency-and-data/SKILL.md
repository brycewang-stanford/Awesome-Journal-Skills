---
name: bjps-transparency-and-data
description: Use when preparing the replication / transparency materials for a British Journal of Political Science (BJPS) manuscript. BJPS is a DA-RT signatory and requires authors to deposit replication data and code in the BJPolS Dataverse (Harvard Dataverse) at acceptance, with restricted-access exemptions. Covers quantitative and qualitative transparency. Prepares the package; it does not waive requirements.
---

# Transparency & Replication Data (bjps-transparency-and-data)

BJPS is a signatory of the **Data Access and Research Transparency (DA-RT)** statement: authors "are
not allowed to withhold information used to perform an analysis featured in a BJPolS piece." At
acceptance, replication data and code are deposited in the **BJPolS Dataverse on Harvard Dataverse**,
which issues a citable DOI for the data. Build the package as you go so acceptance does not stall.

## When to trigger

- Building the replication / transparency package
- A manuscript reached acceptance and you must deposit materials
- Data cannot be fully shared (privacy, ethics, legal/provider restrictions) and you need the
  restricted-access exemption path
- A **Comment** that re-analyzes a published result (materials expectations are central)

## What BJPS requires (verify current wording on the policy page)

1. **Deposit to the BJPolS Dataverse.** Replication data and code are uploaded to the **BJPolS
   Dataverse on Harvard Dataverse**, the journal's dedicated collection with permanent identifiers;
   you receive **citation information including a DOI** for the data. Not a personal website or generic
   cloud link.
2. **No withholding.** You may not withhold information used to produce an analysis in the paper.
   Treat the deposit as enabling independent replication, not as a formality.
3. **Quantitative materials.** Data, code, and documentation sufficient to regenerate every reported
   result. Master script + README + pinned versions + seeds.
4. **Qualitative materials.** Share the materials and evidence used to support the claims (e.g.,
   evidence tables, annotated sources, interview protocols), with access controls where needed (the
   Qualitative Data Repository, QDR, supports controlled access).

## When data cannot be shared (restricted-access exemption)

- **Explain why** the relevant data are not available — BJPS allows exemptions for **restricted-access
  source data** (ethical/privacy concerns or provider/legal restrictions).
- Provide **README instructions on exactly how others can obtain the data** (access process,
  application, provider contact).
- Where possible, **provide synthetic data** resembling the unavailable data so the code can be run.
- Questions about the replication policy can be directed to the BJPolS editorial staff (待核实 current
  contact on the live policy page).

## Build-as-you-go checklist

- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, construction steps, and how to reproduce each exhibit
- [ ] **Seeds** set and reported for every stochastic step
- [ ] Software/package **versions pinned** (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] Exhibit numbers in the manuscript **match** the package output exactly
- [ ] Restricted data: exemption note + access instructions + synthetic data where feasible
- [ ] Preregistration / pre-analysis plan linked (anonymized) where applicable

## Anti-patterns

- Treating the deposit as a post-acceptance afterthought
- Depositing code that does not actually reproduce the printed tables/figures
- A personal URL instead of the BJPolS Dataverse
- Claiming data are restricted without giving an access path or synthetic substitute
- Undocumented, un-seeded, unpinned code that "works on my machine"

## Output format

```
【Repository】BJPolS Dataverse (Harvard) — package staged? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Restricted data?】exemption note + access path + synthetic data?
【Qualitative transparency】evidence/sources documented? [Y/N/NA]
【Next】bjps-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and qualitative-transparency options (QDR, ATI)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — BJPS DA-RT / replication policy + BJPolS Dataverse

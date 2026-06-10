---
name: conbio-reporting-and-data-policy
description: Use when preparing the data-availability statement and the data/code archive for a Conservation Biology manuscript. The journal (Wiley/SCB) expects supporting data and code to be deposited in a public repository such as Dryad with a persistent identifier, and sensitive species data to be protected. Prepares the package; it does not waive requirements.
---

# Reporting & Data Policy (conbio-reporting-and-data-policy)

*Conservation Biology* expects a **data-availability statement** and, in keeping with Wiley/SCB policy,
deposit of the **data and code** supporting the results in an appropriate **public repository** (e.g.,
**Dryad**, Zenodo, Figshare, GenBank) with a **persistent identifier**. Build the package as you go so
acceptance does not stall. Confirm the current mandatory wording on the live policy page (待核实).

## When to trigger

- Writing the data-availability statement and assembling the archive
- A manuscript is heading toward acceptance and you need the deposit ready
- Data cannot be fully shared (sensitive species, privacy, legal/provider restrictions)
- A Review or synthesis where the screened-study dataset should be shared

## What to prepare (verify current wording on the policy page)

1. **Data-availability statement.** A short statement in the manuscript saying where the data and code
   are (repository + DOI/identifier), or why they cannot be shared and how to obtain them.
2. **Public-repository deposit.** Place data and code in a recognized archive with a **persistent
   identifier** and a guarantee of preservation — not a personal website or transient cloud link.
   Dryad is widely used for ecology/conservation; software-heavy work may also use Zenodo/GitHub-Zenodo.
3. **Quantitative materials.** Data, code, and documentation sufficient to regenerate every reported
   result: master script + README + pinned versions + seeds.
4. **Synthesis materials.** For Reviews/meta-analyses, share the screening decisions, included-study
   list, and extracted effect sizes.

## Sensitive-species & restricted data (a conservation-specific duty)

- **Protect at-risk taxa.** For threatened, exploited, or trafficked species, **mask or coarsen precise
  localities** (nests, dens, roosts, populations) so the archive cannot aid poaching or disturbance;
  state that you have done so.
- **Restricted data.** If data are restricted (Indigenous data sovereignty, provider agreements,
  privacy), **explain why**, give **instructions on how others can request access**, and provide
  **synthetic or aggregated data** where feasible so the code can be exercised.

## Build-as-you-go checklist

- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, construction steps, and how to reproduce each exhibit
- [ ] **Seeds** set and reported for every stochastic step
- [ ] Software/package **versions pinned** (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] **Data-availability statement** drafted with repository + identifier
- [ ] Sensitive localities **masked/coarsened**; masking noted
- [ ] Restricted data: reason + access instructions + synthetic/aggregated substitute

## Anti-patterns

- Treating the deposit as a post-publication afterthought
- A personal URL instead of a persistent-identifier repository
- Publishing precise locations of threatened or trafficked species
- Claiming data are restricted with no access path or synthetic substitute
- Undocumented, un-seeded, unpinned code that "works on my machine"


## Operating pass for Conservation Biology

Use this as a second-pass capability check. First lock the species/system threat, conservation decision, and uncertainty relevant to action; then test whether the manuscript addresses conservation-science reviewers who ask whether evidence changes biodiversity, management, or policy action.

- **Primary move:** Return a claim-evidence-risk ledger; every recommendation must point to a manuscript location or missing artifact.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Biological Conservation for applied conservation breadth, Global Change Biology for climate/ecosystem process, Ecology Letters for theory-forward ecology; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Repository】Dryad / Zenodo / other — package staged? [Y/N]
【Data-availability statement】drafted with DOI/identifier? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Sensitive data】localities masked / restricted-data access path? [Y/N/NA]
【Next】conbio-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories and reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Wiley/SCB data-sharing policy and Dryad

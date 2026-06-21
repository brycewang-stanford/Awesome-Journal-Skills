---
name: cps-transparency-and-data
description: Use when preparing the replication and transparency materials for a Comparative Political Studies (CPS) manuscript. Quantitative papers cannot be finally accepted until replication materials are deposited at the CPS Dataverse; a data availability statement is required. Prepares the package; it does not waive requirements.
---

# Transparency & Data (cps-transparency-and-data)

CPS enforces political-science replication norms. **Papers presenting quantitative analyses will not be
granted final acceptance until replication materials (data, code, log files, etc.) are deposited at the
CPS Dataverse on Harvard Dataverse**, and every paper needs a **data availability statement**. Build the
package as you go so final acceptance does not stall — and follow DA-RT-style transparency for
qualitative evidence too.

## When to trigger

- Building the replication/reproducibility package and the data availability statement
- A manuscript is near acceptance and the editorial office expects deposited materials
- Data cannot be fully shared (privacy, ethics, provider restrictions) and you need a path
- Preparing a (optional) anonymized pre-analysis plan as supplementary material

## What CPS requires (verify current wording — 检索于 2026-06；以官网为准)

1. **Deposit to the CPS Dataverse.** Quantitative papers deposit replication materials — **data, code,
   log files, and documentation** — at the **CPS Dataverse on Harvard Dataverse**
   (`dataverse.harvard.edu/dataverse/cps`). This gates **final acceptance**, not post-publication.
2. **Data availability statement.** Every paper includes a statement saying whether data are available,
   where, and — if available but not shared — **why not**.
3. **Reproducibility.** Materials must let an independent researcher regenerate the manuscript's tables
   and figures: master script + README + pinned versions + seeds.
4. **Restricted-data path.** If data cannot be shared and sharing is a publication requirement, **consult
   the journal editorial office**; explain the restriction and document how others can obtain the data.
5. **Preregistration (optional).** Authors *may* submit an **anonymized** pre-analysis plan as
   supplementary material; the journal provides it to reviewers on request. Mark registered vs.
   exploratory analyses.

## Qualitative / multi-method transparency (DA-RT spirit)

- Document sources, interviews, and fieldnotes so the evidentiary basis is auditable; use evidence
  tables or active citation. Where confidentiality requires it, use controlled access (e.g., QDR).
- State clearly which claims rest on which evidence; do not let "the cases show" stand unsupported.

## Sharing posture by evidence type

Choose the transparency route before drafting the data availability statement:

| Evidence type | Default posture | Documentation to include |
|---------------|-----------------|--------------------------|
| Cross-national public datasets | Share constructed data and code; cite original sources | Source versions, merge keys, transformations, and exact download dates |
| Proprietary/admin data | Share code, synthetic or redacted extracts where allowed, and access instructions | License limits, access route, variable construction, and verification path |
| Interviews/fieldnotes | Protect identities; share protocols, coding scheme, and evidence table when ethical | Consent limits, anonymization method, and claim-to-evidence map |
| Text corpus/web data | Share corpus identifiers or permissible text, plus scraping/cleaning code | Collection date, inclusion rules, deduplication, language processing decisions |
| Pre-analysis plan | Submit anonymized plan as supplement when used | Registered vs. exploratory analyses marked in manuscript and code |

The data availability statement should mirror the table: what is shared, where, what is restricted, and
how a qualified reader can audit the claim without violating law, ethics, or provider terms.

## Build-as-you-go checklist

- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, construction, and how to reproduce each exhibit
- [ ] **Seeds** set and reported for every stochastic step
- [ ] Software/package **versions pinned** (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] Exhibit numbers in the manuscript **match** the package output exactly
- [ ] **Data availability statement** drafted (available where / why not shared)
- [ ] Restricted data: explanation + access instructions + editorial-office consultation noted
- [ ] Anonymized pre-analysis plan attached where applicable; registered vs. exploratory marked

## Anti-patterns

- Treating the deposit as a post-publication afterthought (it gates final acceptance for quant papers)
- Depositing code that does not actually reproduce the printed tables/figures
- A personal URL or generic cloud link instead of the CPS Dataverse
- Omitting the data availability statement, or claiming "available on request" with no plan
- Undocumented, un-seeded, unpinned code that "works on my machine"
- Qualitative claims with no documented evidentiary basis

## Output format

```
【Repository】CPS Dataverse (Harvard) — package staged? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Data availability statement】drafted? available where / why not?
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Sharing posture】public / proprietary-admin / interview-fieldnote / text-corpus / PAP route chosen
【Restricted data?】explanation + access path + editorial-office note?
【Qualitative transparency】sources/evidence documented? [Y/N/NA]
【Pre-analysis plan】anonymized + registered/exploratory marked? [Y/N/NA]
【Next】cps-review-process
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — CPS data policy + CPS Dataverse URL
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and qualitative-transparency options (QDR)

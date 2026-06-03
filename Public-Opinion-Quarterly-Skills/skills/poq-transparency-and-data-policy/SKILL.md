---
name: poq-transparency-and-data-policy
description: Use when preparing the transparency materials for a Public Opinion Quarterly (POQ) manuscript — the AAPOR-standard "Appendix A: Disclosure Elements", the replication package deposited to POQ's Harvard Dataverse, and the Data Availability Statement. POQ requires materials that reproduce exactly all published tables and figures, archived before typesetting. Prepares the materials; it does not waive requirements.
---

# Transparency & Data Policy (poq-transparency-and-data-policy)

POQ has two transparency demands that distinguish it from generic social-science venues: **AAPOR-standard
methodological disclosure** of every survey, and a **replication package** that reproduces exactly all
published tables and figures, archived in **POQ's Dataverse before the paper advances to typesetting**.
Build both as you go so acceptance does not stall.

## When to trigger

- Assembling **Appendix A: Disclosure Elements** for every dataset reported
- Building the replication/reproduction package for POQ's Dataverse
- A manuscript was accepted and the office requested materials before typesetting
- Data cannot be fully shared (privacy, ethics, provider restrictions) and you need the exemption path

## AAPOR disclosure — Appendix A: Disclosure Elements

POQ requires manuscripts to **disclose these elements for all data reported (if applicable) or link to
publicly available / published documentation**, gathered in an **"Appendix A: Disclosure Elements"**:

1. **Funding** — who sponsored the data collection.
2. **Exact question wording** of all survey questions used.
3. **Population under study** — a clear description.
4. **Sample design** — frame, selection, stratification, clustering.
5. **Method and dates of data collection** — mode(s) and field period.
6. **Response rate and how it was calculated** — per **AAPOR Standard Definitions** (state RR1–RR6 and
   show the disposition-code computation).
7. **Sample sizes and a discussion of the precision** of the findings.
8. **Design effect due to clustering and weighting** — discuss the adjustment.

For secondary data, **link to the public documentation** rather than reproducing it.

## Replication package — POQ Dataverse (Harvard)

1. **Deposit to POQ's Dataverse** on Harvard Dataverse (the journal's permanent archive with
   persistent identifiers) — not a personal website or generic cloud link.
2. **Reproduce exactly** all published tables and figures: data + code + documentation sufficient to
   regenerate every reported result. Master script + README + pinned versions + seeds.
3. **Archived before typesetting** — accepted manuscripts do not advance until materials are in place.
4. **Data Availability Statement (DAS)** in the article's endmatter describing where/how to access the
   data.

## When data cannot be shared (exemption path)

- **Explain why** the data are restricted (privacy, ethics, provider/legal limits).
- Provide **README instructions on exactly how others can obtain the data** (access process, contact).
- Where possible, provide **synthetic data** so the code can be run.
- A **twelve-month embargo** from the article's appearance may be requested (confirm current terms — 待核实).

## Build-as-you-go checklist

- [ ] **Appendix A** drafted with all eight disclosure elements (or links) for every dataset
- [ ] Response rate stated **with AAPOR definition + calculation**
- [ ] One **master script** regenerates **every** table and figure
- [ ] **README** + provenance + **seeds** + **pinned versions**
- [ ] Exhibit numbers in the manuscript **match** package output exactly
- [ ] **Data Availability Statement** drafted for the endmatter
- [ ] Restricted data: exemption note + access path + synthetic data + embargo request if needed

## Anti-patterns

- A response rate with no AAPOR definition or calculation (an Appendix A failure)
- Treating the deposit as a post-publication afterthought (it gates typesetting)
- Code that does not actually reproduce the printed tables/figures
- A personal URL instead of POQ's Dataverse
- Claiming data are restricted without an access path or synthetic substitute

## Output format

```
【Appendix A】all 8 disclosure elements present (or linked)? [Y/N]
【Response rate】AAPOR definition + calculation shown? [Y/N]
【Repository】POQ Dataverse (Harvard) — package staged? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【DAS】drafted for endmatter? [Y/N]
【Restricted data?】exemption + access path + synthetic + embargo?
【Next】poq-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and the AAPOR disclosure checklist
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AAPOR disclosure elements, POQ Dataverse, DAS, embargo

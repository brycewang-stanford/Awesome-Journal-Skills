---
name: io-transparency-and-data-policy
description: Use when preparing the replication/transparency materials for an International Organization (IO) manuscript. IO's signature requirement is verification BEFORE final acceptance — the editorial staff request data and code at conditional acceptance, IO staff re-run quantitative results and check proofs of formal models, and editors withhold final acceptance until all reported results are confirmed; materials then deposit to the IO Dataverse with a DOI and a Data Availability Statement. Prepares the package; it does not waive requirements.
---

# Transparency & Data Policy (io-transparency-and-data-policy)

IO does not just ask for data — its **editorial staff re-run your quantitative results and verify the
proofs of your formal models, and editors will not issue final acceptance until all reported analyses
are confirmed.** This pre-publication verification is IO's signature. Build the package as you analyze
so conditional acceptance does not stall.

## When to trigger

- Building the reproducibility/replication package (start during analysis, not at acceptance)
- A manuscript reached **conditional acceptance** and the editorial staff requested data and code
- You have a **formal model** whose proofs IO staff will verify
- Data cannot be fully shared (privacy, ethics, legal/provider restrictions) and you need the path
- Writing the **Data Availability Statement**

## What IO requires (verify current wording on the policy page — 待核实 on verbatim text)

1. **No data at initial submission.** Authors **do not** provide data or command files when first
   submitting (consistent with double-blind review).
2. **Data requested at conditional acceptance.** The editorial staff **request the data and command
   files at the time of conditional acceptance.**
3. **Verification before final acceptance.** For papers using quantitative data, **IO staff re-run the
   code to confirm the reported results**; for formal papers, **IO staff verify the proofs**. Editors
   **do not issue final acceptance until all results of all reported analyses are confirmed.** Treat this
   as a real check, not a formality.
4. **Deposit to the IO Dataverse.** On final acceptance, upload quantitative datasets and supporting
   files to the **IO Dataverse on Harvard Dataverse**; the entry mints a **DOI** to be cited in the
   published article. Not a personal website or generic cloud link.
5. **Data Availability Statement.** A DAS is **required for quantitative articles** (encouraged for
   qualitative), appearing **before the reference list**.
6. **Qualitative materials.** Authors are **strongly encouraged** to deposit qualitative data at the
   **Qualitative Data Repository (QDR)** at Syracuse, with access controls where needed.

## When data cannot be shared (exemption path)

- **Explain why** the relevant data are not available (ethical/privacy concerns or legal restrictions by
  the provider).
- Provide **README instructions on exactly how others can obtain the data** (access process,
  application, provider contact).
- Where possible, **provide synthetic or simulated data** so the code runs end-to-end. (Confirm the
  current exemption procedure on the live policy page — 待核实.)

## Build-as-you-go checklist

- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, construction steps, software, and how to reproduce each exhibit
- [ ] **Seeds** set and reported for every stochastic step
- [ ] Software/package **versions pinned** (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] Exhibit numbers in the manuscript **match** the package output exactly (IO staff re-run them)
- [ ] **Formal models**: a complete, checkable **proof appendix** for IO staff to verify
- [ ] **Data Availability Statement** drafted (before the reference list)
- [ ] Restricted data: exemption note + access instructions + synthetic data where feasible
- [ ] Qualitative data: QDR deposit considered; sources documented for the claims

## Anti-patterns

- Treating the deposit as a post-publication afterthought (it gates **final** acceptance)
- Depositing code that does not actually reproduce the printed tables/figures (IO re-runs it)
- A formal model with hand-waved or incomplete proofs (IO verifies proofs)
- A personal URL instead of the IO Dataverse; no DOI cited in the article
- Claiming data are restricted without giving an access path or synthetic substitute
- Forgetting the Data Availability Statement

## Output format

```
【Stage】initial (no data) / conditional acceptance (data requested) / pre-final (verification)
【Quantitative reproduces?】master script re-runs all tables/figures locally? [Y/N]
【Formal proofs】complete, checkable proof appendix? [Y/N/NA]
【Repository】IO Dataverse (Harvard) staged + DOI plan? [Y/N]
【Data Availability Statement】drafted before references? [Y/N]
【Restricted data?】exemption note + access path + synthetic data?
【Qualitative】QDR deposit + sources documented? [Y/N/NA]
【Next】io-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling, formal-proof workflow, and QDR for qualitative IR
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — IO Research Transparency policy + IO Dataverse

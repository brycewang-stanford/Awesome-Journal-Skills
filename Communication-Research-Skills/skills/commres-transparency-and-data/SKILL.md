---
name: commres-transparency-and-data
description: Use when preparing the transparency, open-science, and reproducibility materials for a Communication Research (CR) manuscript — data-availability statement, deposited data/code/materials, preregistration, and the restricted-data path. Prepares the materials; it does not waive requirements.
---

# Transparency & Data (commres-transparency-and-data)

CR is a quantitative, social-scientific journal, and its reviewers increasingly expect the materials
that let others scrutinize how the numbers were produced. SAGE supports a **data-availability
statement** and open-practices options; build the statement and supporting materials **as you write**
so submission and any open-practice claim go smoothly. Confirm the journal's current wording on the
SAGE author page (待核实 on exact policy).

## When to trigger

- Drafting the **data-availability statement**
- Deciding whether to share data, code, and materials, or to preregister
- Preparing a **preregistration** / pre-analysis plan for a prospective design (note it in the cover letter)
- Data cannot be fully shared (privacy, ethics, platform/legal restrictions) and you need the path forward

## What CR / SAGE expects (verify current wording on the policy page)

1. **Data-availability statement.** State where the data are (repository + identifier), under what
   conditions they can be accessed, and — if they cannot be shared — **why**, with instructions for how
   others might obtain them.
2. **Open practices (where pursued).**
   - **Open data** — data and a codebook deposited in a trusted repository with a persistent identifier.
   - **Open materials** — stimuli, instruments, scales, and code deposited so the study can be reproduced.
   - **Preregistration** — a time-stamped, registered design/analysis plan; note it in the cover letter.
3. **Quantitative materials.** Data, code, codebook, scale items, and documentation sufficient to
   regenerate every reported result; master script + README + pinned versions + seeds.
4. **ORCID and ethics.** Provide ORCID where requested; state IRB/ethics approval and informed consent;
   for content analysis, deposit the codebook and intercoder-reliability report.

## When data cannot be shared (restricted-data path)

- **Explain why** in the data-availability statement (ethical/privacy concerns, platform terms of
  service, or legal restrictions by the provider).
- Provide **instructions on how others can obtain the data** (access process, application, provider contact).
- Where possible, provide **synthetic or de-identified data** so the code can be run.

## Build-as-you-go checklist

- [ ] **Data-availability statement** drafted (repository, identifier, access conditions, or exemption)
- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, construction, and how to reproduce each exhibit
- [ ] **Seeds** set and reported for every stochastic step; software/package **versions pinned**
- [ ] Scales/stimuli/codebook deposited (open materials) where claimed
- [ ] Content analysis: codebook + intercoder-reliability report included
- [ ] Materials **anonymized** (no author-identifying paths/links) for double-anonymized review

## Transparency expectations by study type (decision table)

Match the deposit to the design rather than forcing one template:

| Study type | What a CR referee wants deposited | Open practice most relevant |
|------------|-----------------------------------|-----------------------------|
| Experiment | data + codebook + stimuli + analysis script | open data + materials + preregistration |
| Survey / panel | data + scale items + analysis script + measurement model | open data + materials |
| Content analysis | codebook + coder instructions + reliability subsample + texts | open materials (+ open data) |
| Computational / text-as-data | corpus or query, model/version, seeds, **human-validation set** | open materials + open data |

For computational measures, the **human-validation set is itself the evidence** that the automated
label means what the paper claims — depositing the classifier without it leaves the construct unverified.

## Worked micro-example: a DAS for a copyrighted-news corpus (illustrative)

A computational content analysis of **40,000 news articles** (illustrative) hits a familiar wall: the
texts are copyrighted and the feed bars redistribution. The path: (1) deposit the **codebook, article
IDs/URLs, query parameters, and analysis code** so a same-license reader reproduces the pipeline; (2)
deposit the **human-validation sample** and shareable derived data; (3) write a data-availability
statement naming the restriction, provider, and access route, and offering **de-identified derived
features** (frame proportions per article) so modeling re-runs without raw text.

## Anti-patterns

- Treating the data-availability statement as an afterthought rather than a submission element
- Claiming an open-practice credit whose materials are not actually deposited or do not reproduce results
- A personal URL instead of a trusted repository with a persistent identifier
- Claiming data are restricted without giving an access path or synthetic substitute
- De-anonymizing the manuscript via an open-materials link during review

## Output format

```
【Data-availability statement】drafted? repository + identifier or exemption? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Open practices sought】open data / open materials / preregistration (materials staged?)
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Restricted data?】exemption note + access path + synthetic data?
【Ethics/ORCID】IRB + consent stated; ORCID provided? [Y/N]
【Next】commres-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and repositories (OSF, Dataverse, QDR)
- [`../../resources/code/`](../../resources/code/) — master-script + seed-discipline skeleton
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data-availability and open-practices policy

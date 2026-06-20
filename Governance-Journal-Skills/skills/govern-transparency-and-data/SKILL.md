---
name: govern-transparency-and-data
description: Use when preparing the Data Availability Statement and replication materials for a Governance: An International Journal of Policy, Administration, and Institutions manuscript. Governance requires the statement (mandatory) and encourages sharing data/code in a DOI-citable repository, but does not run a verified pre-publication reproduction check like APSR. Builds the statement and materials; it does not waive requirements.
---

# Transparency & Data (govern-transparency-and-data)

*Governance* requires a **Data Availability Statement** with the manuscript — a statement of whether
replication materials (data, code) exist and how a reader can access them. Be clear-eyed about the bar:
the **statement is mandatory**, and sharing in a DOI-citable repository is recommended and increasingly
expected, but *Governance* does **not** run a verified, editor-checked pre-publication reproduction gate
the way APSR's Dataverse workflow does. That makes the statement an honesty-and-access commitment, not a
reproduction certificate — so write it precisely and build the materials as you go.

## When to trigger

- Writing the **Data Availability Statement** for submission (it is required at submission)
- Building the replication package (data, code, documentation) to back that statement
- Data cannot be fully shared (privacy, ethics, legal/provider restrictions) and you need the
  exemption/access path
- A qualitative or comparative-historical paper needs a transparency plan for sources and process tracing
- Referencing a preregistration / pre-analysis plan (it may be supplied as supplementary material)

## The Data Availability Statement (mandatory)

The statement must say, plainly, **whether** replication materials are available and **how** to get them.
Pick the case that matches reality and state it exactly:

- **Openly available** — "The data and code that support the findings of this study are openly available
  in [repository] at [DOI/URL]." Name a **DOI-citable** repository (Harvard Dataverse, OSF, or Zenodo
  are good choices) rather than a personal website or a generic cloud link.
- **Available on request / restricted** — say why (provider terms, privacy, ethics) and give the **exact
  access route** (application process, provider contact, data-use agreement).
- **Not applicable** — only if the study genuinely generated/analyzed no shareable data; say so honestly.

Do not write "available on request" as a euphemism for "not prepared." Match the statement to materials
that actually exist.

## Checklist (build the replication materials as you go)

- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, country/case coverage, construction steps, and how to
      reproduce each exhibit
- [ ] **Seeds** set and reported for every stochastic step
- [ ] Software/package **versions pinned** (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] Exhibit numbers in the manuscript **match** the package output exactly
- [ ] Materials deposited in a **DOI-citable repository**; the DOI appears in the statement

Even though no editor re-runs your code pre-publication, post-publication scrutiny and replication are
real; a package that does not reproduce your tables is a reputational liability.

## Qualitative & comparative-historical transparency

- Document **sources and the process-tracing chain**: an evidence/source table linking each key claim to
  its document, interview, or archival reference.
- Use **active-citation / annotated-source** practices where the analytic weight rests on specific texts.
- The **Qualitative Data Repository (QDR)** is an option for depositing qualitative data with
  controlled access (interview transcripts, fieldnotes) where ethics/consent limit open sharing.

## Restricted data (exemption / access path)

- **Explain why** the data are not openly available (provider terms, privacy, ethics, legal limits).
- Provide **README instructions on exactly how others can obtain the data** (application, provider
  contact, data-use agreement steps).
- Where feasible, provide **synthetic data** resembling the real data so the code can be executed.

## Pre-analysis plan

- An **anonymized pre-analysis plan may be supplied as supplementary material** for prospective designs;
  reference it (anonymized for double-blind review) and keep the analysis consistent with it.

## Anti-patterns

- Treating the Data Availability Statement as boilerplate decoupled from real materials
- "Available on request" used to avoid preparing data that could be shared
- A personal URL or expiring cloud link instead of a DOI-citable repository
- Claiming data are restricted with no access path and no synthetic substitute
- Assuming "no verified reproduction check" means the code need not actually reproduce the tables
- Undocumented, un-seeded, unpinned code that "works on my machine"

## Output format

```
【Statement case】openly available / restricted-with-access / not applicable
【Repository】DOI-citable (Dataverse / OSF / Zenodo)? DOI in statement? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Restricted data?】reason + access path + synthetic data? [Y/N/NA]
【Qualitative transparency】sources/process-tracing documented (QDR if needed)? [Y/N/NA]
【Pre-analysis plan】anonymized, as supplementary? [Y/N/NA]
【Next】govern-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories (Dataverse/OSF/Zenodo), reproducibility tooling, QDR
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — *Governance* Data Availability Statement policy and Wiley data-sharing guidance

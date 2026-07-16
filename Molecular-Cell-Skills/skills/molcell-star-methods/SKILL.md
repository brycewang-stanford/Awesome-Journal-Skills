---
name: molcell-star-methods
description: Use to build Molecular Cell's mandatory STAR Methods — the Key Resources Table, the Resource Availability subsections, Experimental Model and Subject Details, Method Details, and Quantification and Statistical Analysis, in the required order and with the reagent transparency Molecular Cell reviewers demand.
---

# STAR Methods (molcell-star-methods)

## When to trigger

- The manuscript has a free-text Methods section (Molecular Cell requires STAR Methods).
- There is no **Key Resources Table**, or reagents lack identifiers/RRIDs/catalog numbers.
- The **Resource Availability** block is missing one of its required subsections.
- Statistics are scattered in legends with no consolidated analysis section.

**STAR Methods = Structured, Transparent, Accessible Reporting.** It is a Cell Press signature and is **mandatory** at Molecular Cell. Because Molecular Cell papers live or die on reagent- and construct-level detail, this is the single most scrutinized methods deliverable.

## Mandatory STAR Methods structure (exact order)

1. **Key Resources Table (KRT)**
2. **Resource Availability** — required subsections:
   a. **Lead Contact**
   b. **Materials Availability**
   c. **Data and Code Availability**
3. **Experimental Model and Subject Details** (or **Experimental Model and Study Participant Details**)
4. **Method Details**
5. **Quantification and Statistical Analysis** (QSA)

> Some versions add **Additional Resources** at the end. Confirm the current Cell Press STAR Methods structure and headings.

## 1. Key Resources Table (KRT)

A structured table listing **every** reagent and resource, grouped by category, each with its **source** and an **identifier** (RRID, catalog #, accession, DOI, or repository link). For a molecular-biology paper this table is dense — every plasmid, primer, and purified protein must appear.

| REAGENT or RESOURCE | SOURCE | IDENTIFIER |
|---------------------|--------|------------|
| **Antibodies** | | |
| Anti-X (clone, host) | Vendor / lab | Cat# ____; RRID:AB______ |
| **Bacterial and Virus Strains** | | |
| **Chemicals, Peptides, Recombinant Proteins** | | |
| Purified PROTEIN X (residues a–b) | This paper | N/A |
| **Critical Commercial Assays** | | |
| **Deposited Data** | | |
| ChIP-seq / RNA-seq, this paper | This paper | GEO: GSE______ |
| Cryo-EM map / model, this paper | This paper | EMDB: EMD-____ ; PDB: ____ |
| Mass spec, this paper | This paper | PRIDE: PXD______ |
| **Experimental Models: Cell Lines** | | |
| **Experimental Models: Organisms/Strains** | | |
| **Oligonucleotides** | | |
| sgRNA / primer / probe sequence | This paper | N/A |
| **Recombinant DNA** (plasmids) | | Addgene #______ |
| **Software and Algorithms** | | RRID:SCR______ / DOI |

Rules:
- [ ] Every antibody, cell line, strain, plasmid, oligo, purified protein, dataset, and software package appears.
- [ ] Antibodies carry a **catalog #** and **RRID** where available.
- [ ] Purified/recombinant proteins state the construct boundaries and tags.
- [ ] Cell lines and organisms identify source and validation/authentication (and mycoplasma status).
- [ ] Deposited data list the **accession/DOI** for *this paper's* data (see `molcell-data`).
- [ ] Software lists version and an identifier (RRID:SCR___ or DOI); custom code points to its archived repository.

## 2. Resource Availability (required subsections)

- **Lead Contact** — one named corresponding author who fields resource/reagent requests, with email.
- **Materials Availability** — how unique reagents (plasmids, cell lines, antibodies, purified proteins, mouse lines) are shared, via Addgene/repository or under an MTA; or "This study did not generate new unique reagents."
- **Data and Code Availability** — the standardized statement (data / code / additional information), each with a sentence (built in `molcell-data`).

All subsections must be present even when the answer is "none/not applicable."

## 3. Experimental Model and Subject Details

Organisms, strains, cell lines (sex, age, source, passage, authentication, mycoplasma), yeast/bacterial genotypes, recombinant expression hosts, patient/participant details (with ethics approvals and consent), housing and husbandry. State IRB/IACUC approvals and protocol numbers here.

## 4. Method Details

Step-by-step procedures in enough detail to reproduce, organized by technique with subheadings, referencing reagents by their KRT entries: protein expression and purification (constructs, tags, columns), reconstitution conditions, in-vitro assays, cryo-EM/crystallography data collection and processing, genomics library prep and pipelines, and any single-molecule setups. A Molecular Cell reader should be able to rebuild the biochemistry.

## 5. Quantification and Statistical Analysis (QSA)

A consolidated section: for each quantified result, the **statistical test**, definition of **n** and what it represents, **dispersion** (SD/SEM/CI), significance thresholds, software used, and how outliers/exclusions were handled. For structures, report resolution, refinement, and validation statistics; for genomics, normalization and replicate handling; for kinetics/single-molecule, the fitting model and number of events. Statistics in figure legends must match QSA.

## Output format

```
【KRT present】 yes/no — categories covered; antibodies w/ Cat#+RRID; purified proteins w/ constructs; deposited data w/ accession
【Resource Availability】 Lead Contact ☐ / Materials Availability ☐ / Data & Code Availability ☐
【Exp. Model & Subject Details】 organisms/lines/hosts/participants + ethics (IRB/IACUC)? yes/no
【Method Details】 reproducible, KRT-linked, purification/reconstitution described? yes/no
【QSA】 per-result test + n-definition + dispersion + software + structure/genomics stats? yes/no
【Gaps】 [...]
【Next】 molcell-data
```

## Anti-patterns

- **Do not** submit a free-text Methods section — Molecular Cell requires STAR Methods.
- **Do not** omit RRIDs/catalog numbers for antibodies and software.
- **Do not** leave purified-protein constructs, tags, or oligo sequences out of the KRT.
- **Do not** drop any Resource Availability subsection.
- **Do not** leave statistics only in legends — consolidate in QSA.

> The exact STAR Methods headings and KRT categories are set by Cell Press — confirm against the current STAR Methods author guidelines.

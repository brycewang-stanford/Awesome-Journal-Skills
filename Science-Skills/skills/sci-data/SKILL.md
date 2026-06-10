---
name: sci-data
description: Use to build Science's data, code, and materials availability — mandatory deposition in approved repositories, accession numbers, a compliant data-availability statement, and materials/reagent sharing.
---

# Data, Code & Materials Availability (sci-data)

## When to trigger

- There is no data-availability statement, or it says "available on request".
- Sequences/structures/datasets are not deposited or have no accession numbers.
- Custom analysis code is not in a public repository.
- Unique reagents/strains/cell lines have no sharing plan.

## Science's standard (the bar)

Science requires that **all data and methods needed to evaluate and reproduce the conclusions be available** at publication. "Available upon request" is **not** sufficient for primary data underlying the results.

## Deposit in approved repositories (with accessions)

| Data type                          | Deposit in (examples)                      |
|------------------------------------|--------------------------------------------|
| Nucleotide / genome sequences      | GenBank / ENA / DDBJ                        |
| High-throughput sequencing         | GEO / SRA / ArrayExpress                    |
| Protein structures                 | PDB; maps → EMDB                            |
| Proteomics                         | PRIDE / ProteomeXchange                     |
| Crystallographic data              | CCDC / CSD                                  |
| Generic datasets                   | Dryad / Zenodo / Figshare / OSF            |
| Code                               | GitHub/GitLab **+ archived** to Zenodo (DOI) |

- Obtain **accession numbers / DOIs before submission**; cite them in the data-availability statement and Methods.
- Code that produces the results must be public; archive a release to get a citable DOI (a bare GitHub link is not durable).

## Data-availability statement (template)

> All data needed to evaluate the conclusions are present in the paper and/or the Supplementary Materials. [Sequencing data are deposited at GEO under accession GSEXXXXXX.] [Structures are deposited at the PDB under XXXX.] [Analysis code is available at Zenodo (DOI: 10.5281/zenodo.XXXXXXX).] [Any additional materials are available from the corresponding author / under an MTA as noted.]

Avoid bare "data available on request" for primary data; restricted human/clinical data must state the access procedure and the controlling body.

## Materials & reagents

- Unique materials (plasmids, cell lines, strains, antibodies) should be available, e.g., via Addgene/repositories or under an MTA; state how.
- Identify key reagents with RRIDs where available.

## Ethics & compliance (as applicable)

- Human-subjects: IRB/ethics approval + informed consent statement.
- Animal work: IACUC/animal-ethics approval and guideline compliance.
- Field/biodiversity: permits and the Nagoya Protocol where relevant.
- Dual-use / biosafety: flag if applicable.


## Data pass for Science

Use this as a second-pass capability check. First lock the broad discovery claim, decisive evidence, uncertainty/limitations, and why the result belongs in a general-science weekly; then test whether the manuscript addresses general-science reviewers and editors who ask whether the result changes a broad field, is technically decisive, and can be understood outside the subdiscipline.

- **Primary move:** Name data provenance, availability, code/materials access, restrictions, quality control, and the exact evidence needed to reproduce the central result.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Nature for similar broad-scope novelty, PNAS for academy-wide breadth, specialist journals when the claim is field-internal; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Data deposited】 type → repository → accession/DOI (list each)  | gaps
【Code public + archived DOI】 yes/no (link + DOI)
【Availability statement】 drafted? compliant (no "on request" for primary data)?
【Materials sharing】 plan for unique reagents (Addgene/MTA)
【Ethics approvals】 IRB / IACUC / permits present where needed?
【Next】 sci-abstract
```

## Anti-patterns

- **Do not** write "data available on request" for the primary data behind figures.
- **Do not** link only to a personal/lab website (not durable) — use an archival repository with a DOI.
- **Do not** forget to make code public and versioned; reviewers may try to run it.
- **Do not** submit without accession numbers in hand for deposited data.

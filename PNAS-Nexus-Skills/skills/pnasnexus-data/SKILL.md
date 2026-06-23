---
name: pnasnexus-data
description: Use to build PNAS Nexus's Data and Code Availability — mandatory public-repository deposition of all materials, data, code, and protocols upon publication, retention of raw unprocessed images, accession numbers/DOIs, the [dataset] citation tag, and a compliant availability statement. "Available on request" alone is not sufficient, and failure can be grounds for rejection or retraction.
---

# Data & Code Availability (pnasnexus-data)

## When to trigger

- There is no **Data Availability Statement**, or it says only "available on request".
- Sequences/structures/datasets are not deposited or have no accession numbers.
- Custom analysis code or scripts are not in a public, archived repository.
- Raw, unprocessed image files have been discarded.
- Unique reagents/strains/cell lines have no sharing plan.

## PNAS Nexus's standard (the bar is strict, with teeth)

PNAS Nexus has a **mandatory** open-data/open-code policy. In the journal's own words:

- *"Authors must make all materials, data, and associated protocols, including code and scripts, used in the analysis of the study available to readers in a **public repository upon publication**."*
- *"Authors agree to make all data and code used in the analysis of their study fully available upon request during the peer review process or upon publication."*
- *"All data and any direct outputs from imaging systems must be retained in their **raw, unprocessed versions**."*
- *"Failure or refusal to provide data upon request may be grounds for **rejection of the manuscript or retraction of the article**."*

So: **public-repository deposition upon publication is required**, raw images must be kept, and non-compliance is an explicit rejection/retraction risk. (Confirm the current wording in PNAS Nexus author guidelines.)

## Deposit in approved repositories (with accessions)

| Data type                          | Deposit in (examples)                      |
|------------------------------------|--------------------------------------------|
| Nucleotide / genome sequences      | GenBank / ENA / DDBJ                        |
| High-throughput sequencing         | GEO / SRA / ArrayExpress                    |
| Protein/macromolecular structures  | PDB; maps → EMDB                            |
| Proteomics                         | PRIDE / ProteomeXchange                     |
| Crystallographic data              | CCDC / CSD                                  |
| Generic datasets                   | Dryad / Zenodo / Figshare / OSF            |
| Code / scripts                     | GitHub/GitLab **+ archived** to Zenodo (DOI) |

- Obtain **accession numbers / DOIs before/at publication**; cite them in the Data Availability Statement and Materials and Methods.
- Code and scripts that produce the results must be **public and archived** (a versioned release with a citable DOI; a bare GitHub link is not durable).

## Cite data and software properly: the `[dataset]` tag

PNAS Nexus follows the **FORCE11 Data Citation Principles** and asks authors to flag dataset references with the **`[dataset]`** tag in the reference list, so deposited data are formally cited (confirm the exact mechanics in current guidelines). Treat datasets and software as **first-class citable objects**, not just URLs in the text.

## Data & Code Availability Statement (template)

> *All data and code needed to evaluate the conclusions are present in the paper and/or the Supporting Information and have been deposited in a public repository. [Sequencing data: GEO, accession GSEXXXXXX.] [Structures: PDB, XXXX.] [Analysis code and scripts: Zenodo, DOI 10.5281/zenodo.XXXXXXX.] [Previously published data used here are available at …] [Restricted data (e.g., identifiable human-subjects data) are available from … under … subject to …, in line with the journal's policy.]*

Avoid a bare "data available on request" for the primary data behind the figures; restricted human/clinical data must state the access procedure and the controlling body.

## Where the statement and the data live

- The **Data and Code Availability Statement** is a required element of the article (near the end, with the back matter — confirm placement in current guidelines).
- Reference the deposited data in **both** the availability statement **and** the Materials and Methods, so a reader following the methods can reach the data.
- Datasets too large for a figure but central to the conclusions go to a repository cited by accession/DOI — not "available on request."

## Materials & reagents

- Unique materials (plasmids, cell lines, strains, antibodies) should be available, e.g., via Addgene/repositories or under an MTA; state how.
- Identify key reagents with RRIDs where available.

## Ethics & compliance (as applicable)

- Human-subjects: IRB/ethics approval + informed-consent statement.
- Animal work: IACUC/animal-ethics approval and guideline compliance.
- Field/biodiversity: permits and the Nagoya Protocol where relevant.
- Dual-use / biosafety: flag if applicable.

## Output format

```
【Data deposited】 type → repository → accession/DOI (list each) | gaps
【Code/scripts public + archived DOI】 yes/no (link + DOI)
【Raw unprocessed images retained】 yes/no (required)
【Availability statement】 drafted? compliant (public repo on publication; no "on request" only for primary data)?
【[dataset] tags】 data/software cited as first-class objects? yes/no
【Materials sharing】 plan for unique reagents (Addgene/MTA)
【Ethics approvals】 IRB / IACUC / permits present where needed?
【Next】 pnasnexus-significance
```

## Anti-patterns

- **Do not** write "data available on request" as the only provision for the primary data behind the figures.
- **Do not** discard raw/unprocessed image files — the policy requires retaining them.
- **Do not** link only to a personal/lab website (not durable) — use an archival repository with a DOI.
- **Do not** forget to deposit code and scripts publicly and archive a versioned release.
- **Do not** treat the data policy as advisory — non-compliance is an explicit rejection/retraction risk.

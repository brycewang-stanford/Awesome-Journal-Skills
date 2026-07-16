---
name: molcell-data
description: Use to build Molecular Cell's data and code deposition plan and the Data and Code Availability statement inside STAR Methods Resource Availability — approved repositories (GEO, PDB/EMDB, PRIDE), accessions/DOIs at submission, and Cell Press's standardized availability format with Mendeley Data as Elsevier's default.
---

# Data & Code Availability (molcell-data)

## When to trigger

- There is no Data and Code Availability statement, or it says "available on request."
- Sequencing / structures / proteomics / datasets are not deposited or lack accessions.
- Custom analysis code is not in a public, archived repository.
- You need to draft the standardized statement for STAR Methods Resource Availability.

## Where the statement lives

Molecular Cell's **Data and Code Availability** statement is a required subsection of **Resource Availability** inside **STAR Methods** (see `molcell-star-methods`) — not a free-floating paragraph. Datasets deposited for *this paper* must also appear in the **Key Resources Table** under "Deposited Data."

## Deposit in approved repositories (with accession/DOI)

| Data type | Deposit in (examples) |
|-----------|------------------------|
| High-throughput sequencing (ChIP/RNA/ATAC/CLIP-seq) | **GEO** / **SRA** |
| Nucleotide / genome sequences | GenBank / ENA / DDBJ |
| Macromolecular structures | **PDB** |
| Cryo-EM maps (and half-maps) | **EMDB** (map) + **PDB** (model) |
| Crystallography | PDB (coordinates + structure factors) |
| Proteomics / mass spec / cross-linking MS | **PRIDE** / **ProteomeXchange** (+ **jPOST** where used) |
| NMR | **BMRB** + PDB |
| Imaging / general structured datasets | **BioStudies** / BioImage Archive |
| Generic datasets (Elsevier default) | **Mendeley Data**, or Zenodo / Dryad |
| Plasmids / unique reagents | **Addgene** |
| Code (archive a release for a DOI) | GitHub/GitLab **+ Zenodo** (citable DOI) |

> **Mendeley Data is Elsevier's default repository** for datasets without a dedicated community repository. Prefer a community repository (GEO, PDB/EMDB, PRIDE) when one exists for the data type — Molecular Cell's molecular focus means most primary data have one.

- Obtain **accession numbers / DOIs before submission**; reviewers and editors expect them in hand, and for structures they will check map-model fit against the deposited entry.
- Code that reproduces the analysis must be **public and archived** (a citable DOI via Zenodo) — a bare GitHub link is not durable.

## Cell Press Data and Code Availability format

Cell Press uses a standardized statement. Provide a sentence for each item:

```
Data and Code Availability

• [DATA] The [datatype] data generated in this study have been deposited at
  [GEO / PDB+EMDB / PRIDE] and are publicly available as of the date of
  publication. Accession numbers are listed in the Key Resources Table. /
  This paper analyzes existing, publicly available data [accessions in KRT].

• [CODE] All original code has been deposited at [Zenodo/Mendeley Data] and is
  publicly available as of the date of publication. DOIs are listed in the Key
  Resources Table. / This paper does not report original code.

• [ADDITIONAL] Any additional information required to reanalyze the data
  reported in this paper is available from the Lead Contact upon request.
```

Each item must be addressed even if the answer is "this paper does not report…". Restricted human/clinical data must state the controlled-access procedure and the controlling body.

## Structure-specific deposition (Molecular Cell-heavy)

- **Cryo-EM**: deposit the map (and typically half-maps and mask) at **EMDB** and the model at **PDB**; report the resolution and the FSC threshold used.
- **X-ray**: deposit coordinates **and structure factors** at PDB.
- Validation reports should be generatable from the deposited entries — reviewers may request them.

## Materials & ethics cross-links

- Unique materials sharing belongs in **Materials Availability** (`molcell-star-methods`); use Addgene/MTA and state how.
- Ethics approvals (IRB/IACUC, consent, permits) belong in **Experimental Model and Subject Details**.
- Identify key reagents with **RRIDs** in the Key Resources Table.

## Output format

```
【Data deposited】 type → repository → accession/DOI (list each)  | gaps
【Structures】 EMDB/PDB (map+model) or PDB (coords+SF)? resolution/FSC stated?
【Code public + archived DOI】 yes/no (repo + Zenodo/Mendeley DOI)
【Statement】 DATA ☐ / CODE ☐ / ADDITIONAL ☐ — all drafted?
【In KRT "Deposited Data"】 accessions listed? yes/no
【Restricted data】 controlled-access procedure stated where needed?
【Next】 molcell-summary
```

## Anti-patterns

- **Do not** write "available on request" for the primary data behind the figures.
- **Do not** deposit a structure model without its map/structure factors.
- **Do not** link only to a personal/lab website — use an archival repository with a DOI.
- **Do not** forget to mirror accessions into the Key Resources Table.
- **Do not** submit without accession numbers/DOIs in hand.

> Confirm repository requirements and the exact availability wording against current Cell Press / STAR Methods guidelines.

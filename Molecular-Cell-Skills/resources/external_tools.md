# External Tools & Resources for Molecular Cell Submissions

A working list of repositories, software, and references useful when preparing a manuscript for *Molecular
Cell* (Mol. Cell, Cell Press). Always confirm specifics against the current
[Molecular Cell information for authors](https://www.cell.com/molecular-cell/information-for-authors) and
the [STAR Methods guidelines](https://www.cell.com/star-methods).

## 1. Data, structure & code deposition (with accession/DOI)

| Data type | Deposit in |
|-----------|-----------|
| High-throughput sequencing (ChIP/RNA/ATAC/CLIP-seq) | [GEO](https://www.ncbi.nlm.nih.gov/geo/), [SRA](https://www.ncbi.nlm.nih.gov/sra) |
| Nucleotide / genome sequences | [GenBank](https://www.ncbi.nlm.nih.gov/genbank/), [ENA](https://www.ebi.ac.uk/ena), [DDBJ](https://www.ddbj.nig.ac.jp/) |
| Macromolecular structures | [PDB (RCSB)](https://www.rcsb.org/) / [PDBe](https://www.ebi.ac.uk/pdbe/) |
| Cryo-EM maps (+ half-maps) | [EMDB](https://www.ebi.ac.uk/emdb/) (map) + PDB (model) |
| NMR | [BMRB](https://bmrb.io/) + PDB |
| Proteomics / mass spec / XL-MS | [PRIDE](https://www.ebi.ac.uk/pride/) / [ProteomeXchange](http://www.proteomexchange.org/) |
| Imaging / general structured datasets | [BioStudies](https://www.ebi.ac.uk/biostudies/) / [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/) |
| Generic datasets (Elsevier default) | [Mendeley Data](https://data.mendeley.com/), [Zenodo](https://zenodo.org/), [Dryad](https://datadryad.org/) |
| Materials / plasmids | [Addgene](https://www.addgene.org/) |
| Code (archive a release for a DOI) | GitHub/GitLab + [Zenodo integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) |

> **Mendeley Data is Elsevier's default repository** for datasets without a dedicated community repository.
> Prefer a community repository (GEO, PDB/EMDB, PRIDE) when one exists — Molecular Cell's molecular focus
> means most primary data have one. "Available upon request" is not acceptable for primary data; get
> accessions/DOIs **before** submission and mirror them into the STAR Methods **Key Resources Table**
> ("Deposited Data"). Structures must be deposited with maps (cryo-EM) or structure factors (X-ray).

## 2. STAR Methods, reporting & integrity standards

- [Cell Press STAR Methods](https://www.cell.com/star-methods) — Structured, Transparent, Accessible Reporting; the Key Resources Table and Resource Availability structure.
- [CRediT](https://credit.niso.org/) — author contribution taxonomy.
- [ORCID](https://orcid.org/) — author identifiers.
- [RRID / SciCrunch](https://scicrunch.org/resources) — Research Resource Identifiers for antibodies, cell lines, organisms, plasmids, and software (used throughout the Key Resources Table).
- [ARRIVE 2.0](https://arriveguidelines.org/) — animal research reporting.
- [wwPDB validation](https://validate.wwpdb.org/) — structure validation reports; [EMDB map validation](https://www.ebi.ac.uk/emdb/) for cryo-EM.
- [EQUATOR Network](https://www.equator-network.org/) — index of reporting guidelines.

## 3. The Cell Press signature artifacts

- **Highlights** — 3–4 bullets, each ≤ 85 characters; see the author guidelines for exact formatting.
- **eTOC / In Brief blurb** — ~50 words, third-person, for readers outside the exact subfield.
- **Graphical Abstract** — single-panel visual summary of the mechanism; see the [Cell Press Graphical Abstract guidelines](https://www.cell.com/pb-assets/journals/research/cellpress/graphical_abstract_guidelines.pdf) for size and design rules.

## 4. Molecular-biology stack (sequence, structure, imaging)

- Sequence/alignment: [BLAST](https://blast.ncbi.nlm.nih.gov/), [Clustal Omega](https://www.ebi.ac.uk/jdispatcher/msa/clustalo), [MAFFT](https://mafft.cbrc.jp/alignment/software/), [Jalview](https://www.jalview.org/).
- Structure viewing/analysis: [PyMOL](https://pymol.org/), [ChimeraX](https://www.cgl.ucsf.edu/chimerax/), [Coot](https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/); cryo-EM: [RELION](https://relion.readthedocs.io/), [cryoSPARC](https://cryosparc.com/); prediction: [AlphaFold](https://alphafold.ebi.ac.uk/).
- Genomics: [Bowtie2](https://bowtie-bio.sourceforge.net/bowtie2/)/[STAR](https://github.com/alexdobin/STAR), [samtools](http://www.htslib.org/), [deepTools](https://deeptools.readthedocs.io/), [MACS](https://github.com/macs3-project/MACS), [IGV](https://igv.org/), [Bioconductor](https://bioconductor.org/) (DESeq2/edgeR).
- Imaging/quantification: [Fiji/ImageJ](https://imagej.net/software/fiji/) with logging; [CellProfiler](https://cellprofiler.org/); keep unprocessed source images and follow Cell Press digital-image guidelines.

## 5. Figures, statistics & reproducibility

- Vector tools: Adobe Illustrator, [Inkscape](https://inkscape.org/); BioRender for schematics and Graphical Abstracts.
- Plotting: [matplotlib](https://matplotlib.org/), [ggplot2](https://ggplot2.tidyverse.org/), [SciencePlots](https://github.com/garrettj403/SciencePlots).
- Colorblind-safe palettes: [viridis](https://bids.github.io/colormap/), [ColorBrewer](https://colorbrewer2.org/), [Okabe-Ito](https://jfly.uni-koeln.de/color/).
- Statistics: R ([tidyverse](https://www.tidyverse.org/), [lme4](https://cran.r-project.org/package=lme4), [emmeans](https://cran.r-project.org/package=emmeans)), Python ([statsmodels](https://www.statsmodels.org/), [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html), [pingouin](https://pingouin-stats.org/)); power analysis: [G*Power](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower).
- Environments: [conda](https://docs.conda.io/), [renv](https://rstudio.github.io/renv/), [Docker](https://www.docker.com/); record versions and seeds in Quantification and Statistical Analysis.

## 6. References & writing

- Reference managers: [Zotero](https://www.zotero.org/), [EndNote](https://endnote.com/downloads/styles/molecular-cell/) — use the current **Molecular Cell / Cell Press** CSL/style. Cell Press is now **numbered** (superscript, order of appearance); verify full author lists and journal-abbreviation form on a final pass, and re-run the manager after any edit that adds/removes a citation.
- Molecular Cell accepts Word or LaTeX; see the Cell Press LaTeX template and the Editorial Manager submission system.

## 7. Useful pages

| Page | URL |
|------|-----|
| Molecular Cell — home | https://www.cell.com/molecular-cell/home |
| Molecular Cell — information for authors | https://www.cell.com/molecular-cell/information-for-authors |
| Molecular Cell — article types | https://www.cell.com/molecular-cell/article-types |
| Cell Press STAR Methods | https://www.cell.com/star-methods |
| Cell Press numbered referencing style | https://www.cell.com/news-do/cell-press-referencing-style |
| Graphical Abstract guidelines | https://www.cell.com/pb-assets/journals/research/cellpress/graphical_abstract_guidelines.pdf |
| Editorial Manager (submission) | https://www.editorialmanager.com/molecular-cell |

## 8. Notes

1. **Single-blind** review is typical at Molecular Cell — do not anonymize unless instructed.
2. Molecular Cell operates under **embargo**; coordinate any press through Cell Press.
3. **Family fit**: solid and complete but mechanism not deep → **Cell Reports** (more accepting); broad cross-field complete story → **Cell**; specialist structural depth → **NSMB / Structure**. A referral/transfer may be offered.
4. **One Lead Contact** is required in Resource Availability; keep raw source data, unprocessed images, and structure half-maps — editors/reviewers can request them at any stage.

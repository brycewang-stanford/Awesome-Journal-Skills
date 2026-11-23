# External Tools & Resources for Cell Submissions

A working list of repositories, software, and references useful when preparing a manuscript for *Cell* (Cell Press). Always confirm specifics against the current [Cell Press author guidelines](https://www.cell.com/cell/authors) and the [STAR Methods guidelines](https://www.cell.com/star-methods).

## 1. Data & code deposition (with accession/DOI)

| Data type | Deposit in |
|-----------|-----------|
| High-throughput sequencing | [GEO](https://www.ncbi.nlm.nih.gov/geo/), [SRA](https://www.ncbi.nlm.nih.gov/sra) |
| Nucleotide / genome sequences | [GenBank](https://www.ncbi.nlm.nih.gov/genbank/), [ENA](https://www.ebi.ac.uk/ena), [DDBJ](https://www.ddbj.nig.ac.jp/) |
| Protein/macromolecular structures | [PDB](https://www.rcsb.org/); cryo-EM maps → [EMDB](https://www.ebi.ac.uk/emdb/) |
| Proteomics / mass spec | [PRIDE](https://www.ebi.ac.uk/pride/) / [ProteomeXchange](http://www.proteomexchange.org/) |
| Imaging / general structured datasets | [BioStudies](https://www.ebi.ac.uk/biostudies/) / [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/) |
| Generic datasets (Elsevier default) | [Mendeley Data](https://data.mendeley.com/), [Zenodo](https://zenodo.org/), [Dryad](https://datadryad.org/) |
| Materials / plasmids | [Addgene](https://www.addgene.org/) |
| Code (archive a release for a DOI) | GitHub/GitLab + [Zenodo integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) |

> **Mendeley Data is Elsevier's default repository** for datasets without a dedicated community repository. Prefer a community repository (GEO, PDB, PRIDE) when one exists. "Available upon request" is not acceptable for primary data — get accessions/DOIs **before** submission, and mirror them into the STAR Methods **Key Resources Table** ("Deposited Data").

## 2. STAR Methods, reporting & integrity standards

- [Cell Press STAR Methods](https://www.cell.com/star-methods) — Structured, Transparent, Accessible Reporting; the Key Resources Table and Resource Availability structure.
- [CRediT](https://credit.niso.org/) — author contribution taxonomy.
- [ORCID](https://orcid.org/) — author identifiers (required for corresponding/often all authors).
- [RRID / SciCrunch](https://scicrunch.org/resources) — Research Resource Identifiers for antibodies, cell lines, organisms, and software (used throughout the Key Resources Table).
- [ARRIVE 2.0](https://arriveguidelines.org/) — animal research reporting.
- [EQUATOR Network](https://www.equator-network.org/) — index of reporting guidelines by study type.

## 3. The Cell signature artifacts

- **Highlights** — 3–4 bullets, each ≤ 85 characters; see the Cell Press author guidelines for exact formatting.
- **eTOC / In Brief blurb** — ~50 words, third-person, for non-specialists.
- **Graphical Abstract** — single-panel visual summary; see the [Cell Press Graphical Abstract guidelines](https://www.cell.com/pb/assets/raw/shared/figureguidelines/GA_guide.pdf) for size and design rules.

## 4. Figures & visualization

- Vector tools: Adobe Illustrator, [Inkscape](https://inkscape.org/) (free); BioRender for schematics and Graphical Abstracts.
- Plotting: [matplotlib](https://matplotlib.org/), [ggplot2](https://ggplot2.tidyverse.org/), [SciencePlots](https://github.com/garrettj403/SciencePlots).
- Colorblind-safe palettes: [viridis](https://bids.github.io/colormap/), [ColorBrewer](https://colorbrewer2.org/), [Okabe-Ito](https://jfly.uni-koeln.de/color/).
- Image integrity: keep unprocessed source images; [Fiji/ImageJ](https://imagej.net/software/fiji/) with logging; follow Cell Press digital image guidelines.

## 5. Statistics & reproducibility

- R ([tidyverse](https://www.tidyverse.org/), [lme4](https://cran.r-project.org/package=lme4), [emmeans](https://cran.r-project.org/package=emmeans)), Python ([statsmodels](https://www.statsmodels.org/), [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html), [pingouin](https://pingouin-stats.org/)).
- Power analysis: [G*Power](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower).
- Environments: [conda](https://docs.conda.io/), [renv](https://rstudio.github.io/renv/), [Docker](https://www.docker.com/); record versions and seeds (state in Quantification and Statistical Analysis).

## 6. References & writing

- Reference managers: [Zotero](https://www.zotero.org/), [EndNote](https://endnote.com/) — use the **Cell Press** CSL/style (author–date, alphabetical); verify full author lists and journal-name form on a final pass.
- LaTeX/Word: Cell accepts Word or LaTeX; see the Cell Press LaTeX template via Overleaf and the Editorial Manager submission system.
- Journal abbreviations / names: confirm against Cell Press style (often spelled out).

## 7. Useful pages

| Page | URL |
|------|-----|
| Cell — Information for Authors | https://www.cell.com/cell/authors |
| Cell Press STAR Methods | https://www.cell.com/star-methods |
| Graphical Abstract guidelines | https://www.cell.com/pb/assets/raw/shared/figureguidelines/GA_guide.pdf |
| Cell Press data & code availability policy | https://www.cell.com/cell/authors |
| Cell Press journals (Molecular Cell, Cell Reports, etc.) | https://www.cell.com/ |
| Editorial Manager (submission) | https://www.editorialmanager.com/cell/ |

## 8. Notes

1. **Single-blind** review is typical at Cell — do not anonymize unless instructed.
2. Cell operates under **embargo**; coordinate any press through Cell Press.
3. **Family fit**: if the work is solid and complete but not broadly transformative, consider **Cell Reports** (more accepting); deep molecular mechanism → **Molecular Cell**; translational → **Cell Reports Medicine**. A referral/transfer may be offered.
4. **One Lead Contact** is required in Resource Availability; keep raw source data and unprocessed images — editors/reviewers can request them at any stage.

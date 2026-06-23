# External Tools & Resources for PNAS Nexus Submissions

A working list of repositories, software, and references useful when preparing a manuscript for *PNAS Nexus* — the **gold open-access** sibling journal of PNAS, published by **Oxford University Press (OUP)** on behalf of the **National Academy of Sciences (NAS)**. Always confirm specifics against the current [PNAS Nexus author guidelines](https://academic.oup.com/pnasnexus/pages/general-instructions). For the authoritative fact-of-record map (editors, APC, licenses, length, policy), see [`official-source-map.md`](official-source-map.md).

> **PNAS Nexus ≠ flagship PNAS.** Different business model (gold OA + APC), different editors, no Direct/Contributed submission track, page-based length limits, and references that are format-neutral at submission. Do not import facts from the `PNAS-Skills` pack.

## 1. Open access, APC & license

| Need | Where |
|------|-------|
| The binding APC (region/category-personalized) | OUP charges calculator on the [author-instructions page](https://academic.oup.com/pnasnexus/pages/general-instructions) — **confirm live; OUP publishes no fixed figure.** Third-party trackers disagree (≈US$2,200–4,200; [DOAJ](https://doaj.org/toc/2752-6542) ≈US$4,202); the billed amount is personalized and may be waived/discounted |
| OUP open-access charges, licenses & self-archiving | https://academic.oup.com/pages/open-research/open-access/charges-licences-and-self-archiving |
| Read & Publish / transformative agreements (institution pays) | check your library or OUP's institutional-agreements list |
| LMIC waiver/discount + discretionary waiver | OUP low- and middle-income-countries initiative; request at submission (historically openaccess@oup.com — confirm) |
| Choosing a CC license | [Creative Commons](https://creativecommons.org/licenses/) — PNAS Nexus offers **CC BY 4.0** and **CC BY-NC 4.0** |
| Funder OA compliance check | [Journal Checker Tool](https://journalcheckertool.org/) (Plan S / cOAlition S) |

## 2. Data & code deposition (with accession/DOI) — mandatory at PNAS Nexus

| Data type | Deposit in |
|-----------|-----------|
| Nucleotide / genome sequences | [GenBank](https://www.ncbi.nlm.nih.gov/genbank/), [ENA](https://www.ebi.ac.uk/ena), [DDBJ](https://www.ddbj.nig.ac.jp/) |
| High-throughput sequencing | [GEO](https://www.ncbi.nlm.nih.gov/geo/), [SRA](https://www.ncbi.nlm.nih.gov/sra), [ArrayExpress](https://www.ebi.ac.uk/biostudies/arrayexpress) |
| Protein/macromolecular structures | [PDB](https://www.rcsb.org/); maps → [EMDB](https://www.ebi.ac.uk/emdb/) |
| Proteomics | [PRIDE](https://www.ebi.ac.uk/pride/) / [ProteomeXchange](http://www.proteomexchange.org/) |
| Small-molecule crystallography | [CCDC / CSD](https://www.ccdc.cam.ac.uk/) |
| Generic datasets | [Dryad](https://datadryad.org/), [Zenodo](https://zenodo.org/), [Figshare](https://figshare.com/), [OSF](https://osf.io/) |
| Code (archive a release for a DOI) | GitHub/GitLab + [Zenodo integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) |
| Materials / plasmids | [Addgene](https://www.addgene.org/) |

> PNAS Nexus **requires** that materials, data, code, and protocols be available in a **public repository upon publication**, that raw/unprocessed images be retained, and cites data with the **`[dataset]`** tag (FORCE11). "Available on request" alone is not sufficient for primary data. Get accession numbers/DOIs **before/at** publication (see `pnasnexus-data`).

## 3. Reporting & integrity standards

- [ORCID](https://orcid.org/) — author identifiers.
- [RRID / SciCrunch](https://scicrunch.org/resources) — Research Resource Identifiers for reagents, antibodies, software.
- [ARRIVE 2.0](https://arriveguidelines.org/) — animal research reporting.
- [EQUATOR Network](https://www.equator-network.org/) — index of reporting guidelines (CONSORT, STROBE, PRISMA…) by study type.
- [CRediT](https://credit.niso.org/) — author contribution taxonomy.
- [OSF Registrations](https://osf.io/registries) / [AsPredicted](https://aspredicted.org/) — pre-registration; relevant for the **Registered Report** route.

## 4. Figures & visualization

- Vector tools: Adobe Illustrator, [Inkscape](https://inkscape.org/) (free).
- Plotting: [matplotlib](https://matplotlib.org/), [ggplot2](https://ggplot2.tidyverse.org/), [SciencePlots](https://github.com/garrettj403/SciencePlots).
- Colorblind-safe palettes: [viridis](https://bids.github.io/colormap/), [ColorBrewer](https://colorbrewer2.org/), [Okabe-Ito](https://jfly.uni-koeln.de/color/).
- Image integrity: keep unprocessed source images (PNAS Nexus requires it); [Fiji/ImageJ](https://imagej.net/software/fiji/) with logging.
- Color figures display freely online (OA) — confirm there are no separate color charges (see `pnasnexus-figures`).

## 5. Statistics & reproducibility

- R ([tidyverse](https://www.tidyverse.org/), [lme4](https://cran.r-project.org/package=lme4), [emmeans](https://cran.r-project.org/package=emmeans)), Python ([statsmodels](https://www.statsmodels.org/), [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html), [pingouin](https://pingouin-stats.org/)).
- Power analysis: [G*Power](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower).
- Environments: [conda](https://docs.conda.io/), [renv](https://rstudio.github.io/renv/), [Docker](https://www.docker.com/); record versions and seeds (code deposition is mandatory).

## 6. References & writing

- Reference managers: [Zotero](https://www.zotero.org/), [EndNote](https://endnote.com/). PNAS Nexus accepts **any readable style at submission** — focus on consistency, completeness, and DOIs; prepare a numbered/Vancouver style that converts cleanly for production (see `pnasnexus-citation`).
- Templates: PNAS Nexus offers **Word** and **LaTeX (Overleaf)** templates — get them from the author-instructions page.
- Journal abbreviations (if you adopt a numbered style): [CASSI / ISO 4](https://cassi.cas.org/).

## 7. Useful pages

| Page | URL |
|------|-----|
| PNAS Nexus journal home (OUP) | https://academic.oup.com/pnasnexus |
| Information for Authors (load-bearing) | https://academic.oup.com/pnasnexus/pages/general-instructions |
| What makes PNAS Nexus unique (scope, OA, article types) | https://academic.oup.com/pnasnexus/pages/what-makes-pnas-nexus-unique |
| Submitting to the PNAS portfolio (transfer/cascade) | https://academic.oup.com/pnasnexus/pages/submitting-to-the-pnas-portfolio |
| About (publisher, indexing, metrics) | https://academic.oup.com/pnasnexus/pages/about |
| Editorial board | https://academic.oup.com/pnasnexus/pages/editorial-board |
| Submission portal | https://pnasnexus.msubmit.net/ |

## 8. Notes

1. **Business model:** PNAS Nexus is **fully gold open access**; an **APC** applies and is priced via OUP's **personalized calculator** (region/category) — confirm live, and check waivers/Read-&-Publish (`pnasnexus-openaccess`).
2. **No submission tracks:** there is **no Direct vs Contributed (NAS-member) choice** — all editor-assigned peer review. An NAS member **cannot** contribute a paper here.
3. **Transfer route:** sound work declined by PNAS can be **transferred** to PNAS Nexus with reviews carried over (`pnasnexus-fit`).
4. **Significance Statement:** **50–120 words** for Research Reports / Stage 2 Registered Reports — note the **minimum** (`pnasnexus-significance`).
5. **Length is page-based** with named article types (Research Report 6 pp pref / 12 max; Brief Report ≤3 pp; Perspective/Review ≤10 pp; Registered Reports) (`pnasnexus-writing`).
6. **Materials and Methods stay in the main text** (cannot be solely in SI).
7. **Data/code:** public-repository deposition upon publication is **mandatory**, raw images retained, `[dataset]` citations, with rejection/retraction as the stated consequence of non-compliance (`pnasnexus-data`).

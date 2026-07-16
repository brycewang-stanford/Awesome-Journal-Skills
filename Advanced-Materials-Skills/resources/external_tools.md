# External Tools and Resources for Advanced Materials Submissions

This document collects the characterization-analysis, simulation, figure, and data-repository tools
commonly used when preparing an Advanced Materials (Adv. Mater.) submission. It is a practical
reference; always verify current Wiley Advanced Materials requirements on the official author page.

## 1. Manuscript preparation (Wiley-specific)

| Tool | Use |
|------|-----|
| **Wiley Advanced Materials template** | Word / LaTeX templates matching the journal's two-column typeset layout |
| **Overleaf** | Online LaTeX collaboration; hosts Wiley/Adv. Mater. templates |
| **Microsoft Word** | The most common Adv. Mater. submission format for experimental groups |
| **LaTeX (TeX Live / MacTeX)** | For math- or theory-heavy manuscripts |
| **EndNote / Zotero / Mendeley** | Reference management with the Wiley Advanced Materials output style |

> Length is counted in **typeset published pages**, not manuscript pages: ~4 pages for a Communication,
> ~10 for a Research Article, with figures/schemes/tables counted together with text. Typeset in the
> Wiley template to see the real page count. Verify the current limits on the author page.

## 2. Materials characterization — data analysis

| Technique | Analysis software |
|-----------|-------------------|
| **XRD / powder diffraction** | GSAS-II, FullProf, TOPAS, HighScore (Rietveld refinement, phase ID) |
| **TEM / STEM / electron diffraction** | Gatan DigitalMicrograph, ImageJ/Fiji, CrysTBox, py4DSTEM |
| **SEM / EDS mapping** | ImageJ/Fiji (particle statistics), vendor EDS suites (AZtec, Pathfinder) |
| **XPS** | CasaXPS, Avantage, KolXPD (peak fitting, oxidation-state assignment) |
| **XAS (XANES/EXAFS)** | Athena / Artemis (Demeter), Larch |
| **Raman / FTIR / UV-vis / PL** | vendor suites, Fityk, OriginPro (peak deconvolution) |
| **Electrochemistry** | EC-Lab, Nova, RelaxIS (impedance), custom Python for Ragone/rate analysis |
| **Tomography / 3D** | Avizo, Dragonfly, tomopy |

Report distributions and statistics (n, mean ± s.d.), not single hero images; keep instrument
models and settings in the Experimental Section, exhaustive parameters in the SI.

## 3. First-principles simulation and materials databases

### DFT / electronic structure
- **VASP** — plane-wave DFT; the de facto standard for solids (formation energies, band structure, DOS)
- **Quantum ESPRESSO** — open-source plane-wave DFT
- **GPAW / ABINIT / CP2K** — alternative DFT/AIMD codes
- **WIEN2k** — all-electron (L)APW+lo for accurate electronic structure
- **Wannier90** — maximally localized Wannier functions, tight-binding models

### Workflow, analysis, and structure tools
- **pymatgen** — Python materials-analysis library (structures, phase diagrams, defects)
- **ASE** (Atomic Simulation Environment) — build/run/analyze atomistic calculations
- **VESTA** — 3D visualization of crystal structures, charge densities, and diffraction patterns
- **phonopy** — phonon calculations and thermal properties

### Databases (for benchmarking, screening, and structure sourcing)
- **Materials Project** — computed properties for known/predicted inorganic materials
- **ICSD** (Inorganic Crystal Structure Database) — experimental crystal structures
- **AFLOW / OQMD / NOMAD** — high-throughput computed-materials repositories
- **Crystallography Open Database (COD)** — open crystal-structure data
- **CCDC / Cambridge Structural Database (CSD)** — molecular/MOF crystal structures; deposit new
  single-crystal structures with the CCDC and cite the deposition numbers in the manuscript/SI

Report the exchange-correlation functional, k-mesh, cutoff, and convergence in the SI; cite database
entries used for benchmarking.

## 4. Figures and the TOC graphic

| Tool | Use |
|------|-----|
| **OriginPro / matplotlib / plotly** | Publication plots; export vector (PDF/EPS/SVG) |
| **Adobe Illustrator / Inkscape** | Schematics, multi-panel assembly, the TOC graphic |
| **VESTA / Blender / OVITO** | Crystal-structure and atomistic renderings for schematics |
| **ImageJ/Fiji** | Micrograph scale bars, panel preparation, particle statistics |
| **BioRender** | Schematics for biomaterials / device stacks |

Figure norms: two-column-aware layout, in-image scale bars on every micrograph, color-blind-safe and
grayscale-distinguishable palettes, vector line art, high-DPI raster for images. Color is free in
Adv. Mater., but figures still count against the page budget. A designed TOC graphic + blurb is required.

## 5. Data and code availability

| Repository | Use |
|------------|-----|
| **Zenodo** | DOI-minting archive for datasets and code |
| **figshare** | Datasets, figures, supplementary files with DOIs |
| **NOMAD / Materials Cloud** | Deposit DFT inputs/outputs with a DOI |
| **GitHub / GitLab** | Code hosting; pair with a Zenodo release for a citable DOI |
| **ChemRxiv / arXiv** | Preprint posting — disclose any preprint to the editor |

Provide a concrete data-availability statement rather than "available on request"; verify the current
Wiley data policy and what must be deposited versus stated.

## 6. Writing and review aids

- **Grammarly / LanguageTool** — grammar and style (use one English variant consistently)
- **latexdiff / Word track-changes** — generate a marked-up revision for resubmission
- **Wiley Author Services** — proofs, ORCID linking, open-access ordering (verify current toolset)

## 7. Useful links (verify before relying on them)

| Resource | Purpose |
|----------|---------|
| Wiley Advanced Materials journal + author-guidelines pages | Authoritative scope, article types, limits, format, and policy |
| Wiley submission system (Research Exchange / ReX or legacy — verify) | Manuscript submission portal |
| Wiley Author Services | ORCID, proofs, open access, DEAL/transformative agreements |
| Materials Project / ICSD | Property benchmarking and structure sourcing |

## 8. Notes

1. **Verify volatile specifics** (article-type page limits, figure DPI/format, TOC-graphic spec,
   portal, APC, required declarations) on the official Wiley Advanced Materials author page — they change.
2. **Budget figures with text.** Length is counted in typeset pages; a large figure costs text.
3. **Keep the SI honest.** It is peer-reviewed; it is not a place to hide weak or contradictory data.
4. **Triangulate + benchmark.** Multi-technique proof and fair state-of-the-art comparison are expected.
5. **Reproducibility.** Archive data/code with a DOI, report full DFT/synthesis parameters, and disclose
   any preprint to the editor.

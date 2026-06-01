# External Tools & Resources for ASR-Style Sociology

Data sources, software, and packages useful when preparing an *American Sociological Review* (ASR)
submission. ASR is **methodologically broad**: quantitative stratification and demography,
comparative-historical sociology, ethnography and in-depth interviews, social-network analysis, and
computational sociology all appear in its pages. Match tools to your method. Check licenses and
current access terms before use, and verify any ASR-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by sociological subfield

### Stratification, mobility, work, family
| Source | Provider | Typical use |
|--------|----------|-------------|
| GSS (General Social Survey) | NORC | Attitudes, mobility, long-run US trends |
| PSID (Panel Study of Income Dynamics) | Michigan | Income, mobility, family dynamics |
| CPS / IPUMS-CPS | Census/IPUMS | Labor market, earnings, employment |
| NLSY | BLS | Life-course, education-to-work |
| LIS (Luxembourg Income Study) | LIS | Cross-national inequality |

### Demography & population
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS-USA / IPUMS-International | U. Minnesota | Census microdata, harmonized |
| ACS (American Community Survey) | Census | Geographic, demographic detail |
| Human Mortality / Fertility Databases | MPIDR | Formal demography |
| DHS | USAID | Global health, fertility |

### Comparative-historical, networks, computational
| Source | Provider | Typical use |
|--------|----------|-------------|
| Archives / historical records | Various | Comparative-historical sociology |
| Add Health / network surveys | UNC | Social networks |
| Digitized text, web, administrative data | Various | Computational sociology |

## 2. Software by method

### R
- Survey/regression: `survey`, `srvyr`, `fixest`, `lme4`/`brms` (multilevel), `marginaleffects`
- Demography: `demography`, `HMDHFDplus`, life-table tools
- Event history / survival: `survival`, `eha`, `coxme`
- Networks: `igraph`, `statnet`/`ergm`, `RSiena` (longitudinal networks)
- Sequence analysis (life course): `TraMineR`
- Text-as-data: `quanteda`, `stm` (structural topic models), `text2vec`
- Decomposition/inequality: `dineq`, `oaxaca`
- Reproducibility: `renv`, `targets`

### Stata
- `reghdfe`, `xtreg`/`mixed` (multilevel), `stcox`/`streg` (event history), `oaxaca`, `ineqdeco`
- `svy:` survey estimation; `coefplot`; `estout`/`esttab` for tables

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`
- Networks: `networkx`; text: `spaCy`, `scikit-learn`, `transformers`
- `matplotlib` / `seaborn`; pin with `requirements.txt`

### Qualitative & comparative-historical
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Taguette (open source) — coding interviews, fieldnotes, documents
- QCA (qualitative comparative analysis): `QCA` (R), fsQCA — set-theoretic comparative work
- Ethnographic fieldnote management and memoing workflows

## 3. Figures & exhibits
- Coefficient/marginal-effects plots, survival curves, age-period-cohort and Lexis surfaces
- Mobility tables / flow diagrams; network graphs; sequence-analysis chronograms
- Colorblind-safe palettes; grayscale-legible; vector output (PDF/EPS) — note ASR counts tables and
  figures *outside* the 15,000-word limit, but they must still be clear and self-contained

## 4. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to the **ASA Style Guide** (author-date)
- Prepare a **masked manuscript** (no title page, no identifying wording) plus a **separate title
  page** (affiliations, acknowledgments, word count, corresponding-author contact)
- **Double-spaced, Times New Roman 12-point, ≥1-inch margins**; include a **word count**
- Abstract **150-200 words** with no identifying information

## 5. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Sage Track** (ScholarOne Manuscript Central), `mc.manuscriptcentral.com/asr` |
| Owner / publisher | **American Sociological Association (ASA)** / **SAGE** |
| Review model | **Masked (anonymous)** — anonymous manuscript + separate title page |
| Article length | **Articles ≤ 15,000 words** (incl. text, references, footnotes; tables/figures excluded); **Comments/Replies ≤ 3,000** |
| Abstract | **150-200 words**, non-identifying |
| Processing fee | **$25.00 non-refundable**, via Sage Track, **waived for ASA student members** |
| Data policy | **ASA data-sharing policy** — availability after completion/major publication, with confidentiality/proprietary exemptions |

## 6. Cautions
1. **Verify volatile specifics** (editors and term, fee, caps, data policy) on the official SAGE/ASA
   pages — they change; the SAGE author page may 403 to automated tools. Unverified items are 待核实.
2. **Mask properly** — remove the title page and identifying wording, but you *may* cite your own
   work (just not in a way that names you).
3. **Match method to subfield** — ASR judges ethnography, comparative-historical work, demography,
   networks, and computational sociology on their own standards.
4. **Don't over-state ASR's data rules** — the ASA policy is availability after publication, not a
   mandatory editor-verified replication deposit; confirm the current supplementary-materials policy.
5. **Budget the $25 fee** (unless an ASA student member) and never submit elsewhere while under ASR review.

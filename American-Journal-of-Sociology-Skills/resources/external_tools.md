# External Tools & Resources for AJS-Style Sociology

Data sources, software, and packages useful when preparing an *American Journal of Sociology* (AJS)
submission. AJS is a **generalist sociology** journal with notable strength in **social theory** and
**comparative-historical** work, and it welcomes **quantitative, qualitative, ethnographic, network,
computational, and formal** scholarship across sociology and related social sciences. Match tools to
your kind of work and your evidence. Check licenses and current access terms before use, and verify
any AJS-specific policy in [`official-source-map.md`](official-source-map.md).

## 1. Data sources by tradition

### Quantitative & demographic
| Source | Provider | Typical use |
|--------|----------|-------------|
| General Social Survey (GSS) | NORC / U. Chicago | Long-run US social attitudes, stratification |
| IPUMS (USA, International, CPS) | U. Minnesota | Census/survey microdata, mobility, demography |
| PSID / NLSY | U. Michigan / BLS | Panel studies of life course, inequality |
| Add Health, NSFG, ATUS | Carolina / CDC / BLS | Networks, family, time use |
| LIS / Luxembourg Income Study | LIS | Cross-national income and inequality |

### Comparative-historical & macro
| Source | Provider | Typical use |
|--------|----------|-------------|
| V-Dem, Polity5 | Gothenburg / CSP | Regimes, states, democratization over time |
| Correlates of War, MEPV | COW / CSP | States, conflict, world-system dynamics |
| National archives / state records | Various | Process tracing, historical case work |
| Historical census & administrative series | IPUMS / national stats offices | Long-run structural change |

### Qualitative, ethnographic & network
| Source | Provider | Typical use |
|--------|----------|-------------|
| Author-collected fieldnotes, interviews | Author | Ethnography, in-depth interviews, life history |
| Archival & documentary corpora | Archives / libraries | Comparative-historical and cultural analysis |
| QDR (Qualitative Data Repository) | Syracuse | Sharing/citing qualitative data with access controls |
| Network data (egonets, complete nets) | Author / SNAP / ICPSR | Social-network and relational analysis |

## 2. Software by method

### R
- Stratification/mobility & regression: `survey`, `srvyr`, `fixest`, `lme4`/`brms` (multilevel), `marginaleffects`
- Causal inference (where designs allow): `MatchIt`, `WeightIt`, `did` (Callaway–Sant'Anna), `rdrobust`, `sensemakr`
- Event-history / demography: `survival`, `eha`, `demography`
- Networks: `igraph`, `statnet`/`ergm`, `RSiena` (longitudinal nets)
- Text-as-data & cultural analysis: `quanteda`, `stm` (structural topic models), `text2vec`; embeddings/LLM pipelines
- Sequence analysis (life course, careers): `TraMineR`
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Stata
- `reghdfe`, `csdid`, `ivreghdfe`, `margins`/`coefplot`
- `gllamm`/`meglm` (multilevel), `stcox`/`streg` (event history), `seqset` ecosystems for sequences

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`
- Text/computational: `spaCy`, `scikit-learn`, `gensim`, `transformers`/`sentence-transformers`
- Networks: `networkx`, `graph-tool`; `matplotlib`/`seaborn` for exhibits

### Qualitative & mixed-methods
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Taguette (open source) — coding interviews, documents, fieldnotes
- Comparative method: QCA (`QCApro`, `QCA` in R; fsQCA) for set-theoretic comparative analysis
- Process tracing and Bayesian narrative for comparative-historical causation

## 3. Theory, comparative-historical & ethnographic craft (AJS strengths)
- AJS rewards **theoretically ambitious** work; budget time for an explicit theoretical contribution,
  not just a finding (see `ajs-theory-building`)
- Comparative-historical: make **case selection and the comparative logic** explicit; keep a clear
  evidentiary trail from sources to claims (see `ajs-research-design`)
- Ethnography: a transparent account of access, positionality, and the link from fieldnotes to claims;
  protect informant confidentiality (see `ajs-data-and-transparency`)

## 4. Figures & exhibits
- Coefficient/forest plots (`coefplot`, `ggplot2`/`broom`), event-study and survival plots,
  marginal-effects and predicted-probability plots (`marginaleffects`)
- Network diagrams where relational structure is the point; maps (`sf`, `tmap`) for spatial variation
- Sequence-index and tempograms for life-course work
- Colorblind-safe palettes, legible in grayscale; **alt text required for every figure at submission**;
  vector output (PDF/EPS) for print (see `ajs-tables-figures`)

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to **AJS's own author-date house
  style** (documented in the AJS Manuscript Preparation pages and Formatting PDF), **not** the ASA
  Style Guide; an AJS CSL style exists for Zotero/Mendeley (verify it matches the current house style)
- Typesetting: **Editorial Manager accepts Word, PDF, and LaTeX**; serif typeface (e.g., Times Roman)
  ≥11 pt (preferably 12), double-spaced, ≥1-inch margins
- Prepare the manuscript **without identifying information**; submit a **separate cover page**;
  include a **brief originality statement** if the paper overlaps prior work

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Manager** (`editorialmanager.com/ucp-ajs`) — confirm current URL |
| Owner / publisher | **University of Chicago** (Dept. of Sociology) / **University of Chicago Press** (NOT SAGE/ASA) |
| Review model | **Double-blind**; AJS will not knowingly use reviewers in the author's network |
| Editorial structure | Student-run **Manuscript Assignment Board** (Assistant Editors under grad-student Associate Editors); editorial board = entire Chicago sociology faculty |
| Submission fee | **$30**; waived for **sole-author graduate students** (proof may be requested) — verify |
| Abstract | **~150 words**; required (no abstract → not sent to reviewers) |
| Length | **No fixed word limit**; be concise (referees may need more time over ~18,000 words) — verify |
| Distinctive features | **Comment-and-Reply** tradition; substantial **book-review** section; **Roger V. Gould Prize** |

## 7. Cautions
1. **Verify volatile specifics** (current editor, fee/waiver, length and abstract expectations,
   citation-style details, any data policy) on the official UChicago Press AJS pages immediately before
   submission; the source map records the official route for each item, but operational details change.
2. **Use AJS's house style, not the ASA Style Guide** — this is a key contrast with ASA journals
   (e.g., ASR). Confirm the current reference forms against the live prep pages / Formatting PDF.
3. **Prepare for double-blind review** — no identifying information in the manuscript, a separate
   cover page, and carefully worded self-references.
4. **Do not over-state transparency requirements** — AJS does not advertise a mandatory,
   editor-verified replication package; document your work well, but verify the current policy.
5. **Be theoretically ambitious** — AJS prizes a portable theoretical contribution; a bare result is
   rarely enough (see `ajs-theory-building`).

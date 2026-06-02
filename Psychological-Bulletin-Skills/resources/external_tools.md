# External Tools & Resources for Psychological Bulletin-Style Research Synthesis

Tools, software, and standards useful when preparing a *Psychological Bulletin* submission.
Psychological Bulletin publishes **research syntheses** — **systematic reviews, meta-analyses,
meta-reviews/meta-synthesis, and rigorous qualitative reviews** — **not** original primary studies.
So the toolchain is built around the **synthesis lifecycle**: protocol registration, systematic
searching, screening and coding, effect-size computation, random-effects modeling, moderator and
publication-bias analysis, and MARS/PRISMA/JARS-compliant reporting. Check licenses and current
access terms before use, and verify any Psychological Bulletin-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Reporting standards & protocol registration

| Standard / venue | Provider | Use |
|------------------|----------|-----|
| **MARS** (Meta-Analysis Reporting Standards) | APA Style / JARS | Required items for reporting a meta-analysis |
| **PRISMA 2020** (statement + checklist + flow diagram) | PRISMA | Required for systematic reviews; the records-flow diagram |
| **JARS** (Journal Article Reporting Standards) | APA Style | Quantitative / mixed-methods reporting structure |
| **PRISMA extensions** (PRISMA-S search, PRISMA-P protocol, PRISMA-NMA) | PRISMA | Search reporting; protocol; network meta-analysis |
| **PROSPERO** | CRD, University of York | Prospective registration of the review protocol |
| **OSF Registries** | Center for Open Science | Preregister protocol/analysis plan; deposit materials |
| **TOP Guidelines** | Center for Open Science | Transparency/openness levels APA journals adopt |

## 2. Systematic search & screening

- **Databases:** APA **PsycINFO** / PsycNET, **MEDLINE/PubMed**, **Web of Science**, **Scopus**,
  **ERIC**, **EMBASE**, **ProQuest Dissertations & Theses** (grey literature) — search at least the
  core multidisciplinary + psychology databases and document each.
- **Grey literature & registries:** Google Scholar (supplementary), conference programs,
  preprint servers (PsyArXiv), trial/registry records, contacting authors for unpublished data.
- **Search building:** controlled vocabulary (MeSH / APA Thesaurus) + free-text; record the **exact
  string, database, date, and hit count per source** (PRISMA-S); deduplicate and log it.
- **Screening managers:** **Covidence**, **Rayyan**, **DistillerSR**, **EPPI-Reviewer**, or
  **abstractr** — title/abstract then full-text screening with two screeners and a reconciliation log.
- **Citation/reference managers:** **Zotero**, **EndNote**, **Mendeley** for dedup and PRISMA counts.

## 3. Coding & inter-rater reliability

- **Double-coding** of effect sizes and moderators by ≥ 2 trained coders; a **codebook** with
  explicit decision rules; a reconciliation procedure for disagreements.
- **Reliability:** Cohen's / Fleiss' **kappa** for categorical codes, **ICC** for continuous codes;
  report the statistic and the resolution process (`irr`, `psych` in R).

## 4. Effect sizes, meta-analytic models & diagnostics

### R (dominant for psychological meta-analysis)
- **`metafor`** — the workhorse: random/mixed-effects models, meta-regression, `escalc()` for
  effect-size computation (SMD/Hedges' g, log OR/RR, r → z), forest/funnel plots, influence diagnostics
- **`robumeta` / `clubSandwich`** — **robust variance estimation (RVE)** for dependent effect sizes
- **`metafor` rma.mv` + `clubSandwich`** — **multilevel / three-level** meta-analysis
- **`dmetar`** — companion functions, PET-PEESE, GOSH plots
- **`puniform`, `weightr`, `metasens`** — p-uniform, **selection models**, sensitivity to bias
- **`p-curve`** (p-curve.com app or scripts) — evidential value / p-hacking diagnostics
- **`netmeta` / `gemtc`** — network (multiple-treatments) meta-analysis

### Other software
- **Stata:** `meta` suite (`meta set`, `meta summarize`, `meta forestplot`, `meta regress`,
  `meta funnelplot`, `meta bias`, `meta trimfill`)
- **Comprehensive Meta-Analysis (CMA)** — point-and-click meta-analysis
- **Python:** `PythonMeta`, `statsmodels`; **JASP** / **jamovi** (MAJOR module) for GUI workflows
- **RevMan** (Cochrane) — common in health-adjacent syntheses

### Diagnostics to run
- **Heterogeneity:** Q test, **I²**, **τ²** with a prediction interval
- **Publication bias:** **funnel plot**, **Egger's regression**, **trim-and-fill**, **PET-PEESE**,
  **p-curve / p-uniform**, **3-parameter selection models**; sensitivity / leave-one-out
- **Robustness:** RVE, influence/outlier diagnostics, alternative effect-size metrics

## 5. Figures & exhibits Psychological Bulletin expects
- **PRISMA flow diagram** (records identified → screened → eligible → included, with exclusion reasons)
- **Forest plots** (study effects, weights, pooled estimate + CI and prediction interval)
- **Funnel plots** (with contour enhancement) and bias-diagnostic plots
- Moderator / meta-regression bubble plots; colorblind-safe palettes; vector output (PDF/EPS)

## 6. Writing, references & transparency package
- Format to **APA 7th edition**; **abstract ≤ 250 words**; reference managers (Zotero/BibTeX/EndNote)
- Prepare a **masked** manuscript (no author clues; neutralize self-citations) plus a separate title page
- Deposit the **database, codebook, and analysis scripts** to a trusted repository (OSF / institutional)
  with a persistent identifier; state availability per the journal's transparency policy

## 7. Cautions
1. **It is a synthesis, not a study.** Psychological Bulletin does not publish original primary data
   (those go elsewhere; original theory to *Psychological Review*). Build a review, not an experiment.
2. **Search must be systematic and reproducible.** Document every database, string, date, and count
   (PRISMA-S); another team should be able to re-run it.
3. **Model dependent effect sizes correctly.** Multiple effects per study need RVE or multilevel
   models, not naive independence.
4. **Probe publication bias seriously.** Run several complementary diagnostics; no single test settles it.
5. **Verify volatile specifics** (TOP level, abstract/length, accepted types, fee/APC) on the official
   APA page — they change; unverified items are marked 待核实.

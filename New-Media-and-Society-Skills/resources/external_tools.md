# External Tools & Resources for NM&S-Style Digital-Media Research

Data sources, software, and packages useful when preparing a *New Media & Society* (NM&S) submission.
NM&S is **methodologically pluralist**: qualitative interviews and digital ethnography, critical and
theoretical work, content and discourse analysis, computational methods, and mixed methods all appear.
Match tools to your method. Check licenses, platform **terms of service**, and current access terms
before use, and verify any NM&S-specific policy in [`official-source-map.md`](official-source-map.md).

## 1. Data sources by area

### Social media & platform data (mind ToS and ethics)
| Source | Provider | Typical use |
|--------|----------|-------------|
| Platform research APIs (e.g. official academic/researcher APIs) | Platforms | Posts, networks, metadata — within ToS |
| CrowdTangle-style / archived public datasets | Various archives | Historical public posts (where redistributable) |
| Web Archive / Wayback Machine | Internet Archive | Interface change, longitudinal capture |
| App stores, transparency reports, policy docs | Platforms/regulators | Governance, datafication, business models |

### Digital inequality, internet use, society
| Source | Provider | Typical use |
|--------|----------|-------------|
| Pew Research Center datasets | Pew | Internet/technology adoption, attitudes |
| World Internet Project / national digital surveys | Various | Cross-national digital divide |
| ITU / OECD ICT indicators | ITU / OECD | Access, infrastructure, international comparison |
| Eurobarometer / national statistical agencies | EU / states | Attitudes to platforms, privacy, AI |

### Qualitative & critical materials
| Source | Provider | Typical use |
|--------|----------|-------------|
| Interview corpora (own fieldwork) | Researcher | Digital ethnography, in-depth interviews |
| Platform interfaces / screenshots (anonymized) | Researcher | Walkthrough method, interface analysis |
| Policy, ToS, and corporate documents | Platforms/regulators | Critical / political-economy analysis |

## 2. Software by method

### Qualitative (CAQDAS) — interviews, fieldnotes, documents
- NVivo, ATLAS.ti, MAXQDA, Taguette (open source), Dedoose — coding, memoing, retrieval
- Reflexive thematic-analysis and grounded-theory workflows; positionality memo templates

### Content & discourse analysis
- Intercoder reliability: `irr` / `tidycomm` (R), Krippendorff's alpha calculators, ReCal
- Quantitative content analysis: spreadsheet codebooks + reliability; corpus tools
- Discourse/CDA: concordancers (AntConc), qualitative coding for interpretive analysis

### Computational social science / text-as-data / networks
- Python: `pandas`, `numpy`, `scikit-learn`, `spaCy`, `transformers` / Hugging Face, `gensim` (topic models)
- R: `quanteda`, `stm` (structural topic models), `text2vec`, `tidytext`
- Networks: `networkx` / `igraph`, `statnet`/`ergm`; visualization with Gephi
- Scraping/collection (within ToS): official APIs first; document collection window and method
- Validation: always benchmark automated measures against human-labeled samples (precision/recall/F1)

### Statistics (for the quantitative/computational strand)
- R: `fixest`, `lme4`/`brms`, `marginaleffects`, `survey`; Python: `statsmodels`, `linearmodels`
- Pin versions (`renv`, `requirements.txt`) and set seeds for reproducibility

## 3. Figures & exhibits
- Quote-to-claim tables and coding-scheme tables (qualitative exhibits do real analytic work)
- Network graphs (annotated, legible), topic-model/feature plots with uncertainty
- Annotated, **anonymized** platform screenshots (crop/blur identifying detail)
- Colorblind-safe palettes; grayscale-legible; vector output — remember **exhibits count toward the
  8,000-word target**

## 4. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to **SAGE Harvard** (author-date)
- Prepare a **masked manuscript** (no identifying names/affiliations/phrasing) + a **separate title page**
- **Unstructured abstract 150 words**; **≥4 keywords**; include a word count

## 5. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Sage Track**, `mc.manuscriptcentral.com/nms` |
| Publisher | **SAGE** (since 1999; ISSN 1461-4448 / 1461-7315) |
| Review model | **Anonymized workflow** — masked manuscript + separate title page |
| Length | **8,000-word target** — all text incl. notes, references, tables, and charts |
| Abstract / keywords | **150 words**, unstructured; **≥4 keywords** |
| Referencing | **SAGE Harvard** (author-date) |
| Ethics | **SAGE/COPE** + **ICMJE**; data availability statement; online/platform-data ethics (consent, anonymization, ToS) |

## 6. Cautions
1. **Verify volatile specifics** (editor transition, optional open-access fee, and Sage Track prompts)
   on the official SAGE/NM&S pages before upload or acceptance.
2. **Respect platform ToS and ethics** — "publicly available" is not consent; paraphrase verbatim quotes
   to resist reverse-search, strip handles, blur screenshots, and document API/scraping method.
3. **Validate computational measures** against human labels before treating output as a finding.
4. **Match method to standard** — NM&S judges ethnography, discourse, content, and computational work on
   their own terms; don't import one tradition's bar onto another.
5. **Budget the word target carefully** — references and tables count toward 8,000 words; a few hundred
   over may mean no review.

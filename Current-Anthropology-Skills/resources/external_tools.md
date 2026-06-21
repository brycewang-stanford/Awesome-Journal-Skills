# External Tools & Resources for CA-Style Anthropology

Data sources, archives, software, and packages useful when preparing a *Current Anthropology* (CA)
submission. CA is the transnational, **all-subfields** journal: a submission may be ethnographic,
archival/historical, material/archaeological, biological/physical, linguistic, or applied. Match tools to
your subfield and design. Check licenses, ethics, and current access terms before use, and verify any
CA-specific policy in [`official-source-map.md`](official-source-map.md). Remember that **ethics
constraints override convenience** — see
[`../skills/curranthro-transparency-and-data`](../skills/curranthro-transparency-and-data/SKILL.md) — and
that a **Major Article will be debated in public** under the CA✩ Treatment, so document your evidence
trail accordingly.

## 1. Data, archives & primary sources by subfield

### Sociocultural / applied
| Source | Provider | Typical use |
|--------|----------|-------------|
| Author-collected fieldnotes, interviews, media | Researcher | Participant observation, ethnographic evidence |
| QDR (Qualitative Data Repository) | Syracuse | Sharing/citing qualitative data with **access controls** |
| HRAF / eHRAF World Cultures | Yale | Cross-cultural comparison, ethnographic database |
| National & community archives | Various | Historical and policy context; read with their silences |

### Archaeology
| Source | Provider | Typical use |
|--------|----------|-------------|
| tDAR (the Digital Archaeological Record) | Digital Antiquity | Site data, reports, datasets (mind heritage/community controls) |
| Open Context | Alexandria Archive | Published, citable archaeological datasets |
| Radiocarbon databases (e.g., IntCal calibration) | Various | Dating, chronology building |
| GIS basemaps / DEMs (e.g., national surveys) | Various | Site mapping, spatial distribution |

### Biological / physical anthropology
| Source | Provider | Typical use |
|--------|----------|-------------|
| GenBank / ENA | NCBI / EBI | Genetic sequence data (consent & group-harm caveats) |
| Curated skeletal/osteological collections | Museums/institutions | Morphometrics (NAGPRA/repatriation obligations apply) |
| Published comparative measurement datasets | Various | Human variation, growth, paleopathology |

### Linguistic anthropology
| Source | Provider | Typical use |
|--------|----------|-------------|
| Author-collected recordings & transcripts | Researcher | Discourse, interaction, language ideology |
| ELAR / PARADISEC / AILLA | Endangered-language archives | Documentation corpora (community access protocols) |
| ELAN | MPI Nijmegen | Time-aligned multimedia transcription/annotation |

## 2. Software by method

### Qualitative analysis (CAQDAS)
- NVivo, ATLAS.ti, MAXQDA, Dedoose — coding interviews, fieldnotes, documents
- Taguette (open source) — lightweight qualitative coding
- ELAN / FLEx / Praat — linguistic transcription, glossing, and acoustic analysis

### Archaeology / spatial
- QGIS, GRASS GIS, ArcGIS — site mapping, spatial analysis
- R (`sf`, `terra`), Python (`geopandas`) — spatial data; `rcarbon`/OxCal for radiocarbon

### Biological / quantitative subfields
- R (`geomorph` for geometric morphometrics; `vegan`; standard stats), Python (`pandas`, `numpy`, `statsmodels`, `scikit-learn`)
- Report effect sizes + uncertainty; pin versions (`renv` / `requirements.txt`); set seeds (see the
  shared reporting-standards reference linked from [`README.md`](README.md), background only)

## 3. Ethics, consent & accountability tooling
- Consent forms and protocols per IRB/ethics board and **community agreements**; ongoing-consent practices
- Anonymization: pseudonymization, redaction, and composite/masked detail strategies; data-minimization
  for vulnerable/criminalized communities
- Heritage & repatriation: NAGPRA documentation, descendant-community consultation records,
  CARE Principles for Indigenous Data Governance (alongside FAIR where appropriate)
- Image/media consent and rights tracking; withhold sacred/heritage imagery where required
- **Wenner-Gren copyright assignment:** confirm you hold the rights to all included materials before
  assigning copyright (see [`official-source-map.md`](official-source-map.md))

## 4. Figures, media & exhibits (CA file rules)
- Maps (QGIS, `sf`/`tmap`), site plans, stratigraphic and artifact drawings (Inkscape, Illustrator)
- Export figures as **TIFF (`.tif`) or EPS (`.eps`)** files — CA wants figures **separate** from the
  `.doc`/`.rtf` text file, not embedded in a PDF
- Photograph handling with consent metadata; alt text / image descriptions; grayscale-legible encoding
- Interlinear glossed transcripts (LaTeX `gb4e`/`expex`); discourse transcript conventions
- Respect figure/table caps: **12** (Major Article) / **4** (Report)

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — final files use **Chicago Manual of Style
  author-date**, references **alphabetized** and **not embedded in endnotes**; **free-format** is accepted
  at first submission; include **DOIs**
- Typesetting: Word or LaTeX (TeX Live / MacTeX, Overleaf); CA wants the text + tables as a single
  **`.doc`/`.rtf`** file (not PDF)
- Include the **≤ 200-word abstract**; keep jargon minimal so nonspecialists across subfields can follow

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Manager** |
| Publisher / sponsor | **University of Chicago Press** for the **Wenner-Gren Foundation** |
| Signature process | **CA✩ Treatment** — published signed Comments + author's Reply (Major Articles only) |
| Article types | Major Article (6,000–10,000) · Report (3,000–5,000) · Forum · Discussion/Comment (≤ 800) · Current Applications |
| Abstract | **≤ 200 words** (Major Article and Report) |
| Copyright | Assignment to the **Wenner-Gren Foundation** for major articles, reports, forums, discussion items, commentaries |
| Founded / ISSN | 1959 (Sol Tax); ISSN 0011-3204 (print) / 1537-5382 (web) |

## 7. Cautions
1. **Verify volatile specifics** (editors, portal prompts, caps, copyright/data wording, acceptance
   figures) on the official CA / UChicago Press / Wenner-Gren pages and Editorial Manager.
2. **Build for the CA✩ Treatment** — a Major Article will be commented on in print; document evidence and
   pre-engage likely commentators.
3. **Ethics first** — consent, anonymization, and heritage/repatriation obligations override data-sharing
   convenience; protecting people can mean not sharing.
4. **Match method to subfield** — CA judges ethnographic, material, biological, and linguistic work on its
   own terms; do not force a single template.
5. **Write for all subfields** — minimize jargon; keep main ideas legible to nonspecialists worldwide.

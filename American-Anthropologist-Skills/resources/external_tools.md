# External Tools & Resources for AA-Style Anthropology

Data sources, archives, software, and packages useful when preparing an *American Anthropologist* (AA)
submission. AA is the **four-field flagship**: a submission may be ethnographic, archival/historical,
material/archaeological, biological/physical, linguistic, multimodal, or reflexive/public. Match tools
to your subfield and design. Check licenses, ethics, and current access terms before use, and verify any
AA-specific policy in [`official-source-map.md`](official-source-map.md). Remember that **ethics
constraints override convenience** — see
[`../skills/amanthro-transparency-and-data`](../skills/amanthro-transparency-and-data/SKILL.md).

## 1. Data, archives & primary sources by subfield

### Sociocultural / reflexive / public
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

## 4. Figures, media & exhibits
- Maps (QGIS, `sf`/`tmap`), site plans, stratigraphic and artifact drawings (Inkscape, Illustrator)
- Photograph handling with consent metadata; **alt text** for all figures; grayscale-legible encoding
- Interlinear glossed transcripts (LaTeX `gb4e`/`expex`); discourse transcript conventions
- Multimodal: video/audio editing and hosting that preserves consent and access controls

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to **Chicago Manual of Style
  author-date**; AA accepts **free-format** at first submission but keep one consistent style and
  include **DOIs**
- Typesetting: Word or LaTeX (TeX Live / MacTeX, Overleaf); prepare an **anonymized** manuscript
  (no identifying metadata, anonymized **file name**, no obvious self-references) plus a separate title page
- Include the **200-word abstract**; ORCID is required for AAA journals

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Research Exchange** for new manuscripts since 15 Apr 2025 |
| Owner / publisher | **AAA** / **Wiley** |
| Review model | **Anonymous** — anonymize the manuscript and **file name**; ethics of care |
| Sections | Research Articles · Vital Topics Forums · World / Public / Multimodal Anthropologies · Essays · Commentaries · Interviews · Review Essays · Book Reviews |
| Length | Research Articles **≤ 8,000 words** (extendable ~10,500 on acceptance); abstract **200 words** |
| Fee | **None** for submission/publication; OnlineOpen APC **USD 3,570** if choosing open access |
| Ethics & data | AAA *Principles of Professional Responsibility*; Wiley ACT lists no AA-specific data-sharing tier; consent/heritage central |

## 7. Cautions
1. **Verify volatile specifics** (editors, portal prompts, APC, section availability, production-file
   details) on the official AA / Wiley pages and Research Exchange.
2. **Ethics first** — consent, anonymization, and heritage/repatriation obligations override data-sharing
   convenience; protecting people can mean not sharing.
3. **Match method to subfield** — AA judges ethnographic, material, biological, and linguistic work on
   its own terms; do not force a single template.
4. **Anonymize properly** — AA is anonymous; strip author metadata, anonymize the file name, neutralize
   self-references.
5. **Write for four fields** — an AA paper must speak past its subfield to all of anthropology.

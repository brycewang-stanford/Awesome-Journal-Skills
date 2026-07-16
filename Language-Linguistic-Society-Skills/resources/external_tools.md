# External Tools & Resources for Language (LSA) Submissions

Data sources, software, and packages useful when preparing a submission to *Language*, the flagship
journal of the Linguistic Society of America. *Language* spans **every subfield** — phonology,
phonetics, syntax, semantics, morphology, historical and typological linguistics, sociolinguistics,
psycholinguistics, and computational linguistics — so match tools to your subfield and your evidence.
Check licenses and current access terms before use, and verify any *Language*-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by subfield

### Corpora & databases
| Source | Provider | Typical use |
|--------|----------|-------------|
| CHILDES / TalkBank | Carnegie Mellon | Child language acquisition, conversation |
| BNC / COCA / COHA | Oxford / English-Corpora.org | English usage, frequency, diachrony |
| Buckeye, Switchboard, TIMIT | OSU / LDC | Conversational phonetics, ASR-adjacent work |
| Universal Dependencies / Penn Treebank | UD / LDC | Syntactic annotation, parsing, typology |
| WALS, Grambank, Glottolog | MPI-EVA | Typological features, genealogy, areal control |
| PHOIBLE | MPI / self-hosted | Cross-linguistic phoneme inventories |
| ELAR / PARADISEC / AILLA / TLA | archives | Documented endangered-language corpora |

### Elicited & experimental
| Source | Provider | Typical use |
|--------|----------|-------------|
| Author-collected elicitation / fieldwork | Author | Grammaticality/acceptability judgments, paradigms |
| PCIbex / Ibex / Gorilla | community / Gorilla | Web-based acceptability and processing experiments |
| Prolific / MTurk | Prolific / Amazon | Participant recruitment for rating and reaction-time tasks |

## 2. Software by method

### Phonetics & speech
- **Praat** — measurement, annotation, scripting (formants, pitch, duration)
- **Montreal Forced Aligner (MFA)** — forced alignment of audio to transcripts
- **ELAN** — time-aligned multimodal annotation; **FLEx** / **Toolbox** — interlinearization and lexica

### Statistics (R first)
- `lme4` / `lmerTest` (mixed-effects models), `brms` / `rstanarm` (Bayesian mixed models)
- `emmeans` / `marginaleffects` (predictions, contrasts), `ordinal` (ordinal ratings)
- `phonR`, `vowels` (vowel normalization), `gamm`/`mgcv` (dynamic phonetics)
- Reproducibility: `renv` (pin versions), `targets` (pipelines), R Markdown / Quarto

### Corpus & computational
- Python: `spaCy`, `stanza`, `nltk`, `pandas`, `scikit-learn`, `transformers`
- Concordancing: AntConc, `quanteda` (R); regex/CQL over annotated corpora

### Formal analysis
- Syntax trees: `tikz-qtree`, `forest` (LaTeX), phpSyntaxTree
- OT: OTSoft, Praat's OT learner; Autosegmental/metrical diagrams in TikZ
- Semantics: Lambda Calculator, transparent type-driven derivations

## 3. Glossing, IPA & example formatting
- **Leipzig Glossing Rules** — the standard for interlinear morpheme-by-morpheme glosses
- **IPA** — use a Unicode IPA font (Doulos SIL, Charis SIL, Gentium); never fake symbols
- LaTeX: `gb4e` / `expex` / `linguex` (numbered examples + glosses), `leipzig` (gloss abbreviations),
  `tipa`/Unicode for IPA — the **Overleaf template** for *Language* wires these up
- Language codes: **ISO 639-3** and Glottocodes for identifying varieties

## 4. Figures & exhibits
- `ggplot2` (partial-effects, by-speaker variation, vowel plots), colorblind-safe palettes
- Spectrograms and pitch tracks from Praat; export vector (PDF/EPS) for print
- **Alt text / descriptive captions** for every figure (see `lang-tables-figures`)

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX — format to the **Language Style Sheet / Unified Style
  Sheet for Linguistics** (author-date), **not** APA or Chicago; a Unified Style Sheet CSL exists for
  Zotero (verify it matches the current house style)
- Typesetting: the journal's **Overleaf/CUP template**; LaTeX (`gb4e`/`expex`) or Word workflows

## 6. Process & portal
| Item | Note |
|------|------|
| Publisher | **Cambridge University Press** (since Jan 2026; previously Project MUSE / JHU Press) |
| Portal | **CUP ScholarOne**; Overleaf template available — confirm current URL |
| Access | **Fully open access from Volume 102 (2026)** — check APC / waiver / read-and-publish |
| Review | **Double-anonymous** |
| Editors | Shelome Gooden & Michael Putnam — verify the live masthead |
| Sections | General Research Article (≤18,000 words, inclusive), Research Report, Review Article (≤5,000), Discussion Notes, Reviews; online-only: Perspectives, Phonological Analysis, Language & Public Policy, Teaching Linguistics |
| Contact | language@lsadc.org |

## 7. Cautions
1. **Verify volatile specifics** (word/abstract limits, accepted formats, open-access terms, current
   masthead, data policy) on the live CUP/LSA pages before submission; the source map records the route
   for each, but operational details change.
2. **Use the Language / Unified Style Sheet**, not APA or Chicago — a key contrast with many venues.
3. **Prepare for double-anonymous review** — no identifying information; neutralize self-citations.
4. **Gloss to Leipzig conventions and use real IPA** — misaligned glosses and faked symbols are the most
   common example errors.
5. **Model clustered data properly** — mixed-effects in R; avoid pseudoreplication (see
   `lang-data-analysis`).
6. **Respect data ethics** — consultant/community consent governs what may be shared; open is not always
   ethical (see `lang-data-and-transparency`).

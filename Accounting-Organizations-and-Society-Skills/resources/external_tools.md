# Research Tools & Resources (AOS)

External data sources, software, and writing tools for preparing a manuscript for
**Accounting, Organizations and Society (AOS)**. Because AOS is methodologically
plural — qualitative field studies, behavioral experiments, surveys, historical work,
and theory-carrying archival designs — the toolkit spans several research
traditions; use the section matching yours. Verify licensing and current Elsevier/AOS
policies before relying on any resource (see `official-source-map.md`, checked
2026-07-16).

## 1. Qualitative field & historical research

### Data collection
| Tool / source | Use |
|---------------|-----|
| Recorded interviews + secure transcription (e.g., institution-approved services) | Interview corpus; check consent covers recording and quotation |
| Field notebooks / observation protocols | Meetings, routines, artifacts in use |
| Internal documents (budgets, board packs, risk registers) | Triangulation; negotiate access and anonymization terms in writing |
| Corporate & regulatory archives, national archives, professional-body records | Historical/genealogical studies; note custodians and gaps |

### Analysis
- **NVivo**, **ATLAS.ti**, **MAXQDA**, **Dedoose** — coding and retrieval; keep the codebook versioned and export an audit trail.
- A plain **claim → evidence register** (spreadsheet) linking every conceptual claim to interview/observation/document IDs — the artifact reviewers implicitly ask for.
- Timeline tools for process/change studies.

## 2. Experimental / behavioral research

| Tool | Use |
|------|-----|
| Qualtrics | Instrument construction and delivery |
| Prolific / CloudResearch / MTurk | Online pools — justify fit; professional tasks usually need professional participants |
| Professional panels (audit firms, alumni networks, executive programs) | Auditor/manager/analyst participants |
| oTree / z-Tree | Interactive and market experiments |
| AsPredicted / OSF Registries | Pre-registration |
| G*Power, R `pwr` / `simr` | Power analysis (especially for interactions) |

Analysis: ANOVA/ANCOVA with planned contrasts; mediation/moderation via **PROCESS**
(Hayes), R `mediation` / `lavaan` with bootstrap CIs; report effect sizes and per-cell
descriptives.

## 3. Survey research

- Validated instruments from prior accounting/management studies where possible; document adaptation.
- R `psych` / `lavaan` or Mplus for reliability, CFA, and method-bias diagnostics.
- Sampling-frame and response-rate bookkeeping from day one.

## 4. Archival-with-theory strands

- **Stata**: `reghdfe`, `csdid`/`did`, `ivreg2`, `winsor2`; **R**: `fixest`, `did`; **Python**: `pandas`, `linearmodels`.
- Data: Compustat/CRSP via WRDS where the institutional question needs firm panels; regulatory filings (EDGAR), press archives (Factiva/Nexis) for institutional events.
- The vendored [`code/`](code/) skeleton (Stata + Python causal chain) serves this strand — adapt, don't run blind.

## 5. Reference & writing tools

| Tool | Note |
|------|------|
| Zotero / EndNote | Set an author–date style; reconcile against the current AOS Guide for Authors |
| Word / LaTeX | Editorial Manager accepts standard source files and builds the review PDF |
| Grammarly and similar | Language help permitted; generative-AI writing assistance must be declared per Elsevier policy |

## 6. Submission & process

- **Portal:** Editorial Manager at editorialmanager.com/AOS (fully online).
- **Files:** anonymized manuscript + separate identified title page + competing-interests declaration; see `../skills/aos-submission/templates/checklist.md`.
- **Review:** double-anonymized; scrub metadata and self-identifying phrasing.
- **Open access:** optional (hybrid); APC personalized at submission — confirm there.

## 7. Transparency without breaching consent

AOS work often rests on confidential field material. The standard is honest
disclosure, not forced sharing: describe the corpus precisely (data-inventory table),
state what consent and site-anonymity agreements restrict, share instruments and
quantitative code where possible, and retain the underlying materials and analysis
trail for the project's life. Never let anonymization promises erode into vagueness
about how much data exists.

## 8. Verify before you rely

Editors, portal behavior, article types, artwork specs, OA pricing, and declaration
requirements change. Confirm each on the official ScienceDirect Guide for Authors and
in Editorial Manager before submitting.

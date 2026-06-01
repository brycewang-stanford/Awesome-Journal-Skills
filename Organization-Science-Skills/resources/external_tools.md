# Organization-Research Tools & Resources (Organization Science)

This document lists data sources, analysis software, and writing tools commonly used
when preparing a manuscript for **Organization Science** (published by INFORMS).
Because the journal is methodologically eclectic — with a signature strength in
qualitative and inductive work alongside quantitative, experimental, computational, and
formal-analytical research — and spans **micro (individual/team) to macro
(organizational/field/population)** levels, the toolkit is unusually broad. Choose tools
that fit the level of analysis and the theoretical contribution, not the other way around.
Always verify licensing terms and current Organization Science / INFORMS policies before
relying on any resource.

## 1. Data Sources

### Macro: organizational, field, and population level
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat / CRSP | S&P Global / CRSP | Firm financials, performance, survival |
| BoardEx / Execucomp | Management Diagnostics / S&P | Boards, executives, intra-org networks |
| USPTO / PatentsView | US Patent & Trademark Office | Innovation, recombination, knowledge flows |
| SDC Platinum (Refinitiv) | LSEG | Alliances, M&A, founding events |
| Orbis / Amadeus | Bureau van Dijk | Global organizational forms, populations |
| GuideStar / IRS 990 | Candid | Nonprofit forms, fields, ecology |

### Meso / micro: individual, team, and intra-organizational
| Source | Provider | Typical use |
|--------|----------|-------------|
| Prolific / CloudResearch / Qualtrics | Various | Surveys, vignette and online experiments |
| O*NET | US Dept. of Labor | Occupations, task structures, roles |
| LinkedIn / Revelio Labs | Various | Mobility, careers, hiring, team composition |
| Internal archival traces (email, Slack, Git, ticketing) | Field site | Collaboration, communication, coordination |

### Qualitative, process, and field data (a journal signature)
| Source | Use |
|--------|-----|
| Field interviews, observation, ethnography | Inductive theory building; process and identity work |
| Organizational archives, internal documents | Longitudinal process tracing |
| News / press archives (Factiva, LexisNexis, ProQuest) | Events, narratives, field-level change |
| Glassdoor / job postings / online communities | Culture, sensemaking, emergent forms |

## 2. Analysis Software & Packages

### Qualitative & inductive theory building (emphasize given the venue)
- **NVivo**, **ATLAS.ti**, **Dedoose**, **MAXQDA** — coding, retrieval, audit trails.
- Templates for **Gioia** data structures (first-order codes → second-order themes → aggregate dimensions), **grounded-theory** memoing, and process-model diagrams.
- **QCA** (fs/QCA, R `QCApro`, `SetMethods`) for configurational set-theoretic comparison.

### Computational & formal-analytical modeling
- **Agent-based / simulation**: NetLogo, Repast, Mesa (Python), R; for organizational-learning and adaptation models (e.g., NK landscapes, March-style exploration/exploitation).
- **Formal / analytical modeling**: Mathematica, MATLAB, SymPy; game-theoretic and economics-of-organization models.
- **Network analysis**: R `igraph` / `statnet` / `ergm`, Python `networkx`, Pajek, UCINET, Gephi (intra-org, interfirm, and field networks).
- **Text as data / NLP**: Python `spaCy`/`gensim`, R `quanteda`/`stm`, topic models and embeddings for culture, identity, and sensemaking.

### Quantitative & experimental
- **Multilevel / HLM** (micro-in-macro nesting): R `lme4`/`lmerTest`/`nlme`, Stata `mixed`/`melogit`, Mplus, HLM software; report ICC(1)/ICC(2)/r_wg before aggregation.
- **SEM / measurement**: Mplus, R `lavaan`/`semTools`, Stata `sem`/`gsem`.
- **Panel / event-history**: Stata `xtreg`/`reghdfe`/`stcox`/`streg`, R `fixest`/`survival` (organizational ecology, founding/failure).
- **Experiments**: G*Power / R `pwr`/`simr` for design and power; OSF Registries / AsPredicted for pre-registration.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| Zotero | Free; configure to an INFORMS author-date output style |
| EndNote | Broad journal-style support |
| Overleaf / LaTeX | Optional; verify the ScholarOne portal accepts the format |
| Grammarly | Language polish |

Organization Science uses an **INFORMS author-date** house style (author last name + year
in text; alphabetical reference list). Configure your reference manager to an author-date
style and reconcile against the current INFORMS / Organization Science guidelines.

## 4. Submission & Process

- **Submission portal**: ScholarOne Manuscripts at mc.manuscriptcentral.com/orsc (verify the current link).
- **ORCID**: required for the submitting author.
- **Contribution statement**: prepare the mandatory <500-word contribution statement for the cover letter (required since June 1, 2023).
- **Anonymization**: the main manuscript and the separate standalone appendix must be fully anonymized for double-anonymous review.

## 5. Reproducibility & Transparency

1. Keep clean, commented scripts (do-files, R scripts, simulation code, Mplus inputs) that regenerate every table, figure, and reported simulation result.
2. Document data sources, sample-construction steps, coding schemes, and exclusion rules; for qualitative work, maintain an audit trail and representative-quotation table.
3. Provide enough methodological detail and references to **permit replication**; be prepared to provide raw data for editorial review on request and to retain data for a reasonable time after publication.
4. Note: Organization Science currently applies a replicability + data-retention/access-on-request standard rather than the mandatory code-and-data deposit mandate of sister journal Management Science — confirm current policy before making hard claims.
5. Verify all licensing, IRB/ethics, and confidentiality terms (especially for field-site and trace data) before depositing or sharing.

## 6. Verify Before You Rely

Editorial team, submission links, length norms, fees, and transparency/data policies change
over time. Always confirm the current requirements on the official Organization Science
submission-guidelines and editorial-statement pages and the Manuscript Length Policy PDF
before submitting.

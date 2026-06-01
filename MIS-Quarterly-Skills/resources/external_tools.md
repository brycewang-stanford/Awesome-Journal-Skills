# Information-Systems Research Tools & Resources (MISQ)

This document lists external data sources, software, and writing tools commonly used when
preparing an information systems manuscript for **MIS Quarterly (MISQ)**. Because MISQ
spans **four research traditions — behavioral, design science, economics, and
organizational** — the toolkit is genre-aware: a design-science build-and-evaluate paper,
a behavioral survey/experiment, and an economics-of-IS econometric study draw on very
different stacks. Always verify licensing terms and the current MISQ Style Guide and
research-transparency policy before relying on any resource.

## 1. Data Sources

### Platform, digital-trace, and behavioral data (behavioral / economics-of-IS)
| Source | Typical use |
|--------|-------------|
| Platform / app server logs & clickstream | Use, adoption, engagement, IT artifact impact |
| App Store / Google Play, GitHub, Stack Overflow | Open source, app markets, developer behavior |
| Online marketplaces & review platforms (Amazon, Yelp, Airbnb) | Reviews, reputation, two-sided markets |
| Social media APIs (X/Twitter, Reddit) | Online community, UGC, network effects |
| Crowdfunding / gig platforms (Kickstarter, Upwork) | Digital platforms, online labor |
| Crunchbase, PitchBook | IT firms, funding, digital ventures |

### Firm / IT-investment and econometric data (economics & organizational IS)
| Source | Typical use |
|--------|-------------|
| Compustat / CRSP | IT firm value, productivity, market reaction to IT events |
| SEC EDGAR (10-K, 8-K) | IT disclosures, breaches, digital strategy text |
| Harte-Hanks / CI Technology Database | Firm IT spending and infrastructure |
| Privacy Rights Clearinghouse, HHS breach portal | Data breaches, security, privacy |

### Behavioral survey / experiment panels
| Source | Typical use |
|--------|-------------|
| Qualtrics, Prolific, MTurk, CloudResearch | Online surveys and behavioral IS experiments |
| Panel providers (e.g., for organizational adoption studies) | Multi-wave, multi-source designs |

## 2. Software & Packages by Tradition

### Design science research (DSR) — build and evaluate the IT artifact
- **Build:** Python, R, Java; ML/DL stacks (PyTorch, TensorFlow, scikit-learn, Hugging Face) for IT artifacts such as recommender systems, NLP/text-analytics tools, prediction and decision-support systems.
- **Evaluate:** held-out test sets, A/B field experiments, simulation, expert evaluation; report build-and-evaluate cycles against Hevner et al. (2004) design-science guidelines and demonstrate the artifact's utility for a real problem.
- **Reproducibility:** version-controlled artifact (Git), containerization (Docker), and a public repository where confidentiality permits.

### Behavioral IS — measurement and structural models
- **PLS-SEM:** SmartPLS, R `seminr` / `cSEM` (common in IS for predictive/formative models).
- **Covariance-based SEM:** Mplus, R `lavaan`, AMOS; report CFA fit, AVE, discriminant validity (Fornell-Larcker / HTMT).
- **Mediation/moderation:** Hayes PROCESS (SPSS/R), R `mediation`, `interactions`.

### Economics of IS & organizational IS — causal econometrics
- **Stata:** `reghdfe` (high-dimensional FE), `ivreghdfe` (IV/2SLS), `csdid`/`did` (modern staggered DiD), `rdrobust` (RD), `psmatch2`/`teffects` (matching), `xtreg`.
- **R:** `fixest`, `did`, `MatchIt`, `rdrobust`, `sandwich` (clustered/robust SE).
- Natural experiments around IT shocks (platform/policy changes, breaches, system go-lives) for identification.

### Text / network analytics (cross-tradition)
- Topic models, embeddings, LLM-based coding; `igraph`/`networkx` for IT-mediated networks.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| Zotero | Free; configure to **APA 7th edition** per the MISQ Style Guide |
| EndNote / Mendeley | Broad style support; reconcile to APA 7th |
| Overleaf / LaTeX | Optional; the portal accepts Word (.doc/.docx) — verify before using LaTeX |
| Grammarly | Language polish |

The MISQ Style Guide is APA-7th-based; note the MISQ convention that **in-text citations lead with the cited information, not the author name** — check your reference manager's output against the current MISQ Style Guide.

## 4. Submission & Process

- **Submission portal:** ScholarOne Manuscripts (the only accepted method); upload a Word file. Verify the current MISQ submission link.
- **Transparency commitment:** prepare genre-appropriate transparency materials (design/data/analysis plus procedures and/or code sufficient for replication) and upload the commitment at Step 2 (Miscellaneous).
- **Replication & open science:** consider replication badges and the collaboration with AIS Transactions on Replication Research.
- **Reciprocity:** by submitting you agree to review up to three papers/year if invited.

## 5. Reproducibility & Transparency

1. Keep clean, commented scripts/notebooks (and, for DSR, the buildable artifact) that regenerate every table, figure, and reported result.
2. Document data provenance, sample construction, exclusion rules, and (for platforms) the scrape/API window and terms.
3. Because supplementary materials are discouraged and page limits count everything, plan what genuinely fits inside the category page limit versus the transparency package.
4. Share de-identified data and code where confidentiality and platform terms permit; for DSR, share the artifact or a faithful demo.

## 6. Verify Before You Rely

Editorial team, submission links, category page limits, the abstract format, and the
research-transparency policy change over time. Always confirm the current requirements on
the official MISQ submission and instructions pages and the current MISQ Style Guide
before submitting.

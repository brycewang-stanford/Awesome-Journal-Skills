# Marketing-Research Tools & Resources (JM)

This document lists external data sources, analysis software, and writing tools commonly used when preparing a **substantive, managerially relevant** marketing manuscript for the **Journal of Marketing (JM)**. JM is methodologically "big tent" — it welcomes primary data (experiments, field studies, surveys, interviews, observational data) and secondary data, and actively champions **empirics-first** research grounded in real-world marketing phenomena. The toolkit below therefore spans behavioral experiments, marketing-strategy panels, and firm/customer field data. Because JM's bar is *substantive insight with managerial, policy, or societal relevance* — not methodological novelty — pick tools that let you measure marketing phenomena and outcomes that managers and policy makers care about, not the most elaborate estimator. Always verify licensing terms and current AMA/JM policies before using any resource.

## 1. Data Sources

### Marketing-strategy, brand & firm performance (secondary)
| Source | Provider | Typical use |
|--------|----------|-------------|
| Nielsen / NielsenIQ (incl. Kilts-Nielsen at U. Chicago Booth) | NielsenIQ | Retail scanner, household panel, CPG sales |
| IRI / Circana academic dataset | Circana | Store/brand-level sales, promotions |
| Kantar / WPP BrandZ, Interbrand | Kantar / Interbrand | Brand equity, brand value |
| comScore / Similarweb | comScore / Similarweb | Digital traffic, e-commerce behavior |
| Compustat / CRSP | S&P Global / CRSP | Firm financials, abnormal stock returns (marketing-finance) |
| ABI/Kantar Ad Intel, Pathmatics | Kantar / Sensor Tower | Advertising spend, media mix |
| customer / CRM transaction logs (firm-provided) | Partner firms | CLV, churn, RFM, field interventions |

### Consumer behavior, experiments & panels (primary)
| Source | Provider | Typical use |
|--------|----------|-------------|
| Prolific / CloudResearch / MTurk | Various | Online experiments and surveys |
| Qualtrics | Qualtrics | Survey instruments, conjoint, choice experiments |
| Sawtooth Software | Sawtooth | Choice-based conjoint, MaxDiff, willingness-to-pay |
| eye-tracking / biometrics (Tobii, iMotions) | Tobii / iMotions | Attention, arousal, ad processing |
| field-experiment partners (retailers, platforms) | Partner firms | Randomized field tests of marketing actions |

### Text / social / alternative data
| Source | Use |
|--------|-----|
| social platforms (X/Twitter, Reddit, TikTok, Instagram APIs) | WOM, engagement, virality |
| review platforms (Amazon, Yelp, Google reviews) | Sentiment, ratings, online reputation |
| Google Trends / search-query data | Demand signals, attention |
| ad libraries (Meta, Google) | Creative content, targeting |

## 2. Analysis Software & Packages

### Behavioral experiments & mediation/moderation
- **R**: `lavaan` (SEM/CFA), `mediation`, `processR`, `emmeans`, `effectsize` (report effect sizes), `pwr`/`Superpower` (power analysis).
- **SPSS / R PROCESS macro** (Hayes) — conditional indirect effects with bootstrapped CIs.
- **G*Power** — a priori power analysis for experiments.
- **JM requires actual p-values, standard errors, and effect sizes** — configure output accordingly (no "p < .05" thresholds).

### Marketing-strategy / panel & causal field analysis
- **Stata**: `reghdfe` (high-dimensional FE), `ivreghdfe`/`ivreg2` (IV/2SLS), `csdid`/`did` (staggered DiD), `synth`/`sdid` (synthetic control), `teffects`/`psmatch2` (matching), cluster-robust SE.
- **R**: `fixest`, `did`, `Synth`, `MatchIt`, `sandwich`.
- **Choice / demand models**: `mlogit`, `bayesm`, `apollo` (discrete choice); hierarchical Bayes for heterogeneity.

### Customer analytics & marketing metrics
- CLV / buy-till-you-defect (`BTYD`, `CLVTools` in R); marketing-mix and attribution models; elasticity estimation.

### Qualitative / mixed methods
- **NVivo**, **ATLAS.ti**, **Dedoose** — coding; keep interview guides, coding procedures, and annotated examples for the JM replication packet.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| Zotero | Free; configure AMA author-date output |
| EndNote | Broad style support; AMA/JM style |
| Overleaf / LaTeX | AMA provides LaTeX style files; 12-pt font, double-spaced |
| Word (AMA template) | AMA provides a Word manuscript template |
| Grammarly | Language polish |

JM uses **AMA house style**: author-date in-text citations, full author names for up to three authors and "et al." for four or more. Configure your reference manager accordingly and reconcile against the current AMA/JM guidelines.

## 4. Submission & Process

- **Submission portal**: ScholarOne / Manuscript Central (Sage Track) at **mc.manuscriptcentral.com/ama_jm**; online submission only.
- **Anonymization**: double-anonymized review — remove all author/institution identifiers from the manuscript.
- **Plagiarism/originality**: screened with **iThenticate**.
- **Data Availability Statement** required on the title page of final manuscripts.

## 5. Reproducibility & Transparency (JM Dataverse)

1. JM requires a **replication packet** at conditional acceptance, deposited to **JM's Dataverse**: raw data files, analysis programs/scripts, and any details sufficient to replicate all reported analyses. For qualitative work: interview guides, coding procedures, and annotated examples.
2. The packet is accessible to the **processing Editor**, not to reviewers.
3. The policy applies to conditionally accepted revisions of manuscripts submitted on/after **2023-01-01**.
4. **Preregistration is encouraged**: provide anonymized links in the paper and attest you faithfully represented the preregistration.
5. Keep clean, commented analysis scripts that regenerate every reported number, table, and figure; document sample-construction and exclusion rules.

## 6. Verify Before You Rely

Editorial team, submission links, page/format limits, fees/OA prompts, and transparency/data policies change over time. Always confirm current requirements on the official JM/SAGE submission guidelines and the AMA editorial pages before submitting.

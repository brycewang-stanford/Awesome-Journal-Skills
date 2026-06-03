# External Tools & Resources for POQ-Style Public Opinion & Survey Research

Data sources, software, and standards useful when preparing a *Public Opinion Quarterly* (POQ)
submission. POQ is the leading journal of **public opinion and survey methodology**: a submission may
test a substantive opinion/communication question, advance a survey-methods finding, or both. The
unifying frame is **Total Survey Error (TSE)** and **AAPOR-standard methodological disclosure**. Match
tools to your design and document every methodological element. Check licenses and current access
terms before use, and verify any POQ-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Survey data sources

### US opinion & behavior
| Source | Provider | Typical use |
|--------|----------|-------------|
| ANES (American National Election Studies) | Michigan/Stanford | Vote choice, opinion, participation, panel |
| GSS (General Social Survey) | NORC | Long-run US social/political attitudes |
| CES / CCES (Cooperative Election Study) | Harvard | Large-N US survey, district-level analysis |
| Pew Research Center datasets | Pew | Topical opinion, trends, methods experiments |
| Gallup / Roper iPoll (archive) | Gallup / Cornell Roper | Historical poll trends, question archives |

### Cross-national & panel
| Source | Provider | Typical use |
|--------|----------|-------------|
| Eurobarometer | European Commission | Cross-national EU opinion |
| World Values Survey / ISSP | WVS / ISSP | Cross-national values and attitudes |
| CSES | Comparative Study of Electoral Systems | Cross-national electoral behavior |
| Understanding America Study (UAS) / GfK-KnowledgePanel | USC / Ipsos | Probability-based online panels |
| ESS (European Social Survey) | ESS ERIC | High-standard cross-national survey, paradata |

## 2. Survey methodology toolkit (the POQ core)

### Total Survey Error components to address
- **Coverage error** — frame vs. target population; undercoverage of online/RDD/ABS frames
- **Sampling error** — design-based variance; design effects from clustering and stratification
- **Nonresponse error** — unit and item nonresponse; response rate per **AAPOR Standard Definitions**
- **Measurement error** — question wording, order, response scales, social desirability, mode effects
- **Processing/adjustment error** — editing, coding, weighting, imputation

### Response rates & disclosure
- **AAPOR Standard Definitions** (RR1–RR6, COOP, REF, CON rates) — report which definition and show the
  disposition-code calculation; this is required in POQ's **Appendix A: Disclosure Elements**
- AAPOR Transparency Initiative checklist for routine methodological disclosure

## 3. Software by task

### R (widely used in survey methodology)
- Complex-survey estimation: `survey` (Lumley), `srvyr`, `svyVGAM` — design-based SEs, subpopulations
- Weighting/calibration: `anesrake` (raking), `survey::calibrate`, `WeightIt`, `autumn`
- Nonresponse/missing data: `mice` (multiple imputation), `VIM`; weighting-class adjustments
- Measurement/scaling/IRT: `lavaan` (CFA/SEM, MGCFA for measurement invariance), `mirt`, `psych`
- Experiments embedded in surveys: `cregg`/`cjoint` (conjoint), `list` (list experiments), `ri2`
- Mode/mixed-mode and small-area: `lme4`/`brms` (multilevel), `survey` post-stratification (MRP)

### Stata
- `svy:` prefix with `svyset` (design, weights, strata, PSUs); `estat effects` for DEFF
- `raking`/`ipfraking`, `gllamm`/`sem` (measurement invariance), `mi` (multiple imputation)

### Python
- `pandas`, `numpy`, `statsmodels`; `samplics` (complex-survey estimation, weighting, SAE)
- `pyreadstat` (read SPSS/Stata survey files with value labels); `linearmodels`

## 4. Questionnaire design & pretesting
- Cognitive interviewing, behavior coding, and **pretesting** logs; question banks (GSS/ANES/Pew wording)
- Web-survey programming: Qualtrics, Gorilla, SurveyCTO, formr — log paradata (timing, breakoffs)
- Split-ballot / wording and order experiments to quantify measurement effects

## 5. Transparency, replication & disclosure
- Replication/reproduction package destined for **POQ's Dataverse on Harvard Dataverse** — code +
  data that **reproduce exactly all published tables and figures** (see `poq-transparency-and-data-policy`)
- **AAPOR-standard disclosure** assembled into **Appendix A: Disclosure Elements** (funding, exact
  wording, population, sample design, mode and dates, response rate + calculation, sample sizes +
  precision, clustering/weighting design effects)
- Reproducibility hygiene: `renv.lock` / `requirements.txt`, set/report seeds, one master script
- **Data Availability Statement** in the endmatter; restricted-data exemption + access path + synthetic data

## 6. Figures & exhibits
- Trend lines with uncertainty bands for opinion over time; coefficient/forest plots with design-based SEs
- Conjoint AMCE plots; marginal-effects and predicted-probability plots; weighted vs. unweighted overlays
- Colorblind-safe palettes, grayscale-legible; vector output (PDF/EPS) for print

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **ScholarOne Manuscripts** (`mc.manuscriptcentral.com/poq`) — confirm current URL |
| Publisher / affiliate | **Oxford University Press** / **AAPOR** |
| Review model | **Double-blind** — anonymize the manuscript |
| Submission types | Original Article (≤ 6,500 words) · Research Note (< 3,000) · Polls in Context (≤ 2,500) · Research Synthesis (≤ 6,500) · Book Review (~1,200) |
| Disclosure | **Appendix A: Disclosure Elements** per AAPOR standards (response rate per AAPOR definitions, sampling, weighting) |
| Data policy | Replication package to **POQ's Harvard Dataverse** + **Data Availability Statement**; archived before typesetting |

## 8. Cautions
1. **Verify volatile specifics** (editors, exact caps, section names, fee/APC, embargo, data-policy
   wording) on the official OUP/AAPOR pages — they change; unverified items are marked 待核实.
2. **Disclose to AAPOR standards** — report the response rate *and how it was calculated* (AAPOR
   Standard Definitions), sampling, and weighting; assemble Appendix A early, not at the end.
3. **Frame error explicitly** — situate your design in Total Survey Error; do not treat one error
   source in isolation while ignoring the others.
4. **Use design-based inference** — weights, strata, and clusters belong in the variance estimator, not
   just the point estimate.
5. **Build the replication package as you go** — it must reproduce every table and figure and is
   archived before typesetting.

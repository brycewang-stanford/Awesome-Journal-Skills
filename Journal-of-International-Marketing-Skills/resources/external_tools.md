# External Tools & Data Sources for JIM Research

Working inventory for multi-country marketing research aimed at the *Journal of International Marketing*. Availability and licensing change — confirm access terms before building a design around any source.

## Country-level data (the moderator layer)

| Source | What it gives a JIM paper |
|--------|---------------------------|
| Hofstede / GLOBE / Schwartz score sets | national cultural dimensions for theorized moderation (use the dimension, cite the framework's edition) |
| World Bank WDI & Worldwide Governance Indicators | income, rule of law, regulatory quality — the institutional layer |
| WTO / UN Comtrade | trade flows, tariffs — shocks and exposure measures for export designs |
| CEPII gravity databases | bilateral distance measures (geographic, linguistic, colonial) for dyadic models |
| Euromonitor / Statista country reports | market-size and category penetration context (verify licensing for publication) |

## Consumer and firm data across countries

| Source | Use |
|--------|-----|
| Prolific / CINT / Dynata multi-country panels | matched consumer samples; document per-country screening identically |
| GfK / NielsenIQ / Kantar international panels | scanner and household data where partnerships permit |
| Export registries, customs microdata, ORBIS/Amadeus | firm-level internationalization outcomes |
| World Values Survey / ESS | individual-level values with national coverage — useful for ecological-fallacy-free designs |

## Analysis software for the JIM toolchain

| Task | Tools |
|------|-------|
| Measurement invariance (MGCFA, partial, alignment) | lavaan (R), Mplus; `semTools` for ΔCFI machinery; alignment in Mplus / `sirt` |
| Multilevel models with country predictors | lme4 / brms (R; Bayesian helps with few countries), Stata `mixed`, HLM |
| Multi-group SEM | lavaan, Mplus, AMOS |
| Panels, DiD, IV for export designs | Stata (`reghdfe`, `csdid`, `ivreg2`) — see [`code/`](code/) for runnable templates |
| Meta-analysis with country moderators | `metafor` (R) |
| Translation workflow | committee + back-translation logs; keep every language version under version control |

## Search and verification

- SAGE JIM archive (journals.sagepub.com/home/jig) for recent-volume positioning
- ama.org for calls for papers and editorial announcements
- DOI/publisher pages to verify every exemplar citation before use (see [`exemplars/library.md`](exemplars/library.md))

## Method notes

- Archive the country-selection memo (focal dimension, confound audit) with the data — reviewers ask for it a year later.
- Keep raw data → cleaned data → estimates lineage scriptable per country; a single pooled cleaning script hides country-specific decisions that invariance reviewers will probe.
- Version the invariance ladder outputs (fit per step) as artifacts, not just numbers pasted into a table.

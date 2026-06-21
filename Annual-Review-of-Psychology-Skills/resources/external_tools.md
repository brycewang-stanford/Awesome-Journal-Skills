# External Tools for Annual Review of Psychology

Tools that support an **invited review** for ARPsych: literature discovery, systematic
search, evidence synthesis, meta-analysis, and reproducible deposition. A review reports no
new primary data, so the emphasis is on **finding the whole literature** and on **making any
embedded meta-analysis reproducible** — not on a primary-study analysis pipeline.

## Literature discovery & systematic search

| Tool or source | Use |
|----------------|-----|
| APA PsycINFO / PsycNet | the field's primary index; core database for a documentable psychology search |
| Web of Science / Scopus | cross-disciplinary coverage; forward/backward citation chasing |
| Google Scholar | broad recall + "cited by" tracing; cross-check coverage gaps |
| PubMed | for biological/neuro and clinical-adjacent psychology topics |
| Connected Papers / Litmaps / Research Rabbit | visualize citation neighborhoods; surface missed clusters |
| Retraction Watch / database flags | screen out retracted or contested findings before reviewing them |

## Evidence organization

| Tool or source | Use |
|----------------|-----|
| Reference manager (Zotero / EndNote) | build the evidence matrix; keep references complete and accurate |
| Coding spreadsheet | one row per study: construct, population, design, effect, replication status, lab/camp |
| PRISMA flow template | document search → screening → included counts (required for an embedded meta-analysis) |

## Meta-analysis & reproducibility (only if the review embeds quantitative synthesis)

| Tool or source | Use |
|----------------|-----|
| R `metafor` / `meta` | pooled effects, heterogeneity (I²), moderators, forest/funnel plots |
| `robumeta` / `clubSandwich` | robust variance estimation for dependent effect sizes |
| OSF | deposit effect-size data, coding sheet, and analysis code; cite the DOI |
| PROSPERO | prospective registration of a systematic review/meta-analysis protocol |

## Method notes

- Document the search **as you go** (databases, terms, dates, in/out, stopping rule) — a narrative review still benefits from a reproducible protocol; a meta-analysis requires one.
- Note **replication status** alongside each contested effect; post-replication-crisis, ARPsych readers expect it.
- Watch for **WEIRD / sample-diversity** concentration and **citation/self-citation** concentration; both are balance risks the Committee notices.
- Keep figure source files editable and high-resolution; Annual Reviews re-renders exhibits at production and requires permission for reproduced material.

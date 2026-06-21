---
name: fcr-submission
description: Use when running the final pre-submission preflight for Field Crops Research (FCR) via Editorial Manager — article-type selection, abstract (<=400 words) and highlights (3-5 bullets of <=85 characters), complete agronomic reporting, data-availability statement, generative-AI declaration, Elsevier formatting, and the cover letter. Final checks; it does not draft content.
---

# Submission Preflight (fcr-submission)

The last check before pressing submit on **Editorial Manager** at `submit.elsevier.com/FIELD`. FCR's
most common avoidable failures are **scope mismatch** and **incomplete reporting / declarations**. Check
upload-week specifics on the official Elsevier guide before relying on editor names, prices, file
prompts, or article-type menus (see `../../resources/official-source-map.md`).

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Editorial Manager expects
- Confirming scope fit, format, and declarations are complete

## Process facts

- **Publisher:** Elsevier (ISSN **0378-4290**).
- **Portal:** **Editorial Manager** at `submit.elsevier.com/FIELD`.
- **Review model:** **single anonymized** — typically ≥ 2 reviewers.
- **Article types:** Original Research Paper · Short Communication · Review (usually invited) · Opinion
  Paper · Loomis Review (invited).
- **Abstract:** **≤ 400 words**.
- **Highlights:** **3–5 bullets, each ≤ 85 characters** including spaces.
- **Multi-environment rule:** field experiments should span **≥ 2 seasons and/or multiple
  environments** (unless exceptional circumstances are justified).
- **Data availability:** must be **stated at submission**.
- **Generative AI:** **declare any use** in manuscript preparation.

## Preflight checklist

### Scope & type
- [ ] Field-based, multi-season/-environment, a field crop, generally significant (see `fcr-topic-selection`)
- [ ] Article type chosen; Review/Opinion proposal cleared with editors if required

### Manuscript & format
- [ ] Abstract ≤ 400 words; states purpose, environments, quantitative result, conclusion
- [ ] **3–5 highlights**, each ≤ 85 characters, findings not topics
- [ ] Structure: focused intro → complete methods → concise results → interpretive discussion
- [ ] SI units; consistent Elsevier/FCR reference style; grammatically sound English
- [ ] Figures/tables self-contained with units and **SED/LSD/CI** (see `fcr-figures-and-tables`)

### Reporting completeness
- [ ] Crop/cultivar, sites/seasons, soil, **weather vs. phenology**, management, design, statistics
- [ ] Yield data included/linked to biophysical process where relevant

### Declarations & files
- [ ] **Data-availability statement** drafted (shared + repository/ID, or restricted + reason)
- [ ] **Generative-AI** use declared; CRediT roles, funding, competing interests
- [ ] Cover letter establishing scope fit + contribution (see `fcr-cover-letter`)
- [ ] Co-submission to **Data in Brief / MethodsX** considered if relevant

## Highlights bench-test (illustrative)

Highlights are findings, not topics, and the **≤85-character** limit counts spaces. Bench-test each
bullet.

| Draft highlight | Chars | Verdict |
|-----------------|-------|---------|
| "Effects of nitrogen on wheat yield and quality" | 47 | reject — a topic, not a finding |
| "New cultivar raised yield 0.9 t/ha in high-N environments only" | 62 | keep — quantified |
| "G×E explained 38% of yield variance across 8 site-years" | 56 | keep — names the result |

## Worked preflight vignette (illustrative)

*Illustrative dry-run.* A maize MET manuscript reaches the final pass: **2 seasons × 4 sites**, abstract
at **410 words**, 6 highlights, a plot-level dataset, but **no weather-vs-phenology figure**. The
preflight catches four blockers: trim the abstract under the 400-word cap; cut highlights to **5** and
rewrite topic-style bullets as findings; add the weather-vs-phenology panel so the G×E is interpretable;
and draft the **data-availability statement** to the Mendeley Data DOI. Scope and
statistics pass, so once fixed the package is ready for Editorial Manager.

## Anti-patterns

- Submitting controlled-environment-only or single-site/single-season work
- Abstract over length; highlights that are topics or exceed 85 characters
- Methods missing soil/weather-vs-phenology/management (not reproducible)
- Blank data-availability statement; missing generative-AI declaration
- A discussion that repeats results; means with no error term


## Operating pass for Field Crops Research

Treat this skill as an executable review pass, not a prose hint. First lock the crop system, environment structure, GxE logic, and yield or physiology endpoint; then judge whether the current manuscript answers the venue's real reader: agronomy reviewers who expect field-based, multi-environment evidence and crop-level general significance.

- **Do the pass:** Return a claim-evidence-risk ledger rather than a prose-only diagnosis; every recommendation must point to a manuscript location or missing artifact.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Agricultural Systems for whole-system modeling, European Journal of Agronomy for agronomic breadth, Crop Science for cultivar or breeding emphasis; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Submission-ready gate:** do not give final advice until the pack's
  `resources/official-source-map.md` has been checked for upload-week rules and the manuscript has one
  concrete fix for the largest venue-specific risk.

## Output format

```
【Scope & type】field-based + ≥2 seasons/envs + field crop + general; type chosen? [Y/N]
【Abstract & highlights】≤400 words; 3-5 bullets ≤85 chars? [Y/N]
【Reporting complete】cultivar/site/soil/weather-vs-phenology/management/design/stats? [Y/N]
【Declarations】data availability + generative-AI + CRediT/funding? [Y/N]
【Cover letter】scope fit + contribution stated? [Y/N]
【Next】await decision → fcr-revision-and-rebuttal on a revise verdict
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers and Elsevier typesetting/templates
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official FCR URLs behind every fact in this pack

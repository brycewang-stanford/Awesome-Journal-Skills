---
name: arpsych-transparency-and-reproducibility
description: Use when documenting the literature search and making any embedded meta-analysis reproducible for an Annual Review of Psychology (ARPsych) review. Covers search transparency, meta-analytic rigor, and open materials; it does not run the narrative search (arpsych-literature-synthesis) or design exhibits (arpsych-tables-figures).
---

# Transparency & Reproducibility (arpsych-transparency-and-reproducibility)

## When to trigger

- The review documents a systematic search and you must report it reproducibly
- The review embeds a **meta-analysis** or any new quantitative synthesis
- You are deciding what to deposit (search log, coding sheet, effect-size data, code)
- A reader or the Committee should be able to verify how the literature was selected

## A review reports no new data — so transparency bites elsewhere

A pure narrative review has no dataset of its own, so the transparency obligation does **not** look like a primary-paper replication package. It bites on two things:

1. **How the literature was found and selected** — the search protocol from `arpsych-literature-synthesis`, written up so a reader could reproduce the coverage.
2. **Any quantitative synthesis the review itself contributes** — if you compute pooled effects, that *is* original analysis, and it must be reproducible (检索于 2026-06；以官网为准).

Post-replication-crisis, ARPsych readers expect both, and a review that asserts "the literature shows…" with no documented basis reads as less authoritative.

## If the review is narrative (no meta-analysis)

- Report the **search**: databases, terms, date range, inclusion/exclusion, and the stopping rule — a short, near-PRISMA-style account suffices.
- State **selection logic**: why these studies and not others (especially when the field is large and you are selective).
- Be explicit about **replication status** of contested effects (this is part of transparency, not just balance).

## If the review embeds a meta-analysis

Then you have run original analysis and must meet quantitative-synthesis standards:

| Requirement | What to provide |
|-------------|-----------------|
| **PRISMA-style flow** | search → screening → included, with counts at each step |
| **Coding protocol** | how effects were extracted/coded; inter-coder reliability |
| **Effect-size dataset** | the extracted effects + moderators, deposited |
| **Analysis code** | scripts reproducing the pooled estimates and plots |
| **Heterogeneity + bias** | I², moderators, funnel/publication-bias diagnostics |
| **Preregistration (if applicable)** | protocol/PROSPERO registration where the synthesis was prospective |

Deposit data and code in a public repository (e.g., **OSF**) and cite the DOI in the review.

## Required declarations (检索于 2026-06；以官网为准)

Annual Reviews requires authors to **disclose potential sources of bias / conflicts of interest** and to state funding; prepare these per the author pages. **AI tools are not authors.** Re-confirm the exact disclosure format on the live Annual Reviews pages.

## Checklist

- [ ] Search protocol written up reproducibly (databases, terms, dates, in/out, stopping rule)
- [ ] Selection logic stated where coverage is selective
- [ ] Replication status of contested effects made explicit
- [ ] If meta-analytic: PRISMA-style flow with counts
- [ ] If meta-analytic: coding protocol + inter-coder reliability reported
- [ ] If meta-analytic: effect-size data + analysis code deposited (OSF DOI cited)
- [ ] If meta-analytic: heterogeneity and publication-bias diagnostics reported
- [ ] COI / potential-bias disclosure + funding prepared; AI not listed as author

## Anti-patterns

- "The literature shows…" with no documented search behind the claim
- Reporting pooled effects with no deposited data or code (irreproducible meta-analysis)
- A meta-analysis with no heterogeneity or publication-bias assessment
- Treating a review's transparency like a primary-paper replication package (wrong object)
- Omitting the conflict-of-interest / potential-bias disclosure Annual Reviews requires
- Listing an AI tool as an author or hiding its use where disclosure is required

## Output format

```text
【Review type】narrative | embedded-meta-analysis
【Search transparency】protocol documented reproducibly? Y/N
【If meta-analysis】PRISMA flow + coding + reliability? Y/N
【Open materials】effect data + code deposited (OSF DOI)? Y/N | N/A
【Heterogeneity / bias】I² + funnel/pub-bias reported? Y/N | N/A
【Declarations】COI / bias disclosure + funding prepared; AI not author? Y/N
【Next step】→ arpsych-editor-strategy (align scope/timeline with the Editor)
```

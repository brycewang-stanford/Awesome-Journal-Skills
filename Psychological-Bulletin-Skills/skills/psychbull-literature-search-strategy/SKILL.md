---
name: psychbull-literature-search-strategy
description: Use when designing and documenting the systematic literature search for a Psychological Bulletin review or meta-analysis — databases, search strings, grey literature, deduplication, and a PRISMA-compliant records flow. Builds a reproducible search; it does not screen or code studies.
---

# Systematic Search Strategy (psychbull-literature-search-strategy)

A Psychological Bulletin synthesis stands or falls on its **search**: it must be **systematic,
exhaustive, and reproducible**, and **all systematic reviews must conform to PRISMA**. The goal is
that an independent team could re-run your search and recover the same pool. This skill designs and
documents the search; eligibility decisions and coding live in `psychbull-inclusion-and-coding`.

## When to trigger

- Designing the search before screening begins
- A reviewer asks whether the search was exhaustive or reproducible
- Building the **PRISMA flow** counts (identified → screened → eligible → included)
- Updating the search before resubmission

## What an exhaustive search covers

1. **Multiple databases, not one.** At minimum APA **PsycINFO**, plus **MEDLINE/PubMed**, **Web of
   Science**, **Scopus**, and discipline-specific sources (ERIC, EMBASE) as relevant.
2. **Controlled vocabulary + free text.** Combine thesaurus terms (APA Thesaurus / MeSH) with
   free-text synonyms; use Boolean logic and field tags deliberately.
3. **Grey literature & publication-bias mitigation.** Dissertations (ProQuest), preprints (PsyArXiv),
   conference programs, registries, and **author contact** for unpublished/in-press data — to limit
   the file-drawer problem before the bias analysis ever runs.
4. **Backward & forward citation chasing.** Reference lists of included studies and prior reviews;
   forward citations (cited-by) of key papers.
5. **Supplementary tools.** Google Scholar as a supplement (not a primary database, given non-reproducible ranking).

## Documenting for PRISMA / PRISMA-S

- Record, **per source**: the **exact search string**, the **database/platform and date searched**,
  and the **number of hits**. This is the PRISMA-S standard.
- Track the flow: **records identified → duplicates removed → titles/abstracts screened → full texts
  assessed → studies included**, with **counts and exclusion reasons** at each stage.
- Save the raw exports; deduplicate in a reference manager (Zotero/EndNote) or screening tool
  (Covidence/Rayyan) and log the dedup count.

## Anti-patterns

- Searching only one database, or only published, peer-reviewed work (biases the pool)
- Reporting "we searched the literature" with no strings, dates, or counts
- A search that cannot be reproduced because the strings were never recorded
- Letting search scope drift silently from the registered protocol without noting the change
- Skipping grey literature, then being surprised by publication-bias findings

## Output format

```
【Databases】list (PsycINFO + …) with date searched
【Strings】per-database string recorded? [Y/N]
【Grey literature】dissertations / preprints / author contact? [Y/N]
【Citation chasing】backward + forward done? [Y/N]
【PRISMA counts】identified / dedup / screened / full-text / included
【Reproducible】independent team could re-run? [Y/N]
【Next】psychbull-inclusion-and-coding
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — databases, screening managers (Covidence/Rayyan), PRISMA-S
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — PRISMA requirement for systematic reviews

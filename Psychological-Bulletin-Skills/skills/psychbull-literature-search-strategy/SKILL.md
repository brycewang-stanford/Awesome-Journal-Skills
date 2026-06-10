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

## What search referees verify at the APA flagship

A Psychological Bulletin synthesis lives or dies on whether an independent team could rebuild its study
pool. Reviewers at the APA's flagship review journal apply an explicit search bar:

| Search expectation | Pass | Desk-reject / major-revision trigger |
|--------------------|------|--------------------------------------|
| Database breadth | PsycINFO + several others + discipline sources | A single database, usually PsycINFO alone |
| Strings recorded | Per-source string, platform, and date logged | "We searched the literature" with no strings |
| Grey literature | Dissertations, preprints, author contact | Published peer-reviewed work only |
| Citation chasing | Backward and forward, documented | None; pool is whatever the keywords returned |
| PRISMA flow | Counts and exclusion reasons reconcile | Numbers that don't add up to the included k |

## Worked vignette — documenting the search

*Illustrative counts only.* The self-affirmation synthesis (final k = 42) builds its PRISMA flow this
way under this skill's rules:

- **Databases**: PsycINFO, MEDLINE, Web of Science, Scopus, and ERIC, each searched on a stated date
  with its exact thesaurus-plus-free-text string recorded per PRISMA-S.
- **Grey literature**: ProQuest dissertations and PsyArXiv preprints searched; authors of 11 in-progress
  trials contacted, yielding 3 unpublished datasets — narrowing the file drawer before bias diagnostics.
- **Citation chasing**: backward (reference lists of included studies and two prior reviews) and forward
  (cited-by of the 5 anchor papers) added 7 records the keyword search missed.
- **PRISMA flow**: 2,310 identified → 1,640 after dedup → 1,640 screened → 188 full-text →
  42 included, with exclusion reasons tallied so the final box equals the analyzed k.

## Referee pushback → venue-specific fix

- *"The search isn't exhaustive."* → Add the missing databases and grey-literature sources; document
  author contact for unpublished data.
- *"There are PRISMA gaps."* → Supply per-source strings, dates, and hit counts, and make the flow
  diagram reconcile end to end.
- *"This search can't be reproduced."* → Record and deposit the exact strings so an independent team
  recovers the same pool; treat Google Scholar as a supplement, not a primary source.

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

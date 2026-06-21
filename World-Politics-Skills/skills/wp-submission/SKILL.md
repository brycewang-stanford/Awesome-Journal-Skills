---
name: wp-submission
description: Use when running the final pre-submission preflight for World Politics via ScholarOne — article-type selection, triple-blind anonymization, the 12,500-word limit (including notes and references), the 150-word abstract, double-spacing, the 15-page online-supplement cap, house-style formatting, the APSA human-subjects affirmation, and prior-publication rules. Final checks; it does not draft content.
---

# Submission Preflight (wp-submission)

The last check before pressing submit on **ScholarOne** (`mc.manuscriptcentral.com/wp`). World Politics
is **triple-blind**, so the most common avoidable failure is an under-anonymized manuscript. Verify
volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming the word limit, abstract, and anonymization are met

## Process facts (verify volatile items on the official page)

- **Sponsor / publisher:** PIIRS, Princeton University / **Johns Hopkins University Press** (publisher
  from **Vol. 75 / 2023**; Cambridge through Vol. 74 / 2022).
- **Portal:** **ScholarOne** (`mc.manuscriptcentral.com/wp`).
- **Review model:** **triple-blind** — anonymize the manuscript; author anonymity is preserved through
  the editorial decision.
- **Article types:** **research article** and **review article** (review articles usually commissioned;
  confirm before submitting an unsolicited one — 待核实).
- **Length:** **≤ 12,500 words including notes and references**; tables, figures, and appendixes
  **need not** be counted. **Online supplementary material ≤ 15 pages.**
- **Abstract:** **≤ 150 words.**
- **Manuscript:** **double spaced**; word count **indicated**; house **World Politics Style Sheet**
  (author-date).
- **Ethics:** affirm **APSA Principles and Guidance for Human Subjects Research (2020)** if research
  engages human participants; ScholarOne prompts IRB/ethics questions.

## Preflight checklist

### Type & length
- [ ] Article type chosen (research / review; commissioning confirmed for review articles)
- [ ] **≤ 12,500 words including notes and references** (tables/figures/appendixes excluded)
- [ ] Word count **indicated**; manuscript **double spaced**
- [ ] Online supplement **≤ 15 pages**, used judiciously for material central to the argument
- [ ] Abstract **≤ 150 words**, stating question + approach + findings

### Anonymity (triple-blind)
- [ ] No bylines or information that could easily identify the author(s)
- [ ] Self-citations **removed where possible**; no "as we showed in…"
- [ ] Identifying **file metadata stripped** (document properties, comments)

### Format & compliance
- [ ] World Politics Style Sheet formatting; consistent author-date citations
- [ ] Figures/tables self-contained, accessible (see `wp-tables-figures`)
- [ ] **APSA human-subjects** affirmation ready; ethical issues discussed in text/appendix if relevant
- [ ] **Prior-publication rules** cleared: not published, concurrently submitted, or already slated
      elsewhere (a print working paper or an author's own-site paper is generally OK)
- [ ] Quantitative data: replication package planned for the **World Politics Dataverse** at acceptance
      (see `wp-transparency-and-data-policy`)

## Anti-patterns

- Leaving author identifiers in the text or file metadata (breaks triple-blind)
- Forgetting that **notes and references count** toward the 12,500 words
- An online supplement over 15 pages, or used as an overflow dump
- Submitting an unsolicited review article without checking the commissioning norm
- Dual-submitting or submitting previously published material (firm policy)

## Avoidable-rejection map (what trips submissions)

The most common avoidable failures at a triple-blind comparative-and-IR venue are anonymity and
length, not the science. Sort the risk before upload.

| Trip-wire | Why it bites at World Politics | The fix |
|-----------|--------------------------------|---------|
| Author identifiers in text or file metadata | Defeats triple-blind, the venue's core process | Strip bylines, self-cites, document properties |
| Notes + references pushed over the count | They count toward the 12,500 words | Tighten apparatus; move detail to the ≤15-page supplement |
| Supplement used as overflow dump | Capped at 15 pages | Keep only material central to the argument |
| Unsolicited review article | Review articles are usually commissioned | Confirm commissioning before drafting |

## Worked micro-example (illustrative)

A hypothetical comparative paper on **institutional design and post-conflict stability** runs the
preflight:

```text
Type:     research article (not a review → no commissioning check needed)
Length:   12,480 words incl. notes + references — under 12,500 by a thin margin
Abstract: 148 words — under 150
Anonymity: removed 3 self-citations + stripped Word author metadata
Supplement: 14 pages (balance tables + full specs) — within the 15-page cap
Ethics:   no human subjects → APSA affirmation N/A
Repro:    Dataverse package staged for deposit at acceptance
```

The thin word-count margin is the live risk; trim notes first. (Length, abstract, and supplement
limits are volatile — verify each against the official submission page before relying on them.)

## Output format

```
【Type】research / review (commissioning confirmed? Y/N)
【Length】≤ 12,500 incl. notes + refs? supplement ≤ 15 pp? [Y/N]
【Anonymized】bylines + self-cites + file metadata clean? [Y/N]
【Abstract】word count (≤150)
【Double spaced + word count indicated + house style】[Y/N]
【Ethics + prior-publication】APSA affirmation + originality cleared? [Y/N]
【Repro package】planned for World Politics Dataverse? [Y/N/NA]
【Next】await decision → wp-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official World Politics URLs behind every fact in this pack

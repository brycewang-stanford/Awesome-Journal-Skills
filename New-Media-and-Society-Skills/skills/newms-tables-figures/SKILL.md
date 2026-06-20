---
name: newms-tables-figures
description: Use when building exhibits for a New Media & Society (NM&S) manuscript — quote/excerpt tables, coding-scheme tables, network and computational figures, and screenshots of platform interfaces. Makes exhibits clear and self-contained; it does not run the analysis.
---

# Tables & Figures (newms-tables-figures)

NM&S exhibits must be self-contained and legible to an interdisciplinary readership — a discourse
scholar should grasp your network figure, and a computational scholar should grasp your quote table.
**Crucially, NM&S counts tables and figures toward the ~8,000-word target** (the limit is all text
including notes, references, tables, and charts), so every exhibit must earn its space.

## When to trigger

- Designing any table or figure, including qualitative exhibits and platform screenshots
- A reviewer found an exhibit unclear, redundant, or unconvincing
- Deciding what to keep in-text vs. trim, given the strict word/space budget

## Exhibit types and what NM&S expects

| Exhibit | Make it carry | Common failure |
|---------|---------------|----------------|
| Quote / excerpt table | each quote tied to a claim + informant ID | a wall of decontextualized quotes |
| Coding-scheme table | categories, definitions, example, reliability | categories with no definitions |
| Descriptive / content-distribution table | counts + proportions + uncertainty | raw counts only |
| Network figure | what nodes/edges mean, layout logic | a hairball with no legend |
| Computational result figure | measure + validation noted, CIs | a pretty plot, no uncertainty |
| Platform screenshot / interface | annotated, anonymized, permissions noted | unredacted personal data |

## Design principles (NM&S house expectations)

1. **Self-contained.** Title, full caption, units, and source let the exhibit stand alone without the text.
2. **Anonymize and redact.** Screenshots and quotes must not expose identifiable users, handles, faces,
   or private content (see `newms-transparency-and-data`).
3. **Show uncertainty.** Content distributions and computational measures carry intervals or reliability,
   not bare point values.
4. **Accessible.** Colorblind-safe palettes, grayscale-legible, readable at print size; vector output.
5. **Earn the space.** Because exhibits count toward the word target, cut any table that a sentence could
   replace; merge overlapping figures.

## Qualitative exhibits matter at NM&S

A well-built **quote-to-claim table** (claim → representative excerpt → informant ID → prevalence) does
real analytic work: it shows the link from evidence to argument and lets a referee audit it fast. A
**coding-scheme table** with definitions and an example per category is often the difference between a
discourse paper read as systematic vs. impressionistic.

## Worked micro-example (illustrative)

```
Exhibit: a quote-to-claim table for "datafied control."
Columns: Claim | Representative excerpt | Informant (pseudonym, role) | # informants expressing
Rows tie each sub-claim (anticipatory compliance; score anxiety; opacity) to evidence + prevalence.
Ethics: handles removed, employer unnamed, screenshots of the app cropped to hide other users.
Space check: replaces three paragraphs of scattered quotes → saves words against the 8,000 target.
```

## Referee pushback → NM&S-specific fix

- *"Your quotes feel cherry-picked."* → Convert to a quote-to-claim table with prevalence counts.
- *"This figure is a hairball."* → Add a legend, prune to a backbone, and state the layout algorithm.
- *"You exceed the word count."* → Cut redundant tables; remember exhibits count toward the target.

## Calibration anchors

- **Exhibits count toward the word target.** Unlike journals that exclude them, NM&S includes tables and
  charts in the ~8,000-word total — be ruthless about which ones earn their space.
- **Qualitative tables are real exhibits.** A quote-to-claim or coding table is analysis made auditable.
- **Anonymize every exhibit.** A leaked handle or face in a screenshot is an ethics failure, not a typo.

## Anti-patterns

- A wall of quotes with no claim mapping or prevalence
- Coding categories listed without definitions or examples
- Network/computational figures with no legend, units, or uncertainty
- Unredacted screenshots exposing identifiable users or private content
- Padding the paper with exhibits that push it over the word target

## Output format

```
【Exhibit】type and the one claim it carries
【Self-contained】caption/units/source complete? [Y/N]
【Anonymized】quotes/screenshots redacted? [Y/N]
【Uncertainty】reliability/intervals shown where relevant? [Y/N]
【Space】counts toward word target — justified vs. cut?
【Next】newms-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — figure, network, and CAQDAS exhibit tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — NM&S word-target and format facts

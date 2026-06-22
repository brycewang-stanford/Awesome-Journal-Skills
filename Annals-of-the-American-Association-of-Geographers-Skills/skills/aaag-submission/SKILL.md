---
name: aaag-submission
description: Use when running the final pre-submission preflight for the Annals of the American Association of Geographers via ScholarOne Manuscripts — area/article-type selection, double-anonymous preparation, the 11,000-word inclusive cap, Chicago style, keywords, ORCID, and declarations. Final checks; it does not draft content.
---

# Submission Preflight (aaag-submission)

The last check before pressing submit on **ScholarOne Manuscripts**. The Annals is **double-anonymous**
and caps almost everything against the word limit, so the two most common avoidable failures are an
under-anonymized manuscript and an over-length one. Verify volatile specifics on the official pages
before relying on them (检索于 2026-06；以官网为准).

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects, or which area/type to pick
- Confirming the chosen type's cap is met and the manuscript is properly anonymized

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** American Association of Geographers (AAG) / **Taylor & Francis (Routledge)**.
- **Portal:** **ScholarOne Manuscripts** (via the Taylor & Francis journal page).
- **Review model:** **double-anonymous** for Articles, Special Issues, Forums, and Commentaries — by
  **one to three referees, one of which is the editor or a designate**. **Commentary Responses** get
  **single-anonymous** review. Anonymize the manuscript; provide a separate title page.
- **Areas (four + a cross-track):** declare one — **Geographic Methods; Human Geography; Nature and
  Society; Physical Geography, Earth, and Environmental Sciences** — plus a **General Geography /
  cross-disciplinary** track. A **subject editor leads each area** (plus a **Cartography Editor**), all
  on **four-year terms**; your area routes the manuscript. **Current area editors (verified 2026-06-22
  via AAG announcements):** Human Geography — **Paul Adams** (since Jan 2024); Nature and Society —
  **Brian King** (since Jan 2024); General Geography / cross-discipline — **Rachel Franklin** (since
  Jan 2025); Physical Geography, Earth & Environmental Sciences — **Michaela Buenemann** (since Jan
  2025); Geographic Methods — **Anthony Howell** (since Jan 2026). Re-confirm on the AAG page, as terms rotate.
- **Article types & caps:** **Article (regular) ≤ 11,000 words** (incl. abstract, references, notes,
  tables, figure captions); **Forum** intro 2,500 + papers 5,000 each, ≤ 25,000 total; **Commentary**
  < 2,000 incl. references; **Special-Issue papers ~5,000 words**. (检索于 2026-06；以官网为准)
- **Style:** **Chicago Manual of Style, author-date**; abstract + **3-5 italicized, alphabetized keywords**.
- **ORCID:** provide for authors (Taylor & Francis standard; verify requirement).
- **Fee:** no submission fee stated for standard articles; any open-access APC handled by Taylor &
  Francis after acceptance (待核实).

## Preflight checklist

### Area, type & length
- [ ] Area declared (Geographic Methods / Human / Nature and Society / Physical, Earth & Environmental / General-cross)
- [ ] Article type chosen and its cap met (Article ≤ 11,000 / Forum ≤ 25,000 / Commentary < 2,000 / Special-Issue ~5,000)
- [ ] Total word count **includes** abstract, references, notes, tables, and figure captions
- [ ] Abstract present + **3-5 keywords**, italicized and alphabetized at the abstract's end

### Anonymity (double-anonymous)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] No obvious self-references; self-citations neutralized
- [ ] Identifying **file metadata stripped**; study-site detail not de-anonymizing
- [ ] Separate (non-anonymous) title page prepared as a distinct file

### Format, exhibits & metadata
- [ ] Chicago author-date formatting; consistent reference list
- [ ] Maps/figures meet **Graphics Guidelines** (projection, legend, resolution) — see `aaag-tables-figures`
- [ ] ORCID ready; cover letter notes the area and contribution

### Compliance & data
- [ ] Ethics / IRB / consent and **geoprivacy** handled (see `aaag-transparency-and-data`)
- [ ] Data-availability statement drafted; provenance + CRS documented
- [ ] Original work; preprint status checked against Taylor & Francis policy; AI-use policy reviewed

## Geography-specific anonymity trap

Double-anonymous review is harder in geography because the **study site can identify the author**. A
single-county study by the only group working there, named field stations, or distinctive local data can
de-anonymize as effectively as a name in the header. Mitigations:

- Generalize identifying site descriptors where the argument allows ("a mid-sized county in the US
  Southeast" rather than naming a tiny home county) — or note the unavoidable in the cover letter.
- Cite your own prior fieldwork in that site in the third person; strip acknowledgments to funders/locals.
- Remove GPS metadata and identifying coordinates from figures and attached files.

## File set for ScholarOne (verify current requirements)

- Anonymized main manuscript (no identifiers, clean metadata)
- Separate, non-anonymous title page (authors, affiliations, ORCID, acknowledgments)
- Figures/maps at required resolution per the Graphics Guidelines
- Cover letter (area, contribution, fit); data-availability statement; any supplementary materials

## Anti-patterns

- Counting only the body and overrunning once captions/notes/tables/refs are added
- Leaving author identifiers in text, acknowledgments, study-site detail, or file metadata
- Submitting to the wrong area (lands with the wrong editor/reviewers)
- Non-Chicago citations; missing or non-italicized keywords
- Maps that fail the Graphics Guidelines (projection/legend/resolution)

## Output format

```
【Area / type】GeogMethods/Human/Nature&Society/Physical-Earth-Env/General-cross · Article/Forum/Commentary/Special-Issue (cap met? Y/N)
【Word count】total incl. abstract/refs/notes/tables/captions vs. cap
【Anonymized】text + self-refs + metadata + study-site detail clean? [Y/N]
【Style】Chicago author-date + 3-5 italicized keywords? [Y/N]
【Data/ethics】geoprivacy + IRB + data-availability statement? [Y/N]
【Next】await decision → aaag-rebuttal on revision
```

## Supplementary resources

- [`./templates/checklist.md`](./templates/checklist.md) — copy-paste preflight checklist
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Annals/AAG/Taylor & Francis URLs behind every fact

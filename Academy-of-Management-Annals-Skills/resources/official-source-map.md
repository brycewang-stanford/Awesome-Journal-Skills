# Academy of Management Annals Official Source Map

Primary source map for facts used in the Annals skill pack. **Access date: 2026-06.** Proposal rules, deadlines, review mode, fees, AI policy, house style and the editors were **re-verified 2026-11-24** against the live aom.org pages (Submitting to Annals, the Annals editorial-team page, the AOM Editorial Style Guide). journals.aom.org and support.aom.org answer automated clients with HTTP 403 from this environment, so the journal platform home and the Annals FAQ were not read live on 2026-11-24. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://journals.aom.org/journal/annals** — official page used to verify or re-check Annals scope, submission, policy, or author guidance. Access date: 2026-06 (HTTP 403 to automated access on 2026-11-24).
- **https://aom.org/research/publishing-with-aom/author-resources** — official page used to verify or re-check Annals scope, submission, policy, or author guidance. Access date: 2026-06; re-read 2026-11-24 (live).

## Sources re-read 2026-11-24

| URL | Access method | What it verifies |
|-----|---------------|------------------|
| https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/submitting-to-annals/ | live page (curl) | Two issues a year (January, July); proposal deadlines **April 1 and October 1**; proposal decisions about six weeks after the deadline; proposal-first route (no unsolicited full manuscripts); proposals **no longer than 5 pages, single-spaced, 1-inch margins, 12-point font**, references and tables/figures not counted; four required headings (Focus of the review / Related reviews / Review scope and process / New insights); proposals **double-blind** peer-reviewed by the Associate Editors, invited papers then reviewed only by the Associate Editor and Editor; portal https://mc.manuscriptcentral.com/aomannals; **AOM does not charge any fees for author submissions**; AI use disclosed in the cover letter and the article acknowledgements; a cover letter is "not required" but recommended; contact editors Gary Ballinger and Cristina Gibson |
| https://www.aom.org/publications/journals/annals/annals-editorial-team/ | live page (curl) | Editors Gary A. Ballinger (University of Virginia) and Cristina Gibson (Pepperdine University); Managing Editor Stacey Victor |
| https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/author-resources-editorial-style-guides/ | live page (curl) | AOM Editorial Style Guide: Word files, Times New Roman 12 pt, double-spaced body; abstract of **no more than 200 words** with the title on page 2; title page only for accepted papers; footnotes (no endnotes); three levels of bold headings |

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: commissioned and high-level reviews that synthesize management and organization research | Official journal home / author instructions |
| Publisher / owner: Academy of Management (journals.aom.org) | Official journal home |
| Submission route: Academy of Management submission | Author instructions or submission portal |
| Sibling boundary: Academy of Management Review, Journal of Management, Journal of Management Studies, and Annual Review outlets | Inferred from journal scope and local repository taxonomy |
| integrative review | Official pages above; re-check live before submission |
| theory synthesis | Official pages above; re-check live before submission |
| agenda setting | Official pages above; re-check live before submission |
| management field map | Official pages above; re-check live before submission |

## Verified on official pages (re-verified 2026-11-24)

- **Current Editors (Co-Editors-in-Chief): Gary A. Ballinger (University of Virginia, McIntire) and Cristina Gibson (Pepperdine University)**, serving through 2027; this team began receiving proposals on 1 April 2025. Published by the **Academy of Management**. (Verified 2026-06-22 via the AOM Annals current-editorial-team page, <https://aom.org/research/journals/annals/annals-current-editorial-team>, and the UVA McIntire profile confirming Ballinger as Annals Co-Editor-in-Chief through 2027; re-verified 2026-11-24 on the AOM editorial-team and Submitting-to-Annals pages, which name Ballinger and Gibson as the editors.)
  - **STALE-FIX (2026-06-22):** an earlier version of this map listed **Matthew A. Cronin and Elizabeth George** as the editors. They were the **prior** Annals editorial team and have been superseded by Ballinger and Gibson. Do not name Cronin/George as current.
  - **STALE-FIX (2026-11-24):** the submission skill said Annals is "published with Taylor & Francis"; the official AOM pages present Annals as an AOM journal on AOM's own platform (journals.aom.org) and make no mention of Taylor & Francis.
- **Proposal-first submission:** twice-yearly proposal deadlines (April 1 and October 1); Annals does **not** accept unsolicited full manuscripts — authors submit a proposal (≤5 pages, single-spaced, 1-inch margins, 12-point font; references, tables and figures excluded) and, if accepted, are invited to submit a full article. Decisions on proposals arrive about six weeks after the deadline.
- **Review:** proposals are double-blind (Associate Editors); an accepted proposal's full paper forgoes double-blind review and is read by the Associate Editor and Editor.
- **Fees:** AOM does not charge any fees for author submissions.
- **AI policy:** work must be the authors' own; any AI use is disclosed in the cover letter and in the article acknowledgements, and authors confirm they have read AOM's AI policy.
- **House style:** AOM Editorial Style Guide (abstract ≤200 words; Times New Roman 12 pt, double-spaced Word file for manuscripts).

## Unverified / volatile items

- The time allowed to develop the invited full review (previously given as ~3 months) and the ~50-page length norm for full reviews were not stated on the pages readable on 2026-11-24 — **待核实** (the Annals FAQ at support.aom.org returned HTTP 403).
- Exact **OA charge** for an accepted article — **待核实**.
- CV requirement at submission — **待核实**.
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Academy of Management Annals",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 5, "source": "https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/submitting-to-annals/", "note": "PROPOSAL stage (the only unsolicited submission): single-spaced, 1-inch margins, 12-point font; references, tables and figures not counted; invited full reviews have no stated page limit"},
    "page_limit_includes_references": {"value": false, "source": "https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/submitting-to-annals/"},
    "abstract_words_max": {"value": 200, "source": "https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/author-resources-editorial-style-guides/", "note": "AOM Editorial Style Guide, applies to full manuscripts; a proposal carries a brief description in the portal field"},
    "review_mode": {"value": "double-blind", "source": "https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/submitting-to-annals/", "note": "proposals are double-blind (Associate Editors); the invited full paper is reviewed only by the Associate Editor and Editor, not double-blind"},
    "cover_letter": {"value": "optional", "source": "https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/submitting-to-annals/", "note": "not required but recommended; carries any AI-use disclosure"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/submitting-to-annals/", "note": "if AI was used: disclose in the cover letter and in the article acknowledgements"},
    "llm_policy": {"value": "work must be created by the authors, not AI, unless appropriate to the research question and cited; disclose AI use in the cover letter and acknowledgements; confirm reading AOM's AI policy", "source": "https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/submitting-to-annals/"},
    "submission_fee": {"value": "none (AOM does not charge any fees for author submissions)", "source": "https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/submitting-to-annals/"},
    "portal": {"value": "ScholarOne: https://mc.manuscriptcentral.com/aomannals (the only valid submission channel)", "source": "https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/submitting-to-annals/"},
    "reference_style": {"value": "AOM Editorial Style Guide", "source": "https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/author-resources-editorial-style-guides/"},
    "apc": {"value": null, "note": "not stated on the pages readable as of 2026-11-24"}
  }
}
```

# Journal of Management Studies Official Source Map

Primary source map for facts used in the JMS skill pack. **Access date: 2026-06.** Length, abstract, keyword, anonymity, AI-transparency and cover-letter rules and the General Editors were **re-verified 2026-11-24** against the journal's own site, journalofmanagementstudies.ac.uk (operated by SAMS), and the Wiley-hosted Manuscript Preparation Guidelines PDF. Wiley Online Library HTML pages (journal home, author guidelines) and socadms.org.uk answer automated clients with HTTP 403 from this environment, so they were not read live on 2026-11-24. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://onlinelibrary.wiley.com/journal/14676486** — official page used to verify or re-check JMS scope, submission, policy, or author guidance. Access date: 2026-06 (HTTP 403 to automated access on 2026-11-24).
- **https://onlinelibrary.wiley.com/page/journal/14676486/homepage/forauthors.html** — official page used to verify or re-check JMS scope, submission, policy, or author guidance. Access date: 2026-06 (HTTP 403 on 2026-11-24).

## Sources re-read 2026-11-24

| URL | Access method | What it verifies |
|-----|---------------|------------------|
| https://journalofmanagementstudies.ac.uk/publish/author-guidance/manuscript-preparation-guidelines/ | live page (curl) | UK or US English, consistent; double-spaced throughout; word count of **10,000–13,000** includes tables, figures and references (supplements excluded) and over-length new submissions may be returned; names off the manuscript, separate title page; abstract of **no more than 200 words**; **4–6 keywords** in alphabetical order; AI use declared and detailed, preferably in the data or methods section; endnotes only; Roman-numeral tables; author–date references |
| https://journalofmanagementstudies.ac.uk/publish/submit-to-jms/submit-journal-articles/ | live page (curl) | Original and Review Articles via ScholarOne (mc.manuscriptcentral.com/jmstudies); **10,000–13,000 words is typical; Original or Review Articles exceeding 15,000 words may be returned for reduction**; a **cover letter is required** (contribution to JMS debates, AI-use compliance statement — including a statement if no AI was used — prior use of the data, people already familiar with the paper) |
| https://journalofmanagementstudies.ac.uk/publish/author-guidance/the-review-process/ | live page (curl) | Double-blind peer review; desk screen then three reviewers; decision aimed within three months |
| https://journalofmanagementstudies.ac.uk/about-jms/editors/ | live page (curl) | Three General Editors: **Mirko Benischke** (Rotterdam School of Management, Erasmus University), **Johann Fortwengel** (King's College London), **Kristina Potočnik** (University of Edinburgh); Corinne Post listed as General Editor 2023–2026 (past) |
| https://onlinelibrary.wiley.com/pb-assets/assets/14676486/JMS-Manuscript-Preparation-Guidelines-2024-1703285166.pdf | live PDF (curl + pdftotext) | Same preparation rules (abstract ≤200 words, 4–6 alphabetical keywords, inclusive word count, AI transparency, endnotes, author–date references) |

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: management and organization studies, strategy, entrepreneurship, innovation, OB, and critical perspectives | Official journal home / author instructions |
| Publisher / owner: Wiley for the Society for the Advancement of Management Studies | Official journal home |
| Submission route: Wiley online submission | Author instructions or submission portal |
| Sibling boundary: Journal of Management, Organization Studies, AMJ, AMR, and Strategic Management Journal | Inferred from journal scope and local repository taxonomy |
| theoretical pluralism | Official pages above; re-check live before submission |
| organization studies | Official pages above; re-check live before submission |
| critical boundary | Official pages above; re-check live before submission |
| international management | Official pages above; re-check live before submission |

## Verified on official pages (re-verified 2026-11-24)

- **Team-based General Editors (no single EiC): Mirko Benischke (Rotterdam School of Management, Erasmus University), Johann Fortwengel (King's College London), and Kristina Potočnik (University of Edinburgh).** Re-verified 2026-11-24 on the JMS editors page. **STALE-FIX (2026-11-24):** the 2026-06-22 version of this map listed Corinne Post in place of Benischke; the editors page now lists Post as General Editor 2023–2026. Official journal of the **Society for the Advancement of Management Studies (SAMS)**, published by **Wiley**; editorial office at Durham University (business.jms@durham.ac.uk). Re-verify before submission as the General Editor team rotates.
- **Review:** double-blind; author details only on a separate title page.
- **Length:** 10,000–13,000 words is typical, inclusive of tables, figures and references; new submissions over the stated length without justification may be returned, and Original or Review Articles over 15,000 words may be returned for reduction.
- **Abstract and keywords:** abstract of no more than 200 words; 4–6 keywords in alphabetical order.
- **Cover letter (required):** contribution to JMS debates with reference to specific JMS papers, AI-use compliance (state it even if no AI was used), prior use of the same data, and people already familiar with the paper.
- **AI transparency:** any AI use (including copy-editing) declared and detailed in the manuscript, preferably in the data or methods section, and in the cover letter.
- **Portal:** ScholarOne, mc.manuscriptcentral.com/jmstudies.

## Unverified / volatile items

- **OA charge** (Wiley hybrid APC) and any submission fee — not stated on the journal's own pages; the Wiley author-guidelines page was unreachable (HTTP 403) on 2026-11-24; **待核实**.
- Point–CounterPoint and JMS Says length rules quoted in the skills were not re-read on 2026-11-24; **待核实**.
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of Management Studies",
  "verified": "2026-11-24",
  "rules": {
    "total_words_max": {"value": 13000, "soft": true, "source": "https://journalofmanagementstudies.ac.uk/publish/author-guidance/manuscript-preparation-guidelines/", "note": "10,000-13,000 words is typical, including tables, figures and references (supplements excluded); Original or Review Articles over 15,000 words may be returned for reduction"},
    "abstract_words_max": {"value": 200, "source": "https://journalofmanagementstudies.ac.uk/publish/author-guidance/manuscript-preparation-guidelines/"},
    "keywords_required": {"value": true, "source": "https://journalofmanagementstudies.ac.uk/publish/author-guidance/manuscript-preparation-guidelines/", "note": "in alphabetical order below the abstract"},
    "keywords_min": {"value": 4, "source": "https://journalofmanagementstudies.ac.uk/publish/author-guidance/manuscript-preparation-guidelines/"},
    "keywords_max": {"value": 6, "source": "https://journalofmanagementstudies.ac.uk/publish/author-guidance/manuscript-preparation-guidelines/"},
    "review_mode": {"value": "double-blind", "source": "https://journalofmanagementstudies.ac.uk/publish/author-guidance/the-review-process/", "note": "author details on a separate title page only"},
    "cover_letter": {"value": "required", "source": "https://journalofmanagementstudies.ac.uk/publish/submit-to-jms/submit-journal-articles/", "note": "contribution to JMS debates, AI-use compliance (even if none), prior use of data, people familiar with the paper"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://journalofmanagementstudies.ac.uk/publish/author-guidance/manuscript-preparation-guidelines/", "note": "any AI use, including copy-editing, declared and detailed in the manuscript (preferably data/methods section) and in the cover letter"},
    "llm_policy": {"value": "be transparent and specific about AI use in any form, including copy-editing; detail it in the manuscript and confirm compliance with the JMS AI policy in the cover letter", "source": "https://journalofmanagementstudies.ac.uk/publish/submit-to-jms/submit-journal-articles/"},
    "language": {"value": "UK or US English, consistent throughout", "source": "https://journalofmanagementstudies.ac.uk/publish/author-guidance/manuscript-preparation-guidelines/"},
    "reference_style": {"value": "JMS author-date style (alphabetical list; quoted article titles; page numbers as p.12)", "source": "https://journalofmanagementstudies.ac.uk/publish/author-guidance/manuscript-preparation-guidelines/"},
    "portal": {"value": "ScholarOne: mc.manuscriptcentral.com/jmstudies", "source": "https://journalofmanagementstudies.ac.uk/publish/submit-to-jms/submit-journal-articles/"},
    "apc": {"value": null, "note": "Wiley hybrid OA charge not stated on the pages readable as of 2026-11-24"}
  }
}
```

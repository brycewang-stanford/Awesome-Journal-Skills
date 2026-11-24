# Journal of Management Official Source Map

Primary source map for facts used in the JOMgmt skill pack. **Access date: 2026-06.** Length, title/abstract caps, review mode, reporting requirements, the AI policy and the editor were **re-verified 2026-11-24**. SAGE's journals.sagepub.com HTML pages answer automated clients with HTTP 403 from this environment, so the author-instructions page was read via search-engine rendering restricted to journals.sagepub.com (2026-11-24) and corroborated against the Internet Archive snapshot of 2025-07-07; the JOM Style Guide and the Reporting Requirements for Quantitative Submissions are SAGE-hosted PDFs and were read live. The Southern Management Association site (smgmt.org) showed only a "coming soon" placeholder on 2026-11-24. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://journals.sagepub.com/home/jom** — official page used to verify or re-check JOMgmt scope, submission, policy, or author guidance. Access date: 2026-06 (HTTP 403 to automated access on 2026-11-24).
- **https://journals.sagepub.com/author-instructions/JOM** — official page used to verify or re-check JOMgmt scope, submission, policy, or author guidance. Access date: 2026-06; re-read 2026-11-24 via search-engine rendering and the Internet Archive (live page returns HTTP 403).

## Sources re-read 2026-11-24

| URL | Access method | What it verifies |
|-----|---------------|------------------|
| https://journals.sagepub.com/author-instructions/JOM | search-engine rendering (journals.sagepub.com only) + Internet Archive snapshot 2025-07-07 | **50-page limit** that includes all notes, references, tables and figures; papers that greatly exceed 50 pages, are single-spaced, or use footnotes instead of conventional referencing are returned unreviewed; **initial (first) submissions may not include any online supplement material**; anonymized data transparency table for data overlap, described in the letter to the Editor; files in Microsoft Word; adherence to the JOM Style Guide; JOM AI policy (disclose tool and use in the Methods section of all versions); submission queries go to Editor-in-Chief **Chris Rosen** |
| https://journals.sagepub.com/pb-assets/cmscontent/JOM/JOM_Style_Guide_revised_2024-1705959439.pdf | live PDF (curl + pdftotext) | 12-point Times New Roman, double-spaced throughout, 1-inch margins; length **limited to 50 pages inclusive of references, non-supplementary appendices, tables and figures**; portal fields for a **title (limit 15 words)** and an **abstract (limit 250 words)** — the abstract is not placed in the main document; no title page in the main document; blind review with author information in a separate upload; acknowledgements typed into the portal, not the manuscript; notes in a FOOTNOTES section after the references, not page-bottom footnotes; JOM's own author–date reference format (e.g., "Barney, J. 1991. ... Journal of Management, 17: 99-120.") |
| https://journals.sagepub.com/pb-assets/cmscontent/JOM/jomquantitative_submission_reporting_requirements.pdf | live PDF (curl + pdftotext) | Quantitative submissions attest that estimates carry standard errors and **precise p values (e.g., p = .072), not star notation or cutoff bands**; full correlation matrix with means, SDs, reliabilities and Ns; data-handling decisions described; post-hoc analyses labelled as exploratory |
| https://news.uark.edu/articles/82720/christopher-rosen-named-editor-in-chief-of-ft50-journal-of-management | live page, read 2026-09-14 | Christopher C. Rosen named Editor-in-Chief from 2026-07-01 |

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: management theory and empirical work across organizational behavior, strategy, HR, entrepreneurship, and research methods | Official journal home / author instructions |
| Publisher / owner: SAGE for the Southern Management Association | Official journal home |
| Submission route: SAGE / ScholarOne submission | Author instructions or submission portal |
| Sibling boundary: Academy of Management Journal, Strategic Management Journal, Organization Science, and Journal of Management Studies | Inferred from journal scope and local repository taxonomy |
| management theory contribution | Official pages above; re-check live before submission |
| multi-study design | Official pages above; re-check live before submission |
| construct validity | Official pages above; re-check live before submission |
| organizational mechanism | Official pages above; re-check live before submission |

## Verified on official pages (re-verified 2026-11-24)

- **Editor-in-Chief: Christopher C. Rosen (University of Arkansas, Sam M. Walton College of Business)** since **2026-07-01**, succeeding Cynthia E. Devers (Virginia Tech, EiC through 2026-06-30). Rosen holds the William R. & Cacilia Howard Chair in Management and previously served as JOM Associate Editor. Verified 2026-09-14 via the University of Arkansas news announcement (**https://news.uark.edu/articles/82720/christopher-rosen-named-editor-in-chief-of-ft50-journal-of-management**) and re-verified 2026-11-24: the SAGE author-instructions page (search-engine rendering) now directs submission queries to Editor-in-Chief Chris Rosen. Published by **SAGE** for the **Southern Management Association (SMA)**, 3.5-year term ending 2029-06-30.
- **Length:** a **50-page limit** inclusive of notes, references, non-supplementary appendices, tables and figures; 12-point Times New Roman, double-spaced throughout (including references and tables), 1-inch margins.
- **Title and abstract** go into portal fields: title **≤15 words**, abstract **≤250 words**; neither the abstract nor a title page goes into the main document.
- **No online supplement at first submission** — the initial submission must fit the 50 pages; supplemental files (code, output, instruments) can be requested later in review.
- **Masked (double-blind) review**; acknowledgements and peer-reviewer thanks go in the portal / letter to the Editor, not the manuscript; any data overlap is disclosed in an **anonymized data transparency table**.
- **Style:** the **JOM Style Guide** (its own author–date format with "Year." after the names and "volume: pages" — not APA 7th); notes go in a FOOTNOTES section after the references. **STALE-FIX (2026-11-24):** earlier versions of this pack said "APA (7th)".
- **Quantitative reporting:** precise p values with standard errors and test statistics — **no significance stars** or p-cutoff bands; full correlation matrix; authors attest to these requirements at submission.
- **AI policy:** if AI was used in writing, images/graphics, or data collection/analysis, disclose the tool and how it was used **in the Methods section of all versions** of the paper.
- **Fees:** the author instructions (archive copy and search rendering, 2026-11-24) mention no submission fee; whether any fee applies and the optional OA APC amount are **待核实**.

## Unverified / volatile items

- Exact **OA APC amount** — **待核实**; confirm on the SAGE JOM open-access page before relying on it.
- **Portal label/address** (ScholarOne, `mc.manuscriptcentral.com/jom`) appears in the 2025-07-07 archive copy only; re-confirm on the live page.
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of Management",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 50, "source": "https://journals.sagepub.com/pb-assets/cmscontent/JOM/JOM_Style_Guide_revised_2024-1705959439.pdf", "note": "inclusive of notes, references, non-supplementary appendices, tables and figures; 12-pt Times New Roman, double-spaced; papers greatly over 50 pages are returned unreviewed"},
    "page_limit_includes_references": {"value": true, "source": "https://journals.sagepub.com/pb-assets/cmscontent/JOM/JOM_Style_Guide_revised_2024-1705959439.pdf"},
    "title_words_max": {"value": 15, "source": "https://journals.sagepub.com/pb-assets/cmscontent/JOM/JOM_Style_Guide_revised_2024-1705959439.pdf", "note": "entered in a portal field"},
    "abstract_words_max": {"value": 250, "source": "https://journals.sagepub.com/pb-assets/cmscontent/JOM/JOM_Style_Guide_revised_2024-1705959439.pdf", "note": "entered in a portal field; the abstract is not included in the main document"},
    "review_mode": {"value": "double-blind", "source": "https://journals.sagepub.com/pb-assets/cmscontent/JOM/JOM_Style_Guide_revised_2024-1705959439.pdf", "note": "no title page or acknowledgements in the main document"},
    "significance_stars": {"value": "prohibited", "source": "https://journals.sagepub.com/pb-assets/cmscontent/JOM/jomquantitative_submission_reporting_requirements.pdf", "note": "report standard errors, test statistics and precise p values (p = .072), not stars or cutoff bands; quantitative submissions attest to this"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://journals.sagepub.com/author-instructions/JOM", "note": "if AI was used for writing, images/graphics, or data collection/analysis: name the tool and its use in the Methods section of all versions"},
    "supplement_policy": {"value": "initial (first) submissions may not include any online supplement material; everything must fit the 50 pages", "source": "https://journals.sagepub.com/author-instructions/JOM"},
    "data_code_policy": {"value": "anonymized data transparency table for any data overlap; quantitative reporting requirements attested at submission; code, output or original data may be requested during review", "source": "https://journals.sagepub.com/pb-assets/cmscontent/JOM/jomquantitative_submission_reporting_requirements.pdf"},
    "reference_style": {"value": "JOM Style Guide author-date format (e.g., 'Barney, J. 1991. Title. Journal of Management, 17: 99-120.'), not APA", "source": "https://journals.sagepub.com/pb-assets/cmscontent/JOM/JOM_Style_Guide_revised_2024-1705959439.pdf"},
    "file_format": {"value": "Microsoft Word; single 'main document' with body, references, footnotes section, tables, figures, non-supplementary appendices", "source": "https://journals.sagepub.com/author-instructions/JOM"},
    "submission_fee": {"value": null, "note": "not stated on the pages readable as of 2026-11-24"},
    "apc": {"value": null, "note": "optional OA APC amount not stated on pages readable as of 2026-11-24"}
  }
}
```

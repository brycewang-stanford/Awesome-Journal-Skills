# Official Source Map - Production and Operations Management

Access date: 2026-06-01. Author instructions, department/masthead pages and Editor-in-Chief
**re-verified 2026-11-24** by direct fetch of poms.org (pages #1, #2, #7 read in full). The SAGE
pages (#3, #4, #5, #8) returned HTTP 403 to automated clients on 2026-11-24 and were not re-read.
No rule changed; the map now also records the abstract, title and keyword limits that the skills
already used.

This map records the official sources used for Production and Operations Management (POM)
venue-specific facts. POM author rules can move between POMS, SAGE, and ScholarOne pages; reopen
the current official instructions before submission-ready advice.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.poms.org/journal/author_instructions | POMS author instructions: Manuscript Central / ScholarOne submission route, department-editor routing, double-blind preparation, 32-page limit for original and revised manuscripts, 1.5 spacing, 11-point font, 1-inch margins, e-companion handling, cover-letter expectations, same-data disclosure, and no resubmission after rejection without invitation. Re-read 2026-11-24: submission at mc.manuscriptcentral.com/poms to an appropriate Department Editor; double-blind (remove names and acknowledgments); 32 pages for original and revised manuscripts including abstract, tables, figures, appendices and references, 1.5 spaced, size 11 font, one-inch margins, numbered pages; e-companion as a separate "E-Companion" file; first page carries the title (not exceeding 25 words) and an abstract of at most 350 words with no formulas, references or abbreviations; at least 1 and up to 6 keywords at the end of the abstract; author-year citations, alphabetical reference list; POM LaTeX template recommended; cover letter to the Department Editor must outline closely related prior work (incl. same data) and disclose any prior rejection by any POM department; copies (incl. drafts) should be removed from public websites. | 2026-11-24 |
| 2 | https://www.poms.org/journal/review_board/ | POM department/editor structure and scope: departments accept a wide range of OM research topics; papers need clear theory and practice contribution; some departments require cover-letter justification of department fit; re-read 2026-11-24: Founder and Editor-in-Chief Kalyan Singhal, Co-Editor-in-Chief Subodha Kumar (Temple), Executive Editor Jaya Singhal. | 2026-11-24 |
| 3 | https://journals.sagepub.com/home/PAO | SAGE journal home page: POM mission as the flagship research journal in operations management in manufacturing and services. | 2026-06-01 |
| 4 | https://journals.sagepub.com/author-instructions/pao | SAGE author-instructions landing page, which points authors to the full POM author guidelines. | 2026-06-01 |
| 5 | https://www.sagepub.com/shop/subscribe-to-a-journal/production-and-operations-management-203853 | SAGE publication page and journal overview, including mission and department navigation. | 2026-06-01 |
| 6 | https://www.poms.org/POMS_Ethics_for_Research_and_Publishing.pdf | POMS ethics guidance for research and publishing. | 2026-06-01 |
| 7 | https://www.poms.org/node/124 | POMS "POM Journal Editor — Kalyan Singhal" page; confirms Kalyan Singhal as founder & Editor-in-Chief. | 2026-11-24 |
| 9 | https://www.jom-hub.com/submissions/ai-policies | Shared Editorial Policies on AI agreed by the Editors-in-Chief of JOM, POM and Decision Sciences (10/11/24): disclose, justify and verify AI use; AI may not generate substantive content or be listed as an author. Hosted on the JOM site, not a POM page — context only. | 2026-11-24 |
| 8 | https://www.sagepub.com/journals/information-for-authors/publishing-options | SAGE publishing options; POM is a hybrid (Sage Choice) journal — subscription publication is free, optional open access via an APC. | 2026-06-22 |

## Verified facts used in skills

- POM is the flagship research journal of the Production and Operations Management Society, with
  SAGE journal hosting (published by SAGE since January 2024; previously Wiley-Blackwell).
- **Editor-in-Chief:** **Kalyan Singhal** (University of Baltimore), founder & Editor-in-Chief, with
  **Subodha Kumar** as Co-Editor-in-Chief. Verified 2026-06-22 via POMS (#7) and SAGE; re-check the
  live masthead at poms.org/journal before relying on it. (#7)
- **Fees / open access:** **no submission fee** stated; POM is hybrid (Sage Choice) open access —
  subscription publication is free, with an optional open-access APC if the author chooses CC-BY. The
  exact POM-specific APC figure is **待核实** (no journal-specific number confirmed on an authoritative
  page as of 2026-06-22; SAGE lists APCs per journal). (#8)
- Submissions are routed through Manuscript Central / ScholarOne and should be submitted to an
  appropriate Department Editor.
- Manuscripts are double-blind; author-identifying information must be removed from the main file
  and e-companion.
- First page: title (concise, not exceeding **25** words) and an abstract of at most **350** words
  with no formulas, references, or abbreviations; list at least **1** and up to **6** keywords at the
  end of the abstract. (#1, re-verified 2026-11-24)
- The cover letter to the Department Editor must outline closely related prior work (including papers
  using the same data or project) and disclose any prior rejection by any POM department. (#1)
- POM's Editor-in-Chief signed the Shared Editorial Policies on AI with JOM and DSJ; the POMS author
  instructions themselves do not restate an AI rule. (#9)
- Original and revised manuscripts use a 32-page limit for material intended in the main manuscript,
  including abstract, tables, figures, appendices, and references.
- The formatting baseline in the POMS instructions is 1.5 spacing, 11-point font, and 1-inch margins.
- E-companion material should be submitted as a separate file with the E-Companion designation.
- POM expects a clear contribution to both theory and practice.
- The author instructions require disclosure when the paper uses the same data as prior or
  contemporaneous work.
- Rejected manuscripts should not be resubmitted unless the editor explicitly invites resubmission.

## Still volatile

- Department editor names, department boundaries, ScholarOne form fields, issue-specific special
  issue routes, publisher production steps, open-access charges, exact copyright forms, and any
  future SAGE/POMS policy updates.

## UNVERIFIED / 待核实

- **Open-access APC amount.** Still no POM-specific figure: the SAGE pages returned HTTP 403 on
  2026-11-24, and a search of sagepub.com found only the generic Sage Choice range, not a POM price.
- **SAGE-hosted author instructions (#4).** Not re-read on 2026-11-24 (HTTP 403); the POMS author
  instructions (#1) were used as the governing text.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Production and Operations Management",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {
      "value": 32,
      "source": "https://www.poms.org/journal/author_instructions",
      "note": "original and revised manuscripts, including abstract, tables, figures, appendices and references meant for the main manuscript; e-companion separate"
    },
    "page_limit_includes_references": {
      "value": true,
      "source": "https://www.poms.org/journal/author_instructions"
    },
    "abstract_words_max": {
      "value": 350,
      "source": "https://www.poms.org/journal/author_instructions",
      "note": "no formulas, references or abbreviations"
    },
    "title_words_max": {
      "value": 25,
      "source": "https://www.poms.org/journal/author_instructions"
    },
    "keywords_required": {
      "value": true,
      "source": "https://www.poms.org/journal/author_instructions",
      "note": "listed at the end of the abstract"
    },
    "keywords_min": {
      "value": 1,
      "source": "https://www.poms.org/journal/author_instructions"
    },
    "keywords_max": {
      "value": 6,
      "source": "https://www.poms.org/journal/author_instructions"
    },
    "required_statements": {
      "value": ["keywords"],
      "source": "https://www.poms.org/journal/author_instructions"
    },
    "review_mode": {
      "value": "double-blind",
      "source": "https://www.poms.org/journal/author_instructions",
      "note": "remove names and acknowledgments; removing public copies (incl. drafts) is highly recommended"
    },
    "cover_letter": {
      "value": "required",
      "source": "https://www.poms.org/journal/author_instructions",
      "note": "to the Department Editor: closely related prior work incl. same data/project, and any prior rejection by a POM department"
    },
    "template": {
      "value": "1.5 spaced, size 11 font, one-inch margins, numbered pages; POM LaTeX template recommended; e-companion as a separate 'E-Companion' file",
      "source": "https://www.poms.org/journal/author_instructions"
    },
    "reference_style": {
      "value": "author-year in parentheses; alphabetical reference list in POM style",
      "source": "https://www.poms.org/journal/author_instructions"
    },
    "portal": {
      "value": "ScholarOne Manuscript Central (mc.manuscriptcentral.com/poms), submitted to an appropriate Department Editor",
      "source": "https://www.poms.org/journal/author_instructions"
    },
    "preprint_policy": {
      "value": "Highly recommended to remove copies of the manuscript, including prior drafts, from publicly available websites to protect double-blind review",
      "source": "https://www.poms.org/journal/author_instructions"
    },
    "submission_fee": {
      "value": null,
      "note": "not stated on the official POMS pages as of 2026-11-24"
    },
    "apc": {
      "value": null,
      "note": "optional Sage Choice open access; POM-specific APC not stated on a page readable as of 2026-11-24"
    }
  }
}
```

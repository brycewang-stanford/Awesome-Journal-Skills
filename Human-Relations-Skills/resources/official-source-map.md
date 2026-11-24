# Human Relations Official Source Map

Primary source map for facts used in the Human Relations skill pack. **Access date: 2026-06.** Submission rules, length and abstract limits, review mode, AI and data-transparency policies, and the co-editors were **re-verified 2026-11-24** against the journal's own site (humanrelationsjournal.org: submission guidelines, the January 2026 "How to prepare your submission" PDF, the policies page, and the editorial-team page). SAGE's journals.sagepub.com pages answer automated clients with HTTP 403 from this environment, so the SAGE author-instructions page was read only as an Internet Archive copy (snapshot 2025-07-15) and used for corroboration, not as the basis of any rule. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://journals.sagepub.com/home/hum** — official page used to verify or re-check Human Relations scope, submission, policy, or author guidance. Access date: 2026-06 (HTTP 403 to automated access on 2026-11-24).
- **https://journals.sagepub.com/author-instructions/HUM** — official page used to verify or re-check Human Relations scope, submission, policy, or author guidance. Access date: 2026-06 (HTTP 403 on 2026-11-24; Internet Archive snapshot of 2025-07-15 read instead — it still described an older 45-page limit, superseded by the January 2026 PDF below).

## Sources re-read 2026-11-24

| URL | Access method | What it verifies |
|-----|---------------|------------------|
| https://www.humanrelationsjournal.org/journal/submission-guidelines/ | live page (curl) | Guidance for contributors; review papers only through the annual critical-reviews special-issue call (regular-route reviews are desk rejected); at most 2 single-authored submissions per author in any 12-month period, separated by at least 6 months; iThenticate/COPE; link to the January 2026 preparation PDF |
| https://www.humanrelationsjournal.org/wp-content/uploads/2026/01/Human-Relations-How-to-prepare-your-submission-Jan-2026-1.pdf | live PDF (curl + pdftotext) | Double-blind review; anonymise manuscript and any response letter; no acknowledgements at submission; cover letter names the HR works the paper connects to; no conflict-of-interest declaration required in the cover letter; Times New Roman 12 pt, 2.54 cm margins, double-spaced; **≤13,000 words in total, including abstract, text, endnotes, references and appendices but excluding tables and figures** (over-length or mis-formatted papers are sent back); abstract **100–200 words**; keywords = main 3 or 4 key phrases plus at least 3 or 4 more; Word docx/doc, RTF or Excel files; endnotes not footnotes; **SAGE Harvard** references; online-only supplementary files uploaded as "Supplemental Files" |
| https://www.humanrelationsjournal.org/journal/our-policies/ | live page (curl) | AI allowed only for copy-editing/proofing; AI use declared during submission and detailed in the cover letter, **not** in the manuscript; AI statement requested at acceptance; data transparency matrix when other papers use the same dataset |
| https://www.humanrelationsjournal.org/about/editorial-team/ | live page (curl) | Co-Editors-in-Chief Smriti Anand and Penny Dick |

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: work, employment, organizations, social relations, power, identity, and critical management | Official journal home / author instructions |
| Publisher / owner: SAGE for the Tavistock Institute | Official journal home |
| Submission route: SAGE / ScholarOne submission | Author instructions or submission portal |
| Sibling boundary: Organization Studies, Journal of Management Studies, Administrative Science Quarterly, and Work Employment and Society | Inferred from journal scope and local repository taxonomy |
| workplace relation | Official pages above; re-check live before submission |
| power and identity | Official pages above; re-check live before submission |
| employment institution | Official pages above; re-check live before submission |
| qualitative insight | Official pages above; re-check live before submission |

## Verified on official pages (re-verified 2026-11-24)

- Published **monthly by SAGE on behalf of the Tavistock Institute of Human Relations** (London); established 1947. (humanrelationsjournal.org / SAGE)
- **Co-Editors-in-Chief: Smriti Anand (Illinois Institute of Technology) and Penny Dick (Sheffield University Management School).** First verified 2026-06-22 and re-verified 2026-11-24 via the journal editorial-team page (<https://www.humanrelationsjournal.org/about/editorial-team/>). Re-verify before submission as the role rotates.
- **Review and anonymity:** double-blind. No author names anywhere in the manuscript, no acknowledgements (added after acceptance), self-citations in the third person, no "Author, 2006"-style placeholders, and no links to external websites in the manuscript or supplements.
- **Length:** the manuscript must not exceed **13,000 words** in total, counting the abstract, text, endnotes, references and appendices but **excluding tables and figures**. Over-length or incorrectly formatted papers are returned for reformatting.
- **Abstract and keywords:** abstract of **100–200 words**; keywords are the main 3 or 4 key phrases plus at least 3 or 4 additional key words.
- **Format:** Times New Roman 12 pt, 2.54 cm (one-inch) margins, double-spaced except tables and figures; endnotes before the references (no footnotes); references in **SAGE Harvard**.
- **AI policy:** AI may be used only for copy-editing or proofing; any use is declared during submission and detailed in the cover letter, and the manuscript itself must not contain the AI declaration.
- **Data transparency:** when other papers use the same dataset, supply them with a data transparency matrix of overlapping variables or qualitative material.
- **Conflict of interest:** Human Relations does not require a declaration of conflicting interests in the cover letter (January 2026 PDF).

## Unverified / volatile items

- Exact **submission fee / OA APC** — the journal's own pages do not state one, and the SAGE author-instructions page could not be read live on 2026-11-24 (HTTP 403); **待核实**.
- **Portal address** (`mc.manuscriptcentral.com/hr`, used in the skills): the journal site's "Portal" link is a password-protected editor portal, and the SAGE page was unreachable on 2026-11-24 — **待核实**.
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Human Relations",
  "verified": "2026-11-24",
  "rules": {
    "total_words_max": {"value": 13000, "source": "https://www.humanrelationsjournal.org/wp-content/uploads/2026/01/Human-Relations-How-to-prepare-your-submission-Jan-2026-1.pdf", "note": "counts abstract, text, endnotes, references and appendices; excludes tables and figures; over-length papers are sent back"},
    "abstract_words_max": {"value": 200, "source": "https://www.humanrelationsjournal.org/wp-content/uploads/2026/01/Human-Relations-How-to-prepare-your-submission-Jan-2026-1.pdf", "note": "abstract of between 100 and 200 words"},
    "review_mode": {"value": "double-blind", "source": "https://www.humanrelationsjournal.org/wp-content/uploads/2026/01/Human-Relations-How-to-prepare-your-submission-Jan-2026-1.pdf", "note": "no acknowledgements at submission; third-person self-citation; no external links"},
    "cover_letter": {"value": "required", "source": "https://www.humanrelationsjournal.org/wp-content/uploads/2026/01/Human-Relations-How-to-prepare-your-submission-Jan-2026-1.pdf", "note": "names the Human Relations works the paper connects to; carries any AI-use account"},
    "keywords_required": {"value": true, "source": "https://www.humanrelationsjournal.org/wp-content/uploads/2026/01/Human-Relations-How-to-prepare-your-submission-Jan-2026-1.pdf", "note": "main 3 or 4 key phrases plus at least 3 or 4 additional key words"},
    "separate_upload_statements": {"value": ["ai_use_disclosure"], "source": "https://www.humanrelationsjournal.org/journal/our-policies/", "note": "only if AI was used (copy-editing/proofing only); declared in the submission form and the cover letter; the manuscript must NOT contain the declaration"},
    "llm_policy": {"value": "AI allowed only for copy-editing or proofing; declare at submission and detail in the cover letter, not in the manuscript; undisclosed use is grounds for rejection or retraction", "source": "https://www.humanrelationsjournal.org/journal/our-policies/"},
    "data_code_policy": {"value": "if other papers use the same dataset, submit them with a data transparency matrix of overlapping variables or qualitative material", "source": "https://www.humanrelationsjournal.org/journal/our-policies/"},
    "reference_style": {"value": "SAGE Harvard (author-date; alphabetical list)", "source": "https://www.humanrelationsjournal.org/wp-content/uploads/2026/01/Human-Relations-How-to-prepare-your-submission-Jan-2026-1.pdf"},
    "file_format": {"value": "Word docx/doc or RTF; Times New Roman 12 pt, 2.54 cm margins, double-spaced; endnotes, not footnotes", "source": "https://www.humanrelationsjournal.org/wp-content/uploads/2026/01/Human-Relations-How-to-prepare-your-submission-Jan-2026-1.pdf"},
    "supplement_policy": {"value": "online-only supplementary material uploaded to the journal as 'Supplemental Files'; reviewers need not read it, so the manuscript must stand alone", "source": "https://www.humanrelationsjournal.org/wp-content/uploads/2026/01/Human-Relations-How-to-prepare-your-submission-Jan-2026-1.pdf"},
    "submission_fee": {"value": null, "note": "not stated on the journal's own pages as of 2026-11-24; SAGE page unreachable"},
    "apc": {"value": null, "note": "not stated on the journal's own pages as of 2026-11-24; SAGE page unreachable"}
  }
}
```

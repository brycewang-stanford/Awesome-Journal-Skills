# Organization Studies Official Source Map

Primary source map for facts used in the OS skill pack. **Access date: 2026-06.** Length, abstract, keyword, review-mode and reference-style rules and the Editors-in-Chief were **re-verified 2026-11-24**. SAGE's journals.sagepub.com HTML pages answer automated clients with HTTP 403 from this environment, so the SAGE author-instructions page was read via search-engine rendering restricted to journals.sagepub.com (2026-11-24) and corroborated against the Internet Archive snapshot of 2025-07-06; SAGE's PDF assets (the OS Style and Reference Guide) and the EGOS pages were read live. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://journals.sagepub.com/home/oss** — official page used to verify or re-check OS scope, submission, policy, or author guidance. Access date: 2026-06 (HTTP 403 to automated access on 2026-11-24).
- **https://journals.sagepub.com/author-instructions/OSS** — official page used to verify or re-check OS scope, submission, policy, or author guidance. Access date: 2026-06; re-read 2026-11-24 via search-engine rendering and the Internet Archive (live page returns HTTP 403).

## Sources re-read 2026-11-24

| URL | Access method | What it verifies |
|-----|---------------|------------------|
| https://journals.sagepub.com/author-instructions/OSS | search-engine rendering (journals.sagepub.com only) + Internet Archive snapshot 2025-07-06 | Research articles: maximum **13,000 words including references and appendices**; unstructured abstract of **300 words (maximum)** between title and main text; a minimum of **5–7 keywords**, **four** from the OS ScholarOne keyword list; identity transparency "double anonymized"; anonymised manuscript plus a separate Title Page carrying the "Statements and Declarations" (ethics, consent, conflicting interests, funding, data availability); cover letter; preprints accepted (archive only) |
| https://journals.sagepub.com/pb-assets/cmscontent/OSS/OS%20Style%20and%20Reference%20Guide_August%202025_rev-1760951092063.pdf | live PDF (curl + pdftotext) | From **14 August 2025** OS follows the **APA Reference Style (7th edition)** "without any exceptions"; UK or US spelling, used consistently |
| https://www.egos.org/organization_studies/os_editors_and_boards | live page (curl) | Editors-in-Chief **John Amis** (University of Edinburgh) and **Tammar B. Zilber** (Hebrew University of Jerusalem); Managing Editor Sophia Tzagaraki |
| https://www.egos.org/organization_studies/manuscript_submission_guidelines | live page (curl) | Submission via SAGE track / ScholarOne at mc.manuscriptcentral.com/orgstudies; queries to the Managing Editor |
| https://egos.org/organization_studies/OS_EiC_Call_dl_2025_11_30 | search-engine rendering | EGOS call for a new Co-Editor-in-Chief (four-year term from September 2027); search committee includes current EiCs Zilber and Amis |

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: organization theory, institutional theory, critical management, qualitative research, and process studies | Official journal home / author instructions |
| Publisher / owner: SAGE for EGOS | Official journal home |
| Submission route: SAGE / ScholarOne submission | Author instructions or submission portal |
| Sibling boundary: Administrative Science Quarterly, Organization Science, Journal of Management Studies, and Academy of Management Review | Inferred from journal scope and local repository taxonomy |
| institutional process | Official pages above; re-check live before submission |
| qualitative depth | Official pages above; re-check live before submission |
| organization theory | Official pages above; re-check live before submission |
| critical reflexivity | Official pages above; re-check live before submission |

## Verified on official pages (re-verified 2026-11-24)

- **Editors-in-Chief: John Amis (University of Edinburgh) and Tammar B. Zilber (Jerusalem School of Business, Hebrew University of Jerusalem)**, per the EGOS editors page re-read 2026-11-24 (<https://www.egos.org/organization_studies/os_editors_and_boards>) and the SAGE editorial board as rendered by search. **STALE-FIX (2026-11-24):** the previous version of this map named **Renate Meyer and Paolo Quattrone**; both are former co-EiCs (the SAGE board archived in May 2025 already showed Quattrone with Zilber). EGOS is recruiting a new Co-EiC for a term starting September 2027, so re-check the masthead before naming an editor. Managing Editor: Sophia Tzagaraki. Published by **SAGE** on behalf of **EGOS** (est. 1980).
- **Length, abstract, keywords:** research articles at most **13,000 words including references and appendices**; unstructured abstract of at most **300 words**; a minimum of **5–7 keywords**, four of them chosen from the OS ScholarOne keyword list.
- **Review:** double-anonymized; identifying information and the Statements and Declarations go on a separate Title Page that is not sent to reviewers.
- **Referencing:** **APA 7th edition**, without exceptions, since 14 August 2025 (OS Style and Reference Guide, August 2025 revision). **STALE-FIX (2026-11-24):** earlier versions of this pack said "SAGE Harvard".
- **Portal:** ScholarOne at mc.manuscriptcentral.com/orgstudies (EGOS submission page).
- **Fees / OA:** the archived SAGE page (2025-07-06) states that no fees are payable to submit or publish and that optional gold OA is available via Sage Choice for a fee; the APC figure is **待核实** and the no-fee statement was not re-read live on 2026-11-24.

## Unverified / volatile items

- Exact **OA APC amount** — **待核实** (not on the pages readable from this environment on 2026-11-24).
- "No fees to submit or publish" and the preprint policy come from the 2025-07-06 Internet Archive copy of the SAGE page; re-confirm on the live page.
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Organization Studies",
  "verified": "2026-11-24",
  "rules": {
    "total_words_max": {"value": 13000, "source": "https://journals.sagepub.com/author-instructions/OSS", "note": "research articles, including references and appendices; read via search-engine rendering (live page returns 403 to automation)"},
    "abstract_words_max": {"value": 300, "source": "https://journals.sagepub.com/author-instructions/OSS"},
    "abstract_format": {"value": "unstructured", "source": "https://journals.sagepub.com/author-instructions/OSS"},
    "keywords_required": {"value": true, "source": "https://journals.sagepub.com/author-instructions/OSS", "note": "listed after the abstract; four must come from the OS ScholarOne keyword list"},
    "keywords_min": {"value": 5, "source": "https://journals.sagepub.com/author-instructions/OSS", "note": "'a minimum of 5-7 keywords'"},
    "review_mode": {"value": "double-blind", "source": "https://journals.sagepub.com/author-instructions/OSS", "note": "SAGE 'double anonymized'"},
    "separate_upload_statements": {"value": ["ethics_approval", "informed_consent", "conflict_of_interest", "funding", "data_availability"], "source": "https://journals.sagepub.com/author-instructions/OSS", "note": "under 'Statements and Declarations' on the separate Title Page, not in the anonymised manuscript; write 'Not applicable' where relevant"},
    "reference_style": {"value": "APA 7th edition without exceptions (since 14 August 2025)", "source": "https://journals.sagepub.com/pb-assets/cmscontent/OSS/OS%20Style%20and%20Reference%20Guide_August%202025_rev-1760951092063.pdf"},
    "portal": {"value": "ScholarOne (SAGE track): mc.manuscriptcentral.com/orgstudies", "source": "https://www.egos.org/organization_studies/manuscript_submission_guidelines"},
    "submission_fee": {"value": null, "note": "the live SAGE page could not be read on 2026-11-24; the 2025-07-06 archive said no fees to submit or publish"},
    "apc": {"value": null, "note": "Sage Choice OA fee amount not stated on pages readable as of 2026-11-24"}
  }
}
```

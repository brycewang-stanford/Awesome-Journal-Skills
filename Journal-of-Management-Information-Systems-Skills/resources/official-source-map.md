# Journal of Management Information Systems Official Source Map

Primary source map for facts used in the JMIS skill pack. **Re-verified 2026-08-09.** Submission route, review mode, length and abstract limits, file and reference rules and the editor were **re-verified 2026-11-24** against the journal's own contributor page (jmis-web.org). The Taylor & Francis pages (journal home and instructions for authors) answer automated clients with HTTP 403 from this environment and have no Internet Archive capture of the instructions page, so they were not read on 2026-11-24. Re-check editor names, fees, exact length limits, portal forms, data policies, and style details before relying on them. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://www.tandfonline.com/journals/mmis20** — official page used to verify or re-check JMIS scope, submission, policy, or author guidance. Access date: 2026-06 (HTTP 403 to automated access on 2026-11-24).
- **https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=mmis20** — official page used to verify or re-check JMIS scope, submission, policy, or author guidance. Access date: 2026-06 (HTTP 403 on 2026-11-24).
- **https://jmis-web.org/info-for-contributors** — official contributor page re-checked 2026-08-09 and **re-verified 2026-11-24** (live, curl); confirms Vladimir Zwass as Editor-in-Chief, email submission to `jmis@fdu.edu` with the subject line "JMIS Submission", **double-blind** review of a fully anonymized paper (self-references may stay in the reference list), MS Word or PDF, figures and tables at the end of the same file, a separate cover letter (affiliations, addresses, brief biographies, title page with author names, funding sources), an abstract of **up to 150 words** with no citations, a set of key words and phrases, 12-point double-spaced left-justified numbered pages, a complete manuscript of **no more than 50 pages**, an optional separate online appendix, survey instruments as a separate anonymized attachment, optional reviewer nominations, and an alphabetized reference list cited by number in square brackets (e.g., [9]); authors receive 50 free e-prints.

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: information systems, digital transformation, platforms, analytics, IT governance, and organizational impacts of technology | Official journal home / author instructions |
| Publisher / owner: Taylor & Francis | Official journal home |
| Submission route: email to the Editor-in-Chief (jmis@fdu.edu), not a portal | jmis-web.org contributor page |
| Sibling boundary: MIS Quarterly, Information Systems Research, Journal of the AIS, and Management Science | Inferred from journal scope and local repository taxonomy |
| digital platform | Official pages above; re-check live before submission |
| IT governance | Official pages above; re-check live before submission |
| analytics adoption | Official pages above; re-check live before submission |
| information systems theory | Official pages above; re-check live before submission |

## Verified on official pages (re-verified 2026-11-24)

- **Editor-in-Chief: Vladimir Zwass (Fairleigh Dickinson University)** — present EiC. (jmis-web.org / Taylor & Francis)
- Original submissions go by email to `jmis@fdu.edu` (subject "JMIS Submission") with the paper and a separate cover letter as attachments; review is double-blind; the abstract is at most 150 words with no citations, followed by key words and phrases; the complete manuscript may not exceed 50 pages, with figures and tables at the end of the same file; an intention to shorten later is not accepted as a justification. (jmis-web.org contributor page)
- Revisions follow the same rules and add the responses to reviewers in a single anonymous file; accepted papers are supplied in an editable format, preferably MS Word.
- Published by **Taylor & Francis** (print and online).

## Unverified / volatile items

- **Submission fee / OA APC** — not stated on the contributor page; T&F pages unreachable on 2026-11-24; **待核实**.
- Data and code policy and any AI/LLM-use policy — not stated on the contributor page; **待核实**.
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of Management Information Systems",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 50, "source": "https://jmis-web.org/info-for-contributors", "note": "the complete manuscript, with figures and tables at the end of the same file; 12-point, double-spaced"},
    "page_limit_includes_references": {"value": true, "source": "https://jmis-web.org/info-for-contributors", "note": "limit applies to the complete MS"},
    "abstract_words_max": {"value": 150, "source": "https://jmis-web.org/info-for-contributors", "note": "no citations in the abstract"},
    "keywords_required": {"value": true, "source": "https://jmis-web.org/info-for-contributors", "note": "a set of key words and phrases"},
    "review_mode": {"value": "double-blind", "source": "https://jmis-web.org/info-for-contributors", "note": "paper and file fully anonymized; self-references may stay in the reference list"},
    "cover_letter": {"value": "required", "source": "https://jmis-web.org/info-for-contributors", "note": "separate attachment with affiliations, contact details, brief bios, and the title page naming authors and funding sources"},
    "separate_upload_statements": {"value": ["funding"], "source": "https://jmis-web.org/info-for-contributors", "note": "funding sources acknowledged on the title page inside the cover letter, not in the anonymized paper"},
    "portal": {"value": "email to jmis@fdu.edu with subject 'JMIS Submission' (no web portal)", "source": "https://jmis-web.org/info-for-contributors"},
    "file_format": {"value": "MS Word or PDF; 12-point, double-spaced, left-justified, numbered pages; figures and tables at the end of the same file", "source": "https://jmis-web.org/info-for-contributors"},
    "reference_style": {"value": "alphabetized, numbered reference list cited by number in square brackets, e.g. [9]", "source": "https://jmis-web.org/info-for-contributors"},
    "supplement_policy": {"value": "online appendix may be supplied as a separate file; survey instruments not in the paper go as a separate anonymized attachment", "source": "https://jmis-web.org/info-for-contributors"},
    "submission_fee": {"value": null, "note": "not stated on the official pages readable as of 2026-11-24"},
    "llm_policy": {"value": null, "note": "not stated on the official pages readable as of 2026-11-24"}
  }
}
```

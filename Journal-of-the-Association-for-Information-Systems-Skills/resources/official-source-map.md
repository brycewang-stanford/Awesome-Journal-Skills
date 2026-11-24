# Journal of the Association for Information Systems Official Source Map

Primary source map for facts used in the JAIS skill pack. **Re-verified 2026-08-09.** Length limits, review mode, cover-letter contents, the generative-AI transparency document, reference style, data policy, open-access terms and the editor were **re-verified 2026-11-24** against the live AIS eLibrary pages (journal home, About, Information for Authors, Format, Policies, Editorial Board) and the JAIS Style Guide PDF; all were reachable directly. Re-check editor names, fees, exact length limits, portal forms, data policies, and style details before relying on them. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://aisel.aisnet.org/jais/** — official page used to verify or re-check JAIS scope, submission, policy, or author guidance. Access date: 2026-06; re-read 2026-11-24 (Editor-in-Chief Monideepa Tarafdar, University of Massachusetts Amherst).
- **https://aisel.aisnet.org/jais/policies.html** — official page used to verify or re-check JAIS scope, submission, policy, or author guidance. Access date: 2026-06; re-read 2026-11-24 (AIS Green Open Access with no embargo; data available on request to Senior Editors/reviewers; for variance-based methods at minimum the covariance or correlation matrix plus descriptives; dataset reuse must be disclosed and justified; copyright transferred to AIS; appeals 2–10 weeks after the decision).
- **https://aisel.aisnet.org/jais/format.html** — official format page re-checked 2026-08-09 and 2026-11-24; confirms the ScholarOne review-system route, English-language requirement, double-blind review, cover-letter disclosure expectations, and empirical-data validation expectations. It still says "APA 6th edition" and mentions suggesting two reviewers; both are superseded by the Information for Authors page below.
- **https://aisel.aisnet.org/jais/authorinfo.html** — "JAIS Manuscript Categories and Information for Authors", read live 2026-11-24: Research Articles, Theory, Literature Review and Foundational Research manuscripts **over 15,000 words** are very likely to receive extra scrutiny and may be returned to be shortened; Research Perspectives about **10,000** words; Editorials **6000-8000** words; Policy and Impact research articles **5,000-7,000** words; manuscripts that exceed **65 pages including everything** will not be sent out for review; double-spaced Times New Roman 12 pt; **APA (7th ed.)** references; double-blind review; submission at http://mc.manuscriptcentral.com/jais; English; required cover letter giving the manuscript category, the word count including references and appendices, **2-3** potential Senior Editors and all conflicted Senior Editors, closely related research, and any prior JAIS submission history; the cover letter must **not** suggest reviewers; a **Generative AI transparency document** appended to the cover letter on a separate page for every new and revised submission; at least one author must be an **AIS member**.
- **https://aisel.aisnet.org/jais/editorialboard.html** — Editorial Board, read live 2026-11-24 (Editor-in-Chief Monideepa Tarafdar).
- **https://aisel.aisnet.org/jais/JAIS_Style.pdf** — JAIS Style Guide (revision dated March 19, 2021), read live 2026-11-24: review copies double-spaced in Times New Roman 12 pt; numbered section headings (max three levels); APA Publication Manual 7th edition with JAIS exceptions (no routine DOIs).

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: information systems theory, digital innovation, sociotechnical systems, methods, and cumulative IS scholarship | Official journal home / author instructions |
| Publisher / owner: Association for Information Systems | Official journal home |
| Submission route: ScholarOne (mc.manuscriptcentral.com/jais) | Information for Authors page |
| Sibling boundary: MIS Quarterly, Information Systems Research, JMIS, and Management Science | Inferred from journal scope and local repository taxonomy |
| sociotechnical system | Official pages above; re-check live before submission |
| IS theory | Official pages above; re-check live before submission |
| digital innovation | Official pages above; re-check live before submission |
| methodological pluralism | Official pages above; re-check live before submission |

## Verified on official pages (re-verified 2026-11-24)

- **Editor-in-Chief: Monideepa Tarafdar** (University of Massachusetts Amherst; effective 2024-09-01). (AIS announcement / JAIS editorial board, re-read 2026-11-24)
- Published by the **Association for Information Systems (AIS)**; **AIS Green Open Access** (authors may self-archive the accepted paper with no embargo), and JAIS articles are free to AIS members. Submission is through the JAIS ScholarOne review system.
- Review is double-blind; SEM manuscripts supply a full correlation/covariance matrix in an appendix, and editors/reviewers may request the dataset for validation as a condition of publication.
- **Length:** over 15,000 words (Research Articles, Theory, Literature Review, Foundational Research) invites extra scrutiny and possible return; more than 65 pages including everything is not sent out for review.
- **Reference style: APA 7th edition.** **STALE-FIX (2026-11-24):** earlier versions of this pack said APA 6th, following the older Format page; the Information for Authors page and the JAIS Style Guide both specify the 7th edition.
- **Cover letter (required):** category, word count including references and appendices, 2-3 nominated Senior Editors plus every conflicted Senior Editor, closely related research and dataset reuse, prior JAIS submission history, and the **Generative AI transparency document** on a separate page. **STALE-FIX (2026-11-24):** the cover letter must **not** suggest reviewers (letters that do are returned); earlier versions of this pack advised naming two reviewers.
- At least one author must be an AIS member.

## Unverified / volatile items

- **Abstract word limit and keyword count** — not stated on the pages read 2026-11-24; **待核实**.
- Any processing charge — none is stated (Green OA model); confirm before relying on "no APC".
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of the Association for Information Systems",
  "verified": "2026-11-24",
  "rules": {
    "total_words_max": {"value": 15000, "soft": true, "source": "https://aisel.aisnet.org/jais/authorinfo.html", "note": "Research Articles, Theory, Literature Review, Foundational Research: over 15,000 words invites extra scrutiny and possible return; Research Perspectives ~10,000; Editorials 6000-8000; Policy and Impact 5,000-7,000; the cover letter reports the count including references and appendices"},
    "main_text_pages_max": {"value": 65, "source": "https://aisel.aisnet.org/jais/authorinfo.html", "note": "65 pages including everything; longer manuscripts are not sent out for review"},
    "page_limit_includes_references": {"value": true, "source": "https://aisel.aisnet.org/jais/authorinfo.html"},
    "review_mode": {"value": "double-blind", "source": "https://aisel.aisnet.org/jais/authorinfo.html"},
    "cover_letter": {"value": "required", "source": "https://aisel.aisnet.org/jais/authorinfo.html", "note": "category, word count, 2-3 Senior Editor nominations and conflicted SEs, related research, prior history; must NOT suggest reviewers"},
    "separate_upload_statements": {"value": ["ai_use_disclosure"], "source": "https://aisel.aisnet.org/jais/authorinfo.html", "note": "Generative AI transparency document appended to the cover letter on a separate page, for every new and revised submission"},
    "reference_style": {"value": "APA 7th edition (JAIS Style Guide exceptions: no routine DOIs)", "source": "https://aisel.aisnet.org/jais/authorinfo.html"},
    "language": {"value": "English", "source": "https://aisel.aisnet.org/jais/authorinfo.html"},
    "file_format": {"value": "double-spaced, Times New Roman 12 pt; body limited to text, tables and figures and must stand alone; appendices may be separate files", "source": "https://aisel.aisnet.org/jais/authorinfo.html"},
    "portal": {"value": "ScholarOne: mc.manuscriptcentral.com/jais", "source": "https://aisel.aisnet.org/jais/authorinfo.html"},
    "data_code_policy": {"value": "SEM papers include the full correlation or covariance matrix (plus descriptives) in an appendix; datasets available on request to editors/reviewers, as a condition of publication if requested; dataset reuse disclosed and justified", "source": "https://aisel.aisnet.org/jais/policies.html"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"},
    "apc": {"value": null, "note": "no charge stated (AIS Green Open Access) as of 2026-11-24"}
  }
}
```

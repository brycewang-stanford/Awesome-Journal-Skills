# European Economic Review (EER) Official Source Map

Primary source map for EER-specific facts used in this pack. **Access date for all entries: 2026-06.**
Submission fee, review model, abstract / keyword / highlights rules and the AI-declaration policy
**re-verified 2026-11-24**: every ScienceDirect and elsevier.com page refuses automated access (HTTP 403 to
curl and WebFetch), so the guide for authors was **read via search-engine rendering** restricted to
sciencedirect.com / elsevier.com; the Editorial Manager portal loads but renders its content by script. Changes
found on 2026-11-24: the guide states an **abstract of no more than 250 words**, **1 to 7 keywords**, a
**single anonymized** review process, **research highlights encouraged** (3–5 bullets, at most 85 characters
each, separate file) rather than mandatory, and that authors **must declare generative-AI use at submission**.
The fee schedule (EUR 125 / 100 / 50 / waiver) is **unchanged**. The editor roster could **not** be
re-confirmed (see the unverified list). Re-check volatile facts before submission; items that require live confirmation are marked **待核实**.

## Official pages

- **https://www.sciencedirect.com/journal/european-economic-review** — EER journal home on ScienceDirect / Elsevier. Used for publisher, journal scope, ISSN, and article information.
- **https://www.sciencedirect.com/journal/european-economic-review/about/editorial-board** — EER editorial board on ScienceDirect (WebFetch 403; verified via Elsevier editorial-board listing + cross-source search, 2026-06-22).
- **https://www.editorialmanager.com/eerev** — EER Editorial Manager submission portal.
- **https://www.elsevier.com/journals/european-economic-review/0014-2921/guide-for-authors** — Elsevier guide for authors. Used for submission files, declarations, highlights, data/code statements, and formatting expectations.
- **https://www.sciencedirect.com/journal/european-economic-review/publish/guide-for-authors** — current ScienceDirect copy of the guide for authors (read via search-engine rendering 2026-11-24; direct access HTTP 403). Verifies: **single anonymized** review; concise factual abstract of **no more than 250 words**; **1 to 7** keywords; highlights encouraged (**3–5** bullets, at most **85** characters each, separate file); non-refundable **EUR 125** submission fee (EUR 100 PhD-student contact author, EUR 50 Research4Life Group B, waiver for Group A; VAT added for European authors; submissions considered only after payment); authors must **declare generative-AI use upon submission**, AI under human oversight, AI-generated images disclosed in captions. An older elsevier.com copy surfaced in search with a EUR 100 fee and up to 6 JEL codes — treated as superseded.
- **https://www.elsevier.com/researcher/author/policies-and-guidelines** — Elsevier author policies. Used for declarations, ethics, authorship, and AI-author policy checks.

## Verified on official / publisher pages (2026-06-22)

- **Editors-in-Chief:** **Evi Pappa** (Universidad Carlos III de Madrid), **David K. Levine** (Royal Holloway, University of London), **Stefania Garetto** (Boston University), **Peter Rupert** (UC Santa Barbara), and **Robert Sauer** (Royal Holloway, University of London). The journal runs a multi-editor co-Editor-in-Chief masthead; re-confirm names on the ScienceDirect editorial-board page before naming an editor in a cover letter, as the roster rotates. (Elsevier editorial-board listing + cross-source verification, accessed 2026-06-22)
- **Submission fee:** non-refundable **EUR 125** for new submissions; **EUR 100** if the contact author is a PhD student; **EUR 50** if the contact author is from a Research4Life **Group B** country; **waiver** for Research4Life **Group A** countries. Waivers/discounts require a voucher code requested from the journal before submitting to Editorial Manager. (Elsevier guide for authors, accessed 2026-06-22)
- **Open access (optional):** Gold OA Article Publishing Charge **USD 3,760** excluding taxes; the subscription route carries no author APC. (ScienceDirect journal home, accessed 2026-06-22) Re-confirm the current figure before quoting.

## Facts used in the skills

| Fact | Source |
|------|--------|
| EER is an Elsevier economics journal hosted on ScienceDirect | ScienceDirect journal home |
| Submission is through Editorial Manager | Editorial Manager portal |
| Manuscripts need abstract, JEL codes, keywords, declarations, and editable source files | Elsevier guide for authors |
| Data/code availability and replication materials must be handled before publication where applicable | Elsevier guide for authors and policy pages |
| Editors-in-Chief Pappa / Levine / Garetto / Rupert / Sauer | Editorial board (verified 2026-06-22) |
| Submission fee EUR 125 (EUR 100 PhD / EUR 50 R4L Group B / waiver R4L Group A) | Elsevier guide for authors (verified 2026-06-22) |
| Optional OA APC USD 3,760 excl. tax; no APC on subscription route | ScienceDirect home (verified 2026-06-22) |
| Exact style details, abstract/length limits, average timelines are volatile | Re-check live EER / Elsevier pages |

## Unverified / volatile items

- **Resolved 2026-11-24:** abstract limit (no more than 250 words), keywords (1 to 7), single anonymized review, and highlights (encouraged) — guide for authors via search-engine rendering.
- Average timelines and any fixed manuscript length limit are **待核实** on the live Elsevier pages before submission.
- **Editor roster — 待核实 (2026-11-24):** the ScienceDirect editorial-board and "find out more about the editors" pages returned HTTP 403; search snippets of them name Pappa, Levine, Garetto, Rupert and Sauer but disagree on who holds the Editor-in-Chief title and on Sauer's and Levine's affiliations (Royal Holloway vs Bar-Ilan / EUI), and also list **Donna Gilleskie** (UNC Chapel Hill). Keep the 2026-06-22 roster until the page can be opened in a browser.
- Whether JEL codes are required: not shown in the search rendering of the current guide (an older copy asked for up to 6); 待核实.
- Optional OA APC: search results show both USD 3,760 and USD 3,870; 待核实.
- The editor roster and fee schedule were verified on 2026-06-22 but rotate/change; re-confirm on the live ScienceDirect editorial-board and guide-for-authors pages at submission time rather than treating them as permanent.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "European Economic Review",
  "verified": "2026-11-24",
  "rules": {
    "abstract_words_max": {"value": 250, "source": "https://www.sciencedirect.com/journal/european-economic-review/publish/guide-for-authors", "note": "read via search-engine rendering (publisher refuses automated access)"},
    "keywords_min": {"value": 1, "source": "https://www.sciencedirect.com/journal/european-economic-review/publish/guide-for-authors"},
    "keywords_max": {"value": 7, "source": "https://www.sciencedirect.com/journal/european-economic-review/publish/guide-for-authors"},
    "keywords_required": {"value": true, "source": "https://www.sciencedirect.com/journal/european-economic-review/publish/guide-for-authors"},
    "review_mode": {"value": "single-blind", "source": "https://www.sciencedirect.com/journal/european-economic-review/publish/guide-for-authors", "note": "single anonymized"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://www.sciencedirect.com/journal/european-economic-review/publish/guide-for-authors", "note": "declare generative-AI use in manuscript preparation upon submission, if used"},
    "submission_fee": {"value": "EUR 125 non-refundable (EUR 100 PhD-student contact author; EUR 50 Research4Life Group B; waiver for Group A via voucher requested in advance); VAT for European authors", "source": "https://www.sciencedirect.com/journal/european-economic-review/publish/guide-for-authors"},
    "portal": {"value": "Editorial Manager (editorialmanager.com/eerev)", "source": "https://www.editorialmanager.com/eerev"},
    "llm_policy": {"value": "generative AI only under human oversight; authors accountable; use declared at submission; AI images disclosed in captions", "source": "https://www.sciencedirect.com/journal/european-economic-review/publish/guide-for-authors"},
    "jel_codes_required": {"value": null, "note": "not confirmed on the official pages as of 2026-11-24"},
    "main_text_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```

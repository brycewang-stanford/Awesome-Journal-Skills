# JAMA Official Source Map

Primary source map for JAMA-specific facts in this pack. Official pages first checked **2026-06-23**.
Submission rules (Original Investigation limits, structured abstract, Key Points, required statements, peer-review model, AI and preprint policy), access model and masthead **re-verified 2026-11-23** against the live JAMA Instructions for Authors, editors and access pages. Access-method note: jamanetwork.com returns HTTP 403 to plain `curl`; the pages were read through a fetch tool that renders them (WebFetch), in three passes over the 250,000-character Instructions for Authors page. Nothing material changed since 2026-06-23; the Instructions for Authors page is now cited directly (#5).
Re-verify volatile items (current Editor-in-Chief, APC, submission policy) on the official page before relying on them.

## Official pages
| # | URL | What it verifies | Accessed |
|---|---|---|---|
| 1 | https://jamanetwork.com/journals/jama/pages/jama-editors | JAMA masthead: "The Editor in Chief of JAMA is Kirsten Bibbins-Domingo, PhD, MD, MAS." | 2026-11-23 |
| 2 | https://www.ama-assn.org/press-center/ama-press-releases/ama-names-new-editor-chief-jama-and-jama-network | AMA press release naming Bibbins-Domingo as EiC | 2026-06-23 |
| 3 | https://jamanetwork.com/pages/access-at-jama-network | Access model; "all our specialty JAMA Network journals have an open access option" (no fee amounts; flagship JAMA not named); accepted manuscripts may be deposited on acceptance, public on publication | 2026-11-23 |
| 4 | https://portal.issn.org/resource/ISSN/0098-7484 | ISSN registration for JAMA | 2026-06-23 |
| 5 | https://jamanetwork.com/journals/jama/pages/instructions-for-authors | Original Investigation: 3000 words of text, no more than 5 tables and/or figures, structured abstract of no more than 350 words, 3 Key Points of 75-100 words; trial registration, Data Sharing Statement, COI, funding, EQUATOR/CONSORT, cover letter, single-anonymized peer review, AI use, preprints, AMA reference style, portal | 2026-11-23 |

## Verified facts
- **Editor-in-Chief (re-verified 2026-11-23):** Kirsten Bibbins-Domingo, PhD, MD, MAS (UCSF; Lee Goldman Endowed Professor; chair, Dept. of Epidemiology and Biostatistics). 17th EiC of JAMA and the JAMA Network; tenure began July 1, 2022. (#1, #2)
- **Publisher / owner:** American Medical Association (JAMA Network). (#2)
- **APC / fees:** Default route carries no author publication fee (subscription model; no author fee is mentioned on the access page). The access page says the *specialty* JAMA Network journals have an open access option with fee waiver and discount policies; it does not name the flagship JAMA or give any amount, and the Instructions for Authors page gives none either — confirm any OA figure with the editorial office before relying on a number. (#3, #5)
- **ISSN / portal:** ISSN 0098-7484. Manuscripts are submitted online at http://manuscripts.jama.com. (#4, #5)

### Original Investigation (research) — verified 2026-11-23 (#5)
- **Length:** "Maximum length: 3000 words of text", excluding abstract, tables, figures, acknowledgments, references and online-only material; "no more than a total of 5 tables and/or figures". Study-type entries (clinical trials, cohort studies, etc.) suggest 50-75 references; no hard cap is stated for the Original Investigation type itself.
- **Abstract:** "A structured abstract is required." Reports of original data "should include an abstract of no more than 350 words" with the headings Importance, Objective, Design, Setting, Participants, Intervention(s) or Exposure(s), Main Outcome(s) and Measure(s), Results, Conclusions and Relevance, and Trial Registration (trials).
- **Key Points:** "A list of 3 Key Points is required" (Question, Findings, Meaning), limited to 75-100 words.
- **Trial registration:** registration in an ICMJE-acceptable public registry is a condition of consideration; trials enrolling after July 2005 must be registered before onset of patient enrollment, and before manuscript submission; registry name, trial ID and URL go at the end of the abstract and on the submission form. Study protocols with statistical analysis plans are required for all randomized and nonrandomized clinical trials.
- **Data Sharing Statement:** all research reports must provide "a Data Sharing Statement to indicate if data will or will not be shared"; the questions are in the manuscript submission system. Authors of original-data reports also give an access-to-data statement naming one or two authors.
- **Conflicts of interest:** "All authors are required to report potential conflicts of interest"; disclosures go in the Acknowledgment section of the submitted manuscript and must match each author's Authorship Form (ICMJE-based disclosure section), which is requested after submission.
- **Funding:** all financial and material support identified in the Acknowledgment section; "At the time of submission, information on the funding source (including grant identification) must also be completed"; the role of the funder/sponsor in design, conduct, data handling, manuscript preparation and the decision to submit must be stated.
- **Reporting guidelines:** "Follow EQUATOR Reporting Guidelines"; randomized trials include the CONSORT flow diagram and submit the CONSORT checklist; PRISMA for meta-analyses of trials, MOOSE for meta-analyses of observational studies.
- **Ethics:** human or animal studies need IRB approval or waiver and a statement of how informed consent was obtained, in Methods.
- **Cover letter:** required (all JAMA Network journals except JNO); it gives corresponding-author contact details and states whether related papers from the same study were published, posted or submitted.
- **Peer review:** "a single-anonymized peer review process" — reviewer identities are confidential and "author identities are made known to reviewers."
- **AI use:** AI-generated content is discouraged unless part of the formal research design; AI used in a study is described in Methods (platform, tool, version, manufacturer); AI used in manuscript preparation "must be reported in the Acknowledgment section" with tool name, version, manufacturer, dates and description of use.
- **Preprints:** manuscripts previously posted on a preprint server may be submitted; give the preprint link and describe differences at submission.
- **References:** AMA style, numbered in citation order (not alphabetized); up to 6 authors, then first 3 + "et al."

## UNVERIFIED / 待核实
- Optional open-access fee for the flagship JAMA: not stated on the access page or the Instructions for Authors page as of 2026-11-23 (tried both pages and a web search; only third-party figures found, not used).

## Live-check rules
- Treat the Editor-in-Chief and APC as volatile; re-confirm on the masthead/charges page before submission.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "JAMA",
  "verified": "2026-11-23",
  "rules": {
    "main_text_words_max": {"value": 3000, "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors", "note": "Original Investigation; excludes abstract, tables, figures, acknowledgments, references and online-only material"},
    "exhibits_max": {"value": 5, "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors", "note": "total tables and/or figures, Original Investigation"},
    "abstract_words_max": {"value": 350, "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors", "note": "reports of original data"},
    "abstract_format": {"value": "structured", "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors", "note": "Importance, Objective, Design/Setting/Participants, Intervention(s) or Exposure(s), Main Outcome(s) and Measure(s), Results, Conclusions and Relevance, Trial Registration"},
    "review_mode": {"value": "single-blind", "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors", "note": "single-anonymized: author identities are made known to reviewers"},
    "cover_letter": {"value": "required", "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors"},
    "required_statements": {"value": ["structured_abstract", "key_points", "trial_registration", "data_availability", "conflict_of_interest", "funding", "reporting_guideline"], "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors", "note": "trial_registration applies to clinical trials (registry name, ID, URL at end of abstract); data_availability = JAMA Data Sharing Statement; COI disclosures in the Acknowledgment section (Authorship Forms requested after submission); funding source and role of funder; EQUATOR guideline (CONSORT diagram + checklist for RCTs). Conditional: IRB approval/waiver and informed consent in Methods for human studies; AI use in Acknowledgment section; trial protocol + SAP for clinical trials"},
    "portal": {"value": "http://manuscripts.jama.com", "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors"},
    "reference_style": {"value": "AMA style, numbered in citation order; up to 6 authors, else first 3 + et al", "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors"},
    "data_code_policy": {"value": "Data Sharing Statement required for all research reports (whether data will or will not be shared), collected in the submission system", "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors"},
    "llm_policy": {"value": "AI-generated content discouraged unless part of the research design; AI used in the study described in Methods; AI used in manuscript preparation reported in the Acknowledgment section with tool, version, manufacturer, dates and use", "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors"},
    "preprint_policy": {"value": "preprints allowed; give the preprint link and describe differences at submission", "source": "https://jamanetwork.com/journals/jama/pages/instructions-for-authors"},
    "apc": {"value": null, "note": "no author fee on the default route; flagship OA fee not stated on the official pages as of 2026-11-23"}
  }
}
```

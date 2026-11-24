# The Lancet Official Source Map

Primary source map for Lancet-specific facts in this pack. Official pages first checked **2026-06-23**.
Submission rules (Article length, summary, Research in context, required statements, trial registration, reporting guidelines, AI policy, open access) **re-verified 2026-11-23** against the live Lancet *Information for Authors* PDF (#6, dated "August 2026", PDF created 2026-08-19). Access-method note: the thelancet.com HTML pages (#1, #2, #4, #7) return HTTP 403 to `curl` and to the WebFetch renderer from this environment, so they were not re-read; the PDF on the same domain downloads directly and is the authority used for the 2026-11-23 re-check. Changed since 2026-06-23: the Article length is now recorded exactly (3500 words, 4500 for randomised controlled trials, 30 references) and trial reports must follow CONSORT 2025.
Re-verify volatile items (current Editor-in-Chief, APC, submission policy) on the official page before relying on them.

## Official pages
| # | URL | What it verifies | Accessed |
|---|---|---|---|
| 1 | https://www.thelancet.com/lancet/about | About The Lancet: editorial leadership, scope | 2026-06-23 |
| 2 | https://www.thelancet.com/lancet-people | Lancet Group people / editorial team | 2026-06-23 |
| 3 | https://en.wikipedia.org/wiki/Richard_Horton_(editor) | Background on Richard Horton, EiC since 1995 | 2026-06-23 |
| 4 | https://www.thelancet.com/open-access | Lancet open-access policy and fee framework (APC page linked from #6) | 2026-06-23 |
| 5 | https://portal.issn.org/resource/ISSN/0140-6736 | ISSN registration for The Lancet (British edition) | 2026-06-23 |
| 6 | https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf | Information for Authors (August 2026): Articles up to 3500 words (4500 for RCTs) with 30 references; semistructured summary of 5 paragraphs, not exceeding 300 words; Research in context panel; first-submission file list (covering letter, declaration of interests, funding statement); data sharing statement; trial registration; CONSORT 2025 / EQUATOR; ICMJE COI forms after peer review for Articles; AI declaration; preprints; Vancouver references; Editorial Manager portal; hybrid OA | 2026-11-23 |
| 7 | https://www.thelancet.com/lancet/information-for-authors | HTML Information for Authors hub (HTTP 403 from this environment on 2026-11-23; PDF #6 used instead) | — |

## Verified facts
- **Editor-in-Chief (verified 2026-06-23):** Richard Horton. Editor-in-Chief of The Lancet since 1995; active in 2026 (e.g., One Health Summit panels, signed editorials). (#1, #2, #3) Not re-read on 2026-11-23 (masthead pages 403); see UNVERIFIED.
- **Publisher / owner:** Elsevier (The Lancet Group); UK-based, owned by Elsevier since 1991. (#3, #5)
- **APC / fees:** "Manuscript submission to all Lancet journals is free." "The Lancet is a hybrid journal": authors of research Articles whose funding requires open access may choose gold OA (CC BY, CC BY-NC-ND or CC BY-NC) or subscription green OA (accepted version in any repository 6 months after publication; the paper is also made free on the Lancet site 6 months after publication). APC details are on the open-access page; editors do not see payment information. Elsevier applies a personalized/Geographical Pricing for Open Access (GPOA) model for Lancet titles (papers accepted after Oct 2025), so the figure varies by country/institution/agreement — confirm the personalized figure on the live charges page rather than relying on a fixed number. (#4, #6)
- **ISSN / portal:** ISSN 0140-6736 (British edition). Submission online via Editorial Manager at www.editorialmanager.com/thelancet. (#5, #6)

### Articles (original research) — re-verified 2026-11-23 (#6)
- **Length:** "Be up to 3500 words (4500 for randomised controlled trials) with 30 references (the word count is for the manuscript text only)"; qualitative and mixed-methods Articles: main text 4500 words, maximum 30 references.
- **Summary:** "an abstract (semistructured summary), with five paragraphs (Background, Methods, Findings, Interpretation, and Funding), not exceeding 300 words"; RCT abstracts follow CONSORT for abstracts.
- **Research in context:** all research papers must include the panel (Evidence before this study / Added value of this study / Implications of all the available evidence), without references; editors use it at first assessment.
- **First submissions should include:** covering letter; manuscript with tables and panels; figures; authors statement form; declaration of interests and source of funding statements; protocols and CONSORT details for RCTs; Research in context panel for all primary research Articles.
- **Declaration of interests:** "All submissions to The Lancet must include disclosure of all relationships" — under a "Declaration of interests" subheading at the end of the text. For original research Articles the signed ICMJE COI forms and author statements "will be requested after peer review".
- **Funding:** all sources declared as an acknowledgment; a "Role of the funding source" subsection at the end of Methods.
- **Contributors:** individual contributions specified at the end of the text; more than one author must have directly accessed and verified the underlying data.
- **Data sharing:** "All submitted research Articles must contain a data sharing statement, to be included at the end of the manuscript" (what, when, where, by what access criteria; "undecided" is not acceptable).
- **Trial registration:** all interventional trials registered in a WHO ICTRP primary register or ClinicalTrials.gov, with the 24-item dataset public before recruitment of the first participant; observational-study registration encouraged.
- **Reporting guidelines:** "Reports of trials must conform to CONSORT 2025 guidelines" with full protocol (and SAP); STARD, STROBE (with protocol), STREGA, COREQ/SRQR, PRISMA, GATHER, CONSORT-AI/SPIRIT-AI; EQUATOR network.
- **Ethics:** ethics committee approval and informed consent, with the approval number.
- **AI use:** AI tools may support authors under human oversight; "for the use of AI tools we require a disclosure statement upon submission" — a separate AI declaration at the end of the manuscript (tool name and version, purpose, extent of oversight); AI in the research process described in Methods; basic grammar/spelling checks need no declaration; AI cannot be an author.
- **Preprints:** posting on a preprint server "does not conflict with submission to the Lancet journals".
- **Peer review:** in-house assessment first (overall acceptance about 5%), then at least two reviewers and a statistician. The Information for Authors does not state whether review is single- or double-blind.
- **References:** Vancouver numbering style, superscript after punctuation.

## UNVERIFIED / 待核实
- Editor-in-Chief (Richard Horton): not re-read on 2026-11-23 — thelancet.com masthead pages (#1, #2) return HTTP 403 to curl and WebFetch; a web search found only undated or older biographies.
- Exact APC under GPOA: the open-access page (#4) returned 403 on 2026-11-23.
- Review blinding (single vs double): not stated in the Information for Authors PDF (#6) as of 2026-11-23.

## Live-check rules
- Treat the Editor-in-Chief and APC as volatile; re-confirm on the masthead/charges page before submission.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "The Lancet",
  "verified": "2026-11-23",
  "rules": {
    "main_text_words_max": {"value": 3500, "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf", "note": "Articles, manuscript text only; 4500 for randomised controlled trials and for qualitative/mixed-methods Articles"},
    "references_max": {"value": 30, "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf", "note": "Articles"},
    "abstract_words_max": {"value": 300, "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf", "note": "semistructured summary"},
    "abstract_format": {"value": "structured", "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf", "note": "five paragraphs: Background, Methods, Findings, Interpretation, Funding"},
    "cover_letter": {"value": "required", "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf", "note": "first item on the first-submission list; uploaded at the Enter Comments stage"},
    "required_statements": {"value": ["structured_abstract", "conflict_of_interest", "funding", "author_contributions", "data_availability", "trial_registration", "reporting_guideline"], "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf", "note": "Research in context panel also required for all research Articles (no schema key); Declaration of interests at end of text (signed ICMJE forms requested after peer review for Articles); source of funding + Role of the funding source; contributors statement; data sharing statement; trial_registration for interventional trials; CONSORT 2025 + protocol for RCTs, other EQUATOR guidelines by design. Conditional: AI declaration at the end of the manuscript if AI tools were used; ethics approval and consent for human studies"},
    "review_mode": {"value": null, "note": "single/double blind not stated in the Information for Authors as of 2026-11-23; at least two reviewers and a statistician"},
    "portal": {"value": "Editorial Manager (www.editorialmanager.com/thelancet)", "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf"},
    "reference_style": {"value": "Vancouver numbering, superscript after punctuation", "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf"},
    "submission_fee": {"value": "none (manuscript submission to all Lancet journals is free)", "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf"},
    "apc": {"value": "hybrid: gold OA (CC BY / CC BY-NC-ND / CC BY-NC) for funder-mandated research Articles with an APC set per the open-access page (Elsevier personalized pricing); or green OA at 6 months", "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf"},
    "data_code_policy": {"value": "data sharing statement required in all submitted research Articles (what, when, where, access criteria; 'undecided' not acceptable); trials enrolling from 2019-01-01 need a data sharing plan in the registration", "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf"},
    "llm_policy": {"value": "AI tools allowed with human oversight; separate AI declaration at end of manuscript at submission (tool, version, purpose, oversight); research use in Methods; grammar/spelling checks exempt; AI cannot be an author", "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf"},
    "preprint_policy": {"value": "preprint posting does not conflict with submission", "source": "https://www.thelancet.com/pb-assets/Lancet/authors/tl-info-for-authors.pdf"}
  }
}
```

# JBF Official Source Map

Primary and authoritative sources behind the *Journal of Banking & Finance* (JBF)
facts injected into this skill pack. **Policy refresh date: 2026-06-20.** Re-check
the live ScienceDirect pages before submission because fees, editor rosters, and
special-issue instructions can change.

Submission fee, review model, abstract and keyword limits, Highlights, AI declaration
and masthead **re-verified 2026-11-24**. Access method: the live ScienceDirect pages
return HTTP 403 (Cloudflare) to curl, WebFetch and a reader proxy, and the Internet
Archive holds no Guide-for-Authors capture newer than March 2024, so the Guide was
read via **search-engine rendering restricted to sciencedirect.com** (four independent
queries); the newest archived home page (2025-08-25, below) was used only for the
Managing Editor; the Editorial Manager entry https://www.editorialmanager.com/jbf/ is
reachable directly. **Change found on 2026-11-24:** three independent renderings of
the Guide quote the abstract limit as "does not exceed **150** words" (the 2026-06-20
read below recorded 250; the March-2024 Guide capture said "100-150 words"); the pack
now uses 150. Unchanged: **USD 350** fee for unsolicited new manuscripts (non-refundable;
resubmission after editor rejection = new submission); **double anonymized** review
with separate title page and anonymized manuscript (acknowledgements removed);
**1 to 7** English keywords required; Highlights encouraged (3-5 bullets, max **85**
characters each); generative-AI use declared in a new section before the references
when the paper is first submitted (basic grammar/spelling tools exempt); Managing
Editor **Christa Bouwman** (Texas A&M) and Co-Editor **Xiaoyan Zhang**.

## Official journal & publisher pages

- **https://www.sciencedirect.com/journal/journal-of-banking-and-finance** — JBF
  homepage on ScienceDirect. Verifies: publisher = Elsevier; current metrics;
  current **Managing Editor = Christa Bouwman** at Texas A&M University; current
  homepage submission link points to **Editorial Manager**; open-access APC and
  ScienceDirect decision-time insights are displayed on the journal page.
- **https://www.sciencedirect.com/journal/journal-of-banking-and-finance/about/editorial-board** —
  official editorial board. Verifies: **Christa Bouwman** as Managing Editor;
  Co-Editors **Edith Hotchkiss** and **Xiaoyan Zhang**; a large associate-editor
  board; and the country/region distribution of the editorial board.
- **https://www.sciencedirect.com/journal/journal-of-banking-and-finance/publish/guide-for-authors** —
  Guide for Authors. Verifies: JBF scope covers theoretical and empirical finance
  and banking, including asset pricing/management, banking, corporate finance,
  regulation, FinTech, market microstructure, systemic risk, and related areas;
  the journal receives about 1500 new submissions per year; peer review is
  **double anonymized** with editor screening and usually at least one reviewer;
  author submission uses **Editorial Manager**; unsolicited new manuscripts carry
  a **USD 350 submission fee**; resubmitting an editor-rejected paper counts as a
  new submission; fees are non-refundable and papers may be rejected before
  external review; eligible authors can obtain a discount code for use in
  Editorial Manager.
- The same Guide verifies submission-format facts: editable Word/LaTeX source
  files are required; the title page and anonymized manuscript must be separate;
  the anonymized manuscript must omit author details and acknowledgements; the
  abstract must be concise/factual and **not exceed 250 words** (superseded: 150
  words per the 2026-11-24 re-check above); **1-7 English
  keywords** are required; **Highlights** are encouraged at submission and should
  be 3-5 bullets, each no more than 85 characters; generative-AI use in
  manuscript preparation must be declared; SSRN preprint posting is offered
  during submission and becomes public once the paper passes initial desk review.
- The same Guide verifies research-data and reference facts: for this journal,
  Elsevier **Option C** applies, so authors are required to deposit research data
  in a relevant repository and cite/link it, or state why data cannot be shared;
  a data-availability statement is required at submission and appears with the
  published article; Data in Brief / MethodsX co-submission is available through
  Editorial Manager; first submission has no strict reference-format requirement
  if references are complete and consistent, and JBF's proof-stage style is a
  numbered Elsevier reference style with dataset and software examples.
- **https://web.archive.org/web/20250825003547/https://www.sciencedirect.com/journal/journal-of-banking-and-finance**
  — newest Internet Archive capture of the official home (2025-08-25): Managing
  Editor Christa Bouwman (Texas A&M University); APC then USD 3,290 excluding taxes
  (not re-verifiable on 2026-11-24, so not used as a current figure).
- **https://www.editorialmanager.com/jbf/** — Editorial Manager entry for JBF
  (reachable directly 2026-11-24).
- **https://www.elsevier.com/researcher/author/policies-and-guidelines/submission-fees** —
  Elsevier submission-fee policy. Verifies: all Elsevier journals that charge a
  submission fee offer waivers for authors with limited means and authors from
  developing countries, while journal-specific details should be checked in the
  relevant Guide for Authors.

## Current operational notes

- Treat **Editorial Manager** as the submission system.
- Treat **USD 350** as the active unsolicited-new-manuscript fee and plan the
  fee/discount-code decision before submission.
- Treat JBF as **double anonymized**: body manuscript, acknowledgements, metadata,
  and title page must be separated cleanly.
- Treat data sharing as stronger than a generic encouragement: either deposit,
  cite, and link the research data, or make an explicit non-sharing statement.
- Treat JEL codes as finance/economics convention rather than a JBF-specific
  requirement in the currently inspected Guide text; keep them in the checklist
  as helpful metadata, not as a hard journal rule.

## UNVERIFIED / verify-before-quoting

- **Abstract limit 150 vs 250 words:** 150 is quoted by three search-engine renderings of the official
  Guide on 2026-11-24, but the live page could not be opened (HTTP 403); re-open the Guide before relying
  on either number.
- **Option C research-data wording and data statement at submission:** not re-surfaced on 2026-11-24;
  kept from the 2026-06-20 read.
- **Co-Editor Edith Hotchkiss:** not re-surfaced on 2026-11-24 (Christa Bouwman and Xiaoyan Zhang were).
- **Open-access APC:** last official figure seen is USD 3,290 (2025-08-25 archive capture); current
  figure not verified on 2026-11-24.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of Banking & Finance",
  "verified": "2026-11-24",
  "rules": {
    "review_mode": {"value": "double-blind", "source": "https://www.sciencedirect.com/journal/journal-of-banking-and-finance/publish/guide-for-authors", "note": "'double anonymized': title page and anonymized manuscript (no author details or acknowledgements) uploaded as separate files; read via search-engine rendering (live page HTTP 403)"},
    "abstract_words_max": {"value": 150, "source": "https://www.sciencedirect.com/journal/journal-of-banking-and-finance/publish/guide-for-authors", "note": "read via search-engine rendering on 2026-11-24; the 2026-06 read recorded 250 - re-open the live Guide"},
    "keywords_required": {"value": true, "source": "https://www.sciencedirect.com/journal/journal-of-banking-and-finance/publish/guide-for-authors"},
    "keywords_min": {"value": 1, "source": "https://www.sciencedirect.com/journal/journal-of-banking-and-finance/publish/guide-for-authors"},
    "keywords_max": {"value": 7, "source": "https://www.sciencedirect.com/journal/journal-of-banking-and-finance/publish/guide-for-authors", "note": "English keywords"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://www.sciencedirect.com/journal/journal-of-banking-and-finance/publish/guide-for-authors", "note": "only if AI tools were used in manuscript preparation: statement in a new section before the references at first submission"},
    "submission_fee": {"value": "USD 350 for unsolicited new manuscripts; non-refundable; resubmission of an editor-rejected paper counts as new; discount codes for eligible authors", "source": "https://www.sciencedirect.com/journal/journal-of-banking-and-finance/publish/guide-for-authors"},
    "portal": {"value": "Elsevier Editorial Manager (https://www.editorialmanager.com/jbf/)", "source": "https://www.editorialmanager.com/jbf/"},
    "llm_policy": {"value": "declare generative-AI use in manuscript preparation in a section before the references; published with the article; basic grammar/spelling/reference tools exempt", "source": "https://www.sciencedirect.com/journal/journal-of-banking-and-finance/publish/guide-for-authors"},
    "jel_codes_required": {"value": null, "note": "not stated in the Guide text surfaced as of 2026-11-24 (kept as convention, not a JBF rule)"}
  }
}
```

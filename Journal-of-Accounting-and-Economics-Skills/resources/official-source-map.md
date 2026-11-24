# JAE Official Source Map

Canonical sources for every Journal of Accounting and Economics (JAE) claim made in this skill
pack. Sources were refreshed on **2026-06-20**. Portal, conference call and fee signals
**re-verified 2026-11-24**: the Editorial Manager sites and the 2027 JAE Conference call (EAA/ARC,
read through the site's WordPress JSON endpoint) were fetched live, and the Elsevier submission-fees
page was fetched live. Access note: every ScienceDirect page (Guide for Authors, editorial board,
open-access page) returned an HTTP 403 captcha ("Are you a robot?") to curl, WebFetch and a reader
proxy on 2026-11-24, and the newest Internet Archive capture of the Guide is from 2024-02-20, so the
Guide's rules could not be re-read today; the Wharton JAE payment page now returns HTTP 404. Facts
that depend on the live Guide are listed under UNVERIFIED below. Live-check the current ScienceDirect
Guide for Authors, editorial-board page, open-access page, and Elsevier submission-fee page before
upload, because fee amounts, mastheads, file labels, and policy wording can change.

## Official JAE / Elsevier sources

- **https://www.sciencedirect.com/journal/journal-of-accounting-and-economics** — ScienceDirect
  journal home. Use as the current journal entry point for scope, metrics, ISSN, article records,
  guide links, open-access route, and editorial-board navigation.
- **https://www.sciencedirect.com/journal/journal-of-accounting-and-economics/publish/guide-for-authors** —
  ScienceDirect Guide for Authors. Use as the live source before upload for submission fee,
  double-anonymized review, reviewer minimum, file separation, Highlights, keywords, JEL codes,
  reference style, abstract wording, source-file requirements, declarations, data policy, and
  Article Transfer Service wording.
- **http://web.archive.org/web/20240220203615id_/https://www.sciencedirect.com/journal/journal-of-accounting-and-economics/publish/guide-for-authors** —
  archived official ScienceDirect Guide for Authors capture. Confirms the JAE-specific rules used
  as stable local defaults: **USD 650** fee for unsolicited new manuscripts, no fee for resubmissions,
  double-anonymized review with a minimum of two reviewers, mandatory Highlights, up to six keywords,
  up to six JEL codes, Elsevier author-date reference style, numbered sections, elsarticle.cls /
  BibTeX support, and voluntary Elsevier research-data language.
- **https://www.sciencedirect.com/journal/journal-of-accounting-and-economics/about/editorial-board** —
  ScienceDirect editorial-board page. Use as the live source before naming current editors, founding
  editors, associate editors, or board structure.
- **https://www.sciencedirect.com/journal/journal-of-accounting-and-economics/publish/open-access-options** —
  ScienceDirect open-access options page. Use before quoting open-access route, APC, subscription
  route, license, embargo, or author-rights details.
- **https://www.editorialmanager.com/jacec/** — Editorial Manager portal (fetched live 2026-11-24;
  the login page is titled "Journal of Accounting and Economics"; the 2027 JAE Conference call links
  submissions here). Use for live submission and status tracking. **Correction:** the
  `editorialmanager.com/jae/` address this pack used before 2026-11-24 is the Editorial Manager site of
  *The Journal of Adventist Education*, not JAE.

## Official partner / policy sources

- **https://accounting.wharton.upenn.edu/jae-payment/** — Wharton Accounting JAE payment page
  (2026-06-20 reading: fees paid through Elsevier's Submission Start flow; EU authors add applicable
  VAT). Returns **HTTP 404** on 2026-11-24; keep only as a historical pointer.
- **https://eaa-online.org/arc/events/2027-jae-call-for-papers** (also listed as
  https://eaa-online.org/arc/events/2027-journal-of-accounting-and-economics-jae-conference) — 2027 JAE
  Conference call for papers (fetched live 2026-11-24). Confirms: submission deadline **February 26,
  2027**; submission fee **$750**, credit card only; submissions via
  https://www.editorialmanager.com/JACEC/; all conference submissions are formal JAE submissions, R&R
  papers not selected continue in the regular process, and rejected conference papers may not be
  resubmitted; accepted conference papers appear in a special conference issue; **$5,000** attendee-voted
  Best Paper award; attendance by invitation only; sponsored by the **University of Rochester Simon
  Business School**, Charles River Associates, and Cambridge Business Publishers; conference
  October 15-16, 2027 at Simon Business School, Rochester NY.
- **https://eaa-online.org/arc/events/2025-journal-of-accounting-and-economics-conference-call-for-papers/** —
  EAA / ARC 2025 JAE Conference call for papers. Confirms the annual JAE Conference route,
  Wharton / Charles River Associates / Cambridge Business Publishers sponsorship, economics-based
  research framing, dedicated special conference issue, invitation-only attendance, **USD 650**
  submission fee by credit card, and **USD 5,000** attendee-voted Best Paper award.
- **https://www.elsevier.com/researcher/author/policies-and-guidelines/submission-fees** —
  Elsevier submission-fees policy (fetched live 2026-11-24). Confirms that around 50 Elsevier
  economics, finance, and accounting journals levy submission fees, that a journal's fee is flagged in
  its guide for authors and during submission, and that the monies are reinvested as journal community
  funds.
- **https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines** and
  **https://www.elsevier.com/about/policies-and-standards/research-data** — Elsevier research-data
  guidance and policy. Confirms Elsevier's encouragement of data sharing, dataset citation, data
  availability statements, and acceptable explanations when data cannot be shared.
- **https://www.elsevier.com/researcher/author/policies-and-guidelines** — Elsevier author policies
  entry point for ethics, declarations, authorship, similarity checks, AI disclosure, artwork/media,
  and manuscript-preparation policies.

## Facts used in the skills

| Fact | Source URL |
|------|------------|
| JAE is an Elsevier / ScienceDirect accounting-and-economics journal | ScienceDirect journal home |
| Current Editors (verified 2026-06-22): **John Core (MIT Sloan), Ed deHaan (Stanford GSB), Wayne R. Guay (Wharton, U. Penn)**; cross-checked on the ScienceDirect editorial-board page and the JAE Wikipedia entry. Re-verify the masthead before naming editors in author-facing advice. | ScienceDirect editorial-board page; en.wikipedia.org/wiki/Journal_of_Accounting_and_Economics |
| Submission fee verified current at **USD 650** for unsolicited new manuscripts, no fee for resubmissions (re-confirmed 2026-06-22 against the live ScienceDirect Guide for Authors) | ScienceDirect Guide for Authors |
| JAE's durable identity is positive / economics-based accounting research in the Watts-Zimmerman tradition | ScienceDirect journal home; archived Guide for Authors; JAE Conference call |
| Scope includes accounting within firms, capital-market information content, financial contracting, monitoring agency relationships, accounting standards, disclosure regulation, and theory of the accounting firm | archived Guide for Authors |
| Submission route is Elsevier Editorial Manager at www.editorialmanager.com/jacec/ (verified live 2026-11-24) | Editorial Manager portal; 2027 JAE Conference call |
| Fee default for unsolicited new manuscripts is USD 650, with no fee for resubmissions; check current ScienceDirect amount before payment | archived Guide for Authors; JAE Conference call; Elsevier submission-fees policy |
| Fee payment uses Elsevier Submission Start; EU authors add applicable VAT (2026-06-20 reading; page now 404) | Wharton JAE payment page |
| Review is double-anonymized; suitable manuscripts go to at least two independent reviewers; editor makes the final decision | archived Guide for Authors |
| Upload requires anonymized manuscript and separate title page with author details | archived Guide for Authors |
| Highlights are required, 2 to 5 bullets, max 125 characters each | archived Guide for Authors |
| Keywords use American spelling, up to six; JEL classification codes up to six | archived Guide for Authors |
| Abstract should be concise and factual, stand alone, and avoid references and nonstandard abbreviations; no local numeric cap is used without live Guide confirmation | archived Guide for Authors |
| Elsevier author-date / Harvard references, numbered sections, and elsarticle.cls / BibTeX support | archived Guide for Authors |
| Research data sharing is encouraged under Elsevier policy; this pack treats JAE data sharing as voluntary unless the current Guide states otherwise | archived Guide for Authors; Elsevier research-data policy |
| JAE Conference is an invitation-only annual route with selected papers printed in a dedicated special issue; 2025 call listed a USD 650 fee; the **2027** call (deadline February 26, 2027; sponsor University of Rochester Simon Business School) lists a **USD 750** fee and the USD 5,000 Best Paper award | EAA / ARC JAE Conference calls (2025; 2027 re-verified 2026-11-24) |
| Article Transfer Service / journal transfer can apply to unsuitable submissions | Guide for Authors; Elsevier policy pages |

## Live-check items before upload

- Reopen the ScienceDirect Guide for Authors before quoting the current fee, required files, Highlights,
  keywords, JEL codes, abstract wording, reference style, declarations, data policy, or transfer-service
  language.
- Reopen the ScienceDirect editorial-board page before naming current editors, coeditors, associate
  editors, founding editors, or board size.
- Reopen the ScienceDirect open-access page before quoting APCs, subscription route, license, embargo,
  or author-rights details.
- Reopen Elsevier's submission-fee and research-data pages before advising on payment routing, VAT,
  data availability statements, dataset citations, or AI / declaration wording.
- Do not state acceptance rates, fixed review timelines, current editorial roster, or a numeric main-text
  length cap unless the current official page provides the value.

## UNVERIFIED / 待核实 (as of 2026-11-24)

- **Regular submission fee.** Last confirmed at **USD 650** on 2026-06-22. On 2026-11-24 the ScienceDirect
  Guide was blocked (captcha); search-engine snippets of the Guide and of third-party fee lists show
  **USD 750**, and the 2027 JAE Conference call (formal JAE submissions) charges $750. Not changed in the
  facts table until the Guide itself can be read; skills tell authors to expect USD 750 and confirm.
- **Highlights / keywords format.** The 2024 archived Guide says 2-5 Highlights of at most 125
  characters and up to six keywords; search-engine snippets of the current Guide (2026-11-24) describe
  3-5 Highlights of at most 85 characters and 1-7 keywords (Elsevier's newer guide template). Not
  confirmed on the live page; kept at the archived values with a caution in `jae-submission`.
- **Editors.** The pack names John Core, Ed deHaan and Wayne R. Guay (2026-06-22). Search-engine
  rendering of the ScienceDirect editorial-board page on 2026-11-24 suggests Elizabeth Blankespoor is
  an editor and that Core is listed with a 2009-2024 tenure; the page itself could not be loaded
  (captcha), and the 2027 conference's move to Rochester Simon sponsorship may also signal an editorial
  change. Re-verify the masthead before naming editors.
- **Review mode, JEL-code requirement, declarations, data policy, open-access APC** — only the 2024
  archived Guide was available; not re-read on 2026-11-24.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of Accounting and Economics",
  "verified": "2026-11-24",
  "rules": {
    "portal": {"value": "Elsevier Editorial Manager (www.editorialmanager.com/jacec/)", "source": "https://www.editorialmanager.com/jacec/"},
    "submission_fee": {"value": "USD 750 on the 2027 JAE Conference call (conference papers are formal JAE submissions); regular-submission amount not re-readable on the live Guide on 2026-11-24 (last confirmed USD 650, 2026-06-22)", "source": "https://eaa-online.org/arc/events/2027-jae-call-for-papers"},
    "review_mode": {"value": null, "note": "double-anonymized per the 2024 archived Guide; live Guide blocked on 2026-11-24"},
    "keywords_max": {"value": null, "note": "up to six per the 2024 archived Guide; live Guide blocked on 2026-11-24 and snippets suggest a change"},
    "jel_codes_required": {"value": null, "note": "required (up to six) per the 2024 archived Guide; not re-read on 2026-11-24"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"},
    "main_text_pages_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```

# JAE Official Source Map

Primary and authoritative sources behind every Journal of Applied Econometrics (JAE)
specific fact injected into this skill pack.
Access date for all entries: **2026-06-01**; editor/fee live-check verification
**2026-06-22**. Author guidelines, Data Archive instructions, submission portal and masthead
**re-verified 2026-11-24**: the Wiley author-guidelines and editorial-board pages refuse automated access
(HTTP 403, and the Internet Archive serves only Wiley's 403 page for 2025 captures), so they were **read via
search-engine rendering** restricted to onlinelibrary.wiley.com; the Editorial Express e-submit page and the
Queen's Data Archive author instructions were read directly. Change found on 2026-11-24: the guidelines state
the 35-page limit as **double-line spaced with a 12-point font** and that **any submission over 50 pages is
rejected automatically**. The 100-word summary, up to six keywords, single-blind review, three-papers-under-review
cap, Data Archive deposit and Editor Barbara Rossi are **unchanged**. Re-verify volatile items (editors, APC figures, policy wording, page
limits) before relying on them — journal pages change, and several official Wiley pages
require browser access outside this crawler.

**Live-check 2026-06-22:** Editor (Editor-in-Chief) **Barbara Rossi** (Barcelona School
of Economics / ICREA / CEPR) re-confirmed as current via the Wiley Online Library journal
page (current Vol. 41 issues, 2026) and Wikipedia. No author submission fee is encoded;
non-open-access publication is free to authors (optional Wiley OA APC applies only if
chosen — re-confirm the figure on the live Wiley funded-access page). Re-verify before
submission.

## Official author guidelines (Wiley)

- **https://onlinelibrary.wiley.com/page/journal/10991255/homepage/forauthors.html** — JAE Author Guidelines (re-checked 2026-11-24 via search-engine rendering; adds: the 35-page limit is double-line spaced at 12-point font and submissions over 50 pages are automatically rejected; a rejected paper cannot be resubmitted unless invited). Verifies: 100-word summary (no citations); up to six (6) keywords; 35-page article limit with online appendices excluded; references "in any style or format, as long as it is consistent throughout the manuscript"; single-blind peer review by anonymous reviewers in addition to the Editor; mandatory JAE Data Archive deposit for accepted papers unless confidential; no more than three papers from the same author under review at once; cover letter not mandatory; submit via Editorial Express; Research Articles and Replication Articles categories; "Free Format" first submission. Live Wiley page should be re-opened in a browser when preparing an upload; facts are cross-confirmed via the Internet Archive snapshot below.
- **http://web.archive.org/web/20231203052231/https://onlinelibrary.wiley.com/page/journal/10991255/homepage/forauthors.html** — Internet Archive snapshot (2023-12-03) of the same official guidelines. Cross-confirms the 100-word summary, 35-page limit, single-blind "anonymous reviewers in addition to the Editor," Editor-in-Chief final authority, Data Archive deposit requirement, Editorial Express at editorialexpress.com/jae, and three-papers-under-review cap.

## Submission system

- **http://editorialexpress.com/jae** — JAE submission portal (Editorial Express). Verifies: submission system is Editorial Express; manuscripts handled in PDF format.
- **https://editorialexpress.com/cgi-bin/e-editor/e-submit.cgi?dbase=jae** — JAE secure e-submit portal (read directly 2026-11-24). Verifies: platform = Editorial Express; manuscripts "must be uploaded in PDF format only"; the submitter confirms co-authors have reviewed the journal's licensing options; no fee-payment step.
- **https://onlinelibrary.wiley.com/page/journal/10991255/homepage/editorialboard.html** — JAE editorial board (read via search-engine rendering 2026-11-24). Verifies: Editor **Barbara Rossi** (ICREA–Universitat Pompeu Fabra); Co-Editors Todd Clark, Marco Del Negro, Sylvia Frühwirth-Schnatter, Eric Ghysels, Nikolay Gospodinov, Ismael Mourifié and Tong Li; Replication Section Editor Tatevik Sekhposyan.

## JAE Data Archive (the journal's signature norm)

- **http://qed.econ.queensu.ca/jae/author-instructions.html** — JAE Data Archive author instructions (Queen's University; re-read directly 2026-11-24, unchanged). Verifies: authors of accepted JAE papers must submit a complete set of (non-confidential) data; every dataset needs a plain-text ASCII readme; data must be plain ASCII/CSV text (Stata `.dta` and SAS datasets are not acceptable on their own); programs/supplementary material encouraged; confidential-data exception requires a readme describing the source in enough detail that others can apply for access, ideally with extraction programs; responsibility for permission rests with the investigator.
- **http://qed.econ.queensu.ca/jae/** — JAE Data Archive home (Queen's University). Verifies: archive holds data for all papers accepted since January 1994; original host Queen's University Economics Department 1994–late 2022; maintainer J. G. MacKinnon (jgm@econ.queensu.ca); moved to ZBW in 2022.
- **https://journaldata.zbw.eu/** — ZBW Journal Data Archive (current host of the JAE archive since 2022). Verifies: current hosting location for JAE replication data and programs.
- **https://www.re3data.org/repository/r3d100010130** — re3data registry entry for the JAE Data Archive. Verifies: hosted at ZBW Journal Data Archive; ~1,487 datasets; open access to data; repository for replication data and programs.

## Publisher, history, scope, editor

- **https://en.wikipedia.org/wiki/Journal_of_Applied_Econometrics** — Verifies: publisher John Wiley & Sons; Editor-in-Chief Barbara Rossi; established 1986; 7 issues/year; ISSN 0883-7252 (print) / 1099-1255 (online); since 1994 requires authors to deposit a complete set of non-confidential data to the journal's Data Archive to enable replication; scope = applied econometrics (applications of econometric techniques to real data rather than pure econometric theory).

## Bounded live-check rules

- What is confirmed for author costs: no submission fee is encoded; non-OA publication is free to
  authors under the source-map facts. Check the Wiley funded-access page only if choosing optional
  open access.
- Editor-in-Chief Barbara Rossi is the only editor name treated as load-bearing. Do not name co-editors,
  associate editors, or a managing editor unless the live Wiley editorial-board page is open.
- Use the 35-page article cap rather than inventing a separate body word-count limit.
- The Internet Archive snapshot dated 2023-12-03 is a fallback for author-guideline facts; re-open the
  current Wiley page before relying on any volatile number.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of Applied Econometrics",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 35, "source": "https://onlinelibrary.wiley.com/page/journal/10991255/homepage/forauthors.html", "note": "double-line spaced, 12-point font; online appendices excluded; submissions over 50 pages are rejected automatically; read via search-engine rendering"},
    "abstract_words_max": {"value": 100, "source": "https://onlinelibrary.wiley.com/page/journal/10991255/homepage/forauthors.html", "note": "a summary that stands alone and cites no other work"},
    "keywords_max": {"value": 6, "source": "https://onlinelibrary.wiley.com/page/journal/10991255/homepage/forauthors.html", "note": "up to six keywords"},
    "review_mode": {"value": "single-blind", "source": "https://onlinelibrary.wiley.com/page/journal/10991255/homepage/forauthors.html", "note": "anonymous reviewers in addition to the Editor"},
    "cover_letter": {"value": "optional", "source": "https://onlinelibrary.wiley.com/page/journal/10991255/homepage/forauthors.html", "note": "not mandatory"},
    "portal": {"value": "Editorial Express (editorialexpress.com/jae)", "source": "https://editorialexpress.com/cgi-bin/e-editor/e-submit.cgi?dbase=jae"},
    "file_format": {"value": "PDF only (Free Format first submission)", "source": "https://editorialexpress.com/cgi-bin/e-editor/e-submit.cgi?dbase=jae"},
    "reference_style": {"value": "any style, consistent throughout the manuscript", "source": "https://onlinelibrary.wiley.com/page/journal/10991255/homepage/forauthors.html"},
    "data_code_policy": {"value": "accepted papers deposit all non-confidential data in the JAE Data Archive (plain ASCII/CSV with an ASCII readme; programs encouraged); confidential data need a readme explaining how to obtain them", "source": "http://qed.econ.queensu.ca/jae/author-instructions.html"},
    "submission_fee": {"value": "none", "source": "https://editorialexpress.com/cgi-bin/e-editor/e-submit.cgi?dbase=jae", "note": "the e-submit workflow has no fee step; no fee encoded in the guidelines"},
    "jel_codes_required": {"value": null, "note": "not stated on the official pages as of 2026-11-24"},
    "llm_policy": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```

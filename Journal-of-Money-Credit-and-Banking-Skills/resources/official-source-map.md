# Journal of Money, Credit and Banking Official Source Map

Primary source map for facts used in the JMCB skill pack. **Access date: 2026-06.** Submission instructions, fees, length guidance, data-exemption rule and masthead **re-verified 2026-11-24** against the live OSU Department of Economics JMCB pages (submission instructions, JMCB Boards, journal home), all read directly. The Wiley Online Library pages returned HTTP 403 to automated access on 2026-11-24; the Wiley open-access APC was read via search-engine rendering restricted to onlinelibrary.wiley.com. Changes found on 2026-11-24: the OSU Editors list is now **Pok-Sang Lam, Kenneth D. West, Luc Laeven and Jing Cynthia Wu** (Sanjay Chugh and Robert DeYoung no longer listed). Re-check editor names, fees, exact length limits, portal forms, data policies, and style details before relying on them. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://onlinelibrary.wiley.com/journal/15384616** — official page used to verify or re-check JMCB scope, submission, policy, or author guidance. Access date: 2026-06.
- **https://economics.osu.edu/about-us/journal-money-credit-banking/submission-instructions** — **re-verified 2026-11-24.** Manuscripts and cover letters in PDF via **http://editorialexpress.com/jmcb**, with a TITLE PAGE giving each author's name, title and affiliation; fees **$150 subscribers / $200 non-subscribers**, refunded minus **$50** when an editor declines without consulting referees; no fee for a resubmitted revision; 1.5 line spacing; "We strongly recommend that manuscripts not exceed **40** pages" — the suggested length includes reference lists, figures and tables but excludes the online appendix; excessively long submissions may be summarily rejected; if data cannot be shared publicly, ask for a **DATA EXEMPTION** at the time of submission; author-year citations ("Barro (1981)"); asterisks mark significance at the 5 and 1 percent levels "if used".
- **https://economics.osu.edu/about-us/journal-money-credit-banking/jmcb-boards** — **re-verified 2026-11-24.** Editors: Pok-Sang Lam (Ohio State), Kenneth D. West (Wisconsin), Luc Laeven (ECB), Jing Cynthia Wu (Illinois Urbana-Champaign); Advisory Board and Associate Editors listed.
- **https://economics.osu.edu/about-us/journal-money-credit-banking** — **re-verified 2026-11-24.** Published seven times a year by Wiley-Blackwell on behalf of The Ohio State University; final files, data and codes for accepted papers are sent to the editorial office.
- **https://onlinelibrary.wiley.com/page/journal/15384616/homepage/fundedaccess.html** — Wiley open-access page; APC **US$3,990 / £2,690 / €3,330** re-confirmed 2026-11-24 via search-engine rendering restricted to onlinelibrary.wiley.com (live page HTTP 403).

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: monetary economics, banking, credit markets, financial intermediation, and macro-finance | Official journal home / author instructions |
| Publisher / owner: Wiley for the Ohio State University Department of Economics | Official journal home |
| Submission route: Wiley online submission | Author instructions or submission portal |
| Sibling boundary: Journal of Monetary Economics, Review of Economic Dynamics, Journal of Finance, and Journal of Financial Intermediation | Inferred from journal scope and local repository taxonomy |
| monetary transmission | Official pages above; re-check live before submission |
| bank balance sheets | Official pages above; re-check live before submission |
| credit frictions | Official pages above; re-check live before submission |
| central-bank relevance | Official pages above; re-check live before submission |

## Verified on official pages (2026-06)

- **Submission fee: $150 (subscribers) / $200 (non-subscribers)** (re-verified 2026-11-24). Submit a PDF at the JMCB Editorial Express portal **http://editorialexpress.com/jmcb**, with a title page listing each author's name, title, and affiliation. (OSU Department of Economics submission instructions)
- **Open-access APC (optional): US$3,990 / £2,690 / €3,330**, potentially covered by a Wiley Open Access Account or the OhioLINK–Wiley agreement (2024-01-01 to 2026-12-31). (Wiley JMCB open-access page)
- Latest issue at the 2026-06 access: **Vol. 58, Issue 3 (April 2026)**; search-engine rendering of the Wiley current-issue page on 2026-11-24 shows **Vol. 58, No. 7** (Wiley Online Library).

## Verified editors (re-verified 2026-11-24)

- **Editors:** Pok-Sang Lam (Ohio State), Kenneth D. West (Wisconsin), Luc Laeven (European Central Bank), and Jing Cynthia Wu (Illinois Urbana-Champaign), per the OSU JMCB Boards page read directly on 2026-11-24. Sanjay Chugh (Ohio State) and Robert DeYoung (Kansas), listed in the 2026-06-22 version of this map, no longer appear on the Editors list. Re-verify before tailoring a cover letter, as desks rotate.
  - https://economics.osu.edu/about-us/journal-money-credit-banking/jmcb-boards
  - https://onlinelibrary.wiley.com/page/journal/15384616/homepage/editorialboard.html (HTTP 403 on 2026-11-24; not re-read)

## Unverified / volatile items

- Exact **word limits, abstract limits, keywords/JEL, and blinding rules** remain **待核实**: the OSU submission instructions (re-read 2026-11-24) state none of them (they require a title page with author names, which suggests but does not state non-anonymized review), and the Wiley author-guidelines page was unreachable (HTTP 403) on 2026-11-24.
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of Money, Credit and Banking",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 40, "soft": true, "source": "https://economics.osu.edu/about-us/journal-money-credit-banking/submission-instructions", "note": "'strongly recommend' not exceeding 40 pages at 1.5 line spacing; includes reference lists, figures and tables, excludes the online appendix; excessively long submissions may be summarily rejected"},
    "page_limit_includes_references": {"value": true, "source": "https://economics.osu.edu/about-us/journal-money-credit-banking/submission-instructions"},
    "submission_fee": {"value": "USD 150 subscribers / 200 non-subscribers; refunded minus USD 50 on desk rejection without referees; no fee for resubmitted revisions", "source": "https://economics.osu.edu/about-us/journal-money-credit-banking/submission-instructions"},
    "portal": {"value": "Editorial Express (http://editorialexpress.com/jmcb)", "source": "https://economics.osu.edu/about-us/journal-money-credit-banking/submission-instructions"},
    "file_format": {"value": "PDF manuscript and cover letter, 1.5 line spacing, title page with each author's name, title and affiliation", "source": "https://economics.osu.edu/about-us/journal-money-credit-banking/submission-instructions"},
    "data_code_policy": {"value": "if the data cannot be shared publicly, request a data exemption at the time of submission; final files, data and code are sent to the office after acceptance", "source": "https://economics.osu.edu/about-us/journal-money-credit-banking/submission-instructions"},
    "reference_style": {"value": "author-year in text, e.g. Barro (1981); alphabetical list by author, then chronological", "source": "https://economics.osu.edu/about-us/journal-money-credit-banking/submission-instructions"},
    "apc": {"value": "optional open access: USD 3,990 / GBP 2,690 / EUR 3,330", "source": "https://onlinelibrary.wiley.com/page/journal/15384616/homepage/fundedaccess.html"},
    "review_mode": {"value": null, "note": "not stated on the official pages read as of 2026-11-24"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages read as of 2026-11-24"},
    "jel_codes_required": {"value": null, "note": "not stated on the official pages read as of 2026-11-24"}
  }
}
```

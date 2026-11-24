# Official Source Map — The Journal of Finance (JF)

All sources accessed **2026-05-30**; editor masthead and submission fee re-verified 2026-06-22. Submission rules, fees, disclosure and AI policies, data/code policy and masthead **re-verified 2026-11-23** against the live AFA pages (afajof.org/submissions/, the editorial-board page, the JF Submission Guidelines PDF Rev. March 12, 2024, and the Data and Code Sharing Policy PDF), all read directly. Changes found on 2026-11-23: the portal is named explicitly as **Editorial Express**; the 60-page limit is stated to **include internal appendices, references, figures and tables**; the per-author **disclosure statement** is a hard submission requirement; and the submissions page now carries an **AI policy** (see notes below). JF is the journal of the **American Finance Association (AFA)**, published by **Wiley-Blackwell**. Fees, limits, policies, and editors change — re-verify against the live pages before relying on any specific number.

## Primary official sources

| URL | What it verifies |
|-----|------------------|
| https://afajof.org/submissions/ | **Re-verified 2026-11-23.** Submission system: AFA online portal = **Editorial Express** ("Submit a Paper" link); tiered submission fee by economy and AFA membership (high-income member $400 / non-member $525; middle-income $100 / $150; low-income $0) — **fee amounts unchanged**; refund policy (flat $200 on desk reject; full refund if first decision > 100 days; first submission only); **60-page limit that includes appendices, references, figures and tables** (over-length papers are desk-rejected immediately), ≥1.5 spacing, 12-pt font, 1-inch side and 1.5-inch top/bottom margins; refereeing is **single-blind** (title page lists author names); **disclosure statement required at submission** — a separate disclosure for each author by name on the page after the title page, same PDF, not counted toward the 60 pages, submissions without it returned immediately, resubmissions need one too; cover letter normally unnecessary (only for code-exemption requests or COI); Internet Appendix bundled at end of same PDF, titled "Internet Appendix," not counted toward 60 pages, hosted online on acceptance; **AI policy**: AI tools may assist drafting/editing text or improving code, authors remain accountable, AI may not be a co-author, authors may briefly describe tool use in the submission; new datasets/analyses built with AI must use open-source or clearly time-stamped proprietary models with detailed prompt documentation |
| https://afajof.org/wp-content/uploads/JF_Submission_Guidelines.pdf | JF Submission Guidelines and Policies (Rev. March 12, 2024; **re-read 2026-11-23**) — authoritative text for the items above: refereeing "single blind"; title page with title, author names and an **abstract of no more than 100 words**; PDF, ≤60 pages, "This page limit includes internal appendices, reference lists, figures, and tables"; Internet Appendix at the end of the PDF; non-refundable **appeal fee $600** |
| https://afajof.org/wp-content/uploads/Data-and-Code-Sharing-Policy-1-April-2024.pdf | Data and Code Sharing Policy (current rev. 1 April 2024; **re-read 2026-11-23**, unchanged); code required with the final accepted version, published in Supplementary Information, checked by the Data Editor; Submitted Materials due generally within 30 days of conditional acceptance; a disclosure plan and any exemption request are made **at initial submission** |
| https://afajof.org/2018/09/code-sharing-policy-update/ | JF code-sharing policy history (adopted September 2016; subsequent updates) |
| https://afajof.org/editorial-board/ | Editorial board (re-verified 2026-11-23, live page, unchanged since 2026-06-22): Editor **Antoinette Schoar (MIT)**; Co-Editors **Leonid Kogan (MIT), Jonathan Lewellen (Dartmouth), Thomas Philippon (NYU), Adi Sunderam (Harvard)**; 50+ Associate Editors; Data Editor **Hong Ru (NTU)**; Assistant Data Editor **Shuoge Qian (SUSS)**; Business Manager. NOTE: Urban Jermann (Wharton) stepped down as a JF editor 1 July 2025 and was replaced by Adi Sunderam — see editorial-team-update below |
| https://afajof.org/editors/ | Current and past editors of the Journal of Finance |
| https://afajof.org/news/journal-of-finance-editorial-team-update/ | Editorial-team update (verified 2026-06-22): Urban Jermann stepped down as JF editor 1 July 2025; Adi Sunderam (HBS) replaced him; Jermann continues handling pre-July-2025 manuscripts/R&Rs for one year |
| https://afajof.org/journal-of-finance-editor-reports/ | Editor reports — submission statistics (~5% acceptance; ~33–45% desk rejection); review-timeline figures |
| https://onlinelibrary.wiley.com/doi/10.1111/jofi.13435 | Report of the Editor of The Journal of Finance for the Year 2024 (Schoar, 2025) — statistics and process |
| https://onlinelibrary.wiley.com/page/journal/15406261/homepage/forauthors.html | Wiley author guidelines (formatting, supplementary material) |
| https://onlinelibrary.wiley.com/journal/15406261 | Wiley Online Library JF homepage — publisher, ISSN 1540-6261, bimonthly, est. 1946, impact factor (7.870, 2021 JCR) |
| https://en.wikipedia.org/wiki/The_Journal_of_Finance | Overview: founded 1946; Wiley-Blackwell for AFA; bimonthly; editor-in-chief Antoinette Schoar; impact factor; finance top-3 with JFE and RFS; Smith Breeden and Brattle prizes |
| https://en.wikipedia.org/wiki/American_Finance_Association | AFA governance: society that owns and runs the Journal of Finance |

## Landmark JF papers cited in the skills (verified attribution)

- **Sharpe (1964)** CAPM — Journal of Finance.
- **Jensen (1968)** mutual-fund performance — Journal of Finance.
- **Fama & French (1992)**, "The Cross-Section of Expected Stock Returns" — Journal of Finance.
- **Jegadeesh & Titman (1993)**, momentum — Journal of Finance.
- **Carhart (1997)**, four-factor mutual-fund persistence — Journal of Finance.
- **Harvey, Liu & Zhu**, "…and the Cross-Section of Expected Returns" (factor-zoo / multiple testing) — Journal of Finance.
- Cross-check: the **Fama–French three-factor model (1993)** appeared in the **Journal of Financial Economics (JFE)**, not JF — used in the skills as a "cite to the correct top-3 journal" warning.

## UNVERIFIED / verify-before-quoting

- Exact current AE roster (re-verify the 50+ Associate Editor list before relying on any single name).
- Any masthead change after 2026-11-23 (the Co-Editor slate Kogan/Lewellen/Philippon/Sunderam was current as of that date).
- JEL codes and keywords: not stated as a requirement on the AFA submissions page or the Submission Guidelines PDF as of 2026-11-23 (the skills keep them as good practice, not as a JF rule).
- Latest impact factor beyond the 2021 JCR figure (7.870).
- Precise current acceptance rate and median review-timeline figures (use the latest editor report).

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "The Journal of Finance",
  "verified": "2026-11-23",
  "rules": {
    "main_text_pages_max": {"value": 60, "source": "https://afajof.org/submissions/", "note": "includes internal appendices, references, figures and tables; the Internet Appendix bundled at the end of the same PDF and the disclosure-statement pages are not counted; over-length papers are desk-rejected"},
    "page_limit_includes_references": {"value": true, "source": "https://afajof.org/wp-content/uploads/JF_Submission_Guidelines.pdf"},
    "abstract_words_max": {"value": 100, "source": "https://afajof.org/wp-content/uploads/JF_Submission_Guidelines.pdf"},
    "review_mode": {"value": "single-blind", "source": "https://afajof.org/submissions/", "note": "title page carries the title and all author names; no anonymization"},
    "cover_letter": {"value": "discouraged", "source": "https://afajof.org/submissions/", "note": "only for a code-sharing exemption request or a potential conflict of interest"},
    "required_statements": {"value": ["disclosure_statement"], "source": "https://afajof.org/submissions/", "note": "one disclosure per author by name, on the page after the title page in the same PDF; submissions without it are returned"},
    "submission_fee": {"value": "USD 400 AFA member / 525 non-member (high-income); 100 / 150 (middle-income); none (low-income)", "source": "https://afajof.org/submissions/"},
    "portal": {"value": "Editorial Express (via the Submit a Paper link on afajof.org/submissions/)", "source": "https://afajof.org/submissions/"},
    "file_format": {"value": "single PDF; at least 1.5 line spacing, 12-point font, 1-inch side and 1.5-inch top/bottom margins", "source": "https://afajof.org/submissions/"},
    "supplement_policy": {"value": "Internet Appendix placed at the end of the same PDF, titled 'Internet Appendix', not a separate upload; paper must be self-contained", "source": "https://afajof.org/submissions/"},
    "data_code_policy": {"value": "code (and data where shareable, else pseudo data) delivered after conditional acceptance and checked by the Data Editor; disclosure plan and any exemption request at initial submission", "source": "https://afajof.org/wp-content/uploads/Data-and-Code-Sharing-Policy-1-April-2024.pdf"},
    "llm_policy": {"value": "AI may assist drafting/editing text or code; authors accountable; AI not a co-author; tool use may be briefly described at submission; AI-built datasets/analyses need open-source or time-stamped models and prompt documentation", "source": "https://afajof.org/submissions/"},
    "jel_codes_required": {"value": null, "note": "not stated on the official pages as of 2026-11-23"},
    "keywords_required": {"value": null, "note": "not stated on the official pages as of 2026-11-23"}
  }
}
```

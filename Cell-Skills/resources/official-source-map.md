# Cell Official Source Map

Primary source map for Cell-specific facts in this pack. Official pages first checked **2026-06-23**.
Initial- and final-submission requirements, Highlights/eTOC/Graphical Abstract rules and the portal **re-verified 2026-11-23**. Access-method note: cell.com (author pages, masthead, publishing options and the graphical-abstract PDF) returns HTTP 403 (Cloudflare bot check) to `curl` and to the WebFetch renderer from this environment, so the Cell author pages (#6, #7, #8) were **read via search-engine rendering** (search restricted to cell.com); the Cell Press graphical-abstract guide was additionally read in full from its crosstalk.cell.com copy (#9); the Editorial Manager portal (#5) was read live. The masthead (#1) and the open-access charge (#2, #3) could not be re-read today (see UNVERIFIED). The dead graphical-abstract link (`.../pb-assets/journals/research/cellpress/graphical_abstract_guidelines.pdf`, HTTP 404) in `external_tools.md` was repointed to the current Cell Press guide (#8), which carries the same guidance (single panel, take-home message, clear reading direction, no data, minimal text).
Re-verify volatile items (current Editor-in-Chief, APC, submission policy) on the official page before relying on them.

## Official pages
| # | URL | What it verifies | Accessed |
|---|---|---|---|
| 1 | https://www.cell.com/cell/editors-and-staff | Cell masthead: Editor-in-Chief and deputy/scientific editors | 2026-06-23 |
| 2 | https://www.cell.com/cell/information-for-authors/publishing-options | Cell publishing options and open-access charge | 2026-06-23 |
| 3 | https://www.cell.com/open-access | Cell Press open-access policy / GPOA | 2026-06-23 |
| 4 | https://portal.issn.org/resource/ISSN/0092-8674 | ISSN registration for Cell (Cambridge) | 2026-06-23 |
| 5 | https://www.editorialmanager.com/cell | Cell Press Editorial Manager submission portal (live; banner on 2026-11-23 reads "Site under development. Do not use for live manuscript submission.") | 2026-11-23 |
| 6 | https://www.cell.com/cell/information-for-authors/submit-manuscript | Initial submission: no specific manuscript format required (title, authors with affiliations/contact details, summary or abstract, enough experimental detail); keep figure files small (1–2 MB), total no larger than 20 MB | 2026-11-23 (search-engine rendering) |
| 7 | https://www.cell.com/cell/information-for-authors/final-submission | Final submission: up to four Highlights, each no longer than 85 characters including spaces; Highlights and eTOC blurb in one separate Word file; graphical abstract required for Cell | 2026-11-23 (search-engine rendering) |
| 8 | https://www.cell.com/pb/assets/raw/shared/figureguidelines/GA_guide.pdf | Current Cell Press Graphical Abstract Guidelines: one single-panel image giving the take-home message; distinct from model figures; no data items; clear start/end reading direction; minimal text; general-purpose generative AI may not be used to create GAs (dedicated scientific illustration tools allowed); GA optional only for Cell Systems, Current Biology, Patterns, Neuron, Newton | 2026-11-23 (search-engine rendering) |
| 9 | https://crosstalk.cell.com/hubfs/Files/GA_guide.pdf | Cell Press-hosted copy of the Graphical Abstract Guidelines (2014 edition) read in full: single panel, 5.5 inches square at 300 dpi, Arial 12–16 pt, TIFF/PDF/JPG; same content rules as #8 | 2026-11-23 |

## Verified facts
- **Editor-in-Chief (verified 2026-06-23):** John Pham (Editor-in-Chief, Cell), supported by an in-house Cell Press editorial team including deputy editors (e.g., Ann Goldstein, Jiaying Tan, Sri Devi Narasimhan). Cell uses a professional in-house editor model rather than an external academic EiC. (#1)
- **Publisher / owner:** Cell Press, an imprint of Elsevier. (#1, #3)
- **APC / fees:** Hybrid journal — subscription route carries no author publication fee (color-figure charges may apply). Optional gold open access APC is reported at approximately USD 11,400 (excluding taxes); Cell Press titles are largely excluded from Elsevier read-and-publish agreements, and GPOA discounts apply for eligible countries. Confirm the live figure on the publishing-options page before relying on it. (#2, #3)
- **ISSN / portal / review model:** ISSN 0092-8674. Submission via Cell Press Editorial Manager; external peer review managed by in-house scientific editors. (#4, #5)
- **Initial submission (re-verified 2026-11-23):** format-free — no specific manuscript format is required at first submission; include title, author list with affiliations and contact details, a summary/abstract, and enough experimental detail to interpret the results; keep files small (1–2 MB each, 20 MB total). (#6)
- **Final submission (re-verified 2026-11-23):** up to four Highlights of at most 85 characters each (including spaces, avoid abbreviations), supplied with the eTOC blurb in one separate Word file; a graphical abstract is required for Cell. (#7, #8)
- **Graphical abstract (re-verified 2026-11-23):** single panel conveying the take-home message, distinct from the paper's model figures, no data, clear reading direction, simple labels; general-purpose generative AI may not be used to create it. (#8, #9)

## UNVERIFIED / 待核实
- Editor-in-Chief (John Pham) and the ~USD 11,400 open-access charge: masthead and publishing-options pages returned 403 on 2026-11-23; web search found no change but no official confirmation.
- Summary word cap (pack uses ≤ ~150 words), eTOC blurb length for Cell (pack uses ~50 words) and main-text length budget (pack uses ~45,000 characters): not shown for Cell in the search renderings on 2026-11-23 (sister journals state 150-word summaries and 50- or 80-word eTOC blurbs).
- Review model (single-blind, or an optional double-blind route as some Cell Press journals offer): not confirmed for Cell on 2026-11-23.
- Editorial Manager banner "Site under development. Do not use for live manuscript submission." seen on the Cell portal home page on 2026-11-23 — unclear whether submissions are moving to another system; check the submit-manuscript page (#6) before submitting.

## Live-check rules
- Treat the Editor-in-Chief and APC as volatile; re-confirm on the masthead/charges page before submission.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Cell",
  "verified": "2026-11-23",
  "rules": {
    "file_format": {"value": "no specific format required at initial submission (title, authors, summary, enough experimental detail); files 1–2 MB each, 20 MB total", "source": "https://www.cell.com/cell/information-for-authors/submit-manuscript", "note": "read via search-engine rendering; Highlights (up to four, ≤85 characters each), eTOC blurb and graphical abstract are final-submission items"},
    "portal": {"value": "Cell Press Editorial Manager", "source": "https://www.editorialmanager.com/cell", "note": "portal home showed a 'Site under development' banner on 2026-11-23"},
    "required_statements": {"value": null, "note": "initial submission is format-free; Highlights, eTOC blurb and graphical abstract are required at final submission (not at initial submission)"},
    "abstract_words_max": {"value": null, "note": "Cell summary cap not shown on the official pages read on 2026-11-23"},
    "review_mode": {"value": null, "note": "not confirmed on the official pages as of 2026-11-23"},
    "apc": {"value": null, "note": "publishing-options page not readable on 2026-11-23; pack records ~USD 11,400 from 2026-06-23"}
  }
}
```

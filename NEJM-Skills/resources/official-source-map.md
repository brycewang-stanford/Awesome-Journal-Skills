# New England Journal of Medicine (NEJM) Official Source Map

Primary source map for NEJM-specific facts in this pack. Official pages first checked **2026-06-23**.
Original Article limits, abstract format and required statements **re-verified 2026-11-23** against the NEJM Author Center pages (#7, #8, #9) and editorial policies (#4). Access-method note: every nejm.org page returns HTTP 403 (Cloudflare bot check) to `curl`, to the WebFetch renderer and to a reader proxy from this environment, and the Internet Archive was offline, so the 2026-11-23 re-check was **read via search-engine rendering** of the official nejm.org pages (search results restricted to nejm.org). No change found against the pack; the masthead and the peer-review model could not be re-read today (see UNVERIFIED).
Re-verify volatile items (current Editor-in-Chief, APC, submission policy) on the official page before relying on them.

## Official pages
| # | URL | What it verifies | Accessed |
|---|---|---|---|
| 1 | https://www.nejm.org/about-nejm/editors-and-publishers | Masthead: Editor-in-Chief and editorial leadership | 2026-06-23 |
| 2 | https://www.nejmgroup.org/learn-about-nejm-group/leadership/eric-j-rubin/ | NEJM Group leadership profile for Eric J. Rubin | 2026-06-23 |
| 3 | https://www.massmed.org/News/Press-Releases/Eric-J--Rubin,-MD,-PhD,-Named-Editor-in-Chief-of-the-New-England-Journal-of-Medicine-and-NEJM-Group/ | MMS press release: Rubin named EiC; MMS is owner/publisher | 2026-06-23 |
| 4 | https://www.nejm.org/about-nejm/editorial-policies | Editorial/peer-review policies, ethics, authorship; trial registration before onset of enrollment; ICMJE data-sharing statement at submission | 2026-11-23 (search-engine rendering) |
| 5 | https://www.nejm.org/about-nejm/frequently-asked-questions | Submission, access, and open-access FAQs | 2026-06-23 |
| 6 | https://portal.issn.org/resource/ISSN/0028-4793 | ISSN registration for NEJM (print) | 2026-06-23 |
| 7 | https://www.nejm.org/author-center/article-types | Original Article: maximum 2,700 words (excluding abstract, figure legends, table notes); maximum of 5 tables and figures; up to 40 references | 2026-11-23 (search-engine rendering) |
| 8 | https://www.nejm.org/author-center/new-manuscripts | Abstract of not more than 250 words with four labeled paragraphs (Background, Methods, Results, Conclusions) plus trial registration number; references numbered in order of first citation | 2026-11-23 (search-engine rendering) |
| 9 | https://www.nejm.org/author-center/frequently-asked-questions | Author FAQ: online submission only (no email/post/fax); protocol and statistical analysis plan uploaded with trials | 2026-11-23 (search-engine rendering) |

## Verified facts
- **Editor-in-Chief (verified 2026-06-23):** Eric J. Rubin, MD, PhD (Harvard T.H. Chan School of Public Health; Brigham and Women's Hospital). EiC of NEJM and NEJM Group since September 2019. (#1, #2, #3) A 2026-11-23 web search found no announced successor, but the masthead itself could not be re-read.
- **Publisher / owner:** Massachusetts Medical Society (NEJM Group). (#3)
- **APC / fees:** Default subscription route carries no author publication fee. NEJM offers an optional gold open-access add-on (CC BY, Plan S-compliant) whose APC is among the highest in medicine; the exact figure is set by the publisher and not consistently posted publicly — confirm on the live charges/OA page before relying on a number. (#5)
- **ISSN / portal / review model:** ISSN 0028-4793 (print). Single-blind external peer review with editorial board oversight (as recorded 2026-06-23); submission via NEJM's online manuscript system only. (#4, #5, #6, #9)

### Original Article — re-verified 2026-11-23 via search-engine rendering (#7, #8, #4)
- **Length:** maximum 2,700 words, excluding the abstract, figure legends and table notes; maximum of 5 tables and figures; up to 40 references. (#7)
- **Abstract:** not more than 250 words, four labeled paragraphs — Background, Methods, Results, Conclusions — with the trial registration number. (#8)
- **Trial registration:** trials must be registered in an acceptable registry before the onset of patient enrollment (ICMJE / WHO ICTRP primary registries). (#4)
- **Data sharing:** NEJM follows the ICMJE requirement of a data sharing statement at submission for clinical trials, and a data sharing plan in the trial registration for trials enrolling from 2019. (#4)
- **Disclosures / authorship:** ICMJE disclosure form; each author attests to ICMJE authorship criteria before publication. (#4)
- **Trial documents:** protocol and statistical analysis plan submitted with clinical trials (if applicable). (#9)

## UNVERIFIED / 待核实
- Peer-review model (single-blind): recorded 2026-06-23; not re-readable on 2026-11-23 (nejm.org 403; search snippets did not cover it). Kept in the prose, left `null` in the rules block.
- Editor-in-Chief: masthead (#1) not re-readable on 2026-11-23 (403); search found no successor announcement.
- Whether a cover letter is required or optional, and whether the ICMJE disclosure forms are due at submission or later: search renderings were not conclusive on 2026-11-23.
- Optional OA fee: not publicly posted; not re-read.

## Live-check rules
- Treat the Editor-in-Chief and APC as volatile; re-confirm on the masthead/charges page before submission.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "The New England Journal of Medicine",
  "verified": "2026-11-23",
  "rules": {
    "main_text_words_max": {"value": 2700, "source": "https://www.nejm.org/author-center/article-types", "note": "Original Article; excludes abstract, figure legends and table notes; read via search-engine rendering (nejm.org blocks automated access)"},
    "exhibits_max": {"value": 5, "source": "https://www.nejm.org/author-center/article-types", "note": "tables and figures combined, Original Article"},
    "references_max": {"value": 40, "source": "https://www.nejm.org/author-center/article-types", "note": "Original Article"},
    "abstract_words_max": {"value": 250, "source": "https://www.nejm.org/author-center/new-manuscripts"},
    "abstract_format": {"value": "structured", "source": "https://www.nejm.org/author-center/new-manuscripts", "note": "four labeled paragraphs: Background, Methods, Results, Conclusions; include trial registration number"},
    "required_statements": {"value": ["structured_abstract", "trial_registration", "data_availability"], "source": "https://www.nejm.org/about-nejm/editorial-policies", "note": "trial_registration (before onset of enrollment) and the ICMJE data sharing statement apply to clinical trials; ICMJE disclosure form required, timing not confirmed on 2026-11-23; protocol + SAP with trials"},
    "review_mode": {"value": null, "note": "pack records single-blind (2026-06-23); not re-readable on the official pages on 2026-11-23"},
    "reference_style": {"value": "numbered in order of first citation", "source": "https://www.nejm.org/author-center/new-manuscripts"},
    "apc": {"value": null, "note": "optional OA fee not posted on the official pages as of 2026-11-23"}
  }
}
```

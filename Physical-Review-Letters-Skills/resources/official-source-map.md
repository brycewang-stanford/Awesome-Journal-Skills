# Physical Review Letters (PRL) Official Source Map

Primary source map for *Physical Review Letters (PRL)*-specific facts in this pack. Official pages first checked **2026-06-23**.
Submission rules (Letter length and End Matter, word-count procedure, justification paragraph, Data Availability Statement, AI-use disclosure, peer-review model), fees and masthead **re-verified 2026-11-24** against the live APS pages (#1, #2, #5-#9), read by direct fetch (`curl`). Changes since 2026-06-23: the PRL open-access APC is now **USD 4,140** (2026 APC table), not "approximately $2,700"; the word-count procedure **excludes** the abstract, references and acknowledgments (earlier pack text wrongly said they count); the 100-word justification paragraph, two-page End Matter and the in-paper "AI Use Disclosure" heading are now recorded.
Re-verify volatile items (current Lead Editor, APC, submission policy) on the official page before relying on them.

## Official pages
| # | URL | What it verifies | Accessed |
|---|---|---|---|
| 1 | https://journals.aps.org/prl/about | Scope (ten sections), acceptance criteria, APS publisher, CC-BY APC route, SCOAP3 for hep papers since 2018, APC waivers for lower-income countries, ISSN 1079-7114 (online) / 0031-9007 (print) | 2026-11-24 |
| 2 | https://journals.aps.org/prl/authors | Publishing Guidelines: Letters length limit 3750 words (about four journal pages for the core between the abstract and the Acknowledgments) plus up to two pages of End Matter that does not count; waivers of 1/2 page or more on request, not appealable; Essays 3750 words; Comments and Replies 750 words; a PDF is all that is needed for peer review, LaTeX (REVTeX, preferred) or Word source converted on submission; 100-word justification paragraph at submission; Data Availability Statement in all published articles, entered during submission; substantive AI use disclosed in the paper; "All APS journals follow the single-anonymized peer review procedures"; cover letter contents (context, key findings, submission history, recommended/excluded referees); Optional Page Charge $830 ($310 Comment/Reply), not required under the subscription model; print colour $1090 first figure, $595 each additional; submission via the APS Submission Server | 2026-11-24 |
| 3 | https://journals.aps.org/prl/edannounce/APS-appoints-Dr.-Rafael-Fernandes-as-the-newest-Lead-Editor-of-Physical-Review-Letters | Lead Editor appointment (APS announcement) | 2026-06-23 |
| 4 | https://www.aps.org/apsnews/2025/10/meet-lead-editor-prl | Lead Editor profile / confirmation | 2026-06-23 |
| 5 | https://journals.aps.org/prl/staff | Editors of PRL: Robert Garisto, Chief Editor; Rafael Fernandes, Lead Editor (University of Illinois Urbana-Champaign); senior and associate editors | 2026-11-24 |
| 6 | https://journals.aps.org/authors/apcs | 2026 APC table: Physical Review Letters, hybrid, **$4140**; fees covered centrally under institutional OA agreements or SCOAP3; no APC for comments and corrections | 2026-11-24 |
| 7 | https://journals.aps.org/authors/length-guide | Length table (PRL Letter 3,750 words; Comment/Reply 750 words) and word-count procedure: count body text, captions and footnotes/endnotes; exclude title, author list, abstract, PhySH/DOI, references, byline footnotes and acknowledgments; displayed math 16 words per row (32 double-column); single-column figure (150 / aspect ratio) + 20 words, double-column [300 / (0.5 × aspect ratio)] + 40; tables 13 + 6.5 words per line (26 + 13 double-column); REVTeX 4.2 with the `prl` option, a 4-page Letter is likely to conform | 2026-11-24 |
| 8 | https://journals.aps.org/authors/appropriate-use-ai-tools | AI cannot be an author; substantive AI use (reasoning/interpretation, drafting claims, literature synthesis beyond routine organization, figure generation, image analysis) disclosed during submission and in the paper under the heading "AI Use Disclosure" below the Conflicts of Interest statement; AI used in the research described in methods; light polishing need not be disclosed | 2026-11-24 |
| 9 | https://authors.aps.org/Submissions/login/new | APS Submission Server (linked from #2) | 2026-11-24 |

## Verified facts
- **Lead Editor (re-verified 2026-11-24):** Rafael M. Fernandes, condensed-matter theorist, University of Illinois Urbana-Champaign; three-year term began **1 September 2025** (renewable). He serves as lead scientific advisor and chairs the PRL editorial board. The staff page lists **Robert Garisto as Chief Editor**, heading APS's professional editorial staff; divisional associate editors advise and adjudicate appeals. (#3, #4, #5)
- **Publisher / owner:** American Physical Society (APS); PRL is the APS flagship physics letters journal. (#1)
- **Length (re-verified 2026-11-24):** a Letter is limited to **3750 words** for the core (between the abstract and the Acknowledgments, about four journal pages), plus up to **two pages of End Matter** (appendixes and specialist detail, placed after the references) that does not count against the core limit. Figures, tables and displayed math count as word equivalents by the length-guide formulas; the title, author list, abstract, references, byline footnotes and acknowledgments are excluded. Comments and Replies: 750 words. (#2, #7)
- **At submission:** a PDF suffices for review (REVTeX source preferred); a **100-word justification paragraph** stating why the paper meets PRL's criteria; a **Data Availability Statement** entered during submission (required in all published articles); an **AI use disclosure** if AI was used substantively; a cover letter with context, key findings, submission history and referee suggestions/exclusions. (#2, #8)
- **APC / fees (re-verified 2026-11-24):** Hybrid model — **no required author charge** under the traditional subscription route. Optional CC-BY gold open access APC **USD 4,140** (2026). An **Optional Page Charge** of **$830** ($310 for a Comment/Reply) is voluntary. Print colour figures cost $1090 for the first and $595 for each additional (online colour free). PRL is a **SCOAP3** participating journal (hep articles open access at no cost to authors). (#1, #2, #6)
- **ISSN:** 0031-9007 (print) / 1079-7114 (online). (#1)
- **Submission portal / review model:** submit via the APS Submission Server; **single-anonymized** peer review (all APS journals). (#2, #9)

## Live-check rules
- Treat the Lead Editor and APC/page-charge figures as volatile; re-confirm on the PRL author, staff and APC pages before submission.
- Subject categories and editor tracks evolve — verify current options on the official APS / PRL author page each cycle.
- No abstract word or character limit is stated on the PRL author page or the length guide as of 2026-11-24.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Physical Review Letters",
  "verified": "2026-11-24",
  "rules": {
    "main_text_words_max": {"value": 3750, "source": "https://journals.aps.org/prl/authors", "note": "Letter core between abstract and Acknowledgments; figures, tables and displayed math count as word equivalents (length guide); abstract, references, acknowledgments excluded; up to two pages of End Matter not counted"},
    "page_limit_includes_references": {"value": false, "source": "https://journals.aps.org/authors/length-guide"},
    "review_mode": {"value": "single-blind", "source": "https://journals.aps.org/prl/authors", "note": "single-anonymized, all APS journals"},
    "required_statements": {"value": ["data_availability"], "source": "https://journals.aps.org/prl/authors", "note": "Data Availability Statement entered during submission and printed in every article; a 100-word justification paragraph is also requested at submission"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://journals.aps.org/authors/appropriate-use-ai-tools", "note": "only if AI was used substantively; heading 'AI Use Disclosure' below the Conflicts of Interest statement"},
    "template": {"value": "REVTeX 4.2 with the prl option (preferred) or the APS Word template; a PDF suffices for review", "source": "https://journals.aps.org/authors/length-guide"},
    "portal": {"value": "APS Submission Server (https://authors.aps.org/Submissions/login/new)", "source": "https://journals.aps.org/prl/authors"},
    "apc": {"value": "USD 4,140 (2026) for optional CC-BY gold OA; none on the subscription route; SCOAP3 covers eligible hep Letters", "source": "https://journals.aps.org/authors/apcs"},
    "submission_fee": {"value": "none; Optional Page Charge USD 830 (310 for Comment/Reply) is voluntary", "source": "https://journals.aps.org/prl/authors"},
    "llm_policy": {"value": "AI cannot be an author; substantive AI use disclosed at submission and in the paper under 'AI Use Disclosure'; light editing exempt", "source": "https://journals.aps.org/authors/appropriate-use-ai-tools"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```

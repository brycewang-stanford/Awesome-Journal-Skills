# PNAS Official Source Map

Primary source map for *Proceedings of the National Academy of Sciences (PNAS)*-specific facts in this pack. Official pages first checked **2026-06-23**.
Masthead, Research Report length, abstract / Significance Statement / keyword limits and required manuscript statements **re-verified 2026-11-23**. Access-method note: pnas.org HTML pages return HTTP 403 (Cloudflare bot check) to `curl` and to the WebFetch renderer, so the author-center page (#5) was **read via search-engine rendering** (search restricted to pnas.org); the current masthead PDF (#6, dated August 2026) and the main-manuscript template (#7) download directly from pnas.org and were read in full. **Changed:** the masthead now lists **Neil H. Shubin** as President of the Academy (the 2022 masthead PDF previously cited, #1, named Marcia K. McNutt); May R. Berenbaum remains Editor-in-Chief. The publication-charges page (#2) could not be re-read (see UNVERIFIED).
Re-verify volatile items (current Editor-in-Chief, APC, submission policy) on the official page before relying on them.

## Official pages
| # | URL | What it verifies | Accessed |
|---|---|---|---|
| 1 | https://www.pnas.org/cms/asset/ad9ae008-4d5d-4dc3-8905-620effc87dfe/masthead.pdf | Older official masthead (January 2022 PDF; superseded by #6) | 2026-06-23 |
| 2 | https://www.pnas.org/author-center/publication-charges | Publication charges / open-access fees | 2026-06-23 |
| 3 | https://www.pnas.org/about/staff-directory | Editorial leadership / staff | 2026-06-23 |
| 4 | https://www.nationalacademies.org/news/entomologist-may-r-berenbaum-of-the-university-of-illinois-at-urbana-champaign-named-pnas-editor-in-chief | EiC appointment (NAS announcement) | 2026-06-23 |
| 5 | https://www.pnas.org/author-center/submitting-your-manuscript | Research Reports: preferred length 6 pages, maximum 12 pages; a standard 6-page article ≈ 4,000 words, 50 references, 4 medium-size figures/tables; abstract ≤250 words; Significance Statement ≤120 words; at least three keywords; submission only through the PNAS manuscript tracking system | 2026-11-23 (search-engine rendering) |
| 6 | https://www.pnas.org/cms/asset/f93960f4-8d43-47e6-9bb8-eca2d1cdd4d4/masthead.pdf | Current masthead (PDF created 2026-08-12): President of the Academy Neil H. Shubin; Editor-in-Chief May R. Berenbaum; Executive Editor Daniel H. Salsbury | 2026-11-23 |
| 7 | https://www.pnas.org/pb-assets/authors/PNASTemplateforMainManuscript-1755285180130.docx | PNAS Template for Main Manuscript: abstract "may not exceed 250 words" (up to three cited non-numerical references); Significance Statement "should not exceed 120 words but should be at least 50 words", no references; keywords "at least three and no more than five"; Author Contributions, Competing Interest Statement and Classification on the title page; references in order of citation | 2026-11-23 |

## Verified facts
- **Editor-in-Chief (re-verified 2026-11-23):** May R. Berenbaum, entomologist, University of Illinois at Urbana-Champaign; listed as Editor-in-Chief on the current official PNAS masthead (President of the Academy: Neil H. Shubin). (#4, #6)
- **Publisher / owner:** National Academy of Sciences (NAS); PNAS is the official journal of the NAS. Multidisciplinary. (#1, #6)
- **APC / fees:** Open-access publication charge approximately **$4,975** (immediate OA with site license) / **$5,475** (without site license); **delayed (after embargo) OA approximately $2,575.** Discounts and waivers apply under transformative/read-and-publish agreements (e.g. UC, Jisc, Max Planck) and for lower-income-country corresponding authors. **Confirm the live figure on the publication-charges page — fees change yearly.** (#2) Not re-read on 2026-11-23.
- **ISSN:** 0027-8424 (print) / 1091-6490 (online). (#1)
- **Submission portal / review model:** Submit via the PNAS online system (pnascentral); no email submissions. Two tracks — **Direct Submission** (editor-assigned, standard peer review) and **Contributed Submission** (an NAS member communicates their own paper and arranges review); all Research Reports are reviewed by at least two independent experts. See `pnas-track`. (#3, #5)

### Research Reports — re-verified 2026-11-23 (#5, #7)
- **Length:** preferred 6 pages, maximum 12 pages; a standard 6-page article is approximately 4,000 words, 50 references and 4 medium-size graphical elements (figures/tables).
- **Abstract:** may not exceed 250 words; single paragraph; up to three cited (non-numerical) references.
- **Significance Statement:** at most 120 words and at least 50 words; no references; for readers outside the field.
- **Title page items:** Author Contributions, Competing Interest Statement, Classification (major + minor; dual classifications allowed but not within the same major classification), Keywords (at least three, no more than five).
- **References:** listed in order of citation.

## UNVERIFIED / 待核实
- Publication charges ($4,975 / $5,475 / $2,575): the charges page (#2) returned 403 on 2026-11-23; kept from 2026-06-23.
- Review blinding (single vs double anonymous for Direct Submissions): not stated in the 2026-11-23 search renderings.
- Data-availability statement wording and AI policy for flagship PNAS: not re-read on 2026-11-23 (editorial-policies page 403).

## Live-check rules
- Treat the Editor-in-Chief and APC figures as volatile; re-confirm on the masthead and the publication-charges page before submission.
- Submission tracks and member-contribution rules evolve — verify the current track options on the PNAS author center each cycle.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "PNAS",
  "verified": "2026-11-23",
  "rules": {
    "main_text_pages_max": {"value": 12, "source": "https://www.pnas.org/author-center/submitting-your-manuscript", "note": "Research Report maximum; preferred 6 pages (~4,000 words, 50 references, 4 medium-size figures/tables); read via search-engine rendering"},
    "abstract_words_max": {"value": 250, "source": "https://www.pnas.org/pb-assets/authors/PNASTemplateforMainManuscript-1755285180130.docx"},
    "abstract_format": {"value": "unstructured", "source": "https://www.pnas.org/pb-assets/authors/PNASTemplateforMainManuscript-1755285180130.docx", "note": "single paragraph"},
    "keywords_min": {"value": 3, "source": "https://www.pnas.org/pb-assets/authors/PNASTemplateforMainManuscript-1755285180130.docx"},
    "keywords_max": {"value": 5, "source": "https://www.pnas.org/pb-assets/authors/PNASTemplateforMainManuscript-1755285180130.docx"},
    "keywords_required": {"value": true, "source": "https://www.pnas.org/author-center/submitting-your-manuscript"},
    "required_statements": {"value": ["significance_statement", "author_contributions", "conflict_of_interest", "keywords"], "source": "https://www.pnas.org/pb-assets/authors/PNASTemplateforMainManuscript-1755285180130.docx", "note": "Significance Statement 50-120 words, no references; Author Contributions and Competing Interest Statement on the title page; Classification also required (no schema key)"},
    "reference_style": {"value": "numbered in order of citation", "source": "https://www.pnas.org/pb-assets/authors/PNASTemplateforMainManuscript-1755285180130.docx"},
    "template": {"value": "PNAS Template for Main Manuscript (.docx)", "source": "https://www.pnas.org/pb-assets/authors/PNASTemplateforMainManuscript-1755285180130.docx"},
    "review_mode": {"value": null, "note": "blinding not confirmed on the official pages as of 2026-11-23; at least two independent expert reviewers"},
    "apc": {"value": null, "note": "publication-charges page not readable on 2026-11-23; pack records ~USD 4,975 / 5,475 / 2,575 from 2026-06-23"}
  }
}
```

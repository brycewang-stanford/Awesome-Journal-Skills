# Cancer Cell Official Source Map

Primary source map for Cancer Cell-specific facts in this pack. Official pages first checked **2026-06-23**.
Submission requirements (initial vs final files, length and display-item limits, Summary/Highlights/eTOC, required sections, declarations, AI policy, review model), APC and masthead **re-verified 2026-11-24**.
Access-method note: www.cell.com returns HTTP 403 to `curl` and to the fetch tool from this environment, and the Internet Archive's newest captures of the Cancer Cell author pages date from January 2025. The official **Cancer Cell Final File Requirements** PDF (#6, served from cell.com's `pb-assets`) and the Cell Press events page on info.cell.com (#7) were read by direct fetch; the HTML author pages (#3, #8-#11) were read via search-engine rendering restricted to the cell.com domain. Nothing contradicted the 2026-06-23 facts; length, Summary, Highlights, eTOC, display-item and title limits are newly recorded from #6.
Re-verify volatile items (current Editor-in-Chief, APC, submission policy) on the official page before relying on them.

## Official pages
| # | URL | What it verifies | Accessed |
|---|---|---|---|
| 1 | https://www.cell.com/cancer-cell/editors-and-staff | Cancer Cell masthead: Editor-in-Chief and editorial team (403 from this environment on 2026-11-24) | 2026-06-23 |
| 2 | https://www.cell.com/cancer-cell/interviews | Cancer Cell EiC interview (Steve Mao); search rendering 2026-11-24 still titles it "Editor-in-Chief Steve Mao" | 2026-11-24 |
| 3 | https://www.cell.com/cancer-cell/information-for-authors/publishing-options | Publishing options: open-access APC **USD 10,400**; colour-figure charges $1,000 first / $275 each additional, waived for open access (search rendering) | 2026-11-24 |
| 4 | https://en.wikipedia.org/wiki/Cancer_Cell_(journal) | Background, ownership, ISSN | 2026-06-23 |
| 5 | https://www.cell.com/open-access | Cell Press open-access policy / GPOA; APC table lists Cancer Cell at USD 10,400 excluding tax (search rendering) | 2026-11-24 |
| 6 | https://www.cell.com/pb-assets/journals/EM/MasterFFCs/CCELLFFC-1753703594713.pdf | Final File Requirements (direct fetch): main document order (title … Summary, Introduction, Results, Discussion, Resource Availability, Acknowledgments, Author Contributions, Declaration of Interests, legends, STAR Methods, References); title no more than 145 characters including spaces; Summary one paragraph of 150 words or fewer; no more than 7,000 words for Articles and 4,000 words for Reports (title page included; STAR Methods, supplemental video/Excel legends and References excluded); no more than eight main figures and/or tables; Resource Availability with Lead Contact, Materials Availability, Data and Code Availability; Data S1 raw-data file; Highlights 3–4 bullets of no more than 85 characters including spaces; eTOC blurb no longer than 50 words, third person; Declaration of Interests form uploaded and mirrored in a manuscript section; generative-AI declaration section after Declaration of Interests if AI was used in writing; Graphical Abstract 1200 × 1200 px; numbered superscript references | 2026-11-24 |
| 7 | https://info.cell.com/meet-cell-press-editors-cancer-research | Cell Press editor-meeting page (direct fetch) listing "Steve Mao, Editor-in-chief \| Cancer Cell" | 2026-11-24 |
| 8 | https://www.cell.com/cancer-cell/information-for-authors/submit-manuscript | Initial submission (search rendering): no specific manuscript format required; PDF or Word (LaTeX as PDF); keep figures ~1–2 MB and the total under 20 MB; cover letter seen by editors only; declaration of interests form required at initial submission; related manuscripts disclosed and uploaded | 2026-11-24 |
| 9 | https://www.cell.com/cancer-cell/information-for-authors/journal-policies | Journal policies (search rendering): declaration of interests in a form and in the text; AI use declared at submission, AI only to improve readability/language in writing, other AI use reported in (STAR) Methods; preprint-server section exists (text not rendered) | 2026-11-24 |
| 10 | https://www.cell.com/information-for-authors/after-you-submit | Cell Press peer review (search rendering): single-anonymous peer review is the standard across Cell Press journals; double-anonymous opt-in named only for One Earth and Immunity | 2026-11-24 |
| 11 | https://www.cell.com/cancer-cell/information-for-authors/article-types | Article types (search rendering): Articles (main text about 7,000 words, no more than eight figures and/or tables), Reports, Previews | 2026-11-24 |

## Verified facts
- **Editor-in-Chief (re-verified 2026-11-24):** Steve Mao (Editor-in-Chief, Cancer Cell; also a Cell Press Publishing Director). EiC since 2020; in-house Cell Press editor model. (#2, #7; masthead #1 not reachable today)
- **Publisher / owner:** Cell Press, an imprint of Elsevier. (#4, #5)
- **APC / fees (re-verified 2026-11-24):** Hybrid journal — subscription route carries no author publication fee (colour-figure charges $1,000 first figure, $275 each additional, waived under open access). Optional gold open access APC **USD 10,400** (excluding taxes); GPOA discounts apply for eligible countries. (#3, #5)
- **Initial vs final submission:** initial submissions need no specific format (PDF or Word; total under 20 MB), but the Declaration of Interests form is required from the start. The Final File Requirements then impose: Articles ≤ 7,000 words and Reports ≤ 4,000 words (STAR Methods and References excluded), Summary ≤ 150 words, title ≤ 145 characters, ≤ 8 main figures/tables, Highlights 3–4 bullets ≤ 85 characters, eTOC blurb ≤ 50 words, Graphical Abstract, Resource Availability (Lead Contact / Materials Availability / Data and Code Availability), Author Contributions and Declaration of Interests sections. (#6, #8)
- **AI policy:** declare generative-AI use in writing in a section after Declaration of Interests; AI used for analysis goes in STAR Methods. (#6, #9)
- **ISSN / portal / review model:** ISSN 1535-6108 (print), 1878-3686 (online). Submission via Cell Press Editorial Manager; external peer review managed by in-house scientific editors; single-anonymous review is the Cell Press standard. (#4, #8, #10)

## UNVERIFIED / 待核实
- The Cancer Cell masthead page (#1) and the preprint-policy text on #9 could not be read on 2026-11-24 (HTTP 403; search rendering omitted the preprint section). Tried: `curl`, fetch tool, Internet Archive (newest capture January 2025), search rendering restricted to cell.com.
- Whether Cancer Cell itself offers a double-anonymous opt-in: #10 names only One Earth and Immunity, so the pack assumes single-anonymous.

## Live-check rules
- Treat the Editor-in-Chief and APC as volatile; re-confirm on the masthead/charges page before submission.
- The word, Summary and display-item limits come from the final-file checklist; initial submissions are format-free, so treat them as targets at first submission and hard limits at final submission.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Cancer Cell",
  "verified": "2026-11-24",
  "rules": {
    "main_text_words_max": {"value": 7000, "soft": true, "source": "https://www.cell.com/pb-assets/journals/EM/MasterFFCs/CCELLFFC-1753703594713.pdf", "note": "Articles (Reports 4,000); STAR Methods, supplemental legends and References excluded; enforced at final submission, initial submissions are format-free"},
    "abstract_words_max": {"value": 150, "soft": true, "source": "https://www.cell.com/pb-assets/journals/EM/MasterFFCs/CCELLFFC-1753703594713.pdf", "note": "Summary, single paragraph; final-file requirement"},
    "exhibits_max": {"value": 8, "soft": true, "source": "https://www.cell.com/pb-assets/journals/EM/MasterFFCs/CCELLFFC-1753703594713.pdf", "note": "main figures and/or tables; final-file requirement"},
    "title_chars_max": {"value": 145, "soft": true, "source": "https://www.cell.com/pb-assets/journals/EM/MasterFFCs/CCELLFFC-1753703594713.pdf", "note": "including spaces; final-file requirement"},
    "abstract_format": {"value": "unstructured", "source": "https://www.cell.com/pb-assets/journals/EM/MasterFFCs/CCELLFFC-1753703594713.pdf", "note": "Summary is a single paragraph"},
    "review_mode": {"value": "single-blind", "source": "https://www.cell.com/information-for-authors/after-you-submit", "note": "single-anonymous is the Cell Press standard; read via search-engine rendering"},
    "separate_upload_statements": {"value": ["conflict_of_interest"], "source": "https://www.cell.com/cancer-cell/information-for-authors/submit-manuscript", "note": "Declaration of Interests form required at initial submission (mirrored as a manuscript section at final submission)"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://www.cell.com/pb-assets/journals/EM/MasterFFCs/CCELLFFC-1753703594713.pdf", "note": "only if generative AI was used in writing; section after Declaration of Interests"},
    "required_statements": {"value": null, "note": "initial submissions need no specific format as of 2026-11-24; at final submission Resource Availability (incl. Data and Code Availability), Author Contributions, Declaration of Interests, Highlights, eTOC blurb and Graphical Abstract are required"},
    "file_format": {"value": "initial: PDF or Word (LaTeX as PDF), total under 20 MB; final: editable Word (or LaTeX source), figures as separate TIFF/PDF", "source": "https://www.cell.com/cancer-cell/information-for-authors/submit-manuscript"},
    "portal": {"value": "Cell Press Editorial Manager", "source": "https://www.cell.com/cancer-cell/information-for-authors/submit-manuscript"},
    "apc": {"value": "USD 10,400 excluding taxes for optional gold OA; none on the subscription route (colour figures $1,000 + $275 each, waived for OA)", "source": "https://www.cell.com/cancer-cell/information-for-authors/publishing-options"},
    "llm_policy": {"value": "declare generative-AI use in writing in a section after Declaration of Interests; AI only to improve readability/language; AI used in analysis described in STAR Methods", "source": "https://www.cell.com/cancer-cell/information-for-authors/journal-policies"}
  }
}
```

# Submission-readiness report: Otani and Yang (arXiv:2611.21070) → AER: Insights (hypothetical)

*This is a showcase run of `rt-submission-readiness` on a public CC BY 4.0 preprint, dated
2026-11-23. It is a constructive pre-check, not a verdict, and it does not predict
acceptance or rejection. The stage outputs are in this directory; see [README.md](README.md).*

```text
【Venue】American Economic Review: Insights (rules verified 2026-11-23; pack AER-Insights-Skills)
【Stage 0 · Preflight】NO-GO, on anonymization only.
   As run:  tex 3 FAIL · pdf 4 FAIL 1 FLAG · pdf --online 4 FAIL 3 FLAG (several false or misframed; see table)
   Now:     tex 2 FAIL 1 FLAG · pdf 3 FAIL 1 FLAG · pdf --online 3 FAIL 1 FLAG (+ INFO: figure-legend number,
            in-file appendix, 3 grey-literature references)
   Real FAILs: ANON-AUTHOR, ANON-ACK, ANON-META (PDF Author field). Real FLAG: significance asterisks
   (EXH-STARS), which the AEA style guide forbids. Exhibits 5/5; main text ≈5,050 words against the
   6,000 cap that remains after 5 exhibits.
【Stage 1 · Scorecard】1 Fit FLAG · 2 Contribution FLAG · 3 Identification FLAG (top priority) ·
   4 Robustness FLAG · 5 Exhibits FLAG · 6 Exposition FLAG · 7 Mechanics FAIL (anonymization) ·
   8 Data/code FLAG (confidential platform data, no access statement) · 9 Objections FLAG
【Stage 2 · Panel】inline panel, form C. AE: send out, desk-reject risk medium. Band: centred on reject
   as written (AER: Insights has no R&R); conditional accept realistic if D1 is resolved and D2–D3 are
   fixed before submission.
   D1 timing of the minimum-wage revisions vs exposure: the paper's own Table A5 col. 5 moves the wage
      estimate from −0.272 to −0.152 → aeri-identification
   D2 importance: magnitude in yen and earnings; like-for-like contrast with Kurmann et al. on wages
      → aeri-topic-selection + aeri-literature-positioning
   D3 mechanism claims beyond what Table A8 / Fig. A4 support (hotel wage n.s.; unweighted band gap
      n.s.) → aeri-writing-style + aeri-tables-figures
【Stage 3 · Polish】16 claims audited: 9 supported, 6 stronger than the evidence, 1 unsupported (§5
   generality), 0 contradicted. First-page test: magnitude ✗; answer arrives late (¶6, p.4).
【Stage 4 · Letter & statements】cover letter optional → no standalone letter, a form-field note instead.
   Drafted: disclosure-statement template (one per author, separate upload), AI-use description to
   confirm, title-page PDF, data-availability statement. Unknown facts are left as [AUTHOR TO SUPPLY].
【Overall】NO-GO today, on mechanics alone (about an hour of anonymization). After that: CONDITIONAL GO.
   The deciding substantive item is D1, which the authors can resolve with data they already hold.
【Fix order】1 anonymize + separate title-page PDF + separate anonymized appendix → aeri-submission ·
   2 D1 → aeri-identification · 3 D2 → aeri-topic-selection · 4 D3 + polish → aeri-writing-style ·
   5 secondary robustness → aeri-robustness · 6 package: remove asterisks, disclosure PDFs, AI-use field,
   data statement → aeri-submission / aeri-replication-package
【Re-run】python3 tools/preflight.py <anonymized>.pdf --venue "AER: Insights" --online
```

## What the paper does well

- **Timing:** the setting is unusually clean. Chinese arrivals fell 51.7% while other
  origins rose (Fig. 1).
- **A sharp break:** the wage break at the shock is sharp (Fig. 3a).
- **Robustness:** broad for a short paper. Appendix C covers year-over-year comparisons,
  130 regions, establishment fixed effects, dropping the top-three prefectures, binned
  doses, a mixed placebo, and an IV based on realized losses.
- **Calibration:** the abstract's claim about quantities ("no robust change") is
  carefully worded.

## Preflight feedback from this run, and what changed

The reviewer audited every preflight finding against the source. Each problem it found
was fixed in the same release, except two that are working as intended.

| # | Finding (as run) | Type | Evidence | Status in this release |
|---|---|---|---|---|
| 1 | `NUM-MISMATCH` "51.7 percent" (PDF) | False positive | The value is printed in Fig. 1's raster legend, and the note says so | **Fixed:** downgraded to INFO when the same or previous sentence cites a figure and no table |
| 2 | `REF-UNRESOLVED` on a merged reference | Parser bug | The PDF splitter merged the end of Michaels & Zhi (2010) into Sekiya et al. (2026) | **Fixed:** a new entry needs `Surname, Initial`/`Surname, Given`, so "Economics, 2 (3)" no longer starts one |
| 3 | `REF-UNRESOLVED` on a RIETI discussion paper and an arXiv preprint | Expected non-match | These are not Crossref-indexed | **Fixed:** grey literature (working/discussion papers, arXiv, SSRN, NBER, theses) is reported as INFO |
| 4 | `STMT-MISSING` disclosure statement (FAIL) | Misframed | AER: Insights requires a *separate* disclosure PDF per author; putting it in an anonymized manuscript would break anonymity | **Fixed:** new rules key `separate_upload_statements`; these become portal-checklist reminders. Also applied to AEJ: Applied, JFE, JEEA and RFS |
| 5 | `ANON-AUTHOR` quoted the title | Misleading excerpt | The author line is lower on p. 1 | **Fixed:** quotes the line with an email or institution, else a name-shaped line |
| 6 | Exhibit cap and per-exhibit deduction | **Miss with a false-green risk** | `exhibits_max` was in the rules but never read; the word check used 7,000, not 7,000 − 200 × 5; *not checked* was empty | **Fixed:** `LEN-EXHIBITS`, new `words_per_exhibit` key, and a guard that lists *any* rule preflight does not test under *not checked* |
| 7 | Word count included exhibit notes | Over-count (safe direction) | ≈540 words of notes inside floats | **Fixed:** float environments and `Notes:` lines are excluded (tex count now 5,051 against the reviewer's ≈5,050) |
| 8 | Significance asterisks | Miss | Tables use `*, **, ***`; the AEA style guide forbids them | **Fixed:** `significance_stars` rule plus an `EXH-STARS` check (also covers the PDF's `∗` glyph); set for AER: Insights and AEJ: Applied |
| 9 | Appendix bound into the manuscript | Miss | The supplementary appendix is on pp. 19–39 of the same PDF | **Fixed:** `LEN-APPENDIX` INFO when an appendix follows the references in the file |
| 10 | Commented-out declarations and the AI-use policy | Miss | tex lines 271–277 hold commented-out declarations; `llm_policy` requires an AI-use description | **Fixed:** commented-out statement sections are surfaced (INFO), and venue policies are printed as a portal checklist |
| 11 | Third-person self-citations; data-provider footnote | Correct negatives | Allowed under the AEA instructions | Unchanged |

The online run reported "17 checked, 6 not answered". The unanswered ones are unknown,
not failures, and the report treats them that way.

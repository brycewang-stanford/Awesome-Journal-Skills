# External Tools - SODA

Access date: 2026-07-08. SODA policy is reset per cycle by each edition's program
committee; open the live pages before acting. Note: `siam.org` and `hotcrp.com`
refused direct automated fetches during verification (HTTP 403) — if scripted
access fails, read the same URLs through a search engine's rendering and
cross-check two independent surfaces before trusting a date.

## Live official surfaces (2027 cycle)

- SODA 2027 conference page: https://www.siam.org/conferences-events/siam-conferences/soda27/
- SODA 2027 submissions page (deadlines, format, double-blind rules): https://www.siam.org/conferences-events/siam-conferences/soda27/submissions/
- SODA 2027 HotCRP: https://soda27.hotcrp.com/
- ALENEX 2027 (co-located, experimental algorithmics + artifact evaluation): https://www.siam.org/conferences-events/siam-conferences/alenex27/
- SOSA 2027 (co-located, simplicity in algorithms): https://www.siam.org/conferences-events/siam-conferences/sosa27/
- SIAM Publications Library (proceedings of record): https://epubs.siam.org/
- dblp SODA series (attribution and lineage checks): https://dblp.org/db/conf/soda/index.html

## Five author-side verification passes before upload

1. **Calendar pass** — re-read the submissions page the same week you plan to
   upload: deadline (July 9, 2026 AoE for 2027), rebuttal window (September 1-4,
   2026), decision month. Aggregator sites lag; SIAM's page controls.
2. **Format pass** — 11-point+, single column, 1-inch margins, letter paper,
   title page with 1-2 paragraph abstract, no page limit used honestly
   (`skills/soda-submission`). Check `pdffonts` output for embedded fonts and
   `pdfinfo` for page size.
3. **Anonymity pass** — no author block, no acknowledgements, clean PDF
   metadata; but all important references present and un-anonymized, self-cites
   in third person (lightweight double-blind is SODA-specific in this respect).
4. **Lineage pass** — every row of the prior-bound table re-checked against dblp
   and, where journal versions exist, the journal's stated bound
   (`skills/soda-related-work`); final arXiv sweep for concurrent postings.
5. **Record pass** — HotCRP entry created early; conflicts complete; form title
   and abstract byte-identical to the PDF title page; stored PDF re-downloaded
   and visually confirmed.

## Do not infer

- Do not project 2027 dates onto any later cycle; SODA deadlines drift within
  early-to-mid July and every other date follows the PC's calendar.
- Do not assume camera-ready page allowances, SIAM macro names, registration
  duties, or proceedings access terms — these arrive with the acceptance email
  and are marked 待核实 in this pack until then.
- Do not treat co-location as policy coupling: ALENEX and SOSA have their own
  deadlines, formats, and review models; only geography is shared.
- Where surfaces conflict, precedence is: live SIAM cycle page > HotCRP site
  text > aggregators; acceptance email > website for final-version mechanics.

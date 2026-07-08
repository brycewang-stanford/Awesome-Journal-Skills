# External Tools - UAI

Access date: 2026-07-08

Open the current-cycle UAI pages before using any workflow below; every cap, date, and
form in this pack is a 2026 snapshot. If the live pages and this pack disagree, the
live pages win.

## Official workflow surfaces

- AUAI (organizing association): https://www.auai.org/
- UAI 2026 conference site: https://www.auai.org/uai2026/
- UAI 2026 Call for Papers: https://www.auai.org/uai2026/call_for_papers
- UAI 2026 submission instructions: https://www.auai.org/uai2026/submission_instructions
- UAI 2026 important dates: https://www.auai.org/uai2026/important_dates
- UAI 2026 reviewer/AC instructions: https://www.auai.org/uai2026/instructions_for_reviewers_and_area_chairs
- UAI 2026 code of conduct: https://www.auai.org/uai2026/code_of_conduct
- UAI 2026 OpenReview group: https://openreview.net/group?id=auai.org/UAI/2026/Conference
- PMLR proceedings index: https://proceedings.mlr.press/
- UAI mailing list (official announcements): https://groups.google.com/g/uai-list

## Author-side verification passes

Run these against the live pages, in this order, before upload:

1. **Calendar pass** — submission window, response window, notification, camera-ready,
   conference dates; all AoE unless stated otherwise.
2. **Format pass** — current template version, main-part page cap, appendix placement
   (in-PDF for 2026), PDF size cap, supplement ZIP cap.
3. **Anonymity pass** — third-person self-reference, acknowledgement/grant removal,
   link policy, plus metadata scrubbing of PDF and ZIP.
4. **Policy pass** — dual submission, reviewer-volunteer agreement, any checklist or
   AI-use disclosure added since 2026 (none existed then).
5. **Post-acceptance pass** — camera-ready instructions, PMLR forms, registration and
   presentation requirements, poster specs.

## Useful non-official tooling

- `pdfinfo` / `pdftotext` (poppler) for metadata and leak scans of the single PDF.
- `git archive` for building clean, history-free supplement ZIPs.
- OpenReview profile pages for conflict hygiene across the author list.
- The shared ML-conference reproducibility kit in this repository (see
  `code/README.md`) for artifact smoke checks.

## Do not infer

- Do not project the 2026 dates, the 8-page/15 MB/50 MB caps, or the in-PDF-appendix
  rule onto any other year.
- Do not assume UAI keeps AISTATS-style rules or vice versa merely because both publish
  in PMLR; their supplement handling and calendars already differed in 2026.
- Do not assume the absence of an abstract deadline, checklist, or LLM policy persists;
  each was simply unposted in 2026 (待核实 each new cycle).
- When official pages conflict, prefer the newest dated announcement, then the
  OpenReview group's own instructions, then direct chair communication — and record the
  conflict in your notes.

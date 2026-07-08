# External Tools - CHI

Access date: 2026-07-08

Everything in this pack is a snapshot of the CHI 2027 cycle (with CHI 2026 outcome
data as the historical anchor). Open the live pages below before acting on any date,
threshold, or form; where the live pages disagree with this pack, the live pages win.

## Official workflow surfaces

- CHI 2027 conference site: https://chi2027.acm.org/
- CHI 2027 Papers call: https://chi2027.acm.org/authors/papers/
- CHI 2027 Papers review process: https://chi2027.acm.org/papers-review-process/
- Previous cycle (anchor data, guides): https://chi2026.acm.org/ — notably the
  Guide to a Successful Submission, Selecting a Subcommittee, Contributions to CHI,
  and the publication-ready author instructions
- CHI Steering Committee (standing policies, incl. the ADR rubric):
  https://chi.acm.org/
- SIGCHI author guides (accessibility, videos):
  https://sigchi.org/resources/guides-for-authors/
- PCS — Precision Conference Solutions (submission system):
  https://new.precisionconference.com/
- ACM TAPS workflow and `acmart` documentation: https://www.acm.org/publications/taps/
- ACM open-access policy: https://www.acm.org/publications/openaccess
- ACM Digital Library (proceedings, exemplar verification): https://dl.acm.org/

## Author-side verification passes

Run in this order against the live pages before each milestone:

1. **Calendar pass** — submission-site opening, the September deadline, resubmission
   and notification dates, TAPS / publication-ready / registration deadlines; note
   each date's timezone wording on the live page.
2. **Length-and-format pass** — current word-count wording (encouraged range,
   short-paper line, desk-reject threshold), the single-column template version, and
   any new required sections or statements in the template.
3. **Subcommittee pass** — the current cycle's subcommittee list and scope
   descriptions; re-run the fit test in `chi-topic-selection` if the list changed.
4. **Anonymity-and-policy pass** — anonymization wording (including supplemental
   materials and external links), dual-submission rules, and any AI-use disclosure
   fields added to PCS since this snapshot.
5. **Media pass** — video figure and caption requirements, PCS upload caps and
   formats, video-preview specs for the publication-ready package.
6. **Post-acceptance pass** — TAPS instructions, accessibility requirements
   (alt text fields in PCS), e-rights and open-access arrangements, registration
   and presentation rules.

## Useful non-official tooling

- `texcount` for word counts against the length norms; `latexdiff` for the
  tracked-changes resubmission.
- `pdfinfo` / `pdftotext` (poppler) for metadata and identity-leak sweeps.
- `ffmpeg` / `ffprobe` for video-figure encoding, caption muxing, and QA.
- OSF's anonymized-view links (and equivalent anonymous-repository services) for
  double-blind material sharing.
- The shared ML-conference reproducibility kit in this repository (see
  `code/README.md`) for smoke-checking anonymous artifact packages.

## Do not infer

- Do not project the 2027 dates or the 2026 word-count wording onto later cycles;
  CHI has changed review structure, desk-reject criteria, and length policy
  repeatedly in recent years.
- Do not assume ML-conference conventions apply: CHI has no OpenReview, no separate
  supplement deadline, no short rebuttal text box, and no posted artifact badges.
- Do not assume the previous cycle's subcommittee list survives into the current one.
- If official surfaces disagree (conference site vs SIGCHI guide vs PCS form), treat
  the newest statement from that cycle's chairs as controlling, and record the
  conflict in your submission notes.

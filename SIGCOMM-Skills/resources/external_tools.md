# External Tools - ACM SIGCOMM

Access date: 2026-07-09; links moved to SIGCOMM 2027 and re-checked 2026-11-24.

Use these surfaces after reopening the current SIGCOMM cycle pages. SIGCOMM restates its rules
every edition, and the single annual deadline means one stale date can cost a whole year.

## Official workflow

- SIGCOMM 2027 home: https://conferences.sigcomm.org/sigcomm/2027/
- SIGCOMM 2027 Call for Papers: https://conferences.sigcomm.org/sigcomm/2027/cfp/
- SIGCOMM 2027 submission instructions: https://conferences.sigcomm.org/sigcomm/2027/submission/
- SIGCOMM 2027 organizing committee: https://conferences.sigcomm.org/sigcomm/2027/organization/
- SIGCOMM 2027 HotCRP site (named in the CFP; not yet open on 2026-11-24): https://sigcomm27.hotcrp.com
- Camera-ready instructions (the 2027 page still shows the 2026 text): https://conferences.sigcomm.org/sigcomm/2027/cameraready/
- SIGCOMM Call for Artifacts (latest published: 2025): https://conferences.sigcomm.org/sigcomm/2025/cf-artifacts/
- SIGCOMM 2026 pages (history): https://conferences.sigcomm.org/sigcomm/2026/ and https://sigcomm26.hotcrp.com/deadlines
- ACM SIGCOMM award pages: https://www.sigcomm.org/awards/acm-sigcomm-test-of-time-paper-award and https://www.sigcomm.org/awards/best-paper-award

## Author-side verification passes

Run these against the live pages before every SIGCOMM upload; each is a discrete check the generic
tooling cannot make for you.

- **Clock pass.** Confirm the paper cutoff (SIGCOMM 2027: February 2, 2027, hard) and its exact
  time-zone rendering on the HotCRP `/deadlines` page, plus any registration step HotCRP adds.
  SIGCOMM 2026 wrote deadlines in AoE on the CFP and as EST cutoffs on HotCRP, and the 2027 pages
  name no time zone yet — never reuse a previous edition's conversion.
- **Format pass.** Check the 12-single-spaced-page pre-reference limit including figures and tables,
  the 200-word abstract, the "Paper #N, X pages body, Y pages total" author block, 10-point type and
  at most 55 lines per column, a PDF under 15 MB, ACM `acmart.cls` (submission and final), and that
  references plus optional appendices sit outside the cap. Over-length pre-reference content is not
  reviewed; run Banal before upload.
- **Blindness pass.** Verify the PDF, plots, dataset and repository links, acknowledgments, and
  metadata carry no author or institution identity; SIGCOMM double-blind covers self-citation phrasing
  and any linked artifact.
- **Track pass.** Decide research versus experience track honestly; an operational-deployment paper
  judged on research-novelty criteria, or the reverse, wastes a full year on the single deadline.
- **Status pass.** After decisions, classify the outcome (SIGCOMM 2027: conference accept with a
  shepherd / CCR accept, which may be declined / reject; no rebuttal or one-shot revision) and read
  the mechanism the CFP attaches to it before acting.

## Camera-ready and artifacts

- ACM TAPS workflow for the final PDF plus source; ACM template compliance; shepherd sign-off recorded
  in HotCRP, including approval that any appendix is necessary.
- Artifact-evaluation committee submission for ACM badges (the SIGCOMM 2025 call offered Artifacts
  Available and Artifacts Evaluated - Functional); public archive with a DOI for permanent retrieval.

## Do not infer

- Do not infer SIGCOMM 2027 notification or camera-ready dates from the 2026 cycle, nor SIGCOMM 2028
  anything from 2027.
- Do not assume the same page budget, track list, review model (2027 dropped the rebuttal and
  one-shot revision), artifact badges, or
  camera-ready toolchain without reopening the current official pages.
- If official pages disagree, treat the newest CFP, HotCRP deadline page, or a direct chair
  communication as controlling, and record the conflict.

# External Tools - CAV (Computer Aided Verification)

Access date: 2026-07-09

Use these surfaces after reopening the current CAV cycle pages. CAV mechanics — the four
submission categories, per-category page limits, the anonymization matrix, two-stage reviewing,
and artifact badges — are decided per edition, and the `i-cav.org` / `sigplan.org` gateway may
block direct fetches (read via search renderings and cross-check dblp and Springer LNCS). Do not
confuse CAV (Computer Aided Verification) with unrelated "CAV" acronyms, and do not attribute
TACAS, FMCAD, VMCAI, POPL, or PLDI papers to CAV.

## Official workflow

- CAV conference series hub: https://i-cav.org/
- CAV 2026 home (Lisbon, FLoC, Jul 26-29 2026): http://conferences.i-cav.org/2026/
- CAV 2026 Call for Papers: http://conferences.i-cav.org/2026/cfp/
- CAV 2026 Artifact Evaluation: http://conferences.i-cav.org/2026/artifacts/
- CAV 2026 Organization (Program Chairs): https://conferences.i-cav.org/2026/organization/
- CAV 2026 Program: https://conferences.i-cav.org/2026/program/
- SIGPLAN announcement (38th CAV): https://www.sigplan.org/announce/2025-11-21-cav-2026/
- FLoC 2026 (host federation): https://www.floc26.org/
- CAV Award: https://conferences.i-cav.org/2025/award/
- Springer LNCS CAV proceedings: https://link.springer.com/conference/cav
- LNCS author information / `llncs` template: https://www.springer.com/gp/computer-science/lncs

## Cross-check surfaces (when the gateway blocks the primary page)

- dblp CAV stream: https://dblp.org/db/conf/cav/index.html (edition numbering, per-year TOCs,
  exemplar verification, and sibling-venue disambiguation).
- Springer LNCS book pages: CAV 2024 = LNCS 14681-14683; CAV 2025 = LNCS 15931-15934 (open
  access; confirm accepted counts and volume numbers).
- WikiCFP CAV entry and the CAV Facebook / X (@confCAV) posts for the machine-readable deadline
  the CFP paraphrases.
- The submission portal linked from the CFP: **verify whether 2026 uses EasyChair or HotCRP** —
  CAV 2025 used `cav2025.hotcrp.com`; a 2026 rendering mentions EasyChair (**待核实**).

## Verification-community reference surfaces (cite to their real origin)

- **SV-COMP** (Competition on Software Verification), run at TACAS/ETAPS:
  https://sv-comp.sosy-lab.org/ — benchmark set and witness format for software-verifier papers.
- **SMT-COMP** (Satisfiability Modulo Theories Competition):
  https://smt-comp.github.io/ — began as a CAV 2005 satellite; benchmark division for SMT solvers.
- **SMT-LIB** standard: https://smt-lib.org/ — the input format and logics SMT tool papers target.
- **HWMCC** (Hardware Model Checking Competition) and **VNN-COMP** (Verification of Neural
  Networks Competition) — benchmark ecosystems for hardware and neural-network verification.
- Use these for benchmark provenance and baselines; cite each competition/benchmark to its own
  paper and year, and pin the exact benchmark-set revision you ran.

## Author-side checks

- Submission portal profile, co-authors, and the correct **category** (Regular / Short Tool /
  Short Application / Industrial Experience & Case Studies) — the category sets the page limit and
  the anonymization rule.
- LNCS `llncs` class compliance, the current per-category page limit (Regular 18 / short 10,
  excluding references and appendices), and a clearly-marked (optional-to-read) appendix.
- Anonymization where required: Regular and Application papers are double-blind; Tool and
  Industrial papers are not — verify the matrix on the current CFP.
- **Artifact-intent declaration** at submission time (shared with reviewers), and the plan for the
  post-notification AEC submission (Available / Functional / Reusable).
- Benchmark provenance: SV-COMP/SMT-COMP set revision, solver versions, seeds, resource limits
  (time/memory), and proof witnesses / certificates where the claim is soundness.

## Do not infer

- Do not assume a separate abstract deadline precedes the paper deadline — only the paper deadline
  was confirmed for 2026; check the Important Dates.
- Do not assume the anonymization matrix, page limits, or badge set carry over between editions.
- Do not assume artifact evaluation is mandatory or acceptance-conditional — at CAV it is invited
  and non-conditional; confirm on the current Artifact Evaluation page.
- If pages disagree, treat the newest CFP, the portal's deadline page, or a direct chair
  announcement as controlling, and record the conflict.

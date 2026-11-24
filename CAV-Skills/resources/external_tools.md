# External Tools - CAV (Computer Aided Verification)

Access date: 2026-07-09; official links re-verified 2026-11-24 (CAV 2027 pages loaded directly).

Use these surfaces after reopening the current CAV cycle pages. CAV mechanics — the submission
categories (three in CAV 2027, four in 2026), per-category page limits, the anonymization matrix,
two-stage reviewing, and artifact rules — are decided per edition. The `i-cav.org` pages loaded
directly on 2026-11-24; if a gateway blocks them, read via search renderings and cross-check dblp
and Springer LNCS. Do not
confuse CAV (Computer Aided Verification) with unrelated "CAV" acronyms, and do not attribute
TACAS, FMCAD, VMCAI, POPL, or PLDI papers to CAV.

## Official workflow

- CAV conference series hub: https://i-cav.org/
- CAV 2027 home (39th, Amsterdam, KIT, Jul 19-23 2027): https://conferences.i-cav.org/2027/
- CAV 2027 Call for Papers: https://conferences.i-cav.org/2027/cfp/
- CAV 2027 Artifact Evaluation: https://conferences.i-cav.org/2027/artifacts/
- CAV 2027 Organizing Committee (chairs): https://conferences.i-cav.org/2027/organizing-committee/
- CAV 2027 Registration / Proceedings (not yet populated on 2026-11-24):
  https://conferences.i-cav.org/2027/registration/ and https://conferences.i-cav.org/2027/proceedings/
- History — CAV 2026 (38th, Lisbon, FLoC 2026): http://conferences.i-cav.org/2026/ (CFP at
  http://conferences.i-cav.org/2026/cfp/); SIGPLAN announcement:
  https://www.sigplan.org/announce/2025-11-21-cav-2026/; FLoC 2026: https://www.floc26.org/
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
- The submission portal linked from the CFP: CAV 2027 uses **HotCRP**, but the link had not yet
  been posted on 2026-11-24 (**待核实**). CAV 2025 used `cav2025.hotcrp.com`.

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

- Submission portal profile, co-authors, and the correct **category** (CAV 2027: Regular / Tool /
  Application-Industrial-Case Study) — the category sets the page limit, the anonymization rule,
  and whether an artifact is mandatory. At most 5 submissions per author.
- LNCS `llncs` class compliance, the current per-category page limit (CAV 2027: Regular and Tool
  18 / Application 10, excluding references and appendices), and a clearly-marked
  (optional-to-read) appendix.
- Anonymization where required: in CAV 2027 only Regular Papers are double-blind; Tool and
  Application/Industrial/Case Study papers are single-blind — verify the matrix on the current CFP.
- **Artifact-intent declaration** at submission time (shared with reviewers); for Tool Papers the
  mandatory March artifact round (or an exemption request filed at submission); for other papers
  the plan for the post-notification AEC submission (Available / Functional / Reusable).
- Benchmark provenance: SV-COMP/SMT-COMP set revision, solver versions, seeds, resource limits
  (time/memory), and proof witnesses / certificates where the claim is soundness.

## Do not infer

- Do not assume a separate abstract deadline precedes the paper deadline — the CAV 2027 CFP lists
  only "Full papers due" (20 January 2027); check the Important Dates.
- Do not assume the anonymization matrix, page limits, or badge set carry over between editions.
- Do not assume the artifact rule is the same for every category — in CAV 2027 it is mandatory and
  acceptance-conditional for Tool Papers, invited and non-conditional for everything else; confirm
  on the current Artifact Evaluation page.
- If pages disagree, treat the newest CFP, the portal's deadline page, or a direct chair
  announcement as controlling, and record the conflict.

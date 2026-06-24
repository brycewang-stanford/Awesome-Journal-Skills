# Execution-Bridge Rollout — guidance → fitted, audited result (2026-06)

**Goal.** Close the last mile in every empirical depth pack: today the method skills
*advise* a Callaway–Sant'Anna estimate / weak-IV-robust CI / multiple-testing haircut;
after wiring they *run* it through the connected **StatsPAI / Stata MCP** tools and
report the number. This is the single highest-leverage change for "publish faster"
(fewer rejection cycles), because the rigor a top journal demands becomes executable
rather than aspirational.

Origin: the strategic review of 2026-06-23 found **0 / 2895 SKILL.md referenced any
execution MCP**, while the environment exposes ~600 StatsPAI causal-inference tools +
Stata MCP. This campaign fixes that.

## Architecture (why it scales without clone drift)

- **One canonical, venue-neutral playbook:**
  [`shared-resources/empirical-methods/execution-with-mcp.md`](../shared-resources/empirical-methods/execution-with-mcp.md)
  — the orchestration spine, design-family → tool-chain map, objection → tool map,
  reporting → tool map, and the credibility hard-rules. All real content lives here once.
- **Thin per-pack wiring:** each empirical depth pack gets a short, *venue-tailored*
  "Execution bridge" section in its 2–3 execution-heavy skills + one row/bullet in its
  `resources/README`. The section is mostly a pointer + which estimators matter for that
  venue, so it stays well under the clone-audit similarity threshold.
- **Validated, not asserted:** the loop was run end-to-end on synthetic data —
  [`Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md`](../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)
  — every number there is a real tool return (CS −0.0272 vs biased TWFE −0.0227,
  pre-trends p=0.155, honest-DiD breakdown point).

## Per-pack procedure (repeat for each pack)

1. `ls <Pack>-Skills/skills/` — identify the **execution-heavy** skills. Naming varies:
   - econ/finance lane: `*-identification`, `*-robustness`, `*-tables-figures`
   - management/accounting lane: `*-methods`, `*-data-analysis`, `*-tables-figures`
   - (psych/socio/political packs: the `*-methods` / `*-analysis` / `*-results` skills)
2. Add a venue-tailored **## Execution bridge (StatsPAI / Stata MCP)** section to each,
   inserted before `## Checklist` / `## Anti-patterns`. Keep it ~12–20 lines, pointer +
   the design families and estimators that pack's reviewers actually expect. Relative
   link depth from `<Pack>-Skills/skills/<skill>/SKILL.md` is always
   `../../../shared-resources/empirical-methods/execution-with-mcp.md`.
3. Add the `execution-with-mcp` row/bullet to `<Pack>-Skills/resources/README.md`
   (table or list — match the file's existing format). Depth `../../shared-resources/...`.
4. Tailor honestly: theory/structural/optimization/analytical venues note what is
   **outside** the causal-inference toolchain; lab-experiment venues emphasize
   randomization inference + `romano_wolf`; asset-pricing emphasizes the factor-zoo
   haircut + Stata Fama–MacBeth.

## Verification gate (run after each batch — must stay green)

```
python3 tools/run_checks.py            # hard checks incl. clone_audit (0 warnings)
python3 tools/quality_scorecard.py | grep "Execution bridge"   # rollout tracker
```

The scorecard now reports `Execution bridge (StatsPAI/Stata MCP) wired: N/134
empirical depth packs` and an `exb` column. It is **report-only** — the `exec_bridge`
field does not change the composite score (so unwired packs are not penalized; this is
a coverage metric, not a quality deduction).

## Do NOT wire

Breadth bundles (routing-only), and theory-only / humanities packs that the shared
empirical kit explicitly excludes (AMR, Econometric Theory, AHR, PMLA, Mind, …). The
scorecard denominator (`depth` + `code present`) already filters to the 134 candidates.

## Progress — COMPLETE (131 / 134, 98%)

All four tiers wired and committed. Final state verified: `run_checks` all hard checks
pass, `clone_audit` 0 warnings (2895 skills / 345 groups), scorecard mean 93.6.

- **Tier 0 (proof + foundation):** Journal-of-Finance (4 skills), Quarterly-Journal-of-
  Economics (3), Management-Science (3). Loop validated end-to-end with real StatsPAI
  runs → JF worked-example 02.
- **Tier 1 (12):** AEJ Applied/Policy/Macro/Micro, AER:Insights, IER, JDE, JFQA, JFI,
  JFM, JBES, JAE(applied econometrics).
- **Tier 2 (33):** AMJ, ASQ, SMJ, Org Science, Org Studies, J. of Management, JMS,
  Human Relations, HRM, ETP, JBV, JIBS; TAR, JAR, JAE, CAR, RAST, 会计研究; JM, JMR,
  JCR, Marketing Science, JAMS, JCP; Operations Research, M&SOM, JOM, POM, INFORMS JoC;
  MISQ, ISR, JMIS, JAIS.
- **Tier 3 (27):** APSR, AJPS, JOP, BJPS, IO, World Politics, CPS, Governance; ASR, AJS,
  Social Forces, SPQ, ESR, JMF, Criminology, Demography, PDR; JPSP, Psych Science,
  Cognitive Psych, J. Edu. Psych, JAP, Psychological Bulletin(meta template); AERJ;
  J. of Communication, Communication Research, POQ.
- **Tier 4 (~56):** JPE, Econometrica, REStud, JFE, RFS, REStat, JEEA, The Economic
  Journal, EER, RAND, J. Public/Labor/Health/Urban/Intl/Monetary Econ, JMCB, JLEO, JLE,
  JEEM, JEBO, J. Econ Geography/Growth, Quantitative Econ, RED, The Econometrics Journal,
  J. of Econometrics, Experimental Econ, JRU, IMFER, WBER, World Development, Research
  Policy, JPAM, JPART, PAR, Financial Management, JBF, JCF, JIMF, Review of Finance;
  经济研究, 管理世界, 中国工业经济, 经济学季刊, 金融研究, 世界经济, 财经研究,
  中国农村经济, 中国行政管理, 数量经济技术经济研究, 管理科学学报(behavioral-om),
  南开管理评论, 社会学研究.

### Intentionally NOT wired (3 — honest scoping)

- **Annual Review of Economics**, **Academy of Management Annals** — review venues
  (only a tables-figures skill; no primary-empirical methods).
- **Social Sciences in China (中国社会科学)** — generalist theory/argumentation venue;
  no empirical-methods skill to host the bridge.

### Notes for maintainers

- The **scorecard `exb` column / counter is the source of truth** (reads the SKILL
  bodies). A handful of `resources/README` pointers may be absent where the concurrent
  live-check process regenerated the file or where the README has no
  `reporting-standards` / `报告规范` anchor (e.g. 经济研究) — the SKILL-level bridge is
  present regardless.
- Re-verify / regenerate the (now empty) remaining queue any time with:

  ```bash
  python3 tools/quality_scorecard.py --json | python3 -c "import sys,json; d=json.load(sys.stdin); print('\n'.join(r['pack'] for r in sorted([x for x in d if x['pack_type']=='depth' and x['code_status']=='present' and not x['exec_bridge']], key=lambda r:-r['score'])))"
  ```

- Rollout scripts (bilingual, idempotent) live in the session scratchpad; re-run safe.

## Follow-ups — DONE (the strategic-review P0/P1 loop is complete)

The three cross-journal capabilities now form a closed loop — **pick → execute → pass the
bar before submitting**:

- **Execute (P0).** Execution bridge wired to 131/134 empirical depth packs, validated
  with real StatsPAI runs across all three core design families:
  `Journal-of-Finance-Skills/.../02-execution-walkthrough.md` (DiD),
  `shared-resources/empirical-methods/worked-examples/iv-walkthrough.md` (IV),
  `…/rdd-walkthrough.md` (RDD) — every number a real tool return.
- **Pick (P1).** `shared-resources/journal-selection/` — `journal-match.md` methodology +
  `venue-index.tsv` (185-pack stable index) + `tools/gen_venue_index.py`. Validated
  end-to-end on a finance example (index → candidates → live source-map facts).
- **Pass the bar (P1).** `shared-resources/submission-readiness/` — `readiness-checklist.md`
  go/no-go + `simulated-referee.md` multi-agent protocol +
  `worked-example-referee-report.md` (a real AE + 2-referee run on the fictional JF
  cov-lite paper).

### Still open (future, optional)

- Promote the three shared capabilities to formally installable skills once the
  skill/pack-count tripwires (`audit_repo.py`) and the root-README badges can be bumped
  without colliding with the live-check campaign.
- More real-run worked-examples (synthetic control, DML) alongside DiD/IV/RDD.

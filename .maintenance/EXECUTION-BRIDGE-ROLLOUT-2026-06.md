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

## Progress

- **Wired (15 / 134):** Journal-of-Finance (4 skills), Quarterly-Journal-of-Economics
  (3), Management-Science (3), AEJ: Applied / Economic Policy / Macroeconomics /
  Microeconomics plus AER:Insights (3 each), IER / JDE / JAE / JBES / JFI / JFQA
  (3 each), and Journal of Financial Markets (4). Lanes proven: finance/asset-pricing,
  econ/applied-micro, applied econometrics, and management/OR — across both
  skill-naming conventions. clone-audit clean.
- **Remaining (119):** regenerate the flagship-first queue any time with:
  ```
  python3 tools/quality_scorecard.py --json | python3 -c "import sys,json; d=json.load(sys.stdin); print('\n'.join(r['pack'] for r in sorted([x for x in d if x['pack_type']=='depth' and x['code_status']=='present' and not x['exec_bridge']], key=lambda r:-r['score'])))"
  ```

## Suggested cadence (month-long campaign)

Tier 1 remaining (econ/finance flagships): continue with any present but unwired AER /
JPE / Econometrica / REStud / JFE / RFS / public-economics / labor / international /
monetary / RAND packs, then rerun the queue command above before the next batch.
Tier 2 (management/accounting/marketing/IS): AMJ/ASQ/SMJ/Org Sci, TAR/JAR/JAE/CAR/RAST,
JM/JMR/JCR/Marketing Science, MISQ/ISR/JMIS/JAIS, OR/M&SOM/JOM/POM.
Tier 3 (political science / sociology / psych / demography / education / criminology):
APSR/AJPS/JOP/BJPS/IO, ASR/AJS/Social Forces/SPQ/ESR, JAP/JPSP/Psych Science, Demography,
AERJ, Criminology.
Tier 4 (Chinese empirical flagships): 经济研究 / 管理世界 / 中国工业经济 / 金融研究 /
数量经济技术经济研究 / 管理科学学报 etc.

Wire ~6–10 packs per batch, run the verification gate, then continue. Commit per tier.

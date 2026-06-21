# Flagship Depth-Pack Uplift — 2026-06-20

User brief (2026-06-20): "把某些旗舰刊升级成 12-skill 深度包 …… 一个星期 …… 请你全部都做了，中间不要和我讨论。"
Interpretation: take flagship journals that currently exist only as **breadth-bundle profiles**
(root card → one-skill profile, no `[A-depth]` in `JOURNAL-MASTER-LIST.md`) and build each a full
**12-skill depth pack** following `assets/depth-pack-spec.md` to the letter, then reconcile counts +
registry and run all hard gates green. Autonomous; no mid-course check-ins.

## Standard (single source of truth)
- `assets/depth-pack-spec.md` — exact file list, skill-sets, JSON skeletons, README skeleton.
- Reference packs to imitate: `Quantitative-Economics-Skills/` and `Economic-Research-Journal-Skills/`.
- Resource layer (flagship treatment): vendored `resources/code/` (cp from
  `shared-resources/empirical-methods/code`, verbatim, provenance comment prepended),
  `resources/README.md`, `resources/worked-examples/01-introduction.md` (fictional, venue house style),
  `resources/exemplars/library.md` (REAL web-verified papers + sibling-journal guard),
  `resources/official-source-map.md`, `resources/external_tools.md`.
- Honesty norms (repo-wide): no fabricated facts/citations; volatile specifics (current editor, exact
  fee, exact word/length limits) marked `(检索于 2026-06；以官网为准 / 待核实)`; exemplars must be
  genuinely published in THAT venue; document omissions; no silent truncation.

## Audit invariants the build MUST satisfy (`tools/audit_repo.py`)
- Each new pack = +12 SKILL.md and +1 pack root. After each batch, bump in ONE commit:
  `EXPECTED_SKILL_COUNT`, `EXPECTED_PACK_COUNT` in `tools/audit_repo.py`, and the count strings in
  BOTH `README.md` and `README.en.md`. Root journal entries stay 200 (do not add the
  `AJS-ROOT-JOURNAL-ENTRY` marker to pack READMEs).
- Skill folder names are GLOBALLY UNIQUE; frontmatter has ONLY `name`+`description`; `name`==folder.
- marketplace.json `skills[]` == actual `skills/*/SKILL.md` dirs exactly, in workflow order;
  plugin/marketplace name+version+license consistent; exactly one plugin entry.
- Every pack has README.md, README.zh-CN.md, LICENSE. No broken local markdown links
  (shared-hub depth: `../../shared-resources/` from `resources/README.md`;
  `../../../shared-resources/` from `resources/worked-examples/` and `resources/exemplars/`).
- Gates: `python3 tools/run_checks.py --skip-reports` green; `tools/clone_audit.py` new pack < 0.90
  (target < 0.75); `tools/quality_scorecard.py` to confirm the lift.

## Target list — flagship gap (prefix verified collision-free 2026-06-20)
Family `econ` skill-set unless noted. `mgmt` = management skill-set.

### Wave 1 — AEA family + JEEA (econ)
| DIR | PREFIX | PLUGIN | TITLE |
|---|---|---|---|
| AEJ-Applied-Economics | aeja | aej-applied-economics-skills | American Economic Journal: Applied Economics |
| AEJ-Macroeconomics | aejmac | aej-macroeconomics-skills | American Economic Journal: Macroeconomics |
| AEJ-Microeconomics | aejmic | aej-microeconomics-skills | American Economic Journal: Microeconomics |
| AEJ-Economic-Policy | aejpol | aej-economic-policy-skills | American Economic Journal: Economic Policy |
| AER-Insights | aeri | aer-insights-skills | American Economic Review: Insights |
| Journal-of-the-European-Economic-Association | jeea | jeea-skills | Journal of the European Economic Association |

### Wave 2 — general-interest econ
| DIR | PREFIX | PLUGIN | TITLE |
|---|---|---|---|
| The-Economic-Journal | ecj | economic-journal-skills | The Economic Journal |
| International-Economic-Review | ier | ier-skills | International Economic Review |
| Review-of-Economics-and-Statistics | restat | restat-skills | Review of Economics and Statistics |
| European-Economic-Review | eer | eer-skills | European Economic Review |
| Journal-of-Economic-Literature | jel | jel-skills | Journal of Economic Literature (review/survey variant) |
| Journal-of-Economic-Perspectives | jep | jep-skills | Journal of Economic Perspectives (non-technical variant) |

### Wave 3 — finance + applied
| DIR | PREFIX | PLUGIN | TITLE |
|---|---|---|---|
| Journal-of-Money-Credit-and-Banking | jmcb | jmcb-skills | Journal of Money, Credit and Banking |
| Journal-of-Financial-Markets | jfm | jfm-skills | Journal of Financial Markets |
| Journal-of-International-Money-and-Finance | jimf | jimf-skills | Journal of International Money and Finance |
| Financial-Management | finman | financial-management-skills | Financial Management |
| Journal-of-Health-Economics | jhe | jhe-skills | Journal of Health Economics |
| Journal-of-Urban-Economics | jue | jue-skills | Journal of Urban Economics |

### Wave 4 — field econ
| DIR | PREFIX | PLUGIN | TITLE |
|---|---|---|---|
| Journal-of-Environmental-Economics-and-Management | jeem | jeem-skills | Journal of Environmental Economics and Management |
| Journal-of-Economic-Behavior-and-Organization | jebo | jebo-skills | Journal of Economic Behavior and Organization |
| Journal-of-Law-and-Economics | jle | jle-skills | The Journal of Law and Economics |
| World-Development | worlddev | world-development-skills | World Development |
| World-Bank-Economic-Review | wber | wber-skills | The World Bank Economic Review |
| Journal-of-Economic-Geography | jegeo | journal-of-economic-geography-skills | Journal of Economic Geography |

### Wave 5 — applied tail + management
| DIR | PREFIX | PLUGIN | TITLE | FAMILY |
|---|---|---|---|---|
| Journal-of-Risk-and-Uncertainty | jru | jru-skills | Journal of Risk and Uncertainty | econ |
| Experimental-Economics | expecon | experimental-economics-skills | Experimental Economics | econ |
| Journal-of-Management | jmgmt | journal-of-management-skills | Journal of Management | mgmt |
| Journal-of-Management-Studies | jms | jms-skills | Journal of Management Studies | mgmt |
| Research-Policy | respol | research-policy-skills | Research Policy | mgmt |
| Organization-Studies | orgstud | organization-studies-skills | Organization Studies | mgmt |

### Wave 6+ backlog (queued, same pipeline — finish if budget allows)
Academy-of-Management-Annals (amann, mgmt review), Review-of-Accounting-Studies (revacc),
Journal-of-the-Academy-of-Marketing-Science (jams, mgmt), Journal-of-Consumer-Psychology (jcp, mgmt),
Human-Resource-Management (hrm, mgmt), Human-Relations (humrel, mgmt),
Entrepreneurship-Theory-and-Practice (etp, mgmt), Journal-of-Management-Information-Systems (jmis, mgmt),
Journal-of-the-Association-for-Information-Systems (jais, mgmt), INFORMS-Journal-on-Computing (ijoc),
IMF-Economic-Review (imfer, econ), Economic-Policy (ecopol, econ),
Journal-of-Law-Economics-and-Organization (jleo, econ), Annual-Review-of-Economics (arecon, review).

## Progress log
- 2026-06-20: program defined; recon complete; prefixes verified collision-free; build brief locked.
- 2026-06-20: Wave 1 and most of Wave 2 were published as 13 commits, bringing the repo to
  2269 skills / 138 packs.
- 2026-06-20: stuck remainder resumed by Codex; generated the remaining Wave 2 IER pack, all
  Wave 3 finance/applied packs, all Wave 4 field-economics packs, all Wave 5 applied-tail and
  management packs, and the full Wave 6+ backlog. New live inventory: 2665 skills / 171 packs /
  200 root journal entries. Shared README/audit count registration updated in the same worktree.
- 2026-06-20: independent verification + finish (this session). Confirmed on disk: all 44 target
  packs present, each exactly 12 SKILL.md (528 new skills); `python3 tools/run_checks.py
  --skip-reports` green (audit 2665/171/200, clone audit max 0.788 = pre-existing CS-conference
  breadth pairs only, `git diff --check` clean); the 44 new packs show no clone pair >= 0.82
  with anything. `tools/quality_scorecard.py`: the 44 new packs score 90.2-94.0 (mean 92.0),
  at repo parity (mean 92.8); JEL/JEP correctly carry no econometric code kit (survey /
  non-technical). Closed a registration gap the count-only commits left: added all 44 packs to
  the root README depth-pack discovery tables in BOTH README.md and README.en.md (commit
  "Register 44 flagship depth packs ..."). Honest quality note: the 6 hand-built Wave-1 packs +
  JEL are the richest prose (94.0); the bulk built by the parallel lane are complete and
  venue-specific but more templated (90-91) — all above the repo's 85 "excellent" bar.
- 2026-06-20: DEEPENING PASS complete (user: "把剩下的工作全部做扎实"). The 33 packs that were
  still on the templated decision-map skeleton were rewritten skill-by-skill to genuine
  venue-specific flagship prose via 6 QC'd parallel subagent batches (A IER/JMCB/JFM/JIMF/FM/JHE;
  B JUE/JEEM/JLE/WorldDev/WBER; C JEBO/JEG/JRU/ExpEcon/IMFER/EconPolicy/JLEO; D AnnualRevEcon/
  INFORMS-JoC/RAST/JOM/JMS/ResearchPolicy; E+F OrgStudies/AoM-Annals/JAMS/JCP/HRM/HumanRelations/
  ETP/JMIS/JAIS). Brief: `.maintenance/SUBAGENT-DEEPEN-BRIEF.md`. Each rewrite removed every
  template tell, kept frontmatter (name+description, name==folder) and the resource layer untouched,
  and web-verified venue facts (review model, portal, fee, length, data policy, sibling guards) with
  volatile items marked 待核实. Subagents fixed many latent self-loop rebuttal handoffs and surfaced
  real corrections (JLEO portal = Editorial Express not ScholarOne; JCP now Wiley not Elsevier; JMIS
  intake = email to the EIC, not a portal; Economic Policy relaunched 2025 commissioned-only; AEJ:Macro/Micro
  single-blind; ExpEcon now Cambridge UP/OA). RESULT: template-tell sweep across all 44 packs = 0
  remaining; `tools/quality_scorecard.py` for the 44 rose 92.0 → **94.0** (median 94.0, min 93.3),
  repo mean 92.8 → 93.3; `tools/clone_audit.py` no pair ≥ 0.85 repo-wide; `tools/run_checks.py
  --skip-reports` all green (2665/171/200). Committed across batch commits (668cb1b, ccfdcc7,
  b9ee9a4, b06741b) plus auto-commit-hook commits for batch E+F.
- Known follow-ups (logged, honest): (a) a repo auto-commit hook produced very granular commits for
  batch E+F (one per file) — cosmetic git-history noise, not a correctness issue; (b) a few
  `resources/official-source-map.md` files now slightly lag their deepened skills (JCP Elsevier→Wiley,
  Economic Policy 2025 relaunch, JMIS email intake) — the skills carry the corrected facts with 待核实
  markers; refresh the source maps in a later pass; (c) re-confirm all 待核实 volatile facts (current
  editors, fees, exact limits) against official sites before relying on them.

## Phase 2 — Category-2 social-science flagship depth packs (2026-06-20)
User: "把剩下的工作全部做扎实，一个星期，好好利用." Next remaining body = flagship social-science
journals still served only as breadth profiles. Computed the gap: 29 Category-2 flagships absent as
depth packs; all prefixes verified collision-free. Built at FLAGSHIP quality from the start (brief
`.maintenance/SUBAGENT-SS-DEPTH-BRIEF.md`, skill-set variants empirical/psychology/theory/methods/
review/law; code kit only for observational-causal-inference disciplines).
- SS batch 1 (committed): Comparative Political Studies, British Journal of Political Science,
  European Sociological Review, Public Administration Review, JPART, JPAM (EMPIRICAL + code kit).
- SS batch 2 (committed): Governance, Population and Development Review, Communication Research
  (+code kit); New Media & Society, Annals of the AAG, American Anthropologist (no code kit).
- 12/12 done packs: structural QC clean (12 skills, frontmatter, JSON, no template tells), clone
  audit no pair ≥0.82, scorecard 91.2–94.0 (mean 93.6). Counts reconciled to 2809 skills / 183 packs
  (audit green); all 12 registered in README depth tables (en+zh). Many portal corrections vs the
  seed (BJPS/PAR/JPART → Editorial Manager/Editorial Express; etc.).
- REMAINING (17, queued — blocked on subagent quota, resets 3:50pm PT 2026-06-20): SS-3 J.Applied
  Psychology, Developmental Psychology, Cognitive Psychology, J.Educational Psychology, Current
  Anthropology, Sociological Methods & Research; SS-4 Sociological Theory, Psychological Review,
  Annual Review of Sociology, Annual Review of Psychology, Review of Educational Research,
  Perspectives on Psychological Science; SS-5 Progress in Human Geography + 4 law reviews
  (Harvard/Yale/Stanford/Columbia). Run via the same SS brief; register + reconcile counts after.

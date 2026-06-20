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
</content>
</invoke>

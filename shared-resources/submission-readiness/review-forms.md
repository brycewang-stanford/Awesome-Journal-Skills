# Review Forms — what each venue family's referees actually fill in

The simulated referee panel ([`simulated-referee.md`](simulated-referee.md)) is only as
realistic as the form it writes on. A NeurIPS reviewer scores soundness, presentation,
contribution and an overall 1–6; an ARR reviewer scores soundness, excitement and an
overall 1–5 with half-points and a Findings band; an economics referee writes prose plus a
confidential letter to the editor; a JAMA statistical reviewer checks the trial against
CONSORT. Writing the same generic report for all of them is the "venue-blind review"
anti-pattern. This file gives the panel the right form per family.

**Precedence.** The target pack's own review-process / referee-strategy skill and its
`resources/official-source-map.md` override this file — forms change by cycle. The fields
below were read from the official pages on **2026-11-23**; re-read the live page before
quoting a scale to an author.

## How to pick the form

| Venue family | Packs (examples) | Form below |
|---|---|---|
| ML / AI conferences on OpenReview (NeurIPS-style) | NeurIPS, ICML, ICLR, AISTATS, UAI, COLT, KDD, IJCAI, AAAI | A |
| *ACL venues via ACL Rolling Review | ACL, EMNLP, NAACL, EACL, COLING (ARR-routed), COLM (own form — read pack) | B |
| Economics & finance journals | AER-family, QJE, JPE, Econometrica, REStud, JF, JFE, RFS, REStat, EJ, JEEA | C |
| Management, marketing, accounting, IS | AMJ, AMR, ASQ, SMJ, MS, JM, JMR, Marketing Science, TAR, MISQ | D |
| Clinical medicine | NEJM, JAMA, The Lancet, BMJ | E |
| Natural-science flagships | Science, Nature, Cell, PNAS, PNAS Nexus | F |
| Chinese social-science journals | 经济研究, 管理世界, 中国社会科学, 中国工业经济, 世界经济 | G |
| Anything else | — | C's structure, with the pack's own criteria |

## A — ML / AI conferences (NeurIPS-style OpenReview form)

Source: NeurIPS 2025 Reviewer Guidelines, https://neurips.cc/Conferences/2025/ReviewerGuidelines
(read 2026-11-23). ICML, ICLR and others use close variants; ICML changed its form in 2025 —
take field names from the ICML pack when the target is ICML.

| Field | Content / scale |
|---|---|
| Summary | What the paper claims and does, in the reviewer's words |
| Strengths and Weaknesses | Organised along Quality, Clarity, Significance, Originality |
| Quality / Clarity / Significance / Originality | each 4 excellent · 3 good · 2 fair · 1 poor |
| Questions | 3–5 actionable questions whose answers could change the score |
| Limitations | Are limitations and negative societal impact addressed? "yes" or suggestions |
| Overall | 6 Strong Accept · 5 Accept · 4 Borderline accept · 3 Borderline reject · 2 Reject · 1 Strong Reject |
| Confidence | 5 absolutely certain … 1 educated guess |
| Ethical concerns | Flag for ethics review if warranted |

Lenses for this family: **soundness/evaluation** (baselines, seeds/variance, tuning on
test, leakage/contamination, ablations, statistical significance of small gains),
**novelty/positioning** (closest prior work, is the delta real), **clarity/
reproducibility** (enough detail to reimplement; code; checklist answers consistent with
the paper).

## B — ACL Rolling Review form (*ACL venues)

Source: https://aclrollingreview.org/reviewform (read 2026-11-23).

| Field | Content / scale |
|---|---|
| Paper Summary | Claims and contributions |
| Summary of Strengths / Summary of Weaknesses | Weaknesses that would change the decision first |
| Comments/Suggestions/Typos | Everything else |
| Reviewer Confidence | 5 positive … 1 not my area |
| Soundness | 5 Excellent · 4 Strong · 3 Acceptable · 2 Poor · 1 Major Issues (half-points allowed) |
| Excitement | 5 Highly Exciting … 1 Not Exciting (half-points allowed) |
| Overall Assessment | 5 Consider for Award · 4 Conference · 3 Findings · 2 Resubmit next cycle · 1.5 Resubmit after next cycle · 1 Do not resubmit (half-points between) |
| Best paper justification, Limitations and Societal Impact, Ethical Concerns, Reproducibility, Datasets, Software | Additional fields |

Calibration note from the form itself: Findings is judged mainly on **soundness and
reproducibility**; Conference additionally on novelty and impact. A paper can be sound
and still land in Findings — say which band and why. The mandatory Limitations section
is checked by preflight (`STMT-MISSING`), not by the panel.

## C — Economics and finance journals

No numeric form. Each referee writes (i) a **report to the authors** and (ii) a short
**confidential letter to the editor** with a recommendation; the editor (or co-editor)
decides, often after a desk screen. Recommendation vocabulary: *reject* · *reject and
resubmit* (some journals) · *major revision / revise and resubmit* · *minor revision* ·
*accept*. The decisive question at top-5/top-3 journals is general interest plus
credibility; at field journals, correctness and contribution to the field.

Report to authors — structure the panel must follow:
1. One-paragraph summary of question, design, headline estimate.
2. Assessment of contribution relative to the closest 3–5 papers.
3. **Main concerns**, numbered, most decision-relevant first — each naming the section/
   table, why it threatens the conclusion, and the analysis that would resolve it.
4. Minor concerns.

Confidential letter (3–6 sentences): recommendation, the one issue that drives it, and
whether a revision could plausibly clear it.

Lenses: **identification** (variation, assumptions, modern estimators for the design —
see [`reviewer-objection-checklist`](../empirical-methods/reviewer-objection-checklist.md)),
**contribution/general interest**, **inference/robustness** (clustering level, weak-IV-
robust inference, multiple testing, specification search disclosure).

## D — Management, marketing, accounting, IS

Prose reports, developmental in tone, with recommendations *reject · major revision ·
minor revision · accept*. Theory contribution carries more weight than in economics: the
reviewer asks what the paper changes in how we *think* about the phenomenon, and whether
constructs, mechanisms and boundary conditions are specified. Theory-only outlets (AMR)
have no empirical lens; replace it with **logical coherence of propositions**.

Lenses: **theory/contribution** (construct clarity, mechanism, boundary conditions,
dialogue with the conversation the journal hosts), **method/design** (endogeneity,
measurement validity, common-method variance, sample), **implications & writing**.

## E — Clinical medicine (NEJM / JAMA / Lancet family)

Manuscripts are triaged by editors, then reviewed by clinical referees and, for most
original research, a **statistical reviewer**. Adherence to the design's reporting
guideline is part of the review:

| Design | Guideline (current version, read 2026-11-23) | Source |
|---|---|---|
| Randomised trial | CONSORT 2025 | https://www.consort-spirit.org/ |
| Trial protocol | SPIRIT 2025 (34-item checklist) | https://www.consort-spirit.org/ |
| Observational study | STROBE | https://www.equator-network.org/reporting-guidelines/strobe/ |
| Systematic review / meta-analysis | PRISMA 2020 | https://www.prisma-statement.org/ |

Report structure: summary; **major issues** (validity of the primary analysis — ITT,
pre-specified primary outcome matching the registry, handling of missing data, multiplicity,
effect size with CI rather than P values alone, generalisability); minor issues; a
statistical section; recommendation *reject · major revision · minor revision · accept*.

Lenses: **clinical relevance & design**, **statistics** (primary-outcome integrity,
analysis population, missing data, multiplicity, absolute vs relative effects),
**reporting & ethics** (guideline adherence, registration, consent/IRB, data sharing).

## F — Natural-science flagships (Science / Nature / Cell / PNAS)

Editors screen hard for broad significance before review. Referees then address: the main
claims and whether they are novel and of broad interest; whether the evidence supports
them (controls, replication, statistics, alternative explanations); what additional
experiments are essential versus nice-to-have; whether methods and data are sufficient for
reproduction; clarity for non-specialists. Recommendation: *reject · reject with
resubmission encouraged · major revision · minor revision · accept*.

Lenses: **significance & claims**, **experimental/analytical validity**, **data,
methods & reproducibility**.

## G — 中文社科期刊（经济研究 / 管理世界 / 中国社会科学 / 中国工业经济 / 世界经济）

These journals use editorial screening plus anonymous external review, with a final
decision by the editors (three-stage review: initial screen, external review, final
decision). The panel must check the specific journal's process in its pack. The external
review comments usually cover:

1. **选题价值与问题意识** — is it an important question for China's economy and society, and does it engage the literature?
2. **创新性与理论贡献** — the marginal contribution relative to the closest work.
3. **研究设计与识别** — 内生性处理, 识别策略, 稳健性检验, 机制检验 (Baron–Kenny 三步法 alone is no longer convincing).
4. **数据与变量** — data sources, how indicators are constructed, sample selection.
5. **规范与写作** — 学术规范, the literature review, standardised tables and figures, length.

Decision vocabulary: 退稿 · 修改后再审（大修）· 修改后录用（小修）· 录用.
Lenses: **识别与方法**, **贡献与选题**, **规范与稳健性**.

## Output rule for every family

Each simulated referee fills **its family's form** (A–G), then adds two fields the
pipeline needs: `owner_skill` for each major concern (the pack skill that fixes it), and
`evidence` (the §/table/line it rests on). A concern with no evidence location does not
survive verification.

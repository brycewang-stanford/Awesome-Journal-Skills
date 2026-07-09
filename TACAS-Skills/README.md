# TACAS Skills

Twelve agent skills for papers targeting **TACAS — the International Conference on Tools and
Algorithms for the Construction and Analysis of Systems**, a main conference of **ETAPS** (the
European Joint Conferences on Theory and Practice of Software) and the tools-and-algorithms venue of
formal-methods verification. The pack covers the full arc of a TACAS campaign: choosing among its
**four paper categories** (research, case-study, regular tool, tool-demonstration); building sound
algorithms and honest benchmark evidence; packaging the EasyChair submission under the correct
**per-category blind model**; meeting the **mandatory artifact evaluation** that gates tool-paper
acceptance; and delivering the **Springer LNCS gold-open-access** camera-ready with earned ETAPS
Artifact Badges.

Official basis checked on **2026-07-09**: the TACAS 2026 / ETAPS 2026 (Turin) and TACAS 2027 /
ETAPS 2027 (Copenhagen) calls, the ETAPS joint CfP and proceedings policy, the Springer LNCS volume
pages, the `tacas.info` artifact-evaluation pages, and the SV-COMP site. Direct fetches of
`etaps.org`, `link.springer.com`, and `tacas.info` returned 403 in the verification environment, so
official pages were read via search-engine renderings of the exact URLs and cross-checked against
Springer LNCS, dblp, and the SV-COMP site; the full trail, including everything still marked 待核实,
is in [`resources/official-source-map.md`](resources/official-source-map.md).

> Sibling-venue warning: TACAS is **not** CAV, VMCAI, FMCAD, or SPIN. Several canonical verification
> tools (NuSMV, CPAchecker, Storm) debuted at CAV, not TACAS. No exemplar in this pack is attributed
> to TACAS without a dblp/LNCS check.

## What makes TACAS different from its siblings

These venue mechanics, verified for the 2026/2027 cycles, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from CAV, from a journal, or from a pure-theory
verification venue:

- **Four paper categories, each with its own rules.** **Regular research** (≤16 pp), **case-study**
  (≤16 pp), **regular tool** (≤16 pp), and **tool-demonstration** (≤6 pp) papers differ in page
  limit, anonymity, and artifact obligation. Choosing the category is a substantive decision, not a
  label.
- **A per-category blind model.** **Regular research papers are double-blind**; **case-study, tool,
  and tool-demonstration papers are single-blind** and name their authors and tools. Anonymizing the
  wrong category is a real error.
- **Artifact evaluation is a first-class citizen and, for tools, mandatory.** Regular tool and
  tool-demonstration papers **must** submit an artifact shortly after the paper; it is evaluated **in
  parallel with the PC** and its outcome **feeds acceptance**. Research and case-study artifacts are
  **voluntary and post-acceptance**. Badges (**Available / Functional / Reusable**) are awarded by
  the ETAPS Artifact Evaluation Committee and printed on the title page.
- **The LNCS path, gold open access.** TACAS uses Springer **`llncs.cls`** (not ACM `acmart` or IEEE
  `IEEEtran`), and the proceedings are **gold open access under CC-BY since 2018**, with copyright
  retained by the authors — no author-facing APC.
- **The ETAPS umbrella and a single annual round.** TACAS is co-located with **ESOP, FASE, and
  FoSSaCS** on a shared schedule, submitted via **EasyChair**, reviewed in a **single annual round**
  with a rebuttal (unlike ESOP's two rounds).
- **It hosts SV-COMP.** TACAS is home to the **International Competition on Software Verification
  (SV-COMP)** and co-locates VerifyThis — a verifier to be ranked on the common task set is a
  competition contribution, not a stand-alone tool paper.

## Skills

| Skill | What it does |
| --- | --- |
| [`tacas-topic-selection`](skills/tacas-topic-selection/SKILL.md) | Route between TACAS and its siblings (CAV, VMCAI, FMCAD, SPIN, journals) and — distinctively — pick the right one of the four categories, and separate a tool paper from a SV-COMP entry. |
| [`tacas-workflow`](skills/tacas-workflow/SKILL.md) | Run the single-round year backward from the EasyChair deadline through the mandatory tool-paper artifact deadline, rebuttal, notification, voluntary artifact, LNCS camera-ready, and presentation. |
| [`tacas-writing-style`](skills/tacas-writing-style/SKILL.md) | Lead with the construction/analysis contribution and an explicit soundness claim; match structure to category; keep to the 16/6-page LNCS budget. |
| [`tacas-related-work`](skills/tacas-related-work/SKILL.md) | Cover the verification lanes, write delta-first positioning, credit solvers/benchmarks, and keep research-paper self-citations anonymous. |
| [`tacas-experiments`](skills/tacas-experiments/SKILL.md) | Shared benchmarks, fairly configured baselines, honest wall-clock reporting, soundness validation, reproducibility on the clean VM, and SV-COMP vs tool-paper evaluation. |
| [`tacas-reproducibility`](skills/tacas-reproducibility/SKILL.md) | Package for the clean ETAPS evaluation VM: pinned deps, offline runs, claim-to-script mapping, honest reproducibility levels. |
| [`tacas-supplementary`](skills/tacas-supplementary/SKILL.md) | Split content between the reviewed pages, the appendix/website, and the artifact by decision-criticality — nothing that decides acceptance lives outside the body. |
| [`tacas-submission`](skills/tacas-submission/SKILL.md) | Final EasyChair audit: pick the category, meet the LNCS page limit, apply the right blind mode, stage the mandatory tool-paper artifact, desk-risk triage. |
| [`tacas-review-process`](skills/tacas-review-process/SKILL.md) | Model the pipeline — per-category blind review, the single annual PC round with rebuttal, the parallel mandatory artifact evaluation — and where author leverage exists. |
| [`tacas-author-response`](skills/tacas-author-response/SKILL.md) | Write the short single-round rebuttal answering soundness, benchmark-fairness, and artifact objections with checkable evidence, anonymous where the category requires. |
| [`tacas-artifact-evaluation`](skills/tacas-artifact-evaluation/SKILL.md) | Convert the package into ETAPS badges (Available / Functional / Reusable) through the two-round model — mandatory-with-the-PC for tools, voluntary post-acceptance for research. |
| [`tacas-camera-ready`](skills/tacas-camera-ready/SKILL.md) | De-anonymize (research), complete LNCS metadata and the Springer CC-BY rights form, permanentize artifact links, and add earned badges to the title page. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026/2027 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official ETAPS/TACAS/EasyChair/LNCS/SV-COMP surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | dblp/LNCS-verified TACAS papers across categories (BMC, CBMC, Z3, LTSmin), with sibling-venue guardrails and self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional bounded-refinement-checker tool paper's introduction rebuilt to the TACAS arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the TACAS-specific checks (clean-VM run, badge readiness) the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./TACAS-Skills
claude plugin install tacas-skills
```

Or use the files directly: each `skills/tacas-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a TACAS research paper, a tool paper, or a SV-COMP entry?" → `tacas-topic-selection`
- "Audit my draft against the TACAS category rules before EasyChair" → `tacas-submission`
- "Get this tool's artifact ready for the mandatory evaluation and the badges" → `tacas-artifact-evaluation`
- "Reviewers doubt our soundness and baseline fairness — draft the rebuttal" → `tacas-author-response`

## Pack structure

```text
TACAS-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover
├── skills/
│   └── tacas-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md              # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md         # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `tacas-topic-selection`; TACAS overlaps CAV, and the **category** you
   pick fixes your page limit, blind mode, and artifact obligation. Skim the exemplars to see what
   foundational and tool contributions look like at TACAS.
2. **While building the tool/evidence** — keep `tacas-experiments` and `tacas-reproducibility` beside
   the work; shared benchmarks, fair baselines, and a clean-VM artifact cannot be retrofitted at the
   deadline.
3. **While writing** — `tacas-writing-style` for the body against the worked example,
   `tacas-supplementary` for the body/appendix/artifact split, `tacas-related-work` for delta-first
   positioning.
4. **Deadline weeks** — `tacas-submission` end to end on the final LNCS PDF, then (for a tool paper)
   the **mandatory artifact** on its firm post-paper deadline.
5. **After submission** — `tacas-review-process` to calibrate, `tacas-author-response` for the
   rebuttal, then `tacas-artifact-evaluation` and `tacas-camera-ready` — or the routing table in
   `tacas-topic-selection` if the decision goes the other way.

## 2026/2027-cycle anchor facts (historical snapshot, not permanent rules)

- TACAS 2026 is the **32nd** edition, held at **ETAPS 2026 (29th)** in **Turin, Italy** (University
  of Turin), **11-16 April 2026** (main conferences 13-16 April). Reported cycle: paper 16 Oct 2025,
  mandatory tool artifact 30 Oct 2025, rebuttal 8-10 Dec 2025, notification 22 Dec 2025, voluntary
  artifact 8 Jan 2026. As of 2026-07-09 this edition has passed; the live next target is TACAS 2027.
- TACAS 2027 is the **33rd** edition, at **ETAPS 2027 (30th)** in **Copenhagen, Denmark**, **10-15
  April 2027**; ETAPS 2027 voluntary artifact deadline 11 Jan 2027.
- Categories: **research / case-study / regular tool / tool-demonstration**. Format: Springer
  **`llncs.cls`** via **EasyChair**. Review: **double-blind research, single-blind tool/case-study**,
  single annual round with rebuttal. Artifact: **mandatory** for tool/tool-demo, **voluntary** for
  research/case-study; badges **Available / Functional / Reusable**. Proceedings: **LNCS, gold open
  access (CC-BY)**. TACAS hosts **SV-COMP** (15th edition at TACAS 2026).

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026/2027 facts** — carry dates/limits and trace to a numbered source in the source
   map (e.g., the four categories, the per-category blind model, the mandatory tool-paper artifact,
   LNCS gold open access).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the exact
   TACAS 2026 submission counts and the PC-chair roster).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the full PC-chair/AEC
   rosters, the ETAPS awards slate, exact per-category date variations).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and limit above is a **cycle snapshot**. TACAS/ETAPS re-decide structure per edition —
  page limits, badge sets, and the schedule — so verify on the current ETAPS joint CfP and TACAS
  page each year.
- TACAS has no standing editor-in-chief and no author-facing APC; PC chairs rotate per edition and
  ETAPS funds the gold open access centrally.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar tool name is not
  proof of a TACAS placement (CAV is the easiest confusion).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

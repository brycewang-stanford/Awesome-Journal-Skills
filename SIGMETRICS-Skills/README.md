# ACM SIGMETRICS Skills

Twelve agent skills for papers targeting **ACM SIGMETRICS — the ACM SIGMETRICS International
Conference on Measurement and Modeling of Computer Systems**, the flagship for computer-systems
**performance measurement, modeling, and evaluation**. The pack covers the full arc of a SIGMETRICS
campaign: deciding whether a project is SIGMETRICS-shaped or belongs at IMC, SIGCOMM/NSDI/OSDI, a
learning venue, or a performance journal; building evidence that pairs a **proven bound** with
**validation and measurement**; packaging the double-anonymous `acmsmall` submission across the
**three rolling deadlines**; navigating the **hybrid conference-journal review** with its
**one-shot revision** and mandatory shepherding in **POMACS**; and delivering the POMACS
camera-ready plus an ACM-badged artifact.

Official basis checked on **2026-07-09**: the SIGMETRICS 2026 and 2027 calls and Important Dates,
the POMACS journal pages, the per-deadline SIGMETRICS HotCRP sites, the ACM Artifact Review and
Badging policy, and the SIGMETRICS awards pages. Direct fetches of `sigmetrics.org`, `dl.acm.org`,
and the `*.hotcrp.com` sites returned 403 in the verification environment (a WebFetch of the 2027
summer HotCRP returned 403 Forbidden), so official pages were read via search-engine renderings of
the exact URLs and cross-checked against the ACM Digital Library (POMACS), dblp, the SIGARCH
call-for-contributions posts, and the OpenAccept statistics tracker; the full trail, including
everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Acronym-collision warning: SIGMETRICS is **not** IMC (ACM Internet Measurement Conference, pure
> network measurement), **not** SIGCOMM/NSDI (networking systems), and **not** SIGMOD (databases).
> No fact in this pack derives from those.

## What makes SIGMETRICS different from its siblings

These venue mechanics, verified for the 2026/2027 cycles, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from IMC, from a systems venue, or from a pure
learning venue:

- **Papers are journal articles on a rolling schedule.** SIGMETRICS research papers publish in
  **POMACS (Proceedings of the ACM on Measurement and Analysis of Computing Systems)**, an
  open-access ACM journal, submitted through **three deadlines a year — summer, fall, winter**. There
  is no single annual deadline; you choose the cycle whose POMACS timing fits.
- **A hybrid conference-journal review with a one-shot revision.** First decisions are **Accept**
  (every accepted paper is **shepherded**), **One-Shot Revision** (a major-revision decision:
  resubmit a revised paper to one of the next two deadlines, re-reviewed once against an explicit
  list of required changes), or **Reject** (no SIGMETRICS resubmission for 12 months). The revision
  is genuinely **single-shot** — not an open-ended journal R&R.
- **A rigor culture: proofs of performance bounds.** SIGMETRICS papers carry **theorems** — a
  tail-latency bound, a stability condition, a regret rate — validated numerically or empirically.
  Reviewers check proofs and assumptions, not just plots. This is unlike the pure-measurement IMC or
  the systems-building SIGCOMM/NSDI.
- **A theory + measurement + learning blend.** The tracks — **Theory**, **Measurement & Applied
  Modeling**, **Learning**, and the new **Operational Systems Track** — reflect a community that
  prizes stochastic modeling *and* real measurement, often in one paper.
- **The ACM `acmsmall` journal template.** SIGMETRICS 2026 posts **up to 20 pages** of technical
  content (single-column, including tables and figures) **plus unlimited references** — not a
  two-column conference box.
- **Double-anonymous review, with one exception.** Anonymity is expected throughout, except in the
  **Operational Systems Track**, which may reveal the deploying organization or the deployed system.
- **Reproducibility by default.** A seeded simulator that regenerates the figures and matches the
  analysis, pinned measurement provenance, and ACM badges (Available / Functional / Reusable /
  Reproduced) are the community's expectations.

## Skills

| Skill | What it does |
| --- | --- |
| [`sigmetrics-topic-selection`](skills/sigmetrics-topic-selection/SKILL.md) | Route between SIGMETRICS and its neighbors (IMC, SIGCOMM/NSDI/OSDI, NeurIPS/ICML, Performance Evaluation/TON/QUESTA) using the rigor test and pick the right track. |
| [`sigmetrics-workflow`](skills/sigmetrics-workflow/SKILL.md) | Plan across the three rolling deadlines, through registration, shepherding, the one-shot revision, POMACS publication, and presentation. |
| [`sigmetrics-writing-style`](skills/sigmetrics-writing-style/SKILL.md) | Build the performance-evaluation skeleton: contribution on the first page, stated assumptions, theorems paired with validation, 20-page discipline. |
| [`sigmetrics-related-work`](skills/sigmetrics-related-work/SKILL.md) | Cover the performance-evaluation lanes, write delta-first positioning (tighter bound / weaker assumption / newer data), keep self-citations anonymous. |
| [`sigmetrics-experiments`](skills/sigmetrics-experiments/SKILL.md) | Match evidence to claim: proofs, analysis-vs-simulation agreement, real traces, fair baselines, confidence intervals, learning guarantees, measurement provenance. |
| [`sigmetrics-reproducibility`](skills/sigmetrics-reproducibility/SKILL.md) | Treat proofs and seeded simulators as artifacts: regenerate figures, match the analysis, pin trace provenance, state the reproducibility level honestly. |
| [`sigmetrics-supplementary`](skills/sigmetrics-supplementary/SKILL.md) | Split content by decision-criticality — theorem statements, assumptions, and headline validation stay in the body; full proofs to an appendix. |
| [`sigmetrics-submission`](skills/sigmetrics-submission/SKILL.md) | Final HotCRP audit: choose the deadline, register the abstract + track, acmsmall page budget, double-anonymity sweep, desk-risk triage. |
| [`sigmetrics-review-process`](skills/sigmetrics-review-process/SKILL.md) | Model the pipeline — double-anonymous, three outcomes, one-shot revision to a subsequent deadline, the 12-month bar — and where author leverage exists. |
| [`sigmetrics-author-response`](skills/sigmetrics-author-response/SKILL.md) | Write the one-shot revision response letter that closes every item on the reviewers' required-changes list in a single re-reviewed round. |
| [`sigmetrics-artifact-evaluation`](skills/sigmetrics-artifact-evaluation/SKILL.md) | Convert the package into ACM badges (Available / Functional / Reusable / Reproduced) — where a figure must regenerate and match the analysis. |
| [`sigmetrics-camera-ready`](skills/sigmetrics-camera-ready/SKILL.md) | De-anonymize, incorporate the shepherd's required changes, complete POMACS metadata, permanentize artifacts, pass ACM production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eleven sources with URLs and access dates; verified 2026/2027 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces (per-deadline HotCRP, POMACS, ACM badging) plus cross-check sources for when the gateway blocks a direct fetch. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Four archival-verified SIGMETRICS papers across the venue's three cultures — queueing theory, measurement, learning-with-guarantees — with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional scheduling study's abstract and introduction rebuilt to the SIGMETRICS arc (theorem + validation), before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the SIGMETRICS-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./SIGMETRICS-Skills
claude plugin install sigmetrics-skills
```

Or use the files directly: each `skills/sigmetrics-*/SKILL.md` is a standalone instruction file
whose frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a SIGMETRICS paper or should it go to IMC/NSDI?" → `sigmetrics-topic-selection`
- "Which rolling deadline should we target, and audit my draft" → `sigmetrics-submission`
- "We got a One-Shot Revision — plan the response letter" → `sigmetrics-author-response`
- "Get this simulator/artifact ready for the ACM badges" → `sigmetrics-artifact-evaluation`

## Pack structure

```text
SIGMETRICS-Skills/
├── .claude-plugin/                  # plugin.json + marketplace.json (12 skills declared)
├── README.md                        # this file
├── README.zh-CN.md                  # 中文说明
├── LICENSE                          # MIT
├── assets/cover.svg                 # pack cover
├── skills/
│   └── sigmetrics-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md                    # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md               # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `sigmetrics-topic-selection`; the rigor gate (is there a theorem, a
   validated model, or a principled measurement?) and the track choice decide the reviewer pool.
   Skim the exemplars to see what durable SIGMETRICS contributions look like.
2. **While building evidence** — keep `sigmetrics-experiments` and `sigmetrics-reproducibility`
   beside the study; assumptions stated at design time and seeds logged at run time cannot be
   retrofitted.
3. **While writing** — `sigmetrics-writing-style` for the body against the worked example,
   `sigmetrics-supplementary` for the body/appendix/artifact split, `sigmetrics-related-work` for
   delta-first positioning.
4. **Deadline weeks** — register the abstract and track before the earlier cutoff, then
   `sigmetrics-submission` end to end on the final PDF and artifact.
5. **After submission** — `sigmetrics-review-process` to calibrate, `sigmetrics-author-response` for
   the one-shot revision, then `sigmetrics-artifact-evaluation` and `sigmetrics-camera-ready` — or
   the routing table in `sigmetrics-topic-selection` if the decision goes the other way.

## 2026/2027-cycle anchor facts (historical snapshot, not permanent rules)

- SIGMETRICS 2026 is the **52nd** edition: University of Michigan, Ann Arbor, USA (Michigan Union),
  **June 8-12, 2026**. Three deadlines: Summer (paper Jul 29, 2025), Fall (paper Oct 14, 2025),
  Winter (paper Jan 13, 2026), all 23:59 AoE.
- SIGMETRICS 2027 is in **Atlanta, Georgia, USA, June 7-11, 2027**; the summer-round abstract
  registration was **July 3, 2026** — the live next target as of 2026-07-09 (summer paper deadline
  待核实; winter reported as paper Jan 11 / notification Mar 10, 2027).
- Publication: **POMACS**, open access, no APC. Review: **double-anonymous**, hybrid
  conference-journal. Decisions: Accept (shepherded) / **One-Shot Revision** / Reject. Template: ACM
  **acmsmall**, ≤20 pages technical content + unlimited references.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026/2027 facts** — carry dates/budgets and trace to a numbered source in the source
   map (e.g., the three rolling deadlines, the 20-page acmsmall budget, the one-shot-revision rule).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the reported
   2027 winter dates; historical acceptance-rate figures).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the exact 2027 summer
   *paper* deadline, the full track count, whether an artifact track runs this cycle, exact award
   names).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. SIGMETRICS re-decides its three deadline
  dates, page budget, track list, and any artifact track per edition — verify them before anything
  else each cycle.
- SIGMETRICS has **rotating per-edition General and Program Chairs** and **no APC**; POMACS is open
  access. Treat continuity assumptions about people as errors even though the *publication* is a
  journal.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar
  performance-evaluation tool name is not proof of a SIGMETRICS placement (it may be IMC, SIGCOMM,
  NSDI, or NeurIPS).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

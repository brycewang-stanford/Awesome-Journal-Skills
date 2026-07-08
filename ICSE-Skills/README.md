# ICSE Skills

Twelve agent skills for papers targeting **ICSE — the IEEE/ACM International
Conference on Software Engineering**, the flagship conference of the software
engineering research community. The pack covers the full arc of an ICSE
campaign: deciding whether a project is research-track material or belongs at
a co-located track or sibling venue, building empirical evidence that survives
an SE reviewer's audit, packaging the double-anonymous HotCRP submission with
its open-science obligations, navigating the Accept / Major Revision / Reject
decision model, and delivering the camera-ready plus ACM-badged artifact.

Official basis checked on **2026-07-08**: the ICSE 2027 Research Track call,
important-dates page, NIER and Journal-first calls, the ICSE 2026 artifact-
evaluation track, the ICSE 2026 conference records, and the SIGSOFT/ICSE award
pages. Direct fetches of `conf.researchr.org` returned 403 in the verification
environment, so official pages were read via search-engine renderings of the
exact URLs and cross-checked against the ICSE HotCRP sites, the ACM Digital
Library, IEEE Xplore, and dblp; the full trail, including everything still
marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes ICSE different from its siblings

These venue mechanics, verified for the 2027 cycle, drive most of the advice
in the skills — and most of the mistakes made by authors arriving from ML
conferences or from SE journals:

- **One cycle, one chance.** ICSE 2027 runs a single submission cycle
  (mandatory abstract June 23, paper June 30, 2026, AoE) — a change from the
  two-cycle 2025/2026 model. Missing June costs a year.
- **Major Revision is a real decision.** First decisions (October 20, 2026)
  are Accept, Major Revision, or Reject; MR papers revise in four weeks
  (due November 17) for a terminal December 18 decision. In ICSE 2026, most
  accepted papers — 189 of 321 — arrived through Major Revision.
- **Four posted criteria, verifiability among them.** Novelty, Rigor,
  Relevance, and Verifiability & Transparency are scored explicitly; the
  replication package is review material, not an afterthought.
- **A hard 10-page box.** Main text ≤ 10 pages *including appendices*, plus 2
  reference-only pages, in the unmodified IEEE conference template — with
  desk rejection named as the penalty for format tampering. No unlimited
  appendix exists.
- **Open science by default.** Sharing is the expected default; non-sharing
  requires a justification in a Data Availability section after the
  Conclusion. Review is double-anonymous, so review-time artifacts must be
  anonymized.
- **An empirical evidence culture.** Threats-to-validity sections, research-
  question contracts, effect sizes, and real subject programs are community
  norms the reviewer pool enforces even where no rule states them.

## Skills

| Skill | What it does |
| --- | --- |
| [`icse-topic-selection`](skills/icse-topic-selection/SKILL.md) | Apply the two-question fit test and route between the research track, NIER/SEIP/SEIS/Demos, FSE/ASE/ISSTA/MSR/ICSME, and the journal-first path. |
| [`icse-workflow`](skills/icse-workflow/SKILL.md) | Run the single-cycle year backward from June 30, through September response, October decisions, the November sprint, and April in Dublin. |
| [`icse-writing-style`](skills/icse-writing-style/SKILL.md) | Build the empirical-SE paper skeleton: RQ contracts, practitioner-grounded motivation, a threats section that isn't boilerplate, ten-page compression. |
| [`icse-related-work`](skills/icse-related-work/SKILL.md) | Sweep the five literature lanes across ACM DL/IEEE Xplore/dblp, write delta-first positioning, and keep self-citations double-anonymous. |
| [`icse-experiments`](skills/icse-experiments/SKILL.md) | Match evidence to claim shape: real subjects, fair baselines, SE-standard statistics and effect sizes, qualitative rigor, contamination-aware LLM ablations. |
| [`icse-reproducibility`](skills/icse-reproducibility/SKILL.md) | Build the verifiability story: availability statements, provenance pinning for mining and LLM studies, anonymized-but-runnable packages. |
| [`icse-supplementary`](skills/icse-supplementary/SKILL.md) | Split content between the 10-page body and the replication package by review status — nothing decision-critical may live outside the pages. |
| [`icse-submission`](skills/icse-submission/SKILL.md) | Final HotCRP audit: the mandatory abstract, 10+2 format, anonymity sweep with mechanical checks, open-science items, desk-risk triage. |
| [`icse-review-process`](skills/icse-review-process/SKILL.md) | Model the pipeline — criteria, response, Major Revision, the December terminal decision — and where author leverage actually exists. |
| [`icse-author-response`](skills/icse-author-response/SKILL.md) | Write both speaking turns: the September criterion-mapped response and the November revision ledger that survives re-review. |
| [`icse-artifact-evaluation`](skills/icse-artifact-evaluation/SKILL.md) | Convert the accepted paper's package into ACM badges: Available (archival DOI), Reusable (evaluator-proof docs), by the January window. |
| [`icse-camera-ready`](skills/icse-camera-ready/SKILL.md) | Spend the extra camera-ready page well, de-anonymize systematically, permanentize availability links, and pass IEEE production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Twelve official sources with URLs and access dates; verified 2027-cycle facts; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes — the first of which is the cycle-count check. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified ICSE papers across five contribution shapes, three of them Most Influential Paper winners, with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional flaky-test paper's abstract and introduction rebuilt to the four review criteria, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the ICSE-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its
own marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ICSE-Skills
claude plugin install icse-skills
```

Or use the files directly: each `skills/icse-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to
trigger it. Typical invocations:

- "Is this an ICSE paper or should it go to ISSTA?" → `icse-topic-selection`
- "Audit my draft against the ICSE research-track rules" → `icse-submission`
- "We got a Major Revision — plan the four weeks" → `icse-author-response`
- "Get this artifact ready for the badge deadline" → `icse-artifact-evaluation`

## Pack structure

```text
ICSE-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── icse-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `icse-topic-selection`; a wrong-venue or
   one-rung-early submission wastes a single-cycle year. Skim the exemplars
   library to see what decade-certified ICSE contributions look like.
2. **While designing the study** — keep `icse-experiments` and
   `icse-reproducibility` beside the codebase; threats named at design time
   and provenance pinned at mining time cannot be retrofitted in June.
3. **While writing** — `icse-writing-style` for the body against the worked
   example, `icse-supplementary` for the body/package split,
   `icse-related-work` for positioning.
4. **Deadline weeks** — abstract registered before June 23, then
   `icse-submission` end to end on the final PDF and package.
5. **After submission** — `icse-review-process` to calibrate expectations,
   `icse-author-response` for September and any November sprint, then
   `icse-artifact-evaluation` and `icse-camera-ready` — or the rerouting
   table in `icse-topic-selection` if December goes the other way.

## 2027-cycle anchor facts (historical snapshot, not permanent rules)

- ICSE 2027 is the **49th** edition: Dublin, Ireland, **April 25 – May 1,
  2027** (core days Wednesday–Friday, April 28–30).
- Research track: single cycle; abstract (mandatory) June 23, 2026; paper
  June 30, 2026; both 23:59:59 AoE; submission at `icse2027.hotcrp.com`.
- Pipeline: author response September 2026 · notification October 20, 2026 ·
  Major Revision due November 17, 2026 · final MR decision December 18, 2026.
- Format: IEEE conference template · main text ≤ 10 pages including
  figures/tables/appendices · +2 reference-only pages · camera-ready gets one
  extra main-text page.
- Review: double-anonymous; criteria = Novelty, Rigor, Relevance,
  Verifiability & Transparency; governed by the ICSE Open Science policy.
- Context: ICSE 2026 (48th, Rio de Janeiro, April 12–18, 2026) accepted 321
  of 1,469 across two cycles (~22%), with 189 of the 321 via Major Revision.

## Fact discipline

This pack separates three classes of statement, and the skills are written to
keep them distinguishable:

1. **Verified 2027-cycle facts** — carry dates/budgets and trace to a
   numbered source in the source map (e.g., the 10+2 page model, the
   June 30 deadline, the four criteria definitions).
2. **Reported facts** — read only via secondary renderings and labeled as
   such (e.g., the ICSE 2026 acceptance statistics, pending confirmation
   against the proceedings front matter).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 and
   phrased as questions to resolve (e.g., 2027 artifact deadlines,
   response-format caps, registration rules, any AI-use policy).

If any statement in the skills presents class 2 or 3 material in class 1
voice, treat it as a bug and fix it against the live official pages.

## Maintenance notes

- Every date and budget above is a **2027-cycle snapshot**. ICSE re-decides
  its structure per edition — including the number of submission cycles,
  which changed between 2026 and 2027 — so verify the cycle count before
  anything else each year.
- Items unverifiable on 2026-07-08 are marked 待核实 in the source map —
  notably the 2027 program chairs, artifact-evaluation and camera-ready
  deadlines, author-response format, registration and presentation rules,
  and any LLM/AI-use policy. Do not state these as facts until confirmed.
- ICSE has no standing editorial board; chairs rotate per edition. Treat
  journal-style continuity assumptions as errors here.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) —
  companion-volume papers are not research-track exemplars.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

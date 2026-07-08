# ASPLOS Skills

Twelve agent skills for papers targeting **ASPLOS — the ACM International Conference
on Architectural Support for Programming Languages and Operating Systems**, the
premier forum for multidisciplinary computer-systems research spanning hardware,
software, and their interaction, sponsored by ACM SIGARCH, SIGPLAN, and SIGOPS. The
pack covers the full arc of an ASPLOS campaign: proving the work genuinely lives at
the architecture-PL-OS intersection, building hardware-grade evidence across
simulators, FPGAs, and real silicon, surviving the two-page rapid-review screen,
navigating the two-deadline cycle with its Major Revision channel, and converting
acceptance into a badged, artifact-backed ACM publication.

Official basis checked on **2026-07-08**: the ASPLOS 2027 Call for Papers, the
conference hub with the 2027 timeline, the April-cycle HotCRP deadline page, the
artifact-evaluation pages, the ACM DL proceedings for the 30th and 31st editions,
and the SIGARCH/SIGPLAN/SIGOPS Influential Paper Award pages. Direct fetches of
`asplos-conference.org`, HotCRP, and dblp were blocked in the verification
environment, so official pages were read via search-engine renderings of the exact
URLs and cross-checked against the ACM Digital Library and SIGARCH postings; the
full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes ASPLOS different from its siblings

These 2027-cycle mechanics drive most of the advice in the skills — and most of the
mistakes made by authors arriving from single-community venues:

- **The intersection is the admission ticket.** ASPLOS wants work in operating
  systems, programming languages, computer architecture, *and their intersection* —
  and its rapid-review round explicitly prioritizes intersection work. A clean
  single-community paper belongs at ISCA/MICRO, PLDI/POPL, or SOSP/OSDI instead.
- **Two deadlines per edition, not one and not three.** ASPLOS 2027 accepts papers
  on April 15, 2026 and September 9, 2026 (both AoE, no abstract deadline),
  replacing the recent three-round model. As of this pack's check date the April
  round's author-response window (July 6-9, 2026) was literally in progress.
- **A two-page rapid review.** The first screening round reads only the first two
  pages of each submission, double-blind, and a majority of submissions may not
  advance past it. Pages 1-2 are a survival organ, engineered separately.
- **Major Revision is a real outcome.** Beyond Accept and Reject, some papers get a
  revision channel: resubmit at the camera-ready deadline six weeks after
  notification, and the revision itself counts as a submission on record.
- **Rebuttals have an attention budget.** No hard word cap, but reviewers are not
  expected to read beyond 800 words, and the CFP scopes rebuttals to correcting
  factual errors and answering questions.
- **Citation rules with teeth.** References (excluded from the 11-page limit) must
  give every co-author's full first and last name — no "et al." — with hyperlinked
  citation numbers and DOIs per entry.
- **Artifact culture with ACM badges.** Post-acceptance artifact evaluation is an
  ASPLOS tradition: an Artifact Appendix (`ae.tex`), a collaborative committee, and
  Available / Functional / Reproducible badges, with the Available badge requiring
  a public archival repository.

## Skills

| Skill | What it does |
| --- | --- |
| [`asplos-topic-selection`](skills/asplos-topic-selection/SKILL.md) | Apply the cross-layer deletion test and route between ASPLOS, ISCA/MICRO/HPCA, PLDI/POPL, SOSP/OSDI/EuroSys, SC, and MLSys; pick a deadline by evidence maturity. |
| [`asplos-workflow`](skills/asplos-workflow/SKILL.md) | Run the two-gate 2027 calendar with owners per risk, a September-9 countdown, and branch plans for accept, revision, and both reject types. |
| [`asplos-writing-style`](skills/asplos-writing-style/SKILL.md) | Engineer pages 1-2 for the rapid review, distill the one-sentence cross-layer insight, structure per-layer mechanism sections, budget figures inside 11 pages. |
| [`asplos-related-work`](skills/asplos-related-work/SKILL.md) | Cover five literature lanes across three communities, differentiate on boundary placement, and handle own-work/arXiv material under the 2027 double-blind rules. |
| [`asplos-experiments`](skills/asplos-experiments/SKILL.md) | Match claims to instruments — silicon, FPGA, simulator — with cycle-accuracy caveats, strong tuned baselines, per-layer ablations, and honest adverse results. |
| [`asplos-reproducibility`](skills/asplos-reproducibility/SKILL.md) | Capture machine/simulator/firmware state per result, script the capture, and write three-tier availability statements for hardware evaluators may lack. |
| [`asplos-supplementary`](skills/asplos-supplementary/SKILL.md) | Split content between the self-contained 11 pages and appendices reviewers need not read; use anonymized supplements for unciteable own work. |
| [`asplos-artifact-evaluation`](skills/asplos-artifact-evaluation/SKILL.md) | Build the `ae.tex` Artifact Appendix, target the three badges, lay out an evaluator-navigable package, and plan mitigations for hardware-dependent claims. |
| [`asplos-submission`](skills/asplos-submission/SKILL.md) | Final pre-upload audit: 11-page geometry, mandatory template, full-name/DOI citations, anonymity sweep, GenAI disclosure, HotCRP completion before AoE. |
| [`asplos-review-process`](skills/asplos-review-process/SKILL.md) | Model the staged pipeline — rapid screen, full review, response, Accept/Major Revision/Reject — and where author leverage exists at each stage. |
| [`asplos-author-response`](skills/asplos-author-response/SKILL.md) | Triage reviews into the CFP's sanctioned buckets, budget for 800 read words, argue only from submitted evidence, and negotiate revision terms. |
| [`asplos-camera-ready`](skills/asplos-camera-ready/SKILL.md) | Convert the decision into a publishable ACM paper in six weeks: de-anonymization diff, rights forms, change notes for revisions, badge and artifact integration. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten official sources with URLs and 2026-07-08 access dates; verified 2027-cycle facts; the explicit 待核实 list; the gateway access-method note. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes (geometry, citations, anonymity, two-page, HotCRP status). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five Influential-Paper-Award-verified ASPLOS papers as contribution shapes, each with a self-check question and a venue-attribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional CXL-tiering abstract and introduction rebuilt to survive the two-page rapid review, before → after, mapped to skill rules. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared conference reproducibility kit, plus four hardware-shaped checks (simulator pinning, hardware deps, firmware state, badge mapping) it cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ASPLOS-Skills
claude plugin install asplos-skills
```

Or use the files directly: each `skills/asplos-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to trigger it.
Typical invocations:

- "Is this accelerator paper ASPLOS or ISCA?" → `asplos-topic-selection`
- "Red-team my first two pages before the September deadline" → `asplos-writing-style`
- "We got a Major Revision — plan the six weeks" → `asplos-review-process` + `asplos-camera-ready`
- "Package the gem5 experiments for artifact evaluation" → `asplos-artifact-evaluation`

## Pack structure

```text
ASPLOS-Skills/
├── .claude-plugin/             # plugin.json + marketplace.json (12 skills declared)
├── README.md                   # this file
├── README.zh-CN.md             # 中文说明
├── LICENSE                     # MIT
├── assets/cover.svg            # pack cover
├── skills/
│   └── asplos-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md               # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md          # adapter to the shared repro kit
```

## 2027 anchor facts (one cycle's snapshot, not permanent rules)

- ASPLOS 2027: **Heraklion, Crete, Greece, April 11-15, 2027**. ASPLOS 2026 was the
  31st edition (ACM DL), held March 22-26, 2026 in Pittsburgh; 2025 (30th,
  Rotterdam) ran as the first joint ASPLOS-EuroSys conference.
- Deadlines: **April 15, 2026** and **September 9, 2026**, 11:59 PM AoE, on HotCRP
  (one site per cycle), no abstract deadline.
- April cycle: response July 6-9, 2026; notification July 27, 2026. September
  cycle: response December 1-4, 2026; notification December 21, 2026.
- Format: ≤ **11 pages** single-spaced two-column including all text, figures,
  tables, and footnotes; references excluded and unlimited; mandatory LaTeX
  template; appendices allowed but reviewers neither required nor encouraged to
  read them.
- Review: double-blind; **two-page rapid review** first; rebuttal read expectation
  ~**800 words**; outcomes Accept / **Major Revision** (due 6 weeks after
  notification, counts as a submission) / Reject.
- Artifacts: post-acceptance evaluation; badges **Available / Functional /
  Reproducible**; Artifact Appendix from `ae.tex`.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified 2027-cycle facts** — carry dates/caps and trace to a numbered source
   in the source map (e.g., the 11-page rule, the September 9 deadline).
2. **Derived or secondary facts** — labeled as such (e.g., "32nd edition" is
   arithmetic from the ACM DL's 31st-edition title, not a fetched ordinal).
3. **Unverifiable-at-check-time items** — marked 待核实 and phrased as questions
   (e.g., camera-ready page allowance, 2027 chairs, attendance rules, AE dates).

If any skill states class-2 or class-3 material as class 1, treat it as a bug and
fix it against the live official pages.

## Maintenance notes

- Every date and cap above is a **2027-cycle snapshot**. The deadline structure
  itself changed between 2026 and 2027 (three rounds → two); assume nothing for
  2028 without reopening `asplos-conference.org`.
- Items not verifiable live on 2026-07-08 are listed in the source map's 待核实
  sections — notably the 2027 chairs, the September-cycle HotCRP URL, camera-ready
  page allowance, registration/attendance rules, AE calendar, and any per-author
  submission cap. Do not state these as facts until confirmed.
- Program leadership rotates per edition; there is no standing editor-in-chief and
  no policy memory to appeal to across years.
- When adding exemplars, follow the recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — award pages
  give titles, but the ACM DL entry is the bibliographic authority.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

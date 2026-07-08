# OSDI Skills

Twelve agent skills for papers targeting **OSDI — the USENIX Symposium on Operating
Systems Design and Implementation**, the USENIX flagship for operating systems, storage,
distributed systems, cloud infrastructure, and machine-learning systems. The pack covers
the whole arc of an OSDI cycle: deciding whether the contribution is a built-and-measured
system, designing the evaluation, fitting the story into the 12-page reviewed body,
surviving a double-blind review that (in 2026) had **no author-response period**, clearing
conditional-accept shepherding, and converting acceptance into an open-access USENIX paper
with a sysartifacts artifact badge.

Official basis checked on **2026-07-08**: the OSDI '26 conference page, Call for Papers
(HTML and PDF editions), Requirements for Authors, Call for Artifacts, the
`osdi26.usenix.hotcrp.com` deadlines page, the USENIX blog posts on OSDI's annual cadence
and the retirement of USENIX ATC, and the OSDI '27 conference stub. Direct fetches of
`usenix.org` returned HTTP 403 in the verification environment, so official pages were
read through search-engine renderings of the exact official URLs and cross-checked against
dblp and the HotCRP site; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes OSDI different from other venues

These mechanics, verified for the 2026 cycle, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from ACM or ML conferences:

- **It is a USENIX venue, not an ACM one.** Proceedings are **open access from the day
  the event begins** — every OSDI paper since the 1990s is a free PDF on `usenix.org`.
  There is no paywall, no ACM DL fee, and no author publication charge.
- **Submission runs on HotCRP**, not OpenReview or CMT, with USENIX's local-time
  convention: OSDI '26 deadlines were **2:59 pm PST**, not Anywhere-on-Earth midnight.
- **12 reviewed pages, references free, appendices forbidden at submission.** The '26
  CFP allowed unlimited reference pages but explicitly disallowed supplementary appendix
  material in the submission; everything reviewers weigh must fit the 12-page body.
  Accepted papers grow to 14 pages plus references *and* appendices.
- **No rebuttal in 2026.** OSDI '26 eliminated the author-response period. The levers
  moved to before submission (clarity) and after notification (**conditional acceptance
  with heavyweight shepherding** — mandated changes verified by a shepherd).
- **Two reviewing tracks**: the classic Research track and an **Operational Systems
  track** for design-implementation-and-experience papers about deployed systems.
- **Artifact evaluation via the sysartifacts community**, after conditional acceptance.
  In 2026 only the **Artifacts Available** badge was evaluated — a deliberate narrowing
  from the earlier Available / Functional / Reproduced triple.
- **Both OS flagships are now annual.** OSDI has run yearly since 2021 and SOSP yearly
  since 2024, so a December OSDI miss retargets within months, not years.
- **Best-paper lineage**: the **Jay Lepreau Best Paper Award**, inaugurated at OSDI '08.

## Skills

| Skill | What it does |
| --- | --- |
| [`osdi-topic-selection`](skills/osdi-topic-selection/SKILL.md) | Apply the built-and-measured test, choose Research vs Operational Systems track, and route between OSDI, SOSP, NSDI, FAST, EuroSys, and ATC. |
| [`osdi-workflow`](skills/osdi-workflow/SKILL.md) | Run the December-to-July year: title registration, submission, the silent review window, artifact deadline, shepherded final papers, Seattle. |
| [`osdi-writing-style`](skills/osdi-writing-style/SKILL.md) | Build the systems narrative — pain point, abstraction, mechanism, measurement — inside 12 pages that reviewers are told to down-rank for padding. |
| [`osdi-related-work`](skills/osdi-related-work/SKILL.md) | Cover the six systems literature lanes, exploit USENIX's free proceedings for verification, and keep own-prior-work anonymous under the renamed-system rule. |
| [`osdi-experiments`](skills/osdi-experiments/SKILL.md) | Design an evaluation that answers research questions: mature baselines, realistic workloads, scalability, tail behavior, and component breakdowns. |
| [`osdi-reproducibility`](skills/osdi-reproducibility/SKILL.md) | Record hardware, configuration, workload, and measurement provenance while experiments run, so the artifact and the paper cannot drift apart. |
| [`osdi-supplementary`](skills/osdi-supplementary/SKILL.md) | Live with the no-appendix submission rule: what goes in the 12 pages, what waits for the 14-page final, what becomes the artifact. |
| [`osdi-artifact-evaluation`](skills/osdi-artifact-evaluation/SKILL.md) | Package the artifact for sysartifacts evaluation — the 2026 Artifacts Available badge, Zenodo archiving, and the May deadline after conditional accept. |
| [`osdi-submission`](skills/osdi-submission/SKILL.md) | Final HotCRP audit: the two December deadlines, PST cutoffs, 12-page check, institution-level anonymization, renamed-system rule, eight-submission cap. |
| [`osdi-review-process`](skills/osdi-review-process/SKILL.md) | Model the double-blind PC pipeline with no rebuttal: what reviewers see, how conditional acceptance and shepherding work, where author leverage lives. |
| [`osdi-author-response`](skills/osdi-author-response/SKILL.md) | Operate in a no-rebuttal regime: pre-empt objections in the submission, then treat the shepherd revision letter as the real author response. |
| [`osdi-camera-ready`](skills/osdi-camera-ready/SKILL.md) | Deliver the June final paper: 14 pages plus appendices, the two-page artifact appendix, de-anonymization, USENIX open-access publication, presenter duties. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eleven official sources with URLs and access dates, verified 2026-cycle facts, the access-method note, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces (USENIX pages, HotCRP, sysartifacts) plus author-side verification passes to run before upload. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five dblp/USENIX-verified OSDI papers across two decades and five system classes, with self-check questions and a sibling-venue misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional storage-system abstract and introduction rebuilt into the OSDI design-narrative arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit, plus the OSDI-specific checks the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./OSDI-Skills
claude plugin install osdi-skills
```

Or use the files directly: each `skills/osdi-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to trigger it. Typical
invocations:

- "Is this scheduler an OSDI paper or an NSDI paper?" → `osdi-topic-selection`
- "Audit my draft against the OSDI submission rules" → `osdi-submission`
- "We got a conditional accept — what now?" → `osdi-author-response`, `osdi-camera-ready`
- "Prepare the artifact for the badge" → `osdi-artifact-evaluation`

## Pack structure

```text
OSDI-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── osdi-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared repro kit
```

## Suggested use

1. **Months before the deadline** — run `osdi-topic-selection`; if nothing is built and
   measured, the fit test just saved you a cycle. Study the exemplars library to see how
   accepted OSDI papers put a working system at the center.
2. **While building** — keep `osdi-experiments` and `osdi-reproducibility` beside the
   test cluster; workload realism and measurement provenance cannot be retrofitted in
   deadline week.
3. **While writing** — `osdi-writing-style` for the 12-page narrative,
   `osdi-supplementary` for the no-appendix triage, `osdi-related-work` for positioning
   against the freely downloadable OSDI/SOSP/NSDI record.
4. **December** — `osdi-submission` end to end: title registration a week before the
   paper, PST cutoffs, anonymization down to the institution and system name.
5. **After notification** — `osdi-review-process` to read the decision,
   `osdi-author-response` for the shepherding exchange, `osdi-artifact-evaluation` and
   `osdi-camera-ready` for the May–June deliverables.

## 2026 anchor facts (historical snapshot, not permanent rules)

- OSDI '26 is the **20th** edition: The Westin Seattle, Seattle, WA, USA,
  **July 13–15, 2026**. Program Co-Chairs: Eddie Kohler (Harvard University) and
  Amar Phanishayee (NVIDIA).
- 2026 pipeline: title/abstract registration **December 4, 2025** · full submission
  **December 11, 2025** (both 2:59 pm PST, on HotCRP) · notification **March 26, 2026** ·
  artifact submission **May 8, 2026** (8:59 pm PDT) · final papers **June 9, 2026**.
- Format: **12 pages** including figures and tables plus unlimited references at
  submission; **no appendices** in the submitted PDF; **14 pages** plus references and
  appendices for final papers; up to **two extra pages** of artifact appendix for papers
  that pass artifact evaluation.
- Policy: double-blind, institutions anonymized, arXiv posting allowed only under a
  different system name, at most **eight submissions per author**, no author-response
  period, conditional acceptance with shepherding.
- Publication: USENIX **open-access** proceedings, free to all once the event begins;
  no author fee; registration-funded conference with hardship discounts.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026-cycle facts** — carry dates/caps and trace to a numbered source in
   the source map (e.g., the 12-page body, the December 11 deadline, the single
   Artifacts Available badge).
2. **Reported facts** — found only in secondary renderings and labeled as such (e.g.,
   OSDI '27's Baltimore dates, which come from event aggregators pending the official
   page).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 and phrased as
   questions to resolve, never as facts (e.g., the OSDI '27 CFP deadlines, registration
   rates, any AI-use policy).

If any statement in the skills presents class 2 or 3 material as class 1, treat it as a
bug and fix it against the live official pages.

## Maintenance notes

- Every date and cap above is a **2026-cycle snapshot**; reopen the current
  `usenix.org/conference/osdi<yy>` pages before giving deadline-sensitive advice.
- The author-response and artifact-badge policies **changed at OSDI '26** (response
  removed; badges narrowed to Available-only). They may change again — check the
  current CFP and Call for Artifacts rather than assuming either direction.
- USENIX ATC ended after ATC '25 and its successor is run by ACM SIGOPS; do not cite
  "co-located ATC" logistics from pre-2026 OSDI pages.
- OSDI chairs rotate per edition; there is no standing editor. Re-check the current
  organizers page before naming anyone.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — famous systems
  papers scatter across OSDI, SOSP, NSDI, and ATC, and the venue must be proven, not
  remembered.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

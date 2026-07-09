# ESEC/FSE Skills

Twelve agent skills for papers targeting **ESEC/FSE — the ACM International Conference on the
Foundations of Software Engineering**, the ACM SIGSOFT flagship and, alongside ICSE, one of the
two general software-engineering flagships. The pack covers the full arc of an FSE campaign:
deciding whether a project is FSE-shaped or belongs at ICSE, ASE, ISSTA, or an SE journal;
building empirical evidence that survives an SE reviewer's audit; packaging the double-anonymous
HotCRP submission with its open-science obligations; navigating the **journal-style Major Revision**
of PACMSE; and delivering the PACMSE camera-ready plus an ACM-badged artifact.

Official basis checked on **2026-07-09**: the FSE 2026 and FSE 2027 research-track calls and
Important Dates pages, the PACMSE journal pages, the FSE HotCRP sites, the ACM Artifact Review and
Badging policy, and the SIGSOFT/ESEC-FSE award pages. Direct fetches of `conf.researchr.org` and
`dl.acm.org` returned 403 in the verification environment, so official pages were read via
search-engine renderings of the exact URLs and cross-checked against the ACM Digital Library
(PACMSE), dblp, and the FSE HotCRP sites; the full trail, including everything still marked 待核实,
is in [`resources/official-source-map.md`](resources/official-source-map.md).

> Name-collision warning: `fse.iacr.org` is *Fast Software Encryption*, a cryptography conference,
> and is **not** this FSE. No fact in this pack derives from it.

## What makes FSE different from its siblings

These venue mechanics, verified for the 2026/2027 cycles, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from ICSE, from a PL/ML venue, or from an SE
journal:

- **Papers are journal articles.** FSE research papers publish in **PACMSE (Proceedings of the ACM
  on Software Engineering)**, an open-access ACM journal (Vol 1 = FSE 2024, Vol 2 = FSE 2025,
  Vol 3 = FSE 2026). The submission is judged like a journal manuscript that also earns a
  conference slot.
- **Major Revision is a real, journal-style round.** First decisions are Accept, **Major
  Revision**, or Reject; a Major Revision is a genuine revise-and-resubmit, re-read by the original
  reviewers, with an anonymous point-by-point response letter — closer to a journal R&R than to a
  rebuttal.
- **A single annual research deadline (currently), with a caveat.** FSE 2026 closed 11 Sep 2025;
  FSE 2027 closes 2 Oct 2026. FSE 2024 experimented with a two-deadline model; whether a year runs
  one deadline or two is decided per edition — verify the cadence before anything else.
- **Heavy double-anonymity.** Anonymity is maintained through all reviewing *and* discussion, and
  even the Major Revision response letter must stay anonymous.
- **The ACM path, not IEEE.** FSE uses the **ACM Primary Article Template** with a generous
  single-column budget (FSE 2027: ≤18 pages text+figures + 4 reference pages) — not ICSE's IEEE
  10+2 box. Do not carry an IEEEtran habit across.
- **Open science and ACM badging by default.** A Data Availability statement and an
  anonymized-but-runnable artifact are expected at review time; ACM badges (Available / Functional
  / Reusable / Reproduced) are earned post-acceptance on a separate deadline.
- **An empirical-SE evidence culture.** Research-question contracts, real subject systems, fair
  baselines, effect sizes, and threats-to-validity arguments are community norms the reviewer pool
  enforces even where no rule states them.

## Skills

| Skill | What it does |
| --- | --- |
| [`fse-topic-selection`](skills/fse-topic-selection/SKILL.md) | Route between ESEC/FSE and its siblings (ICSE, ASE, ISSTA, MSR, ICSME, EMSE/TSE/TOSEM) using contribution shape, the model-swap and re-label tests, and the calendar. |
| [`fse-workflow`](skills/fse-workflow/SKILL.md) | Run the single-cycle year backward from the deadline, through registration, the Major Revision round, artifact evaluation, PACMSE camera-ready, and presentation. |
| [`fse-writing-style`](skills/fse-writing-style/SKILL.md) | Build the empirical-SE skeleton: SE contribution on the first page, RQ contracts, threats that argue rather than recite, page-budget discipline. |
| [`fse-related-work`](skills/fse-related-work/SKILL.md) | Cover the SE literature lanes, write delta-first positioning, and keep self-citations double-anonymous. |
| [`fse-experiments`](skills/fse-experiments/SKILL.md) | Match evidence to claim shape: real subjects, fair baselines, SE statistics and effect sizes, qualitative rigor, contamination-aware LLM ablations, mining provenance. |
| [`fse-reproducibility`](skills/fse-reproducibility/SKILL.md) | Build the open-science story: an honest Data Availability statement, provenance pinning, and anonymized-but-runnable artifacts. |
| [`fse-supplementary`](skills/fse-supplementary/SKILL.md) | Split content between the reviewed pages and the artifact by decision-criticality — nothing that decides acceptance may live outside the body. |
| [`fse-submission`](skills/fse-submission/SKILL.md) | Final HotCRP audit: the two-step registration+submission, the ACM template and page budget, the heavy-anonymity sweep, open-science items, desk-risk triage. |
| [`fse-review-process`](skills/fse-review-process/SKILL.md) | Model the pipeline — heavy double-anonymity, ≥3 reviewers, Accept/Major Revision/Reject, the journal-style re-review — and where author leverage exists. |
| [`fse-author-response`](skills/fse-author-response/SKILL.md) | Write both turns: the initial rebuttal and the anonymous Major Revision response letter that maps every request to a tracked change. |
| [`fse-artifact-evaluation`](skills/fse-artifact-evaluation/SKILL.md) | Convert the accepted paper's package into ACM badges (Available / Functional / Reusable / Reproduced) on the artifact track's own deadline. |
| [`fse-camera-ready`](skills/fse-camera-ready/SKILL.md) | De-anonymize systematically, complete PACMSE journal metadata, permanentize availability links, and pass ACM production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026/2027 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified FSE papers across five contribution shapes — Test-of-Time and Distinguished-Paper honorees — with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional review-bot study's abstract and introduction rebuilt to the FSE arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the FSE-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./FSE-Skills
claude plugin install fse-skills
```

Or use the files directly: each `skills/fse-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an FSE paper or should it go to ICSE/ISSTA?" → `fse-topic-selection`
- "Audit my draft against the FSE research-track rules" → `fse-submission`
- "We got a Major Revision — plan the revision letter" → `fse-author-response`
- "Get this artifact ready for the ACM badges" → `fse-artifact-evaluation`

## Pack structure

```text
FSE-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── fse-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `fse-topic-selection`; FSE and ICSE overlap, so choosing by calendar
   and community pull matters. Skim the exemplars library to see what decade-influential FSE
   contributions look like.
2. **While building evidence** — keep `fse-experiments` and `fse-reproducibility` beside the study;
   threats named at design time and provenance pinned at collection time cannot be retrofitted.
3. **While writing** — `fse-writing-style` for the body against the worked example,
   `fse-supplementary` for the body/artifact split, `fse-related-work` for delta-first positioning.
4. **Deadline weeks** — register before the earlier registration cutoff, then `fse-submission` end
   to end on the final PDF and artifact.
5. **After submission** — `fse-review-process` to calibrate, `fse-author-response` for the rebuttal
   and any Major Revision round, then `fse-artifact-evaluation` and `fse-camera-ready` — or the
   routing table in `fse-topic-selection` if the decision goes the other way.

## 2026/2027-cycle anchor facts (historical snapshot, not permanent rules)

- FSE 2026 is the **34th** edition: Montreal, Canada (Concordia SGW Campus), **July 5-9, 2026**.
  Research registration 4 Sep 2025; submission 11 Sep 2025 (AoE). General Chairs Shin Hwei Tan and
  Foutse Khomh.
- FSE 2027 is the **35th** edition: Shenzhen, China, **July 12-16, 2027**; research deadline
  **2 Oct 2026** (AoE); page budget **≤18 pages** text+figures **+ 4** reference pages; **≥3** PC
  reviewers per paper. This is the live next research target as of 2026-07-09.
- Publication: **PACMSE**, open access, no APC. Review: **double-anonymous "heavy."** Decisions:
  Accept / **Major Revision** / Reject. Template: **ACM Primary Article Template**.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026/2027 facts** — carry dates/budgets and trace to a numbered source in the source
   map (e.g., the PACMSE publication, the 18+4 FSE 2027 budget, the heavy-anonymity rule).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the exact
   organizing-committee roster beyond the named General Chairs).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., FSE 2026/2027 full
   Program Co-Chair rosters, artifact-track deadlines, any AI-use disclosure policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. FSE re-decides its structure per edition —
  including the number of submission deadlines, which differed between FSE 2024 and later years — so
  verify the cadence before anything else each year.
- FSE has no standing editor-in-chief and no APC; chairs rotate per edition. Treat journal-style
  *continuity* assumptions about people as errors even though the *publication* is a journal.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar tool name is not
  proof of an FSE placement.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

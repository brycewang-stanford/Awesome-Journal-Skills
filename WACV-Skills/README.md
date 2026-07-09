# WACV Skills

Twelve agent skills for papers targeting **WACV — the IEEE/CVF Winter Conference on
Applications of Computer Vision**, the applications-first winter member of the Computer
Vision Foundation's four-venue calendar (CVPR in summer, ICCV/ECCV in autumn, WACV in
winter). The pack covers the whole arc of a WACV campaign as it actually runs: choosing the
**Applications or Algorithms track**, deciding **which of two submission rounds** to enter,
building constraint-aware evidence, clearing OpenReview's double-blind checks, writing the
optional **one-page Round 1 rebuttal**, executing a **Revise-and-Resubmit** revision into
the **no-rebuttal Round 2**, and landing the paper in CVF open access and IEEE Xplore.

Official basis cross-checked on **2026-07-09**: the WACV 2027 Call for Papers, Author
Guidelines, and Dates page; the WACV 2027 Round 1 / Round 2 OpenReview groups; the WACV 2026
Author/Reviewer Guides and conference page; the IEEE Computer Society WACV call; CVF
open-access and IEEE Xplore records; dblp; and the official `@wacv_official` account's posted
round statistics. Direct fetches of `wacv.thecvf.com` and `openaccess.thecvf.com` were
blocked (HTTP 403) in the verification environment, so official pages were read through
search-engine renderings of the exact URLs and cross-checked against OpenReview, dblp, IEEE
Xplore, and archived per-year WACV sites; the full trail — including everything still marked
待核实 — is in [`resources/official-source-map.md`](resources/official-source-map.md).

**Cycle status:** WACV 2026 (Tucson, March 6-10, 2026) is the most recent completed cycle
and supplies the verified formatting anchors. The **WACV 2027 cycle is live and mid-flight**:
as of 2026-07-09 the Round 1 paper deadline (reported June 26, 2026) has passed and we are
inside the Round 1 review window, with the Round 2 deadline (reported August 28, 2026)
imminent. The exact 2027 conference dates and host city are still 待核实.

## What makes WACV unlike its CVF siblings

The mechanics that drive every skill in this pack — and that CVPR, ICCV, and ECCV do **not**
share:

- **A two-round, journal-style review.** Round 1 papers get at least three reviews and an
  area-chair recommendation of **Accept**, **Revise and Resubmit**, or **Reject**. Revised
  papers and new submissions are then judged in Round 2, which returns only **Accept** or
  **Reject**. No other CVF venue offers a formal revision path.
- **The revision lap is the main event.** In WACV 2025's Round 1, of 1,381 submissions
  roughly 12% were accepted outright, ~37% rejected, and **~51% invited to revise** — most
  papers are decided in the Revise-and-Resubmit lap, not the first review.
- **The rebuttal exists only in Round 1.** Authors may file an optional one-page rebuttal
  after Round 1 reviews; **Round 2 has no rebuttal**, so a rushed revision cannot be argued
  back later.
- **Two tracks, two review criteria.** An **Applications track** (judged on systems-level
  innovation, domain novelty, and comparative assessment under real constraints) and an
  **Algorithms track** (judged on algorithmic novelty and matched-baseline evaluation).
  Authors pick one primary track, and the choice reshapes the first page.
- **Applications-first identity.** WACV exists to review computer vision that works under
  real-world constraints — low-power inference, data scarcity, in-the-wild robustness — not
  method for its own sake.
- **Familiar CVF plumbing.** Eight pages including figures and tables (references-only
  overflow), double-blind OpenReview submission with a valid-profile-or-desk-reject rule, an
  anonymized supplement, and dual publication in CVF open access (free, watermarked) plus
  IEEE Xplore (version of record). No article-processing charge; chairs rotate each edition,
  so there is no standing editor-in-chief.

## Skills

| Skill | What it does |
| --- | --- |
| [`wacv-topic-selection`](skills/wacv-topic-selection/SKILL.md) | Test whether a project is an applications-under-constraint contribution, route between WACV and CVPR/ICCV/ECCV/3DV/journals, and choose the Applications vs Algorithms track. |
| [`wacv-workflow`](skills/wacv-workflow/SKILL.md) | Run the branching two-round calendar: round/track choice, Round 1 submission and rebuttal, the Accept/Revise-and-Resubmit/Reject fork, the Round 2 revision, camera-ready, and the winter conference. |
| [`wacv-writing-style`](skills/wacv-writing-style/SKILL.md) | Write the first page for your track and for the two-round reviewer, so the obvious revision question is answered before it is asked. |
| [`wacv-related-work`](skills/wacv-related-work/SKILL.md) | Cover the vision, sibling-venue, concurrent, and application-domain shelves; keep self-citations double-blind; verify cited "WACV papers" are WACV papers. |
| [`wacv-experiments`](skills/wacv-experiments/SKILL.md) | Build track-appropriate evidence — constraint-aware systems results or matched-baseline novelty — with comparative assessment and honest uncertainty. |
| [`wacv-reproducibility`](skills/wacv-reproducibility/SKILL.md) | Maintain the recipe ledger, reproduce the deployed constraint not just accuracy, and keep paper and artifact in sync across the revision lap. |
| [`wacv-supplementary`](skills/wacv-supplementary/SKILL.md) | Split content between the 8-page body and the anonymized supplement; package videos as evidence without breaking double-blind. |
| [`wacv-artifact-evaluation`](skills/wacv-artifact-evaluation/SKILL.md) | Build the sealed anonymous review artifact and the public release, including constraint reproduction and dataset licensing. |
| [`wacv-submission`](skills/wacv-submission/SKILL.md) | Final OpenReview audit: round and track fields, profiles, page cap, anonymity sweep, dual submission, desk-reject triage. |
| [`wacv-review-process`](skills/wacv-review-process/SKILL.md) | Model the two-round pipeline, the three Round 1 recommendations, the no-rebuttal Round 2, and where author leverage actually exists. |
| [`wacv-author-response`](skills/wacv-author-response/SKILL.md) | Write the one-page Round 1 rebuttal and, separately, the Revise-and-Resubmit change summary that carries a paper into Round 2. |
| [`wacv-camera-ready`](skills/wacv-camera-ready/SKILL.md) | Deliver the version of record: de-anonymization, real links, dataset release, CVF/IEEE dual publication, and the winter presentation. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Thirteen official sources with access dates, the verified two-round and formatting facts, the access-method disclosure, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces (both OpenReview round groups) plus five author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Metadata-verified WACV papers across the two tracks (GeoDiffuser, Re-Evaluating LiDAR Scene Flow), plus a sibling-venue misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional applications-track first page rebuilt for the two-round reviewer, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit, with WACV-only notes on round-syncing and constraint reproduction. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./WACV-Skills
claude plugin install wacv-skills
```

Or use the files directly: each `skills/wacv-*/SKILL.md` is a standalone instruction file
whose frontmatter `description` tells an agent when to fire. Typical invocations:

- "Is this a WACV paper, and which track?" → `wacv-topic-selection`
- "Should I submit in Round 1 or Round 2?" → `wacv-workflow` / `wacv-submission`
- "I got Revise and Resubmit — what now?" → `wacv-author-response` / `wacv-review-process`
- "Audit my draft against WACV's page and anonymity rules" → `wacv-submission`

## Pack structure

```text
WACV-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── wacv-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared repro kit
```

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified facts** — trace to a numbered source in the source map (the two-round model
   and its three Round 1 outcomes, the 8-page-including-figures cap, the double-blind
   OpenReview rule, the WACV 2025 Round 1 statistics, the CVF/IEEE dual publication).
2. **Reported facts** — consistent secondary or single-first-party sources, labeled as such
   (the reported WACV 2027 round dates read via search rendering, blended acceptance-rate
   bands, best-paper designations beyond the verified GeoDiffuser item).
3. **Unverifiable-at-check-time items** — explicitly 待核实 (the exact WACV 2027 conference
   dates and city, supplementary size caps, camera-ready page allowance and forms,
   presentation obligations, any AI-disclosure requirement).

If a skill states class-2/3 material as class 1, treat it as a bug and fix it against the
live official pages.

## Maintenance notes

- Every date and rule here is a **cycle snapshot**. WACV policies are re-set annually by
  rotating chairs — reopen `wacv.thecvf.com` for the current cycle, and remember it runs
  **two OpenReview groups**, before deadline-sensitive advice.
- The reported WACV 2027 round dates were read through search renderings; reconfirm them on
  the live Dates page, and treat the conference dates/city as 待核实.
- The two-round model, the three Round 1 outcomes, and the Applications/Algorithms split are
  the load-bearing distinctives — if a future cycle changes them, most of this pack must be
  re-reasoned, not just re-dated.
- When adding exemplars, follow the verification recipe at the bottom of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a `thecvf.com` URL is
  only a WACV citation if its path reads `WACV20XX`.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

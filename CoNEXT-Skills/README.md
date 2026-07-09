# ACM CoNEXT Skills

Twelve agent skills for papers targeting **CoNEXT — the ACM International Conference on emerging
Networking EXperiments and Technologies**, ACM SIGCOMM's systems-networking venue and, since its
move into **PACMNET (Proceedings of the ACM on Networking)**, a journal-style publication. The
pack covers the full arc of a CoNEXT campaign: deciding whether a networking project is
CoNEXT-shaped or belongs at SIGCOMM, NSDI, IMC, or SIGMETRICS; building measurement and
systems evidence that survives a networking reviewer's scrutiny; choosing between the **December**
and **June** submission cycles; packaging the double-anonymous HotCRP submission; navigating the
**one-shot "major" revision** re-read by the original reviewers; and delivering the PACMNET
camera-ready plus an optional ACM reproducibility badge.

Official basis checked on **2026-07-09**: the CoNEXT 2026 call and Important Dates, the CoNEXT
2025 CFP, the PACMNET journal and editorial pages, the CoNEXT HotCRP sites, and the ACM
reproducibility-badging policy. Direct fetches of `conferences.sigcomm.org`, `dl.acm.org`, and the
CFP mirrors returned 403 in the verification environment, so official pages were read via
search-engine renderings of the exact URLs and cross-checked against the ACM Digital Library
(PACMNET editorials and tables of contents), dblp CoNEXT proceedings, and the RIPE RACI re-posting
of the CFP; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Name-collision warning: "Conext" is also a Schneider Electric inverter product line and an
> unrelated networking product; this pack is **only** about the ACM SIGCOMM conference. No fact
> here derives from any other "Conext."

## What makes CoNEXT different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice in the skills — and
most of the mistakes made by authors arriving from SIGCOMM, NSDI, IMC, or an ML venue:

- **Two submission deadlines a year, one program.** CoNEXT runs a **December** cycle and a
  **June** cycle that both feed the same annual conference and the same rolling PACMNET volume.
  The December-cycle path for CoNEXT 2026: register 5 Dec 2025, submit 12 Dec 2025, notify
  31 Mar 2026; the June-cycle submission is 5 Jun 2026. Which cycle you enter is a real strategic
  choice, not a formality.
- **Papers are journal articles.** CoNEXT research papers publish in **PACMNET**, an open-access
  ACM journal backed by SIGCOMM; accepted papers are scheduled into the **closest PACMNET issue**
  (issues are named by cycle, e.g., Vol 4 CoNEXT1 March 2026). The submission is judged like a
  journal manuscript that also earns a conference slot.
- **A one-shot "major" revision, re-read by the same reviewers.** First decisions are Accept,
  **Reject**, or a **one-shot major revision** that arrives with a summary of merits and a list of
  **minimum necessary changes**; authors get about **two months** to revise, then the **original
  reviewers** decide accept or reject. It is a genuine journal-style R&R, not a rebuttal, and there
  is exactly one shot.
- **Double-anonymous, SIGCOMM-style review.** Two rounds of reviews, online discussion, and a
  **TPC meeting**, with **shepherding** of revised/conditionally-accepted papers, all under
  double-anonymity — carrying the SIGCOMM public-review and shepherding culture.
- **The ACM `acmart` path.** Long papers **≤16 pages** (+ unlimited references + up to 4 appendix
  pages), short papers **≤10 pages** (+ unlimited references + up to 2 appendix pages), in the ACM
  `acmart` template — not an IEEE two-column box.
- **Reproducibility by a committee, badges by opt-in.** A separate **reproducibility committee**
  awards **optional ACM badges**; you must **opt in before the submission deadline** and send a
  one-page artifact description within a week of acceptance.
- **A systems-and-measurement evidence culture.** Real testbeds, deployments, traces, and
  reproducible measurement — not leaderboard scores — are the community norms the networking
  reviewer pool enforces.

## Skills

| Skill | What it does |
| --- | --- |
| [`conext-topic-selection`](skills/conext-topic-selection/SKILL.md) | Route between CoNEXT and its siblings (SIGCOMM, NSDI, IMC, SIGMETRICS, MobiCom, HotNets) by contribution shape, evidence maturity, and — decisively — which of the two annual cycles lands first. |
| [`conext-workflow`](skills/conext-workflow/SKILL.md) | Run the two-cycle year backward from the December or June deadline, through registration, the one-shot revision window, reproducibility badging, PACMNET camera-ready, and presentation. |
| [`conext-writing-style`](skills/conext-writing-style/SKILL.md) | Build the networking-systems skeleton: the networking problem and deployment context up front, claims tied to measurements, page-budget discipline in `acmart`. |
| [`conext-related-work`](skills/conext-related-work/SKILL.md) | Cover the networking literature lanes, write delta-first positioning against SIGCOMM/NSDI/IMC, and keep self-citations double-anonymous. |
| [`conext-experiments`](skills/conext-experiments/SKILL.md) | Match evidence to claim shape: real testbeds and deployments, honest baselines, measurement statistics, trace provenance, and contamination-aware ML-for-networking ablations. |
| [`conext-reproducibility`](skills/conext-reproducibility/SKILL.md) | Build the reproducible-networking story: pinned traces and configs, a runnable artifact, and the one-page description the reproducibility committee needs. |
| [`conext-supplementary`](skills/conext-supplementary/SKILL.md) | Split content between the reviewed pages, the appendix budget, and the artifact by decision-criticality — nothing that decides acceptance may hide in an appendix or repo. |
| [`conext-submission`](skills/conext-submission/SKILL.md) | Final HotCRP audit: the right cycle and its registration step, the `acmart` page budget, the double-anonymous sweep, reproducibility opt-in, and desk-risk triage. |
| [`conext-review-process`](skills/conext-review-process/SKILL.md) | Model the pipeline — double-anonymity, two review rounds, discussion, TPC meeting, the one-shot major revision, shepherding — and where author leverage exists. |
| [`conext-author-response`](skills/conext-author-response/SKILL.md) | Write both turns: the initial rebuttal and the one-shot major-revision response letter that maps every "minimum necessary change" to a tracked edit for the same reviewers. |
| [`conext-artifact-evaluation`](skills/conext-artifact-evaluation/SKILL.md) | Convert the accepted paper's package into optional ACM badges via the reproducibility committee, from the opt-in to the one-page description to evaluator-proof reuse. |
| [`conext-camera-ready`](skills/conext-camera-ready/SKILL.md) | De-anonymize systematically, complete PACMNET journal metadata, permanentize artifact links, and pass ACM production checks for the assigned issue. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026-cycle facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Web-verified CoNEXT papers across contribution shapes, with self-check questions and sibling-venue guards. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional congestion-control study's abstract and introduction rebuilt to the CoNEXT arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the CoNEXT-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./CoNEXT-Skills
claude plugin install conext-skills
```

Or use the files directly: each `skills/conext-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a CoNEXT paper or should it go to SIGCOMM/NSDI/IMC?" → `conext-topic-selection`
- "Which cycle should we target, December or June?" → `conext-workflow`
- "Audit my draft against the CoNEXT CFP rules" → `conext-submission`
- "We got a one-shot major revision — plan the response" → `conext-author-response`
- "Get this artifact ready for an ACM reproducibility badge" → `conext-artifact-evaluation`

## Pack structure

```text
CoNEXT-Skills/
├── .claude-plugin/              # plugin.json + marketplace.json (12 skills declared)
├── README.md                    # this file
├── README.zh-CN.md              # 中文说明
├── LICENSE                      # MIT
├── assets/cover.svg             # pack cover
├── skills/
│   └── conext-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md                # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md           # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `conext-topic-selection`; CoNEXT overlaps SIGCOMM and NSDI, and the
   two-cycle calendar means the *nearest honest deadline* often decides. Skim the exemplars library
   to see what CoNEXT contributions look like.
2. **While building evidence** — keep `conext-experiments` and `conext-reproducibility` beside the
   testbed; traces and configs pinned at collection time cannot be reconstructed later, and badge
   opt-in is due at submission.
3. **While writing** — `conext-writing-style` for the body against the worked example,
   `conext-supplementary` for the body/appendix/artifact split, `conext-related-work` for
   delta-first positioning.
4. **Deadline weeks** — pick the cycle in `conext-workflow`, register before the earlier cutoff,
   then `conext-submission` end to end on the final PDF and artifact.
5. **After submission** — `conext-review-process` to calibrate, `conext-author-response` for the
   rebuttal and the one-shot major-revision letter, then `conext-artifact-evaluation` and
   `conext-camera-ready` — or the routing table in `conext-topic-selection` if the decision goes
   the other way.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- CoNEXT 2026 is the **22nd** edition: **Utrecht, The Netherlands, December 7-11, 2026**, sponsored
  by ACM SIGCOMM, papers in **PACMNET**.
- **December cycle:** registration 5 Dec 2025, submission 12 Dec 2025, early-reject Feb 2026,
  notification 31 Mar 2026, camera-ready 30 Apr 2026, June 2026 PACMNET issue. Major-revision path:
  revision due 29 May 2026, resubmission 5 Jun 2026, camera-ready 31 Jul 2026. **June cycle:**
  submission 5 Jun 2026.
- Publication: **PACMNET**, open access. Review: **double-anonymous**, two rounds + TPC meeting.
  Decisions: Accept / Reject / **one-shot major revision**. Template: **ACM `acmart`**; long ≤16
  pages (+refs + ≤4 appendix), short ≤10 pages (+refs + ≤2 appendix). Optional **ACM reproducibility
  badges** via a committee, opt-in before submission.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026-cycle facts** — carry dates/budgets and trace to a numbered source in the
   source map (e.g., PACMNET publication, the two-cycle dates, the one-shot revision, the badge
   opt-in rule).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the
   organizing-committee roster beyond what the live committee page confirms).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., exact 2026 page numbers,
   per-cycle HotCRP URLs, whether public reviews are published with PACMNET articles, the full-year
   acceptance rate).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. CoNEXT re-decides its structure per edition
  — including both cycles' dates and the revision mechanics — so verify the two-cycle calendar
  before anything else each year.
- CoNEXT has no standing conference editor-in-chief and rotates chairs per edition; PACMNET's
  Editorial Board is the journal-side continuity. Treat continuity assumptions about conference
  *people* as errors even though the *publication* is a journal.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar tool name is not
  proof of a CoNEXT placement (many networking classics are SIGCOMM, NSDI, or IMC papers).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

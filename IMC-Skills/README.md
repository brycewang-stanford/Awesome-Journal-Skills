# ACM IMC Skills

Twelve agent skills for papers targeting **IMC — the ACM Internet Measurement Conference**, the
ACM SIGCOMM-sponsored flagship for empirical Internet and network measurement. The pack covers
the full arc of an IMC campaign: deciding whether a project is measurement-first (IMC) or belongs
at SIGCOMM, NSDI, CoNEXT, or PAM; designing measurements whose **vantage points, datasets, and
methodology** survive a measurement reviewer's audit; clearing IMC's **measurement-ethics and
responsible-disclosure** bar; packaging the double-blind `acmart` HotCRP submission with its
**artifact-availability declaration**; navigating the **two-deadline cycle** and its
**One-Shot-Revision** round; and — if the work releases a dataset, tool, or platform — competing
for the **Community Contribution Award**.

Official basis first checked on **2026-07-09** and **re-verified 2026-11-23** by direct page loads:
the IMC 2027 home, call for papers, submission instructions, and committees page (the pack now
targets **IMC 2027**, Atlanta, Georgia, USA, October 25-29, 2027); the IMC 2026 pages as the
previous cycle; the IMC 2025 call; the IMC HotCRP sites; the SIGCOMM IMC event page; and the ACM
Digital Library IMC proceedings (`dl.acm.org` still returns 403 from the verification
environment). The full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Name-collision warning: "IMC" is also the Leeds *International Medieval Congress* and an *Indian
> Management Conclave*, and there is an IEEE services-computing "IMC" track — **none** of those is
> this IMC. No fact in this pack derives from them.

## What makes IMC different from its siblings

These venue mechanics, verified for the IMC 2027 cycle, drive most of the advice in the skills — and
most of the mistakes made by authors arriving from SIGCOMM, NSDI, a security venue, or an ML
conference:

- **Measurement is the contribution.** IMC rewards *what you learned about the real Internet* and
  *how you measured it* — vantage points, datasets, ground truth, and methodology — more than a
  new system or protocol. A brilliant system with a thin measurement is a SIGCOMM/NSDI paper; a
  modest technique that reveals something real about the network is IMC-shaped.
- **Two deadlines a year, with a One-Shot-Revision round.** IMC runs two submission deadlines
  (IMC 2027: cycle 1 17 Nov 2026, cycle 2 7 Apr 2027), and IMC 2027 adds a **short rebuttal
  phase**. Decisions are Accept, **One-Shot-Revision**, or Reject. A One-Shot-Revision is a *tightly bounded* revise-and-resubmit — a few concrete
  action points, a required reviewer champion, re-judged by the same reviewers at the next
  deadline — not an open-ended major revision.
- **Ethics is a gate, not a footnote.** A **mandatory Ethics appendix section** is required;
  papers without one may be rejected. IMC 2027 adds two more mandatory appendix sections,
  **Open Science** and **Generative AI**. Measurement that touches human subjects, user data, or
  live networks is judged against **Belmont Report** principles (respect for persons, beneficence,
  justice), with **IRB** review and **responsible disclosure** expectations that most systems
  venues do not enforce as hard.
- **Datasets and artifacts are first-class.** Every submission carries an **artifact-availability
  declaration** (full / partial / none) and, in IMC 2027, an **Open Science** appendix; accepted papers are **shepherded** to make promised
  artifacts available; and the **Community Contribution Award** exists specifically to honor a
  released dataset, tool, or platform (public by camera-ready).
- **A Replicability Track.** IMC runs a dedicated track — screened by an **Expression of
  Interest** — for studies that reproduce or replicate prior measurement results, with priority
  to replicability. Measurement's dependence on a moving Internet makes this a venue-defining
  feature.
- **The ACM path, double-blind, generous body.** IMC uses the **ACM `acmart` template**,
  **double-blind** review, a **BBL upload** of the references, and a comparatively generous
  budget (IMC 2027: **up to 13 pages** of technical content + unlimited references/appendices;
  short papers up to 6). Do not carry an IEEE two-column habit across.

## Skills

| Skill | What it does |
| --- | --- |
| [`imc-topic-selection`](skills/imc-topic-selection/SKILL.md) | Route between IMC and its siblings (SIGCOMM, NSDI, CoNEXT, PAM, USENIX Security, WWW, journals) using the measurement-first test, the dataset/vantage-point lens, and the two-deadline calendar. |
| [`imc-workflow`](skills/imc-workflow/SKILL.md) | Run the year backward from whichever of the two deadlines you are targeting, through registration, the One-Shot-Revision round, shepherding, and the camera-ready. |
| [`imc-writing-style`](skills/imc-writing-style/SKILL.md) | Build the measurement-paper skeleton: the finding on the first page, methodology and vantage points made auditable, limitations argued, the Ethics section written early. |
| [`imc-related-work`](skills/imc-related-work/SKILL.md) | Cover the measurement literature lanes, position against prior datasets and vantage points, and keep the delta and self-citations double-blind. |
| [`imc-experiments`](skills/imc-experiments/SKILL.md) | Match evidence to claim: representative vantage points, ground truth, longitudinal stability, ethical active measurement, and honest confounds for a moving Internet. |
| [`imc-reproducibility`](skills/imc-reproducibility/SKILL.md) | Build the availability story: the artifact-availability declaration, dataset release with provenance, and reproducibility for measurements that cannot be re-run identically. |
| [`imc-supplementary`](skills/imc-supplementary/SKILL.md) | Split content between the reviewed body and the appendix/artifact, keeping decision-critical evidence and the Ethics discussion in the reviewed pages. |
| [`imc-submission`](skills/imc-submission/SKILL.md) | Final HotCRP audit: registration, `acmart` + BBL, double-blind sweep, the Ethics section, the artifact declaration, cycle choice, and desk-risk triage. |
| [`imc-review-process`](skills/imc-review-process/SKILL.md) | Model the pipeline — double-blind, multi-round review, Accept / One-Shot-Revision / Reject, the champion rule, early reject, shepherding — and where author leverage exists. |
| [`imc-author-response`](skills/imc-author-response/SKILL.md) | Write the rebuttal and, distinctively, the One-Shot-Revision resubmission that addresses a bounded set of action points for the same reviewers. |
| [`imc-artifact-evaluation`](skills/imc-artifact-evaluation/SKILL.md) | Turn the accepted paper's data and code into a released, usable artifact — availability shepherding, DOI-issuing archives, and Community Contribution Award eligibility. |
| [`imc-camera-ready`](skills/imc-camera-ready/SKILL.md) | De-anonymize, finalize the Ethics and availability statements, permanentize dataset/code links, and pass ACM production checks for the IMC proceedings. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Web-verified IMC papers across measurement contribution shapes, with self-check questions and sibling-venue guards. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional censorship-measurement study's abstract and introduction rebuilt to the IMC arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the IMC-specific checks (availability declaration, dataset provenance, ethics) the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./IMC-Skills
claude plugin install imc-skills
```

Or use the files directly: each `skills/imc-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an IMC paper or should it go to SIGCOMM/NSDI?" → `imc-topic-selection`
- "Audit my draft against the IMC submission rules" → `imc-submission`
- "We got a One-Shot-Revision — plan the resubmission" → `imc-author-response`
- "Get our dataset ready for release and the Community Contribution Award" → `imc-artifact-evaluation`

## Pack structure

```text
IMC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── imc-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before measuring** — run `imc-topic-selection`; IMC and SIGCOMM/NSDI overlap, and the
   measurement-first test plus the two-deadline calendar decide the target. Skim the exemplars to
   see what an influential measurement contribution looks like.
2. **While collecting data** — keep `imc-experiments` and `imc-reproducibility` beside the study;
   vantage-point choices, ethics approvals, and dataset provenance cannot be retrofitted.
3. **While writing** — `imc-writing-style` for the body against the worked example,
   `imc-supplementary` for the body/appendix split, `imc-related-work` for dataset-aware
   positioning, and write the Ethics section early, not last.
4. **Deadline weeks** — register before the cycle's registration cutoff, then `imc-submission` end
   to end on the final PDF, BBL, and artifact declaration.
5. **After submission** — `imc-review-process` to calibrate, `imc-author-response` for the
   rebuttal and any One-Shot-Revision, then `imc-artifact-evaluation` and `imc-camera-ready` — or
   the routing table in `imc-topic-selection` if the decision goes the other way.

## IMC 2027 anchor facts (cycle snapshot, not permanent rules; re-verified 2026-11-23)

- IMC 2027: **Atlanta, Georgia, USA, October 25-29, 2027** (the 27th IMC). General Chairs Alberto
  Dainotti and Mike Bailey (Georgia Tech); Program Chairs Romain Fontugne (Internet Initiative
  Japan) and Narseo Vallina-Rodriguez (IMDEA Networks Institute).
- **Two deadlines (AoE):** cycle 1 register 10 Nov 2026, submit 17 Nov 2026 (One-Shot-Revision
  papers from IMC 2026: 2 Dec 2026), early reject 5 Jan 2027, **new rebuttal period 26 Jan - 2 Feb
  2027**, notification 25 Feb 2027, camera-ready 14 Apr 2027; cycle 2 register 31 Mar 2027, submit
  7 Apr 2027, notification 22 Jul 2027, camera-ready 2 Sep 2027. One-Shot-Revision resubmits to
  the next deadline, judged by the same reviewers.
- Format: **`acmart`, double-blind, BBL upload**; full papers **up to 13 pages** of technical
  content, short papers **up to 6**, + unlimited references/appendices. Three mandatory appendix
  sections: **Ethics**, **Open Science**, **Generative AI**.
- Submission sites: cycle-specific HotCRP instances (`imc2027-cycle1.hotcrp.com`, then
  `imc2027-cycle2` and `imc2027-repro` for the Replicability EoI).
- Previous cycle (history): IMC 2026 was held in Karlsruhe, Germany, October 12-16, 2026, with the
  same 13/6-page budget.
- Datasets/artifacts: **availability declaration** at submission, **shepherding** after
  acceptance, **Community Contribution Award** for public releases; a **Replicability Track** with
  an EoI screen.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified IMC 2027 facts** — carry dates/limits and trace to a numbered source in the source map
   (e.g., the two-deadline cadence, One-Shot-Revision, the mandatory Ethics section, the artifact
   declaration, the Community Contribution Award).
2. **Reported facts** — read only via secondary renderings and labeled as such (since the
   2026-11-23 direct re-read, the IMC 2027 registration and camera-ready dates are verified, not
   reported).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., whether formal ACM
   reproducibility badges are awarded, the public-review tradition's
   current status, acceptance rate, and the full PC roster).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and limit above is a **cycle snapshot**. IMC re-decides its structure per edition —
  including the exact deadline dates, page limits, and One-Shot-Revision mechanics — so verify on
  the current call and submission instructions before anything else each year.
- IMC has no standing editor-in-chief; chairs rotate per edition under ACM SIGCOMM. Treat
  continuity assumptions about people as errors.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar dataset or tool
  name is not proof of an IMC placement (much measurement work lands at SIGCOMM, NSDI, or PAM).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

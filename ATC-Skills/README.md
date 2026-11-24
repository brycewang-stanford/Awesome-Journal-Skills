# ATC Skills

Twelve agent skills for papers targeting **ATC — the ACM SIGOPS Annual Technical Conference**, the
venue known for about fifty years as the **USENIX Annual Technical Conference** and, from the 2026
edition, continued under **ACM SIGOPS**. ATC is the systems community's **broad, practical**
conference: it takes a wider slice of computer systems than the more selective OSDI/SOSP flagships,
prizes real implementations and experimental results, and runs a dedicated **Operational Systems**
lane. The pack covers a full ATC campaign: deciding whether a project is ATC-shaped or belongs at
OSDI, NSDI, EuroSys, FAST, or a workshop; surviving the **two-round review whose first round reads
only your first two pages**; anonymizing the double-blind HotCRP submission; using the 72-hour
author response; navigating **conditional acceptance and shepherding**; and delivering the
camera-ready plus a badged artifact.

Official basis **re-verified on 2026-11-24** by direct fetch: the ATC 2027 SIGOPS home page, call
for papers and organizers page, the `atc27.hotcrp.com` site, the ATC 2026 home page, call and
HotCRP clock, the sysartifacts ATC 2026 page, the USENIX ATC '25 artifact call, the USENIX sunset
announcement, and the ACM SIGOPS conference list. The original 2026-07-09 pass read `sigops.org`
and `usenix.org` through search-engine renderings because they then returned 403. The full trail,
including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> **USENIX ATC is retired.** USENIX ended the USENIX Annual Technical Conference after **USENIX
> ATC '25 (July 2025)**; there is no USENIX ATC '26 or later. The conference continues, same
> acronym, as the **ACM SIGOPS Annual Technical Conference** (first SIGOPS edition: ATC 2026, Hong
> Kong, November 2026). This pack now describes **ATC 2027**.

> Acronym-collision warning: **ATC** also names the *American Transplant Congress* and an *Academic
> Tax Conference*. Neither is this ATC, and no fact in this pack derives from them. This ATC is the
> computer-systems conference.

## What makes ATC different from its siblings

These venue mechanics, verified for the 2027 cycle (re-verified 2026-11-24), drive most of the
advice in the skills — and most of the mistakes made by authors arriving from OSDI/SOSP, from
NSDI, from an older USENIX ATC cycle, or even from ATC 2026:

- **Sponsor, name, and calendar changed — and keep changing.** After ~50 years as **USENIX ATC**,
  ATC is an **ACM SIGOPS** conference. ATC 2026 met in Hong Kong (15-18 November 2026) on a June
  deadline; **ATC 2027 meets in Rennes, France, 28 June – 1 July 2027**, with a **19 January 2027
  (AoE)** submission deadline. Do not carry a USENIX-era or 2026 assumption forward.
- **Round one reads your first two pages.** Submissions get two review rounds; the **first is based
  on the first two pages** and rejects papers that are out of scope, poorly motivated, hard to
  understand, incremental, poorly placed against related work, or weakly evaluated. Make the
  introduction self-contained. (ATC 2026 used a separate two-page extended abstract instead; that
  is gone in 2027.)
- **A 72-hour author response for every paper** (3-5 April 2027): facts and answers to reviewer
  questions only — no new experiments or data, no promises.
- **Tight caps.** Long papers ≤ **12** pages and short ≤ **6**, excluding references but
  **including appendices**; each author may be on at most **2** submissions.
- **Breadth is the point.** ATC's scope spans OS, runtimes, storage, networking, ML for systems and
  systems for ML, virtualization, distributed systems, performance, reliability, energy, and
  troubleshooting, with an emphasis on **implementations and experimental results**. Papers whose
  main contribution is not systems may be desk-rejected.
- **Operational Systems papers are first-class.** A dedicated track judges deployment papers on new
  insights, data, or lessons, and may identify the organization behind the system.
- **Double-blind, then shepherded.** Accepted papers are **conditionally accepted** and must satisfy
  a **shepherd**; every accepted paper is presented orally and/or as a poster, and not every paper
  gets an oral slot.
- **Badged artifacts.** Artifacts earn badges from an Artifact Evaluation Committee on a separate
  post-acceptance schedule (USENIX lineage: Available / Functional / Reproduced; ATC '25: 94%
  Functional, 77% Reproduced). The ATC 2027 artifact call is not yet published.
- **Open access with an APC.** USENIX ATC published proceedings, slides, and talk videos free; the
  SIGOPS editions publish under **ACM Open Access**, with an APC for authors outside ACM Open
  institutions.

## Skills

| Skill | What it does |
| --- | --- |
| [`atc-topic-selection`](skills/atc-topic-selection/SKILL.md) | Route between ATC and its siblings (OSDI, SOSP, NSDI, EuroSys, FAST, HotOS/workshops) using breadth-vs-selectivity, the deployed-systems test, and the calendar. |
| [`atc-workflow`](skills/atc-workflow/SKILL.md) | Run the year backward from the 19 January 2027 deadline through the two review rounds, the 72-hour response, conditional-acceptance shepherding, artifact evaluation, and the 28 May camera-ready. |
| [`atc-writing-style`](skills/atc-writing-style/SKILL.md) | Build the systems paper: first two pages that survive round one on their own, an implementation-and-measurement narrative, and page-budget discipline in the two-column format. |
| [`atc-related-work`](skills/atc-related-work/SKILL.md) | Cover the systems literature lanes, position against OSDI/NSDI/EuroSys/FAST, and keep self-citation double-blind. |
| [`atc-experiments`](skills/atc-experiments/SKILL.md) | Match evidence to claim: real testbeds, honest baselines, end-to-end plus microbenchmarks, tail latency and variance, and workload realism. |
| [`atc-reproducibility`](skills/atc-reproducibility/SKILL.md) | Build the artifact story: pinned environments, a turnkey path to the headline numbers, and an anonymized-but-runnable review package. |
| [`atc-supplementary`](skills/atc-supplementary/SKILL.md) | Split content across the first two pages, the body, the in-limit appendix, and the artifact by review-round and decision-criticality. |
| [`atc-submission`](skills/atc-submission/SKILL.md) | Final HotCRP audit: the 12/6-page budget with appendices inside it, the two-paper author cap, the double-blind sweep, and desk-risk triage before the AoE cutoff. |
| [`atc-review-process`](skills/atc-review-process/SKILL.md) | Model the pipeline — two rounds with a first-two-pages gate, the 72-hour response, conditional acceptance, shepherding, oral vs. poster — and where author leverage exists. |
| [`atc-author-response`](skills/atc-author-response/SKILL.md) | Write the 72-hour author response, the resubmission change summary, and the description-of-changes a shepherd will check line by line. |
| [`atc-artifact-evaluation`](skills/atc-artifact-evaluation/SKILL.md) | Convert the accepted paper's package into Available / Functional / Reproduced badges on the AEC's own deadline. |
| [`atc-camera-ready`](skills/atc-camera-ready/SKILL.md) | De-anonymize, satisfy the shepherd's required revisions, complete ACM Open Access metadata, and pass production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Fourteen sources with URLs and access dates; verified ATC 2027 facts; ATC 2026 and USENIX ATC history; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces (SIGOPS CFP, ATC HotCRP, USENIX legacy pages, ACM DL) plus cross-check sources for when the gateway blocks a direct fetch. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Verified USENIX ATC papers across contribution shapes — Test-of-Time and Best-Paper honorees — with self-check questions and sibling-venue guards. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional storage-cache paper's opening two pages (abstract + introduction) rebuilt to the ATC arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the ATC-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ATC-Skills
claude plugin install atc-skills
```

Or use the files directly: each `skills/atc-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an ATC paper or should it go to OSDI/NSDI?" → `atc-topic-selection`
- "Audit my draft against the ATC 2027 rules" → `atc-submission`
- "Make my first two pages survive round one" → `atc-writing-style`
- "We were conditionally accepted — plan the shepherd revision" → `atc-author-response`
- "Get this artifact ready for the ATC badges" → `atc-artifact-evaluation`

## Pack structure

```text
ATC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── atc-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `atc-topic-selection`; ATC overlaps OSDI/NSDI/EuroSys/FAST, and the
   breadth-vs-selectivity call plus the January-deadline calendar matters. Skim the exemplars for what durable
   ATC contributions look like.
2. **While building evidence** — keep `atc-experiments` and `atc-reproducibility` beside the system;
   testbed provenance and pinned environments cannot be retrofitted at submission time.
3. **While writing** — `atc-writing-style` for self-standing first two pages and body,
   `atc-supplementary` for the first-pages/body/appendix/artifact split, `atc-related-work` for
   sibling-aware positioning.
4. **Deadline weeks** — `atc-submission` end to end on the paper upload, the author-cap check,
   and the double-blind sweep, before the 19 January 2027 AoE cutoff.
5. **After submission** — `atc-review-process` to calibrate the two rounds, `atc-author-response`
   for the 72-hour response and the shepherd's description-of-changes, then `atc-artifact-evaluation` and
   `atc-camera-ready` — or the routing table in `atc-topic-selection` if the decision goes the
   other way.

## 2027-cycle anchor facts (dated snapshot, not permanent rules)

- ATC 2027 is the **second ACM SIGOPS Annual Technical Conference**: **Le Couvent des Jacobins,
  Rennes, France, 28 June – 1 July 2027**. General Chair David Bromberg; PC Chairs Vijay
  Chidambaram and Peter Pietzuch; AE Chairs Miguel Matos and Valerio Schiavoni.
- **Dates:** submission **19 January 2027** (AoE, no extensions); author response **3-5 April
  2027** (72 hours); notification **27 April 2027**; camera-ready **28 May 2027**. HotCRP:
  `atc27.hotcrp.com`.
- **Review:** two rounds, the first based on the first two pages; optional author response for
  every paper. **≤12 pages** long, **≤6** short, excluding references but including appendices;
  **two-column**, 178×229 mm, 10pt, `\documentclass[sigplan,10pt]{acmart}`. **Double-blind.**
  **≤2 submissions per author.** **Conditional acceptance + shepherding**; oral and/or poster.
- **Publication:** ACM Open Access (APC for authors outside ACM Open; the ATC CFP quotes no rate).
- **History:** ATC 2026 (first SIGOPS edition) met in Hong Kong, 15-18 November 2026, after a
  **10 June 2026** deadline and a two-page extended-abstract first round. USENIX ATC '25 (July
  2025) was the last USENIX edition.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2027 facts** — carry dates/limits and trace to a numbered source in the source map
   (e.g., the first-two-pages round, the 12/6-page budget including appendices, the two-paper cap).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., past
   submission volumes).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the ATC 2027 artifact
   call and badge set, the camera-ready page allowance, the exact APC applied to ATC papers).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- ATC is still settling after the transition: ATC 2026 moved name, sponsor, publisher and calendar
  at once, and ATC 2027 then dropped the extended abstract, moved the deadline to January, counted
  appendices in the page limit, and added a two-paper cap. Re-verify each rule against the current
  SIGOPS call before advising — none is a stable, permanent rule yet.
- ATC has no standing editor-in-chief; chairs rotate per edition under SIGOPS. USENIX's legacy ATC
  proceedings, slides, and videos remain on the USENIX site; new editions publish in the ACM DL
  under Open Access.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a famous systems name is not
  proof of an ATC placement (many landmark systems papers are OSDI/SOSP/NSDI, not ATC).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

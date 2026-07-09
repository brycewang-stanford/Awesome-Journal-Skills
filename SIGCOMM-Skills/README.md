# SIGCOMM Skills

Twelve agent skills for papers targeting **ACM SIGCOMM — the flagship conference of the
ACM Special Interest Group on Data Communication**, the top-tier annual venue for the
design, measurement, and analysis of computer networks and communication systems. The
pack is shaped around the way a SIGCOMM campaign actually runs, which departs from its
networking siblings in a way authors coming from USENIX or SIGMOBILE venues consistently
underestimate: **one main-track deadline per year** feeding **one** August conference, a
review pipeline that layers an **early-reject cut**, a **rebuttal**, and a **shepherd-run
one-shot revision**, **shepherding of accepted papers** through camera-ready, ACM
double-column formatting via **TAPS**, and an evidence bar written in the language of
**real traffic, real topology, tail latency, and reproducible "runnable" artifacts**.

Official basis checked on **2026-07-09**: the ACM SIGCOMM 2026 conference, Call-for-Papers,
submission, and camera-ready pages on `conferences.sigcomm.org`; the `sigcomm26.hotcrp.com`
deadline clock; the SIGCOMM Call-for-Artifacts and the `sigcomm.org` Test-of-Time and
Best-Paper award pages; and dblp / the ACM Digital Library for exemplar verification. Direct
fetches of `conferences.sigcomm.org`, `sigcomm.org`, `hotcrp.com`, and `dblp.org` returned
**HTTP 403** in the verification environment, so every fact below was read through
search-engine renderings of the exact official URLs and cross-checked across independent
renderings; the full trail — including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes SIGCOMM unlike its siblings

Verified for the 2026 edition; these mechanics drive most of the advice in the skills and
most of the missteps by authors arriving from a two-deadline venue:

- **One deadline, one conference, one shot per year.** SIGCOMM 2026 (the **40th** edition,
  August 17-21, 2026, Colorado Convention Center, Denver, CO) took abstracts on
  **January 30, 2026** and full papers on **February 6, 2026** (AoE; rendered as 6:59:59 AM
  EST the next morning on HotCRP). There is no fall gate to fall back on — a rejected paper
  waits a full year, which raises the stakes of the single submission far above a
  spring/fall venue.
- **Two lanes on one deadline.** Submissions choose a **research** track or an **experience**
  track for operational and deployment results; the experience track is judged on
  generalizable lessons from real operation, not on novelty alone.
- **A three-layer author-facing review pipeline.** Consensus rejects get an **early
  notification** so the work can be redirected; papers reaching the discussion phase get a
  **rebuttal**; and a small set receive a **one-shot revision** — a merits summary plus a
  required-changes list, resubmitted about a month later, **managed by a PC shepherd**,
  re-reviewed by the same reviewers where possible, and ending in **accept or reject only**.
- **Shepherding does not stop at acceptance.** A PC shepherd guides accepted papers through
  camera-ready, confirms reviewer feedback is addressed, and **must approve that any appendix
  is necessary**, signing off the final version in HotCRP.
- **12 single-spaced pages that count figures.** The body — everything before references — is
  capped at **12 single-spaced pages including figures and tables**, with references and
  optional appendices beyond the cap; pre-reference content over 12 pages **is not reviewed**.
- **Double-blind on HotCRP, ACM templates throughout.** Submissions are anonymous on
  `sigcomm26.hotcrp.com`; the abstract-registration step precedes the paper upload; both
  submission and final papers use ACM `acmart.cls` (or the ACM Word template).
- **TAPS camera-ready.** Final papers upload **PDF plus source** to HotCRP and are processed
  by the **ACM Publishing System (TAPS)** for the ACM Digital Library and Computer
  Communication Review.
- **A reproducibility culture, not just a badge.** SIGCOMM helped pioneer artifact evaluation
  in networking; accepted papers may earn **ACM badges** (Artifacts Available, Evaluated,
  Results Reproduced) through a separate committee, and the field's "runnable papers" heritage
  sets a high bar for public code, traces, and topologies.
- **The Test-of-Time and Best-Paper lineage anchors the canon** — Chord, DCTCP, pFabric, VL2,
  and other SIGCOMM classics — and reminds authors that the field's most-cited results are
  also its most-misfiled across NSDI, MobiCom, CoNEXT, and IMC.

## Skills

| Skill | What it does |
| --- | --- |
| [`sigcomm-topic-selection`](skills/sigcomm-topic-selection/SKILL.md) | Test the networking-stack contribution against SIGCOMM's breadth, pick research vs. experience track, and route misfits to NSDI, MobiCom, CoNEXT, IMC, or SIGMETRICS. |
| [`sigcomm-workflow`](skills/sigcomm-workflow/SKILL.md) | Plan the single-deadline year: backward schedule to February, the review-to-shepherd timeline, and forward planning for the next edition. |
| [`sigcomm-writing-style`](skills/sigcomm-writing-style/SKILL.md) | Build the measured-pain → design-principle → tail-evidence arc inside 12 figure-inclusive pages, with percentiles replacing superlatives. |
| [`sigcomm-related-work`](skills/sigcomm-related-work/SKILL.md) | Sweep the networking literature across venues, prove placements via dblp/ACM DL, separate main-track from CCR editorials, and handle blind-safe self-citation. |
| [`sigcomm-experiments`](skills/sigcomm-experiments/SKILL.md) | Climb the evidence ladder (micro → testbed/trace → deployment), pick baselines that fight back, and report tails, variance, and break points. |
| [`sigcomm-reproducibility`](skills/sigcomm-reproducibility/SKILL.md) | Keep topology, traffic, configuration, and run ledgers; characterize variance; decide early what data and code can legally ship. |
| [`sigcomm-supplementary`](skills/sigcomm-supplementary/SKILL.md) | Place content across body, references, and shepherd-approved appendices, and keep the main paper self-contained under the 12-page cap. |
| [`sigcomm-artifact-evaluation`](skills/sigcomm-artifact-evaluation/SKILL.md) | Package for the AEC: ACM badge selection as claim calibration, downscaled topologies, trace substitutes, and a fast smoke path. |
| [`sigcomm-submission`](skills/sigcomm-submission/SKILL.md) | Final audit: right HotCRP registration, AoE clock, 12-page pre-reference check, double-blind sweep, and track choice. |
| [`sigcomm-review-process`](skills/sigcomm-review-process/SKILL.md) | Read the outcome space (accept / one-shot revision / early or formal reject) and the shepherd and reviewer-continuity rules that shape strategy. |
| [`sigcomm-author-response`](skills/sigcomm-author-response/SKILL.md) | Execute the rebuttal and, separately, the one-shot revision as a shepherd-managed contract: issue triage, change memo, marked diff. |
| [`sigcomm-camera-ready`](skills/sigcomm-camera-ready/SKILL.md) | Deliver the TAPS final paper in 12 pages, clear shepherd sign-off, de-anonymize, and release the public artifact by the badge deadline. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eleven official sources with URLs and access dates, the verified-fact list, the access-method note, and the explicit 待核实 register. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes (clock, format, blindness, track, status). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Six venue-verified SIGCOMM papers (2001-2015) across six system classes, each with a self-check, plus the OpenFlow-CCR / Hedera-NSDI / RED-journal / BBR-CACM misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional flowlet-steering system's abstract and introduction rebuilt into the SIGCOMM measured-evidence arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit, with the SIGCOMM-specific checks (topology, traces, tail measurement) the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./SIGCOMM-Skills
claude plugin install sigcomm-skills
```

Or use the files directly: each `skills/sigcomm-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to trigger it. Typical
invocations:

- "Is this congestion-control result SIGCOMM or NSDI material?" → `sigcomm-topic-selection`
- "We have one deadline in February — build the backward plan" → `sigcomm-workflow`
- "We got a one-shot revision with a shepherd — build the plan" → `sigcomm-author-response`
- "Audit the PDF before the abstract registration closes" → `sigcomm-submission`

## Pack structure

```text
SIGCOMM-Skills/
├── .claude-plugin/              # plugin.json + marketplace.json (12 skills declared)
├── README.md                    # this file
├── README.zh-CN.md              # 中文说明
├── LICENSE                      # MIT
├── assets/cover.svg             # pack cover
├── skills/
│   └── sigcomm-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md                # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md           # adapter to the shared repro kit
```

## Suggested use

1. **Before committing the year** — `sigcomm-topic-selection` for scope and track,
   `sigcomm-workflow` for the single-deadline math; the exemplars library shows what
   cleared the bar in accepted form.
2. **While building** — `sigcomm-experiments` and `sigcomm-reproducibility` next to the
   testbed; trace provenance and tail-variance characterization cannot be added
   retroactively.
3. **While writing** — `sigcomm-writing-style` against the worked example,
   `sigcomm-supplementary` for the body/appendix split, `sigcomm-related-work` with the
   networking canon open and venues verified.
4. **Deadline week** — `sigcomm-submission` end to end on the exact upload candidate.
5. **After the letter** — `sigcomm-review-process` to classify the outcome, then
   `sigcomm-author-response` (rebuttal or revision), or `sigcomm-artifact-evaluation` +
   `sigcomm-camera-ready` (accept).

## 2026 anchor facts (dated snapshot, not standing rules)

- **SIGCOMM 2026** is the **40th** edition: **August 17-21, 2026, Colorado Convention
  Center, Denver, CO, USA**.
- One main-track deadline: abstracts **January 30, 2026**, full papers **February 6, 2026**
  (AoE). Camera-ready **July 3, 2026, 23:59 UTC** via ACM TAPS. As of 2026-07-09 the
  deadline has passed, decisions have issued, and the live phase is camera-ready
  finalization, shepherd sign-off, artifact evaluation, and August presentation — with
  forward planning already open for the next edition.
- Tracks: research and experience. Format: 12 single-spaced pre-reference pages including
  figures and tables, references and optional appendices beyond, double-blind, ACM
  `acmart.cls`.
- Review pipeline: early reject, rebuttal, and a shepherd-run one-shot revision
  (accept/reject only); accepted papers are shepherded through camera-ready.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified cycle facts** — dates, caps, and rules traced to a numbered source in the
   source map (e.g., the February 6 deadline, the 12-page pre-reference rule, the
   one-shot-revision mechanics).
2. **Reported facts** — carried only by secondary renderings and labeled as such (e.g.,
   Test-of-Time selections named via award pages and author institutions).
3. **待核实 items** — explicitly marked and phrased as open (e.g., the 2026 chairs, the
   exact notification date, the full 2026 artifact-badge set).

A statement of class 2 or 3 presented as class 1 anywhere in the skills is a bug; fix it
against the live pages.

## Maintenance notes

- Every date above is a **2026 snapshot**. SIGCOMM reissues rules per edition — reopen the
  current CFP and the HotCRP deadline page before deadline-sensitive advice.
- The **single-deadline** model is the defining constraint; do not import two-deadline or
  rolling-deadline reasoning from NSDI or MobiCom.
- Chairs rotate per edition and the 2026 roster was not retrievable — check the organization
  page before naming anyone.
- New exemplars must pass the venue-verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md); the networking canon's
  most famous papers are the most frequently misfiled, and CCR editorial notes are not
  main-track papers.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

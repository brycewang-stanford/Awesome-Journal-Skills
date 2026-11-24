# SIGCOMM Skills

Twelve agent skills for papers targeting **ACM SIGCOMM — the flagship conference of the
ACM Special Interest Group on Data Communication**, the top-tier annual venue for the
design, measurement, and analysis of computer networks and communication systems. The
pack is shaped around the way a SIGCOMM campaign actually runs, which departs from its
networking siblings in a way authors coming from USENIX or SIGMOBILE venues consistently
underestimate: **one main-track deadline per year** feeding **one** August conference, a
review model that in **SIGCOMM 2027** became **collaborative reviewing with one consensus
review and no rebuttal or one-shot revision**, a third outcome (**acceptance into CCR**),
**shepherding of accepted papers** through camera-ready, ACM
double-column formatting via **TAPS**, and an evidence bar written in the language of
**real traffic, real topology, tail latency, and reproducible "runnable" artifacts**.

Official basis **re-verified on 2026-11-24** by direct fetch: the ACM SIGCOMM 2027 home,
Call-for-Papers, submission-instructions, organizing-committee and camera-ready pages on
`conferences.sigcomm.org`; the SIGCOMM 2025 Call for Artifacts (the latest published); and the
`sigcomm.org` Test-of-Time and Best-Paper award pages. The original 2026-07-09 pass (SIGCOMM
2026 pages, the `sigcomm26.hotcrp.com` clock, dblp / ACM DL exemplar checks) was read through
search-engine renderings because those hosts then returned **HTTP 403**. The full trail —
including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes SIGCOMM unlike its siblings

Verified for the 2027 edition (re-verified 2026-11-24); these mechanics drive most of the
advice in the skills and most of the missteps by authors arriving from a two-deadline venue:

- **One deadline, one conference, one shot per year.** SIGCOMM 2027 (the **41st** edition,
  August 8-12, 2027, Queen Sirikit National Convention Center, Bangkok, Thailand) takes papers
  by **February 2, 2027** — a hard deadline, no extensions. There is no fall gate to fall back
  on — a rejected paper waits a full year, which raises the stakes of the single submission far
  above a spring/fall venue.
- **Two lanes on one deadline.** Submissions choose a **research** track or an **experience**
  track; in 2027 the experience track is judged on the **depth of the lessons learned** from
  deployment or operation, not on deployment size, and its titles begin "Experience:".
- **No reply window in 2027.** Reviewers discuss each paper together from the start and return
  **one short consensus review**; **there are no rebuttals or one-shot revisions** (SIGCOMM
  2026 had an early-reject cut, a rebuttal and a shepherd-run one-shot revision). The paper
  must pre-empt every objection itself, and must pass a new **general-accessibility** test.
- **Three outcomes.** Accepted into the conference, **accepted into CCR** as a research article
  (authors may decline), or rejected. Conference papers owe a **video** and an in-person
  presentation at a small-scale discussion session; a subset also gets a plenary talk.
- **Shepherding does not stop at acceptance.** Every accepted conference paper gets a shepherd,
  who confirms reviewer feedback is addressed and **must approve that any appendix is
  necessary**, signing off the final version in HotCRP.
- **12 single-spaced pages that count figures.** The body — everything before references — is
  capped at **12 single-spaced pages including figures and tables**, with references and
  optional appendices beyond the cap; pre-reference content over 12 pages **is not reviewed**,
  reviewers need not read appendices, and the abstract is limited to **200 words**.
- **Double-blind on HotCRP, ACM templates throughout.** Submissions are anonymous on
  `sigcomm27.hotcrp.com` (not yet open on 2026-11-24); the form takes ORCIDs, an ethics
  description and a named reciprocal reviewer; at most eight submissions per author; both
  submission and final papers use ACM `acmart.cls` (or the ACM Word template).
- **TAPS camera-ready.** Final papers upload **PDF plus source** to HotCRP and are processed
  by the **ACM Publishing System (TAPS)** for the ACM Digital Library and Computer
  Communication Review.
- **A reproducibility culture, not just a badge.** SIGCOMM helped pioneer artifact evaluation
  in networking; accepted papers may earn **ACM badges** (the latest published call, SIGCOMM
  2025, offered Artifacts Available and Artifacts Evaluated - Functional) through a separate
  committee, and the field's "runnable papers" heritage
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
| [`sigcomm-review-process`](skills/sigcomm-review-process/SKILL.md) | Read the 2027 collaborative-review model and outcome space (conference accept / CCR accept / reject), and how it differs from the 2026 early-reject/rebuttal/one-shot pipeline. |
| [`sigcomm-author-response`](skills/sigcomm-author-response/SKILL.md) | With no rebuttal in 2027: pre-empt objections in the paper, decide a CCR offer, run the shepherd revision; keeps the 2026 rebuttal/one-shot playbook. |
| [`sigcomm-camera-ready`](skills/sigcomm-camera-ready/SKILL.md) | Deliver the TAPS final paper in 12 pages, clear shepherd sign-off, de-anonymize, and release the public artifact by the badge deadline. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eleven current official sources plus five SIGCOMM 2026 history rows, with URLs and access dates, the verified-fact list, the access-method note, and the explicit 待核实 register. |
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
- "We were offered CCR instead of the conference — take it or resubmit?" → `sigcomm-author-response`
- "Audit the PDF before the February 2 deadline" → `sigcomm-submission`

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
   `sigcomm-author-response` (CCR decision or shepherd revision), or `sigcomm-artifact-evaluation` +
   `sigcomm-camera-ready` (accept).

## 2027 anchor facts (dated snapshot, not standing rules)

- **SIGCOMM 2027** is the **41st** edition: **August 8-12, 2027, Queen Sirikit National
  Convention Center, Bangkok, Thailand**. CFP posted October 19, 2026.
- One main-track deadline: papers **February 2, 2027** (hard, no extensions; HotCRP clock and
  time zone 待核实 until `sigcomm27.hotcrp.com` opens). Official publication date **July 18th,
  2027**. The 2027 camera-ready deadline is not yet published.
- Tracks: research and experience. Format: 12 single-spaced pre-reference pages including
  figures and tables, references and optional appendices beyond, 200-word abstract,
  double-blind, ACM `acmart.cls`, PDF under 15 MB.
- Review: collaborative reviewing, one consensus review, **no rebuttal or one-shot revision**;
  outcomes are conference accept (shepherded, video + in-person presentation), CCR accept, or
  reject.
- Chairs: General Chairs Kanchana Kanchanasut and Jim Kurose; Program Chairs Ranjita Bhagwan,
  Nate Foster, Aurojit Panda and Scott Shenker.
- History: SIGCOMM 2026 (40th, Denver, August 17-21, 2026) took abstracts January 30 and papers
  February 6, 2026 (AoE) and used an early-reject / rebuttal / one-shot-revision pipeline.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified cycle facts** — dates, caps, and rules traced to a numbered source in the
   source map (e.g., the February 2, 2027 deadline, the 12-page pre-reference rule, the
   no-rebuttal review model).
2. **Reported facts** — carried only by secondary renderings and labeled as such (e.g.,
   Test-of-Time selections named via award pages and author institutions).
3. **待核实 items** — explicitly marked and phrased as open (e.g., the 2027 HotCRP clock, the
   2027 notification and camera-ready dates, the 2027 artifact-badge set).

A statement of class 2 or 3 presented as class 1 anywhere in the skills is a bug; fix it
against the live pages.

## Maintenance notes

- Every date above is a **2027 snapshot**. SIGCOMM reissues rules per edition — reopen the
  current CFP and the HotCRP deadline page before deadline-sensitive advice.
- The **single-deadline** model is the defining constraint; do not import two-deadline or
  rolling-deadline reasoning from NSDI or MobiCom.
- Chairs rotate per edition — check the organization page before naming anyone (the 2027
  roster above was read on 2026-11-24).
- New exemplars must pass the venue-verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md); the networking canon's
  most famous papers are the most frequently misfiled, and CCR editorial notes are not
  main-track papers.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

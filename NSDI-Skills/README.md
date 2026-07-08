# NSDI Skills

Twelve agent skills for papers targeting **NSDI — the USENIX Symposium on Networked
Systems Design and Implementation**, the community's home for networked and
distributed systems built, deployed, and measured under realistic traffic. The pack
follows the full shape of an NSDI campaign, which differs from every single-deadline
sibling: **two submission gates per edition** (spring and fall), a **one-shot
revise-and-resubmit** channel that spans those gates, a resubmission ban that makes
speculative submissions expensive, three tracks with different evidence contracts,
artifact badges, and a Community Award tied to public code and data.

Official basis checked on **2026-07-08**: the NSDI '27 conference page and Call for
Papers, the NSDI '26 conference page, CFP, multiple-deadlines process page, and Call
for Artifacts, the per-deadline HotCRP sites, the USENIX Test of Time awards page,
and dblp's NSDI stream for exemplar verification. Direct fetches of `usenix.org` and
`dblp.org` returned HTTP 403 in the verification environment, so every source was
read through search-engine renderings of the exact official URLs and cross-checked
across independent renderings; the full trail — including everything still marked
待核实 — is in [`resources/official-source-map.md`](resources/official-source-map.md).

## The mechanics that make NSDI unlike its siblings

Verified for the 2026-27 cycle; these drive most of the advice in the skills and most
of the mistakes made by authors arriving from single-deadline venues:

- **Two deadlines feed one symposium.** NSDI '27 (May 11-13, 2027, Providence, RI)
  accepted papers at a spring gate (papers April 23, 2026) and accepts them at a fall
  gate (abstracts September 10, papers September 17, 2026, 11:59 pm US EDT). Each
  gate is its own HotCRP site, its own review cohort, its own accepted-papers list.
- **The one-shot revision is the author-response mechanism.** No rebuttal phase
  appears in the rendered CFP. Instead, borderline papers receive a reviewer-written
  list of required issues and one chance to resubmit at a later deadline — same
  reviewers where possible, mandatory change-highlighted diff and change memo, and
  terminal rejection if the list is dodged.
- **Rejection carries a ban.** A paper rejected without a revision option cannot
  enter the next deadline — spring rejects skip the same edition's fall gate. "Submit
  and see" spends two deadlines, not one.
- **Three tracks, three contracts:** research (design + implementation + practical
  evaluation), operational systems (deployed experience; anonymization relaxed for
  system and company names), and a frontiers track for bold ideas without complete
  evaluations.
- **12 pages including footnotes, figures, and tables** — for submissions *and* final
  papers — with references and appendices allowed beyond the cap.
- **Double-blind with a track-shaped exception**, an eight-submissions-per-author
  cap across deadlines, and a fixed citation sentence for concurrent submissions.
- **USENIX open access**: every NSDI paper ever published is a free PDF, which raises
  the bar for related-work coverage and removes excuses for venue misattribution.
- **Artifacts and openness are institutionalized**: post-acceptance badge evaluation
  (Artifacts Available confirmed by name for '26) and a **Community Award** for the
  best paper with public code/data by the final-papers deadline.

## Skills

| Skill | What it does |
| --- | --- |
| [`nsdi-topic-selection`](skills/nsdi-topic-selection/SKILL.md) | Test the networking-stack contribution against the CFP's explicit out-of-scope list, pick the honest track, and route misfits to SIGCOMM, OSDI/SOSP, FAST, or SIGMETRICS. |
| [`nsdi-workflow`](skills/nsdi-workflow/SKILL.md) | Plan across the spring/fall gates: backward schedules, ban arithmetic, revision windows, and what to do during NSDI's long review silences. |
| [`nsdi-writing-style`](skills/nsdi-writing-style/SKILL.md) | Build the operational-pain → design-principle → evidence arc inside 12 figure-inclusive pages, with tail percentiles replacing superlatives. |
| [`nsdi-related-work`](skills/nsdi-related-work/SKILL.md) | Sweep six literature lanes including the current edition's spring cohort, prove venues via dblp/USENIX, and handle blind-safe self-citation. |
| [`nsdi-experiments`](skills/nsdi-experiments/SKILL.md) | Climb the evidence ladder (micro → trace/testbed → deployment), pick baselines that fight back, and report tails, variance, and break points. |
| [`nsdi-reproducibility`](skills/nsdi-reproducibility/SKILL.md) | Keep topology, traffic, configuration, and run ledgers; characterize variance; decide early what data can legally ship. |
| [`nsdi-supplementary`](skills/nsdi-supplementary/SKILL.md) | Place content across body, references, permitted appendices, and HotCRP auxiliary material — including the mandatory revision packet. |
| [`nsdi-artifact-evaluation`](skills/nsdi-artifact-evaluation/SKILL.md) | Package for the AEC: badge selection as claim calibration, downscaled topologies, trace substitutes, and the fifteen-minute smoke path. |
| [`nsdi-submission`](skills/nsdi-submission/SKILL.md) | Final audit: right HotCRP site, US-Eastern cutoffs, 12-page check, track-dependent blinding, author cap, and the resubmission-ban check. |
| [`nsdi-review-process`](skills/nsdi-review-process/SKILL.md) | Read the three-way outcome space (accept / one-shot revision / reject-with-ban) and the reviewer-continuity rules that shape strategy. |
| [`nsdi-author-response`](skills/nsdi-author-response/SKILL.md) | Execute the one-shot revision as a contract: issue triage, change memo, highlighted diff, and pre-emptive response inside the original PDF. |
| [`nsdi-camera-ready`](skills/nsdi-camera-ready/SKILL.md) | Deliver the open-access final paper in the same 12 pages, hit the Community-Award release clock, and designate the presenter for May. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eleven official sources with URLs and access dates, the verified-fact list, the access-method note, and the explicit 待核实 register. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes (clock, budget, blindness, status, revision). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five venue-verified NSDI papers (2007-2020) across five system classes, each with a self-check, plus the Raft/B4/Chord/Spanner/Tor misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional RPC-retry system's abstract and introduction rebuilt into the NSDI operational-evidence arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit, with the NSDI-specific checks (topology, traces, timing variance) the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./NSDI-Skills
claude plugin install nsdi-skills
```

Or use the files directly: each `skills/nsdi-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to trigger it. Typical
invocations:

- "Is this congestion-control system NSDI or SIGCOMM material?" → `nsdi-topic-selection`
- "Which deadline should we target, and what does a reject cost us?" → `nsdi-workflow`
- "We got a one-shot revision — build the plan" → `nsdi-author-response`
- "Audit the PDF before the fall upload" → `nsdi-submission`

## Pack structure

```text
NSDI-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── nsdi-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared repro kit
```

## Suggested use

1. **Before committing a deadline** — `nsdi-topic-selection` for scope and track,
   `nsdi-workflow` for the gate math; the exemplars library shows what cleared the
   bar in accepted form.
2. **While building** — `nsdi-experiments` and `nsdi-reproducibility` next to the
   testbed; trace provenance and variance characterization cannot be added
   retroactively.
3. **While writing** — `nsdi-writing-style` against the worked example,
   `nsdi-supplementary` for the body/appendix split, `nsdi-related-work` with the
   current edition's cohort lists open.
4. **Deadline week** — `nsdi-submission` end to end on the exact upload candidate.
5. **After the letter** — `nsdi-review-process` to classify the outcome, then
   `nsdi-author-response` (revision), or `nsdi-artifact-evaluation` +
   `nsdi-camera-ready` (accept).

## 2026-27 anchor facts (dated snapshot, not standing rules)

- **NSDI '27** is the **24th** edition: **May 11-13, 2027, Omni Providence Hotel,
  Providence, RI, USA**.
- '27 spring gate: abstracts April 16 / papers April 23, 2026; notification
  July 23, 2026. '27 fall gate: abstracts September 10 / papers September 17, 2026;
  notification December 8, 2026. All 11:59 pm **US EDT** (where '26 used PDT — the
  convention itself moves).
- Tracks: research, operational systems, frontiers. Cap: eight submissions per
  author across deadlines. Format: 12 pages + references + appendices, double-blind.
- **NSDI '26** (23rd) ran May 4-6, 2026, Renton, WA; its artifact evaluation offered
  three badges with artifacts due July 31, 2025.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified cycle facts** — dates, caps, and rules traced to a numbered source in
   the source map (e.g., the April 23 spring deadline, the 12-page rule, the
   one-shot-revision requirements).
2. **Reported facts** — carried only by secondary renderings and labeled as such
   (e.g., Test of Time selections reported via author institutions, the Spark Best
   Paper via the Apache project).
3. **待核实 items** — explicitly marked and phrased as questions (e.g., the '27
   co-chairs, camera-ready dates, the full '26 badge names, any rebuttal phase).

A statement of class 2 or 3 presented as class 1 anywhere in the skills is a bug;
fix it against the live pages.

## Maintenance notes

- Every date above is a **2026-27 snapshot**. NSDI reissues rules per edition *and
  per deadline* — reopen the current CFP and the specific HotCRP `/deadlines` page
  before deadline-sensitive advice.
- The **frontiers track appears in the rendered '27 CFP**; do not assume it exists
  (or keeps its terms) in other editions.
- The deadline **time zone changed between '26 (PDT) and '27 (EDT)**; never reuse a
  previous cycle's time conversion.
- Chairs rotate per edition and the '27 co-chairs were not retrievable — check the
  organizers page before naming anyone.
- New exemplars must pass the venue-verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md); the systems
  canon's most famous papers are the most frequently misfiled.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

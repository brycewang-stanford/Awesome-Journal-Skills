# MobiCom Skills

Twelve agent skills for papers aimed at **MobiCom — the ACM International Conference
on Mobile Computing and Networking**, the ACM SIGMOBILE flagship where mobile and
wireless-networking systems are designed, built, and measured over real radios. The
pack is shaped around the way a MobiCom campaign actually runs, which departs from the
single-deadline conference and from its USENIX-style siblings alike: a **rolling
two-deadlines-per-year calendar** in which each deadline feeds the *next* edition, a
**two-round review with an early-reject cut and a rebuttal window**, a **retained
one-shot revision** path on top of that, double-column ACM formatting, and an evidence
bar written in the language of the physical layer — over-the-air measurement, channel
and mobility conditions, and energy on real hardware.

Official basis checked on **2026-07-09**: the MobiCom 2026 conference and Call-for-Papers
pages on `sigmobile.org`, the `mobicom26.hotcrp.com` submission and deadlines pages, the
SIGMOBILE MobiCom landing and artifact-evaluation pages, the SIGMOBILE Test-of-Time award
pages, a community deadline aggregator for the forthcoming 2027-cycle dates, and dblp /
the ACM Digital Library for exemplar verification. Direct fetches of `sigmobile.org`,
`hotcrp.com`, and `dblp.org` returned **HTTP 403** in the verification environment, so
every fact below was read through search-engine renderings of the exact official URLs and
cross-checked across independent renderings; the full trail — including everything still
marked 待核实 — is in [`resources/official-source-map.md`](resources/official-source-map.md).

## What makes MobiCom unlike its siblings

Verified for the 2026 edition and the opening of the 2027 cycle; these mechanics drive
most of the advice in the skills and most of the missteps by authors arriving from a
single-deadline venue or from a USENIX systems conference:

- **Two rolling deadlines per year, each feeding the next edition.** MobiCom has run a
  multi-deadline model since its 25th edition (2019). The winter/spring round and the
  summer/fall round each hold their own PC meeting; a paper submitted to the summer 2026
  round is competing for **MobiCom 2027**, not the 2026 program already set.
- **Two review rounds *plus* a rebuttal, not a single verdict.** Within one deadline,
  papers that do not advance past the first round get an early notification with reviews;
  survivors reach a second round whose reviews are released before a fixed **rebuttal
  window**. This is a genuinely different response surface from a USENIX venue that offers
  no rebuttal at all.
- **The one-shot revision is retained on top of the rebuttal.** Beyond accept/reject,
  MobiCom keeps a major-revision channel intended to raise the timeliness and quality of
  results; a revised paper returns to reviewers against the issue list it was given.
- **Double-column, 12 pages that count figures.** The body is capped at 12 single-spaced
  numbered pages *including figures and tables*, in the ACM double-column geometry, with
  references (and optional appendices after them) outside the cap.
- **Double-blind on HotCRP.** Submissions are anonymous on the per-edition
  `mobicom<yy>.hotcrp.com` site; the abstract/registration step precedes the paper upload.
- **ACM artifact badges, not a USENIX scheme.** Accepted papers may earn the three ACM
  badges — *Artifacts Available*, *Artifacts Evaluated — Functional*, and *Results
  Reproduced* — through a separate artifact-evaluation committee.
- **Evidence is measured over the air.** MobiCom's reviewer culture expects real-device
  testbeds, RF/channel measurement methodology, mobility realism, and energy accounting;
  a simulation-only or single-run result reads as under-evaluated here in a way it might
  not at a theory or ML venue.
- **The SIGMOBILE Test-of-Time award** anchors the canon and is presented at MobiCom —
  useful for exemplars, and a reminder that the field's most-cited results are also its
  most-misfiled across INFOCOM, SIGCOMM, and NSDI.

## Skills

| Skill | What it does |
| --- | --- |
| [`mobicom-topic-selection`](skills/mobicom-topic-selection/SKILL.md) | Test whether the contribution is a mobile/wireless-networking mechanism MobiCom rewards, and route platform, sensing, broad-networking, or security misfits to MobiSys, SenSys, SIGCOMM/NSDI, or WiSec. |
| [`mobicom-workflow`](skills/mobicom-workflow/SKILL.md) | Plan against the rolling summer/winter deadline pair: which edition a round feeds, backward schedules that leave time for over-the-air runs, and where the early-reject cut and revision path change the plan. |
| [`mobicom-writing-style`](skills/mobicom-writing-style/SKILL.md) | Build the wireless-pain → mechanism → measured-evidence arc inside the double-column 12 pages, with percentiles and confidence intervals instead of superlatives. |
| [`mobicom-related-work`](skills/mobicom-related-work/SKILL.md) | Sweep the SIGMOBILE and networking literature lanes, prove venues via dblp/ACM DL against the INFOCOM/SIGCOMM/NSDI misattribution traps, and self-cite blind-safely. |
| [`mobicom-experiments`](skills/mobicom-experiments/SKILL.md) | Design the real-testbed evaluation: RF and channel measurement methodology, mobility conditions, energy profiling, baselines on tuned hardware, and honest ground-truth. |
| [`mobicom-reproducibility`](skills/mobicom-reproducibility/SKILL.md) | Keep radio, hardware, channel, and mobility provenance so results survive a different testbed, and decide early what traces and firmware can legally ship. |
| [`mobicom-supplementary`](skills/mobicom-supplementary/SKILL.md) | Place content across the 12-page body, references, optional appendices, and HotCRP fields — and keep the rebuttal and revision packets out of the page cap. |
| [`mobicom-artifact-evaluation`](skills/mobicom-artifact-evaluation/SKILL.md) | Package for the AEC: which of the three ACM badges to claim, a hardware-optional path for evaluators without radios, and the smoke run that proves functionality. |
| [`mobicom-submission`](skills/mobicom-submission/SKILL.md) | Final audit: right HotCRP site and round, AoE cutoff, 12-page double-column check, double-blind sweep including radio-trace giveaways, and the abstract-registration prerequisite. |
| [`mobicom-review-process`](skills/mobicom-review-process/SKILL.md) | Read the outcome space of the two-round process — early reject, rebuttal, accept, and one-shot revision — and the reviewer-continuity that shapes revision strategy. |
| [`mobicom-author-response`](skills/mobicom-author-response/SKILL.md) | Execute the rebuttal under its length limit and, separately, the one-shot revision as a contract against the reviewers' required-changes list. |
| [`mobicom-camera-ready`](skills/mobicom-camera-ready/SKILL.md) | Deliver the de-anonymized double-column final paper, complete ACM rights and metadata, coordinate artifact badges, and plan the in-person talk. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | The official sources with URLs and access dates, the verified-fact list, the access-method note (sigmobile.org / hotcrp.com / dblp.org all 403'd direct fetches), and the explicit 待核实 register. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes (clock, budget, blindness, status, revision/rebuttal). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five venue-verified MobiCom papers (2000-2013) across five sub-areas, each with a self-check, plus the RADAR/XORs/WiSee-demo misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional backscatter-link paper's abstract and introduction rebuilt into the MobiCom measured-evidence arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit, with the MobiCom-specific checks (radio provenance, channel conditions, energy) the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./MobiCom-Skills
claude plugin install mobicom-skills
```

Or use the files directly: each `skills/mobicom-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to trigger it. Typical
invocations:

- "Is this a MobiCom paper or a MobiSys paper?" → `mobicom-topic-selection`
- "Which deadline are we writing for, and which edition does it feed?" → `mobicom-workflow`
- "Reviews are out — draft the rebuttal" or "we got a major revision" → `mobicom-author-response`
- "Audit the PDF before the HotCRP upload" → `mobicom-submission`

## Pack structure

```text
MobiCom-Skills/
├── .claude-plugin/               # plugin.json + marketplace.json (12 skills declared)
├── README.md                     # this file
├── README.zh-CN.md               # 中文说明
├── LICENSE                       # MIT
├── assets/cover.svg              # pack cover
├── skills/
│   └── mobicom-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md                 # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md            # adapter to the shared repro kit
```

## Suggested use

1. **Before committing to a round** — `mobicom-topic-selection` for scope and sibling
   routing, `mobicom-workflow` for which edition the round feeds and whether the radio
   experiments fit the calendar; the exemplars library shows what cleared the bar.
2. **While building** — `mobicom-experiments` and `mobicom-reproducibility` at the
   testbed; channel logs, mobility conditions, and energy traces cannot be reconstructed
   after the fact.
3. **While writing** — `mobicom-writing-style` against the worked example,
   `mobicom-supplementary` for the body/appendix split, `mobicom-related-work` with the
   current cohort and the venue-verification recipe open.
4. **Deadline week** — `mobicom-submission` end to end on the exact upload candidate.
5. **After the notification** — `mobicom-review-process` to classify the outcome, then
   `mobicom-author-response` (rebuttal or revision), or `mobicom-artifact-evaluation` +
   `mobicom-camera-ready` (accept).

## 2026-27 anchor facts (dated snapshot, not standing rules)

- **MobiCom 2026** is the **32nd** edition: **October 26-30, 2026, Austin, TX, USA**;
  its two rounds are decided and the program is set.
- MobiCom 2026's **winter/spring round** registered abstracts by **March 7, 2026** and
  took papers by **March 14, 2026** (an 11:59 pm AoE cutoff shown as 7:59 am EDT), with
  final notification reported around **June 22, 2026**.
- The **next open gate** as of 2026-07-09 is the **MobiCom 2027 first round**, a
  summer/fall deadline reported around **September 3, 2026** with notification around
  **November 24, 2026** — dates from a community aggregator, marked 待核实 until the 2027
  CFP is posted.
- Format: **12 double-column pages including figures and tables**, references and
  optional appendices outside the cap; **double-blind** on HotCRP.
- Artifact evaluation offers the three **ACM badges**; the **SIGMOBILE Test-of-Time**
  award is presented at MobiCom.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified cycle facts** — dates, caps, and rules traced to a numbered source in the
   source map (e.g., the 12-page double-column rule, the two-round + rebuttal process,
   the March 14 2026 winter-round deadline).
2. **Reported facts** — carried only by secondary renderings and labeled as such (e.g.,
   the June 2026 winter-round notification and the September 2026 2027-round deadline,
   reported by a community aggregator; Best-Paper and Test-of-Time selections via author
   institutions and SIGMOBILE award pages).
3. **待核实 items** — explicitly marked and phrased as questions (e.g., the 2027 CFP's
   exact dates, the 2026 chairs, the rebuttal window length, and the current artifact
   deadlines).

A statement of class 2 or 3 presented as class 1 anywhere in the skills is a bug; fix it
against the live pages.

## Maintenance notes

- Every date above is a **2026-27 snapshot**. MobiCom reissues its rules per edition *and
  runs two deadlines per year* — reopen the current CFP and the specific HotCRP
  `/deadlines` page before deadline-sensitive advice.
- The deadline is an **AoE** cutoff even when the page prints a US-Eastern clock time;
  never reuse a previous cycle's local conversion.
- Which **edition a round feeds** shifts every cycle — confirm on the live CFP that the
  round you are targeting is the one you think it is.
- Chairs rotate per edition and the 2026 committee names were not retrievable — check the
  committee page before naming anyone.
- New exemplars must pass the venue-verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md); the wireless canon's
  most famous papers are the most frequently misfiled across INFOCOM/SIGCOMM/NSDI.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

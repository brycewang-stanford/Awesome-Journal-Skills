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

Official basis **re-verified on 2026-11-24** by direct fetch: the MobiCom 2027 home page,
Call for Papers, Call for Artifacts and committee pages on `sigmobile.org`, the
`mobicom27.hotcrp.com` deadline clock, the MobiCom 2026 home page and CFP (history), the
SIGMOBILE MobiCom landing page, and the SIGMOBILE Test-of-Time award page. The original
2026-07-09 pass (including dblp / the ACM Digital Library for exemplar verification) was read
through search-engine renderings because `sigmobile.org`, `hotcrp.com`, and `dblp.org` then
returned **HTTP 403**. The full trail — including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes MobiCom unlike its siblings

Verified for MobiCom 2027 (re-verified 2026-11-24); these mechanics drive
most of the advice in the skills and most of the missteps by authors arriving from a
single-deadline venue or from a USENIX systems conference:

- **Two rolling deadlines per year, each feeding the next edition.** MobiCom has run a
  multi-deadline model since its 25th edition (2019). Each round holds its own PC meeting;
  **MobiCom 2027** (33rd, **October 18-22, 2027, Athens, Greece**) took its summer round in
  August/September 2026 (papers September 2, 2026 AoE, decisions November 19, 2026) and lists
  its winter round as **"TBD"**.
- **Two review rounds *plus* a rebuttal, not a single verdict.** Within one deadline,
  papers that do not advance past the first round get an early notification with reviews;
  survivors reach a second round whose reviews are released before a fixed **rebuttal
  window** — optional, **500 words**, facts and answers only, no new experiments, data, or
  figures. This is a genuinely different response surface from a USENIX venue that offers
  no rebuttal at all.
- **The one-shot revision is retained on top of the rebuttal.** Beyond accept/reject,
  MobiCom keeps a major-revision channel (at most **three** required changes, resubmitted at
  the next deadline); a revised paper returns to reviewers against the issue list it was
  given. Accepts are **conditional** until 4-6 weeks of anonymous shepherding, and a plain
  reject cannot return to MobiCom for **11 months**.
- **Every submission brings a reviewer.** New in 2027: one senior author per paper reviews up
  to three submissions in the same round.
- **Double-column, 12 pages that count figures.** The body is capped at 12 single-spaced
  numbered pages *including figures and tables*, in the ACM double-column geometry, with
  references (and optional appendices after them, starting on a new page) outside the cap;
  no embedded hyperlinks, PDF under 15 MB, `acmart` `sigconf,10pt`.
- **Double-blind on HotCRP.** Submissions are anonymous on the per-edition
  `mobicom<yy>.hotcrp.com` site; the abstract/registration step (at least 100 words, no
  "TBD") precedes the paper upload.
- **ACM artifact badges, not a USENIX scheme.** Accepted and conditionally accepted papers
  may earn the three ACM badges — *Artifacts Available*, *Artifacts Evaluated — Functional*,
  and *Results Reproduced* — through a separate artifact-evaluation committee.
- **ACM open access.** Authors outside ACM Open institutions pay an APC unless waived
  (2027 subsidized: $500 ACM/SIG members, $750 non-members); every accepted paper ships a
  90-second teaser video and an in-person presenter.
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

## MobiCom 2027 anchor facts (dated snapshot, not standing rules)

- **MobiCom 2027** is the **33rd** edition: **October 18-22, 2027, Athens, Greece**. General
  Co-Chairs Dimitrios Koutsonikolas and Symeon Papavassiliou; TPC Co-Chairs Joerg Widmer and
  Nirupam Roy.
- **Summer round** (decided): abstracts **August 26, 2026**, papers **September 2, 2026**
  (23:59 AoE), early reject October 23, rebuttal November 3-6, acceptance November 19, 2026.
  **Winter round: TBD** on 2026-11-24 — the next open gate has no published date.
- Artifacts: summer round due January 17, 2027 (notification February 17, 2027); winter round
  due July 24, 2027 (notification August 24, 2027).
- Format: **12 double-column pages including figures and tables**, references and optional
  appendices outside the cap; **double-blind** on HotCRP; rebuttal at most 500 words.
- History: **MobiCom 2026** (32nd) met in Austin, TX, October 26-30, 2026; its winter round
  took abstracts March 6 and papers March 13, 2026 (AoE).

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified cycle facts** — dates, caps, and rules traced to a numbered source in the
   source map (e.g., the 12-page double-column rule, the two-round + 500-word rebuttal
   process, the September 2, 2026 summer-round deadline).
2. **Reported facts** — carried only by secondary renderings and labeled as such (e.g.,
   Best-Paper selections via author institutions).
3. **待核实 items** — explicitly marked and phrased as questions (e.g., the 2027 winter-round
   dates, the 2027 camera-ready deadline, registration fees).

A statement of class 2 or 3 presented as class 1 anywhere in the skills is a bug; fix it
against the live pages.

## Maintenance notes

- Every date above is a **MobiCom 2027 snapshot** (re-verified 2026-11-24). MobiCom reissues its rules per edition *and
  runs two deadlines per year* — reopen the current CFP and the specific HotCRP
  `/deadlines` page before deadline-sensitive advice.
- The deadline is an **AoE** cutoff even when the page prints a US-Eastern clock time;
  never reuse a previous cycle's local conversion.
- Which **edition a round feeds** shifts every cycle — confirm on the live CFP that the
  round you are targeting is the one you think it is.
- Chairs rotate per edition — check the committee page before naming anyone (the 2027 names
  above were read on 2026-11-24).
- New exemplars must pass the venue-verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md); the wireless canon's
  most famous papers are the most frequently misfiled across INFOCOM/SIGCOMM/NSDI.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

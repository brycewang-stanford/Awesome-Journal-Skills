# SenSys Skills

Twelve agent skills for papers aimed at **SenSys — the ACM/IEEE International Conference on
Embedded Artificial Intelligence and Sensing Systems**, the SIGMOBILE-affiliated flagship where
sensing systems are designed, built, and **measured on real hardware under real energy budgets**.
The pack is shaped around how a SenSys campaign actually runs, which now differs sharply from
every sibling venue: beginning with the 2026 edition, SenSys is a **merged conference** that
absorbed IPSN and IoTDI, so its scope spans low-power networked sensing, embedded systems, IoT,
and on-device / embedded AI; it runs a **two-deadline, self-contained review model** in which a
first-deadline reject may return at the second deadline **only with a substantive revision**;
and its evidence bar is written in the language of the platform — **energy per operation, duty
cycle, on-device latency and memory, sensor ground truth, and long-term deployment**.

Official basis checked on **2026-07-09**: the SenSys landing and Call-for-Papers pages on
`sensys.acm.org` (2026 and 2027), the per-edition HotCRP sites, the SenSys artifact-evaluation
and Test-of-Time pages, and dblp / the ACM Digital Library for exemplar verification. Direct
fetches of `sensys.acm.org`, `hotcrp.com`, and `dblp.org` returned **HTTP 403** in the
verification environment, so every fact below was read through search-engine renderings of the
exact official URLs and cross-checked; the full trail — including everything still marked
待核实 — is in [`resources/official-source-map.md`](resources/official-source-map.md).

## What makes SenSys unlike its siblings

Verified for the 2026 edition and the open 2027 cycle; these mechanics drive most of the advice
in the skills and most of the missteps by authors arriving from a single-deadline or an ML/theory
venue:

- **A merged venue with a wider mandate.** From 2026, SenSys, **IPSN**, and **IoTDI** merged into
  one flagship styled *Embedded Artificial Intelligence and Sensing Systems*. Topic routing that
  once split across three CFPs now lands in one place — but the reviewer culture is still
  systems-first: a contribution must be **built and measured**, not simulated or benchmarked alone.
- **Two deadlines per cycle, each a self-contained round.** SenSys runs two submission deadlines;
  each is fully reviewed on its own. A paper rejected at the first deadline may enter the second
  **only with a substantive revision and a "Response to Reviewers" statement** mapping each
  concern to a specific change — the resubmission is a contract, not a fresh coat of paint.
- **Energy is the headline metric.** SenSys reviewers expect power and energy reported with a
  **named measurement method** — source-meter, shunt, or power monitor, with sampling rate and
  wake/sleep boundaries — not the adjectives "lightweight" or "low-power."
- **Evidence is physical and deployed.** Real testbeds, energy-harvesting rigs, long-term
  deployments, and **honest sensor ground truth** are the currency. A single-run or
  simulation-only result reads as under-evaluated here in a way it might not at a theory venue.
- **On-device AI, measured on device.** Post-merger, embedded-AI papers are in-scope — but the
  claim is **quantized model size, RAM/flash peak, and on-hardware inference latency**, not
  offline accuracy on a workstation.
- **Double-blind on per-edition HotCRP.** Submissions are anonymous, including **blinded artifact
  links** (anonymized GitHub/GitLab/Zenodo, never a lab or company domain).
- **ACM artifact badges.** An Artifact Evaluation Committee awards three independent badges —
  *Artifacts Available*, *Artifacts Evaluated — Functional*, and *Results Reproduced* — printed on
  the paper and recorded in the ACM DL.
- **The SenSys Test-of-Time award** anchors the canon (B-MAC, FTSP, CTP, Protothreads) and is the
  cleanest source of venue-verified exemplars.

## Skills

| Skill | What it does |
| --- | --- |
| [`sensys-topic-selection`](skills/sensys-topic-selection/SKILL.md) | Test whether the contribution is a **built, measured sensing/embedded system** SenSys rewards after the merger, and route mobile-networking, pure-ML, or signal-processing misfits to MobiCom, MobiSys, an ML venue, or a DSP venue. |
| [`sensys-workflow`](skills/sensys-workflow/SKILL.md) | Plan against the two-deadline calendar and which edition a deadline feeds, backward-schedule so deployments and energy campaigns fit, and place the resubmission-with-revision path. |
| [`sensys-writing-style`](skills/sensys-writing-style/SKILL.md) | Build the sensing-pain → mechanism → measured-behavior arc inside the ACM double-column pages, with energy numbers and distributions instead of superlatives. |
| [`sensys-related-work`](skills/sensys-related-work/SKILL.md) | Sweep the sensing/embedded/IoT/on-device-AI lanes, prove venues via dblp/ACM DL against the MobiCom/NSDI/IPSN misattribution traps, and self-cite blind-safely. |
| [`sensys-experiments`](skills/sensys-experiments/SKILL.md) | Design the real-hardware evaluation: energy and low-power measurement, testbed and deployment realism, sensor ground truth, on-device latency/memory, and honest baselines. |
| [`sensys-reproducibility`](skills/sensys-reproducibility/SKILL.md) | Keep energy, hardware, firmware, and ground-truth provenance so results survive a different testbed, and decide early what traces and firmware can ship. |
| [`sensys-supplementary`](skills/sensys-supplementary/SKILL.md) | Place content across the page body, unlimited references and appendices, and HotCRP fields — and keep the response-to-reviewers packet out of the body. |
| [`sensys-artifact-evaluation`](skills/sensys-artifact-evaluation/SKILL.md) | Package for the AEC: which of the three ACM badges to claim, a hardware-optional path for evaluators without your testbed, and the smoke run that proves functionality. |
| [`sensys-submission`](skills/sensys-submission/SKILL.md) | Final audit: right HotCRP site and deadline, AoE cutoff, 12/6-page double-column check, double-blind sweep including hardware/deployment giveaways, and the resubmission contract if applicable. |
| [`sensys-review-process`](skills/sensys-review-process/SKILL.md) | Read the outcome space of the two-deadline model — reject, resubmit-with-revision at the next deadline, accept — and how reviewer expectations shape the revision. |
| [`sensys-author-response`](skills/sensys-author-response/SKILL.md) | Execute the response-to-reviewers as a contract against the required changes, and stage the additional experiments a systems revision usually demands. |
| [`sensys-camera-ready`](skills/sensys-camera-ready/SKILL.md) | Deliver the de-anonymized double-column final, complete ACM rights and metadata, coordinate artifact badges, and plan the in-person talk and demo. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Official sources with URLs and access dates, the verified-fact list, the access-method note (sensys.acm.org / hotcrp.com / dblp.org all 403'd), and the explicit 待核实 register. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes (round/clock, format, blindness, resubmission, artifact/deployment). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five venue-verified SenSys Test-of-Time papers across five contribution types, each with a self-check, plus the directed-diffusion / Glossy / TinyDB misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional batteryless-classifier paper's abstract and introduction rebuilt into the SenSys measured-behavior arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit, with the SenSys-specific checks (energy accounting, hardware provenance, sensor ground truth, on-device footprint) the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./SenSys-Skills
claude plugin install sensys-skills
```

Or use the files directly: each `skills/sensys-*/SKILL.md` is a standalone instruction file
whose frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a SenSys paper or a MobiCom paper?" → `sensys-topic-selection`
- "Which deadline are we targeting, and what does a resubmission require?" → `sensys-workflow`
- "Reviews are out — we can resubmit with revision" → `sensys-author-response`
- "Audit the PDF before the HotCRP upload" → `sensys-submission`

## Pack structure

```text
SenSys-Skills/
├── .claude-plugin/               # plugin.json + marketplace.json (12 skills declared)
├── README.md                     # this file
├── README.zh-CN.md               # 中文说明
├── LICENSE                       # MIT
├── assets/cover.svg              # pack cover
├── skills/
│   └── sensys-<topic>/SKILL.md   # 12 skills, one directory each
└── resources/
    ├── README.md                 # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md            # adapter to the shared repro kit
```

## Suggested use

1. **Before committing to a deadline** — `sensys-topic-selection` for scope and sibling routing
   after the merger, `sensys-workflow` for which deadline to target and whether the deployment
   fits the calendar; the exemplars library shows what cleared the bar.
2. **While building** — `sensys-experiments` and `sensys-reproducibility` at the testbed; energy
   traces, deployment logs, and ground truth cannot be reconstructed after the fact.
3. **While writing** — `sensys-writing-style` against the worked example, `sensys-supplementary`
   for the body/appendix split, `sensys-related-work` with the venue-verification recipe open.
4. **Deadline week** — `sensys-submission` end to end on the exact upload candidate.
5. **After the notification** — `sensys-review-process` to classify the outcome, then
   `sensys-author-response` (resubmit with revision) or `sensys-artifact-evaluation` +
   `sensys-camera-ready` (accept).

## 2026-27 anchor facts (dated snapshot, not standing rules)

- **SenSys 2026** — the first merged edition — was held **May 11-14, 2026 in Saint-Malo,
  France**; its program is complete and its proceedings are in the ACM DL.
- **SenSys 2027** is scheduled **May 10-13, 2027 in New York City, NY, USA**, submitting via
  `sensys27.hotcrp.com`; the **first-round deadline is June 6, AoE**. The second-round deadline
  and notification dates are 待核实 until confirmed live.
- Format (2027): **≤ 12 pages** full / **≤ 6 pages** short, **references and appendices
  unlimited** and outside the cap; **double-blind** on HotCRP with blinded artifact links.
- Artifact evaluation offers the three **ACM badges**; the **SenSys Test-of-Time** award anchors
  the canon.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified cycle facts** — traced to a numbered source in the source map (the merger, the
   two-deadline model, the 12/6-page format, the June 6 first-round deadline).
2. **Reported facts** — carried by a single rendering and labeled as such (e.g., specific 2026
   sub-deadlines and 2027 notification timing).
3. **待核实 items** — explicitly marked and phrased as questions (the second-round deadline, the
   2026/2027 chairs, the exact template geometry, the ethics/AI-use wording).

A statement of class 2 or 3 presented as class 1 anywhere in the skills is a bug; fix it against
the live pages.

## Maintenance notes

- Every date above is a **2026-27 snapshot**. SenSys reissues its rules per edition *and runs two
  deadlines per cycle* — reopen the current CFP and the specific HotCRP `/deadlines` page before
  deadline-sensitive advice.
- The deadline is an **AoE** cutoff; convert it per coauthor and never reuse a prior local
  conversion.
- The **merged scope** is new — re-check that your contribution still routes to SenSys rather
  than a venue whose community joined the merger under different expectations.
- Chairs rotate per edition and the 2026/2027 committee names were not cleanly retrievable —
  check the committee page before naming anyone.
- New exemplars must pass the venue-verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md); the sensing canon's most
  famous papers are the most frequently misfiled across MobiCom, NSDI, and IPSN.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

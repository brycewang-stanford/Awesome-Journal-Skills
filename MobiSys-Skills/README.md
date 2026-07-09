# MobiSys Skills

Twelve agent skills for papers aimed at **MobiSys — the ACM International Conference on
Mobile Systems, Applications, and Services**, the ACM SIGMOBILE venue where the *system*
that runs on a phone, wearable, vehicle, or embedded board is the contribution, not the
radio underneath it. Where its sibling MobiCom is about the wireless link, MobiSys is about
everything built on top of the device: mobile runtimes and operating systems, on-device
machine-learning inference, sensing pipelines and services, computation offload, and the
energy, latency, and memory budgets that decide whether any of it ships. The pack tracks the
way a MobiSys campaign actually runs — a **single annual deadline** in early December that
feeds the following June conference, a **two-round review with an early-reject cut and a
rebuttal**, double-blind HotCRP submission, a 12-page ACM double-column body, and an
evidence bar written in milliseconds, millijoules, and megabytes measured on real hardware.

Official basis checked on **2026-07-09**: the MobiSys 2026 Call for Papers, Artifact
Evaluation, Awards, and Organizing-Committee pages on `sigmobile.org`, the
`mobisys26.hotcrp.com` deadlines and program-committee pages, the official `@ACMMobiSys`
announcement of the CFP, the ACM Digital Library MobiSys proceedings, dblp's `conf/mobisys`
stream for exemplar verification, and the SIGMOBILE Test-of-Time award pages. Direct fetches
of `sigmobile.org` and `hotcrp.com` returned **HTTP 403** in the verification environment,
so every fact below was read through search-engine renderings of the exact official URLs and
cross-checked against the ACM DL, dblp, and the SIGMOBILE news feed; the full trail —
including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

**Cycle status (2026-07-09):** **MobiSys 2026** (the 24th edition, Cambridge, UK, June 21–25,
2026) *just concluded* — the paper deadline was **December 5, 2025**, notifications and
rebuttals ran across the spring, and the conference wrapped in late June, so this pack is
being written days after the event. The **next open gate** is **MobiSys 2027**: a community
aggregator and the venue's own cadence put its paper deadline near **December 5, 2026** with
notification near **March 2027**, but the 2027 CFP was not confirmed posted at check time, so
those dates are 待核实 until the official page appears. Everything about the 2027 host,
chairs, and exact clock is unverified.

## What makes MobiSys unlike its siblings

Verified 2026-cycle mechanics that drive the advice in these skills, and the missteps they
prevent for authors arriving from a wireless-networking venue or a two-deadline systems
conference:

- **The system on the device is the contribution.** The house test is a *mobile or embedded
  system, application, or service* whose behavior on real hardware is the result — an
  on-device inference engine, a mobile OS/runtime mechanism, a sensing service, an offload
  scheduler. A pure PHY/MAC or protocol result belongs at MobiCom; a sensor-network
  infrastructure result at SenSys; a data-center or distributed-systems result at NSDI.
- **One deadline a year, not a rolling pair.** MobiSys runs a single early-December paper
  deadline feeding the next June's conference. This is the opposite of MobiCom's and NSDI's
  two-deadlines-per-year model, and it changes the whole calculus: a miss costs a full year,
  so the workflow skill plans backward from one hard date.
- **Two review rounds, an early-reject cut, then a rebuttal.** Papers that do not advance
  past the first round receive an early rejection with reviews so the authors can re-plan;
  survivors reach a second round and then a **rebuttal window** limited to correcting factual
  errors and answering specific reviewer questions. New results are admissible only if they
  directly address feedback, or may be *promised* for camera-ready.
- **No standing one-shot revision channel.** Unlike MobiCom and NSDI, the rendered 2026 CFP
  describes accept/reject through the rebuttal, not a separate major-revision resubmission
  path; treat any revision mechanism as 待核实 for the cycle you target.
- **12 double-column pages that count figures.** The main body is capped at **12
  single-spaced numbered pages including figures and tables** in the ACM template;
  references and appendices sit outside the cap.
- **Double-blind on HotCRP.** Author identities have been hidden from reviewers since 2017;
  submission and rebuttal run on the per-edition `mobisys<yy>.hotcrp.com` site, with a paper
  registration step preceding the upload.
- **Three independent ACM artifact badges.** A single-blind Artifact Evaluation Committee
  awards *Artifacts Available*, *Artifacts Evaluated — Functional*, and *Results Reproduced*;
  authors may seek one, two, or all three, and passing badges are printed on the paper and in
  the ACM DL. Evaluators run the authors' workflow scripts on the evaluators' own machines —
  a strong, script-first artifact culture.
- **Evidence is measured on the device.** MobiSys reviewers expect real phones, wearables,
  or embedded boards; energy in joules, latency in milliseconds, memory footprint, thermal
  behavior, and — where the claim is a service — a deployment or user study. A simulation-only
  or single-run result reads as under-evaluated here.
- **The canon is mobile-systems, and it is easy to misfile.** MAUI, SoundSense, Odessa,
  MCDNN, and DeepMon are MobiSys papers; the SIGMOBILE Test-of-Time award (a cross-venue,
  ten-year-horizon prize) is a reminder that the field's most-cited results are also its most
  misattributed across MobiCom, SenSys, OSDI, and NSDI.

## Skills

| Skill | What it does |
| --- | --- |
| [`mobisys-topic-selection`](skills/mobisys-topic-selection/SKILL.md) | Test whether the contribution is a mobile/embedded *system* MobiSys rewards, and route wireless-mechanism, sensor-network, distributed-systems, ubicomp, or early-idea misfits to MobiCom, SenSys, NSDI/OSDI, IMWUT, or HotMobile. |
| [`mobisys-workflow`](skills/mobisys-workflow/SKILL.md) | Plan backward from the single December deadline through the two-round review, rebuttal, notification, artifact evaluation, camera-ready, and June presentation — with device-experiment lead time built in. |
| [`mobisys-writing-style`](skills/mobisys-writing-style/SKILL.md) | Build the mobile-pain → system-design → on-device-evidence arc inside 12 double-column pages, with latency/energy distributions instead of superlatives. |
| [`mobisys-related-work`](skills/mobisys-related-work/SKILL.md) | Cover the mobile-systems literature lanes — offload, on-device ML, mobile OS, sensing, energy — prove venues via dblp/ACM DL against the MobiCom/SenSys/OSDI traps, and self-cite blind-safely. |
| [`mobisys-experiments`](skills/mobisys-experiments/SKILL.md) | Design the real-device evaluation: energy instrumentation, latency and frame-rate tails, memory and thermal budgets, tuned system baselines, and deployment/user studies where a service is the claim. |
| [`mobisys-reproducibility`](skills/mobisys-reproducibility/SKILL.md) | Keep device, OS, SoC, model-version, and power-instrument provenance so results survive a different phone, and decide early what data and firmware can legally ship. |
| [`mobisys-supplementary`](skills/mobisys-supplementary/SKILL.md) | Place content across the 12-page body, references, optional appendices, demo video/media, and HotCRP fields — keeping the paper self-contained under reviewer discretion. |
| [`mobisys-artifact-evaluation`](skills/mobisys-artifact-evaluation/SKILL.md) | Package for the AEC: which of the three ACM badges to claim, a hardware-optional path for evaluators without the exact device, and the workflow script that proves functionality. |
| [`mobisys-submission`](skills/mobisys-submission/SKILL.md) | Final HotCRP audit: right site, UTC cutoff, 12-page double-column check, double-blind sweep including device/trace giveaways, registration prerequisite, and desk-reject triage. |
| [`mobisys-review-process`](skills/mobisys-review-process/SKILL.md) | Model the outcome space of the two-round process — early reject, rebuttal, accept — the reviewer pool, and how a systems-and-services reviewer scores an on-device claim. |
| [`mobisys-author-response`](skills/mobisys-author-response/SKILL.md) | Execute the rebuttal under its scope limit: correct factual errors first, answer specific questions, add only directly-responsive results, and promise camera-ready work honestly. |
| [`mobisys-camera-ready`](skills/mobisys-camera-ready/SKILL.md) | Deliver the de-anonymized double-column final paper, complete ACM rights and metadata, coordinate artifact badges, and plan the Cambridge in-person talk and demo. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | The official MobiSys 2026 sources with URLs and access dates, the verified-fact list, the access-method note (sigmobile.org / hotcrp.com both 403'd direct fetches), and the explicit 待核实 register. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces (site, HotCRP, ACM DL, dblp, SIGMOBILE) plus the author-side verification passes to run each cycle. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five metadata-verified MobiSys papers (2009–2017) across mobile-systems classes — offload/energy, on-phone sensing, perception offload, on-device DNN serving, mobile-GPU inference — each with a self-check, plus a do-not-misattribute guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional on-device inference paper's first page rebuilt to lead with the mobile-system contribution and on-device evidence, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit, plus the MobiSys-only checks (device provenance, energy boundary, hardware-optional smoke run) the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./MobiSys-Skills
claude plugin install mobisys-skills
```

Or use the files directly: each `skills/mobisys-*/SKILL.md` is a standalone instruction file
whose frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a MobiSys paper or a MobiCom / SenSys paper?" → `mobisys-topic-selection`
- "Plan the schedule back from the December deadline" → `mobisys-workflow`
- "Reviews are out — draft the rebuttal within its scope" → `mobisys-author-response`
- "Audit the PDF before the HotCRP upload" → `mobisys-submission`

## Pack structure

```text
MobiSys-Skills/
├── .claude-plugin/               # plugin.json + marketplace.json (12 skills declared)
├── README.md                     # this file
├── README.zh-CN.md               # 中文说明
├── LICENSE                       # MIT
├── assets/cover.svg              # pack cover
├── skills/
│   └── mobisys-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md                 # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md            # adapter to the shared repro kit
```

## Suggested use

1. **Before committing to the cycle** — `mobisys-topic-selection` for scope and sibling
   routing, `mobisys-workflow` to fit the device experiments inside one December deadline;
   the exemplars library shows what cleared the bar in accepted form.
2. **While building** — `mobisys-experiments` and `mobisys-reproducibility` next to the
   bench; energy traces, device/OS provenance, and thermal logs cannot be reconstructed after
   the fact.
3. **While writing** — `mobisys-writing-style` against the worked example,
   `mobisys-supplementary` for the body/appendix/demo split, `mobisys-related-work` with the
   venue-verification recipe open.
4. **Deadline week** — `mobisys-submission` end to end on the exact upload candidate.
5. **After the notification** — `mobisys-review-process` to classify the outcome, then
   `mobisys-author-response` (rebuttal), or `mobisys-artifact-evaluation` +
   `mobisys-camera-ready` (accept).

## 2026-27 anchor facts (dated snapshot, not standing rules)

- **MobiSys 2026** is the **24th** edition: **June 21–25, 2026, Cambridge, UK**, hosted with
  the University of Cambridge under ACM SIGMOBILE; General Chairs **Fahim Kawsar** and
  **Cecilia Mascolo** (program chairs 待核实).
- MobiSys 2026 timeline (AoE/UTC as posted): **paper registration November 28, 2025**,
  **paper submission December 5, 2025**; two-round review with early reject and a rebuttal;
  the conference just concluded in late June 2026.
- Format: **12 single-spaced double-column pages including figures and tables**; references
  and appendices outside the cap; **double-blind** on `mobisys26.hotcrp.com`.
- Artifact evaluation offers the three independent **ACM badges** (Available, Functional,
  Results Reproduced), single-blind, script-first; proceedings appear in the **ACM Digital
  Library**.
- **MobiSys 2027** (25th edition): paper deadline reported near **December 5, 2026**,
  notification near **March 2027** — 待核实 until the official CFP is posted; host and chairs
  unverified.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified 2026-cycle facts** — trace to a numbered source in the source map (e.g., the
   Cambridge dates, the December 5 2025 paper deadline, the 12-page double-column budget, the
   three ACM badge names, the two-round + rebuttal process).
2. **Reported facts** — consistent secondary sources, labeled as such (e.g., the MobiSys 2027
   December deadline and March notification from a community aggregator; Test-of-Time and
   Best-Paper selections via SIGMOBILE award pages and author institutions).
3. **待核实 items** — explicitly marked and phrased as questions (e.g., the program chairs,
   the exact rebuttal-window length, whether any revision channel exists this cycle, and
   everything about the 2027 host, chairs, and dates).

A statement of class 2 or 3 presented as class 1 anywhere in the skills is a bug; fix it
against the live pages.

## Maintenance notes

- Every date, cap, and rule here is a **2026-cycle snapshot**. MobiSys reissues its rules per
  edition — reopen the current `sigmobile.org/mobisys/<year>` CFP and the specific
  `mobisys<yy>.hotcrp.com/deadlines` page before deadline-sensitive advice.
- The deadline is a single hard **December** cutoff printed in UTC/AoE; a miss costs a year,
  and the clock convention can move — never reuse a previous cycle's local conversion.
- Page cap, double-blind exceptions, rebuttal scope, and whether a revision path exists can
  change between editions; confirm on the live CFP rather than carrying a rule forward.
- Chairs rotate per edition; confirm the organizing-committee page before naming anyone, and
  treat the 2027 committee as entirely unverified.
- New exemplars must pass the venue-verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md); the mobile-systems
  canon's most famous papers are frequently misfiled across MobiCom, SenSys, OSDI, and NSDI.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

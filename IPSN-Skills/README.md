# IPSN Skills

Twelve agent skills for papers targeting **IPSN — the ACM/IEEE International Conference on
Information Processing in Sensor Networks**, the CPS-IoT Week venue where sensing theory,
on-device/TinyML inference, localization, and networked embedded systems meet. The pack covers the
full arc of an IPSN campaign: deciding whether a project is an **Information Processing (IP)**
contribution or a **Sensor Platforms, Tools and Design Methods (SPOTS)** contribution; building
real-deployment and estimation-theoretic evidence that survives a sensor-systems reviewer's audit;
packaging the double-anonymous HotCRP submission on the ACM template; and — the fact that governs
everything now — routing an IPSN-shaped paper into the venue's **successor**, because IPSN merged
into the reconstituted **SenSys (Embedded AI and Sensing Systems)** from 2025-2026.

Official basis checked on **2026-07-09**: the IPSN 2024 (23rd edition) research call and the
`ipsn.acm.org/2024` pages, the CPS-IoT Week 2024/2025/2026 sites, the SenSys 2025/2026 calls that
absorbed IPSN, the ACM Digital Library and IEEE Xplore IPSN proceedings, and dblp. Direct fetches
of `ipsn.acm.org`, `dl.acm.org`, and `dblp.org` returned 403 in the verification environment, so
official pages were read via search-engine renderings of the exact URLs and cross-checked across
ACM DL, IEEE Xplore, dblp, and the CPS-IoT Week program pages; the full trail, including everything
still marked 待核实, is in [`resources/official-source-map.md`](resources/official-source-map.md).

> **Status warning you must read first.** IPSN ran as a standalone conference through **IPSN 2024**
> (its 23rd edition, Hong Kong, CPS-IoT Week 2024). Starting in 2025, **SenSys, IPSN, and IoTDI
> merged**; from 2026 the merged venue is the **ACM/IEEE International Conference on Embedded
> Artificial Intelligence and Sensing Systems (SenSys)**, held within CPS-IoT Week. There is **no
> standalone "IPSN 2026/2027."** This pack teaches the IPSN *tradition and bar* and routes you to
> where that work is submitted now. Confirm the current successor call before acting.
>
> Name-collision guard: "IPSN" is also the WHO *International Pathogen Surveillance Network* and an
> IEEE *IP-over-Sensor-Network* workshop — neither is this IPSN. No fact here derives from them.

## What makes IPSN different from its siblings

These venue mechanics — verified for the IPSN lineage and its 2025/2026 successor — drive most of
the advice in the skills, and most of the mistakes made by authors arriving from SenSys, MobiSys,
MobiCom, or a pure signal-processing venue:

- **The signature dual track: IP and SPOTS.** IPSN split submissions into the **Information
  Processing (IP) track** — algorithms, estimation, signal processing, inference, learning,
  localization — and the **Sensor Platforms, Tools and Design Methods (SPOTS) track** — hardware,
  embedded software, tools, measurement, and real deployments. Which track you pick reshapes the
  reviewer pool and the evidence bar. No sibling flagship has this split.
- **It lives inside CPS-IoT Week.** IPSN is co-located with **RTAS, HSCC, and ICCPS** (and
  historically IoTDI) under CPS-IoT Week — a real-time-systems, hybrid-systems, and cyber-physical
  neighborhood, not the mobile-computing world of MobiSys/MobiCom or the standalone fall SenSys.
- **Joint ACM/IEEE sponsorship.** IPSN is sponsored by **ACM SIGBED and IEEE**; papers appeared in
  **both the ACM Digital Library and IEEE Xplore** — a two-publisher footprint that shapes rights
  forms and metadata.
- **Sensing theory sits beside systems.** An IPSN paper can be a Cramér-Rao-bound estimator, a
  compressive-sensing result, or a TinyML inference pipeline on a microcontroller — the "information
  processing" in the name is load-bearing, and a purely systems reviewer is not the only audience.
- **Double-blind on the ACM template, ≤12 pages.** IPSN 2024 used **double-blind** review, the
  **ACM Primary Article Template** (two-column, 9 pt), and a **≤12-page** budget inclusive of
  figures, tables, and references — submitted through **HotCRP**, not OpenReview.
- **An artifact and deployment culture with its own prize.** IPSN gave a **Best Paper Award** and a
  **Best Research Artifact Award**; real-world deployments (bridges, buildings, wildlife, factories)
  are a native contribution shape, not an afterthought.
- **The merger is the biggest live fact.** The highest-leverage thing this pack does is stop you
  from chasing a conference that no longer runs and point you at its successor with the IP/SPOTS
  instincts intact.

## Skills

| Skill | What it does |
| --- | --- |
| [`ipsn-topic-selection`](skills/ipsn-topic-selection/SKILL.md) | Decide IP track vs SPOTS track, and route between the IPSN lineage (now SenSys) and CPS-IoT Week neighbors (RTAS/ICCPS/HSCC), MobiSys/MobiCom, INFOCOM, or a signal-processing journal. |
| [`ipsn-workflow`](skills/ipsn-workflow/SKILL.md) | Run the CPS-IoT Week calendar backward from the deadline, through the merger-aware routing, double-blind submission, deployment logistics, artifact award, and camera-ready. |
| [`ipsn-writing-style`](skills/ipsn-writing-style/SKILL.md) | Build the sensing-systems skeleton: a real sensing problem up front, an honest end-to-end system-or-estimator claim, ground-truth methodology, and energy/latency/accuracy budgets. |
| [`ipsn-related-work`](skills/ipsn-related-work/SKILL.md) | Cover the sensor-networks lanes (IPSN/SenSys/MobiCom/MobiSys/INFOCOM + signal-processing venues), write delta-first positioning, and keep self-citation double-blind. |
| [`ipsn-experiments`](skills/ipsn-experiments/SKILL.md) | Match evidence to claim shape: real testbeds and deployments, ground-truth instrumentation, energy/latency measurement, on-device/TinyML profiling, and estimation-theoretic baselines. |
| [`ipsn-reproducibility`](skills/ipsn-reproducibility/SKILL.md) | Build the reproducibility story a hardware/embedded artifact needs: firmware, board files, traces, calibration, and the honest degrees of reproducibility for a physical system. |
| [`ipsn-supplementary`](skills/ipsn-supplementary/SKILL.md) | Split content between the ≤12 reviewed pages and the artifact/appendix by decision-criticality, plus demo/poster and dataset release paths. |
| [`ipsn-submission`](skills/ipsn-submission/SKILL.md) | Final HotCRP audit: IP-vs-SPOTS track choice, the ACM template and 12-page budget, the double-blind sweep for hardware papers, and desk-reject triage — routed to the current successor call. |
| [`ipsn-review-process`](skills/ipsn-review-process/SKILL.md) | Model the pipeline — double-blind, per-track TPCs, rebuttal, Best Research Artifact judging — and how it differs from SenSys's revision model and OpenReview venues. |
| [`ipsn-author-response`](skills/ipsn-author-response/SKILL.md) | Write the double-blind rebuttal that answers the sensor-systems reviewer on ground truth, baselines, deployment realism, and energy accounting without leaking identity. |
| [`ipsn-artifact-evaluation`](skills/ipsn-artifact-evaluation/SKILL.md) | Target the ACM badges and the IPSN Best Research Artifact Award for a hardware-plus-software artifact: firmware, datasets, DOI archives, and evaluator-proof docs. |
| [`ipsn-camera-ready`](skills/ipsn-camera-ready/SKILL.md) | De-anonymize, complete the dual ACM/IEEE metadata (CCS, ORCID, DOI, IEEE PDF eXpress), permanentize dataset links, and pass two-publisher production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Sources with URLs and access dates; verified IPSN-lineage and merger facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces (IPSN archive, CPS-IoT Week, the successor SenSys, ACM DL, IEEE Xplore) plus cross-check sources for when the gateway blocks a direct fetch. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Three archival-verified IPSN papers across IP, SPOTS, and deployment shapes, with self-check questions and a sibling-confusion guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional TinyML-on-a-microcontroller study's abstract and introduction rebuilt to the IPSN arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the IPSN-specific hardware/firmware/deployment checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./IPSN-Skills
claude plugin install ipsn-skills
```

Or use the files directly: each `skills/ipsn-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an IP-track or a SPOTS-track paper — and where does IPSN work go now?" → `ipsn-topic-selection`
- "Audit my draft against the IPSN double-blind ACM-template rules" → `ipsn-submission`
- "Reviews are in — draft the rebuttal on ground truth and energy" → `ipsn-author-response`
- "Get this firmware+dataset artifact ready for the Best Research Artifact Award" → `ipsn-artifact-evaluation`

## Pack structure

```text
IPSN-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── ipsn-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `ipsn-topic-selection`; the IP-vs-SPOTS choice and the merger routing
   are the two decisions that most change your outcome. Skim the exemplars to see what an IP-track
   theory paper, a SPOTS-track platform paper, and a real deployment look like.
2. **While building evidence** — keep `ipsn-experiments` and `ipsn-reproducibility` beside the
   testbed; ground truth, energy traces, and calibration logged at collection time cannot be
   retrofitted.
3. **While writing** — `ipsn-writing-style` for the body against the worked example,
   `ipsn-supplementary` for the body/artifact/dataset split, `ipsn-related-work` for delta-first
   positioning across the sensing lanes.
4. **Deadline weeks** — confirm the successor call's registration cutoff, then `ipsn-submission`
   end to end on the final PDF, the track choice, and the double-blind sweep.
5. **After submission** — `ipsn-review-process` to calibrate, `ipsn-author-response` for the
   rebuttal, then `ipsn-artifact-evaluation` and `ipsn-camera-ready` — or the routing table in
   `ipsn-topic-selection` if the decision goes the other way.

## Lineage and successor anchor facts (historical snapshot, not permanent rules)

- **IPSN 2024** was the **23rd** ACM/IEEE International Conference on Information Processing in
  Sensor Networks: **Hong Kong**, within **CPS-IoT Week 2024** (May 13-16, 2024). Double-blind,
  **ACM Primary Article Template**, **≤12 pages** inclusive, via HotCRP (`ipsn2024.hotcrp.com`).
  Two tracks: **IP** and **SPOTS**. Awards: **Best Paper** and **Best Research Artifact**. This was
  the **last standalone IPSN**.
- **The merger:** SenSys, IPSN, and IoTDI combined; **SenSys 2025** (CPS-IoT Week 2025, Irvine)
  was the first combined event, and from 2026 the venue is **SenSys — ACM/IEEE International
  Conference on Embedded Artificial Intelligence and Sensing Systems**. **SenSys 2026** ran at
  **CPS-IoT Week 2026** (Saint Malo, France, May 11-14, 2026; paper deadline 13 Nov 2025 AoE,
  double-blind). As of 2026-07-09 the live next target for IPSN-lineage work is the following
  SenSys edition (**next exact deadline 待核实**).
- **Publication:** historically ACM DL + IEEE Xplore. In the merged venue, regular technical papers
  publish in the **ACM** proceedings and demos/posters in the **IEEE** proceedings (verify per
  edition).

## Fact discipline

This pack separates three classes of statement, and the skills keep them distinguishable:

1. **Verified lineage/successor facts** — carry dates/budgets and trace to a numbered source in the
   source map (e.g., IPSN 2024's 12-page double-blind ACM format, the IP/SPOTS tracks, the SenSys
   merger and the 13 Nov 2025 SenSys 2026 deadline).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., exact
   organizing rosters, some award histories).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the next successor-edition
   deadline, any IPSN "Test of Time" award, per-track acceptance rates, any generative-AI
   disclosure policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **snapshot**, and IPSN's very existence as a standalone venue
  ended after 2024 — always re-confirm the current successor (SenSys) call before advising.
- IPSN had **no standing editor-in-chief**; leadership rotated per edition as General and per-track
  Program Chairs under CPS-IoT Week, ACM SIGBED, and IEEE.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar sensor-network
  tool name is not proof of an IPSN placement (many live at SenSys, MobiCom, or NSDI).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

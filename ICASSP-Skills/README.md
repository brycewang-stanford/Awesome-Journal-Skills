# ICASSP Skills

Twelve agent skills for papers targeting **ICASSP — the IEEE International Conference on
Acoustics, Speech and Signal Processing**, the flagship conference of the **IEEE Signal
Processing Society (SPS)**. ICASSP is deliberately broad: speech and audio are only one part of a
program that also covers image and video, communications and radar, sensor arrays, estimation and
detection theory, and machine learning for signals. The pack walks the full annual arc — venue
routing, the IEEE 4+1 format, single-blind submission on the CMS portal, the recently added
rebuttal, IEEE Xplore camera-ready, task-matched evaluation, and the conference itself.

Official basis checked on **2026-07-09**: the ICASSP 2026 (Barcelona) paper kit and submission
pages on `cmsworkshops.com` and `2026.ieeeicassp.org`, the ICASSP 2027 (Toronto) call, the IEEE
Signal Processing Society site, and dblp / IEEE Xplore for exemplar verification. Several primary
pages were blocked to direct fetches by the verification environment's gateway (HTTP 403), so they
were read through search-engine renderings of exact URLs and cross-checked against one another and
against dblp; the complete trail, including every item still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes ICASSP unlike its neighbors

These mechanics drive the advice in the skills — and the mistakes made by authors arriving from
double-blind ML venues or from the speech community's own Interspeech:

- **Single-blind, not anonymous.** The submitted PDF **must** carry the author list. The failure
  mode is a *missing* author block, not an identity leak — the opposite of OpenReview and ISCA
  venues.
- **Four pages plus a reference page.** A regular paper is 4 content pages (text, figures, and
  references) with an optional 5th page for references, funding acknowledgements, and the
  Compliance-with-Ethical-Standards statement *only*. There is **no reviewed appendix**; whatever
  decides acceptance lives on the four pages.
- **Submission is on CMS, not CMT.** ICASSP uses Conference Management Services
  (`cmsworkshops.com`) and routes papers by **EDICS** subject category — a genuine SPS fingerprint,
  distinct from the Microsoft CMT that Interspeech uses.
- **A rebuttal now exists.** ICASSP historically had *no* author response; recent cycles added a
  short rebuttal window (2026: reported to ~22 December 2025). Do not assume it recurs — verify.
- **A September clock.** The paper deadline falls in autumn (ICASSP 2026: 17 Sep 2025), months
  offset from Interspeech's February deadline — often the deciding factor for a speech paper.
- **Alternative publication paths.** The **OJSP-ICASSP** track (8+1 pages, open-access publication
  in the IEEE Open Journal of Signal Processing, presented but not in the proceedings) and the
  **SPS-journal presentation** option (present a recently accepted SPS-journal paper, not
  re-reviewed) sit alongside the standard track. Signal Processing **Grand Challenges** run too.
- **Proceedings in IEEE Xplore.** Camera-ready means PDF eXpress validation and the IEEE
  electronic copyright form; presentation is in person, oral or poster, by a registered author.

## The ICASSP-vs-Interspeech routing decision

Because speech is only one ICASSP track, the pack teaches this choice explicitly (see
[`skills/icassp-topic-selection`](skills/icassp-topic-selection/SKILL.md)):

| Dimension | ICASSP (IEEE SPS) | Interspeech (ISCA) |
| --- | --- | --- |
| Scope | All signal processing; speech is one track | Speech and spoken language only |
| Anonymity | Single-blind (author list included) | Double-anonymous with anonymity period |
| Deadline | September | Late February |
| Portal | CMS (`cmsworkshops.com`) | Microsoft CMT |
| Proceedings | IEEE Xplore | ISCA Archive (open access) |

Route a **signal-processing method** whose speech use is one instance to ICASSP; route a
**spoken-language-centric** contribution to Interspeech.

## Skills

| Skill | What it does |
| --- | --- |
| [`icassp-topic-selection`](skills/icassp-topic-selection/SKILL.md) | Find the signal-processing primitive and run the ICASSP-vs-Interspeech (and ICIP/EUSIPCO/WASPAA/SPS-journal/ML) routing decision. |
| [`icassp-workflow`](skills/icassp-workflow/SKILL.md) | Run the annual clock — September deadline, winter rebuttal, spring notification, Xplore camera-ready, May conference — with owners and track choice. |
| [`icassp-writing-style`](skills/icassp-writing-style/SKILL.md) | Lead with the mechanism and a task-matched metric, and compress into the IEEE 4+1 two-column shape with no reviewed appendix. |
| [`icassp-related-work`](skills/icassp-related-work/SKILL.md) | Position across SPS journals, IEEE conferences, siblings, and ML venues, cite normally under single-blind, and dodge venue misattribution. |
| [`icassp-experiments`](skills/icassp-experiments/SKILL.md) | Match the metric to the task law (WER, SI-SDR, EER/minDCF, PSNR/SSIM, BER, RMSE), anchor a strong baseline, and sweep the operating condition. |
| [`icassp-reproducibility`](skills/icassp-reproducibility/SKILL.md) | Ship the scoring ruler, pin dataset versions and front-end settings, and control randomness so the headline number is reconstructable. |
| [`icassp-supplementary`](skills/icassp-supplementary/SKILL.md) | Manage the three shelves — 4 content pages, reference page, optional public release/media — and keep the paper self-contained. |
| [`icassp-artifact-evaluation`](skills/icassp-artifact-evaluation/SKILL.md) | Package code, splits, scorers, checkpoints, and demo media (public from the start under single-blind), even with no artifact badge. |
| [`icassp-submission`](skills/icassp-submission/SKILL.md) | Final CMS audit: 4+1 and PDF eXpress, the single-blind author-block check, EDICS, ethics statement, 9-paper cap, and desk-reject triggers. |
| [`icassp-review-process`](skills/icassp-review-process/SKILL.md) | Model the SPS technical-committee pipeline, EDICS routing, the short rebuttal, oral/poster allocation, and how to decode a decision. |
| [`icassp-author-response`](skills/icassp-author-response/SKILL.md) | Answer subfield-expert reviewers from the four-page record in a short rebuttal window, for the committee decision. |
| [`icassp-camera-ready`](skills/icassp-camera-ready/SKILL.md) | Convert acceptance into a correct IEEE Xplore entry: PDF eXpress, IEEE copyright form, reviewer fixes within the accepted claim, registration. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; the verified 2026 fact base; the ICASSP 2027 gate; the 待核实 list; the gateway access-method note. |
| [`resources/external_tools.md`](resources/external_tools.md) | The CMS portal, IEEE Xplore, the SPS site, and five author-side verification passes with a conflict rule. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Six dblp/IEEE-Xplore-verified ICASSP exemplars (Deep-RNN ASR, LAS, LibriSpeech, Deep Clustering, CNN audio, x-vectors) with self-checks and a misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional array-processing (DOA) first page rewritten from generic-ML draft into the ICASSP mechanism-and-metric shape. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit plus five signal-processing-specific measurement checks. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ICASSP-Skills
claude plugin install icassp-skills
```

Or use the files directly — each `skills/icassp-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to fire. Typical invocations:

- "Is this speech paper ICASSP or Interspeech?" → `icassp-topic-selection`
- "Get my array-processing draft into four IEEE pages" → `icassp-writing-style`
- "Am I reporting the right metric for separation?" → `icassp-experiments`
- "We got accepted — what does IEEE Xplore camera-ready need?" → `icassp-camera-ready`

## Pack structure

```text
ICASSP-Skills/
├── .claude-plugin/                 # plugin.json + marketplace.json (12 skills)
├── README.md                       # this file
├── README.zh-CN.md                 # 中文说明
├── LICENSE                         # MIT
├── assets/cover.svg                # pack cover (waveform + spectrum)
├── skills/
│   └── icassp-<topic>/SKILL.md     # 12 skills, one directory each
└── resources/
    ├── README.md                   # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md              # shared repro-kit adapter
```

## 2026/2027 anchor facts (snapshot, not permanent rules)

- **ICASSP 2026: Barcelona, Spain, 4-8 May 2026** (51st ICASSP), theme "Where Signals Meet
  Intelligence"; paper deadline 17 Sep 2025; rebuttal reported to ~22 Dec 2025.
- **ICASSP 2027: Toronto, Canada, 16-21 May 2027**; full-paper deadline reported **~16 September
  2026 — the next major gate as of 2026-07-09** (待核实 until the 2027 CFP is readable directly).
- Format: 4 content pages + 1 optional reference/acknowledgements/ethics page.
- Review: single-blind on the CMS portal; EDICS routing; no reviewed appendix.
- Publication: IEEE Xplore proceedings; OJSP-ICASSP and SPS-journal-presentation alternatives.

## Fact discipline

Three statement classes are kept distinguishable throughout the pack:

1. **Verified 2026-cycle facts** — traceable to a numbered source in the source map (the 4+1
   format, single-blind policy, CMS portal, 9-paper cap).
2. **Reported facts** — found only in secondary renderings and labeled as such (the rebuttal
   window dates, the ICASSP 2027 September deadline).
3. **待核实 items** — unresolved at check time and phrased as questions, never as facts (exact 2027
   dates, any AI-use policy, whether double-blind or a rebuttal returns in a future cycle).

If a skill states class-2/3 material as class 1, treat it as a bug and repair it against the live
official pages.

## Maintenance notes

- Every date above is a **snapshot**. ICASSP is rebuilt by a new local committee each year; nothing
  carries from Barcelona 2026 to Toronto 2027 automatically — not the dates, not the rebuttal, not
  the portal details.
- The pack was verified through gateway-limited access (renderings, not direct fetches); the first
  maintenance task each cycle is to re-open the primary URLs directly and refresh
  [`resources/official-source-map.md`](resources/official-source-map.md).
- New exemplars must be verified against dblp `conf/icassp/` per the recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — signal-processing landmarks
  are scattered across ICASSP, Interspeech, ICIP, EUSIPCO, and SPS journals, and venue
  misattribution is the characteristic error to guard against.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

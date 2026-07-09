# ACM MM Skills

Twelve agent skills for papers aimed at **ACM MM — the ACM International Conference on
Multimedia**, the flagship annual meeting of **ACM SIGMM** and the field's central venue
for work that treats *more than one medium at once*: vision fused with audio, language,
sensor, and interaction, plus the systems that transport, index, and render that content.
The pack walks the full ACM MM arc — deciding whether a project is genuinely a multimedia
contribution rather than a single-modality computer-vision or NLP result, choosing among
sixteen thematic areas and half a dozen tracks, clearing the April OpenReview deadline
chain, writing an anonymous rebuttal, and landing the paper in the ACM Digital Library
under an ACM sigconf layout.

Official basis checked on **2026-07-09**: the ACM MM 2026 site (`2026.acmmm.org`) Calls &
Dates, Important Dates, Call for Technical Papers, Topics of Interest, Review Process
Guidelines, and the Reproducibility / Open Source / Dataset / Brave New Ideas / Grand
Challenge track calls; the ACM MM 2026 OpenReview groups; the ACM Digital Library
proceedings; dblp's `conf/mm` index; and `sigmm.org` (Test-of-Time award, hosting
invitations). Direct fetches of `2026.acmmm.org` were blocked (HTTP 403) in the
verification environment, so official pages were read through search-engine renderings of
the exact URLs and cross-checked against OpenReview, the ACM DL, dblp, and SIGMM news; the
full trail — including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

**Cycle status (2026-07-09):** ACM MM 2026 (Rio de Janeiro, November 10–14, 2026) is the
*live* cycle. The submission chain closed in April (abstract March 25, paper April 1,
supplement April 8), the anonymous rebuttal window ran in early June, and **author
notification lands right now in early July** — this pack is being written on the seam
between decision and camera-ready. Accepted authors are entering the camera-ready run
(reported August 6); rejected authors are re-routing. MM 2027 is slated for Asia/Oceania
(Hong Kong reported); its CFP and dates were not yet published at check time.

## What makes ACM MM unlike its siblings

Verified 2026-cycle mechanics that drive the advice in these skills:

- **Multimedia, not one modality.** The house test is *cross-modal integration or a
  media-systems contribution* — vision+audio+language+sensor, quality of experience,
  transport/delivery, art and culture. A pure object-detector belongs at CVPR/ICCV; a pure
  language model at ACL; ACM MM wants the seam between them.
- **Sixteen thematic areas, one main track.** Submissions pick a thematic area (Multimodal
  Fusion, Generative and Foundation Models, Search and Recommendation, Engagement/Emotion,
  Art and Culture, Systems, Transport and Delivery, Responsible Multimedia, and more), and
  the area shapes which reviewers see the paper.
- **A short paper by ACM standards.** 6–8 pages of body in the **ACM `sigconf` template**,
  with references allowed up to two additional pages that must contain *only* references.
  Overlength papers are desk-rejected without review.
- **Double-blind with named exceptions.** The main track and most tracks are double-blind;
  the **Reproducibility, Open Source Software, and Dataset** tracks are single-blind by
  design because the artifact *is* the paper and cannot be anonymized.
- **A dedicated track economy.** Beyond the main track: Brave New Ideas (vision papers),
  the Multimedia Grand Challenge, an Open Source Software Competition, a Reproducibility
  track with ACM artifact badging, Interactive Art, Doctoral Symposium, and workshops —
  each with its own call and rules.
- **OpenReview, but not NeurIPS-style openness.** ACM MM 2026 runs on OpenReview with an
  optional anonymous rebuttal; reviews are not made public by default, and the community
  norm is a closed, ACM-badged review rather than an open forum.
- **Publication is ACM, not open-access-by-default.** Accepted papers appear in the **ACM
  Digital Library**; there is no author-facing APC, but ACM's rights/OA options (including
  ACM Open) and the sigconf rights block are settled at camera-ready. No standing
  editor-in-chief — the rotating analogue is the per-edition Program and General Chairs.

## Skills

| Skill | What it does |
| --- | --- |
| [`acmmm-topic-selection`](skills/acmmm-topic-selection/SKILL.md) | Test whether the contribution is genuinely multimedia, pick a thematic area, and route between ACM MM, CVPR/ICCV, ACL, ICMR, MMSys, NeurIPS/ICLR, and TOMM. |
| [`acmmm-workflow`](skills/acmmm-workflow/SKILL.md) | Run the SIGMM calendar from thematic-area scoping through the April OpenReview chain, June rebuttal, July decision, August camera-ready, and November presentation. |
| [`acmmm-writing-style`](skills/acmmm-writing-style/SKILL.md) | Write the multimedia first page: the cross-modal contribution up front, media evidence framed as evidence, and the argument compressed into 6–8 sigconf pages. |
| [`acmmm-related-work`](skills/acmmm-related-work/SKILL.md) | Cover the multimedia literature spread — vision, audio/speech, language, HCI/QoE, systems — handle arXiv concurrency, and verify that cited "ACM MM papers" are ACM MM papers, not ICMR/CVPR. |
| [`acmmm-experiments`](skills/acmmm-experiments/SKILL.md) | Design cross-modal evidence: matched baselines per modality, ablations that isolate the fusion, user studies / QoE where subjective quality is the claim, and honest compute reporting. |
| [`acmmm-reproducibility`](skills/acmmm-reproducibility/SKILL.md) | Prepare for the ACM badging pipeline: environment capture, data/media access, seeds, and the Reproducibility-track path to Artifacts Evaluated / Results Reproduced. |
| [`acmmm-supplementary`](skills/acmmm-supplementary/SKILL.md) | Package the supplement due a week after the paper: video/audio demos, appendices, and anonymized media that render on the reviewer's machine. |
| [`acmmm-artifact-evaluation`](skills/acmmm-artifact-evaluation/SKILL.md) | Build the anonymous review artifact and the public release, and decide between the Open Source Software Competition, the Dataset track, and main-track supplementary evidence. |
| [`acmmm-submission`](skills/acmmm-submission/SKILL.md) | Final OpenReview audit: thematic area, sigconf page budget, anonymity vs. the named single-blind tracks, media/link sweep, dual-submission, desk-reject triage, and last-week sequencing. |
| [`acmmm-review-process`](skills/acmmm-review-process/SKILL.md) | Model the ACM MM pipeline — thematic-area routing, reviewers and ACs, the anonymous rebuttal, meta-review, and the oral/poster and award decision tiers. |
| [`acmmm-author-response`](skills/acmmm-author-response/SKILL.md) | Turn multiple reviews into one anonymous rebuttal that stays inside policy: fix factual errors first, add small confirmatory results, concede calibratedly, no new links. |
| [`acmmm-camera-ready`](skills/acmmm-camera-ready/SKILL.md) | Deliver the ACM version of record: de-anonymization, ACM rights/CCS metadata, sigconf compliance, artifact release, registration, and Rio presentation prep. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | The official ACM MM 2026 sources with access dates, the verified 2026-cycle facts, the access-method disclosure, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces (site, OpenReview groups, ACM DL, dblp, SIGMM) plus the author-side verification passes to run each cycle. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five metadata-verified ACM MM papers across contribution types (Caffe, VLFeat, affective-image classification, adversarial and autoencoder cross-modal retrieval), plus a do-not-misattribute guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional cross-modal paper's first page rebuilt to lead with the multimedia contribution, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit, plus ACM MM-only checks (media rendering, anonymity of demo assets, badging readiness). |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ACM-MM-Skills
claude plugin install acm-mm-skills
```

Or use the files directly: each `skills/acmmm-*/SKILL.md` is a standalone instruction file
whose frontmatter `description` tells an agent when to fire. Typical invocations:

- "Is this an ACM MM paper or should it go to CVPR / ACL?" → `acmmm-topic-selection`
- "Audit my draft against the ACM MM page, sigconf, and anonymity rules" → `acmmm-submission`
- "Reviews are out — plan the anonymous rebuttal" → `acmmm-author-response`
- "What must ship for the Reproducibility badge and camera-ready?" → `acmmm-camera-ready`

## Pack structure

```text
ACM-MM-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover
├── skills/
│   └── acmmm-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md              # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md         # adapter to the shared repro kit
```

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- ACM MM 2026: November 10–14, 2026, Rio de Janeiro, Brazil; the 34th edition; organized
  under ACM SIGMM.
- Deadlines (AoE): abstract March 25, 2026 · paper April 1 · supplement April 8 · rebuttal
  June 4 · author notification early July (the CFP page listed July 7; the Important-Dates
  and Dataset pages listed July 9) · camera-ready reported August 6, 2026.
- Format: 6–8 pages of body in the ACM `sigconf` template, references allowed on up to two
  additional references-only pages; overlength papers desk-rejected; submission via
  OpenReview.
- Tracks: Main (16 thematic areas), Dataset, Brave New Ideas, Multimedia Grand Challenge,
  Open Source Software Competition, Reproducibility (ACM badging), Interactive Art,
  Doctoral Symposium, workshops, tutorials, panels, demos.
- Review: double-blind main track; Reproducibility, Open Source Software, and Dataset
  tracks single-blind; optional anonymous rebuttal.
- Publication: ACM Digital Library; no author-side APC; ACM rights/OA settled at
  camera-ready; no standing editor — Program/General Chairs rotate each edition.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified 2026-cycle facts** — trace to a numbered source in the source map (e.g., the
   Rio dates, the April 1 paper deadline, the 6–8-page sigconf budget, the named
   single-blind tracks).
2. **Reported facts** — consistent secondary sources, labeled as such (e.g., the August 6
   camera-ready date from deadline mirrors, MM 2027's Hong Kong host).
3. **Unverifiable-at-check-time items** — explicitly 待核实 and phrased as questions (e.g.,
   the exact notification date given the July 7 vs. July 9 conflict, supplement size caps,
   the ACM rights/OA form specifics, per-track award structure, and everything about the
   2027 cycle).

If a skill states class-2/3 material as class 1, treat it as a bug and fix it against the
live official pages.

## Maintenance notes

- Every date, cap, and track rule here is a **2026-cycle snapshot**. ACM MM policy is
  rewritten each edition by rotating chairs — reopen `2026.acmmm.org` (then the next-year
  site) for the current cycle before deadline-sensitive advice.
- The thematic-area list, the set of active tracks, and the double-blind exceptions shift
  between years; confirm the current Topics of Interest and each track's own call.
- Reproducibility badging follows ACM's evolving artifact-review terminology; check the
  current Reproducibility-track call and ACM's badge definitions each cycle.
- When adding exemplars, follow the verification recipe at the bottom of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — famous multimedia
  papers frequently belong to ICMR, MMSys, CVPR, or TOMM, not the ACM MM main conference.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。

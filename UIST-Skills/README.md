# UIST Skills

Twelve agent skills for papers targeting **UIST — the ACM Symposium on User Interface
Software and Technology**, the SIGCHI community's home for interface *systems*: novel
interaction techniques, enabling hardware, toolkits and authoring environments, and the
engineering that makes new interactions possible. The pack walks the whole arc of a UIST
cycle — testing whether the artifact really is the contribution, building evaluation that
matches a systems claim, producing the video figure a demo-culture venue expects,
surviving the 5,000-character rebuttal, and landing the ACM TAPS camera-ready with its
accessibility obligations.

Official basis checked on **2026-07-08**: the UIST 2026 home, Call for Participation,
Author Guide, and organizers pages, the ACM Digital Library main and adjunct proceedings
records for UIST 2025, the dblp series index, and UIST awards/archive pages for the
Lasting Impact lineage. Direct automated fetches of `uist.acm.org` returned 403 in the
verification environment, so official pages were read via search-engine renderings of the
exact URLs and cross-checked against the ACM DL, dblp, and SIGCHI; the complete trail —
including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes UIST different from its siblings

- **The artifact is the contribution.** UIST's bar is a working interface system whose
  novelty is a *capability*: something a user can now do that no published system
  enabled. Empirical insight about people, however rigorous, routes to CHI or CSCW; the
  routing test is taught explicitly in `uist-topic-selection`.
- **Demo culture is review culture.** The video figure (≤ 3 minutes, 1080p/4K, MP4/H.264
  in 2026) is formally optional and practically decisive — reviewers watch it to decide
  whether the system is real before they weigh the prose.
- **Hard page limits, PCS mechanics.** 2026 reviewed two-column `acmart` submissions at
  10 pages (standard) or 5 pages (short), excluding references and appendices, with
  over-limit desk rejection — via PCS with an abstract deadline one week before the
  paper deadline.
- **A rebuttal that becomes a contract.** The 5,000-character response is an input to
  the PC decision, and acceptances are conditional on delivering exactly the changes the
  rebuttal describes.
- **One community, two archival containers.** Papers land in the main proceedings;
  Demos and Posters (separate chairs and deadlines) land in the adjunct proceedings —
  a real fallback lane for rejected systems, with a one-adjunct-track-per-work rule.
- **Decade-scale memory.** The Lasting Impact Award retro-honors papers like Sensing
  Techniques for Mobile Interaction (UIST 2000), DiamondTouch (UIST 2001), and SHARK2
  (UIST 2004) — the venue's own statement of what its contribution bar produces.

## Skills

| Skill | What it does |
| --- | --- |
| [`uist-topic-selection`](skills/uist-topic-selection/SKILL.md) | Run the artifact-subtraction test, make the CHI-vs-UIST call on contribution shape, and re-route to CSCW, IMWUT, TEI, ISMAR, IUI, or TOCHI when the system is an instrument rather than the contribution. |
| [`uist-workflow`](skills/uist-workflow/SKILL.md) | Plan backwards from late March: feature freeze, evaluation window, video-production weeks, rebuttal, conditional acceptance, July camera-ready, November conference — with named owners per risk. |
| [`uist-writing-style`](skills/uist-writing-style/SKILL.md) | Write the systems arc — walkthrough before mechanism, implementation prose with measurement conditions, capability claims instead of superlatives — inside the 10/5-page budget. |
| [`uist-related-work`](skills/uist-related-work/SKILL.md) | Position by capability delta across the technique lineage, toolkit ancestry, and commercial practice; verify venue attribution on DL/dblp; handle third-person self-citation. |
| [`uist-experiments`](skills/uist-experiments/SKILL.md) | Match evaluation to claim type (technique, hardware, toolkit, pipeline), characterize the operating envelope with distributions, and avoid the ritual usability study. |
| [`uist-reproducibility`](skills/uist-reproducibility/SKILL.md) | Keep the three ledgers — build (parts, firmware, magic numbers), measurement (protocols per reported figure), study — and write honest availability statements. |
| [`uist-supplementary`](skills/uist-supplementary/SKILL.md) | Script the video figure around claims, hit the 2026 spec, anonymize frames and audio, and decide what else ships in the supplement. |
| [`uist-artifact-evaluation`](skills/uist-artifact-evaluation/SKILL.md) | Package code, toolkits, and hardware design files for the five-minute anonymous skeptic, then re-package for public reuse — in a venue with no badge committee. |
| [`uist-submission`](skills/uist-submission/SKILL.md) | Final PCS audit: abstract-then-paper deadlines, page-limit gate, anonymous acmart options, the overlap-attachment rule, mechanical sweeps, deadline-week sequencing. |
| [`uist-review-process`](skills/uist-review-process/SKILL.md) | Model the pipeline — PC plus externals reviewing paper and video, rebuttal, PC meeting, conditional accept — and pick the adjunct-fallback, repair, or re-route exit after rejection. |
| [`uist-author-response`](skills/uist-author-response/SKILL.md) | Budget 5,000 characters by expected value, answer novelty challenges with capability deltas, and keep a promise ledger that fits the +10% camera-ready allowance. |
| [`uist-camera-ready`](skills/uist-camera-ready/SKILL.md) | Deliver the rebuttal contract, work TAPS/APTARA with alt text on every figure and table, de-anonymize, finalize the video, and start Detroit logistics early. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten official sources with URLs and access dates, verified 2026-cycle facts, the access-method note, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes (track/calendar, format, video, anonymity, camera-ready). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Six DL/dblp-verified UIST papers spanning 2000-2023, four with the Lasting Impact Award, each with a self-check question and a venue-verification recipe. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional electrotactile-glove abstract and introduction rebuilt from motivation-essay shape into the capability → mechanism → evidence arc. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference kit plus the five UIST-specific checks (video spec, hardware reconstruction, measurement protocols) it cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./UIST-Skills
claude plugin install uist-skills
```

Or use the files directly — each `skills/uist-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to fire. Typical invocations:

- "Is this system a UIST paper or should the study version go to CHI?" → `uist-topic-selection`
- "Plan our video figure shoot around the paper's claims" → `uist-supplementary`
- "Reviews are in and the rebuttal window opens Thursday" → `uist-author-response`
- "We're conditionally accepted — what does TAPS need from us?" → `uist-camera-ready`

## Pack structure

```text
UIST-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── uist-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared repro kit
```

## Suggested use

1. **At project conception** — `uist-topic-selection` before any code: if the
   artifact-subtraction test leaves a people-finding, the CHI routing just saved a year.
   Calibrate ambition against the exemplars library.
2. **During the build** — install the `uist-reproducibility` ledgers and the
   `uist-experiments` evidence plan while the system is young; measurement harnesses
   retrofit badly in deadline month.
3. **Writing and filming** — `uist-writing-style` for the body, `uist-related-work` for
   the novelty proof, `uist-supplementary` for the video, with the worked example as the
   before/after reference.
4. **Deadline week** — `uist-submission` on the exact files bound for PCS, abstract
   deadline included.
5. **Review season** — `uist-review-process` to read the reviews, `uist-author-response`
   for the one-week rebuttal, then `uist-camera-ready` or the adjunct-track fallback.

## 2026 anchor facts (historical snapshot, not permanent rules)

- UIST 2026 is the **39th** edition: **Detroit, Michigan, USA (GM Renaissance Center),
  November 2-5, 2026**; the Doctoral Symposium runs in person on November 2.
- Papers timetable: abstracts **March 24**, papers **March 31** (11:59 pm AoE), rebuttal
  **May 28 - June 5** (≤ 5,000 characters), notification **June 27**, camera-ready
  **July 24**.
- Format: two-column `acmart` (`[sigconf,review,anonymous]` for review), **10-page
  standard / 5-page short** body limits excluding references and appendices, desk reject
  if exceeded, +10% growth at camera-ready.
- Video figure: ≤ 3 minutes, 1080p or 4K, MP4/H.264, anonymous, optional but highly
  encouraged.
- Anonymization: third-person self-citation with full references; anonymized copy of
  heavily overlapping prior submissions attached as supplementary material.
- Publication: ACM main proceedings via TAPS with APTARA accessible tagging; alt text
  required for every figure, subfigure, and table. UIST 2025 (38th) was Busan,
  September 28 - October 1, 2025 — proceedings DOI 10.1145/3746059, adjunct 10.1145/3746058.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified 2026-cycle facts** — carry dates/limits and trace to a numbered source in
   the source map (the March 31 deadline, the 10/5-page limits, the video spec).
2. **Reported facts** — found only in secondary sources and labeled as such (e.g.
   Sikuli's Best Student Paper award, sourced from an author CV).
3. **Unverifiable-at-check-time items** — marked 待核实 and phrased as questions (adjunct
   deadlines, registration rules, AI-use policy, PCS file caps, open-access terms).

Any statement presenting class 2 or 3 material as class 1 is a bug; fix it against the
live official pages.

## Maintenance notes

- Every date and limit above is a **2026-edition snapshot**. UIST publishes a fresh CFP
  and Author Guide per edition and has changed its length rules across recent cycles;
  reopen `uist.acm.org/<year>/` before deadline-sensitive advice.
- Chairs rotate annually (the 2026 committee is recorded in the source map); do not
  carry names or track configurations forward.
- The 待核实 list in the source map — adjunct-track deadlines, registration and
  presentation requirements, AI-use policy, open-access terms, file-size caps, 2026
  acceptance statistics — must be resolved against live pages before being stated.
- New exemplars require the DL/dblp verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md); note the main vs
  adjunct proceedings distinction, which sibling packs do not have to worry about.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
